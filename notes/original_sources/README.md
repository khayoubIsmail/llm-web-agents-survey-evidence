# Historical Original Note Sources

This directory preserves the original Markdown source notes selected by the
title-and-coverage audit. These files are historical provenance snapshots; the
canonical, one-paper-per-file evidence notes remain in [`../papers/`](../papers/).

## Coverage

| Item | Count |
|---|---:|
| Included register records | 403 |
| Records with a reliable original source note | 335 |
| Unique original source files preserved here | 229 |
| Source files mapped to more than one record | 20 |
| Records without a reliable original source match | 68 |
| Final notes created or replaced during remediation | 71 |

The number of source files is lower than the number of mapped records because
some original documents are merged section-level syntheses containing notes for
several papers. Those documents are preserved in full rather than split or
rewritten. Other source files are standalone notes, for example
[`S2/P0/2017-06 - Attention Is All You Need.md`](S2/P0/2017-06%20-%20Attention%20Is%20All%20You%20Need.md).

## Integrity and mapping

[`../../data/original_note_source_manifest.csv`](../../data/original_note_source_manifest.csv)
maps each of the 335 register records to its final note, original archive path,
repository snapshot, byte count, line count, source layout, and SHA-256 digest.
The export script copies the source bytes without normalizing headings, line
endings, or spacing:

```bash
python scripts/export_original_note_sources.py \
  --audit data/paper_note_audit.csv \
  --source-root /path/to/review-archive/markdowns \
  --output-root notes/original_sources \
  --manifest-output data/original_note_source_manifest.csv
```

## Interpretation

- Use `notes/papers/` for the final synthesis and claim-level evidence trail.
- Use this directory to inspect the historical source material and verify note
  provenance.
- A complete merged source can contain batch-level synthesis or additional
  historical entries. Its presence here does not add those entries to the
  403-paper register or make them eligible for claim-level use.
- The presence of an original note does not by itself prove a new full-text
  check in the current remediation cycle; consult `data/paper_note_audit.csv`.
- The 68 unmatched records do not have invented historical sources. Their final
  notes and remediation status are documented in the canonical note corpus.
- No third-party paper PDFs are stored here. Bibliographic metadata, paper
  titles, and any attributed third-party material remain outside the scope of
  the repository's license where applicable.
