#!/usr/bin/env python3
"""Match the canonical 403-study register to an external tree of Markdown notes.

The source notes are intentionally external to the repository.  This script creates
an auditable inventory only; it does not copy third-party full text.
"""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path


STOP = {
    "a", "an", "and", "as", "at", "by", "for", "from", "in", "into", "is",
    "of", "on", "or", "the", "to", "toward", "towards", "via", "with",
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().replace("&", " and ")
    text = re.sub(r"\barxiv\s*:\s*\d{4}\.\d+(?:v\d+)?\b", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def tokens(text: str) -> set[str]:
    return {t for t in normalize(text).split() if t not in STOP and len(t) > 1}


def clean_candidate(text: str) -> str:
    text = re.sub(r"^#+\s*", "", text).strip()
    text = re.sub(r"^\d+(?:\.\d+)*[.)]?\s*", "", text)
    text = re.sub(r"^S\d+(?:[._]\d+)?[_ -]+P[0-4](?:[_ -]+\d+)?[_ -]+", "", text, flags=re.I)
    text = re.sub(r"^\d{4}(?:-\d{2})?\s*[-_:]\s*", "", text)
    return text.strip(" _-")


def candidate_strings(path: Path, notes_root: Path) -> list[str]:
    result = [clean_candidate(path.stem.replace("_", " "))]
    try:
        with path.open(encoding="utf-8", errors="ignore") as handle:
            for line_no, line in enumerate(handle):
                if line_no > 10000:
                    break
                if re.match(r"^#{1,4}\s+", line):
                    value = clean_candidate(line)
                    if 3 <= len(value.split()) <= 35:
                        result.append(value)
    except OSError:
        pass
    # Stable de-duplication.
    return list(dict.fromkeys(v for v in result if len(v) >= 8))


def score(title: str, candidate: str) -> float:
    nt, nc = normalize(title), normalize(candidate)
    if not nt or not nc:
        return 0.0
    tt, tc = tokens(title), tokens(candidate)
    overlap = len(tt & tc) / max(1, len(tt | tc))
    containment = len(tt & tc) / max(1, len(tt))
    sequence = SequenceMatcher(None, nt, nc).ratio()
    exact_bonus = 0.15 if nt == nc else (0.08 if nt in nc or nc in nt else 0.0)
    return min(1.0, 0.48 * containment + 0.27 * overlap + 0.25 * sequence + exact_bonus)


def source_kind(path: Path) -> str:
    low = path.name.lower()
    if "merged" in low or "global" in low:
        return "merged"
    if "index" in low or "readme" in low or "report" in low or "synthesis" in low:
        return "index_or_report"
    return "individual"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--notes-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--overrides", type=Path)
    args = parser.parse_args()

    note_paths = sorted(args.notes_root.rglob("*.md"))
    candidates: list[tuple[str, Path]] = []
    inverted: dict[str, set[int]] = defaultdict(set)
    for path in note_paths:
        for text in candidate_strings(path, args.notes_root):
            idx = len(candidates)
            candidates.append((text, path))
            for token in tokens(text):
                inverted[token].add(idx)

    with args.register.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    overrides: dict[int, str] = {}
    if args.overrides and args.overrides.exists():
        with args.overrides.open(encoding="utf-8-sig", newline="") as handle:
            overrides = {
                int(item["record_id"]): item["source_path"]
                for item in csv.DictReader(handle)
                if item.get("source_path")
            }

    output_rows = []
    for row in rows:
        title = row["title"]
        title_tokens = tokens(title)
        candidate_hits: Counter[int] = Counter()
        for token in title_tokens:
            candidate_hits.update(inverted.get(token, ()))
        minimum_hits = 2 if len(title_tokens) >= 3 else 1
        candidate_ids = [idx for idx, hits in candidate_hits.items() if hits >= minimum_hits]
        ranked = sorted(
            ((score(title, candidates[i][0]), candidates[i][0], candidates[i][1]) for i in candidate_ids),
            reverse=True,
            key=lambda item: item[0],
        )
        best = ranked[0] if ranked else (0.0, "", None)
        override_path = overrides.get(int(row["record_id"]))
        if override_path:
            path = args.notes_root / override_path
            if not path.is_file():
                raise FileNotFoundError(f"note override does not exist: {path}")
            best = (1.0, title, path)
            ranked = [best, *ranked]
        strong_paths = []
        for match_score, _candidate, path in ranked:
            if match_score < 0.73:
                break
            value = str(path.relative_to(args.notes_root))
            if value not in strong_paths:
                strong_paths.append(value)
        output_rows.append({
            "record_id": row["record_id"],
            "section": row["section"],
            "priority": row["priority"],
            "title": title,
            "register_note_quality": row["note_quality"],
            "register_evidence_readiness": row["evidence_readiness"],
            "best_match_score": f"{best[0]:.3f}",
            "best_match_candidate": best[1],
            "best_source_kind": source_kind(best[2]) if best[2] is not None else "none",
            "best_source_path": str(best[2].relative_to(args.notes_root)) if best[2] is not None else "",
            "matched_source_count": len(strong_paths),
            "matched_source_paths": " | ".join(strong_paths),
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=output_rows[0].keys(), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(output_rows)

    matched = sum(float(row["best_match_score"]) >= 0.73 for row in output_rows)
    print(f"register_rows={len(output_rows)}")
    print(f"markdown_files={len(note_paths)}")
    print(f"title_candidates={len(candidates)}")
    print(f"matched_at_0.73={matched}")
    print(f"unmatched_at_0.73={len(output_rows)-matched}")


if __name__ == "__main__":
    main()
