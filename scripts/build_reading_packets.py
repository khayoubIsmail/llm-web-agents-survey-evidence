#!/usr/bin/env python3
"""Build compact, page-cited reading packets from extracted full texts.

Packets are local working material.  They surface the abstract and the pages
containing the method, evaluation/results, limitations, and conclusion so a
reviewer can inspect the whole document efficiently without losing page-level
traceability.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


SECTION_NAMES = {
    "introduction": {"introduction"},
    "method": {"method", "methodology", "approach", "architecture", "framework", "systemoverview", "model", "algorithm"},
    "evaluation_results": {"evaluation", "experimentalsetup", "experiment", "experiments", "result", "results", "empiricalevaluation"},
    "limitations": {"limitation", "limitations", "limitationsandfuturework", "threattovalidity", "threatstovalidity"},
    "conclusion": {"conclusion", "conclusions", "conclusionandfuturework", "discussionandconclusion"},
}


def compact(text: str) -> str:
    text = re.sub(r"(?<=\w)-\n\s*(?=\w)", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clipped_page(page: str, match: re.Match[str] | None, limit: int) -> str:
    start = match.start() if match else 0
    value = compact(page[start : start + limit * 2])
    return value[:limit].rstrip()


def normalized_heading(line: str) -> str:
    line = re.sub(r"^\s*(?:[A-Z]\s+)?\d+(?:\.\d+)*[.)]?\s*", "", line.strip())
    return re.sub(r"[^a-z]", "", line.lower())


def find_heading(page: str, names: set[str]) -> tuple[int, int] | None:
    offset = 0
    for line in page.splitlines(keepends=True):
        value = normalized_heading(line)
        if value in names and len(line.strip()) <= 100:
            return offset, offset + len(line)
        offset += len(line)
    return None


def locate(pages: list[str], names: set[str], limit: int = 2600) -> tuple[int | None, str]:
    for index, page in enumerate(pages):
        heading = find_heading(page, names)
        if heading:
            content = page[heading[0] :]
            if len(compact(content)) < limit // 2 and index + 1 < len(pages):
                content += "\n" + pages[index + 1]
            return index + 1, compact(content)[:limit].rstrip()
    return None, ""


def abstract(pages: list[str], limit: int = 2600) -> tuple[int | None, str]:
    for index, page in enumerate(pages[:4]):
        heading = find_heading(page, {"abstract"})
        if not heading:
            continue
        content = page[heading[1] :]
        end = find_heading(content, {"introduction"})
        if end:
            content = content[: end[0]]
        return index + 1, compact(content)[:limit].rstrip()
    return (1, compact(pages[0])[:limit].rstrip()) if pages else (None, "")


def evidence_lines(pages: list[str], limit: int = 14) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    cue = re.compile(
        r"(?i)\b(?:outperform|improv|increase|decrease|achiev|accuracy|success rate|pass@|f1|win rate|ablation|significant)\w*\b"
    )
    number = re.compile(r"(?:\b\d+(?:\.\d+)?\s*%|\b\d+\.\d+\b)")
    for page_no, page in enumerate(pages, start=1):
        for raw in re.split(r"(?<=[.!?])\s+|\n", compact(page)):
            line = raw.strip()
            if 45 <= len(line) <= 420 and cue.search(line) and number.search(line):
                result.append((page_no, line))
                if len(result) >= limit:
                    return result
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--text-cache", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--qualities", default="C,Missing")
    args = parser.parse_args()

    allowed = {value.strip() for value in args.qualities.split(",")}
    with args.register.open(encoding="utf-8-sig", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["note_quality"] in allowed]
    args.output.mkdir(parents=True, exist_ok=True)

    built = 0
    for row in rows:
        record_id = int(row["record_id"])
        text_path = args.text_cache / f"{record_id:04d}.txt"
        if not text_path.exists() or not text_path.stat().st_size:
            continue
        pages = text_path.read_text(encoding="utf-8", errors="replace").split("\f")
        if pages and not pages[-1].strip():
            pages.pop()
        sections = {"abstract": abstract(pages)}
        sections.update({name: locate(pages, names) for name, names in SECTION_NAMES.items()})
        lines = [
            f"# Reading packet — record {record_id}",
            "",
            f"- Title: {row['title']}",
            f"- Section / priority: {row['section']} / {row['priority']}",
            f"- Register note quality: {row['note_quality']}",
            f"- Register identifier: {row['identifier'] or 'not recorded'}",
            f"- Extracted pages: {len(pages)}",
            "",
        ]
        for name, (page_no, content) in sections.items():
            lines.extend([f"## {name.replace('_', ' ').title()}", ""])
            if content:
                lines.extend([f"Source location: PDF p. {page_no}", "", content, ""])
            else:
                lines.extend(["No reliably detected heading; inspect the complete text.", ""])
        lines.extend(["## Quantitative evidence candidates", ""])
        candidates = evidence_lines(pages)
        if candidates:
            lines.extend(f"- PDF p. {page_no}: {line}" for page_no, line in candidates)
        else:
            lines.append("- No quantitative result sentence detected automatically.")
        lines.extend(["", "## Full-text coverage check", ""])
        lines.extend(
            f"- PDF p. {page_no}: {compact(page)[:220]}"
            for page_no, page in enumerate(pages, start=1)
            if page.strip()
        )
        (args.output / f"{record_id:04d}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        built += 1
    print(f"requested={len(rows)}")
    print(f"built={built}")
    print(f"missing_full_text={len(rows) - built}")


if __name__ == "__main__":
    main()
