# A1 — Copy-Ready Manuscript and Reviewer-Response Text

## Where to update the manuscript

Insert the following subsection in the **Methods / Review Methodology** section, immediately after the eligibility-screening description and before thematic coding or synthesis. Replace any sentence saying that P2/P3 studies received only “rapid targeted reading.”

## Manuscript insertion

### Full-text assessment, priority classification, and evidence notes

Each candidate study underwent an initial full-text assessment used jointly for eligibility and priority classification. Classification considered the study's fit with the review questions, the directness of its contribution to Web/GUI agents or enabling agent methods, the type of evidence it could contribute, and its publication status. P0 denoted cornerstone studies defining the scope or core methods; P1 denoted direct evidence for central architectures, methods, benchmarks, empirical results, or risk claims; P2 denoted supporting or extending evidence; P3 denoted historical or contextual evidence that remained within scope; and P4 denoted peripheral or out-of-scope studies. P4 studies were excluded from the final synthesis, leaving 403 published or accepted P0–P3 studies.

All accessible studies in this 403-paper pool were then read in full at a tier-appropriate depth. P0/P1 studies received deep critical analysis and detailed notes covering methods, evaluation, results, limitations, evidentiary role, and relevance to the review. P2/P3 studies received complete full-text reading with a lighter structured analysis focused on relevance, methodology, results, contributions, and limitations. Priority therefore governed analytical depth and evidence use; it was not a risk-of-bias or publication-quality score.

To verify the evidence trail, we audited the existing notes against all 403 register records and materialized one normalized paper-specific note per record in the companion repository. The consolidated record documents full-text analysis for 402 studies: 134 source PDFs were independently retrieved, extracted, hashed, and title-checked during the remediation audit, and 268 substantive paper-specific notes were retained from the prior review archive after title and coverage checking. One P3 study (record 249) remained inaccessible after publisher and exact-title searches. It is retained in the publication-eligible register for traceability but is explicitly blocked from claim-level synthesis and is not represented as fully read. The per-paper notes, provenance audit, remediation log, and access-exception record are available in the companion evidence repository.

## Shorter manuscript version if space is limited

Candidate studies underwent an initial full-text assessment used for both eligibility and P0–P4 priority classification. P4 studies were excluded as peripheral or out of scope; the final published/accepted pool contains 403 P0–P3 studies. All accessible included studies were then read in full: P0/P1 studies received deep critical analysis and detailed notes, whereas P2/P3 studies received complete full-text reading with lighter structured analysis of relevance, methods, results, contributions, and limitations. We audited and normalized one paper-specific note for every register record. Full-text analysis is documented for 402 studies; one P3 record remained inaccessible and was retained only for traceability, with claim-level use blocked pending a complete copy. The note provenance and access decision are documented in the companion repository.

## Response to reviewer A1

Thank you for identifying that our earlier description of the reading process was ambiguous. We have replaced the phrase “rapid targeted reading” because it could incorrectly suggest that P2/P3 studies were assessed only from abstracts or selected sections. We now clarify that every candidate first underwent an initial full-text assessment used jointly for eligibility and P0–P4 priority classification. The classification criteria are now explicitly defined. P4 studies were excluded as peripheral or out of scope, and the final 403-study published/accepted pool consists of P0–P3 records.

We also clarify the second-stage reading protocol. P0/P1 studies received full-text reading with deep critical analysis and detailed notes, while P2/P3 studies received complete full-text reading with a lighter structured analysis focused on relevance, methodology, results, contributions, and limitations. Thus, priority determined the depth and intended evidence use, not whether the paper was read in full.

In response to the comment, we additionally audited the evidence notes against all 403 included records. Automated title matching located 335 reliable paper-specific source notes; 68 records had no reliable source-note match. After manual review, we created or replaced 71 notes in total—the 68 unmatched records plus three additional records selected for deeper priority-adjusted remediation—and materialized exactly one normalized Markdown note for every included record. During this remediation cycle, 134 source PDFs were independently retrieved, extracted, hashed, and title-checked; 268 substantive paper-specific notes were retained from the prior review archive after title and coverage auditing.

We have also made one access limitation explicit rather than overstating the evidence. The full text of record 249 could not be obtained from the publisher endpoint or through exact-title and preprint searches. This published P3 record remains in the eligibility register for traceability but is blocked from claim-level synthesis and is not described as fully read. The revised methodology, 403 paper notes, per-record provenance audit, remediation log, and access-exception record are available in the companion repository: <https://github.com/khayoubIsmail/llm-web-agents-survey-evidence>.

## Repository evidence to cite in the response letter

- `notes/papers/` — one normalized note for each of the 403 records.
- `data/paper_note_audit.csv` — one audit row per paper, including provenance, full-text status, and claim-use status.
- `data/note_remediation_log.csv` — the 71 notes created or replaced during the audit.
- `data/note_source_overrides.csv` — manually adjudicated title/source matches.
- `docs/METHODOLOGY_AND_VERSIONING.md` — classification and reading-depth protocol.
- `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md` — record 249 retrieval attempts and synthesis restriction.

## Final consistency check before submission

Use the same counts everywhere in the manuscript, response letter, supplementary files, and repository: **403 included records; 402 with documented full-text analysis; 71 remediated notes; 134 current-cycle PDF checks; 268 retained substantive archive notes; one access exception (record 249).** Do not state that all 403 were read in full unless record 249 is obtained and analyzed before resubmission.
