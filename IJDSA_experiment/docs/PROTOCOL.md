# Protocol v3 — 3 architectures × 3 LLMs

## 1. Experimental question

This experiment compares **agent architecture** and **LLM backend** as two separate factors for schema-guided extraction from frozen headphone listing pages.

The factorial design is:

- 3 agent architectures: A1, A2, A3
- 3 LLM backends: Gemma 4 (131k local configuration), Qwen 2.5-VL 7B, Kimi K2.6
- 4 frozen listing pages
- 3 repetitions

Total formal runs: **3 × 3 × 4 × 3 = 108**.

The unit called an "agent configuration" is one architecture-model pair, e.g. `A3__kimi`. There are 9 such configurations.

## 2. Agent architectures

### A1 — Direct DOM Snapshot Agent

A1 receives one assigned product card at a time as frozen outer HTML plus a deterministic evidence catalog. The catalog contains only DOM evidence derived from that card: node ID, tag, exact CSS, exact XPath, normalized text, and selected attributes. The model returns one complete record directly. It does not browse or call tools. One bounded syntax/contract repair is allowed and fully logged.

### A2 — Schema-State Ground-and-Verify Agent

A2 is a fixed two-stage architecture. Stage 1 receives compact DOM nodes without exact selector paths and predicts values plus the DOM node ID supporting each field. Stage 2 receives only the exact nodes chosen in stage 1, including CSS/XPath/text/attributes, and must finalize the record. This architecture explicitly separates extraction planning from provenance grounding.

### A3 — Playwright-MCP ReAct Agent

A3 uses a live Chromium instance controlled through `@playwright/mcp`. The agent iteratively issues read/inspect/final actions. Exact selector paths are revealed only by an inspect operation. It must inspect supporting nodes before finalization. The browser is restricted to the assigned local frozen page and cannot access gold or external network resources.

## 3. Model backends

The same three backends are used in all three architectures, matching the frozen `config.json` and completed result metadata:

- Gemma: `gemma4-131k:latest`, Ollama local
- Qwen: `qwen2.5vl:7b`, Ollama local
- Kimi: `kimi-k2.6`, Moonshot API

Qwen 2.5-VL is used in text/DOM mode in this experiment; a separate vision-only condition is not introduced because the formal design crosses the same model set with all three architectures.

Local models use temperature 0.0. Kimi K2.6 uses non-thinking mode and provider sampling behavior required by the API. All settings are recorded in run metadata.

## 4. Task scope

Four frozen product-listing pages are evaluated: MediaMarkt DE, Saturn DE, Alternate DE, and Amazon DE. For each page, the target set is the first 10 product cards in DOM order under a fixed listing-container selector. Sponsored cards inside that listing are included.

The listing selector and card index define scope equally for all architectures. The experiment therefore evaluates extraction and evidence grounding inside known record boundaries; it does not evaluate discovery of the listing container.

Each record contains:

- `product_name`
- `price.amount`
- `price.currency`
- `rating`
- field-level evidence

Price means the current selling price payable now, not an old/struck-through price, UVP/RRP, installment, shipping amount, coupon, or financing total. Currency is EUR. Rating is a numeric 0–5 value when present, otherwise null.

## 5. Provenance contract

Every non-null field must provide one evidence object containing:

- `css`
- `xpath`
- `text_quote`
- `attribute`

CSS and XPath are both mandatory and must uniquely identify the **same DOM element**. Evidence is rejected when the pair disagrees, matches multiple elements, has a fabricated quote, points outside the aligned record card, or fails to support the predicted value.

Gold uses the same CSS+XPath convention. The supplied 40 records contain 113 non-null evidence groups. The selectors were checked against the frozen DOM; this is not a claim of independent second-human annotation unless separately documented.

## 6. Isolation and leakage controls

Gold is stored outside the served snapshot tree. A3's browser network allowlist accepts only the assigned frozen HTML route and blocks external images/scripts, service workers, arbitrary navigation, and local files. Model API secrets are not passed to the browser subprocess.

A1/A2 receive only deterministic representations of the assigned snapshot card. They do not import gold files. Their evidence catalogs expose DOM values and selectors already present in the snapshot, not annotations or target labels.

## 7. Run budgets

Per formal page run, the frozen configuration uses:

- wall-clock timeout: 3,600 s
- model HTTP timeout: 300 s
- output token cap per call: 4,096
- local context setting: 32,768
- maximum turns per card: 10
- A3: maximum 80 browser actions per page
- A1: direct generation + at most 1 bounded contract repair per card
- A2: stage-1 planning + stage-2 finalization + at most 1 bounded contract repair per card

All calls, repairs, tokens, failures, timings, and A3 browser actions are logged. Predictions are not silently rewritten after generation.

## 8. Ground truth and alignment

Gold contains 40 records. Record alignment is one-to-one using exact product name after Unicode NFKC normalization, whitespace collapse, and case folding. Duplicate names are disambiguated using valid product-name evidence/card identity, additional matching fields, and deterministic tie-breaking.

The conceptual fields flatten to four strict scoring targets: `product_name`, `price.amount`, `price.currency`, and `rating`. Null gold ratings are excluded from the non-null field denominator; hallucinated ratings are false positives.

## 9. Metrics

Primary extraction metrics:

- strict field precision, recall, F1
- record precision, recall, F1
- record completeness
- schema adherence

Provenance metrics:

- CSS/XPath selector-pair coverage
- exact quote coverage
- verified provenance precision
- verified provenance recall
- supported/unsupported field counts

H8 post-processing additionally reports:

- unsupported-value rate
- non-schema-field rate

Efficiency/behavior metrics:

- latency
- input/output tokens
- model calls where logged
- tool actions
- browser actions (A3 only)

Task success requires:

- record recall ≥ 0.90
- strict field F1 ≥ 0.85
- schema adherence = 1
- completed run

## 10. Aggregation

Each architecture-model configuration has 12 formal page runs (4 sites × 3 repetitions). `summary_table.csv` reports all 9 configurations. Separate architecture-level and model-level summaries are also generated, but those marginal means should not replace the full factorial table when interactions are important.

A 95% percentile interval for strict field F1 is computed with **2,000 site-cluster bootstrap resamples using seed 42**. Because there are only four site clusters, these intervals are exploratory and are not used for significance claims.

## 11. Reproducibility and interpretation

The freeze manifest hashes snapshots, gold, prompts, schema, configuration, schedule, agent/evaluator code, Python requirements, and the Node lockfile. Completed outputs are checksum-protected.

Two interrupted-run archive directories were retained for auditability but are excluded by the evaluator; exactly 108 scheduled rows were scored. Four snapshot HTML files differ from repository bytes only because the original Windows freeze used CRLF while Git normalized committed text to LF. Converting the committed files back to CRLF reproduces the recorded freeze hashes exactly. `.gitattributes` now marks `*.html -text` to avoid future line-ending normalization.

This is a controlled frozen-page extraction experiment, not a general claim about unrestricted Web navigation. Architecture effects should be interpreted jointly with model effects because architecture × model interactions are substantial.