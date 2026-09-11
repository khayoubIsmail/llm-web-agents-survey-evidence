# G2 — Operational Definitions for the G1 System × Requirement Audit

## Purpose

G2 fixes the coding rules that must exist **before** G1 evaluates the manuscript's universal absence claim:

> No representative reviewed system jointly demonstrates unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly as one evaluated end-to-end capability.

Without operational definitions, a system-by-requirement matrix can be made to support almost any conclusion after the fact. G2 therefore freezes the meaning of the disputed terms before candidate systems are coded.

The four reviewer-sensitive terms are:

1. field-level provenance;
2. complete dataset assembly;
3. cross-site transfer; and
4. joint evaluation.

For G1 completeness, G2 also defines the two companion requirements already present in C1-11: unfamiliar-site navigation, explicit schema coverage, and unsupported-value control.

## Coding states

Every G1 requirement cell must use exactly one of four states:

- **YES** — the requirement is directly implemented and empirically evaluated/demonstrated by the same system.
- **PARTIAL** — the system has a related capability or proxy, but does not meet the full operational definition.
- **NO** — the paper/system explicitly lacks the requirement or its design is incompatible with it.
- **NR** — not reported / insufficient evidence to decide.

These states are intentionally asymmetric:

- `NR` is **not** evidence of absence.
- `PARTIAL` is **not** upgraded to `YES` because the capability seems plausible.
- a system closes the complete contract only when every required G1 cell is `YES` and `joint evaluation = YES`.

This prevents the absence claim from being manufactured from missing reporting.

---

## G2-01 — Field-level provenance

### Operational definition

For each predicted non-null field, the system preserves an auditable link to the **exact source evidence** that supports that field value and its entity association. The locator may be a passage, DOM element/path, stable attribute, table cell, screenshot region, or equivalent source object.

A page URL or answer-level citation alone is not field-level provenance.

### Coding rule

**YES** requires all of the following:

- provenance is attached at field/value granularity;
- the locator identifies evidence that supports the value, not merely the page containing it;
- the field is associated with the intended record/entity;
- the mechanism is evaluated or verifiably demonstrated in system outputs.

**PARTIAL** applies when:

- citations exist only at answer, document, page, or record level;
- only some fields have evidence;
- locators are stored but support/association is not checked.

**NO** applies when structured outputs have no source binding or only browser/trajectory logs.

**NR** applies when provenance granularity cannot be established from the paper.

### Non-qualifying examples

- one URL for a whole product record;
- a bibliography at the end of a generated report;
- a browser history showing which pages were visited;
- a generic statement that an answer is "grounded".

### Why this definition matters

This definition separates **source discovery** from **value support**. A system can find the correct page and still attach the wrong price, date, rating, or entity value.

---

## G2-02 — Complete dataset assembly

### Operational definition

The evaluated system constructs a **multi-record dataset over a declared collection boundary** and performs the operations required to make that dataset coherent: record construction, collection coverage/completeness, normalization, duplicate/entity reconciliation, missingness/conflict handling, and final dataset output.

### Coding rule

**YES** requires:

- a declared collection boundary or gold dataset target;
- multi-record output rather than one answer/record;
- evaluated collection completeness/coverage;
- explicit normalization and duplicate/entity handling sufficient to assemble the final dataset.

**PARTIAL** applies when:

- multiple records are produced but completeness is not evaluated;
- deduplication/entity reconciliation is omitted;
- the method assumes that the source table/data have already been acquired.

**NO** applies to:

- single-answer or single-record systems;
- page-local extraction only;
- data-cleaning systems that operate on an already assembled dataset.

**NR** applies when a paper says it outputs structured data but does not establish dataset-level assembly or coverage.

### Non-qualifying examples

- returning JSON for the current page;
- extracting the first `k` results without a declared collection boundary;
- cleaning a supplied CSV;
- narrative multi-source aggregation.

### Why this definition matters

The survey's endpoint is a usable data product, not a successful page parse. A system that extracts correct individual records but silently misses pages or duplicates entities has not demonstrated complete dataset assembly.

---

## G2-03 — Cross-site transfer

### Operational definition

The **same** agent, policy, or extraction method is evaluated on held-out or previously unseen websites/site families **without site-specific redevelopment after the test sites are known**.

Site-specific redevelopment includes retraining for the target site, manually engineered selectors/wrappers, new site adapters, or equivalent hand-coded target-specific logic.

### Coding rule

**YES** requires:

- an explicit held-out/unseen website or site-family evaluation;
- the same method/policy is reused on those sites;
- no target-specific redevelopment is required.

**PARTIAL** applies when:

- several websites are evaluated but all were exposed during training/development;
- only new pages/layouts within one site are tested;
- few-shot or site-specific adaptation is required.

**NO** applies when:

- one site/template is evaluated;
- a new scraper/wrapper/selector is built per site.

**NR** applies when multiple sites are mentioned but site exposure/adaptation is unclear.

### Non-qualifying examples

- training on 100 websites and testing on those same 100;
- applying one scraper to new pages from the same template family;
- cross-task generalization on the same website.

### Distinction from unfamiliar-site navigation

A system may dynamically navigate a website with general actions yet still fail cross-site transfer because all evaluation sites were known during development. These are separate requirements in G1.

---

## G2-04 — Joint evaluation

### Operational definition

The required capabilities are demonstrated by the **same end-to-end system** under a common experimental pipeline/task set. Evidence must show that the capabilities coexist in one evaluated implementation rather than being assembled across different systems, papers, modules, or hypothetical architecture components.

### Coding rule

**YES** requires:

- one identifiable executable system/configuration;
- evidence for every requirement needed by the claim;
- the evidence belongs to the same system/run family rather than a literature-level composition.

**PARTIAL** applies when:

- several requirements are evaluated together but one or more are missing;
- separate benchmark tracks test disjoint capability subsets without demonstrating coexistence in one end-to-end configuration.

**NO** applies when:

- the claim is assembled by combining one paper's navigation, another paper's provenance, and another paper's dataset handling;
- an architecture diagram proposes components that were not evaluated together.

**NR** applies when the paper does not make clear whether the reported modules/results belong to the same executable configuration.

### Why this definition matters

G1 tests a **joint capability claim**, not whether the literature collectively contains every component. The literature already contains most components separately; the disputed statement is whether one evaluated system closes the full contract.

---

# Companion G1 requirements

## G2-05 — Unfamiliar-site navigation

The agent dynamically discovers/traverses a Web environment using general observations/actions rather than a site-specific hard-coded navigation script.

- **YES:** executable browser/site interaction with dynamic action selection on unseen or non-site-engineered Web environments.
- **PARTIAL:** offline next-action prediction, fixed benchmark sites, or substantial site-specific scaffolding.
- **NO:** static HTML extraction or hard-coded wrapper traversal.
- **NR:** navigation mechanism is unclear.

This is not the same as cross-site transfer.

## G2-06 — Explicit schema coverage

A machine-readable target schema or equivalent explicit field/constraint set is a first-class extraction contract, and the system tracks or evaluates whether required fields/records are covered.

- **YES:** schema fields/constraints govern extraction and coverage/completeness is evaluated or explicitly tracked.
- **PARTIAL:** fixed JSON/template output but no general schema input or coverage tracking.
- **NO:** free-form answer/report with implicit targets.
- **NR:** structured output exists but schema role is unclear.

JSON syntax alone does not establish schema coverage.

## G2-07 — Unsupported-value control

The system explicitly prevents, flags, nulls, abstains from, or penalizes predicted field values that lack source evidence or violate the declared extraction contract.

- **YES:** unsupported non-null fields are explicitly detected/blocked/penalized and this behavior is evaluated.
- **PARTIAL:** generic hallucination mitigation, reflection, or confidence scoring without field-specific support checks.
- **NO:** structured values can be emitted without an unsupported-value check.
- **NR:** verification is mentioned but unsupported-field behavior is unspecified.

This is complementary to field-level provenance: attaching a source locator is not enough if unsupported values can survive validation.

---

# G1 decision rule fixed by G2

For each candidate system, G1 must create one row with at least these columns:

- system / study ID;
- unfamiliar-site navigation;
- explicit schema coverage;
- field-level provenance;
- unsupported-value control;
- cross-site transfer;
- complete dataset assembly;
- joint evaluation;
- checked source locations;
- coder rationale.

The central absence claim can be retained only when:

1. every plausible counterexample has been coded using these frozen definitions;
2. no candidate system has `YES` for all six capability requirements **and** `YES` for joint evaluation;
3. `NR` cells are not interpreted as `NO`;
4. ambiguous high-risk candidates are re-read rather than downgraded by assumption;
5. all candidate studies are revalidated against final `N_SYNTH` membership.

If one system satisfies all requirements jointly, C1-11 must be revised or removed.

If no system does, the manuscript should still avoid an absolute claim about all possible literature. The defensible wording is scoped to the **representative reviewed systems under the stated operational definitions**.

## Recommended manuscript phrasing after G1 passes

> Under the operational definitions used in our system-level comparison, none of the representative reviewed systems jointly demonstrates unfamiliar-site navigation, explicit schema coverage, field-level provenance, unsupported-value control, cross-site transfer, and complete dataset assembly in one evaluated end-to-end pipeline.

This wording is stronger methodologically than "no system does X" because it is explicitly bounded by the reviewed corpus and the published coding rules.
