# Data Dictionary

Field definitions for the current corpus registers, final synthesis files, search-reporting artifacts, paper-note audits, and evaluation-protocol supplements.

## Authoritative corpus layers

| Layer | Count | Authoritative artifact |
|---|---:|---|
| Mapping corpus | 805 | `data/studies_805_mapping_corpus.csv` |
| Publication-eligible pool | 454 | `data/publication_status_corpus_freeze_summary.json` |
| Historical normalized-note / synthesis-candidate set | 403 | `notes/papers/` + historical candidate manifests |
| Final qualitative synthesis | 385 | `data/final_synthesis_membership.csv` |

The historical 403-record file/note layer must not be described as the current publication-eligible pool. The final publication-status audit expanded/reconciled publication eligibility across all 805 mapped studies and freezes `N_POOL = 454`; intersecting eligibility with the historical candidate set and full-text availability yields `N_SYNTH = 385`.

## `data/studies_805_mapping_corpus.csv`

| Field | Meaning |
|---|---|
| `record_id` | Stable identifier in the reconciled 805-study mapping corpus. |
| `section` | Primary thematic section assigned during mapping. |
| `priority` | Evidence-use tier: P0 cornerstone, P1 primary, P2 supporting/extending, P3 contextual/historical. Not a risk-of-bias score. |
| `year` | Canonical publication year after verification. |
| `title` | Canonical study title. |
| `publication_status` | Full verified publication status. |
| `status_category` | Normalized publication-status category. |
| `venue` | Canonical venue. |
| `identifier` | DOI, official proceedings/OpenReview URL, arXiv identifier, or other persistent identifier. |
| `verification_source` | Source/audit trail used to verify publication metadata/status. |
| `bibliography_eligibility` | Record-level eligibility wording inherited from the corpus/status audit. For current pool membership, use the frozen publication-status artifacts rather than assuming that the historical 403-file set is authoritative. |
| `note_quality` | Historical/internal note-readiness grade. |
| `evidence_readiness` | Claim-use readiness after validation. |
| `pages` | Final page range where available. |
| `canonical_status_detail` | Detailed final status/version decision. |
| `final_exclusion_reason` | Explicit final exclusion reason where applicable. |

### Priority counts

| Tier | Mapping 805 | Publication-eligible 454 | Final synthesis 385 |
|---|---:|---:|---:|
| P0 | 20 | 18 | 18 |
| P1 | 179 | 110 | 96 |
| P2 | 444 | 233 | 189 |
| P3 | 162 | 93 | 82 |

## `data/final_synthesis_membership.csv`

This file is the authoritative study-level membership table for the 385-study final qualitative synthesis. It should be used for final synthesis counts, tier counts, status counts, and downstream claim/system revalidation.

## `data/search_queries_historical.csv`

| Field | Meaning |
|---|---|
| `query_id` | Stable label Q1–Q5. |
| `query_text` | Verbatim Boolean query preserved in the first 152-page SLR. |
| `historical_source` | Historical location from which the string was recovered. |
| `historical_source_date` | Date of the preserved historical manuscript. |
| `provenance` | Whether the string is verbatim historical text rather than a later template. |

## `data/search_source_reporting.csv`

| Field | Meaning |
|---|---|
| `source` | Search/discovery/verification interface. |
| `role` | Direct scholarly search, repository-assisted discovery, or supplementary resolution/version verification. |
| `access_route` | How the source was accessed when retained/confirmed. |
| `query_set` | Historical query set used, or `NA` when the source was not a recurring direct-query interface in the final audit. |
| `coverage_window` | Review/search period. |
| `last_search` | Last retained search/update month; exact day is marked unavailable where not preserved. |
| `language_restriction` | Language scope. |
| `field_restriction` | Actual search-field practice; no source-specific field syntax is inferred. |
| `gross_records_retrieved` | Historical gross per-source count, `NR` where not recoverable. |
| `gross_count_status` | Explanation of why source-level counts are or are not available. |
| `provenance` | Historical manuscript vs author-confirmed/current-audit basis. |

## `data/exclusion_ledger_availability.csv`

This is **not a synthetic exclusion ledger**. It is an availability map showing which exclusion stages retain record-level identities/reasons and which historical rows are missing. In particular, the complete 2,643-row P4 record-level exclusion ledger has not been recovered and is not reconstructed.

## `data/paper_note_audit.csv`

| Field | Meaning |
|---|---|
| `record_id` | Stable ID linking note evidence to the historical 403 candidate set. |
| `title`, `section`, `priority` | Canonical register metadata. |
| `initial_note_quality` | Readiness label present before remediation. |
| `audit_computed_source_quality` | Heuristic coverage grade for matched historical source material. |
| `source_match_score` | Normalized title-similarity score for selected historical source note. |
| `original_note_source` | Historical review-archive provenance path or explicit no-match label. |
| `content_provenance` | Whether the live note preserves archive evidence, is a current-cycle remediation, or is an access exception. |
| `note_file` | Canonical normalized paper note under `notes/papers/`. |
| `full_text_status` | Current full-text verification/access state. |
| `full_text_basis` | Human-readable basis for full-text verification. |
| `pdf_pages`, `pdf_sha256`, `title_similarity` | PDF verification fields when applicable. |
| `review_standard` | Tier-specific reading/analysis depth. |
| `claim_use_status` | Whether the note may support the final synthesis. |

## `notes/papers/` and `notes/original_sources/`

Both directories contain **403 paper-specific files keyed to the historical normalized-note/synthesis-candidate set**. They are retained for provenance and audit continuity. They are not equivalent to the current 454 publication-eligible pool or the final 385-study synthesis.

`notes/papers/<id>.md` is the normalized live note. `notes/original_sources/<id>.md` is the paper-specific synthesis-source record keyed to the same historical record ID.

## Historical source snapshots

`data/historical_original_note_source_manifest.csv` and `notes/historical_source_snapshots/` preserve the earlier note provenance. Historical source-note matching establishes provenance; it does not by itself establish current-cycle reading or final synthesis membership.

## H1–H9 evaluation-protocol artifacts

### `docs/H1_H9_METRIC_SPECIFICATION.md`

Authoritative pre-experiment operational specification for the survey's extraction metric stack. It fixes record alignment, null/collection/nested-field handling, micro/macro aggregation, semantic-equivalence policy, provenance support, zero-output behavior, confidence intervals, the unsupported-value/non-schema split, and the worked-example scoring rules **before** the Reviewer-1 three-agent experiment.

### `schemas/evidence_object.schema.json`

JSON Schema for one field-level source-evidence object. It links a task/run/record/field claim to source identity, snapshot/retrieval timestamps, a representation-specific locator (DOM, text, or vision), and a replayable transformation history. The optional evaluator-populated verification object records availability `A(p)`, support `S(p)`, method, and reason. This schema supports H5 and the formal evidence-object requirement raised separately by Reviewer 1.

### `data/h9_worked_scoring_example.json`

Machine-readable synthetic wireless-headphones-style example used to verify H9 before the real experiment. It contains the declared schema, two gold records, three predicted records, the accepted alignment, raw score counts, final scores, and arithmetic derivations. It is **not** presented as an empirical model result.

### `docs/H1_H9_MANUSCRIPT_PATCH.md`

Exact LaTeX replacement/addition blocks for the current manuscript's Section 7.2 and statistical-reporting paragraph. The patch is kept separate because the current editable `sn-article.tex` is not stored in this evidence repository.

## Current frozen statistics

- Mapping corpus: **805**
- Publication-eligible pool: **454**
- Historical normalized-note/candidate set: **403**
- Final qualitative synthesis: **385**
- Deep P0/P1 analysis in final synthesis: **114**
- Structured P2/P3 reading in final synthesis: **271**
- Published final-synthesis studies: **377**
- Accepted final-synthesis studies: **8**
