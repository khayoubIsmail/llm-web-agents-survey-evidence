# Data Dictionary

Field definitions for all columns in `data/studies_805_mapping_corpus.{csv,json}`,  
`data/studies_403_published_accepted_pool.{csv,json}`, and  
`data/records_excluded_from_strict_pool.{csv,json}`.

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
