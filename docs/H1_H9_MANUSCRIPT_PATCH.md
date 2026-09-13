# Manuscript Patch — H1–H9 Metric-Stack Specification

This patch targets the current `sn-article.tex` Section 7.2 (`\subsection{Proposed extraction metric stack}`) and the statistical-reporting paragraph in Section 7.4. The repository is the authoritative implementation-level supplement; the manuscript text below is the compact paper version.

---

## 1. Replace the current opening metric paragraph in §7.2

Replace the paragraph beginning `Let $G$ be the set of gold field-value pairs...` through the current definition of `unsupported-field rate` with:

```latex
Let $Y$ and $\hat Y$ denote the gold and predicted record sets and let $F$ be the declared schema fields. Evaluation first aligns records and then scores fields; alignment itself is not treated as proof that a record is correct. Each schema declares canonical identity fields $K$. After deterministic field normalization, exact canonical-key matches are aligned first. Remaining unmatched records are compared one-to-one using
\begin{equation}
\operatorname{sim}(r,\hat r)=\frac{1}{|F_r|}\sum_{f\in F_r}
\mathbb{1}[c_f(r_f,\hat r_f)=1],
\end{equation}
where $F_r$ is the set of non-null gold schema fields and $c_f$ is the predeclared field comparator; a missing predicted value contributes zero. Remaining pairs are greedily accepted in decreasing similarity order subject to one-to-one matching and a threshold $\tau$ fixed before evaluation. In the worked experiment we use $\tau=0.20$, matching the current WADE-Bench scorer. Unmatched predictions reduce record precision and unmatched gold records reduce recall; duplicate predictions cannot receive repeated credit for the same gold record. Because fallback alignment is threshold-sensitive, record F1 is treated as diagnostic and strict field F1 is the primary extraction-correctness metric.

Nested objects are scored at leaf field paths. Collection-valued fields declare in advance whether order and multiplicity matter (ordered sequence, set, or multiset), and strict field credit is awarded only when the complete normalized collection satisfies that comparator. Gold null/absent optional fields are not positive recall targets; predicting a non-null value for such a field is a false-positive field claim, whereas omitting a non-null gold value is a false negative. Missing/null required fields also reduce required-field completeness and may invalidate the schema.

Strict field precision, recall, and F1 are micro-averaged over non-null schema-field claims,
\begin{equation}
P_F=\frac{N_{\mathrm{correct}}}{N_{\mathrm{pred,nonnull}}},\quad
R_F=\frac{N_{\mathrm{correct}}}{N_{\mathrm{gold,nonnull}}},\quad
F1_F=\frac{2P_FR_F}{P_F+R_F},
\end{equation}
with unmatched predicted and gold records retained in the respective denominators. Task-macro (and, when multiple tasks share a site, site-macro) F1 is reported secondarily to expose heterogeneity. Record and provenance aggregates are labelled explicitly as micro or macro rather than using an unspecified average.

Field equivalence is defined before evaluation by a deterministic type-aware comparator: normalized strings, canonical URLs, declared numeric tolerance, money amount/currency, canonical dates, booleans, closed enums/aliases, or declared ordered/set/multiset comparison. Parse failure on both sides never implies equality. Free-text semantic equivalence, when indispensable, is a separately reported secondary analysis under a frozen rubric with the evaluator blinded to agent identity; the strict deterministic score remains primary.
```

---

## 2. Add provenance support, zero-output behavior, and the H8 split immediately after the replacement above

```latex
For each non-null predicted schema field $p$, let $A(p)$ denote whether a syntactically complete evidence object is supplied and let $S(p)$ denote whether that evidence actually supports the value against the frozen source artifact. The evidence object stores the field and record identifiers, predicted value, source URL/page identifier, snapshot and retrieval timestamps, a representation-specific locator, and a replayable transformation history (formal JSON Schema in the supplementary repository). For DOM/text evidence, $S(p)=1$ only when the page/snapshot identity matches, the locator resolves unambiguously, the quoted evidence occurs at that location, and the claimed value is either directly supported under the field comparator or reproduced by the declared deterministic transformation chain. Vision evidence uses the analogous screenshot/tile/bounding-box check; when automatic verification is unavailable, the frozen screenshot is manually adjudicated and the method is logged. Evidence availability alone therefore does not imply evidential correctness.

We report provenance coverage $\sum A(p)/N_{\mathrm{pred}}$, conditional provenance correctness $\sum S(p)/\sum A(p)$, and joint provenance faithfulness $\sum S(p)/N_{\mathrm{pred}}$, where $N_{\mathrm{pred}}$ counts non-null predictions on schema fields. We also split the earlier ``unsupported-field rate'' into two distinct errors. The \emph{unsupported-value rate} is the fraction of non-null predictions on valid schema fields for which $S(p)=0$. The \emph{non-schema-field rate} is the fraction of all non-null output claims whose leaf field path is absent from the target schema. Raw counts are reported with both rates, and schema validity remains a separate metric.

Zero-output cases are explicit. If the gold set contains at least one target but an agent predicts no records/fields, record and field precision are set to zero by convention, recall and F1 are zero, and required-field completeness is zero; provenance and prediction-error ratios with zero denominators are reported as N/A rather than as perfect scores. If both gold and prediction are legitimately empty, the task may be marked as a correct empty result, but zero-denominator record, field, and provenance ratios remain N/A. If the gold set is empty but predictions are non-empty, the claims are false positives and the task-level extraction F1 is zero.
```

---

## 3. Add the H9 worked example in §7.2 before `A practical report should include at least:`

```latex
\paragraph{Worked scoring example.}
Consider the running wireless-headphones schema with required fields \texttt{product\_name} and \texttt{price}, optional \texttt{rating}, and no additional properties. Gold contains two records: (SoundWave X1, EUR~79.99, 4.5) and (QuietBeat Pro, EUR~129.99, null). A prediction contains three records: an exact first record with valid evidence; a second record (QuietBeat Pro Headphones, EUR~129.99, 4.7) plus an extra \texttt{color} field, with only the price source-supported; and an unsupported extra record (Phantom Pods, EUR~49.99, 4.9). The first pair aligns by exact key; the second aligns by the fallback because one of its two non-null gold fields matches ($\operatorname{sim}=0.5\geq\tau$); the third prediction remains unmatched. Thus $P_R=2/3$, $R_R=1$, and $F1_R=0.800$. Across schema fields there are 5 non-null gold targets, 9 non-null predicted schema-field claims, and 4 correct claims, giving $P_F=4/9$, $R_F=4/5$, and $F1_F=0.571$. Required-field completeness is $(1+0.5)/2=0.750$. All nine schema-field claims carry evidence but only four are supported, so provenance coverage is 1.000 and joint faithfulness is $4/9=0.444$; the unsupported-value rate is $5/9=0.556$. Including the extra \texttt{color} claim gives one non-schema claim among 10 non-null output claims, hence a non-schema-field rate of 0.100. This example shows why record discovery, field correctness, provenance support, and schema deviation are reported separately. The complete machine-readable example is released with the supplementary evidence.
```

---

## 4. Replace the statistical-reporting paragraph in §7.4

Replace the paragraph beginning `Results should include repeated runs because LLM agents are stochastic...` with:

```latex
Results should include repeated runs because LLM agents are stochastic. Unless a benchmark defines a different preregistered estimator, we report 95\% paired hierarchical cluster-bootstrap intervals with 10,000 replicates. Each replicate samples sites with replacement and retains all tasks from each sampled site; when repeated stochastic runs exist for a task/system cell, runs are additionally sampled with replacement within that task. The complete aggregate metric is recomputed for every replicate, and the 2.5th and 97.5th percentiles form the interval. Pairwise system differences use the same bootstrap draws so that comparisons remain paired. If only one run per task is available, the interval reflects task/site heterogeneity but not run-to-run stochasticity; if only one site/task is evaluated, no site-level confidence interval is claimed and repeated-run dispersion is reported descriptively instead. Model, prompt, tool, website snapshot, evaluator, and metric-protocol versions must be fixed or recorded, and cost/latency distributions should be reported rather than means alone.
```

---

## 5. Supplementary implementation references

Add near the end of §7.2 or in Data Availability:

```latex
The complete operational scoring contract, zero-denominator conventions, evidence-object JSON Schema, and machine-readable worked example are released in the supplementary evidence repository (`docs/H1_H9_METRIC_SPECIFICATION.md`, `schemas/evidence_object.schema.json`, and `data/h9_worked_scoring_example.json`).
```

---

## Reviewer-item mapping

- **H1:** exact-key-first + one-to-one fallback alignment; fixed `tau`; unmatched/duplicates defined.
- **H2:** nested, collections, optional/null/missing behavior fixed.
- **H3:** primary micro + secondary task/site macro specified.
- **H4:** deterministic comparator registry; semantic judgement bounded and secondary.
- **H5:** `A(p)` separated from verified `S(p)`; evidence object formalized.
- **H6:** zero-prediction/empty-target conventions fixed.
- **H7:** 95% paired hierarchical site-cluster bootstrap, 10,000 replicates.
- **H8:** unsupported-value rate separated from non-schema-field rate.
- **H9:** complete numerical headphones-style worked example added.

This patch should be applied **before** the R1-2 three-agent experiment is scored.