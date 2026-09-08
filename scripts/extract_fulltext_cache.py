#!/usr/bin/env python3
"""Extract page-preserving text from the local full-text PDF audit cache.

The PDFs and extracted text remain outside version control.  A small JSONL
manifest records extraction success, page counts, hashes, and first-page title
similarity so that later note reviews can be traced to a specific document.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def title_similarity(title: str, first_pages: str) -> float:
    expected = normalize(title)
    observed = normalize(first_pages[:12_000])
    if not expected or not observed:
        return 0.0
    if expected in observed:
        return 1.0
    words = expected.split()
    window = max(len(words) + 4, 10)
    candidates = observed.split()
    best = 0.0
    for start in range(0, min(len(candidates), 450)):
        sample = " ".join(candidates[start : start + window])
        best = max(best, SequenceMatcher(None, expected, sample).ratio())
    return best


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--pdf-cache", type=Path, required=True)
    parser.add_argument("--text-cache", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()

    with args.register.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_id = {int(row["record_id"]): row for row in rows}
    args.text_cache.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)

    results = []
    for pdf_path in sorted(args.pdf_cache.glob("*.pdf")):
        try:
            record_id = int(pdf_path.stem)
        except ValueError:
            continue
        row = by_id.get(record_id)
        if row is None:
            continue
        text_path = args.text_cache / f"{record_id:04d}.txt"
        process = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), str(text_path)],
            capture_output=True,
            text=True,
        )
        text = text_path.read_text(encoding="utf-8", errors="replace") if text_path.exists() else ""
        page_texts = text.split("\f") if text else []
        if page_texts and not page_texts[-1].strip():
            page_texts.pop()
        pages = len(page_texts)
        first_pages = "\f".join(page_texts[:2])
        results.append(
            {
                "record_id": record_id,
                "title": row["title"],
                "priority": row["priority"],
                "register_note_quality": row["note_quality"],
                "pdf_file": pdf_path.name,
                "pdf_sha256": sha256(pdf_path),
                "pdf_bytes": pdf_path.stat().st_size,
                "extracted_pages": pages,
                "extracted_characters": len(text),
                "title_similarity": round(title_similarity(row["title"], first_pages), 3),
                "status": "extracted" if process.returncode == 0 and text.strip() else "failed",
                "extractor_message": process.stderr.strip(),
            }
        )

    with args.manifest.open("w", encoding="utf-8") as handle:
        for result in sorted(results, key=lambda item: item["record_id"]):
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")
    print(f"pdfs={len(results)}")
    print(f"extracted={sum(item['status'] == 'extracted' for item in results)}")
    print(f"title_similarity_below_0.75={sum(item['title_similarity'] < 0.75 for item in results)}")


if __name__ == "__main__":
    main()
