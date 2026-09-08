#!/usr/bin/env python3
"""Extract paper-specific note segments and assess structured-note coverage.

This is an audit aid, not a substitute for scholarly judgment.  It reports the
presence of expected note dimensions and preserves the exact source segment for
manual comparison against the full text.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from build_note_audit import score


DIMENSIONS = {
    "problem_or_question": r"\b(core idea|problem|research question|objective|aim|motivation)\b",
    "method": r"\b(method|approach|architecture|framework|pipeline|training)\b",
    "evaluation": r"\b(evaluation|experiment|benchmark|dataset|baseline|metric)\b",
    "results": r"\b(result|finding|performance|improv|outperform|achiev)\w*\b",
    "contribution": r"\b(contribution|novel|introduc|propos)\w*\b",
    "limitations": r"\b(limitations?|weakness|threats? to validity|caution|failure)\b",
    "survey_relevance": r"\b(relevance|use in thesis|how to use|connects? to|survey)\b",
    "evidence_location": r"\b(page|pp\.|section|table|figure|appendix)\s*[A-Z]?\d",
}


def extract_segment(path: Path, title: str, source_kind: str) -> tuple[str, str, float]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if source_kind == "individual":
        return text.strip(), "whole file", 1.0
    lines = text.splitlines()
    headings: list[tuple[int, int, str, float]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        value = match.group(2).strip()
        headings.append((index, len(match.group(1)), value, score(title, value)))
    if not headings:
        return text.strip(), "whole file; no headings", 0.0
    # Merged archives sometimes contain a table-of-contents heading immediately
    # followed by the real paper heading.  Both can be exact title matches, so a
    # score-only maximum can select a three-word stub.  Among near-equivalent
    # title matches, prefer the candidate with substantive section content.
    candidates: list[tuple[float, int, int, int, str, str]] = []
    for start, level, heading, match_score in headings:
        end = len(lines)
        for index, next_level, _value, _score in headings:
            if index > start and next_level <= level:
                end = index
                break
        value = "\n".join(lines[start:end]).strip()
        words = word_count(value)
        candidates.append((match_score, min(words, 500), start, level, heading, value))
    best_title_score = max(item[0] for item in candidates)
    eligible = [item for item in candidates if item[0] >= best_title_score - 0.02]
    match_score, _words, start, level, heading, segment = max(
        eligible, key=lambda item: (item[1], -item[2])
    )
    return segment, f"heading: {heading}", match_score


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--match-audit", type=Path, required=True)
    parser.add_argument("--notes-root", type=Path, required=True)
    parser.add_argument("--segments", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    with args.match_audit.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    args.segments.mkdir(parents=True, exist_ok=True)
    output_rows = []
    for row in rows:
        record_id = int(row["record_id"])
        matched = float(row["best_match_score"]) >= 0.73 and bool(row["best_source_path"])
        segment = ""
        selector = ""
        section_score = 0.0
        if matched:
            path = args.notes_root / row["best_source_path"]
            segment, selector, section_score = extract_segment(
                path, row["title"], row["best_source_kind"]
            )
            (args.segments / f"{record_id:04d}.md").write_text(segment + "\n", encoding="utf-8")
        found = {
            name: bool(re.search(pattern, segment, flags=re.I))
            for name, pattern in DIMENSIONS.items()
        }
        dimensions_present = sum(found.values())
        words = word_count(segment)
        if not matched or words < 100:
            computed = "Missing"
        elif words >= 650 and dimensions_present >= 7:
            computed = "A"
        elif words >= 350 and dimensions_present >= 5:
            computed = "B"
        else:
            computed = "C"
        output = {
            "record_id": record_id,
            "section": row["section"],
            "priority": row["priority"],
            "title": row["title"],
            "register_note_quality": row["register_note_quality"],
            "matched": "yes" if matched else "no",
            "match_score": row["best_match_score"],
            "source_kind": row["best_source_kind"],
            "source_path": row["best_source_path"],
            "segment_selector": selector,
            "segment_heading_score": f"{section_score:.3f}",
            "word_count": words,
            **{name: "yes" if present else "no" for name, present in found.items()},
            "dimensions_present": dimensions_present,
            "computed_note_quality": computed,
        }
        output_rows.append(output)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=output_rows[0].keys(), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"records={len(output_rows)}")
    for value in ("A", "B", "C", "Missing"):
        print(f"computed_{value}={sum(row['computed_note_quality'] == value for row in output_rows)}")


if __name__ == "__main__":
    main()
