#!/usr/bin/env python3
import csv, sys
from pathlib import Path

p = Path(sys.argv[1] if len(sys.argv) > 1 else 'data/publication_status_verification_v2.csv')
rows = {int(r['record_id']): r for r in csv.DictReader(p.open(encoding='utf-8-sig'))}
expected = {
    1: 'OK_ARCHIVAL',      # Attention Is All You Need
    110: 'VENUE_MISMATCH', # EMNLP demo/system track vs COLM negative-control case
    135: 'UPGRADE',        # AppWorld
    323: 'DOWNGRADE',      # known preprint-only / no archival evidence case
    774: 'VENUE_MISSING',  # accepted record with blank register venue
}
failed = []
for rid, verdict in expected.items():
    got = rows.get(rid, {}).get('VERDICT')
    print(f'{rid}: expected={verdict} got={got}')
    if got != verdict:
        failed.append((rid, verdict, got))
if failed:
    raise SystemExit('Known-answer verification failed: ' + '; '.join(f'{r} expected {e} got {g}' for r,e,g in failed))
print('All publication-status known-answer checks passed.')
