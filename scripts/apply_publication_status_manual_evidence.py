#!/usr/bin/env python3
"""Augment automated publication-status output with explicitly logged authoritative evidence.

This does not alter the 805-study register. It is only for cases where OpenAlex/
Crossref do not expose an already verified archival venue. Every manual item must
carry a source URL and note in data/publication_status_manual_evidence.csv.
"""
import csv, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_publication_status_v2 import REGISTER_PUBLISHED, venues_agree

out_path = Path(sys.argv[1] if len(sys.argv) > 1 else 'data/publication_status_verification_v2.csv')
ev_path = Path(sys.argv[2] if len(sys.argv) > 2 else 'data/publication_status_manual_evidence.csv')

with out_path.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fields = list(reader.fieldnames or [])
    rows = list(reader)
by_id = {int(r['record_id']): r for r in rows}

with ev_path.open(encoding='utf-8-sig', newline='') as f:
    evidence_rows = list(csv.DictReader(f))

if 'manual_evidence_url' not in fields:
    fields.append('manual_evidence_url')
if 'manual_evidence_note' not in fields:
    fields.append('manual_evidence_note')

for ev in evidence_rows:
    rid = int(ev['record_id'])
    if rid not in by_id:
        raise SystemExit(f'manual evidence record absent from verification output: {rid}')
    row = by_id[rid]
    status = (ev.get('external_status') or '').strip().lower()
    venue = (ev.get('external_venue') or '').strip()
    url = (ev.get('evidence_url') or '').strip()
    note = (ev.get('evidence_note') or '').strip()
    if not url or not note:
        raise SystemExit(f'manual evidence must include URL and note: {rid}')

    row['manual_evidence_url'] = url
    row['manual_evidence_note'] = note
    existing = (row.get('archival_evidence') or '').strip()
    signal = f"manual authoritative evidence: {venue or status} ({url})"
    row['archival_evidence'] = ' | '.join(x for x in [existing, signal] if x)

    if status == 'archival':
        if venue:
            row['found_venue'] = venue
        reg_status = row.get('register_status', '')
        reg_venue = (row.get('register_venue') or '').strip()
        if reg_status in REGISTER_PUBLISHED:
            if not reg_venue:
                row['VERDICT'] = 'VENUE_MISSING'
                row['notes'] = f"register venue blank; authoritative archival venue '{venue}'"
            elif venues_agree(reg_venue, venue):
                row['VERDICT'] = 'OK_ARCHIVAL'
                row['notes'] = ''
            else:
                row['VERDICT'] = 'VENUE_MISMATCH'
                row['notes'] = f"register '{reg_venue}' vs authoritative '{venue}'"
        else:
            if reg_venue and venue and not venues_agree(reg_venue, venue):
                row['VERDICT'] = 'VENUE_MISMATCH'
                row['notes'] = f"register '{reg_venue}' vs authoritative '{venue}'"
            else:
                row['VERDICT'] = 'UPGRADE'
                row['notes'] = f"register '{reg_status}'; authoritative archival evidence '{venue}'"
    else:
        raise SystemExit(f'unsupported manual external_status for {rid}: {status}')

with out_path.open('w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader(); w.writerows(rows)

print(f'applied {len(evidence_rows)} manual publication-evidence record(s)')
