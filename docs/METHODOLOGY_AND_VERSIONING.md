# Methodology and Versioning

## Corpus construction pipeline

| Stage | Description | Count |
|---|---|---|
| 1 | Identification ledger (author-approved records) | 3,462 |
| 2 | After normalization and deduplication | 3,455 |
| 3 | Excluded during screening / eligibility | 2,643 |
| 4 | Provisional inclusions | 812 |
| 5 | Post-inclusion reconciliation (six duplicate study representations and one non-study template artifact removed) | −7 |
| 6 | **Final systematic-mapping corpus** | **805** |
| 7 | **Published / accepted citation-eligibility layer** | **403** |
| 8 | Strict pool exclusions after final validation | 3 |

## Full-text assessment and priority classification

Candidate papers underwent an **initial full-text assessment used for eligibility and priority classification**. The classification was not based on titles or abstracts alone and was not merely a decision about reading priority. Each paper was assessed against the survey scope and research questions, the directness of its contribution to web/GUI agents or enabling agent methods, the type and strength of evidence it could contribute, and whether it met the publication-status rule for the final synthesis.

| Tier | Predefined classification criterion | Synthesis treatment |
|---|---|---|
| P0 | Cornerstone work that defines the survey scope, core method, or indispensable conceptual foundation | Included; deep critical analysis and detailed notes |
| P1 | Direct evidence for a central architecture, method, benchmark, empirical result, or risk claim | Included; deep critical analysis and detailed notes |
| P2 | Supporting or extending evidence that materially informs a comparison, component, or adjacent design choice | Included; complete full-text reading with lighter structured analysis |
| P3 | Historical, contextual, or peripheral-but-relevant evidence within the survey boundary | Included; complete full-text reading with lighter structured analysis |
| P4 | Peripheral to the research questions, out of scope, or insufficiently connected to the intended synthesis | Excluded from the final synthesis |

The final 403-paper published/accepted pool therefore consists only of P0–P3 records. Priority is an evidence-use and reading-depth classification, not a risk-of-bias score and not a publication-quality ranking.

## Reading depth and structured notes

All accessible papers in the 403-paper pool were subject to complete full-text reading at a tier-appropriate depth:

- **P0/P1:** full-text reading plus deep critical analysis, detailed methods/results notes, limitations, evidentiary role, and relevance to the survey.
- **P2/P3:** full-text reading plus a lighter structured analysis of relevance, methodology, results, contributions, and limitations.

The consolidated evidence record documents full-text analysis for 402 papers. One included record (249) remains inaccessible after publisher and exact-title searches. It is retained in the publication-eligible register for traceability but is blocked from claim-level synthesis; it is not represented as fully read. Details are recorded in `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`.

**Ismail Khayoub** and **Firdaous Ait Mohamed** conducted and cross-checked screening, eligibility assessment, thematic coding, evidence extraction, and synthesis. **Mohamed-Amine Chadi** and **Hajar Mousannif** performed final analytical verification and audit of the priority assignments, status categories, and strict exclusion decisions.

## Paper-note remediation audit

The supplied review archive contained 1,522 Markdown files, including individual notes, merged section notes, duplicate stubs, and verification reports. The remediation audit used normalized title matching to locate candidate source notes, followed by manual overrides for verified title variants and duplicate-stub cases. Automated matching was used as triage, not as evidence that a note was substantively complete.

| Audit result | Count |
|---|---:|
| Included register records checked | 403 |
| Reliable paper-specific source-note matches | 335 |
| Records without a reliable source-note match | 68 |
| Notes created or replaced after manual review | 71 |
| Normalized final paper-note files | 403 |
| PDFs independently retrieved/extracted/title-checked in this remediation cycle | 134 |
| Substantive notes retained from the supplied archive without a new PDF check | 268 |
| Unresolved full-text access exceptions | 1 |

The 71 remediations comprise the 68 no-match records plus three matched records selected for deeper priority-adjusted remediation after manual inspection. Current-cycle PDFs are not committed; the audit records extracted page counts, SHA-256 hashes, and title similarity in local working data, while `data/paper_note_audit.csv` retains the provenance and verification status needed to distinguish current rechecks from archived review evidence.

## Historical source-note preservation

The 335 reliable source-note mappings resolve to 229 unique historical Markdown files. Twenty are shared or merged source documents covering 126 mapped records; the remaining source files map to one register record each. The files are preserved byte-for-byte under `notes/original_sources/`, including complete merged documents rather than reconstructed fragments. `data/original_note_source_manifest.csv` maps every sourced record to its canonical final note and historical snapshot and records the snapshot's byte count, line count, layout, and SHA-256 digest.

These historical snapshots provide provenance but are not the canonical synthesis corpus. The one-record-per-file notes in `notes/papers/` remain authoritative. A preserved merged file may contain batch-level synthesis or additional historical entries; their presence does not add records to the 403-paper register or authorize claim-level use. A historical source file also does not imply that its paper was independently re-downloaded in the current cycle; the current-cycle, retained-archive, and blocked-access statuses remain those recorded in `data/paper_note_audit.csv`. No historical source is fabricated for the 68 records without a reliable match.

## Publication-status verification

All 403 records in the published/accepted pool were individually verified against at least one canonical source (ACM DL, IEEE Xplore, Springer, OpenReview, Semantic Scholar, or direct author confirmation). Three records (IDs: 432, 656, 686) could not be confirmed as archival-published or formally accepted and were retained in the 805-study mapping corpus but excluded from the strict citation-eligibility pool.

## Version policy

- **Canonical published metadata supersedes preprint metadata.** Where a journal or conference version exists, the canonical title, venue, year, and identifiers from that version are used.
- **Preprints and non-archival workshop papers** remain visible in the 805-study mapping file but are excluded from the strict evidence pool unless a final published or formally accepted version is verified.
- **Record IDs are stable.** Existing IDs will not be reassigned in future patch releases. New studies may receive new IDs appended to the corpus.
- **Patch releases** document bibliographic corrections in the commit log. Major changes to scope or methodology will increment the version number.

## Validation audit (v1.1.1)

| Check | Result |
|---|---|
| 805-study corpus — unique record IDs | ✅ Verified, no duplicates |
| 403-pool — fully contained within 805-study corpus | ✅ Verified |
| Strict exclusion count | ✅ Exactly 3 (records 432, 656, 686) |
| CSV ↔ JSON identifier agreement | ✅ All IDs match |
| SHA-256 checksums for all data files | ✅ All pass |
| One normalized note per 403-pool record | ✅ 403 files; no missing or extra IDs |
| Historical source-note archive | ✅ 229 exact files mapped to 335 records; SHA-256 verified |
| Access exceptions prevented from claim-level use | ✅ Record 249 explicitly blocked |
