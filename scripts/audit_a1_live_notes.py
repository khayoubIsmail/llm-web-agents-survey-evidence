#!/usr/bin/env python3
"""Audit live 403-paper notes for A1 completion defects.

A TODO/template marker is evidence that the live synthesis is incomplete, not a
completed reading. The report is deliberately conservative and reviewer-facing.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

PAPERS = Path('notes/papers')
OUT = Path('data/a1_live_note_audit.csv')
SUMMARY = Path('data/a1_live_note_audit_summary.json')
TODO_PATTERNS = [
    'When reading this paper, extract',
    'Key evidence to extract from the paper',
]

def field(text, label):
    m = re.search(rf'^- {re.escape(label)}:\s*(.*)$', text, re.M)
    return m.group(1).strip() if m else ''

def title(text):
    m = re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else ''

rows = []
for p in sorted(PAPERS.glob('*.md')):
    text = p.read_text(encoding='utf-8')
    exact_todo = 'When reading this paper, extract' in text
    template_evidence = any(x in text for x in TODO_PATTERNS)
    no_current = 'no current-cycle PDF verification' in text
    blocked = 'blocked pending full text' in text
    numeric_evidence = bool(re.search(r'(?i)(?:table\s*\d+.{0,500})?\b\d+(?:\.\d+)?\s*%|\b\d{2,}\s+(?:tasks|instances|records|examples|turns|websites|fields|pairs)\b', text, re.S))
    status = 'complete-or-needs-manual-quality-check'
    if blocked:
        status = 'blocked-full-text-unavailable'
    elif template_evidence or no_current:
        status = 'needs-a1-full-text-remediation'
    rows.append({
        'record_id': int(p.stem),
        'title': title(text),
        'section_priority': field(text, 'Section / priority'),
        'has_exact_when_reading_todo': exact_todo,
        'has_template_evidence_block': template_evidence,
        'no_current_cycle_verification': no_current,
        'has_concrete_numeric_evidence_signal': numeric_evidence,
        'claim_use_status': field(text, 'Claim-use status'),
        'a1_status': status,
        'note_file': p.as_posix(),
    })

if len(rows) != 403:
    raise SystemExit(f'expected 403 live notes, found {len(rows)}')

fields = list(rows[0])
with OUT.open('w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=fields)
    w.writeheader(); w.writerows(rows)

summary = {
    'live_notes': len(rows),
    'exact_when_reading_todo': sum(r['has_exact_when_reading_todo'] for r in rows),
    'template_evidence_block': sum(r['has_template_evidence_block'] for r in rows),
    'no_current_cycle_verification': sum(r['no_current_cycle_verification'] for r in rows),
    'numeric_evidence_signal': sum(r['has_concrete_numeric_evidence_signal'] for r in rows),
    'needs_a1_full_text_remediation': sum(r['a1_status'] == 'needs-a1-full-text-remediation' for r in rows),
    'blocked_full_text_unavailable': sum(r['a1_status'] == 'blocked-full-text-unavailable' for r in rows),
    'audit_rule': 'A note containing a reading TODO/template or lacking current-cycle verification is not counted here as A1-remediated.'
}
SUMMARY.write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
print(json.dumps(summary, indent=2))
