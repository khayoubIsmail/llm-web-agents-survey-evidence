#!/usr/bin/env python3
"""Build a conservative manual-adjudication queue from publication-status v2.2.

This script does NOT modify the 805-study corpus and does NOT make final publication
status decisions. It only prioritizes records that require manual authoritative review.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

SRC = Path("data/publication_status_verification_v2.csv")
OUT = Path("data/publication_status_adjudication_queue.csv")
SUMMARY = Path("data/publication_status_adjudication_queue_summary.json")

FLAGGED = {"DOWNGRADE", "UPGRADE", "VENUE_MISMATCH", "VENUE_MISSING", "NO_MATCH"}
AUTHORITATIVE_HOSTS = {
    "openreview.net",
    "proceedings.neurips.cc",
    "proceedings.mlr.press",
    "aclanthology.org",
    "dl.acm.org",
    "ieeexplore.ieee.org",
    "link.springer.com",
    "www.sciencedirect.com",
    "sciencedirect.com",
    "jmlr.org",
    "www.jmlr.org",
    "aaai.org",
    "ojs.aaai.org",
    "ijcai.org",
    "www.ijcai.org",
    "usenix.org",
    "www.usenix.org",
    "aclanthology.org",
    "proceedings.iclr.cc",
}


def host_of(identifier: str) -> str:
    identifier = (identifier or "").strip()
    if not identifier.startswith(("http://", "https://")):
        return ""
    return (urlparse(identifier).hostname or "").lower()


def is_direct_authoritative(identifier: str) -> bool:
    host = host_of(identifier)
    return host in AUTHORITATIVE_HOSTS or any(host.endswith("." + h) for h in AUTHORITATIVE_HOSTS)


def suspicious_ok_preprint(row: dict[str, str]) -> bool:
    if row.get("VERDICT") != "OK_PREPRINT":
        return False
    try:
        archival = int(row.get("archival_candidate_count") or 0)
    except ValueError:
        archival = 0
    note = (row.get("notes") or "").lower()
    return archival > 0 or "uncorroborated" in note or "archival" in note


with SRC.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

queue = []
for row in rows:
    verdict = row.get("VERDICT", "")
    suspicious = suspicious_ok_preprint(row)
    if verdict not in FLAGGED and not suspicious:
        continue

    identifier = (row.get("register_identifier") or "").strip()
    direct = is_direct_authoritative(identifier)
    if verdict in {"VENUE_MISMATCH", "VENUE_MISSING"}:
        priority = "A1"
    elif verdict == "DOWNGRADE" and direct:
        priority = "A2"
    elif verdict == "UPGRADE":
        priority = "A3"
    elif verdict == "DOWNGRADE":
        priority = "B1"
    elif verdict == "NO_MATCH":
        priority = "B2"
    else:
        priority = "C1"

    queue.append({
        "record_id": row.get("record_id", ""),
        "title": row.get("title", ""),
        "register_status": row.get("register_status", ""),
        "register_venue": row.get("register_venue", ""),
        "register_identifier": identifier,
        "identifier_host": host_of(identifier),
        "direct_authoritative_identifier": "yes" if direct else "no",
        "machine_verdict": verdict,
        "machine_notes": row.get("notes", ""),
        "found_title": row.get("found_title", ""),
        "found_venue": row.get("found_venue", ""),
        "found_year": row.get("found_year", ""),
        "found_doi": row.get("found_doi", ""),
        "candidate_sources": row.get("candidate_sources", ""),
        "archival_evidence": row.get("archival_evidence", ""),
        "suspicious_ok_preprint": "yes" if suspicious else "no",
        "priority": priority,
        "adjudication_decision": "PENDING",
        "authoritative_evidence_url": "",
        "authoritative_evidence_note": "",
        "adjudicated_by": "",
        "adjudicated_at": "",
    })

queue.sort(key=lambda r: (r["priority"], int(r["record_id"])))
fields = list(queue[0].keys()) if queue else []
with OUT.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(queue)

counts = Counter(r["machine_verdict"] for r in queue)
priority_counts = Counter(r["priority"] for r in queue)
direct_counts = Counter(r["direct_authoritative_identifier"] for r in queue)
out = {
    "source_rows": len(rows),
    "queue_rows": len(queue),
    "machine_verdict_counts": dict(sorted(counts.items())),
    "priority_counts": dict(sorted(priority_counts.items())),
    "direct_authoritative_identifier_counts": dict(sorted(direct_counts.items())),
    "policy": "queue_only_no_corpus_mutation",
}
SUMMARY.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
