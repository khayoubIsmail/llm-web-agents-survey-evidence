#!/usr/bin/env python3
"""Validate the C1 load-bearing claim evidence matrix.

This is a structural/current-register gate. Final N_SYNTH membership must be checked
separately after publication-status adjudication and synthesis-set reconciliation.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "data" / "c1_claim_evidence_matrix.csv"
REGISTER = ROOT / "data" / "studies_805_mapping_corpus.csv"
NOTES = ROOT / "notes" / "papers"

REQUIRED_COLUMNS = {
    "claim_id",
    "manuscript_location",
    "normalized_claim",
    "primary_study_ids",
    "corroborating_study_ids",
    "boundary_study_ids",
    "quantitative_evidence",
    "source_locations_checked",
    "evidence_strength",
    "verification_status",
}

FORBIDDEN_EVIDENCE_IDS = {249}


def parse_ids(value: str) -> list[int]:
    if not value.strip():
        return []
    out: list[int] = []
    for token in value.split(";"):
        token = token.strip()
        if not token:
            continue
        if not token.isdigit():
            raise ValueError(f"invalid study id token: {token!r}")
        out.append(int(token))
    return out


def load_register_ids() -> set[int]:
    with REGISTER.open("r", encoding="utf-8-sig", newline="") as fh:
        return {int(row["record_id"]) for row in csv.DictReader(fh)}


def main() -> None:
    register_ids = load_register_ids()

    with MATRIX.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing_columns:
            raise SystemExit(f"C1 FAIL: missing columns: {sorted(missing_columns)}")
        rows = list(reader)

    if len(rows) != 11:
        raise SystemExit(f"C1 FAIL: expected 11 load-bearing claims, found {len(rows)}")

    claim_ids = [row["claim_id"].strip() for row in rows]
    expected_claim_ids = [f"C1-{i:02d}" for i in range(1, 12)]
    if claim_ids != expected_claim_ids:
        raise SystemExit(
            f"C1 FAIL: claim IDs/order mismatch: expected {expected_claim_ids}, got {claim_ids}"
        )

    seen: set[str] = set()
    all_evidence_ids: set[int] = set()

    for row in rows:
        claim_id = row["claim_id"].strip()
        if claim_id in seen:
            raise SystemExit(f"C1 FAIL: duplicate claim ID {claim_id}")
        seen.add(claim_id)

        if not row["manuscript_location"].strip():
            raise SystemExit(f"C1 FAIL: {claim_id} missing manuscript location")
        if len(row["normalized_claim"].strip()) < 30:
            raise SystemExit(f"C1 FAIL: {claim_id} claim text is missing/too short")
        if not row["source_locations_checked"].strip():
            raise SystemExit(f"C1 FAIL: {claim_id} missing source-location evidence")
        if not row["evidence_strength"].strip():
            raise SystemExit(f"C1 FAIL: {claim_id} missing evidence strength")
        if not row["verification_status"].strip():
            raise SystemExit(f"C1 FAIL: {claim_id} missing verification status")

        try:
            primary = parse_ids(row["primary_study_ids"])
            corroborating = parse_ids(row["corroborating_study_ids"])
            boundary = parse_ids(row["boundary_study_ids"])
        except ValueError as exc:
            raise SystemExit(f"C1 FAIL: {claim_id}: {exc}") from exc

        if not primary:
            raise SystemExit(f"C1 FAIL: {claim_id} has no primary study IDs")

        ids = set(primary + corroborating + boundary)
        all_evidence_ids.update(ids)

        forbidden = ids & FORBIDDEN_EVIDENCE_IDS
        if forbidden:
            raise SystemExit(
                f"C1 FAIL: {claim_id} uses synthesis-blocked record(s): {sorted(forbidden)}"
            )

        unknown = ids - register_ids
        if unknown:
            raise SystemExit(
                f"C1 FAIL: {claim_id} contains record IDs absent from 805 register: {sorted(unknown)}"
            )

        missing_notes = [rid for rid in sorted(ids) if not (NOTES / f"{rid:04d}.md").exists()]
        if missing_notes:
            raise SystemExit(
                f"C1 FAIL: {claim_id} missing normalized paper note(s): {missing_notes}"
            )

        if re.search(r"\b(TODO|TBD|FIXME)\b", row["source_locations_checked"], re.I):
            raise SystemExit(f"C1 FAIL: {claim_id} has unresolved source-location TODO")

    print(
        "C1 structural gate PASS: "
        f"{len(rows)} claims, {len(all_evidence_ids)} unique evidence records, "
        "all IDs resolve to the 805 register, normalized notes exist, and record 249 is absent."
    )
    print(
        "Final gate still required: revalidate all evidence IDs against final N_SYNTH "
        "after publication-status/manual adjudication."
    )


if __name__ == "__main__":
    main()
