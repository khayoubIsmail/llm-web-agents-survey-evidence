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
| 7 | **Citation-eligibility register used for the survey** | **403** |
| 8 | Strict pool exclusions after the earlier publication-status validation | 3 |

## Full-text assessment and priority classification

The review protocol uses full-text assessment for eligibility and priority classification. Classification is not based on titles or abstracts alone. Each study is assigned according to its fit with the survey scope and research questions, the directness of its contribution to web/GUI agents or enabling agent methods, the kind of evidence it can contribute, and its publication-status eligibility.

| Tier | Predefined classification criterion | Synthesis treatment |
|---|---|---|
| P0 | Cornerstone work defining the survey scope, core method, or indispensable conceptual foundation | Deep critical full-text analysis and detailed notes |
| P1 | Direct evidence for a central architecture, method, benchmark, empirical result, or risk claim | Deep critical full-text analysis and detailed notes |
| P2 | Supporting or extending evidence that materially informs a comparison, component, or adjacent design choice | Complete full-text reading with lighter structured analysis |
| P3 | Historical, contextual, or peripheral-but-relevant evidence within the survey boundary | Complete full-text reading with lighter structured analysis |
| P4 | Peripheral to the research questions, out of scope, or insufficiently connected to the intended synthesis | Excluded from final synthesis |

The 403-record survey register contains P0–P3 records. Priority is an evidence-use and reading-depth classification, not a risk-of-bias score or publication-quality ranking.

## A1 evidence-status correction and closure

An earlier repository state incorrectly blurred the difference between the **intended reading protocol** and the evidence actually documented in the live notes. During the reviewer-A1 audit, some live records still contained prospective/template language such as `When reading this paper, extract...`, and many historical notes still carried `existing review archive audited; no current-cycle PDF verification`. Historical source matching was therefore not accepted as proof that the full-text protocol had been completed.

A1 was remediated paper by paper. The conservative rule was:

- a live note containing a prospective reading TODO/template remained incomplete until that block was replaced by findings checked against the paper;
- a historical source-note match, even with an A/B quality grade, did not by itself prove a current-cycle full-text reread/reverification;
- a record counted as current-cycle verified only when supported by an explicit A1 reread/reverification entry or by a previously documented current-cycle full-text check in `data/paper_note_audit.csv`;
- inaccessible papers remained blocked rather than being reconstructed from abstracts, metadata, or code.

The final generated audit on **2026-09-11** meets the closure criterion:

| A1 closure measure | Final count |
|---|---:|
| Live paper notes | **403** |
| Exact `When reading this paper...` TODOs | **0** |
| Generic evidence-template blocks | **0** |
| Accessible records without current-cycle full-text verification | **0** |
| Records still requiring A1 full-text remediation | **0** |
| Full-text access exceptions | **1** |

Thus **402 accessible included records have documented current-cycle full-text analysis/verification**. Record **249** is the sole full-text access exception and is blocked from claim-level synthesis. The repository deliberately does **not** state that all 403 were read in full.

The authoritative closure artifacts are `data/a1_live_note_audit.csv`, `data/a1_live_note_audit_summary.json`, `data/a1_fulltext_rechecks.csv`, `data/a1_evidence_batches/`, and `data/paper_note_audit.csv`.

## Reading-depth standard used during A1

For every accessible included paper, verification follows the tier-specific standard:

- **P0/P1:** full-text reading plus deep critical analysis, concrete methods/results, limitations, evidentiary role, relevance to the survey, and evidence locations in the paper.
- **P2/P3:** full-text reading plus a complete structured analysis of relevance, methodology, results/concrete benchmark properties where applicable, contributions, limitations, and evidence locations.

A generic topic summary, a list of items to extract later, or publication metadata alone is not accepted as a completed note. Where a source is a survey, framework/design paper, or qualitative study with no appropriate numerical result, completion is based on its actual scope, taxonomy/design, evidence base, conclusions, and limitations rather than an artificial requirement for numbers.

## A1 evidence batches and reread ledger

`data/a1_evidence_batches/` contains the paper-grounded remediation entries used to replace incomplete live notes. Each entry records the source/version checked, the full-text basis, concrete evidence, and limitations. `scripts/apply_a1_evidence_batches.py` applies only these explicitly reviewed entries and is idempotent, so repeated CI runs do not duplicate verification blocks.

`data/a1_fulltext_rechecks.csv` records explicit A1 rereads/reverification. A row is added only after the paper has actually been checked and its live note has been replaced or confirmed with paper-grounded evidence. `scripts/apply_a1_fulltext_rechecks.py` synchronizes those entries into `data/paper_note_audit.csv`; it does not infer reading from note formatting or source-file existence and does not invent PDF hashes for papers reviewed through authoritative web/PDF sources.

The final 402 accessible-record verification total combines explicit A1 rereads/reverification with papers already supported by documented current-cycle full-text checks before the A1 recheck ledger was introduced.

## Live-note A1 audit

`scripts/audit_a1_live_notes.py` scans all 403 live notes and emits:

- `data/a1_live_note_audit.csv` — one row per live note, including template/TODO and verification flags;
- `data/a1_live_note_audit_summary.json` — aggregate closure status.

The audit is stricter than the historical source-matching audit. A note with a reading TODO/template or without current-cycle verification is unresolved even if a historical source matched its title. The final audit contains zero such accessible records.

## Historical paper-note remediation audit

The supplied review archive contained 1,522 Markdown files, including individual notes, merged section notes, duplicate stubs, and verification reports. An earlier structural audit used normalized title matching to locate candidate source notes, followed by manual overrides for title variants and duplicate-stub cases. That matching was provenance triage only; it did **not** establish a completed full-text reading.

| Historical/structural result | Count |
|---|---:|
| Included register records checked | 403 |
| Reliable historical source-note mappings | 335 |
| Records without a reliable historical source-note match | 68 |
| Notes created or replaced in the earlier remediation pass | 71 |
| Normalized paper-note files | 403 |
| Paper-specific synthesis-source files | 403 |
| PDFs retrieved/extracted/title-checked in the earlier remediation cycle | 134 |
| Records retained from the historical archive without a new PDF check at that earlier stage | 268 |
| Previously identified full-text access exceptions | 1 |

These figures remain for provenance and reproducibility only. They are **not** the final A1 completion counts. The 268 archive-only records were subsequently subjected to the stricter A1 recheck process; the final live audit now reports zero accessible records without current-cycle verification.

## One-paper-per-file synthesis-source layer

Release v1.2.0 materializes a one-to-one paper-specific source layer under `notes/original_sources/`, with exactly 403 Markdown files keyed to the same stable IDs as `notes/papers/`. This storage structure improves traceability, but file existence is not evidence of completed reading. The source layer is regenerated from the live notes after paper-specific remediation.

For the 335 papers with reliable historical source-note mappings, exact historical provenance remains available separately. When a historical note proved template-heavy or insufficient, the live note and generated synthesis-source file were replaced only after actual paper review.

## Historical source-note preservation

The 335 reliable historical mappings resolved to **229 unique historical Markdown files**. Twenty were shared/merged source documents covering 126 mapped records. Those exact files are preserved byte-for-byte under `notes/historical_source_snapshots/` and remain available in the immutable provenance release at commit `83aca98913e2202d912778917ff7c5b92ff67399`.

The frozen historical manifest is `data/historical_original_note_source_manifest.csv`. Historical snapshots document what existed in the earlier review archive; they are not substituted for A1 verification.

## Full-text access exception

Record **249**, *Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement*, remains blocked because a complete verifiable paper copy has not been obtained despite renewed publisher, bibliographic, exact-title, preprint, author-page, and author-repository searches. It is retained for traceability but is not used for claim-level synthesis. See `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`.

## Publication-status verification is separate from A1

The earlier publication-status validation excluded records 432, 656, and 686 from the strict citation layer. During the A1 paper rereads, records **323** and **419** were successfully read in full but their archival-published/formally-accepted status could not be revalidated with the same confidence as their reading evidence. They are therefore separately marked `blocked pending publication-status revalidation` for claim use.

These records are **not full-text access exceptions and do not make A1 incomplete**. Their bibliographic eligibility should be resolved independently before the final manuscript/citation-pool freeze.

## Version policy

- **Canonical published metadata supersedes preprint metadata.** Where a journal or conference version exists, the canonical title, venue, year, and identifiers from that version are used.
- **Preprints and non-archival workshop papers** should not support strict publication-eligible claims unless a final published or formally accepted version is verified.
- **Record IDs are stable.** Existing IDs will not be reassigned in future patch releases.
- **A1 status is evidence-driven.** CI/file generation alone cannot make a paper verified; an explicit paper-grounded evidence record is required.
- **Exceptions remain visible.** Missing full text or unresolved publication status is represented as a block, not silently converted into a completed/eligible record.

## Validation status after A1 closure

| Check | Status |
|---|---|
| 805-study corpus — unique record IDs | ✅ Verified |
| 403 survey-register records contained within 805-study corpus | ✅ Verified |
| Earlier strict exclusion count | ✅ 3 records (432, 656, 686) |
| One normalized note per 403 register record | ✅ 403 files |
| One generated synthesis source per 403 register record | ✅ 403 files |
| Historical provenance snapshot | ✅ 229 exact files for 335 historical mappings |
| Live TODO/template-free note corpus | ✅ **0 TODOs / 0 templates** |
| Current-cycle full-text verification for every accessible included paper | ✅ **402/402 accessible records** |
| Full-text access exception | ⚠️ **Record 249 only** |
| Publication-status revalidation blocks | ⚠️ **Records 323 and 419; separate from A1** |

**A1 full-text evidence remediation is closed as of 2026-09-11 under the generated audit criterion.**
