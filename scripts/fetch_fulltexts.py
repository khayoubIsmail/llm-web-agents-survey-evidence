#!/usr/bin/env python3
"""Fetch legally accessible full-text PDFs for register entries.

PDFs are stored in a local audit cache and are never added to the repository.
Only direct open-access locations derived from canonical identifiers or resolved
metadata are attempted.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def identifier_candidates(identifier: str) -> list[str]:
    value = identifier.strip()
    low = value.lower()
    result: list[str] = []

    arxiv = re.search(r"(?:arxiv(?::|\.org/(?:abs|pdf)/)?\s*)(\d{4}\.\d{4,5})(?:v\d+)?", value, re.I)
    if arxiv:
        result.append(f"https://arxiv.org/pdf/{arxiv.group(1)}")

    openreview = re.search(r"openreview\.net/(?:forum|pdf)\?id=([^&#]+)", value, re.I)
    if openreview:
        result.append(f"https://openreview.net/pdf?id={openreview.group(1)}")

    acl_doi = re.search(r"10\.18653/v1/([^\s/?#]+)", value, re.I)
    if acl_doi:
        result.append(f"https://aclanthology.org/{acl_doi.group(1) }.pdf")

    acl_url = re.search(r"https?://aclanthology\.org/([^/?#]+)/?", value, re.I)
    if acl_url:
        result.append(f"https://aclanthology.org/{acl_url.group(1)}.pdf")

    pmlr = re.search(r"https?://proceedings\.mlr\.press/(v\d+)/([^/?#]+)\.html", value, re.I)
    if pmlr:
        result.append(
            f"https://raw.githubusercontent.com/mlresearch/{pmlr.group(1)}/main/"
            f"assets/{pmlr.group(2)}/{pmlr.group(2)}.pdf"
        )

    if "proceedings.neurips.cc" in low and "-abstract-" in low:
        pdf = re.sub(r"-Abstract-([^./]+)\.html(?:\?.*)?$", r"-Paper-\1.pdf", value, flags=re.I)
        result.append(pdf.replace("/hash/", "/file/"))
    springer_doi = re.search(r"(10\.1007/[^\s?#]+)", value, re.I)
    if springer_doi:
        result.append(f"https://link.springer.com/content/pdf/{springer_doi.group(1).rstrip('/')}.pdf")
    if low.endswith(".pdf"):
        result.append(value)
    return list(dict.fromkeys(result))


def load_resolved(path: Path | None) -> dict[int, list[str]]:
    result: dict[int, list[str]] = {}
    if path is None or not path.exists():
        return result
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        urls = []
        for key in ("best_oa_location", "primary_location"):
            location = item.get(key) or {}
            if location.get("pdf_url"):
                urls.append(location["pdf_url"])
        for location in item.get("locations") or []:
            if location.get("pdf_url"):
                urls.append(location["pdf_url"])
            landing = location.get("landing_page_url")
            if landing and landing.lower().endswith(".pdf"):
                urls.append(landing)
        result[int(item["record_id"])] = list(dict.fromkeys(urls))
    return result


def load_semantic_scholar(path: Path | None) -> dict[int, list[str]]:
    result: dict[int, list[str]] = {}
    if path is None or not path.exists():
        return result
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        record_id = int(item["record_id"])
        paper = item.get("result") or {}
        urls = []
        arxiv_id = (paper.get("externalIds") or {}).get("ArXiv")
        if arxiv_id:
            urls.append(f"https://arxiv.org/pdf/{arxiv_id}")
        acl_id = (paper.get("externalIds") or {}).get("ACL")
        if acl_id:
            urls.append(f"https://aclanthology.org/{acl_id}.pdf")
        oa_url = (paper.get("openAccessPdf") or {}).get("url")
        if oa_url:
            urls.append(oa_url)
        result[record_id] = list(dict.fromkeys(urls))
    return result


def fetch_pdf(url: str, destination: Path) -> tuple[bool, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 evidence-register-audit/1.0",
            "Accept": "application/pdf,text/html;q=0.8,*/*;q=0.5",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=50) as response:
            data = response.read(80 * 1024 * 1024)
            final_url = response.geturl()
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        return False, f"{type(exc).__name__}: {exc}"
    if not data.startswith(b"%PDF-"):
        return False, f"not_pdf final_url={final_url} bytes={len(data)}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    return True, final_url


def pdf_pages(path: Path) -> int | None:
    try:
        output = subprocess.check_output(["pdfinfo", str(path)], text=True, stderr=subprocess.DEVNULL)
        match = re.search(r"^Pages:\s+(\d+)", output, re.M)
        return int(match.group(1)) if match else None
    except (OSError, subprocess.SubprocessError):
        return None


def fetch_record(row: dict, cache: Path, resolved_urls: list[str]) -> dict:
    record_id = int(row["record_id"])
    destination = cache / f"{record_id:04d}.pdf"
    if destination.exists() and destination.read_bytes()[:5] == b"%PDF-":
        return {
            "record_id": record_id,
            "title": row["title"],
            "status": "cached",
            "pdf_path": str(destination),
            "pages": pdf_pages(destination),
            "bytes": destination.stat().st_size,
        }
    candidates = identifier_candidates(row["identifier"]) + resolved_urls
    candidates = list(dict.fromkeys(url for url in candidates if url))
    attempts = []
    for url in candidates:
        ok, detail = fetch_pdf(url, destination)
        attempts.append({"url": url, "result": detail})
        if ok:
            return {
                "record_id": record_id,
                "title": row["title"],
                "status": "downloaded",
                "source_url": detail,
                "pdf_path": str(destination),
                "pages": pdf_pages(destination),
                "bytes": destination.stat().st_size,
                "attempts": attempts,
            }
    return {
        "record_id": record_id,
        "title": row["title"],
        "status": "not_retrieved",
        "attempts": attempts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--resolved-metadata", type=Path)
    parser.add_argument("--semantic-scholar-metadata", type=Path)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--qualities", help="Comma-separated note_quality values; default all")
    args = parser.parse_args()

    with args.register.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if args.qualities:
        allowed = {value.strip() for value in args.qualities.split(",")}
        rows = [row for row in rows if row["note_quality"] in allowed]

    resolved = load_resolved(args.resolved_metadata)
    semantic_scholar = load_semantic_scholar(args.semantic_scholar_metadata)
    existing = {}
    if args.log.exists():
        for line in args.log.read_text(encoding="utf-8").splitlines():
            if line.strip():
                item = json.loads(line)
                existing[int(item["record_id"])] = item
    pending = [row for row in rows if int(row["record_id"]) not in existing]
    args.log.parent.mkdir(parents=True, exist_ok=True)
    completed = len(existing)
    with args.log.open("a", encoding="utf-8") as handle:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(
                    fetch_record,
                    row,
                    args.cache,
                    resolved.get(int(row["record_id"]), [])
                    + semantic_scholar.get(int(row["record_id"]), []),
                ): row
                for row in pending
            }
            for future in as_completed(futures):
                item = future.result()
                handle.write(json.dumps(item, ensure_ascii=False) + "\n")
                handle.flush()
                completed += 1
                if completed % 20 == 0 or completed == len(rows):
                    print(f"processed={completed}/{len(rows)}", flush=True)
                time.sleep(0.03)


if __name__ == "__main__":
    main()
