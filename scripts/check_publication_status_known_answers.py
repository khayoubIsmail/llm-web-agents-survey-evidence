#!/usr/bin/env python3
import csv, re, sys
from difflib import SequenceMatcher
from pathlib import Path

p = Path(sys.argv[1] if len(sys.argv) > 1 else 'data/publication_status_verification_v2.csv')
rows = {int(r['record_id']): r for r in csv.DictReader(p.open(encoding='utf-8-sig'))}

# These cases cover the failure modes that matter for corpus membership:
# - archival work whose arXiv/OpenAlex record is only a preprint (4)
# - exact archival DOI/location evidence (1, 14)
# - preprint IDs that OpenAlex has previously mis-linked to unrelated works (15, 29, 33)
# - authoritative manual evidence / venue mismatch (110)
# - genuine upgrade, downgrade and missing-venue cases (135, 323, 774)
expected = {
    1: 'OK_ARCHIVAL',
    4: 'OK_ARCHIVAL',
    14: 'OK_ARCHIVAL',
    15: 'OK_PREPRINT',
    29: 'OK_PREPRINT',
    33: 'OK_PREPRINT',
    110: 'VENUE_MISMATCH',
    135: 'UPGRADE',
    323: 'DOWNGRADE',
    774: 'VENUE_MISSING',
}

def norm(s):
    s = re.sub(r'[^a-z0-9 ]+', ' ', (s or '').lower())
    return re.sub(r'\s+', ' ', s).strip()

def sim(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()

failed = []
for rid, verdict in expected.items():
    row = rows.get(rid, {})
    got = row.get('VERDICT')
    print(f'{rid}: expected={verdict} got={got}')
    if got != verdict:
        failed.append(f'{rid} expected {verdict} got {got}')

# Global invariant: every resolved external record must describe the same paper
# as the register row. This catches false arXiv/OpenAlex identifier links.
for rid, row in rows.items():
    how = row.get('resolved_via', '')
    found = row.get('found_title', '')
    if how and how != 'unresolved':
        score = sim(row.get('title', ''), found)
        if not found or score < 0.80:
            failed.append(
                f'{rid} title-inconsistent resolution via {how}: '
                f'{score:.3f} -> {found!r}'
            )

# Require provenance columns emitted only by the hardened resolver, so an older
# verifier cannot accidentally pass this stronger gate.
required_cols = {
    'candidate_sources', 'candidate_count', 'archival_candidate_count',
    'rejected_title_mismatches'
}
header = set(next(iter(rows.values())).keys()) if rows else set()
missing = sorted(required_cols - header)
if missing:
    failed.append('missing hardened-verifier columns: ' + ', '.join(missing))

if failed:
    raise SystemExit('Known-answer verification failed: ' + '; '.join(failed))
print('All publication-status known-answer and title-consistency checks passed.')
