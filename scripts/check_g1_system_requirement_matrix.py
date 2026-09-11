#!/usr/bin/env python3
import csv
from pathlib import Path

MATRIX = Path('data/g1_system_requirement_matrix.csv')
REGISTER = Path('data/studies_805_mapping_corpus.csv')
ALLOWED = {'YES', 'PARTIAL', 'NO', 'NR'}
CAPS = [
    'unfamiliar_site_navigation',
    'explicit_schema_coverage',
    'field_level_provenance',
    'unsupported_value_control',
    'cross_site_transfer',
    'complete_dataset_assembly',
]
REQUIRED = [
    'record_id', 'system_name', 'candidate_family', *CAPS, 'joint_evaluation',
    'checked_source_locations', 'coder_rationale', 'full_contract_result',
    'verification_status'
]


def fail(msg: str) -> None:
    raise SystemExit(f'G1 audit failed: {msg}')


if not MATRIX.exists():
    fail(f'missing {MATRIX}')
if not REGISTER.exists():
    fail(f'missing {REGISTER}')

with REGISTER.open(encoding='utf-8-sig', newline='') as f:
    register_ids = {int(r['record_id']) for r in csv.DictReader(f)}

with MATRIX.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = reader.fieldnames or []

missing = [c for c in REQUIRED if c not in fields]
if missing:
    fail(f'missing columns: {missing}')
if len(rows) < 8:
    fail(f'counterexample set too small: {len(rows)} rows')

seen = set()
full_contract_rows = []
families = set()
for i, row in enumerate(rows, start=2):
    try:
        rid = int(row['record_id'])
    except Exception:
        fail(f'line {i}: invalid record_id')
    if rid in seen:
        fail(f'line {i}: duplicate record_id {rid}')
    seen.add(rid)
    if rid not in register_ids:
        fail(f'line {i}: record {rid} absent from 805-row register')
    if rid == 249:
        fail('record 249 cannot be used in synthesis-level G1 evidence')
    note = Path(f'notes/papers/{rid:04d}.md')
    if not note.exists():
        fail(f'line {i}: missing note {note}')

    if not row['system_name'].strip() or not row['candidate_family'].strip():
        fail(f'line {i}: missing system name or family')
    families.add(row['candidate_family'].strip())

    for col in CAPS + ['joint_evaluation']:
        if row[col] not in ALLOWED:
            fail(f'line {i}: {col}={row[col]!r} not one of {sorted(ALLOWED)}')

    for col in ['checked_source_locations', 'coder_rationale']:
        if len(row[col].strip()) < 20:
            fail(f'line {i}: {col} is too weak/empty')

    full = all(row[c] == 'YES' for c in CAPS) and row['joint_evaluation'] == 'YES'
    expected = 'YES' if full else 'NO'
    if row['full_contract_result'] != expected:
        fail(f'line {i}: full_contract_result should be {expected}')
    if full:
        full_contract_rows.append((rid, row['system_name']))

    status = row['verification_status']
    if 'final_membership_pending' not in status and 'final_membership_verified' not in status:
        fail(f'line {i}: verification_status must state final membership state')

# Ensure the audit is not one-sided.
family_text = ' '.join(families).lower()
for token in ['web agent', 'extraction', 'aggregation', 'workflow']:
    if token not in family_text:
        fail(f'candidate families do not cover expected counterexample family: {token}')

print(f'G1 matrix structural audit passed: {len(rows)} candidates; {len(full_contract_rows)} full-contract counterexamples.')
if full_contract_rows:
    print('Counterexamples that satisfy the complete contract:')
    for rid, name in full_contract_rows:
        print(f'  {rid}: {name}')
else:
    print('No coded candidate satisfies all six capabilities plus joint evaluation.')
print('Final corpus-membership revalidation remains a separate gate.')
