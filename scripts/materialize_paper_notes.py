#!/usr/bin/env python3
"""Materialize one auditable Markdown note for every record in the 403-paper register.

The script combines paper-specific segments recovered from the original review
archive with manually remediated notes.  It records provenance and current-cycle
full-text verification without copying or committing third-party PDFs.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


MARKER = "<!-- normalized-paper-note -->"
BODY_MARKER = "<!-- note-body-start -->"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_manifest(path: Path) -> dict[int, dict]:
    result: dict[int, dict] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                result[int(row["record_id"])] = row
    return result


def existing_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace").strip()
    if BODY_MARKER in text:
        text = text.split(BODY_MARKER, 1)[1].strip()
    return text


def normalize_heading_depth(text: str) -> str:
    """Nest an archived note under the generated Analysis heading."""
    lines = text.splitlines()
    in_fence = False
    levels: list[int] = []
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"^#{1,6}\s+", line):
            levels.append(len(line) - len(line.lstrip("#")))
    if not levels:
        return text
    offset = max(0, 3 - min(levels))
    output: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            output.append(line)
            continue
        match = None if in_fence else re.match(r"^(#{1,6})(\s+.*)$", line)
        if match:
            level = min(6, len(match.group(1)) + offset)
            line = "#" * level + match.group(2)
        output.append(line)
    return "\n".join(output).strip()


def review_standard(priority: str) -> str:
    if priority in {"P0", "P1"}:
        return "Deep critical analysis and detailed notes"
    return "Complete structured reading focused on relevance, method, results, contributions, and limitations"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--coverage-audit", type=Path, required=True)
    parser.add_argument("--segments", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--notes", type=Path, required=True)
    parser.add_argument("--audit-output", type=Path, required=True)
    parser.add_argument("--remediation-output", type=Path, required=True)
    args = parser.parse_args()

    register = read_csv(args.register)
    coverage = {int(row["record_id"]): row for row in read_csv(args.coverage_audit)}
    manifest = load_manifest(args.manifest)
    args.notes.mkdir(parents=True, exist_ok=True)

    if args.remediation_output.exists():
        remediation_ids = {
            int(row["record_id"]) for row in read_csv(args.remediation_output)
        }
    else:
        remediation_ids = {
            int(path.stem) for path in args.notes.glob("[0-9][0-9][0-9][0-9].md")
        }

    expected_ids = {int(row["record_id"]) for row in register}
    if not remediation_ids <= expected_ids:
        raise SystemExit("Remediation directory contains IDs outside the register")

    audit_rows: list[dict[str, str | int | float]] = []
    remediation_rows: list[dict[str, str | int]] = []
    for row in register:
        record_id = int(row["record_id"])
        note_path = args.notes / f"{record_id:04d}.md"
        coverage_row = coverage[record_id]
        segment_path = args.segments / f"{record_id:04d}.md"

        if record_id in remediation_ids:
            if not note_path.exists():
                raise SystemExit(f"Missing remediated note for record {record_id}")
            body = existing_body(note_path)
            content_provenance = "current-cycle full-text remediation"
            if record_id == 249:
                content_provenance = "current-cycle access-exception note"
            remediation_reason = (
                "No reliable paper-specific note matched the register title"
                if coverage_row["matched"] == "no"
                else "Selected for deeper priority-adjusted remediation after manual review"
            )
            if record_id == 249:
                remediation_reason = "Full text remained unavailable after publisher and exact-title searches"
            remediation_rows.append(
                {
                    "record_id": record_id,
                    "title": row["title"],
                    "priority": row["priority"],
                    "initial_note_quality": row["note_quality"],
                    "audit_computed_quality": coverage_row["computed_note_quality"],
                    "reason": remediation_reason,
                    "action": "Created or replaced with structured note",
                }
            )
        else:
            if not segment_path.exists():
                raise SystemExit(f"No archived segment or remediation for record {record_id}")
            body = segment_path.read_text(encoding="utf-8", errors="replace").strip()
            content_provenance = "existing paper-specific note preserved after title and coverage audit"

        pdf = manifest.get(record_id)
        if record_id == 249:
            full_text_status = "blocked: full text unavailable"
            full_text_basis = "Publisher/metadata checks only; not used for claim-level synthesis"
            claim_status = "blocked pending full text"
        elif pdf and pdf.get("status") == "extracted":
            full_text_status = "current-cycle full text extracted and title-checked"
            qualifier = ""
            if record_id == 491:
                qualifier = "; title changed from HEAP to SteP between versions"
            full_text_basis = (
                f"{pdf['extracted_pages']} extracted PDF pages; SHA-256 {pdf['pdf_sha256']}"
                f"; title similarity {pdf['title_similarity']}{qualifier}"
            )
            claim_status = "paper-specific note ready for synthesis"
        else:
            full_text_status = "existing review archive audited; no current-cycle PDF verification"
            full_text_basis = (
                "Paper-specific substantive note retained from the supplied review archive; "
                "the repository does not store third-party PDFs"
            )
            claim_status = "paper-specific note retained for synthesis"

        source = (
            coverage_row["source_path"]
            if coverage_row["matched"] == "yes"
            else "no reliable paper-specific source note"
        )
        lines = [
            MARKER,
            f"# {row['title']}",
            "",
            "## Audit metadata",
            "",
            f"- Record ID: {record_id}",
            f"- Section / priority: {row['section']} / {row['priority']}",
            f"- Year / venue: {row['year']} / {row['venue']}",
            f"- Publication status: {row['publication_status']} ({row['status_category']})",
            f"- Identifier: {row['identifier'] or 'not recorded'}",
            f"- Initial register note quality: {row['note_quality']}",
            f"- Audit-computed source-note quality: {coverage_row['computed_note_quality']}",
            f"- Required review standard: {review_standard(row['priority'])}",
            f"- Content provenance: {content_provenance}",
            f"- Original note source: {source}",
            f"- Full-text status: {full_text_status}",
            f"- Full-text basis: {full_text_basis}",
            f"- Claim-use status: {claim_status}",
            "",
            "## Analysis",
            "",
            BODY_MARKER,
            normalize_heading_depth(body),
            "",
        ]
        # Archived Markdown sometimes uses trailing spaces for hard line breaks.
        # Strip them so regenerated notes pass repository whitespace checks while
        # preserving all substantive text and blank-line structure.
        raw_note = "\n".join(lines)
        clean_note = "\n".join(line.rstrip() for line in raw_note.splitlines()) + "\n"
        note_path.write_text(clean_note, encoding="utf-8")

        audit_rows.append(
            {
                "record_id": record_id,
                "title": row["title"],
                "section": row["section"],
                "priority": row["priority"],
                "initial_note_quality": row["note_quality"],
                "audit_computed_source_quality": coverage_row["computed_note_quality"],
                "source_match_score": coverage_row["match_score"],
                "original_note_source": source,
                "content_provenance": content_provenance,
                "note_file": note_path.as_posix(),
                "full_text_status": full_text_status,
                "full_text_basis": full_text_basis,
                "pdf_pages": pdf.get("extracted_pages", "") if pdf else "",
                "pdf_sha256": pdf.get("pdf_sha256", "") if pdf else "",
                "title_similarity": pdf.get("title_similarity", "") if pdf else "",
                "review_standard": review_standard(row["priority"]),
                "claim_use_status": claim_status,
            }
        )

    args.audit_output.parent.mkdir(parents=True, exist_ok=True)
    with args.audit_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=audit_rows[0].keys(), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(audit_rows)
    with args.remediation_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=remediation_rows[0].keys(), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(remediation_rows)

    print(f"register_records={len(register)}")
    print(f"materialized_notes={len(list(args.notes.glob('[0-9][0-9][0-9][0-9].md')))}")
    print(f"remediated_notes={len(remediation_rows)}")
    print(
        "current_cycle_full_texts="
        + str(sum(row["full_text_status"].startswith("current-cycle") for row in audit_rows))
    )
    print(f"access_exceptions={sum(row['record_id'] == 249 for row in audit_rows)}")


if __name__ == "__main__":
    main()
