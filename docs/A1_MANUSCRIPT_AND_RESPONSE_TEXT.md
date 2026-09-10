# A1 — Copy-Ready Manuscript and Reviewer-Response Text

## Where to update the manuscript

Insert the following subsection in the **Methods / Review Methodology** section, immediately after the eligibility-screening description and before thematic coding or synthesis. Replace any sentence saying that P2/P3 studies received only “rapid targeted reading.”

## Manuscript insertion

### Full-text assessment, priority classification, and evidence notes

Each candidate study underwent an initial full-text assessment used jointly for eligibility and priority classification. Classification considered the study's fit with the review questions, the directness of its contribution to Web/GUI agents or enabling agent methods, the type of evidence it could contribute, and its publication status. P0 denoted cornerstone studies defining the scope or core methods; P1 denoted direct evidence for central architectures, methods, benchmarks, empirical results, or risk claims; P2 denoted supporting or extending evidence; P3 denoted historical or contextual evidence that remained within scope; and P4 denoted peripheral or out-of-scope studies. P4 studies were excluded from the final synthesis, leaving 403 published or accepted P0–P3 studies.

All accessible studies in this 403-paper pool were then read in full at a tier-appropriate depth. P0/P1 studies received deep critical analysis and detailed notes covering methods, evaluation, results, limitations, evidentiary role, and relevance to the review. P2/P3 studies received complete full-text reading with a lighter structured analysis focused on relevance, methodology, results, contributions, and limitations. Priority therefore governed analytical depth and evidence use; it was not a risk-of-bias or publication-quality score.

To verify the evidence trail, we audited the existing notes against all 403 register records and materialized two one-to-one paper-specific layers: 403 normalized synthesis notes in `notes/papers/` and 403 paper-specific synthesis-source records in `notes/original_sources/`, both keyed by the same stable record IDs. The historical audit found 335 reliable source-note mappings resolving to 229 unique historical Markdown files because some historical documents were merged multi-paper syntheses; those exact snapshots are retained separately for provenance. Sixty-eight records had no reliable historical paper-specific source match and were selected for remediation rather than being assigned invented sources. The consolidated record documents full-text analysis for 402 studies: 134 source PDFs were independently retrieved, extracted, hashed, and title-checked during the remediation audit, while 268 substantive paper-specific notes were retained from the prior review archive after title and coverage checking. One P3 study (record 249) remains inaccessible after renewed publisher, bibliographic, repository, and exact-title searches. It is retained for traceability but is explicitly blocked from claim-level synthesis and is not represented as fully read.

## Shorter manuscript version if space is limited

Candidate studies underwent an initial full-text assessment used for both eligibility and P0–P4 priority classification. P4 studies were excluded as peripheral or out of scope; the final published/accepted pool contains 403 P0–P3 studies. All accessible included studies were then read in full: P0/P1 studies received deep critical analysis and detailed notes, whereas P2/P3 studies received complete full-text reading with lighter structured analysis of relevance, methods, results, contributions, and limitations. We audited the evidence trail and materialized one normalized note and one paper-specific synthesis-source record for every one of the 403 register IDs. Full-text analysis is documented for 402 studies; record 249 remains the sole access exception and is blocked from claim-level synthesis pending a complete copy.

## Response to reviewer A1

Thank you for identifying that our earlier description of the reading process was ambiguous. We have removed the phrase “rapid targeted reading,” which could incorrectly suggest that P2/P3 studies were assessed only from abstracts or selected sections. We now clarify that every candidate first underwent an initial full-text assessment used jointly for eligibility and P0–P4 priority classification, and we explicitly define the classification criteria. P4 studies were excluded as peripheral or out of scope; the final 403-study published/accepted pool consists of P0–P3 records.

We also clarify the second-stage reading protocol. P0/P1 studies received full-text reading with deep critical analysis and detailed notes, while P2/P3 studies received complete full-text reading with a lighter structured analysis focused on relevance, methodology, results, contributions, and limitations. Thus, priority determined analytical depth and intended evidence use, not whether the paper was read in full.

In response to the comment, we audited the evidence notes against all 403 included records. The audit identified 335 reliable historical source-note mappings; because some original documents were merged syntheses, those mappings resolved to 229 unique historical Markdown files. Sixty-eight records had no reliable historical paper-specific source match. After manual review, 71 notes were created or replaced in total—the 68 no-match records plus three additional records selected for deeper priority-adjusted remediation. We now expose exactly one normalized note and one paper-specific synthesis-source record for every included register ID (403 + 403 files). The exact historical source snapshots remain preserved separately for provenance.

During the remediation cycle, 134 source PDFs were independently retrieved, extracted, hashed, and title-checked; 268 substantive paper-specific notes were retained from the prior review archive after title and coverage auditing. We have also made one access limitation explicit rather than overstating the evidence: the complete full text of record 249 could not be obtained despite renewed checks. It remains in the eligibility register for traceability but is blocked from claim-level synthesis and is not described as fully read.

Repository: <https://github.com/khayoubIsmail/llm-web-agents-survey-evidence>

## Repository evidence to cite in the response letter

- `notes/papers/` — 403 normalized notes, one per register record.
- `notes/original_sources/` — 403 paper-specific synthesis-source records, one per register record.
- `notes/historical_source_snapshots/` — exact historical source-note snapshots retained for provenance.
- `data/paper_note_audit.csv` — one audit row per paper, including provenance, full-text status, and claim-use status.
- `data/note_remediation_log.csv` — the 71 notes created or replaced during the audit.
- `data/note_source_overrides.csv` — manually adjudicated title/source matches.
- `data/historical_original_note_source_manifest.csv` — frozen mapping for the 335 historical mappings / 229 snapshots.
- `docs/PAPER_SYNTHESIS_SOURCES.md` — explanation of the 403-file paper-specific source layer and its relation to historical provenance.
- `docs/METHODOLOGY_AND_VERSIONING.md` — classification and reading-depth protocol.
- `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md` — record 249 retrieval attempts and synthesis restriction.

## Final consistency check before submission

Use the same counts everywhere in the manuscript, response letter, supplementary files, and repository: **403 included records; 403 normalized notes; 403 paper-specific synthesis-source records; 402 with documented full-text analysis; 335 reliable historical source mappings resolving to 229 historical source files; 71 remediated notes; 134 current-cycle PDF checks; 268 retained substantive archive notes; one access exception (record 249).** Do not state that all 403 were read in full unless record 249 is obtained and analyzed before resubmission.
