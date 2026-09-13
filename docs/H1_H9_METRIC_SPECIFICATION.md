# H1–H9 — Operational Metric Specification for Schema-Guided Web Extraction

**Status:** frozen protocol for the survey revision and the subsequent wireless-headphones worked experiment.

**Purpose.** Reviewer 2 correctly noted that the metric stack in Section 7.2 was conceptually useful but not sufficiently operational to reproduce an evaluation. This document fixes H1–H9 before any new three-agent scoring is performed. The protocol deliberately separates (i) record association, (ii) value correctness, (iii) schema compliance, and (iv) source-evidence faithfulness so that one capability cannot silently substitute for another.

The specification reuses the deterministic, type-aware comparison and one-to-one matching principles already developed in WADE-Bench, but freezes the rules here as the evaluation contract for the survey's worked example. Any future deviation must be reported as a protocol change rather than silently changing the score after seeing model outputs.

---

## Notation

For a task, let:

- `Y = {r_1, ..., r_n}` be the gold record set.
- `Yhat = {rhat_1, ..., rhat_m}` be the predicted record set.
- `F` be the declared schema field paths.
- `F_req ⊆ F` be the required field paths.
- `K ⊆ F` be the declared identity fields used for exact record-key matching.
- `c_f(x,y) ∈ {0,1}` be the deterministic comparator for field `f` after its declared normalization.
- `M ⊆ Y × Yhat` be the accepted one-to-one record alignment.
- `A(p) ∈ {0,1}` indicate that prediction `p` contains a syntactically complete evidence object.
- `S(p) ∈ {0,1}` indicate that the stored evidence actually supports prediction `p` against the frozen source artifact.

A **field claim** is a non-null predicted value attached to a field path. Evaluator metadata and provenance containers are not counted as field claims.

---

## H1 — Predicted ↔ gold record alignment

Record alignment is a deterministic association step performed before field scoring. It is not itself proof that a record is correct.

1. **Normalize identity fields.** Apply the same field-specific canonicalizers used by the field scorer.
2. **Exact key pass.** Match records whose complete, non-null canonical identity key `K` is exactly equal. A record may participate in at most one match.
3. **Fallback pass.** For remaining unmatched records, compute

   `sim(r, rhat) = (1 / |F_r|) * Σ_{f∈F_r} 1[c_f(r_f, rhat_f)=1]`,

   where `F_r` is the set of non-null gold schema fields in `r` for which the prediction exposes a comparable value. Candidate pairs are sorted by decreasing similarity and greedily accepted under a one-to-one constraint when `sim >= τ`.
4. **Frozen threshold.** For the wireless-headphones worked experiment, `τ = 0.20`, inherited from the current WADE-Bench scorer and fixed **before** inspecting the three agents' outputs.
5. **Unmatched records.** Unmatched predictions are false-positive records; unmatched gold records are false-negative records. Duplicate predictions cannot receive repeated credit for the same gold record.

Record precision, recall, and F1 are:

`P_R = |M| / |Yhat|`, `R_R = |M| / |Y|`, `F1_R = 2 P_R R_R / (P_R + R_R)`.

Because fallback alignment is threshold-sensitive, record F1 is a **diagnostic association metric**. Strict field F1 is the primary extraction-correctness metric.

---

## H2 — Nested, multi-valued, optional, and missing fields

### Nested objects

Nested schema objects are evaluated at **leaf field paths** (for example, `seller.name` and `seller.url`). A missing/null parent implies missing/null descendants. The parent container itself is not an additional scored field unless the schema explicitly declares it as a value-bearing field.

### Multi-valued fields

Each collection-valued schema field must declare its comparison semantics before evaluation:

- `ordered`: normalize each item and compare the sequence in order;
- `set`: normalize items and compare set equality, ignoring order and duplicate repetitions;
- `multiset`: normalize items and compare multiplicities while ignoring order.

The **strict field score gives one field-level credit only when the whole normalized collection satisfies the declared comparator**. Optional element-level list precision/recall may be reported as a diagnostic, but it does not replace strict field correctness.

### Optional and missing values

- A gold non-null value is a positive target.
- A gold `null`/absent optional value is **not** a positive recall target.
- A missing/null prediction for a non-null gold value is a false negative.
- A non-null prediction for a schema field whose gold value is null/absent is a false-positive field claim and therefore hurts field precision.
- A required field that is missing or null is incorrect and reduces required-field completeness; it may also make the record schema-invalid according to the declared JSON Schema.
- Keys not present in the target schema are handled separately under H8; they are not merged into the unsupported-value error.

---

## H3 — Micro versus macro averaging

The aggregation rule is fixed as follows.

### Primary field score: micro

Strict field precision/recall/F1 are **micro-averaged** over all task field claims:

`P_F = N_correct / N_pred_nonnull_schema`,

`R_F = N_correct / N_gold_nonnull`,

`F1_F = 2 P_F R_F / (P_F + R_F)`.

The denominators include claims from unmatched records: unmatched predicted schema-field claims hurt precision and non-null fields in unmatched gold records hurt recall.

### Secondary macro reporting

To make heterogeneity visible, also report:

- task-macro field F1: arithmetic mean of task-level field F1;
- site-macro field F1 when multiple tasks come from the same site;
- task-macro record F1 as a secondary record-discovery summary.

Provenance metrics are field-pooled (micro) as primary and task-macro as secondary. The paper must label each aggregate explicitly; an unlabeled average is not permitted.

---

## H4 — Semantic-equivalence judgments

Primary scoring avoids an unconstrained LLM judge.

Each field is assigned **one comparator before evaluation**:

- normalized exact/case-folded string;
- canonical URL;
- integer/decimal with declared tolerance;
- money (amount + currency, plus declared range/period semantics where applicable);
- canonical date/time;
- boolean;
- closed enum/alias map;
- ordered list, set, or multiset;
- `semantic_text` only for predesignated free-text fields that cannot be reduced to a deterministic comparator.

For deterministic comparators, two values are equivalent only when the declared comparator returns 1. Parse failure on both sides never implies equality.

If `semantic_text` is used, it is a **secondary analysis only**. Candidate pairs that fail strict comparison are adjudicated using a frozen written rubric, with the evaluator blind to agent identity when manual adjudication is required. The decision, rationale, and evaluator version are stored. The strict deterministic score is always reported alongside the semantic score.

For the planned wireless-headphones schema (`product_name`, `price`, `rating`), the primary experiment uses deterministic comparators only; no semantic judge is needed.

---

## H5 — Provenance availability and support `S(p)`

Provenance **availability** and **correctness/support** are distinct.

### Availability `A(p)`

`A(p)=1` iff a non-null schema-field prediction carries a syntactically valid evidence object conforming to `schemas/evidence_object.schema.json`; otherwise `A(p)=0`.

### Support `S(p)`

For a DOM/text evidence object, `S(p)=1` iff all of the following hold against the frozen artifact used for the task:

1. **Source identity:** `page_id`/URL and snapshot identity correspond to the evaluated artifact.
2. **Locator resolution:** the declared selector/XPath/accessibility node/text offsets resolve to exactly the claimed source region; an ambiguous or unresolved locator fails.
3. **Evidence presence:** the stored quote is present in that resolved region after deterministic text normalization.
4. **Value support:** the predicted value is directly supported by the quote after the field comparator, or the declared deterministic transformation history can be replayed from the quoted source value to the predicted normalized value.

For vision evidence, the cited screenshot/tile/bounding box must exist and the visible text or stored crop must support the value. If automatic visual verification is unavailable, the item is manually adjudicated against the frozen screenshot using the same support rule; the method and decision are logged rather than silently treated as automatic verification.

If no valid evidence object exists, `A(p)=0` and `S(p)=0`.

### Provenance metrics

Let `N_pred` be the number of non-null predictions on valid schema fields.

- **Provenance coverage:** `ProvCov = Σ A(p) / N_pred`.
- **Conditional provenance correctness:** `ProvCond = Σ S(p) / Σ A(p)` (N/A if `ΣA=0`).
- **Joint provenance faithfulness:** `ProvJoint = Σ S(p) / N_pred`.

Evidence support is checked against the **source artifact**, not inferred merely from agreement with the gold annotation. A value can therefore be field-incorrect yet evidentially supported, or field-correct yet have invalid provenance; the two dimensions remain separate.

---

## H6 — Zero-prediction and empty-target cases

The evaluator uses explicit zero-denominator rules rather than silently returning perfect scores.

### Gold contains at least one target, prediction is empty

- record precision = 0 (convention), recall = 0, record F1 = 0;
- field precision = 0 (convention), recall = 0, strict field F1 = 0;
- required-field completeness = 0;
- provenance coverage / conditional correctness / joint faithfulness = N/A because there are no predicted field claims;
- unsupported-value rate and non-schema-field rate = N/A because their prediction denominators are zero.

### Gold is empty and prediction is empty

The task-level empty-result decision is correct, but record/field/provenance ratios with zero denominators are reported **N/A**, not 1.0. The task may separately receive `empty_result_correct = 1`.

### Gold is empty and prediction is non-empty

All predicted records/field claims are false positives. Record and field precision are 0; recall is N/A; F1 is defined as 0 for the task-level extraction summary. Provenance is still evaluated independently for any claimed fields.

---

## H7 — Confidence intervals and repeated runs

The default uncertainty report is a **95% paired hierarchical cluster-bootstrap interval**.

1. Fix the evaluated task set and systems before analysis.
2. Use `B = 10,000` bootstrap replicates.
3. At each replicate, sample **sites with replacement** and retain all tasks belonging to each sampled site. This preserves within-site dependence.
4. If multiple stochastic runs exist for a task/system cell, sample runs with replacement within the sampled task before recomputing the metric.
5. Recompute the complete metric from the sampled data; do not average precomputed confidence limits.
6. Report the 2.5th and 97.5th percentiles of the bootstrap distribution.
7. For pairwise system differences, use the **same bootstrap samples** for both systems and bootstrap the paired difference.

If only one run per task exists, the interval represents task/site heterogeneity but **not run-to-run model stochasticity**, and this must be stated. If an experiment contains only one site/task, no site-level confidence interval is claimed; repeated-run dispersion can be reported descriptively instead.

This protocol applies to field F1, record F1, completeness, provenance, cost, and other aggregate metrics. Binary task-success rates use the same site-cluster bootstrap when the corpus contains multiple sites.

---

## H8 — Split unsupported values from non-schema outputs

The previous single “unsupported-field rate” mixed two different failure modes. It is replaced by two separately reported measures.

### Unsupported-value rate (UVR)

A **schema-valid field path** with a non-null predicted value is unsupported when `S(p)=0`.

`UVR = N_unsupported_schema_values / N_pred_nonnull_schema`.

This measures evidentially unsupported claims. It is distinct from field-value correctness.

### Non-schema field rate (NSFR)

A **non-schema field** is a non-null output claim whose leaf field path does not occur in the declared target schema.

`NSFR = N_non_schema_claims / N_all_nonnull_output_claims`.

Report both rates **and their raw counts**. Schema-validity rate is reported separately. A non-schema claim is never relabeled as an unsupported schema value.

---

## H9 — Worked scoring example

The machine-readable worked example is released as `data/h9_worked_scoring_example.json`. The example is intentionally small and synthetic; it validates the scoring contract before the real three-agent wireless-headphones case study (R1-2).

### Schema

Required identity/value fields:

- `product_name`: string, required, identity field;
- `price`: money, required;
- `rating`: float in `[0,5]`, optional;
- additional properties are disallowed.

### Gold

- `g1`: SoundWave X1 — EUR 79.99 — rating 4.5.
- `g2`: QuietBeat Pro — EUR 129.99 — rating null.

### Predictions

- `p1`: exact values for `g1`, all three schema-field claims supported by valid evidence.
- `p2`: `QuietBeat Pro Headphones`, EUR 129.99, rating 4.7, plus non-schema field `color=black`. Only the price claim is source-supported; the name is not strict-equal to the gold identity and its evidence does not support the longer claimed name; rating 4.7 is a hallucinated optional value.
- `p3`: an extra unmatched record `Phantom Pods`, EUR 49.99, rating 4.9, with unsupported evidence.

### Alignment

- `g1 ↔ p1`: exact key.
- `g2 ↔ p2`: fallback similarity = `1/2 = 0.5` because price matches but product name does not; `0.5 >= τ=0.20`.
- `p3`: unmatched.

Therefore `P_R=2/3=0.667`, `R_R=2/2=1.000`, and `F1_R=0.800`.

### Strict field scoring

Gold non-null field targets: 5. Predicted non-null **schema-field** claims: 9. Correct field claims: 4 (`p1`'s three fields + `p2.price`). Therefore:

- `P_F = 4/9 = 0.444`;
- `R_F = 4/5 = 0.800`;
- `F1_F = 0.571`.

This is lower than record F1, illustrating why record discovery and field correctness must not be conflated.

### Required-field completeness

For required fields `{product_name, price}`, `g1/p1` is `2/2 = 1.0`; `g2/p2` is `1/2 = 0.5` because the product name is not correct under the strict comparator. Mean completeness is `0.750`.

### Provenance and error split

All nine schema-field predictions carry evidence objects, but only four are source-supporting. Thus:

- provenance coverage = `9/9 = 1.000`;
- conditional provenance correctness = `4/9 = 0.444`;
- joint provenance faithfulness = `4/9 = 0.444`;
- unsupported-value rate = `5/9 = 0.556`;
- there are 10 total non-null output claims after including `color`, of which one is outside the schema, so non-schema field rate = `1/10 = 0.100`.

The example demonstrates the intended separation: **record matching, field correctness, provenance support, and schema deviation are four different measurements.**

---

## Frozen protocol for R1-2

Before running the ≥3-agent wireless-headphones experiment:

1. freeze the target page snapshot(s), schema, gold records, and evidence-object format;
2. freeze `τ=0.20` and all field comparators;
3. run each agent under the same task instruction and source snapshot;
4. retain raw outputs, evidence objects, traces, latency, token/cost logs, and model/configuration metadata;
5. score with this document without changing rules after inspecting results;
6. report strict micro field F1 as primary, with record F1, required-field completeness, provenance coverage/support, UVR, NSFR, cost, and latency as separate dimensions;
7. use the H7 bootstrap only if the experimental unit structure supports it; do not manufacture a confidence interval for a single one-off page.

This freezes H1–H9 before R1-2 and prevents post-hoc metric adaptation.