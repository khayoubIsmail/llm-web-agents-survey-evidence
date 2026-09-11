#!/usr/bin/env python3
"""Validate G2 operational definitions used by the G1 absence-claim audit."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFS = ROOT / "data" / "g2_operational_definitions.csv"

REQUIRED_COLUMNS = {
    "definition_id",
    "scope",
    "term",
    "operational_definition",
    "yes_rule",
    "partial_rule",
    "no_rule",
    "nr_rule",
    "minimum_evidence",
    "common_nonqualifiers",
    "g1_use",
}

EXPECTED = {
    "G2-01": ("reviewer_requested", "field-level provenance"),
    "G2-02": ("reviewer_requested", "complete dataset assembly"),
    "G2-03": ("reviewer_requested", "cross-site transfer"),
    "G2-04": ("reviewer_requested", "joint evaluation"),
    "G2-05": ("g1_companion", "unfamiliar-site navigation"),
    "G2-06": ("g1_companion", "explicit schema coverage"),
    "G2-07": ("g1_companion", "unsupported-value control"),
}


def main() -> None:
    with DEFS.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"G2 FAIL: missing columns: {sorted(missing)}")
        rows = list(reader)

    if len(rows) != len(EXPECTED):
        raise SystemExit(f"G2 FAIL: expected {len(EXPECTED)} definitions, found {len(rows)}")

    ids = [row["definition_id"].strip() for row in rows]
    if ids != list(EXPECTED):
        raise SystemExit(f"G2 FAIL: definition IDs/order mismatch: {ids}")

    for row in rows:
        did = row["definition_id"].strip()
        expected_scope, expected_term = EXPECTED[did]
        if row["scope"].strip() != expected_scope:
            raise SystemExit(f"G2 FAIL: {did} scope mismatch")
        if row["term"].strip() != expected_term:
            raise SystemExit(f"G2 FAIL: {did} term mismatch")

        for field in REQUIRED_COLUMNS - {"definition_id", "scope", "term"}:
            if len(row[field].strip()) < 20:
                raise SystemExit(f"G2 FAIL: {did} field {field} missing/too short")
            if re.search(r"\b(TODO|TBD|FIXME)\b", row[field], re.I):
                raise SystemExit(f"G2 FAIL: {did} unresolved placeholder in {field}")

        if not row["yes_rule"].lstrip().startswith("YES"):
            raise SystemExit(f"G2 FAIL: {did} YES rule is not explicit")
        if not row["partial_rule"].lstrip().startswith("PARTIAL"):
            raise SystemExit(f"G2 FAIL: {did} PARTIAL rule is not explicit")
        if not row["no_rule"].lstrip().startswith("NO"):
            raise SystemExit(f"G2 FAIL: {did} NO rule is not explicit")
        if not row["nr_rule"].lstrip().startswith("NR"):
            raise SystemExit(f"G2 FAIL: {did} NR rule is not explicit")

    joint = rows[3]
    joint_text = " ".join(
        [joint["operational_definition"], joint["yes_rule"], joint["g1_use"]]
    ).lower()
    for required_phrase in ("same", "end-to-end", "all"):
        if required_phrase not in joint_text:
            raise SystemExit(
                f"G2 FAIL: joint-evaluation definition missing concept: {required_phrase}"
            )

    provenance = rows[0]
    if "record-level citation is insufficient" not in provenance["g1_use"].lower():
        raise SystemExit("G2 FAIL: field-level provenance must reject record-level citation")

    cross_site = rows[2]
    if "unseen" not in (cross_site["operational_definition"] + cross_site["yes_rule"]).lower():
        raise SystemExit("G2 FAIL: cross-site transfer must require unseen/held-out sites")

    print(
        "G2 gate PASS: 4 reviewer-requested operational definitions + 3 G1 companion "
        "definitions are explicit, four-state coding rules are complete, and the joint-"
        "evaluation rule requires one end-to-end system rather than cross-paper composition."
    )
    print("G1 may now use these definitions; G1 itself remains a separate unfinished audit.")


if __name__ == "__main__":
    main()
