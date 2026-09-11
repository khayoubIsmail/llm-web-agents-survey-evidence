# A1 — Copy-Ready Manuscript and Reviewer-Response Text

## Where to update the manuscript

Insert the following subsection in the **Methods / Review Methodology** section, immediately after the eligibility-screening description and before thematic coding or synthesis. Replace any sentence saying that P2/P3 studies received only “rapid targeted reading.”

## Manuscript insertion

### Full-text assessment, priority classification, and evidence notes

Each candidate study underwent a full-text assessment used jointly for eligibility and priority classification. Classification considered the study's fit with the review questions, the directness of its contribution to Web/GUI agents or enabling agent methods, the type of evidence it could contribute, and its publication status. P0 denoted cornerstone studies defining the scope or core methods; P1 denoted direct evidence for central architectures, methods, benchmarks, empirical results, or risk claims; P2 denoted supporting or extending evidence; P3 denoted historical or contextual evidence that remained within scope; and P4 denoted peripheral or out-of-scope studies. P4 studies were excluded from the final synthesis, leaving a 403-record P0–P3 survey register.

All accessible studies in this 403-record register were read in full at a tier-appropriate depth. P0/P1 studies received deep critical analysis and detailed notes covering methods, evaluation, results, limitations, evidentiary role, and relevance to the review. P2/P3 studies received complete full-text reading with lighter structured analysis focused on relevance, methodology, results or concrete benchmark properties where applicable, contributions, and limitations. Priority therefore governed analytical depth and evidence use; it was not a risk-of-bias or publication-quality score.

Following reviewer feedback, we performed a paper-by-paper audit of the live evidence notes rather than treating historical source-note matches as proof of completed reading. Notes containing prospective language such as “When reading this paper, extract…” or lacking current-cycle full-text verification were classified as unresolved and remediated against complete paper sources. The final generated audit covers all 403 live notes and contains zero prospective reading TODOs, zero generic evidence-template blocks, and zero accessible records without current-cycle full-text verification. Full-text analysis/verification is documented for all 402 accessible records. One P3 study (record 249) remains the sole full-text access exception after renewed publisher, bibliographic, repository, preprint, and exact-title searches; it is retained for traceability but blocked from claim-level synthesis and is not represented as fully read.

For traceability, the repository exposes one normalized live note and one generated paper-specific synthesis-source record for every register ID (403 + 403 files). Exact historical provenance is preserved separately: 335 reliable historical mappings resolve to 229 historical Markdown snapshots because some source files were merged multi-paper syntheses. These historical files are retained as provenance only and are not used as substitutes for current-cycle full-text verification.

## Shorter manuscript version if space is limited

Candidate studies underwent full-text assessment for both eligibility and P0–P4 priority classification. P4 studies were excluded as peripheral or out of scope; the survey register contains 403 P0–P3 records. All accessible included studies were read in full at tier-appropriate depth: P0/P1 studies received deep critical analysis and detailed notes, whereas P2/P3 studies received complete full-text reading with lighter structured analysis of relevance, methods, results or benchmark properties, contributions, and limitations. Following reviewer feedback, we audited all 403 live notes paper by paper and replaced prospective/template evidence blocks only after checking the underlying papers. The final generated audit reports zero reading TODOs, zero generic template blocks, and zero accessible records without current-cycle verification. Full-text analysis is documented for 402 accessible studies; record 249 remains the sole full-text access exception and is blocked from claim-level synthesis pending a complete copy.

## Response to reviewer A1

Thank you for identifying that our earlier description of the reading process and its evidence trail was ambiguous. We have removed the phrase “rapid targeted reading,” which could incorrectly suggest that P2/P3 studies were assessed only from abstracts or selected sections. We now clarify that full-text assessment was used for eligibility and P0–P4 priority classification. P0/P1 studies received full-text reading with deep critical analysis and detailed notes, while P2/P3 studies received complete full-text reading with a lighter structured analysis focused on relevance, methodology, results or concrete benchmark properties, contributions, and limitations. Priority therefore determines analytical depth and evidence use, not whether a paper is read in full.

We also re-audited the evidence repository paper by paper because the previous repository state contained historical notes that still included prospective phrases such as “When reading this paper, extract…” or were marked as lacking a current-cycle PDF verification. We did not treat file existence or historical source matching as evidence of completed reading. A record was removed from the remediation queue only after paper-specific evidence had been checked against a complete paper source and the live note had been replaced or confirmed at the required tier-specific depth.

The final reviewer-facing audit now covers all 403 live notes and reports **0 prospective reading TODOs, 0 generic evidence-template blocks, 0 accessible records without current-cycle full-text verification, and 0 records remaining in the A1 remediation queue**. Full-text analysis/verification is documented for **402 accessible records**. The only full-text access exception is **record 249**, for which a complete verifiable manuscript could not be obtained despite renewed publisher, bibliographic, repository, preprint, author-page, and exact-title searches. We retained this record for traceability but blocked it from claim-level synthesis rather than reconstructing its evidence from metadata or code.

For auditability, the repository contains exactly one normalized live note and one generated paper-specific synthesis-source record for every register ID (`notes/papers/`: 403; `notes/original_sources/`: 403). The exact historical note archive remains available separately: 335 reliable historical source-note mappings resolve to 229 unique historical Markdown files because some original files covered multiple papers. The repository also exposes the final 403-row live-note audit, explicit full-text recheck ledger, paper-specific remediation evidence batches, and the documented access exception.

Repository: <https://github.com/khayoubIsmail/llm-web-agents-survey-evidence>

## Repository evidence to cite in the response letter

- `data/a1_live_note_audit_summary.json` — final aggregate A1 closure check.
- `data/a1_live_note_audit.csv` — one final A1 audit row per included paper.
- `data/a1_fulltext_rechecks.csv` — explicit current-cycle reread/reverification ledger.
- `data/a1_evidence_batches/` — paper-grounded evidence used to replace incomplete/template notes.
- `data/paper_note_audit.csv` — one audit row per paper, including provenance, full-text status, and claim-use status.
- `notes/papers/` — 403 normalized live notes, one per register record.
- `notes/original_sources/` — 403 generated paper-specific synthesis-source records, one per register record.
- `notes/historical_source_snapshots/` — 229 exact historical source-note files retained for provenance.
- `data/historical_original_note_source_manifest.csv` — frozen mapping for the 335 historical mappings / 229 snapshots.
- `docs/METHODOLOGY_AND_VERSIONING.md` — classification, reading-depth protocol, A1 audit rule, and closure state.
- `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md` — record 249 retrieval attempts and synthesis restriction.

## Important separate bibliographic note

A1 concerns reading/evidence completeness. During the paper rereads, records **323** and **419** were successfully read from complete available versions but their archival-published/formally-accepted status could not be revalidated with the same confidence as their reading evidence. They are therefore separately blocked from claim-level use pending publication-status revalidation. They are **not** full-text access exceptions and do not change the A1 closure counts, but their citation-eligibility status should be resolved before the final manuscript/citation-pool freeze.

## Final consistency check before submission

Use these A1 counts consistently in the manuscript, response letter, supplementary files, and repository:

- **403** live included/register records audited;
- **402** accessible records with documented current-cycle full-text analysis/verification;
- **1** full-text access exception: record **249**;
- **0** live `When reading this paper...` TODOs;
- **0** generic evidence-template blocks;
- **0** accessible records without current-cycle full-text verification;
- **0** records remaining in the A1 full-text remediation queue;
- **403** normalized live notes and **403** generated paper-specific synthesis-source records;
- historical provenance: **335** reliable historical mappings resolving to **229** unique historical source files.

Do **not** state that all 403 papers were read in full unless record 249 is later obtained and analyzed. The defensible wording is: **all 402 accessible included records have documented full-text analysis/verification; one record remains an explicit access exception and is blocked from claim-level synthesis.**
