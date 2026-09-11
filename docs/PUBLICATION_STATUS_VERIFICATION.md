# Publication-status verification protocol

## Scope

This check is separate from A1. A1 concerns whether the 403 included papers have an auditable full-text evidence trail. Publication-status verification checks the bibliographic status of the broader 805-study mapping corpus and must not be used as a proxy for reading completeness.

## Why v1 is deprecated

The original `scripts/verify_publication_status.py` / `data/publication_status_verification.csv` run is retained only in Git history as a failed first implementation. Its verdicts must not be used for corpus edits because it (1) examined only OpenAlex `primary_location`, even when another OpenAlex location represented the archival paper, and (2) searched by title while ignoring DOI/arXiv identifiers already present in the register. This produced obvious false downgrades and excessive `NO_MATCH` results.

## v2 resolution and evidence rules

`scripts/verify_publication_status_v2.py` resolves each register row in this order:

1. DOI lookup when a DOI is available;
2. arXiv-ID lookup when an arXiv identifier is available;
3. title lookup as a fallback;
4. Crossref title lookup when OpenAlex remains unresolved.

For an OpenAlex match, v2 inspects all available publication locations (`primary_location`, every entry in `locations[]`, and `best_oa_location`) rather than treating the primary location as authoritative. A work is considered to have external archival evidence when at least one non-preprint location is a journal, conference, book series, or ebook-platform source. DOI-publisher prefixes and page ranges are retained as corroborating archival signals. The exact signals used are written to the `archival_evidence` column.

Venue comparison is normalized before a mismatch is asserted: common venue acronyms are canonicalized, and proceedings/year/ordinal/track boilerplate is removed. Normalization is deliberately not allowed to erase genuine disagreements.

## Verdicts

- `OK_ARCHIVAL` — register and external evidence agree on archival status.
- `OK_PREPRINT` — register and external evidence agree that only a preprint/technical-report status is established.
- `UPGRADE` — register is preprint/unconfirmed, but archival evidence is found.
- `DOWNGRADE` — register claims archival status, but the automated sources provide no archival evidence.
- `VENUE_MISMATCH` — archival evidence exists, but the normalized venues materially disagree.
- `VENUE_MISSING` — the register venue is blank while an archival venue is externally recovered.
- `NO_MATCH` — automated resolution failed. This is not evidence of non-publication.

## Mandatory known-answer gate

The 805-row v2 output is not admissible for corpus maintenance unless these checks pass:

- record 1, *Attention Is All You Need* → `OK_ARCHIVAL`;
- record 110, known EMNLP-vs-COLM disagreement → `VENUE_MISMATCH`;
- record 135, *AppWorld* → `UPGRADE`;
- record 323 → `DOWNGRADE`;
- record 774 → `VENUE_MISSING`.

The gate is implemented in `scripts/check_publication_status_known_answers.py`. The workflow stops before committing v2 evidence if any known answer fails.

## Evidence products

After a successful gated run, the workflow produces:

- `data/publication_status_verification_v2.csv` — one verification row per mapping-corpus record;
- `data/publication_status_verification_v2_summary.json` — aggregate verdict counts and gate status;
- `data/verification_cache_v2/` — raw API responses used by the run, retained as an auditable cache.

The verifier never writes back to `data/studies_805_mapping_corpus.csv`.

## Manual-review rules

Automated verdicts are evidence for review, not automatic corpus changes. In particular:

- `DOWNGRADE` must be checked manually before changing an accepted/published record. Accepted or “to appear” papers may not yet be indexed; record 214 is a known example requiring manual handling.
- `NO_MATCH` is never interpreted as non-publication. Recent 2026 papers are especially susceptible to indexing lag.
- `VENUE_MISSING`, `UPGRADE`, and `VENUE_MISMATCH` should be checked against the publisher/proceedings page before the canonical register is patched.

Any later register change should be logged separately with the external bibliographic evidence that justified it.
