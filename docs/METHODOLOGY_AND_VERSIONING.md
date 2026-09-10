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

The review protocol defines an initial full-text assessment for eligibility and priority classification. Classification is not intended to be based on titles or abstracts alone. Each study is assigned according to its fit with the survey scope and research questions, the directness of its contribution to web/GUI agents or enabling agent methods, the kind of evidence it can contribute, and its publication-status eligibility.

| Tier | Predefined classification criterion | Intended synthesis treatment |
|---|---|---|
| P0 | Cornerstone work defining the survey scope, core method, or indispensable conceptual foundation | Deep critical full-text analysis and detailed notes |
| P1 | Direct evidence for a central architecture, method, benchmark, empirical result, or risk claim | Deep critical full-text analysis and detailed notes |
| P2 | Supporting or extending evidence that materially informs a comparison, component, or adjacent design choice | Complete full-text reading with lighter structured analysis |
| P3 | Historical, contextual, or peripheral-but-relevant evidence within the survey boundary | Complete full-text reading with lighter structured analysis |
| P4 | Peripheral to the research questions, out of scope, or insufficiently connected to the intended synthesis | Excluded from final synthesis |

The final 403-paper published/accepted pool contains P0–P3 records. Priority is an evidence-use and reading-depth classification, not a risk-of-bias score or publication-quality ranking.

## Important A1 evidence-status correction

The preceding table describes the **intended review protocol**, not a completed-current-cycle claim. During the reviewer-A1 audit, the live note corpus was found to contain prospective/template language such as `When reading this paper, extract...` in records that had previously been labeled as substantive historical notes. The same audit also found many records whose provenance field stated `existing review archive audited; no current-cycle PDF verification`.

Those records cannot be treated as current-cycle evidence that the intended full-text protocol was actually completed. Accordingly, this repository **does not currently claim that all 403 papers have been independently re-read or fully re-verified in the A1 remediation cycle**.

The remediation rule is deliberately conservative:

- a live note containing a prospective reading TODO/template is incomplete for A1 until the paper-specific block is replaced with findings actually checked against the paper;
- a historical source-note match, even with an A/B quality grade, does not by itself prove a current-cycle full-text reread;
- only papers explicitly listed in `data/a1_fulltext_rechecks.csv`, or already supported by a documented current-cycle full-text check in `data/paper_note_audit.csv`, count as current-cycle verified;
- inaccessible papers remain blocked rather than being reconstructed from abstracts or metadata.

The current reviewer-facing state is generated in `data/a1_live_note_audit.csv` and `data/a1_live_note_audit_summary.json`. These generated files are the authoritative progress report for A1 while remediation is underway. The target for closure is **zero live reading-TODO/template blocks and zero unresolved no-current-cycle-verification records, except explicitly documented access exceptions**.

## Reading-depth standard used during remediation

For every paper actually re-read in the A1 remediation cycle, the note must meet its tier-specific standard:

- **P0/P1:** full-text reading plus deep critical analysis, concrete methods/results, limitations, evidentiary role, relevance to the survey, and evidence locations in the paper.
- **P2/P3:** full-text reading plus a complete structured analysis of relevance, methodology, results/concrete benchmark properties where applicable, contributions, limitations, and evidence locations.

A generic topic summary, a list of items to extract later, or publication metadata alone is not accepted as a completed note.

## Paper-note remediation audit

The supplied review archive contained 1,522 Markdown files, including individual notes, merged section notes, duplicate stubs, and verification reports. The initial remediation audit used normalized title matching to locate candidate source notes, followed by manual overrides for title variants and duplicate-stub cases. Automated matching was triage only; it did **not** establish that the matched note reflected a completed full-text reading.

The historical structural audit found:

| Historical/structural result | Count |
|---|---:|
| Included register records checked | 403 |
| Reliable historical source-note mappings | 335 |
| Records without a reliable historical source-note match | 68 |
| Notes created or replaced in the earlier remediation pass | 71 |
| Normalized paper-note files | 403 |
| Paper-specific synthesis-source files | 403 |
| PDFs retrieved/extracted/title-checked in the earlier remediation cycle | 134 |
| Records retained from the historical archive without a new PDF check at that stage | 268 |
| Previously identified full-text access exceptions | 1 |

These historical counts are retained for reproducibility, but **they are not the A1 completion counts**. In particular, the 268 archive-only records are now being re-audited individually, and template-heavy notes are being replaced from the actual papers. Progress is recorded separately in `data/a1_fulltext_rechecks.csv` and recomputed by `scripts/audit_a1_live_notes.py`.

## A1 full-text recheck ledger

`data/a1_fulltext_rechecks.csv` is append-only in meaning: a record is added only after its paper has actually been re-read and its live note has been replaced or confirmed with paper-grounded evidence. Each row records the review date, source/version used, full-text basis, provenance, and claim-use status.

`data/paper_note_audit.csv` is synchronized from that explicit ledger by `scripts/apply_a1_fulltext_rechecks.py`. The script intentionally does not infer a reread from note formatting or source-file existence and does not fabricate local PDF hashes for papers reviewed through authoritative web/PDF sources.

## Live-note A1 audit

`scripts/audit_a1_live_notes.py` scans all 403 live notes and emits:

- `data/a1_live_note_audit.csv` — one row per live note, including template/TODO and verification flags;
- `data/a1_live_note_audit_summary.json` — aggregate current status.

The audit is intentionally stricter than the earlier source-matching audit. A note with a reading TODO/template or no current-cycle verification remains in the remediation queue even if a historical source matched its title.

## One-paper-per-file synthesis-source layer

Release v1.2.0 materializes a one-to-one paper-specific source layer under `notes/original_sources/`, with exactly 403 Markdown files keyed to the same stable IDs as `notes/papers/`. This storage structure improves traceability, but **file existence is not evidence of completed reading**. The source layer is regenerated from the live notes after paper-specific remediation.

For the 335 papers with reliable historical source-note mappings, exact historical provenance remains available separately. For records whose historical notes prove to be template-heavy or insufficient, the live note and generated synthesis-source file are replaced only after actual paper review.

## Historical source-note preservation

The 335 reliable historical mappings resolved to **229 unique historical Markdown files**. Twenty were shared/merged source documents covering 126 mapped records. Those exact files are preserved byte-for-byte under `notes/historical_source_snapshots/` and remain available in the immutable provenance release at commit `83aca98913e2202d912778917ff7c5b92ff67399`.

The frozen historical manifest is `data/historical_original_note_source_manifest.csv`. Historical snapshots provide provenance for what existed in the earlier review archive; they do not prove that the corresponding paper was independently re-opened in the present A1 cycle.

## Full-text access exception

Record 249, *Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement*, remains blocked because a complete verifiable paper copy has not been obtained despite renewed publisher, bibliographic, exact-title, preprint, and author-repository searches. It is retained in the publication-eligible register for traceability but is not used for claim-level synthesis. See `docs/FULL_TEXT_ACCESS_EXCEPTIONS.md`.

## Publication-status verification

All 403 records in the published/accepted pool were individually checked for publication/status evidence. Three records (IDs 432, 656, 686) could not be confirmed as archival-published or formally accepted and were retained in the 805-study mapping corpus but excluded from the strict citation-eligibility pool.

## Version policy

- **Canonical published metadata supersedes preprint metadata.** Where a journal or conference version exists, the canonical title, venue, year, and identifiers from that version are used.
- **Preprints and non-archival workshop papers** remain visible in the 805-study mapping file but are excluded from the strict evidence pool unless a final published or formally accepted version is verified.
- **Record IDs are stable.** Existing IDs will not be reassigned in future patch releases.
- **A1 progress is evidence-driven.** A record moves out of the remediation queue only after its paper-specific evidence has actually been checked; CI/file generation alone cannot close a paper.

## Validation status during A1 remediation

| Check | Status |
|---|---|
| 805-study corpus — unique record IDs | ✅ Verified |
| 403-pool contained within 805-study corpus | ✅ Verified |
| Strict exclusion count | ✅ 3 records (432, 656, 686) |
| One normalized note per 403-pool record | ✅ 403 files |
| One generated synthesis source per 403-pool record | ✅ 403 files |
| Historical provenance snapshot | ✅ 229 exact files for 335 historical mappings |
| Live TODO/template-free note corpus | 🔄 **In remediation — see `data/a1_live_note_audit_summary.json`** |
| Current-cycle full-text verification for every accessible included paper | 🔄 **In remediation — see `data/a1_live_note_audit_summary.json` and `data/a1_fulltext_rechecks.csv`** |
| Access exception handling | ⚠️ Record 249 explicitly blocked |

**A1 must not be described as closed until the generated live-note audit reaches the closure criterion above.**
