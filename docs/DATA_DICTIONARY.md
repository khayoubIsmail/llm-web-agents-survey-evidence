# Data Dictionary

| Field | Meaning |
|---|---|
| `record_id` | Stable identifier in the reconciled 805-study corpus. |
| `section` | Primary thematic section assigned during mapping. |
| `priority` | Evidence-use tier: P0 cornerstone, P1 primary, P2 supporting/extending, P3 peripheral/historical/recency context. It is not a risk-of-bias score. |
| `year` | Canonical publication year after verification. |
| `title` | Canonical study title. |
| `publication_status` | Published, accepted, preprint, workshop-only, unconfirmed, or corrected final status. |
| `status_category` | Normalized publication-status category. |
| `venue` | Canonical venue where verified. |
| `identifier` | DOI, OpenReview URL, arXiv identifier, or other canonical identifier. |
| `verification_source` | Source or audit used to confirm metadata/status. |
| `bibliography_eligibility` | Whether the record may enter the strict journal bibliography if it supports an actual manuscript claim. |
| `note_quality` | Internal evidence-note readiness grade. |
| `evidence_readiness` | Claim-use readiness after validation. |
| `pages` | Final page range when supplied by a validation patch. |
| `canonical_status_detail` | Full final status wording from the paper-specific validation. |
| `final_exclusion_reason` | Reason a record was removed from the strict published/accepted pool. |
