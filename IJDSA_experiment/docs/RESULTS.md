# Experiment results

All 108 scheduled runs finished and were scored.

| Configuration | Runs | Macro Field F1 | Micro Field F1 | Task success | Verified provenance precision |
|---|---:|---:|---:|---:|---:|
| A1 + Gemma | 12 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| A1 + Qwen | 12 | 0.0581 | 0.0541 | 0.0000 | 0.1250 |
| A1 + Kimi | 12 | 0.9440 | 0.9492 | 0.8333 | 0.8822 |
| A2 + Gemma | 12 | 0.2199 | 0.2543 | 0.0000 | 0.5139 |
| A2 + Qwen | 12 | 0.2576 | 0.3762 | 0.0833 | 0.2152 |
| A2 + Kimi | 12 | 0.8524 | 0.8649 | 0.7500 | 0.7899 |
| A3 + Gemma | 12 | 0.0455 | 0.0510 | 0.0000 | 0.1875 |
| A3 + Qwen | 12 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| A3 + Kimi | 12 | 0.7872 | 0.8033 | 0.1667 | 0.8021 |

The strongest observed configuration is A1 + Kimi. This is a result for this controlled case study, not a general architecture ranking.

Two patterns matter for the paper. First, A2 improves the weaker local models compared with A1, but the model gap remains large. Second, extraction quality and task completion can disagree: A3 + Kimi reaches macro Field F1 0.7872 while task success is 0.1667.

Schema adherence alone is also not enough. A1 + Gemma can produce structurally valid output while strict Field F1 remains 0.0000.

The non-schema-field rate is 0 across the completed experiment. Unsupported output appears as in-schema values that are not correctly supported, rather than as extra schema keys.

## Worked scoring trace

A1 + Kimi on MediaMarkt DE, repetition 3, aligned all 10 predicted records with the 10 gold records. It produced 39 true-positive field claims, 1 false-positive field claim, and 0 false negatives, giving Field F1 0.9873. The single failing field was a rating. Its locator pair and quote were valid, but the claimed value was not the supported correct value. This is why locator validity and value support are checked separately.

## Integrity checks

- 108 scheduled runs / 108 scored runs
- H8 error-rate columns populated
- interrupted-run archives were not part of scoring
- four snapshot hash differences were caused only by Windows CRLF to Git LF normalization; the original byte hashes reproduce after restoring CRLF
- HTML normalization is disabled with `.gitattributes`
- bootstrap: 2,000 site-cluster resamples, seed 42

The machine-readable summaries and per-run scoring details are in `results/`. Raw run outputs are in `runs/`.

`PROTOCOL.md` is kept byte-for-byte as part of the frozen experiment because it is listed in `freeze_manifest.json`.
