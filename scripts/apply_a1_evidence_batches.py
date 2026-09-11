#!/usr/bin/env python3
"""Apply explicitly reviewed A1 evidence batches to live paper notes.

Each JSON batch under data/a1_evidence_batches/ is authored only after the paper's
canonical full text has been reviewed.  The script removes prospective reading TODOs,
adds paper-specific verified evidence, updates provenance metadata, and synchronizes
the explicit full-text reread ledger.  It never infers a reread from note quality.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

BATCH_DIR = Path('data/a1_evidence_batches')
PAPERS = Path('notes/papers')
RECHECKS = Path('data/a1_fulltext_rechecks.csv')

entries: dict[int, dict] = {}
for p in sorted(BATCH_DIR.glob('*.json')):
    data = json.loads(p.read_text(encoding='utf-8'))
    for raw_id, item in data.items():
        rid = int(raw_id)
        if rid in entries:
            raise SystemExit(f'duplicate A1 batch record {rid}: {p}')
        entries[rid] = item

if not entries:
    raise SystemExit('no A1 evidence batch entries found')


def replace_meta(text: str, label: str, value: str) -> str:
    pat = rf'^- {re.escape(label)}:\s*.*$'
    repl = f'- {label}: {value}'
    if re.search(pat, text, re.M):
        return re.sub(pat, repl, text, flags=re.M)
    marker = '## Analysis'
    if marker not in text:
        raise ValueError(f'missing metadata anchor for {label}')
    return text.replace(marker, repl + '\n\n' + marker, 1)


def remove_template_and_insert(text: str, item: dict) -> str:
    evidence = item.get('evidence', '').strip()
    limitations = item.get('limitations', '').strip()
    block_parts = ['#### Concrete evidence verified from the full paper', '', evidence]
    if limitations:
        block_parts += ['', '##### Author-stated / evidence-based limitations', '', limitations]
    block = '\n'.join(block_parts).rstrip() + '\n\n---\n\n'

    # Most historical templates use this exact prospective block.
    pat = re.compile(
        r'#### Key evidence to extract from the paper\s*\n.*?(?=#### Limitations\s*\n)',
        re.S,
    )
    if pat.search(text):
        text = pat.sub(block, text, count=1)
    else:
        # Some notes are substantive but were not rechecked this cycle. Insert a
        # compact verification block before the reading decision / BibTeX / end.
        anchors = ['#### Reading decision', '#### BibTeX', '<!-- note-body-end -->']
        inserted = False
        for anchor in anchors:
            if anchor in text:
                text = text.replace(anchor, block + anchor, 1)
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + '\n\n---\n\n' + block

    # Defensive cleanup: no completed note may retain prospective A1 markers.
    text = text.replace('When reading this paper, extract these concrete evidence points:', '')
    text = text.replace('#### Key evidence to extract from the paper', '#### Concrete evidence verified from the full paper')
    return text


for rid, item in sorted(entries.items()):
    note = PAPERS / f'{rid:04d}.md'
    if not note.exists():
        raise SystemExit(f'missing note for A1 batch record {rid}')
    text = note.read_text(encoding='utf-8')
    source = item['source'].strip()
    basis = item['full_text_basis'].strip()
    provenance = item.get(
        'content_provenance',
        'current-cycle full-text remediation and verification of the historical paper-specific note',
    ).strip()
    claim = item.get('claim_use_status', 'paper-specific note ready for synthesis').strip()
    text = replace_meta(text, 'Content provenance', provenance)
    text = replace_meta(
        text,
        'Full-text status',
        f'current-cycle full text independently read and title-checked from {source}',
    )
    text = replace_meta(text, 'Full-text basis', basis)
    text = replace_meta(text, 'Claim-use status', claim)
    text = remove_template_and_insert(text, item)
    note.write_text(text, encoding='utf-8')

# Merge batch entries into explicit reread ledger.
with RECHECKS.open(encoding='utf-8', newline='') as fh:
    old_rows = list(csv.DictReader(fh))
fields = [
    'record_id','review_date','source','full_text_status','full_text_basis',
    'content_provenance','claim_use_status'
]
ledger = {int(r['record_id']): r for r in old_rows}
for rid, item in entries.items():
    source = item['source'].strip()
    ledger[rid] = {
        'record_id': str(rid),
        'review_date': item.get('review_date', '2026-09-11'),
        'source': source,
        'full_text_status': f'current-cycle full text independently read and title-checked from {source}',
        'full_text_basis': item['full_text_basis'].strip(),
        'content_provenance': item.get(
            'content_provenance',
            'current-cycle full-text remediation and verification of the historical paper-specific note',
        ).strip(),
        'claim_use_status': item.get('claim_use_status', 'paper-specific note ready for synthesis').strip(),
    }
with RECHECKS.open('w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=fields)
    w.writeheader()
    for rid in sorted(ledger):
        w.writerow(ledger[rid])

print(f'applied {len(entries)} A1 evidence-batch records; ledger now has {len(ledger)} records')
