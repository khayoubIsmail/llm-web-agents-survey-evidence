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

## Reading depth

**Ismail Khayoub** and **Firdaous Ait Mohamed** conducted in-depth reading of P0/P1 studies (methods, results, limitations, and relevance) and rapid targeted reading of P2/P3 studies (abstract, conclusions, and key claims). They also performed and cross-checked screening, eligibility assessment, thematic coding, evidence extraction, and synthesis across the full 805-study corpus.

**Mohamed-Amine Chadi** and **Hajar Mousannif** performed final analytical verification and audit of the priority assignments, status categories, and strict exclusion decisions.

## Publication-status verification

All 403 records in the published/accepted pool were individually verified against at least one canonical source (ACM DL, IEEE Xplore, Springer, OpenReview, Semantic Scholar, or direct author confirmation). Three records (IDs: 432, 656, 686) could not be confirmed as archival-published or formally accepted and were retained in the 805-study mapping corpus but excluded from the strict citation-eligibility pool.

## Version policy

- **Canonical published metadata supersedes preprint metadata.** Where a journal or conference version exists, the canonical title, venue, year, and identifiers from that version are used.
- **Preprints and non-archival workshop papers** remain visible in the 805-study mapping file but are excluded from the strict evidence pool unless a final published or formally accepted version is verified.
- **Record IDs are stable.** Existing IDs will not be reassigned in future patch releases. New studies may receive new IDs appended to the corpus.
- **Patch releases** document bibliographic corrections in the commit log. Major changes to scope or methodology will increment the version number.

## Validation audit (v1.0.0)

| Check | Result |
|---|---|
| 805-study corpus — unique record IDs | ✅ Verified, no duplicates |
| 403-pool — fully contained within 805-study corpus | ✅ Verified |
| Strict exclusion count | ✅ Exactly 3 (records 432, 656, 686) |
| CSV ↔ JSON identifier agreement | ✅ All IDs match |
| SHA-256 checksums for all data files | ✅ All pass |
