# Data Dictionary

Field definitions for the corpus registers and paper-note audit files.

---

| Field | Type | Meaning |
|---|---|---|
| `record_id` | integer | Stable identifier in the reconciled 805-study corpus. |
| `section` | string | Primary thematic section assigned during mapping. |
| `priority` | string | Evidence-use tier: P0 cornerstone, P1 primary, P2 supporting/extending, P3 contextual/historical. Not a risk-of-bias score. |
| `year` | integer | Canonical publication year after verification. |
| `title` | string | Canonical study title, normalized for consistency. |
| `publication_status` | string | Full verified publication status. |
| `status_category` | string | Normalized publication-status category used in summary statistics. |
| `venue` | string | Canonical publication venue. |
| `identifier` | string | DOI, OpenReview URL, arXiv identifier, or other canonical persistent identifier. |
| `verification_source` | string | Source/audit trail used to confirm metadata and publication status. |
| `bibliography_eligibility` | boolean | Whether the record enters the strict 403-study published/accepted citation layer. |
| `note_quality` | string | Internal evidence-note readiness grade. |
| `evidence_readiness` | string | Overall claim-use readiness after validation. |
| `pages` | string | Final page range where available. |
| `canonical_status_detail` | string | Detailed final status wording from study-specific validation. |
| `final_exclusion_reason` | string | Reason a record was removed from the strict citation pool; empty for eligible records. |

## Priority tier summary

| Tier | Corpus intent | Count in 805 | Count in 403 |
|---|---|---:|---:|
| P0 | Cornerstone | 20 | 18 |
| P1 | Primary | 179 | 98 |
| P2 | Supporting / extending | 444 | 204 |
| P3 | Contextual / historical | 162 | 83 |

## `data/paper_note_audit.csv`

| Field | Meaning |
|---|---|
| `record_id` | Stable ID linking the note audit to the 403-paper register. |
| `title`, `section`, `priority` | Canonical register metadata. |
| `initial_note_quality` | Readiness label present before remediation. |
| `audit_computed_source_quality` | Heuristic coverage grade for the matched historical source-note segment. |
| `source_match_score` | Normalized title-similarity score for the selected historical source note. |
| `original_note_source` | Historical review-archive path selected by the title audit, or an explicit no-reliable-match label. Historical paths are provenance identifiers and may refer to the frozen September 9 snapshot release. |
| `content_provenance` | Whether the final note preserves audited archive evidence, is a current-cycle remediation, or is an access-exception record. |
| `note_file` | Canonical normalized paper-specific Markdown note under `notes/papers/`. The same basename identifies its paper-specific synthesis-source record under `notes/original_sources/`. |
| `full_text_status` | Distinguishes current-cycle PDF verification, retained archive evidence, and blocked access. |
| `full_text_basis` | Human-readable verification basis, including page count/hash for current-cycle PDFs. |
| `pdf_pages`, `pdf_sha256`, `title_similarity` | Current-cycle full-text verification fields; blank when no PDF was rechecked in this cycle. |
| `review_standard` | Tier-specific required reading/analysis depth. |
| `claim_use_status` | Whether the note may support synthesis or remains blocked pending full text. |

## `notes/papers/` and `notes/original_sources/`

Both directories contain **403 files keyed by the same record-ID basename**. `notes/papers/<id>.md` is the canonical normalized note. `notes/original_sources/<id>.md` is the one-paper-per-file detailed synthesis-source record for that same paper. See `docs/PAPER_SYNTHESIS_SOURCES.md` for provenance semantics and the record-249 exception.

## `data/note_remediation_log.csv`

| Field | Meaning |
|---|---|
| `record_id`, `title`, `priority` | Register identity and tier. |
| `initial_note_quality` | Original readiness label. |
| `audit_computed_quality` | Coverage grade of the best historical source-note match before remediation. |
| `reason` | Why the record was selected for note creation or replacement. |
| `action` | Remediation performed in the current cycle. |

## `data/note_source_overrides.csv`

Manual corrections for title variants or duplicate-stub cases where automatic matching did not select the best substantive historical note. `source_path` is relative to the supplied review archive; `reason` records the adjudication basis.

## `data/historical_original_note_source_manifest.csv`

Frozen record-level manifest for the **335 reliable historical source-note mappings** from the September 9 provenance release. Those mappings resolve to **229 unique historical Markdown files**, including 20 shared/merged files covering multiple records. The exact snapshots are retained under `notes/historical_source_snapshots/` and in commit `83aca98913e2202d912778917ff7c5b92ff67399`.

The manifest's `repository_source` values describe the paths as they existed in that frozen provenance release. In release v1.2.0 the exact snapshot tree is separated from the new 403-file paper-specific source layer; do not interpret the historical path as a current `notes/original_sources/<id>.md` path.

| Field | Meaning |
|---|---|
| `record_id`, `title`, `priority` | Register identity and evidence tier. |
| `final_note` | Canonical normalized note in `notes/papers/`. |
| `original_source` | Path recorded in the supplied historical review archive. |
| `repository_source` | Path used by the frozen v1.1.1 provenance snapshot. |
| `source_sha256` | SHA-256 digest of the exact historical source bytes. |
| `source_bytes`, `source_lines` | Historical file size and line count. |
| `records_mapped_to_source` | Number of register records linked to the same historical file. |
| `source_layout` | `standalone` or `shared/merged`. |
