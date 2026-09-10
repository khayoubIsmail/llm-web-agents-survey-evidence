# Paper-Specific Synthesis Source Layer

## Purpose

`notes/original_sources/` is the one-paper-per-file synthesis-source layer for the 403-study published/accepted evidence pool. It uses the same stable record-ID filenames as `notes/papers/`, so every included record has an explicit one-to-one source path:

- `notes/papers/<record_id>.md` — canonical normalized note used for synthesis and audit.
- `notes/original_sources/<record_id>.md` — paper-specific detailed synthesis source record for the same paper.

The directory contains exactly **403 Markdown files for 403 unique register IDs**. It does not contain merged multi-paper synthesis files.

## How the 403 source records were established

The note audit found **335 reliable historical source-note mappings**. Those mappings originally resolved to only **229 historical Markdown files** because 20 of the historical files were shared/merged documents covering 126 mapped records. The paper-specific analysis from those audited sources had already been materialized into one normalized record per paper in `notes/papers/`; the new source layer therefore gives every mapped paper its own stable, paper-specific source record rather than pointing several papers to the same merged file.

The remaining **68 records had no reliable paper-specific historical source match**. They were selected for remediation rather than being assigned an invented historical source. For accessible records, the remediation notes were written from independently retrieved, extracted, and title-checked full text and record the PDF page count, SHA-256 digest, and title-similarity evidence in `data/paper_note_audit.csv`. Across the complete audit, 134 papers received such a current-cycle PDF check.

## Historical provenance is retained separately

The exact byte-for-byte historical files from the September 9 provenance release are retained under `notes/historical_source_snapshots/`. They remain unchanged, including merged source documents. Their frozen 335-record/229-file manifest is retained as `data/historical_original_note_source_manifest.csv`.

The prior provenance release is also permanently recoverable from commit `83aca98913e2202d912778917ff7c5b92ff67399`.

## Full-text exception

Record **249**, *Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement*, remains the sole full-text access exception. Its publisher metadata, DOI, bibliographic records, and authors' code repository were rechecked, but a complete paper copy could not be verified. Therefore `notes/original_sources/0249.md` is intentionally the auditable access-exception record, not a fabricated full-text synthesis, and record 249 remains blocked from claim-level synthesis.

Consequently the repository has **403 paper-specific source files**, but only **402 records with documented full-text analysis** until a complete copy of record 249 is obtained and analyzed.

## Interpretation

The term *source* in `notes/original_sources/` means the paper-specific synthesis record underlying the normalized evidence trail; these files are not copies of third-party papers. No publisher PDF is redistributed. The historical snapshots preserve provenance, while `data/paper_note_audit.csv` remains the authoritative record of whether each synthesis came from retained review-archive evidence, a current-cycle full-text remediation, or an unresolved access exception.
