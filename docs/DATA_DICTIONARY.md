# Data Dictionary

Field definitions for the corpus registers and paper-note audit files.

---

| Field | Type | Meaning |
|---|---|---|
| `record_id` | integer | Stable identifier in the reconciled 805-study corpus. IDs are unique and do not change between versions of this release. |
| `section` | string | Primary thematic section assigned during mapping (e.g., "Web Automation", "Data Extraction", "Agent Architectures"). |
| `priority` | string | Evidence-use tier assigned by the authors. **P0** = cornerstone (directly defines scope or method); **P1** = primary (cited for a specific empirical claim); **P2** = supporting/extending (cited for context or comparison); **P3** = peripheral, historical, or recency context. This is **not** a risk-of-bias score. |
| `year` | integer | Canonical publication year after verification. For preprints without an accepted version, this is the earliest public release year. |
| `title` | string | Canonical study title, normalized for consistency. |
| `publication_status` | string | Full verified status: `published`, `accepted`, `preprint`, `workshop-only`, `unconfirmed`, or a corrected final status after audit. |
| `status_category` | string | Normalized category used for summary statistics: `Archival published`, `Preprint/technical report`, `Workshop/conditional`, `Archival accepted`, or `Unconfirmed/other`. |
| `venue` | string | Canonical venue name where the work is published or accepted, verified against official sources where possible. |
| `identifier` | string | Primary canonical identifier: DOI, OpenReview URL, arXiv identifier (e.g., `arXiv:2301.00001`), or another persistent identifier. |
| `verification_source` | string | Source or audit log used to confirm the metadata and publication status (e.g., "OpenReview", "ACM DL", "Semantic Scholar", "Author verification"). |
| `bibliography_eligibility` | boolean | Whether the record is eligible to enter the strict 403-study published/accepted pool and may be cited as a direct empirical claim in the manuscript. `true` = eligible; `false` = excluded. |
| `note_quality` | string | Internal evidence-note readiness grade, indicating how thoroughly claim-level notes were extracted for this study. |
| `evidence_readiness` | string | Overall claim-use readiness after validation, combining publication status and note quality. |
| `pages` | string | Final page range when supplied by a publication validation patch. Empty for preprints. |
| `canonical_status_detail` | string | Full, verbatim final status wording from the study-specific validation record, including any corrections applied after the initial screening round. |
| `final_exclusion_reason` | string | If `bibliography_eligibility` is `false`, the reason the record was removed from the strict published/accepted pool (e.g., "Status unconfirmed after verification"). Empty for eligible records. |

---

## Priority tier summary

| Tier | Corpus intent | Count in 805 | Count in 403 |
|---|---|---|---|
| P0 | Cornerstone — defines scope, methodology, or core framework | 20 | 18 |
| P1 | Primary — cited for a specific claim | 179 | 98 |
| P2 | Supporting / extending — context or comparison | 444 | 204 |
| P3 | Peripheral / historical / recency context | 162 | 83 |

## `data/paper_note_audit.csv`

| Field | Meaning |
|---|---|
| `record_id` | Stable ID linking the note audit to the 403-paper register. |
| `title`, `section`, `priority` | Canonical register metadata copied for human auditability. |
| `initial_note_quality` | Readiness label present in the register before this remediation cycle. |
| `audit_computed_source_quality` | Heuristic coverage grade for the matched source-note segment; it is a triage aid, not a scholarly quality score. |
| `source_match_score` | Normalized title-similarity score for the selected source note. |
| `original_note_source` | Source-archive path selected by title audit, or an explicit no-reliable-match label. |
| `content_provenance` | Whether the final note preserves an audited source note, is a current-cycle remediation, or is an access-exception note. |
| `note_file` | Path to the normalized paper-specific Markdown note. |
| `full_text_status` | Distinguishes current-cycle PDF verification, retained archive evidence, and blocked access. |
| `full_text_basis` | Human-readable verification basis, including page count/hash for current-cycle PDFs. |
| `pdf_pages`, `pdf_sha256`, `title_similarity` | Current-cycle full-text verification fields; blank when no PDF was rechecked in this cycle. |
| `review_standard` | Tier-specific required reading/analysis depth. |
| `claim_use_status` | Whether the note may support synthesis or remains blocked pending full text. |

## `data/note_remediation_log.csv`

| Field | Meaning |
|---|---|
| `record_id`, `title`, `priority` | Register identity and tier. |
| `initial_note_quality` | Original readiness label in the 403-paper register. |
| `audit_computed_quality` | Coverage grade of the best source-note match before the final note was materialized. |
| `reason` | Why the record was selected for note creation or replacement. |
| `action` | Remediation performed in the current cycle. |

## `data/note_source_overrides.csv`

Manual corrections for title variants or duplicate-stub cases where automatic matching did not select the best substantive note. `source_path` is relative to the supplied review archive; `reason` records the adjudication basis.

## `data/original_note_source_manifest.csv`

One row per register record with a reliable original note-source match. Because
some historical files contain notes for multiple papers, the 335 rows resolve to
229 unique Markdown files.

| Field | Meaning |
|---|---|
| `record_id`, `title`, `priority` | Register identity and evidence tier. |
| `final_note` | Canonical normalized note in `notes/papers/`. |
| `original_source` | Path recorded in the supplied historical review archive. |
| `repository_source` | Preserved source snapshot under `notes/original_sources/`. |
| `source_sha256` | SHA-256 digest of the exact exported source bytes. |
| `source_bytes`, `source_lines` | File size and line count of the preserved source. |
| `records_mapped_to_source` | Number of register records linked to the same historical file. |
| `source_layout` | `standalone` for a one-record source or `shared/merged` for a multi-record source. |
