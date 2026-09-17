# Final DOI audit — 386-study synthesis

**Status:** complete

**Audit cutoff:** 2026-09-16

**Scope:** the 385-study frozen synthesis plus revision-stage Record 760

## Results

| Measure | Count |
|---|---:|
| Synthesis records audited | 386 |
| Records with a verified archival DOI | 249 |
| Records without a verified archival DOI | 137 |
| Unresolved records | 0 |
| Duplicate final DOIs | 0 |
| Documented manual decisions | 26 |

“Without a verified archival DOI” does not mean that a paper is unpublished. It
includes archival venues that identify articles with stable proceedings or
OpenReview URLs rather than item-level DOIs, plus publisher records for which no
DOI had been assigned by the cutoff date.

## Audit method

1. Construct the exact 386-record scope from
   `final_synthesis_membership.csv` and
   `final_synthesis_revision_additions.csv`.
2. Normalize DOI syntax and validate existing DOI identifiers.
3. Search saved Crossref and OpenAlex results by exact title for records without
   a verified DOI.
4. Retain only archival publisher/proceedings DOI families. Exclude arXiv DOIs,
   repository reposts, preprint DOIs, and Crossref `posted-content` objects.
5. Resolve edge cases against official publisher, proceedings, ACL Anthology,
   CVF, OpenReview, or NeurIPS records. Every override is documented in
   `doi_audit_386_manual_decisions.csv`.
6. Require 386 unique record IDs and titles, no unresolved statuses, no duplicate
   final DOI, valid DOI syntax, and an exact match to the synthesis membership.

The executable audit supports a live Crossref/OpenAlex run and a deterministic
offline finalization of saved API results. The offline pass closed the manual
edge cases in the restricted finalization environment. The repository workflow
then completed a live Crossref/OpenAlex rerun and refreshed the published
ledger. Both passes produced the same headline totals and no unresolved rows or
duplicate final DOIs.

## Corrections made during finalization

The title-only first pass contained four non-archival or incorrect DOI choices:

| Record | Paper | Final decision |
|---:|---|---|
| 1 | *Attention Is All You Need* | No archival DOI; removed repository repost DOI `10.65215/2q58a426` |
| 25 | *Multimodal Chain-of-Thought Reasoning in Language Models* | No archival DOI; removed `posted-content` DOI `10.59350/90sh1-hbs94` |
| 162 | *OS Agents* | Replaced Preprints.org DOI with ACL DOI `10.18653/v1/2025.acl-long.369` |
| 320 | *LLM-Powered GUI Agents in Phone Automation* | No archival DOI; removed Preprints.org DOI `10.20944/preprints202501.0413.v1` |

The seven records left ambiguous by the automated first pass were all closed:
Records 3 and 214 have no verified archival DOI; Records 288, 372, 436, 463,
and 659 have verified archival DOIs. An additional 12 archival DOIs and seven
no-DOI decisions were resolved from official records, for 26 documented manual
decisions overall.

## Released files

- `data/doi_audit_386.csv` — one row per synthesis record, including the final
  DOI decision, evidence source, verification URL, automated match metadata,
  and notes.
- `data/doi_audit_386_summary.json` — counts, execution mode, and integrity
  results.
- `data/doi_title_map_386.json` — compact record/title/DOI/status map.
- `data/doi_audit_386_manual_decisions.csv` — official-source adjudications for
  the 26 edge cases.
- `scripts/doi_audit_386.py` — reproducible live audit and offline finalizer.
