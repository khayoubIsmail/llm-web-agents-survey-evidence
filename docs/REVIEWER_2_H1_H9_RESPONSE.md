# Reviewer 2 — Response for H1–H9 Metric-Stack Specification

We thank the reviewer for identifying that the proposed metric stack was not yet operational enough to implement reproducibly. We have now frozen an implementation-level scoring protocol before running the new three-agent wireless-headphones experiment. The full protocol is released in `docs/H1_H9_METRIC_SPECIFICATION.md`, the field-level evidence structure in `schemas/evidence_object.schema.json`, and a machine-readable worked example in `data/h9_worked_scoring_example.json`.

## H1 — Predicted-to-gold record alignment

Each schema declares canonical identity fields. Exact normalized identity-key matches are aligned first. Remaining records are matched one-to-one using a predeclared field-aware similarity; missing predicted values score zero in that similarity. For the wireless-headphones worked experiment, the fallback threshold is fixed at `tau=0.20` before model outputs are inspected. Extra predictions lower record precision, missing records lower recall, and duplicates cannot match one gold record more than once. Because fallback alignment is threshold-sensitive, record F1 is diagnostic and strict field F1 is primary.

## H2 — Nested, multi-valued, optional, and missing fields

Nested objects are scored at leaf field paths. Collection fields declare ordered, set, or multiset semantics before evaluation. Gold null/absent optional values are not positive recall targets; a non-null prediction against a null/absent gold field is a false-positive field claim, while omission of a non-null gold value is a false negative. Missing/null required fields reduce completeness and may invalidate the schema. Non-schema keys are scored separately under H8.

## H3 — Macro versus micro averaging

The primary strict field precision/recall/F1 is micro-averaged over all non-null schema-field claims, including unmatched records in the relevant denominators. Task-macro field F1 and, when applicable, site-macro field F1 are secondary summaries. Provenance uses field-pooled micro reporting as primary with task-macro reporting secondarily. Every aggregate is now explicitly labelled.

## H4 — Semantic equivalence

Primary scoring uses only field-specific deterministic comparators fixed before evaluation: normalized strings, canonical URLs, numeric tolerances, money amount/currency, dates, booleans, enum aliases, and declared collection semantics. Free-text semantic equivalence is permitted only as a separately reported secondary analysis under a frozen rubric; strict deterministic scores remain primary. The planned headphones experiment uses only deterministic comparators.

## H5 — Provenance support `S(p)`

We now distinguish evidence availability `A(p)` from evidence support `S(p)`. `S(p)=1` only when the frozen source identity is correct, the locator resolves unambiguously, the quote/evidence is present at that location, and the source evidence directly supports the predicted value or reproduces it through a declared deterministic transformation chain. Vision evidence uses the analogous screenshot/tile/bounding-box rule, with logged manual adjudication when automatic verification is unavailable. We report provenance coverage, conditional provenance correctness, and joint provenance faithfulness separately. A formal evidence-object JSON Schema is released and also addresses the underlying data-structure requirement raised by Reviewer 1.

## H6 — Empty predictions

When gold contains targets but no records/fields are predicted, field and record precision are set to zero by convention, recall/F1 are zero, and completeness is zero. Provenance and prediction-error ratios with zero prediction denominators are reported as N/A, never as perfect scores. Legitimately empty gold+prediction tasks may be marked as correct empty results, while zero-denominator extraction ratios remain N/A.

## H7 — Confidence intervals

The default uncertainty procedure is now fixed to a 95% paired hierarchical cluster bootstrap with 10,000 replicates: sites are sampled with replacement, all tasks from sampled sites are retained, and repeated stochastic runs are resampled within task/system cells when available. Pairwise system differences use the same bootstrap draws. If only one run per task exists, the interval is explicitly described as task/site heterogeneity rather than run-to-run uncertainty; no site-level CI is claimed for a one-site/one-task experiment.

## H8 — Unsupported values versus non-schema fields

The former combined “unsupported-field rate” is split into two measures: (1) **unsupported-value rate**, the fraction of non-null predictions on valid schema fields for which source support fails, and (2) **non-schema-field rate**, the fraction of all non-null output claims whose field path is absent from the target schema. Raw counts and schema validity are reported separately.

## H9 — Worked scoring example

We added a complete numerical wireless-headphones-style example with two gold records and three predictions. It explicitly demonstrates exact and fallback record alignment, optional-field hallucination, a non-schema field, an unmatched extra record, and unsupported provenance. The example yields record F1 `0.800`, strict field F1 `0.571`, required-field completeness `0.750`, joint provenance faithfulness `0.444`, unsupported-value rate `0.556`, and non-schema-field rate `0.100`. The machine-readable derivation is released in `data/h9_worked_scoring_example.json`.

These changes make H1–H9 implementable before the real ≥3-agent experiment. We will use this frozen protocol for the Reviewer-1 wireless-headphones case study rather than defining or adjusting metrics after inspecting agent outputs.