#!/usr/bin/env python3
"""Validate the 403-paper note corpus and its provenance audit."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--register-json", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--remediation", type=Path, required=True)
    parser.add_argument("--notes", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()

    register = read_csv(args.register)
    audit = read_csv(args.audit)
    remediation = read_csv(args.remediation)
    register_json = json.loads(args.register_json.read_text(encoding="utf-8"))
    summary = json.loads(args.summary.read_text(encoding="utf-8"))

    register_ids = [int(row["record_id"]) for row in register]
    audit_ids = [int(row["record_id"]) for row in audit]
    remediation_ids = [int(row["record_id"]) for row in remediation]
    json_ids = [int(row["record_id"]) for row in register_json]
    note_paths = sorted(args.notes.glob("[0-9][0-9][0-9][0-9].md"))
    note_ids = [int(path.stem) for path in note_paths]

    if len(register_ids) != 403 or len(set(register_ids)) != 403:
        fail("register must contain 403 unique record IDs")
    if register_ids != json_ids:
        fail("CSV and JSON register IDs differ or are ordered differently")
    if set(audit_ids) != set(register_ids) or len(audit_ids) != 403:
        fail("paper-note audit is not a one-to-one match with the register")
    if set(note_ids) != set(register_ids) or len(note_ids) != 403:
        fail("paper-note files are not a one-to-one match with the register")
    if len(remediation_ids) != 71 or len(set(remediation_ids)) != 71:
        fail("remediation log must contain 71 unique records")
    if not set(remediation_ids) <= set(register_ids):
        fail("remediation log contains a record outside the register")

    register_by_id = {int(row["record_id"]): row for row in register}
    audit_by_id = {int(row["record_id"]): row for row in audit}
    for path in note_paths:
        record_id = int(path.stem)
        text = path.read_text(encoding="utf-8", errors="replace")
        row = register_by_id[record_id]
        if not text.startswith("<!-- normalized-paper-note -->\n"):
            fail(f"record {record_id} lacks the normalized-note marker")
        if f"# {row['title']}\n" not in text:
            fail(f"record {record_id} note title differs from the register")
        if f"- Record ID: {record_id}\n" not in text:
            fail(f"record {record_id} note lacks its stable ID")
        body = text.split("<!-- note-body-start -->", 1)[-1]
        words = len(re.findall(r"\b[\w'-]+\b", body))
        minimum = 1 if record_id == 249 else (400 if row["priority"] in {"P0", "P1"} else 100)
        if words < minimum:
            fail(f"record {record_id} body has {words} words; expected at least {minimum}")
        if record_id in remediation_ids and record_id != 249:
            if not re.search(r"(?i)limitations?|critical assessment", body):
                fail(f"remediated record {record_id} lacks critical limitations")
            if not re.search(r"(?i)relevance to (?:the )?survey|survey relevance", body):
                fail(f"remediated record {record_id} lacks explicit survey relevance")

    status_counts = Counter(row["full_text_status"] for row in audit)
    current = status_counts["current-cycle full text extracted and title-checked"]
    archived = status_counts["existing review archive audited; no current-cycle PDF verification"]
    blocked = status_counts["blocked: full text unavailable"]
    if (current, archived, blocked) != (134, 268, 1):
        fail(f"unexpected full-text status counts: {(current, archived, blocked)}")
    exception = audit_by_id[249]
    if exception["claim_use_status"] != "blocked pending full text":
        fail("record 249 is not blocked from claim-level synthesis")
    if any(
        row["claim_use_status"] == "blocked pending full text" and int(row["record_id"]) != 249
        for row in audit
    ):
        fail("an unexpected record is blocked from synthesis")

    expected_summary = summary["paper_note_audit"]
    calculated = {
        "normalized_note_files": len(note_ids),
        "current_cycle_note_remediations": len(remediation_ids),
        "current_cycle_pdf_full_text_checks": current,
        "retained_substantive_archive_notes": archived,
        "full_text_analysis_documented": current + archived,
        "full_text_access_exceptions": blocked,
        "access_exception_record_ids": [249],
    }
    for key, value in calculated.items():
        if expected_summary.get(key) != value:
            fail(f"summary field {key!r} is {expected_summary.get(key)!r}, expected {value!r}")

    print("validation=passed")
    print("register_records=403")
    print("normalized_notes=403")
    print("remediated_notes=71")
    print("current_cycle_full_texts=134")
    print("retained_archive_notes=268")
    print("access_exceptions=1 (record 249)")


if __name__ == "__main__":
    main()
