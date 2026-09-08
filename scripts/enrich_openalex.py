#!/usr/bin/env python3
"""Resolve canonical register titles against OpenAlex and record OA full-text links."""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value.lower()).split())


def similarity(left: str, right: str) -> float:
    a, b = norm(left), norm(right)
    sa, sb = set(a.split()), set(b.split())
    token_f1 = 2 * len(sa & sb) / max(1, len(sa) + len(sb))
    return 0.55 * SequenceMatcher(None, a, b).ratio() + 0.45 * token_f1


def fetch_json(url: str, attempts: int = 5) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "evidence-register-audit/1.0"})
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                return json.load(response)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def compact_location(location: dict | None) -> dict:
    location = location or {}
    source = location.get("source") or {}
    return {
        "landing_page_url": location.get("landing_page_url"),
        "pdf_url": location.get("pdf_url"),
        "source": source.get("display_name"),
        "version": location.get("version"),
        "is_oa": location.get("is_oa"),
    }


def resolve_row(row: dict) -> dict:
    record_id = row["record_id"]
    params = urllib.parse.urlencode({"search": row["title"], "per-page": 5})
    url = f"https://api.openalex.org/works?{params}"
    try:
        payload = fetch_json(url)
        ranked = sorted(
            ((similarity(row["title"], item.get("title") or ""), item)
             for item in payload.get("results", [])),
            key=lambda pair: pair[0],
            reverse=True,
        )
        match_score, match = ranked[0] if ranked else (0.0, {})
        locations = [compact_location(value) for value in match.get("locations", [])]
        seen = set()
        unique_locations = []
        for loc in locations:
            key = (loc.get("landing_page_url"), loc.get("pdf_url"))
            if key not in seen:
                seen.add(key)
                unique_locations.append(loc)
        return {
            "record_id": int(record_id),
            "register_title": row["title"],
            "register_identifier": row["identifier"],
            "match_score": round(match_score, 4),
            "openalex_id": match.get("id"),
            "matched_title": match.get("title"),
            "doi": match.get("doi"),
            "publication_year": match.get("publication_year"),
            "type": match.get("type"),
            "open_access": match.get("open_access"),
            "best_oa_location": compact_location(match.get("best_oa_location")),
            "primary_location": compact_location(match.get("primary_location")),
            "locations": unique_locations,
            "retrieval_status": "matched" if match_score >= 0.82 else "needs_manual_check",
        }
    except Exception as exc:
        return {
            "record_id": int(record_id),
            "register_title": row["title"],
            "register_identifier": row["identifier"],
            "match_score": 0.0,
            "retrieval_status": "request_failed",
            "error": f"{type(exc).__name__}: {exc}",
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--sleep", type=float, default=0.12)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    with args.register.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    existing: dict[str, dict] = {}
    if args.output.exists():
        for line in args.output.read_text(encoding="utf-8").splitlines():
            if line.strip():
                item = json.loads(line)
                existing[str(item["record_id"])] = item

    args.output.parent.mkdir(parents=True, exist_ok=True)
    completed = len(existing)
    pending = [row for row in rows if row["record_id"] not in existing]
    with args.output.open("a", encoding="utf-8") as handle:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(resolve_row, row): row for row in pending}
            for future in as_completed(futures):
                item = future.result()
                handle.write(json.dumps(item, ensure_ascii=False) + "\n")
                handle.flush()
                completed += 1
                if completed % 25 == 0 or completed == len(rows):
                    print(f"resolved={completed}/{len(rows)}", flush=True)
                time.sleep(args.sleep)


if __name__ == "__main__":
    main()
