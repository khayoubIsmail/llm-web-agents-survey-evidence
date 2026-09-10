# Methodology and Versioning

## Corpus construction pipeline

| Stage | Description | Count |
|---|---|---:|
| 1 | Identification ledger (author-approved records) | 3,462 |
| 2 | After normalization and deduplication | 3,455 |
| 3 | Excluded during screening / eligibility | 2,643 |
| 4 | Provisional inclusions | 812 |
| 5 | Post-inclusion reconciliation (six duplicate study representations and one non-study template artifact removed) | −7 |
| 6 | **Final systematic-mapping corpus** | **805** |
| 7 | **Published / accepted citation-eligibility layer** | **403** |
| 8 | Strict pool exclusions after final validation | 3 |

## Full-text assessment and priority classification

Candidate papers underwent an **initial full-text assessment used for eligibility and priority classification**. Classification was not based on titles or abstracts alone. Each paper was assessed against the survey scope and research questions, the directness of its contribution to web/GUI agents or enabling agent methods, the type and strength of evidence it could contribute, and whether it met the publication-status rule for the final synthesis.

| Tier | Predefined classification criterion | Synthesis treatment |
|---|---|---|
| P0 | Cornerstone work defining the survey scope, core method, or indispensable conceptual foundation | Included; deep critical analysis and detailed notes |
| P1 | Direct evidence for a central architecture, method, benchmark, empirical result, or risk claim | Included; deep critical analysis and detailed notes |
| P2 | Supporting or extending evidence that materially informs a comparison, component, or adjacent design choice | Included; complete full-text reading with lighter structured analysis |
| P3 | Historical, contextual, or peripheral-but-relevant evidence within the survey boundary | Included; complete full-text reading with lighter structured analysis |
| P4 | Peripheral to the research questions, out of scope, or insufficiently connected to the intended synthesis | Excluded from the final synthesis |

The final 403-paper published/accepted pool therefore consists only of P0–P3 records. Priority is an evidence-use and reading-depth classification, not a risk-of-bias score or publication-quality ranking.

## Reading depth and structured notes

All accessible papers in the 403-paper pool were subject to complete full-text reading at a tier-appropriate depth:

- **P0/P1:** full-text reading plus deep critical analysis, detailed methods/results notes, limitations, evidentiary role, and relevance to the survey.
- **P2/P3:** full-text reading plus a lighter structured analysis of relevance, methodology, results, contributions, and limitations.

The consolidated evidence record documents full-text analysis for **402 papers**. One included record (249) remains inaccessible after publisher, bibliographic, author-repository, exact-title, DOI, and preprint searches. It is retained in the publication-eligible register for traceability but is blocked from claim-level synthesis and is not represented as fully read. Details are recorded in `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`.

**Ismail Khayoub** and **Firdaous Ait Mohamed** conducted and cross-checked screening, eligibility assessment, thematic coding, evidence extraction, and synthesis. **Mohamed-Amine Chadi** and **Hajar Mousannif** performed final analytical verification and audit of priority assignments, status categories, and strict exclusion decisions.

## Paper-note remediation audit

The supplied review archive contained 1,522 Markdown files, including individual notes, merged section notes, duplicate stubs, and verification reports. The remediation audit used normalized title matching to locate candidate source notes, followed by manual overrides for verified title variants and duplicate-stub cases. Automated matching was used as triage, not as evidence that a note was substantively complete.

| Audit result | Count |
|---|---:|
| Included register records checked | 403 |
| Reliable historical source-note mappings | 335 |
| Records without a reliable historical source-note match | 68 |
| Notes created or replaced after manual review | 71 |
| Normalized final paper-note files | 403 |
| Paper-specific synthesis-source files | 403 |
| PDFs independently retrieved/extracted/title-checked in this remediation cycle | 134 |
| Substantive notes retained from the supplied archive without a new PDF check | 268 |
| Unresolved full-text access exceptions | 1 |

The 71 remediations comprise the 68 no-match records plus three matched records selected for deeper priority-adjusted remediation after manual inspection. Current-cycle PDFs are not committed; the audit records extracted page counts, SHA-256 hashes, and title similarity, while `data/paper_note_audit.csv` distinguishes current rechecks, retained archive evidence, and blocked access.

## One-paper-per-file synthesis-source layer

Release v1.2.0 materializes a one-to-one paper-specific source layer under `notes/original_sources/`. It contains exactly **403 Markdown files for the 403 unique register IDs**, using the same record-ID filenames as `notes/papers/`.

For the 335 papers with reliable historical source-note mappings, the audit had already isolated/preserved the paper-specific analysis in the normalized note corpus even when the underlying historical source was a merged document. For the 68 papers without a reliable historical source match, remediation was based on independently retrieved and title-checked full text wherever accessible; record 249 is the sole exception and remains explicitly blocked rather than being assigned a fabricated full-text synthesis.

The paper-specific source files retain the detailed analysis and provenance metadata needed to trace each synthesis record. They are review artifacts, not copies of third-party PDFs.

## Historical source-note preservation

The 335 reliable historical mappings originally resolved to **229 unique historical Markdown files**. Twenty were shared/merged source documents covering 126 mapped records. Those exact files are preserved byte-for-byte under `notes/historical_source_snapshots/` and remain available in the immutable provenance release at commit `83aca98913e2202d912778917ff7c5b92ff67399`.

The frozen historical manifest is retained as `data/historical_original_note_source_manifest.csv`. Its source paths describe the September 9 provenance snapshot. Historical snapshots provide provenance but do not replace the authoritative paper-specific synthesis layer and do not imply a new PDF check.

See `docs/PAPER_SYNTHESIS_SOURCES.md` for the distinction between the 403 paper-specific synthesis-source records and the historical 229-file snapshot archive.

## Publication-status verification

All 403 records in the published/accepted pool were individually verified against canonical publication/status evidence. Three records (IDs 432, 656, 686) could not be confirmed as archival-published or formally accepted and were retained in the 805-study mapping corpus but excluded from the strict citation-eligibility pool.

## Version policy

- **Canonical published metadata supersedes preprint metadata.** Where a journal or conference version exists, the canonical title, venue, year, and identifiers from that version are used.
- **Preprints and non-archival workshop papers** remain visible in the 805-study mapping file but are excluded from the strict evidence pool unless a final published or formally accepted version is verified.
- **Record IDs are stable.** Existing IDs will not be reassigned in future patch releases.
- **Patch releases** document bibliographic corrections. Major evidence-structure or methodology changes increment the release version.

## Validation audit (v1.2.0)

| Check | Result |
|---|---|
| 805-study corpus — unique record IDs | ✅ Verified, no duplicates |
| 403-pool — fully contained within 805-study corpus | ✅ Verified |
| Strict exclusion count | ✅ Exactly 3 (432, 656, 686) |
| CSV ↔ JSON identifier agreement | ✅ All IDs match |
| One normalized note per 403-pool record | ✅ 403 files |
| One paper-specific synthesis source per 403-pool record | ✅ 403 files |
| Historical provenance snapshot | ✅ 229 exact files for 335 historical mappings |
| Current-cycle PDF checks | ✅ 134 records |
| Full-text analysis documented | ✅ 402 records |
| Access exceptions prevented from claim-level use | ✅ Record 249 explicitly blocked |
