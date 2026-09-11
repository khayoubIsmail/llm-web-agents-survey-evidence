#!/usr/bin/env python3
"""Apply verified A1 full-text rereads to the paper-note audit.

Only records explicitly listed in data/a1_fulltext_rechecks.csv are changed.
This script does not infer that a paper was read from note formatting or metadata.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

AUDIT = Path('data/paper_note_audit.csv')
RECHECKS = Path('data/a1_fulltext_rechecks.csv')
SUMMARY = Path('data/summary.json')

with RECHECKS.open(encoding='utf-8', newline='') as fh:
    rechecks = {int(r['record_id']): r for r in csv.DictReader(fh)}

with AUDIT.open(encoding='utf-8', newline='') as fh:
    reader = csv.DictReader(fh)
    fields = reader.fieldnames
    rows = list(reader)

seen = set()
for row in rows:
    rid = int(row['record_id'])
    r = rechecks.get(rid)
    if not r:
        continue
    seen.add(rid)
    row['content_provenance'] = r['content_provenance']
    row['full_text_status'] = r['full_text_status']
    row['full_text_basis'] = r['full_text_basis']
    row['claim_use_status'] = r['claim_use_status']
    # These web-reviewed records were not locally hashed PDFs; do not invent a hash.
    row['pdf_pages'] = ''
    row['pdf_sha256'] = ''
    row['title_similarity'] = ''

missing = set(rechecks) - seen
if missing:
    raise SystemExit(f'recheck IDs absent from paper_note_audit.csv: {sorted(missing)}')

with AUDIT.open('w', encoding='utf-8', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

# Recompute note-audit counts from the actual audit rows. Keep full-text access
# exceptions distinct from records that were read in full but are blocked for a
# separate bibliographic/publication-status reason.
no_current = sum('no current-cycle PDF verification' in r['full_text_status'] for r in rows)
current_cycle = sum(r['full_text_status'].startswith('current-cycle') for r in rows)
retained = sum('existing review archive audited' in r['full_text_status'] for r in rows)
access_exception_ids = sorted(
    int(r['record_id'])
    for r in rows
    if r['claim_use_status'].startswith('blocked pending full text')
)
publication_status_block_ids = sorted(
    int(r['record_id'])
    for r in rows
    if 'blocked pending publication-status revalidation' in r['claim_use_status']
)

with SUMMARY.open(encoding='utf-8') as fh:
    summary = json.load(fh)
pa = summary.setdefault('paper_note_audit', {})
pa['current_cycle_full_text_rechecks_or_pdf_checks'] = current_cycle
pa['records_still_without_current_cycle_full_text_verification'] = no_current
pa['retained_archive_only_records'] = retained
pa['full_text_access_exceptions'] = len(access_exception_ids)
pa['access_exception_record_ids'] = access_exception_ids
pa['publication_status_revalidation_blocks'] = len(publication_status_block_ids)
pa['publication_status_revalidation_record_ids'] = publication_status_block_ids
pa['a1_verified_rereads_logged'] = len(rechecks)
SUMMARY.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print(
    f'applied {len(rechecks)} verified rereads; '
    f'remaining no-current-cycle records: {no_current}; '
    f'full-text access exceptions: {len(access_exception_ids)}; '
    f'publication-status revalidation blocks: {len(publication_status_block_ids)}'
)
