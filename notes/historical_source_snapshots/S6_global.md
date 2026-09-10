# S6 - LLM-Based Web Information Extraction

Generated on: 2026-05-07 23:40

---

## P0 (1 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P0\2025-04 - WebLists- Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents.md

# S6 P0 Paper Note — WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents

## Metadata

- **Title:** WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents
- **Short name:** WebLists / BardeenAgent
- **Authors:** Arth Bohra, Manvel Saroyan, Danil Melkozerov, Vahe Karufanyan, Gabriel Maher, Pascal Weinberger, Artem Harutyunyan, Giovanni Campagna
- **Year:** 2025
- **Venue/status:** arXiv / CoRR preprint; no confirmed final peer-reviewed venue found in this check
- **DOI:** 10.48550/arXiv.2504.12682
- **arXiv ID:** arXiv:2504.12682
- **Thesis section:** S6 — LLM-based Agents for Web Data Extraction
- **Priority:** P0
- **BibTeX key:** `bohra2025weblists`

---

## Simple understanding

This paper is the **P0 anchor for S6** because it directly targets your thesis core:

```text
LLM-based agents for structured web data extraction
```

Most web-agent papers focus on:

```text
navigation
form filling
shopping
question answering
general browser tasks
```

WebLists shifts the focus to:

```text
interactive schema-bound structured data extraction across live websites
```

This means the agent must:

```text
1. navigate to the correct webpage
2. interact with filters, pagination, forms, or content hubs
3. reveal the relevant data
4. extract complete datasets
5. respect a predefined schema
6. output structured machine-readable rows
```

The paper also proposes **BardeenAgent**, which records one successful extraction process and converts it into a repeatable executable program using CSS selectors and list loops.

---

## Four-note template

- **Core idea:**  
  WebLists introduces a benchmark for interactive schema-bound web data extraction, and BardeenAgent solves it by converting agent execution into reusable extraction programs that exploit regular HTML/list structure.

- **Key finding:**  
  Existing LLM search systems and SOTA web agents perform poorly on structured extraction: LLM+Search reaches only about 3.3% overall recall, Agent-E about 12.1%, Wilbur about 30.5%, while BardeenAgent reaches 66.2% recall and reduces amortized cost per correct output row by more than 3×.

- **Limitation connected to thesis:**  
  BardeenAgent substantially improves recall and cost, but still struggles with complex widgets, wrong list selection, overly broad selectors, precision/recall trade-offs, dynamic websites, and extraction verification beyond exact URL matching.

- **Connects to:**  
  S5.2 DOM/HTML representation, S5.3 decomposition and planning, S5.4 training/executable agents, S5.5 reliability failures, S6 structured extraction, S8 deployment and cost.

- **Use in thesis:**  
  Use as the main S6 P0 anchor paper because it defines the missing extraction-focused benchmark and proposes an agent architecture specifically optimized for structured web data extraction.

---

## Why this paper is P0 for S6

S6 is about:

```text
LLM-based agents for web data extraction
```

WebLists is P0 because it is one of the clearest papers that separates **web navigation** from **web extraction**.

The paper argues that existing web-agent benchmarks are insufficient because:

```text
they focus mostly on navigation and transaction tasks
they rarely require structured machine-readable output
they use too few websites
they do not test extraction completeness at scale
they often evaluate answers rather than full datasets
```

WebLists introduces the exact problem your thesis needs:

```text
interactive schema-bound data extraction across websites
```

This makes it more central to your thesis than general web-agent navigation papers.

---

## Main problem defined by the paper

The problem is:

```text
given:
  a high-level extraction task
  a target website
  a desired schema

the agent must:
  navigate to the correct part of the website
  interact with the page to expose the data
  extract all matching rows
  output them according to the schema
```

This is different from question answering.

In question answering, the agent may only need one final answer.

In WebLists, the agent must return a complete table.

---

## WebLists benchmark

## 1. Benchmark scope

WebLists contains:

```text
200 tasks
50 live websites
4 use cases
deterministic evaluation scripts
schema-bound output
```

The four use cases are:

```text
1. Blogs / product updates
2. Testimonials / customer case studies
3. Jobs
4. Job categories / filtered jobs
```

## 2. Output schemas

The benchmark requires structured rows.

Examples:

```text
Blogs:
- Update Title
- Update URL

Testimonials:
- Name
- Testimonial
- URL

Jobs:
- Job Title
- Job URL

Job Categories:
- Job Title
- Job URL
```

The URL column acts as an identifier for matching extracted rows to ground truth.

## 3. Why WebLists differs from older benchmarks

Compared with WebShop, Mind2Web, WebArena, and WebVoyager, WebLists is important because it combines:

```text
live websites
deterministic evaluation
many websites
structured output
data completeness
interactive extraction
```

The paper compares benchmarks as follows:

```text
WebShop       → simulated, 1 website
Mind2Web      → recorded demonstrations, 137 websites
WebArena      → simulated, 4 websites
WebVoyager    → live, 15 websites, LLM judge
WebLists      → live, 50 websites, deterministic evaluation
```

This is a strong argument for S6: extraction needs different evaluation from general navigation.

---

## BardeenAgent

## 1. Core idea

BardeenAgent does not ask the LLM to extract every row directly.

Instead, it uses a two-phase approach:

```text
Record phase:
  the agent navigates and extracts the first item
  it records actions and selectors

Replay phase:
  the recorded actions are converted into an executable program
  list structures become loops
  pagination is handled programmatically
  the program extracts all rows
```

This is the key insight:

```text
do not call the LLM once per item;
use the LLM to discover the extraction program,
then run the program at scale.
```

## 2. Why this matters

This solves a major extraction problem:

```text
LLMs have limited output length
LLM calls compound errors over many items
large datasets require repeated extraction
```

BardeenAgent avoids repeated LLM decisions by converting one successful execution into a reusable program.

This connects to classical scraping:

```text
wrapper induction
DOM extraction
CSS selectors
pagination handling
structured scraping
```

but with an LLM-based agent that can discover the right page and extraction procedure interactively.

---

## Key tools and operations

BardeenAgent uses a DSL with tools such as:

```text
Click(element)
TypeInput(element, value, enter)
GoBack()
EnterList(elements, description, pagination)
ExitList()
SaveCurrentURL(column)
SaveText(element, column, regex)
SaveLink(element, column)
AnswerQuestion(element, column, question)
Finish()
Fail(errorCode, errorMessage)
```

The most important tool is:

```text
EnterList(elements, description, pagination)
```

It allows the agent to identify a repeated list structure and record operations only on the first element. During replay, those operations are applied to all elements.

---

## CSS selector generation

BardeenAgent needs selectors that generalize across list items and pages.

It uses two methods:

```text
1. heuristic selector generation
2. LLM-based CSS selector generation
```

## 1. Heuristic selectors

The heuristic method samples selectors from:

```text
parent-child structure
position
HTML classes
IDs
attributes
tag names
```

## 2. LLM-based selectors

The LLM-based selector model is used when list structures are complex, for example:

```text
blog posts across different categories
headers mixed with list items
irregular page layouts
```

The selector model receives:

```text
goal
schema
HTML of least common ancestor
list description
```

and generates a CSS selector for the relevant items.

This is central to BardeenAgent’s success because extraction at scale depends on selecting the right repeated structure.

---

## Schema-bound data table creation

BardeenAgent creates schema-bound tables in three ways:

```text
1. Direct extraction
2. Regular expression extraction
3. Question answering fallback
```

## 1. Direct extraction

Use when the desired value appears directly in an HTML element or attribute.

Example:

```text
SaveText(element, "Job Title")
SaveLink(element, "Job URL")
```

## 2. Regular expression extraction

Use when only part of the text is needed.

Examples:

```text
email
price
date
salary
```

## 3. Question answering fallback

Use when the value is not directly available as a clean element.

Example:

```text
AnswerQuestion(article, "Summary", "Summarize this article")
```

This is more expensive because it uses an LLM for each item, but it is useful when structured extraction requires interpretation.

---

## Main results

## 1. Precision and recall

Overall results:

```text
Agent-E:
  Precision 44.3
  Recall 12.1

Wilbur:
  Precision 82.0
  Recall 30.5

LLM + Search:
  Precision 19.6
  Recall 3.3

BardeenAgent:
  Precision 72.5
  Recall 66.2

BardeenAgent without selector model:
  Precision 70.9
  Recall 35.6
```

The key result is:

```text
BardeenAgent more than doubles the recall of the best existing web agent baseline.
```

## 2. Cost

BardeenAgent has higher per-task cost, but much lower cost per correct output row.

Per correct output row:

```text
Agent-E:       3.21 cents
Wilbur:        4.55 cents
BardeenAgent:  1.07 cents
```

This is important because extraction tasks are dataset-scale tasks, not single-answer tasks.

The right cost metric is not only:

```text
cost per task
```

but:

```text
cost per correct extracted row
```

This is very relevant for S8 deployment.

## 3. Question answering

BardeenAgent also reaches about 60% accuracy on question-answering tasks, showing that the executable extraction approach does not completely sacrifice QA ability.

However, BardeenAgent is less optimized for precise question answering than extraction.

---

## Important figures / tables

## Figure 1 — Record/replay framework

Figure 1 shows the central idea:

```text
Recording phase:
  navigate to page
  enter list mode
  extract first item
  record actions

Replay phase:
  convert actions into program
  loop over list items/pages
  output structured table
```

This is the most important figure for S6.

## Table 1 — Use cases and schemas

Table 1 defines the four extraction tasks:

```text
Blogs
Testimonials
Jobs
Job Categories
```

and their output columns.

This table should be cited when explaining why WebLists is extraction-focused.

## Table 2 — Benchmark comparison

Table 2 compares WebLists to WebShop, Mind2Web, WebArena, and WebVoyager.

This is useful for arguing that existing web-agent benchmarks do not adequately evaluate structured extraction.

## Table 3 — Main benchmark results

Table 3 is the main evidence for BardeenAgent’s improvement:

```text
BardeenAgent recall: 66.2
Wilbur recall: 30.5
Agent-E recall: 12.1
LLM+Search recall: 3.3
```

## Table 4 — Cost per output row

Table 4 supports the deployment argument:

```text
BardeenAgent reduces cost per correct output row by more than 3×.
```

## Figure 2 — Selector extraction example

Figure 2 shows how a simplified DOM is converted into CSS selectors:

```text
List: #blog li.blog-item
Update Title: :scope .title > a
Update URL: :scope .title > a
Author: :scope .author
Pagination: a.load-more
```

This figure directly connects LLM agents to classical web scraping.

---

## Connection to S5.2

S5.2 discussed perception, representation, DOM, screenshots, and grounding.

WebLists/BardeenAgent depends heavily on S5.2:

```text
DOM representation
CSS selectors
list detection
pagination controls
HTML regularity
scoped extraction
selector robustness
```

The key connection is:

```text
structured extraction requires not only seeing the page,
but finding the repeated structure behind the page.
```

---

## Connection to S5.3

S5.3 discussed planning.

WebLists requires planning because the agent must:

```text
navigate to the right data page
configure filters
enter list mode
extract the first item
handle pagination
replay extraction across all items
```

The strongest connection is to WebDART, because WebDART decomposes complex web tasks into:

```text
navigation
information extraction
execution
```

WebLists makes this decomposition concrete for structured data extraction.

---

## Connection to S5.4

S5.4 discussed training and generalization.

WebLists is relevant because it reveals a missing training target:

```text
agents need to be trained/evaluated on complete structured extraction,
not only navigation success.
```

Future S5.4 work could use WebLists-style tasks to train:

```text
selector generation
list detection
schema adherence
pagination handling
field-level verification
program synthesis for extraction
```

---

## Connection to S5.5

S5.5 discussed failure modes.

WebLists reveals extraction-specific failures:

```text
low recall
early termination
missing pages
wrong list selection
overly broad CSS selectors
incorrect filtering
missing URLs
index/search mismatch
outdated indexed data
LLM output limit
compounding errors from per-page extraction
```

These are different from ordinary navigation failures.

For S5.5, WebLists adds:

```text
extraction reliability is not the same as task success reliability.
```

---

## Connection to S8

S8 discusses deployment.

WebLists is highly relevant because extraction is a practical business use case.

Deployment lessons:

```text
cost per correct row matters
complete recall matters
schema consistency matters
deterministic evaluation matters
repeatable programs are more scalable than repeated LLM calls
```

But deployment gaps remain:

```text
handling complex widgets
selector brittleness
dynamic website changes
CAPTCHAs
authentication
legal/ethical scraping constraints
human validation
data quality monitoring
```

---

## Limitations connected to thesis

The main limitations are:

```text
1. BardeenAgent still has imperfect precision.
2. Wrong list selection can extract irrelevant rows.
3. CSS selectors can be too broad or too narrow.
4. Complex forms and widgets remain difficult.
5. The benchmark is limited to 50 cloud-company websites.
6. Evaluation focuses heavily on URL matching.
7. The method is text/DOM-based, not multimodal.
8. QA fallback can return imprecise answers.
9. The system still needs stronger validation for business-critical extraction.
10. Live websites change continuously.
```

For your thesis, this is not a weakness. It is a strong gap statement.

---

## Thesis-ready paragraph

Bohra et al. introduce **WebLists**, a benchmark designed specifically for interactive, schema-bound structured data extraction from live websites. Unlike most web-agent benchmarks, which focus on navigation, transactions, or question answering, WebLists requires agents to navigate to the relevant webpage, interact with filters or pagination, extract complete datasets, and output rows under a predefined schema. The benchmark contains 200 tasks across 50 live websites and four business-oriented use cases: blogs, testimonials, jobs, and filtered job categories. The paper also proposes **BardeenAgent**, an executable LLM-agent framework that records a successful extraction trajectory, converts it into a reusable program, and replays it using generalizable CSS selectors and list loops. This approach exploits the regular structure of HTML and avoids repeated LLM calls for every item. Empirically, BardeenAgent reaches 66.2% overall recall on WebLists, more than doubling Wilbur’s 30.5% recall and greatly outperforming Agent-E and LLM+Search. It also reduces amortized cost per correct output row by more than 3×. For this thesis, WebLists is a key S6 anchor because it reframes web automation around structured extraction completeness, schema adherence, and scalable replay, not only task completion. However, remaining limitations around selector reliability, complex widgets, filtering, precision, dynamic sites, and extraction verification motivate further research on robust, source-verifiable web data extraction agents.

---

## One-sentence summary

WebLists shows that general web agents are weak at complete structured web data extraction, and BardeenAgent improves extraction by turning one successful interaction into a reusable CSS-selector-based executable program.

---

## BibTeX

```bibtex
@article{bohra2025weblists,
  title         = {WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents},
  author        = {Bohra, Arth and Saroyan, Manvel and Melkozerov, Danil and Karufanyan, Vahe and Maher, Gabriel and Weinberger, Pascal and Harutyunyan, Artem and Campagna, Giovanni},
  journal       = {arXiv preprint arXiv:2504.12682},
  year          = {2025},
  doi           = {10.48550/arXiv.2504.12682},
  url           = {https://arxiv.org/abs/2504.12682},
  eprint        = {2504.12682},
  archivePrefix = {arXiv}
}
```

---

## Source links

- https://arxiv.org/abs/2504.12682


---

## P1 (26 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\_archived_duplicates_or_moved\2025-04 - BardeenAgent-WebLists -- archived_duplicate_with_S6_P0.md

# Archived duplicate / moved paper — BardeenAgent / WebLists

The uploaded file:

```text
2025-04 - BardeenAgent- A Web Agent for Accurate Large-Scale Web Data Extraction.pdf
```

is the same research line as the S6 P0 anchor:

```text
WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents
```

Decision:

```text
Do not cite BardeenAgent/WebLists again as S6 P1.
Keep it as S6 P0 only.
```

Use citation key already assigned in S6 P0:

```text
bohra2025weblists
```

Reason:

```text
WebLists/BardeenAgent is the S6 cornerstone because it directly defines interactive schema-bound web extraction and BardeenAgent.
Repeating it in S6 P1 would create duplicate citation and synthesis confusion.
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\01 - 2024-09 - AutoScraper- A Progressive Understanding Web Agent for Web Scraper Generation.md

# AutoScraper: A Progressive Understanding Web Agent for Web Scraper Generation

## Metadata

- **Short name:** AutoScraper
- **Authors:** Wenhao Huang, Zhouhong Gu, Chenghao Peng, Zhixu Li, Jiaqing Liang, Yanghua Xiao, Liqian Wen, Zulong Chen
- **Year used for thesis:** 2024
- **Venue/status:** EMNLP 2024 Main Conference
- **DOI:** 10.18653/v1/2024.emnlp-main.141
- **arXiv ID:** arXiv:2404.12753
- **Venue/status source:** ACL Anthology + arXiv + official GitHub
- **S6 cluster:** LLM-generated reusable web scrapers
- **Priority:** P1
- **BibTeX key:** `huang2024autoscraper`
- **Section role:** scraper generation / executable extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a two-stage LLM framework for generating reusable web scrapers by progressively understanding long HTML documents and synthesizing page-level scrapers into website-level extraction logic.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a two-stage LLM framework for generating reusable web scrapers by progressively understanding long HTML documents and synthesizing page-level scrapers into website-level extraction logic.

- **Key finding:**  
  AutoScraper consistently outperforms baselines across three datasets and introduces an executability metric that better measures whether a generated scraper works across multiple webpages of the same site.

- **Limitation connected to thesis:**  
  Restricted mainly to vertical web information extraction; it can miss multi-valued fields and struggles when webpages in the same site are not structurally generalizable.

- **Connects to:**  
  WebLists/BardeenAgent, SCRIBES, ReaderLM-v2, S5.2 DOM understanding, S5.3 executable planning, S8 cost-efficient deployment.

- **Use in thesis:**  
  Use as the first S6 P1 method paper showing the bridge between LLM agents and classical wrapper/scraper generation.

---

## Detailed notes

- Frames scraper generation as a reusable alternative to per-page LLM extraction.
- Combines wrapper-based extraction and language-agent-based extraction.
- Progressive generation handles long HTML by exploiting hierarchical structure.
- Synthesis integrates multiple generated scrapers from different pages into a cohesive site-level scraper.
- Introduces an executability metric because per-page extraction F1 does not capture whether a scraper is usable across a website.
- Experiments cover multiple LLMs and datasets, with AutoScraper outperforming baselines in zero-shot settings.
- Efficiency improves when many pages from the same website must be extracted; the paper estimates the break-even threshold on SWDE.
- Error analysis identifies non-generalizable webpage structures and missed multi-valued fields.

---

## Figures / tables to remember

- Figure 1 compares wrapper-based methods, language-agent-based direct extraction, and AutoScraper’s reusable wrapper-generation paradigm.
- Figure 2 presents AutoScraper’s progressive generation and synthesis pipeline.
- Table 6 estimates the page-count threshold where reusable scrapers become more efficient than direct LLM extraction.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
scraper generation / executable extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Restricted mainly to vertical web information extraction; it can miss multi-valued fields and struggles when webpages in the same site are not structurally generalizable.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

AutoScraper contributes to S6 by addressing scraper generation / executable extraction. Introduces a two-stage LLM framework for generating reusable web scrapers by progressively understanding long HTML documents and synthesizing page-level scrapers into website-level extraction logic. The main result is that AutoScraper consistently outperforms baselines across three datasets and introduces an executability metric that better measures whether a generated scraper works across multiple webpages of the same site. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Restricted mainly to vertical web information extraction; it can miss multi-valued fields and struggles when webpages in the same site are not structurally generalizable. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

AutoScraper shows that **Introduces a two-stage LLM framework for generating reusable web scrapers by progressively understanding long HTML documents and synthesizing page-level scrapers into website-level extraction logic**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@inproceedings{huang2024autoscraper,
  title     = {AutoScraper: A Progressive Understanding Web Agent for Web Scraper Generation},
  author    = {Wenhao Huang, Zhouhong Gu, Chenghao Peng, Zhixu Li, Jiaqing Liang, Yanghua Xiao, Liqian Wen, Zulong Chen},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  year      = {2024},
  doi       = {10.18653/v1/2024.emnlp-main.141},
  eprint        = {2404.12753},
  archivePrefix = {arXiv},
  url       = {https://aclanthology.org/2024.emnlp-main.141/}
}
```

---

## Source links

- https://aclanthology.org/2024.emnlp-main.141/
- https://arxiv.org/abs/2404.12753


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\02 - 2024-10 - Infogent- An Agent-Based Framework for Web Information Aggregation.md

# Infogent: An Agent-Based Framework for Web Information Aggregation

## Metadata

- **Short name:** Infogent
- **Authors:** Revanth Gangi Reddy, Sagnik Mukherjee, Jeonghwan Kim, Zhenhailong Wang, Dilek Hakkani-Tür, Heng Ji
- **Year used for thesis:** 2025
- **Venue/status:** Findings of NAACL 2025
- **DOI:** 10.18653/v1/2025.findings-naacl.318
- **arXiv ID:** arXiv:2410.19054
- **Venue/status source:** ACL Anthology + arXiv + project page
- **S6 cluster:** web information aggregation
- **Priority:** P1
- **BibTeX key:** `reddy2025infogent`
- **Section role:** web information aggregation / multi-source extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a modular Navigator–Extractor–Aggregator framework for open-ended web information aggregation across multiple sources under direct API-driven and interactive visual access settings.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a modular Navigator–Extractor–Aggregator framework for open-ended web information aggregation across multiple sources under direct API-driven and interactive visual access settings.

- **Key finding:**  
  Infogent beats a SOTA multi-agent search framework by 7% on FRAMES under Direct API-Driven Access and improves over an information-seeking web agent by 4.3% on AssistantBench under Interactive Visual Access.

- **Limitation connected to thesis:**  
  It focuses on aggregation and final answer quality rather than schema-bound row-level extraction, provenance, or complete dataset extraction.

- **Connects to:**  
  S5.3 planning/backtracking, S5.7 deep research, S6 aggregation, S7/S8 verification and source coverage.

- **Use in thesis:**  
  Use as the S6 P1 paper connecting structured web extraction to broader web information aggregation and multi-source synthesis.

---

## Detailed notes

- Separates web information aggregation from linear task-completion web navigation.
- Uses three components: Navigator, Extractor, and Aggregator.
- Adds an enhanced action set so the Navigator can backtrack and transfer control when aggregation is needed.
- Uses feedback-driven navigation: Aggregator feedback guides what the Navigator should explore next.
- Supports Direct API-driven Access using search APIs and text extraction.
- Supports Interactive Visual Access using screenshots and browser interaction when paywalls, logins, or visually dependent interactions appear.
- Evaluates on AssistantBench, FRAMES, and FanOutQA.
- Relevant to thesis because many extraction tasks require multi-source evidence, not one page.

---

## Figures / tables to remember

- Figure 1 shows the two access settings and the Navigator–Extractor–Aggregator feedback loop.
- Main results compare Infogent against multi-agent search and information-seeking web-agent baselines.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
web information aggregation / multi-source extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It focuses on aggregation and final answer quality rather than schema-bound row-level extraction, provenance, or complete dataset extraction.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

Infogent contributes to S6 by addressing web information aggregation / multi-source extraction. Introduces a modular Navigator–Extractor–Aggregator framework for open-ended web information aggregation across multiple sources under direct API-driven and interactive visual access settings. The main result is that Infogent beats a SOTA multi-agent search framework by 7% on FRAMES under Direct API-Driven Access and improves over an information-seeking web agent by 4.3% on AssistantBench under Interactive Visual Access. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, It focuses on aggregation and final answer quality rather than schema-bound row-level extraction, provenance, or complete dataset extraction. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

Infogent shows that **Introduces a modular Navigator–Extractor–Aggregator framework for open-ended web information aggregation across multiple sources under direct API-driven and interactive visual access settings**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@inproceedings{reddy2025infogent,
  title     = {Infogent: An Agent-Based Framework for Web Information Aggregation},
  author    = {Revanth Gangi Reddy, Sagnik Mukherjee, Jeonghwan Kim, Zhenhailong Wang, Dilek Hakkani-Tür, Heng Ji},
  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
  year      = {2025},
  doi       = {10.18653/v1/2025.findings-naacl.318},
  eprint        = {2410.19054},
  archivePrefix = {arXiv},
  url       = {https://aclanthology.org/2025.findings-naacl.318/}
}
```

---

## Source links

- https://aclanthology.org/2025.findings-naacl.318/
- https://arxiv.org/abs/2410.19054


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\03 - 2025-03 - ReaderLM-v2- Small Language Model for HTML to Markdown and JSON.md

# ReaderLM-v2: Small Language Model for HTML to Markdown and JSON

## Metadata

- **Short name:** ReaderLM-v2
- **Authors:** Feng Wang, Zesheng Shi, Bo Wang, Nan Wang, Han Xiao
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **DOI:** 10.48550/arXiv.2503.01151
- **arXiv ID:** arXiv:2503.01151
- **Venue/status source:** arXiv + Jina AI project/blog
- **S6 cluster:** HTML-to-Markdown and schema-guided JSON extraction
- **Priority:** P1
- **BibTeX key:** `wang2025readerlmv2`
- **Section role:** content cleaning / HTML-to-JSON extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a compact 1.5B model for converting messy long-context HTML into clean Markdown or JSON using a three-stage DRAFT–REFINE–CRITIQUE data synthesis pipeline and multi-stage training.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a compact 1.5B model for converting messy long-context HTML into clean Markdown or JSON using a three-stage DRAFT–REFINE–CRITIQUE data synthesis pipeline and multi-stage training.

- **Key finding:**  
  ReaderLM-v2 outperforms GPT-4o and larger models by 15–20% on curated HTML extraction benchmarks, especially for documents above 100K tokens, while remaining computationally efficient.

- **Limitation connected to thesis:**  
  Strong for HTML cleaning and conversion, but not a full autonomous web agent: it does not navigate, interact with filters/pagination, or verify extracted values across live websites.

- **Connects to:**  
  S5.2 webpage representation, S6 content extraction infrastructure, IndexLM, ScrapeGraphAI-100k, RAG context preparation.

- **Use in thesis:**  
  Use as the S6 P1 infrastructure paper for turning noisy HTML into LLM-ready Markdown/JSON.

---

## Detailed notes

- Targets HTML main content conversion, instruction-guided Markdown extraction, and schema-guided JSON extraction.
- Processes long documents up to 512K tokens.
- Uses DRAFT–REFINE–CRITIQUE synthetic data generation.
- Training includes continuous pretraining, supervised fine-tuning, direct preference optimization, and self-play iterative tuning.
- Shows very strong HTML-to-Markdown performance compared with GPT-4o, Gemini, and Qwen baselines.
- JSON extraction is evaluated with tree-based precision/recall/F1 and pass-rate metrics.
- Best positioned as a content-preparation model for web agents and RAG systems.
- Useful for S6 because extraction agents often need cleaned Markdown/JSON before reasoning.

---

## Figures / tables to remember

- Figure 1 shows the DRAFT–REFINE–CRITIQUE synthetic data and training pipeline.
- Tables 1–2 report Markdown and JSON extraction results.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
content cleaning / HTML-to-JSON extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Strong for HTML cleaning and conversion, but not a full autonomous web agent: it does not navigate, interact with filters/pagination, or verify extracted values across live websites.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

ReaderLM-v2 contributes to S6 by addressing content cleaning / HTML-to-JSON extraction. Introduces a compact 1.5B model for converting messy long-context HTML into clean Markdown or JSON using a three-stage DRAFT–REFINE–CRITIQUE data synthesis pipeline and multi-stage training. The main result is that ReaderLM-v2 outperforms GPT-4o and larger models by 15–20% on curated HTML extraction benchmarks, especially for documents above 100K tokens, while remaining computationally efficient. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Strong for HTML cleaning and conversion, but not a full autonomous web agent: it does not navigate, interact with filters/pagination, or verify extracted values across live websites. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

ReaderLM-v2 shows that **Introduces a compact 1.5B model for converting messy long-context HTML into clean Markdown or JSON using a three-stage DRAFT–REFINE–CRITIQUE data synthesis pipeline and multi-stage training**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{wang2025readerlmv2,
  title         = {ReaderLM-v2: Small Language Model for HTML to Markdown and JSON},
  author        = {Feng Wang, Zesheng Shi, Bo Wang, Nan Wang, Han Xiao},
  journal       = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year          = {2025},
  doi           = {10.48550/arXiv.2503.01151},
  eprint        = {2503.01151},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2503.01151}
}
```

---

## Source links

- https://arxiv.org/abs/2503.01151
- https://arxiv.org/abs/2503.01151


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\04 - 2025-07 - STRUCTSENSE- A Task-Agnostic Agentic Framework for Structured Information Extraction.md

# STRUCTSENSE: A Task-Agnostic Agentic Framework for Structured Information Extraction with Human-In-The-Loop Evaluation and Benchmarking

## Metadata

- **Short name:** STRUCTSENSE
- **Authors:** Tek Raj Chhetri, Yibei Chen, Puja Trivedi, Dorota Jarecka, Saif Haobsh, Patrick Ray, Lydia Ng, Satrajit S. Ghosh
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint / OpenReview entry; no final peer-reviewed venue confirmed in this check
- **DOI:** 10.48550/arXiv.2507.03674
- **arXiv ID:** arXiv:2507.03674
- **Venue/status source:** arXiv + OpenReview + GitHub
- **S6 cluster:** agentic structured information extraction with ontology and HITL
- **Priority:** P1
- **BibTeX key:** `chhetri2025structsense`
- **Section role:** HITL and ontology-grounded structured extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a modular multi-agent framework for task-agnostic structured information extraction using an Extractor Agent, Alignment Agent, Judge Agent, and Feedback Agent with ontology grounding and human-in-the-loop validation.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a modular multi-agent framework for task-agnostic structured information extraction using an Extractor Agent, Alignment Agent, Judge Agent, and Feedback Agent with ontology grounding and human-in-the-loop validation.

- **Key finding:**  
  Demonstrates that ontology-guided agentic extraction can support diverse neuroscience IE tasks, including NER, survey-to-schema conversion, and literature-review resource/metadata extraction.

- **Limitation connected to thesis:**  
  Focused on scientific documents and neuroscience rather than live web scraping; evaluation is domain-specific and not centered on interactive website extraction.

- **Connects to:**  
  S6 schema-grounded extraction, S7 verification/HITL, S8 FAIR data and auditability.

- **Use in thesis:**  
  Use as the S6 paper for ontology grounding, judge agents, and human-in-the-loop validation in structured extraction.

---

## Detailed notes

- Targets structured information extraction from unstructured scientific sources.
- Uses four specialized agents: extractor, alignment, judge, and feedback.
- The Alignment Agent maps extracted terms to ontologies or knowledge graphs.
- The Judge Agent evaluates extraction and alignment outputs.
- The Feedback Agent incorporates human correction and updates memory.
- Designed to be task-agnostic through task and agent configurations.
- Emphasizes FAIR-aligned outputs, semantic interoperability, and auditability.
- Useful for thesis because it addresses schema/ontology grounding and human validation, two gaps in web extraction agents.

---

## Figures / tables to remember

- Figure 1 shows the STRUCTSENSE architecture: Extractor Agent, Alignment Agent, Judge Agent, Feedback Agent, ontology database, memory, and human feedback.
- Table 1 illustrates ontology disambiguation for the term cortex across neuroscience and plant biology.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
HITL and ontology-grounded structured extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Focused on scientific documents and neuroscience rather than live web scraping; evaluation is domain-specific and not centered on interactive website extraction.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

STRUCTSENSE contributes to S6 by addressing HITL and ontology-grounded structured extraction. Introduces a modular multi-agent framework for task-agnostic structured information extraction using an Extractor Agent, Alignment Agent, Judge Agent, and Feedback Agent with ontology grounding and human-in-the-loop validation. The main result is that Demonstrates that ontology-guided agentic extraction can support diverse neuroscience IE tasks, including NER, survey-to-schema conversion, and literature-review resource/metadata extraction. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Focused on scientific documents and neuroscience rather than live web scraping; evaluation is domain-specific and not centered on interactive website extraction. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

STRUCTSENSE shows that **Introduces a modular multi-agent framework for task-agnostic structured information extraction using an Extractor Agent, Alignment Agent, Judge Agent, and Feedback Agent with ontology grounding and human-in-the-loop validation**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{chhetri2025structsense,
  title         = {STRUCTSENSE: A Task-Agnostic Agentic Framework for Structured Information Extraction with Human-In-The-Loop Evaluation and Benchmarking},
  author        = {Tek Raj Chhetri, Yibei Chen, Puja Trivedi, Dorota Jarecka, Saif Haobsh, Patrick Ray, Lydia Ng, Satrajit S. Ghosh},
  journal       = {arXiv preprint / OpenReview entry; no final peer-reviewed venue confirmed in this check},
  year          = {2025},
  doi           = {10.48550/arXiv.2507.03674},
  eprint        = {2507.03674},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2507.03674}
}
```

---

## Source links

- https://arxiv.org/abs/2507.03674
- https://arxiv.org/abs/2507.03674


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\05 - 2025-09 - A Systematic Review of Web Scraping- Techniques LLM-Enhanced Approaches Performance Metrics and Legal-Ethical Issues.md

# A Systematic Review of Web Scraping: Techniques, LLM-Enhanced Approaches, Performance Metrics, and Legal-Ethical Issues

## Metadata

- **Short name:** Systematic Review of Web Scraping
- **Authors:** Navroz Kaur Kahlon, Williamjeet Singh
- **Year used for thesis:** 2026
- **Venue/status:** Data & Knowledge Engineering, Volume 164, July 2026, Article 102598; earlier SSRN preprint posted September 2025
- **DOI:** 10.1016/j.datak.2026.102598
- **arXiv ID:** Not applicable
- **Venue/status source:** ScienceDirect search result + SSRN preprint page
- **S6 cluster:** survey/background: scraping techniques, metrics, legal and ethical issues
- **Priority:** P1
- **BibTeX key:** `kahlon2026systematicwebscraping`
- **Section role:** background survey / metrics / legal-ethical grounding

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Systematically reviews web scraping techniques, applications, LLM-enhanced scraping, performance metrics, and legal/ethical issues across 260 studies.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Systematically reviews web scraping techniques, applications, LLM-enhanced scraping, performance metrics, and legal/ethical issues across 260 studies.

- **Key finding:**  
  Provides a broad taxonomy of classical and LLM-enhanced scraping, identifies performance metrics, application areas, tools, and legal/ethical constraints.

- **Limitation connected to thesis:**  
  It is a broad survey rather than a method paper; it does not provide a new extraction agent, benchmark, or empirical system for LLM-based web extraction.

- **Connects to:**  
  S6.1 foundations, S8 legal/ethical deployment, S5.5 reliability, S7 verification and responsible extraction.

- **Use in thesis:**  
  Use as background support for classical scraping foundations, metrics, applications, and legal/ethical constraints.

---

## Detailed notes

- Reviews 260 studies from journals, conferences, and workshops.
- Compares itself to previous surveys and claims broader coverage of LLM-based scraping, legal/ethical issues, metrics, and applications.
- Defines web scraping as automated extraction and transformation of web data into structured formats such as CSV, JSON, and Excel.
- Surveys traditional techniques, tools/software, LLM-based systems, RAG-style approaches, and LLMOps integrations.
- Includes performance metrics such as accuracy, precision, recall, F1, execution time, completeness, robustness, and scalability.
- Discusses application areas such as e-commerce, academics, health, tourism, and corpus construction.
- Highlights privacy, terms of service, institutional oversight, data validity, and legal ambiguity.
- Important for thesis background but not the S6 core anchor.

---

## Figures / tables to remember

- Table 1 compares this review against previous web scraping surveys.
- Figure 4 gives the research-question hierarchy.
- Section 3.3 summarizes performance metrics used in web scraping studies.
- Sections 6–8 discuss implications, limitations, and legal/ethical issues.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
background survey / metrics / legal-ethical grounding
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It is a broad survey rather than a method paper; it does not provide a new extraction agent, benchmark, or empirical system for LLM-based web extraction.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

Systematic Review of Web Scraping contributes to S6 by addressing background survey / metrics / legal-ethical grounding. Systematically reviews web scraping techniques, applications, LLM-enhanced scraping, performance metrics, and legal/ethical issues across 260 studies. The main result is that Provides a broad taxonomy of classical and LLM-enhanced scraping, identifies performance metrics, application areas, tools, and legal/ethical constraints. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, It is a broad survey rather than a method paper; it does not provide a new extraction agent, benchmark, or empirical system for LLM-based web extraction. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

Systematic Review of Web Scraping shows that **Systematically reviews web scraping techniques, applications, LLM-enhanced scraping, performance metrics, and legal/ethical issues across 260 studies**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{kahlon2026systematicwebscraping,
  title   = {A Systematic Review of Web Scraping: Techniques, LLM-Enhanced Approaches, Performance Metrics, and Legal-Ethical Issues},
  author  = {Navroz Kaur Kahlon, Williamjeet Singh},
  journal = {Data & Knowledge Engineering},
  volume  = {164},
  pages   = {102598},
  year    = {2026},
  doi     = {10.1016/j.datak.2026.102598},
  url     = {https://www.sciencedirect.com/science/article/abs/pii/S0169023X26000455}
}
```

---

## Source links

- https://www.sciencedirect.com/science/article/abs/pii/S0169023X26000455
- SSRN preprint: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5429131


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\06 - 2025-10 - SCRIBES- Web-Scale Script-Based Semi-Structured Data Extraction with Reinforcement Learning.md

# SCRIBES: Web-Scale Script-Based Semi-Structured Data Extraction with Reinforcement Learning

## Metadata

- **Short name:** SCRIBES
- **Authors:** Shicheng Liu, Kai Sun, Lisheng Fu, Xilun Chen, Xinyuan Zhang, Zhaojiang Lin, Rulin Shao, Yue Liu, Anuj Kumar, Wen-tau Yih, Xin Luna Dong
- **Year used for thesis:** 2026
- **Venue/status:** ICLR 2026 Poster
- **DOI:** 10.48550/arXiv.2510.01832
- **arXiv ID:** arXiv:2510.01832
- **Venue/status source:** OpenReview ICLR 2026 + arXiv
- **S6 cluster:** RL-trained reusable extraction scripts for semi-structured web data
- **Priority:** P1
- **BibTeX key:** `liu2026scribes`
- **Section role:** RL-based web-scale script extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Trains models to generate reusable extraction scripts for groups of structurally similar webpages, using cross-page layout generalization as a reinforcement learning reward.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Trains models to generate reusable extraction scripts for groups of structurally similar webpages, using cross-page layout generalization as a reinforcement learning reward.

- **Key finding:**  
  Outperforms strong agentic baselines by more than 13% in script quality and boosts downstream QA accuracy by more than 4% for GPT-4o with extracted triples.

- **Limitation connected to thesis:**  
  Targets semi-structured HTML tables/lists/infoboxes and depends on group-level structural similarity; complex/free-form pages and noisy synthetic annotations remain challenging.

- **Connects to:**  
  AutoScraper, WebLists/BardeenAgent, ReaderLM-v2, IndexLM, S5.4 RL, S6 web-scale extraction.

- **Use in thesis:**  
  Use as the strongest S6 P1 method after WebLists for scalable script-based semi-structured data extraction.

---

## Detailed notes

- Extracts triples from semi-structured HTML such as tables, lists, and infoboxes.
- Uses one representative webpage to generate a script that should apply to other pages in the same structural group.
- Reward combines self-score and cross-score across webpages in a group, encouraging generalizable scripts.
- Uses GRPO/RLVR style training with fuzzy triple-level F1 as the training reward.
- Adds CommonCrawl failure-case training with synthetic LLM annotations after initial training on gold annotated data.
- HTML deduplication collapses repeated HTML blocks while preserving structure, reducing token usage from over 114k to under 17k on average in the profiled set.
- Best Q-32B + CC model reaches 33.2 F1_LM overall and 32.4 holdout F1_LM in the reported setting.
- Downstream QA improves when SCRIBES triples are appended to flattened HTML; GPT-4o improves from 82.5 to 86.6.

---

## Figures / tables to remember

- Figure 1 shows training-time script generation, reward calculation across in-group pages, and inference-time generalization to unseen groups.
- Figure 2 shows structurally similar SEC pages under the same website.
- Figure 3 shows the CommonCrawl data pipeline.
- Table 1 reports script generation results; Table 4 shows QA gains from SCRIBES triples.
- Figure 5 and Table 5 show the HTML deduplication mechanism and token reduction.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
RL-based web-scale script extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Targets semi-structured HTML tables/lists/infoboxes and depends on group-level structural similarity; complex/free-form pages and noisy synthetic annotations remain challenging.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

SCRIBES contributes to S6 by addressing RL-based web-scale script extraction. Trains models to generate reusable extraction scripts for groups of structurally similar webpages, using cross-page layout generalization as a reinforcement learning reward. The main result is that Outperforms strong agentic baselines by more than 13% in script quality and boosts downstream QA accuracy by more than 4% for GPT-4o with extracted triples. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Targets semi-structured HTML tables/lists/infoboxes and depends on group-level structural similarity; complex/free-form pages and noisy synthetic annotations remain challenging. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

SCRIBES shows that **Trains models to generate reusable extraction scripts for groups of structurally similar webpages, using cross-page layout generalization as a reinforcement learning reward**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@inproceedings{liu2026scribes,
  title     = {SCRIBES: Web-Scale Script-Based Semi-Structured Data Extraction with Reinforcement Learning},
  author    = {Shicheng Liu, Kai Sun, Lisheng Fu, Xilun Chen, Xinyuan Zhang, Zhaojiang Lin, Rulin Shao, Yue Liu, Anuj Kumar, Wen-tau Yih, Xin Luna Dong},
  booktitle = {International Conference on Learning Representations},
  year      = {2026},
  eprint        = {2510.01832},
  archivePrefix = {arXiv},
  url       = {https://openreview.net/forum?id=gQSnEIA3Z3}
}
```

---

## Source links

- https://openreview.net/forum?id=gQSnEIA3Z3
- https://arxiv.org/abs/2510.01832


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\07 - 2025-12 - An Index-based Approach for Efficient and Effective Web Content Extraction.md

# An Index-based Approach for Efficient and Effective Web Content Extraction

## Metadata

- **Short name:** IndexLM / Index-based Web Content Extraction
- **Authors:** Yihan Chen, Benfeng Xu, Xiaorui Wang, Zhendong Mao
- **Year used for thesis:** 2025
- **Venue/status:** CoRR/arXiv preprint; no final peer-reviewed venue confirmed in this check
- **DOI:** 10.48550/arXiv.2512.06641
- **arXiv ID:** arXiv:2512.06641
- **Venue/status source:** arXiv + DBLP/CoRR result
- **S6 cluster:** index-based query-relevant content extraction for RAG/web agents
- **Priority:** P1
- **BibTeX key:** `chen2025indexwebextraction`
- **Section role:** efficient content extraction / context compression

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Reframes web content extraction from token-by-token generation into discriminative index prediction over structure-aware HTML blocks.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Reframes web content extraction from token-by-token generation into discriminative index prediction over structure-aware HTML blocks.

- **Key finding:**  
  IndexLM improves RAG QA accuracy and is much faster than generative extraction methods; IndexLM-4B reaches 87.40 F1 on main-content extraction and 31.69 F1 on query-relevant extraction in direct evaluation.

- **Limitation connected to thesis:**  
  It extracts relevant content spans rather than schema-bound structured records; it supports context reduction but not full extraction workflows with forms, pagination, provenance, or schema validation.

- **Connects to:**  
  ReaderLM-v2, HtmlRAG, S5.2 context compression, S6 extraction infrastructure, S8 cost/latency.

- **Use in thesis:**  
  Use as the S6 P1 paper for efficient content selection and context compression before extraction or web-agent reasoning.

---

## Detailed notes

- Partitions cleaned HTML into addressable structure-aware blocks with numeric indices.
- IndexLM outputs closed index intervals such as [[1,2],[3,5]] rather than generating extracted content.
- Supports both main content extraction and query-relevant extraction.
- Decouples extraction latency from output content length because the model emits short index intervals.
- Uses Qwen3-based models at 0.6B, 1.7B, and 4B scales.
- Evaluated as a post-retrieval processing module in RAG QA on HotpotQA, NQ, TriviaQA, Musique, and MultiHopRAG.
- IndexLM improves average QA F1 over chunk-rerank, HtmlRAG, ReaderLM-v2, Firecrawl Extract, and prompt-based extraction baselines in the reported settings.
- Useful for agents that must read many long webpages under limited context budgets.

---

## Figures / tables to remember

- Figure 1 plots effectiveness versus latency and shows IndexLM models in the more efficient/effective region.
- Figure 2 compares index-based extraction with heuristic rules, chunk-rerank, and generative extraction.
- Figure 3 shows the full pipeline: index construction, index extraction, post-processing.
- Figure 4 gives a simplified indexed block example.
- Tables 2–3 report RAG QA and direct extraction results.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
efficient content extraction / context compression
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It extracts relevant content spans rather than schema-bound structured records; it supports context reduction but not full extraction workflows with forms, pagination, provenance, or schema validation.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

IndexLM / Index-based Web Content Extraction contributes to S6 by addressing efficient content extraction / context compression. Reframes web content extraction from token-by-token generation into discriminative index prediction over structure-aware HTML blocks. The main result is that IndexLM improves RAG QA accuracy and is much faster than generative extraction methods; IndexLM-4B reaches 87.40 F1 on main-content extraction and 31.69 F1 on query-relevant extraction in direct evaluation. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, It extracts relevant content spans rather than schema-bound structured records; it supports context reduction but not full extraction workflows with forms, pagination, provenance, or schema validation. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

IndexLM / Index-based Web Content Extraction shows that **Reframes web content extraction from token-by-token generation into discriminative index prediction over structure-aware HTML blocks**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{chen2025indexwebextraction,
  title         = {An Index-based Approach for Efficient and Effective Web Content Extraction},
  author        = {Yihan Chen, Benfeng Xu, Xiaorui Wang, Zhendong Mao},
  journal       = {CoRR/arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year          = {2025},
  doi           = {10.48550/arXiv.2512.06641},
  eprint        = {2512.06641},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2512.06641}
}
```

---

## Source links

- https://arxiv.org/abs/2512.06641
- https://arxiv.org/abs/2512.06641


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\08 - 2026-01 - Beyond BeautifulSoup- Benchmarking LLM-Powered Web Scraping for Everyday Users.md

# Beyond BeautifulSoup: Benchmarking LLM-Powered Web Scraping for Everyday Users

## Metadata

- **Short name:** Beyond BeautifulSoup
- **Authors:** Arth Bhardwaj, Nirav Diwan, Gang Wang
- **Year used for thesis:** 2026
- **Venue/status:** AICS Workshop at AAAI 2026 + arXiv preprint
- **DOI:** 10.48550/arXiv.2601.06301
- **arXiv ID:** arXiv:2601.06301
- **Venue/status source:** arXiv + Gang Wang publications page + AICS 2026 program
- **S6 cluster:** benchmarking LLM-powered scraping accessibility and security tiers
- **Priority:** P1
- **BibTeX key:** `bhardwaj2026beyondbeautifulsoup`
- **Section role:** benchmark / usability / scraping democratization

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Benchmarks what novice users can accomplish with off-the-shelf LLM-assisted scripting and end-to-end LLM agents across 35 websites and five security/complexity tiers.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Benchmarks what novice users can accomplish with off-the-shelf LLM-assisted scripting and end-to-end LLM agents across 35 websites and five security/complexity tiers.

- **Key finding:**  
  Traditional LLM-assisted scripting is fastest for static HTML, while end-to-end agents are more accessible and successful on complex, authenticated, protected, and CAPTCHA-like scenarios.

- **Limitation connected to thesis:**  
  Small benchmark, limited tools, limited hardware/session conditions, and a focus on accessibility rather than extraction correctness, schema adherence, or large-scale scraping reliability.

- **Connects to:**  
  AutoScraper, WebLists, S5.5 reliability, S8 safety/legal/anti-bot implications.

- **Use in thesis:**  
  Use as a S6/S8 bridge paper: it shows how LLM agents change practical scraping capability and risk for everyday users.

---

## Detailed notes

- Defines two workflows: LLM-assisted scripting and end-to-end LLM agents.
- LLM-assisted scripting uses LLM-generated BeautifulSoup/Scrapy scripts but leaves execution and debugging to the user.
- End-to-end agents use Claude and Simular.ai to navigate and extract through integrated tools.
- Benchmarks 35 websites across simple HTML, complex HTML, simple authentication, complex authentication, and CAPTCHA categories.
- Measures extraction success rate, execution time, and manual effort required.
- Traditional tools achieve high success and low latency for static sites.
- Agents are slower but handle authentication, dynamic UI, and protected workflows that basic BeautifulSoup/Scrapy workflows cannot reasonably support for novices.
- Frames LLM-powered scraping as both a benign capability amplifier and an abuse/defense concern.

---

## Figures / tables to remember

- Figure 1 shows the benchmark design for LLM-assisted scripting versus end-to-end LLM agents.
- Table 1 defines the five website difficulty tiers.
- Table 2 reports extraction success rate across categories.
- Table 3 reports manual effort required.
- Figure 2 reports execution time on a log scale.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
benchmark / usability / scraping democratization
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Small benchmark, limited tools, limited hardware/session conditions, and a focus on accessibility rather than extraction correctness, schema adherence, or large-scale scraping reliability.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

Beyond BeautifulSoup contributes to S6 by addressing benchmark / usability / scraping democratization. Benchmarks what novice users can accomplish with off-the-shelf LLM-assisted scripting and end-to-end LLM agents across 35 websites and five security/complexity tiers. The main result is that Traditional LLM-assisted scripting is fastest for static HTML, while end-to-end agents are more accessible and successful on complex, authenticated, protected, and CAPTCHA-like scenarios. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Small benchmark, limited tools, limited hardware/session conditions, and a focus on accessibility rather than extraction correctness, schema adherence, or large-scale scraping reliability. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

Beyond BeautifulSoup shows that **Benchmarks what novice users can accomplish with off-the-shelf LLM-assisted scripting and end-to-end LLM agents across 35 websites and five security/complexity tiers**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@inproceedings{bhardwaj2026beyondbeautifulsoup,
  title     = {Beyond BeautifulSoup: Benchmarking LLM-Powered Web Scraping for Everyday Users},
  author    = {Arth Bhardwaj, Nirav Diwan, Gang Wang},
  booktitle = {Artificial Intelligence for Cyber Security Workshop at AAAI 2026},
  year      = {2026},
  eprint        = {2601.06301},
  archivePrefix = {arXiv},
  url       = {https://arxiv.org/abs/2601.06301}
}
```

---

## Source links

- https://arxiv.org/abs/2601.06301
- https://arxiv.org/abs/2601.06301


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\09 - 2026-02 - ScrapeGraphAI-100k- A Large-Scale Dataset for LLM-Based Web Information Extraction.md

# ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction

## Metadata

- **Short name:** ScrapeGraphAI-100k
- **Authors:** William Brach, Francesco Zuppichini, Marco Vinciguerra, Lorenzo Padoan
- **Year used for thesis:** 2026
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **DOI:** 10.48550/arXiv.2602.15189
- **arXiv ID:** arXiv:2602.15189
- **Venue/status source:** arXiv + Hugging Face / project release
- **S6 cluster:** large-scale real-world LLM extraction dataset
- **Priority:** P1
- **BibTeX key:** `brach2026scrapegraphai100k`
- **Section role:** dataset / schema-constrained extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a 93,695-example real-world dataset of LLM web extraction events derived from 9M opt-in ScrapeGraphAI telemetry events, including Markdown content, prompt, JSON schema, LLM response, and complexity/validation metadata.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a 93,695-example real-world dataset of LLM web extraction events derived from 9M opt-in ScrapeGraphAI telemetry events, including Markdown content, prompt, JSON schema, LLM response, and complexity/validation metadata.

- **Key finding:**  
  Shows that schema complexity drives extraction failures and that fine-tuning a 1.7B model narrows the gap to 30B baselines on structural extraction metrics.

- **Limitation connected to thesis:**  
  Dataset reflects ScrapeGraphAI telemetry and is skewed toward GPT-4o-mini; it uses Markdown rather than raw HTML/DOM/visual inputs and schema validity does not guarantee semantic correctness.

- **Connects to:**  
  ReaderLM-v2, STRUCTSENSE, IndexLM, S5.4 fine-tuning, S6 schema-constrained extraction, S8 reproducibility.

- **Use in thesis:**  
  Use as the S6 P1 dataset paper for training, benchmarking, and failure analysis of schema-constrained LLM web extraction.

---

## Detailed notes

- Starts from about 9M opt-in production telemetry events collected during Q2–Q3 2025.
- After cleaning, deduplication, and balancing by schema, releases 93,695 examples.
- Each example contains source/content, natural-language prompt, JSON schema, LLM response, validation flag, model metadata, execution time, and schema complexity metrics.
- Retains invalid responses, enabling failure-mode analysis.
- Computes schema depth, key count, element count, cyclomatic complexity, and composite complexity score.
- Finds validation declines sharply at high schema complexity thresholds such as depth ≥ 7 and key count ≥ 200.
- Fine-tuned Qwen3-1.7B improves schema compliance and key F1, approaching 30B models on structural metrics.
- Highlights a structural-semantic gap: models can produce correct JSON skeletons while extracting imperfect values.

---

## Figures / tables to remember

- Figure 1 shows schema complexity distributions.
- Figure 2 shows validation rate declines as schema complexity increases.
- Tables 1–2 summarize dataset fields and descriptive statistics.
- Table 3 compares ScrapeGraphAI-100k with existing datasets.
- Table 4 reports fine-tuning results.
- Figures 5–6 in the appendix show metric correlations and language distribution.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
dataset / schema-constrained extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Dataset reflects ScrapeGraphAI telemetry and is skewed toward GPT-4o-mini; it uses Markdown rather than raw HTML/DOM/visual inputs and schema validity does not guarantee semantic correctness.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

ScrapeGraphAI-100k contributes to S6 by addressing dataset / schema-constrained extraction. Introduces a 93,695-example real-world dataset of LLM web extraction events derived from 9M opt-in ScrapeGraphAI telemetry events, including Markdown content, prompt, JSON schema, LLM response, and complexity/validation metadata. The main result is that Shows that schema complexity drives extraction failures and that fine-tuning a 1.7B model narrows the gap to 30B baselines on structural extraction metrics. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Dataset reflects ScrapeGraphAI telemetry and is skewed toward GPT-4o-mini; it uses Markdown rather than raw HTML/DOM/visual inputs and schema validity does not guarantee semantic correctness. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

ScrapeGraphAI-100k shows that **Introduces a 93,695-example real-world dataset of LLM web extraction events derived from 9M opt-in ScrapeGraphAI telemetry events, including Markdown content, prompt, JSON schema, LLM response, and complexity/validation metadata**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{brach2026scrapegraphai100k,
  title         = {ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction},
  author        = {William Brach, Francesco Zuppichini, Marco Vinciguerra, Lorenzo Padoan},
  journal       = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year          = {2026},
  doi           = {10.48550/arXiv.2602.15189},
  eprint        = {2602.15189},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2602.15189}
}
```

---

## Source links

- https://arxiv.org/abs/2602.15189
- https://arxiv.org/abs/2602.15189


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\2025-05 - NEXT-EVAL- Next Evaluation of Traditional and LLM Web Data Record Extraction.md

# NEXT-EVAL: Next Evaluation of Traditional and LLM Web Data Record Extraction

## Metadata

- **Short name:** NEXT-EVAL
- **Authors:** Soyeon Kim, Namhee Kim, Yeonwoo Jeong
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint. Project pages mention NeurIPS 2025 / in review, but no final accepted peer-reviewed proceedings status was confirmed in this check.
- **DOI:** 10.48550/arXiv.2505.17125
- **arXiv ID:** arXiv:2505.17125
- **S6 cluster:** evaluation benchmark for traditional and LLM-based web data record extraction
- **Priority:** P1
- **BibTeX key:** `kim2025nexteval`
- **Section role:** extraction evaluation / record extraction benchmark

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
NEXT-EVAL builds a concrete evaluation framework for web data record extraction,
allowing traditional heuristic extraction methods and LLM-based extraction methods
to be compared fairly on the same DOM-grounded task.
```

The paper focuses on **web data record extraction**, meaning extraction of repeated structured records from webpages, such as:

```text
product listings
company directories
contact tables
record lists
structured web tables
```

Its main contribution is not a new extraction agent, but a **benchmarking and evaluation framework**.

---

## Four-note template

- **Core idea:**  
  NEXT-EVAL creates a reproducible benchmark framework for evaluating traditional and LLM-based web data record extraction using MHTML snapshots, XPath-based labels, DOM-preserving preprocessing, and structure-aware metrics.

- **Key finding:**  
  Flat JSON input gives LLMs the best extraction performance among the tested input formats, reaching an F1 score of **0.9567** with minimal hallucination compared with Slimmed HTML and Hierarchical JSON.

- **Limitation connected to thesis:**  
  NEXT-EVAL improves evaluation rigor for web data record extraction, but it does not solve interactive navigation, schema-bound multi-page extraction, source provenance, live-web robustness, or verification of extracted values beyond DOM-position matching.

- **Connects to:**  
  WebLists/BardeenAgent, AutoScraper, SCRIBES, ReaderLM-v2, IndexLM, ScrapeGraphAI-100k, S5.1 evaluation, S5.5 reliability, S6 extraction evaluation, S8 deployment evaluation.

- **Use in thesis:**  
  Use as the S6 P1 evaluation paper for record extraction, especially when discussing why extraction systems need structure-aware metrics and DOM-grounded labels rather than only text-level exact matching.

---

## Why this paper is important for S6

S6 focuses on:

```text
LLM-based web information extraction and aggregation
```

NEXT-EVAL is important because extraction papers need reliable evaluation. Without a clear evaluation protocol, it is difficult to compare:

```text
traditional algorithms
DOM/tree-based extraction
heuristic record detection
LLM zero-shot extraction
LLM extraction using transformed HTML/JSON inputs
```

The paper argues that existing evaluation is limited by:

```text
static benchmarks
domain-specific datasets
opaque scoring practices
difficulty comparing traditional and LLM methods
lack of consistent DOM-grounded supervision
```

NEXT-EVAL addresses this by creating an evaluation framework from arbitrary MHTML snapshots and using XPath-based supervision labels.

---

## Main contribution

## 1. Reproducible evaluation dataset generation

NEXT-EVAL systematically generates evaluation datasets from:

```text
arbitrary MHTML snapshots
```

This matters because MHTML snapshots preserve webpage content in a reproducible form. For extraction evaluation, this avoids one of the major problems of live-web benchmarks:

```text
the page changes between runs
```

For the thesis, this supports the S8 idea that reproducibility is a major challenge in web-agent evaluation.

---

## 2. XPath-based supervision labels

The framework annotates extraction targets using:

```text
XPath-based labels
```

This is important because web data record extraction is not only about matching output text. The system should extract the correct **DOM-positioned record**, not hallucinate a plausible text answer.

XPath labels allow evaluation to measure whether the system selected the correct structural locations in the page.

This is directly relevant to your thesis because generalized extraction agents must preserve:

```text
where the value came from
which page element supports it
which record/list/table it belongs to
```

---

## 3. Structure-aware metrics

NEXT-EVAL uses structure-aware metrics for consistent scoring.

The paper’s key evaluation concern is hallucination:

```text
text hallucination
positional hallucination
```

The framework is designed to prevent text hallucination and focus evaluation on whether the model extracts the correct DOM positions.

This is important because LLMs can generate correct-looking records that are not actually grounded in the page.

For S6, this supports the claim:

```text
extraction evaluation must be source-grounded,
not only text-output based.
```

---

## 4. DOM-preserving preprocessing formats

NEXT-EVAL compares different input formats for LLM-based extraction:

```text
Slimmed HTML
Hierarchical JSON
Flat JSON
```

### Slimmed HTML

This format reduces the raw HTML size while trying to preserve important DOM semantics.

### Hierarchical JSON

This preserves nested DOM structure in a JSON representation.

### Flat JSON

This flattens the DOM into key-value pairs, typically where the key is an XPath-like location and the value is the text content.

The important result is:

```text
Flat JSON gives the best extraction accuracy.
```

The reported headline result is:

```text
Flat JSON F1 = 0.9567
```

This suggests that LLMs benefit when webpage structure is converted into an explicit, compact, position-aware representation.

---

## 5. Synthetic dataset creation

NEXT-EVAL also creates a public synthetic dataset by:

```text
transforming DOM structures
modifying content
```

This is useful because extraction evaluation needs controlled diversity.

Synthetic transformation can test whether methods are robust to:

```text
layout variations
DOM changes
content changes
record order changes
structural perturbations
```

For your thesis, this supports the idea that extraction benchmarks should include controlled transformations, not only static pages.

---

## 6. Benchmarking traditional and LLM methods

NEXT-EVAL benchmarks:

```text
deterministic heuristic algorithms
off-the-shelf LLMs
```

across different DOM-preserving input formats.

This is valuable because your thesis covers both:

```text
classical web extraction / scraping
and
LLM-based agentic extraction
```

NEXT-EVAL gives a way to compare these paradigms under one evaluation framework.

---

## Figures / tables to remember

The paper is especially useful for these visual ideas:

```text
1. Evaluation pipeline:
   MHTML snapshot → preprocessing → XPath labels → extraction → structure-aware scoring

2. Input-format comparison:
   Slimmed HTML vs Hierarchical JSON vs Flat JSON

3. Extraction-performance comparison:
   traditional heuristics vs off-the-shelf LLMs

4. Hallucination-aware evaluation:
   preventing text hallucination and measuring DOM-position correctness
```

The most important result to remember is:

```text
Flat JSON input achieves F1 = 0.9567
```

---

## Thesis relevance

NEXT-EVAL supports the S6 claim that **web extraction evaluation must be different from ordinary QA evaluation**.

A web data extraction system should be judged by:

```text
record-level correctness
field-level correctness
DOM/source grounding
structure preservation
hallucination control
layout robustness
schema/record consistency
```

For your thesis, NEXT-EVAL is useful because it gives evaluation language for:

```text
source-grounded extraction
DOM-positioned evidence
structure-aware metrics
record extraction fairness
traditional-vs-LLM comparison
```

It is especially relevant to your core thesis problem:

```text
generalized web automation and data extraction
```

because generalized extraction cannot rely only on final text answers. It needs to know whether the extracted data is actually supported by the webpage structure.

---

## Limitation as thesis gap

NEXT-EVAL is strong for evaluation, but it is not a full solution.

It does not fully solve:

```text
interactive navigation before extraction
pagination and multi-page extraction
filter interaction
login/authentication flows
visual-DOM mismatch
source provenance across multiple pages
schema-bound extraction with complex nested outputs
semantic correctness of extracted values
live-web drift
human-in-the-loop validation
deployment cost and safety
```

For the thesis, the limitation is:

```text
NEXT-EVAL improves extraction evaluation, but generalized web extraction agents still need
an end-to-end architecture that combines navigation, interaction, extraction, provenance,
verification, and robust deployment.
```

---

## Connection to S6 P0 WebLists

WebLists evaluates interactive schema-bound extraction from live websites.

NEXT-EVAL complements WebLists by focusing on:

```text
record extraction evaluation
DOM/XPath-grounded labels
input-format comparison
hallucination-aware scoring
traditional-vs-LLM benchmarking
```

So the relationship is:

```text
WebLists = task/benchmark for interactive structured extraction
NEXT-EVAL = evaluation framework for DOM-grounded record extraction
```

Use both together in S6.

---

## Connection to other S6 P1 papers

| Paper | Connection |
|---|---|
| AutoScraper | Both evaluate scraper/extractor generation; NEXT-EVAL adds structure-aware evaluation |
| SCRIBES | Both care about reusable extraction over structurally similar webpages |
| ReaderLM-v2 | NEXT-EVAL tests how input representation affects extraction quality |
| IndexLM | Both preserve structure and avoid naive text-only extraction |
| ScrapeGraphAI-100k | Both are useful for schema/record extraction evaluation, but ScrapeGraphAI-100k is dataset/training-focused |
| STRUCTSENSE | Both support evaluation/validation; STRUCTSENSE adds HITL and ontology alignment |
| Beyond BeautifulSoup | NEXT-EVAL is evaluation-focused; Beyond BeautifulSoup is practical usability/security-focused |

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.1** | Evaluation design, benchmark realism, scoring reliability |
| **S5.2** | HTML/DOM representation and Flat JSON as structure-preserving input |
| **S5.5** | Hallucination, extraction failure, evaluation failure |
| **S6** | Main role: record extraction evaluation |
| **S7** | Verification, provenance, hallucination prevention |
| **S8** | Reproducibility, live-web drift, deployment evaluation |

---

## Thesis-ready paragraph

Kim et al. introduce **NEXT-EVAL**, a benchmark and evaluation framework for comparing traditional and LLM-based web data record extraction methods. The framework addresses a key weakness of existing extraction evaluation: static, domain-specific benchmarks and opaque scoring make it difficult to compare heuristic DOM-based methods with LLM-based zero-shot extraction. NEXT-EVAL generates evaluation datasets from arbitrary MHTML snapshots, annotates XPath-based supervision labels, and uses structure-aware metrics to evaluate whether extracted records correspond to the correct webpage positions. It also compares multiple DOM-preserving preprocessing strategies, including Slimmed HTML, Hierarchical JSON, and Flat JSON. The main result is that Flat JSON provides the strongest representation for LLM-based extraction, achieving an F1 score of 0.9567 with minimal hallucination. For this thesis, NEXT-EVAL is important because it shows that web extraction evaluation must be source-grounded and structure-aware, not only text-output based. However, the framework does not solve interactive navigation, multi-page extraction, provenance tracking, schema-level semantic verification, or live-web robustness. It therefore complements WebLists by strengthening the evaluation side of agentic web data extraction.

---

## One-sentence summary

NEXT-EVAL shows that fair evaluation of web data record extraction requires DOM-grounded, structure-aware metrics, and that Flat JSON is a strong input representation for LLM-based record extraction.

---

## BibTeX

```bibtex
@article{kim2025nexteval,
  title         = {NEXT-EVAL: Next Evaluation of Traditional and LLM Web Data Record Extraction},
  author        = {Kim, Soyeon and Kim, Namhee and Jeong, Yeonwoo},
  journal       = {arXiv preprint arXiv:2505.17125},
  year          = {2025},
  doi           = {10.48550/arXiv.2505.17125},
  url           = {https://arxiv.org/abs/2505.17125},
  eprint        = {2505.17125},
  archivePrefix = {arXiv}
}
```

---

## Source links

- https://arxiv.org/abs/2505.17125
- https://github.com/wordbricks/next-eval


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\_archived_duplicates_or_moved\2025-04 - BardeenAgent-WebLists -- archived_duplicate_with_S6_P0.md

# Archived duplicate / moved paper — BardeenAgent / WebLists

The uploaded file:

```text
2025-04 - BardeenAgent- A Web Agent for Accurate Large-Scale Web Data Extraction.pdf
```

is the same research line as the S6 P0 anchor:

```text
WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents
```

Decision:

```text
Do not cite BardeenAgent/WebLists again as S6 P1.
Keep it as S6 P0 only.
```

Use citation key already assigned in S6 P0:

```text
bohra2025weblists
```

Reason:

```text
WebLists/BardeenAgent is the S6 cornerstone because it directly defines interactive schema-bound web extraction and BardeenAgent.
Repeating it in S6 P1 would create duplicate citation and synthesis confusion.
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\01 - 2024-09 - AutoScraper- A Progressive Understanding Web Agent for Web Scraper Generation.md

# AutoScraper: A Progressive Understanding Web Agent for Web Scraper Generation

## Metadata

- **Short name:** AutoScraper
- **Authors:** Wenhao Huang, Zhouhong Gu, Chenghao Peng, Zhixu Li, Jiaqing Liang, Yanghua Xiao, Liqian Wen, Zulong Chen
- **Year used for thesis:** 2024
- **Venue/status:** EMNLP 2024 Main Conference
- **DOI:** 10.18653/v1/2024.emnlp-main.141
- **arXiv ID:** arXiv:2404.12753
- **Venue/status source:** ACL Anthology + arXiv + official GitHub
- **S6 cluster:** LLM-generated reusable web scrapers
- **Priority:** P1
- **BibTeX key:** `huang2024autoscraper`
- **Section role:** scraper generation / executable extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a two-stage LLM framework for generating reusable web scrapers by progressively understanding long HTML documents and synthesizing page-level scrapers into website-level extraction logic.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a two-stage LLM framework for generating reusable web scrapers by progressively understanding long HTML documents and synthesizing page-level scrapers into website-level extraction logic.

- **Key finding:**  
  AutoScraper consistently outperforms baselines across three datasets and introduces an executability metric that better measures whether a generated scraper works across multiple webpages of the same site.

- **Limitation connected to thesis:**  
  Restricted mainly to vertical web information extraction; it can miss multi-valued fields and struggles when webpages in the same site are not structurally generalizable.

- **Connects to:**  
  WebLists/BardeenAgent, SCRIBES, ReaderLM-v2, S5.2 DOM understanding, S5.3 executable planning, S8 cost-efficient deployment.

- **Use in thesis:**  
  Use as the first S6 P1 method paper showing the bridge between LLM agents and classical wrapper/scraper generation.

---

## Detailed notes

- Frames scraper generation as a reusable alternative to per-page LLM extraction.
- Combines wrapper-based extraction and language-agent-based extraction.
- Progressive generation handles long HTML by exploiting hierarchical structure.
- Synthesis integrates multiple generated scrapers from different pages into a cohesive site-level scraper.
- Introduces an executability metric because per-page extraction F1 does not capture whether a scraper is usable across a website.
- Experiments cover multiple LLMs and datasets, with AutoScraper outperforming baselines in zero-shot settings.
- Efficiency improves when many pages from the same website must be extracted; the paper estimates the break-even threshold on SWDE.
- Error analysis identifies non-generalizable webpage structures and missed multi-valued fields.

---

## Figures / tables to remember

- Figure 1 compares wrapper-based methods, language-agent-based direct extraction, and AutoScraper’s reusable wrapper-generation paradigm.
- Figure 2 presents AutoScraper’s progressive generation and synthesis pipeline.
- Table 6 estimates the page-count threshold where reusable scrapers become more efficient than direct LLM extraction.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
scraper generation / executable extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Restricted mainly to vertical web information extraction; it can miss multi-valued fields and struggles when webpages in the same site are not structurally generalizable.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

AutoScraper contributes to S6 by addressing scraper generation / executable extraction. Introduces a two-stage LLM framework for generating reusable web scrapers by progressively understanding long HTML documents and synthesizing page-level scrapers into website-level extraction logic. The main result is that AutoScraper consistently outperforms baselines across three datasets and introduces an executability metric that better measures whether a generated scraper works across multiple webpages of the same site. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Restricted mainly to vertical web information extraction; it can miss multi-valued fields and struggles when webpages in the same site are not structurally generalizable. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

AutoScraper shows that **Introduces a two-stage LLM framework for generating reusable web scrapers by progressively understanding long HTML documents and synthesizing page-level scrapers into website-level extraction logic**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@inproceedings{huang2024autoscraper,
  title     = {AutoScraper: A Progressive Understanding Web Agent for Web Scraper Generation},
  author    = {Wenhao Huang, Zhouhong Gu, Chenghao Peng, Zhixu Li, Jiaqing Liang, Yanghua Xiao, Liqian Wen, Zulong Chen},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  year      = {2024},
  doi       = {10.18653/v1/2024.emnlp-main.141},
  eprint        = {2404.12753},
  archivePrefix = {arXiv},
  url       = {https://aclanthology.org/2024.emnlp-main.141/}
}
```

---

## Source links

- https://aclanthology.org/2024.emnlp-main.141/
- https://arxiv.org/abs/2404.12753


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\02 - 2024-10 - Infogent- An Agent-Based Framework for Web Information Aggregation.md

# Infogent: An Agent-Based Framework for Web Information Aggregation

## Metadata

- **Short name:** Infogent
- **Authors:** Revanth Gangi Reddy, Sagnik Mukherjee, Jeonghwan Kim, Zhenhailong Wang, Dilek Hakkani-Tür, Heng Ji
- **Year used for thesis:** 2025
- **Venue/status:** Findings of NAACL 2025
- **DOI:** 10.18653/v1/2025.findings-naacl.318
- **arXiv ID:** arXiv:2410.19054
- **Venue/status source:** ACL Anthology + arXiv + project page
- **S6 cluster:** web information aggregation
- **Priority:** P1
- **BibTeX key:** `reddy2025infogent`
- **Section role:** web information aggregation / multi-source extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a modular Navigator–Extractor–Aggregator framework for open-ended web information aggregation across multiple sources under direct API-driven and interactive visual access settings.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a modular Navigator–Extractor–Aggregator framework for open-ended web information aggregation across multiple sources under direct API-driven and interactive visual access settings.

- **Key finding:**  
  Infogent beats a SOTA multi-agent search framework by 7% on FRAMES under Direct API-Driven Access and improves over an information-seeking web agent by 4.3% on AssistantBench under Interactive Visual Access.

- **Limitation connected to thesis:**  
  It focuses on aggregation and final answer quality rather than schema-bound row-level extraction, provenance, or complete dataset extraction.

- **Connects to:**  
  S5.3 planning/backtracking, S5.7 deep research, S6 aggregation, S7/S8 verification and source coverage.

- **Use in thesis:**  
  Use as the S6 P1 paper connecting structured web extraction to broader web information aggregation and multi-source synthesis.

---

## Detailed notes

- Separates web information aggregation from linear task-completion web navigation.
- Uses three components: Navigator, Extractor, and Aggregator.
- Adds an enhanced action set so the Navigator can backtrack and transfer control when aggregation is needed.
- Uses feedback-driven navigation: Aggregator feedback guides what the Navigator should explore next.
- Supports Direct API-driven Access using search APIs and text extraction.
- Supports Interactive Visual Access using screenshots and browser interaction when paywalls, logins, or visually dependent interactions appear.
- Evaluates on AssistantBench, FRAMES, and FanOutQA.
- Relevant to thesis because many extraction tasks require multi-source evidence, not one page.

---

## Figures / tables to remember

- Figure 1 shows the two access settings and the Navigator–Extractor–Aggregator feedback loop.
- Main results compare Infogent against multi-agent search and information-seeking web-agent baselines.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
web information aggregation / multi-source extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It focuses on aggregation and final answer quality rather than schema-bound row-level extraction, provenance, or complete dataset extraction.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

Infogent contributes to S6 by addressing web information aggregation / multi-source extraction. Introduces a modular Navigator–Extractor–Aggregator framework for open-ended web information aggregation across multiple sources under direct API-driven and interactive visual access settings. The main result is that Infogent beats a SOTA multi-agent search framework by 7% on FRAMES under Direct API-Driven Access and improves over an information-seeking web agent by 4.3% on AssistantBench under Interactive Visual Access. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, It focuses on aggregation and final answer quality rather than schema-bound row-level extraction, provenance, or complete dataset extraction. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

Infogent shows that **Introduces a modular Navigator–Extractor–Aggregator framework for open-ended web information aggregation across multiple sources under direct API-driven and interactive visual access settings**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@inproceedings{reddy2025infogent,
  title     = {Infogent: An Agent-Based Framework for Web Information Aggregation},
  author    = {Revanth Gangi Reddy, Sagnik Mukherjee, Jeonghwan Kim, Zhenhailong Wang, Dilek Hakkani-Tür, Heng Ji},
  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
  year      = {2025},
  doi       = {10.18653/v1/2025.findings-naacl.318},
  eprint        = {2410.19054},
  archivePrefix = {arXiv},
  url       = {https://aclanthology.org/2025.findings-naacl.318/}
}
```

---

## Source links

- https://aclanthology.org/2025.findings-naacl.318/
- https://arxiv.org/abs/2410.19054


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\03 - 2025-03 - ReaderLM-v2- Small Language Model for HTML to Markdown and JSON.md

# ReaderLM-v2: Small Language Model for HTML to Markdown and JSON

## Metadata

- **Short name:** ReaderLM-v2
- **Authors:** Feng Wang, Zesheng Shi, Bo Wang, Nan Wang, Han Xiao
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **DOI:** 10.48550/arXiv.2503.01151
- **arXiv ID:** arXiv:2503.01151
- **Venue/status source:** arXiv + Jina AI project/blog
- **S6 cluster:** HTML-to-Markdown and schema-guided JSON extraction
- **Priority:** P1
- **BibTeX key:** `wang2025readerlmv2`
- **Section role:** content cleaning / HTML-to-JSON extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a compact 1.5B model for converting messy long-context HTML into clean Markdown or JSON using a three-stage DRAFT–REFINE–CRITIQUE data synthesis pipeline and multi-stage training.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a compact 1.5B model for converting messy long-context HTML into clean Markdown or JSON using a three-stage DRAFT–REFINE–CRITIQUE data synthesis pipeline and multi-stage training.

- **Key finding:**  
  ReaderLM-v2 outperforms GPT-4o and larger models by 15–20% on curated HTML extraction benchmarks, especially for documents above 100K tokens, while remaining computationally efficient.

- **Limitation connected to thesis:**  
  Strong for HTML cleaning and conversion, but not a full autonomous web agent: it does not navigate, interact with filters/pagination, or verify extracted values across live websites.

- **Connects to:**  
  S5.2 webpage representation, S6 content extraction infrastructure, IndexLM, ScrapeGraphAI-100k, RAG context preparation.

- **Use in thesis:**  
  Use as the S6 P1 infrastructure paper for turning noisy HTML into LLM-ready Markdown/JSON.

---

## Detailed notes

- Targets HTML main content conversion, instruction-guided Markdown extraction, and schema-guided JSON extraction.
- Processes long documents up to 512K tokens.
- Uses DRAFT–REFINE–CRITIQUE synthetic data generation.
- Training includes continuous pretraining, supervised fine-tuning, direct preference optimization, and self-play iterative tuning.
- Shows very strong HTML-to-Markdown performance compared with GPT-4o, Gemini, and Qwen baselines.
- JSON extraction is evaluated with tree-based precision/recall/F1 and pass-rate metrics.
- Best positioned as a content-preparation model for web agents and RAG systems.
- Useful for S6 because extraction agents often need cleaned Markdown/JSON before reasoning.

---

## Figures / tables to remember

- Figure 1 shows the DRAFT–REFINE–CRITIQUE synthetic data and training pipeline.
- Tables 1–2 report Markdown and JSON extraction results.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
content cleaning / HTML-to-JSON extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Strong for HTML cleaning and conversion, but not a full autonomous web agent: it does not navigate, interact with filters/pagination, or verify extracted values across live websites.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

ReaderLM-v2 contributes to S6 by addressing content cleaning / HTML-to-JSON extraction. Introduces a compact 1.5B model for converting messy long-context HTML into clean Markdown or JSON using a three-stage DRAFT–REFINE–CRITIQUE data synthesis pipeline and multi-stage training. The main result is that ReaderLM-v2 outperforms GPT-4o and larger models by 15–20% on curated HTML extraction benchmarks, especially for documents above 100K tokens, while remaining computationally efficient. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Strong for HTML cleaning and conversion, but not a full autonomous web agent: it does not navigate, interact with filters/pagination, or verify extracted values across live websites. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

ReaderLM-v2 shows that **Introduces a compact 1.5B model for converting messy long-context HTML into clean Markdown or JSON using a three-stage DRAFT–REFINE–CRITIQUE data synthesis pipeline and multi-stage training**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{wang2025readerlmv2,
  title         = {ReaderLM-v2: Small Language Model for HTML to Markdown and JSON},
  author        = {Feng Wang, Zesheng Shi, Bo Wang, Nan Wang, Han Xiao},
  journal       = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year          = {2025},
  doi           = {10.48550/arXiv.2503.01151},
  eprint        = {2503.01151},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2503.01151}
}
```

---

## Source links

- https://arxiv.org/abs/2503.01151
- https://arxiv.org/abs/2503.01151


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\04 - 2025-05 - NEXT-EVAL- Next Evaluation of Traditional and LLM Web Data Record Extraction.md

# NEXT-EVAL: Next Evaluation of Traditional and LLM Web Data Record Extraction

## Metadata

- **Short name:** NEXT-EVAL
- **Authors:** Soyeon Kim, Namhee Kim, Yeonwoo Jeong
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint. Project pages mention NeurIPS 2025 / in review, but no final accepted peer-reviewed proceedings status was confirmed in this check.
- **DOI:** 10.48550/arXiv.2505.17125
- **arXiv ID:** arXiv:2505.17125
- **S6 cluster:** evaluation benchmark for traditional and LLM-based web data record extraction
- **Priority:** P1
- **BibTeX key:** `kim2025nexteval`
- **Section role:** extraction evaluation / record extraction benchmark

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
NEXT-EVAL builds a concrete evaluation framework for web data record extraction,
allowing traditional heuristic extraction methods and LLM-based extraction methods
to be compared fairly on the same DOM-grounded task.
```

The paper focuses on **web data record extraction**, meaning extraction of repeated structured records from webpages, such as:

```text
product listings
company directories
contact tables
record lists
structured web tables
```

Its main contribution is not a new extraction agent, but a **benchmarking and evaluation framework**.

---

## Four-note template

- **Core idea:**  
  NEXT-EVAL creates a reproducible benchmark framework for evaluating traditional and LLM-based web data record extraction using MHTML snapshots, XPath-based labels, DOM-preserving preprocessing, and structure-aware metrics.

- **Key finding:**  
  Flat JSON input gives LLMs the best extraction performance among the tested input formats, reaching an F1 score of **0.9567** with minimal hallucination compared with Slimmed HTML and Hierarchical JSON.

- **Limitation connected to thesis:**  
  NEXT-EVAL improves evaluation rigor for web data record extraction, but it does not solve interactive navigation, schema-bound multi-page extraction, source provenance, live-web robustness, or verification of extracted values beyond DOM-position matching.

- **Connects to:**  
  WebLists/BardeenAgent, AutoScraper, SCRIBES, ReaderLM-v2, IndexLM, ScrapeGraphAI-100k, S5.1 evaluation, S5.5 reliability, S6 extraction evaluation, S8 deployment evaluation.

- **Use in thesis:**  
  Use as the S6 P1 evaluation paper for record extraction, especially when discussing why extraction systems need structure-aware metrics and DOM-grounded labels rather than only text-level exact matching.

---

## Why this paper is important for S6

S6 focuses on:

```text
LLM-based web information extraction and aggregation
```

NEXT-EVAL is important because extraction papers need reliable evaluation. Without a clear evaluation protocol, it is difficult to compare:

```text
traditional algorithms
DOM/tree-based extraction
heuristic record detection
LLM zero-shot extraction
LLM extraction using transformed HTML/JSON inputs
```

The paper argues that existing evaluation is limited by:

```text
static benchmarks
domain-specific datasets
opaque scoring practices
difficulty comparing traditional and LLM methods
lack of consistent DOM-grounded supervision
```

NEXT-EVAL addresses this by creating an evaluation framework from arbitrary MHTML snapshots and using XPath-based supervision labels.

---

## Main contribution

## 1. Reproducible evaluation dataset generation

NEXT-EVAL systematically generates evaluation datasets from:

```text
arbitrary MHTML snapshots
```

This matters because MHTML snapshots preserve webpage content in a reproducible form. For extraction evaluation, this avoids one of the major problems of live-web benchmarks:

```text
the page changes between runs
```

For the thesis, this supports the S8 idea that reproducibility is a major challenge in web-agent evaluation.

---

## 2. XPath-based supervision labels

The framework annotates extraction targets using:

```text
XPath-based labels
```

This is important because web data record extraction is not only about matching output text. The system should extract the correct **DOM-positioned record**, not hallucinate a plausible text answer.

XPath labels allow evaluation to measure whether the system selected the correct structural locations in the page.

This is directly relevant to your thesis because generalized extraction agents must preserve:

```text
where the value came from
which page element supports it
which record/list/table it belongs to
```

---

## 3. Structure-aware metrics

NEXT-EVAL uses structure-aware metrics for consistent scoring.

The paper’s key evaluation concern is hallucination:

```text
text hallucination
positional hallucination
```

The framework is designed to prevent text hallucination and focus evaluation on whether the model extracts the correct DOM positions.

This is important because LLMs can generate correct-looking records that are not actually grounded in the page.

For S6, this supports the claim:

```text
extraction evaluation must be source-grounded,
not only text-output based.
```

---

## 4. DOM-preserving preprocessing formats

NEXT-EVAL compares different input formats for LLM-based extraction:

```text
Slimmed HTML
Hierarchical JSON
Flat JSON
```

### Slimmed HTML

This format reduces the raw HTML size while trying to preserve important DOM semantics.

### Hierarchical JSON

This preserves nested DOM structure in a JSON representation.

### Flat JSON

This flattens the DOM into key-value pairs, typically where the key is an XPath-like location and the value is the text content.

The important result is:

```text
Flat JSON gives the best extraction accuracy.
```

The reported headline result is:

```text
Flat JSON F1 = 0.9567
```

This suggests that LLMs benefit when webpage structure is converted into an explicit, compact, position-aware representation.

---

## 5. Synthetic dataset creation

NEXT-EVAL also creates a public synthetic dataset by:

```text
transforming DOM structures
modifying content
```

This is useful because extraction evaluation needs controlled diversity.

Synthetic transformation can test whether methods are robust to:

```text
layout variations
DOM changes
content changes
record order changes
structural perturbations
```

For your thesis, this supports the idea that extraction benchmarks should include controlled transformations, not only static pages.

---

## 6. Benchmarking traditional and LLM methods

NEXT-EVAL benchmarks:

```text
deterministic heuristic algorithms
off-the-shelf LLMs
```

across different DOM-preserving input formats.

This is valuable because your thesis covers both:

```text
classical web extraction / scraping
and
LLM-based agentic extraction
```

NEXT-EVAL gives a way to compare these paradigms under one evaluation framework.

---

## Figures / tables to remember

The paper is especially useful for these visual ideas:

```text
1. Evaluation pipeline:
   MHTML snapshot → preprocessing → XPath labels → extraction → structure-aware scoring

2. Input-format comparison:
   Slimmed HTML vs Hierarchical JSON vs Flat JSON

3. Extraction-performance comparison:
   traditional heuristics vs off-the-shelf LLMs

4. Hallucination-aware evaluation:
   preventing text hallucination and measuring DOM-position correctness
```

The most important result to remember is:

```text
Flat JSON input achieves F1 = 0.9567
```

---

## Thesis relevance

NEXT-EVAL supports the S6 claim that **web extraction evaluation must be different from ordinary QA evaluation**.

A web data extraction system should be judged by:

```text
record-level correctness
field-level correctness
DOM/source grounding
structure preservation
hallucination control
layout robustness
schema/record consistency
```

For your thesis, NEXT-EVAL is useful because it gives evaluation language for:

```text
source-grounded extraction
DOM-positioned evidence
structure-aware metrics
record extraction fairness
traditional-vs-LLM comparison
```

It is especially relevant to your core thesis problem:

```text
generalized web automation and data extraction
```

because generalized extraction cannot rely only on final text answers. It needs to know whether the extracted data is actually supported by the webpage structure.

---

## Limitation as thesis gap

NEXT-EVAL is strong for evaluation, but it is not a full solution.

It does not fully solve:

```text
interactive navigation before extraction
pagination and multi-page extraction
filter interaction
login/authentication flows
visual-DOM mismatch
source provenance across multiple pages
schema-bound extraction with complex nested outputs
semantic correctness of extracted values
live-web drift
human-in-the-loop validation
deployment cost and safety
```

For the thesis, the limitation is:

```text
NEXT-EVAL improves extraction evaluation, but generalized web extraction agents still need
an end-to-end architecture that combines navigation, interaction, extraction, provenance,
verification, and robust deployment.
```

---

## Connection to S6 P0 WebLists

WebLists evaluates interactive schema-bound extraction from live websites.

NEXT-EVAL complements WebLists by focusing on:

```text
record extraction evaluation
DOM/XPath-grounded labels
input-format comparison
hallucination-aware scoring
traditional-vs-LLM benchmarking
```

So the relationship is:

```text
WebLists = task/benchmark for interactive structured extraction
NEXT-EVAL = evaluation framework for DOM-grounded record extraction
```

Use both together in S6.

---

## Connection to other S6 P1 papers

| Paper | Connection |
|---|---|
| AutoScraper | Both evaluate scraper/extractor generation; NEXT-EVAL adds structure-aware evaluation |
| SCRIBES | Both care about reusable extraction over structurally similar webpages |
| ReaderLM-v2 | NEXT-EVAL tests how input representation affects extraction quality |
| IndexLM | Both preserve structure and avoid naive text-only extraction |
| ScrapeGraphAI-100k | Both are useful for schema/record extraction evaluation, but ScrapeGraphAI-100k is dataset/training-focused |
| STRUCTSENSE | Both support evaluation/validation; STRUCTSENSE adds HITL and ontology alignment |
| Beyond BeautifulSoup | NEXT-EVAL is evaluation-focused; Beyond BeautifulSoup is practical usability/security-focused |

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.1** | Evaluation design, benchmark realism, scoring reliability |
| **S5.2** | HTML/DOM representation and Flat JSON as structure-preserving input |
| **S5.5** | Hallucination, extraction failure, evaluation failure |
| **S6** | Main role: record extraction evaluation |
| **S7** | Verification, provenance, hallucination prevention |
| **S8** | Reproducibility, live-web drift, deployment evaluation |

---

## Thesis-ready paragraph

Kim et al. introduce **NEXT-EVAL**, a benchmark and evaluation framework for comparing traditional and LLM-based web data record extraction methods. The framework addresses a key weakness of existing extraction evaluation: static, domain-specific benchmarks and opaque scoring make it difficult to compare heuristic DOM-based methods with LLM-based zero-shot extraction. NEXT-EVAL generates evaluation datasets from arbitrary MHTML snapshots, annotates XPath-based supervision labels, and uses structure-aware metrics to evaluate whether extracted records correspond to the correct webpage positions. It also compares multiple DOM-preserving preprocessing strategies, including Slimmed HTML, Hierarchical JSON, and Flat JSON. The main result is that Flat JSON provides the strongest representation for LLM-based extraction, achieving an F1 score of 0.9567 with minimal hallucination. For this thesis, NEXT-EVAL is important because it shows that web extraction evaluation must be source-grounded and structure-aware, not only text-output based. However, the framework does not solve interactive navigation, multi-page extraction, provenance tracking, schema-level semantic verification, or live-web robustness. It therefore complements WebLists by strengthening the evaluation side of agentic web data extraction.

---

## One-sentence summary

NEXT-EVAL shows that fair evaluation of web data record extraction requires DOM-grounded, structure-aware metrics, and that Flat JSON is a strong input representation for LLM-based record extraction.

---

## BibTeX

```bibtex
@article{kim2025nexteval,
  title         = {NEXT-EVAL: Next Evaluation of Traditional and LLM Web Data Record Extraction},
  author        = {Kim, Soyeon and Kim, Namhee and Jeong, Yeonwoo},
  journal       = {arXiv preprint arXiv:2505.17125},
  year          = {2025},
  doi           = {10.48550/arXiv.2505.17125},
  url           = {https://arxiv.org/abs/2505.17125},
  eprint        = {2505.17125},
  archivePrefix = {arXiv}
}
```

---

## Source links

- https://arxiv.org/abs/2505.17125
- https://github.com/wordbricks/next-eval


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\04 - 2025-07 - STRUCTSENSE- A Task-Agnostic Agentic Framework for Structured Information Extraction.md

# STRUCTSENSE: A Task-Agnostic Agentic Framework for Structured Information Extraction with Human-In-The-Loop Evaluation and Benchmarking

## Metadata

- **Short name:** STRUCTSENSE
- **Authors:** Tek Raj Chhetri, Yibei Chen, Puja Trivedi, Dorota Jarecka, Saif Haobsh, Patrick Ray, Lydia Ng, Satrajit S. Ghosh
- **Year used for thesis:** 2025
- **Venue/status:** arXiv preprint / OpenReview entry; no final peer-reviewed venue confirmed in this check
- **DOI:** 10.48550/arXiv.2507.03674
- **arXiv ID:** arXiv:2507.03674
- **Venue/status source:** arXiv + OpenReview + GitHub
- **S6 cluster:** agentic structured information extraction with ontology and HITL
- **Priority:** P1
- **BibTeX key:** `chhetri2025structsense`
- **Section role:** HITL and ontology-grounded structured extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a modular multi-agent framework for task-agnostic structured information extraction using an Extractor Agent, Alignment Agent, Judge Agent, and Feedback Agent with ontology grounding and human-in-the-loop validation.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a modular multi-agent framework for task-agnostic structured information extraction using an Extractor Agent, Alignment Agent, Judge Agent, and Feedback Agent with ontology grounding and human-in-the-loop validation.

- **Key finding:**  
  Demonstrates that ontology-guided agentic extraction can support diverse neuroscience IE tasks, including NER, survey-to-schema conversion, and literature-review resource/metadata extraction.

- **Limitation connected to thesis:**  
  Focused on scientific documents and neuroscience rather than live web scraping; evaluation is domain-specific and not centered on interactive website extraction.

- **Connects to:**  
  S6 schema-grounded extraction, S7 verification/HITL, S8 FAIR data and auditability.

- **Use in thesis:**  
  Use as the S6 paper for ontology grounding, judge agents, and human-in-the-loop validation in structured extraction.

---

## Detailed notes

- Targets structured information extraction from unstructured scientific sources.
- Uses four specialized agents: extractor, alignment, judge, and feedback.
- The Alignment Agent maps extracted terms to ontologies or knowledge graphs.
- The Judge Agent evaluates extraction and alignment outputs.
- The Feedback Agent incorporates human correction and updates memory.
- Designed to be task-agnostic through task and agent configurations.
- Emphasizes FAIR-aligned outputs, semantic interoperability, and auditability.
- Useful for thesis because it addresses schema/ontology grounding and human validation, two gaps in web extraction agents.

---

## Figures / tables to remember

- Figure 1 shows the STRUCTSENSE architecture: Extractor Agent, Alignment Agent, Judge Agent, Feedback Agent, ontology database, memory, and human feedback.
- Table 1 illustrates ontology disambiguation for the term cortex across neuroscience and plant biology.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
HITL and ontology-grounded structured extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Focused on scientific documents and neuroscience rather than live web scraping; evaluation is domain-specific and not centered on interactive website extraction.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

STRUCTSENSE contributes to S6 by addressing HITL and ontology-grounded structured extraction. Introduces a modular multi-agent framework for task-agnostic structured information extraction using an Extractor Agent, Alignment Agent, Judge Agent, and Feedback Agent with ontology grounding and human-in-the-loop validation. The main result is that Demonstrates that ontology-guided agentic extraction can support diverse neuroscience IE tasks, including NER, survey-to-schema conversion, and literature-review resource/metadata extraction. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Focused on scientific documents and neuroscience rather than live web scraping; evaluation is domain-specific and not centered on interactive website extraction. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

STRUCTSENSE shows that **Introduces a modular multi-agent framework for task-agnostic structured information extraction using an Extractor Agent, Alignment Agent, Judge Agent, and Feedback Agent with ontology grounding and human-in-the-loop validation**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{chhetri2025structsense,
  title         = {STRUCTSENSE: A Task-Agnostic Agentic Framework for Structured Information Extraction with Human-In-The-Loop Evaluation and Benchmarking},
  author        = {Tek Raj Chhetri, Yibei Chen, Puja Trivedi, Dorota Jarecka, Saif Haobsh, Patrick Ray, Lydia Ng, Satrajit S. Ghosh},
  journal       = {arXiv preprint / OpenReview entry; no final peer-reviewed venue confirmed in this check},
  year          = {2025},
  doi           = {10.48550/arXiv.2507.03674},
  eprint        = {2507.03674},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2507.03674}
}
```

---

## Source links

- https://arxiv.org/abs/2507.03674
- https://arxiv.org/abs/2507.03674


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\05 - 2025-09 - A Systematic Review of Web Scraping- Techniques LLM-Enhanced Approaches Performance Metrics and Legal-Ethical Issues.md

# A Systematic Review of Web Scraping: Techniques, LLM-Enhanced Approaches, Performance Metrics, and Legal-Ethical Issues

## Metadata

- **Short name:** Systematic Review of Web Scraping
- **Authors:** Navroz Kaur Kahlon, Williamjeet Singh
- **Year used for thesis:** 2026
- **Venue/status:** Data & Knowledge Engineering, Volume 164, July 2026, Article 102598; earlier SSRN preprint posted September 2025
- **DOI:** 10.1016/j.datak.2026.102598
- **arXiv ID:** Not applicable
- **Venue/status source:** ScienceDirect search result + SSRN preprint page
- **S6 cluster:** survey/background: scraping techniques, metrics, legal and ethical issues
- **Priority:** P1
- **BibTeX key:** `kahlon2026systematicwebscraping`
- **Section role:** background survey / metrics / legal-ethical grounding

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Systematically reviews web scraping techniques, applications, LLM-enhanced scraping, performance metrics, and legal/ethical issues across 260 studies.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Systematically reviews web scraping techniques, applications, LLM-enhanced scraping, performance metrics, and legal/ethical issues across 260 studies.

- **Key finding:**  
  Provides a broad taxonomy of classical and LLM-enhanced scraping, identifies performance metrics, application areas, tools, and legal/ethical constraints.

- **Limitation connected to thesis:**  
  It is a broad survey rather than a method paper; it does not provide a new extraction agent, benchmark, or empirical system for LLM-based web extraction.

- **Connects to:**  
  S6.1 foundations, S8 legal/ethical deployment, S5.5 reliability, S7 verification and responsible extraction.

- **Use in thesis:**  
  Use as background support for classical scraping foundations, metrics, applications, and legal/ethical constraints.

---

## Detailed notes

- Reviews 260 studies from journals, conferences, and workshops.
- Compares itself to previous surveys and claims broader coverage of LLM-based scraping, legal/ethical issues, metrics, and applications.
- Defines web scraping as automated extraction and transformation of web data into structured formats such as CSV, JSON, and Excel.
- Surveys traditional techniques, tools/software, LLM-based systems, RAG-style approaches, and LLMOps integrations.
- Includes performance metrics such as accuracy, precision, recall, F1, execution time, completeness, robustness, and scalability.
- Discusses application areas such as e-commerce, academics, health, tourism, and corpus construction.
- Highlights privacy, terms of service, institutional oversight, data validity, and legal ambiguity.
- Important for thesis background but not the S6 core anchor.

---

## Figures / tables to remember

- Table 1 compares this review against previous web scraping surveys.
- Figure 4 gives the research-question hierarchy.
- Section 3.3 summarizes performance metrics used in web scraping studies.
- Sections 6–8 discuss implications, limitations, and legal/ethical issues.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
background survey / metrics / legal-ethical grounding
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It is a broad survey rather than a method paper; it does not provide a new extraction agent, benchmark, or empirical system for LLM-based web extraction.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

Systematic Review of Web Scraping contributes to S6 by addressing background survey / metrics / legal-ethical grounding. Systematically reviews web scraping techniques, applications, LLM-enhanced scraping, performance metrics, and legal/ethical issues across 260 studies. The main result is that Provides a broad taxonomy of classical and LLM-enhanced scraping, identifies performance metrics, application areas, tools, and legal/ethical constraints. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, It is a broad survey rather than a method paper; it does not provide a new extraction agent, benchmark, or empirical system for LLM-based web extraction. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

Systematic Review of Web Scraping shows that **Systematically reviews web scraping techniques, applications, LLM-enhanced scraping, performance metrics, and legal/ethical issues across 260 studies**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{kahlon2026systematicwebscraping,
  title   = {A Systematic Review of Web Scraping: Techniques, LLM-Enhanced Approaches, Performance Metrics, and Legal-Ethical Issues},
  author  = {Navroz Kaur Kahlon, Williamjeet Singh},
  journal = {Data & Knowledge Engineering},
  volume  = {164},
  pages   = {102598},
  year    = {2026},
  doi     = {10.1016/j.datak.2026.102598},
  url     = {https://www.sciencedirect.com/science/article/abs/pii/S0169023X26000455}
}
```

---

## Source links

- https://www.sciencedirect.com/science/article/abs/pii/S0169023X26000455
- SSRN preprint: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5429131


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\06 - 2025-10 - SCRIBES- Web-Scale Script-Based Semi-Structured Data Extraction with Reinforcement Learning.md

# SCRIBES: Web-Scale Script-Based Semi-Structured Data Extraction with Reinforcement Learning

## Metadata

- **Short name:** SCRIBES
- **Authors:** Shicheng Liu, Kai Sun, Lisheng Fu, Xilun Chen, Xinyuan Zhang, Zhaojiang Lin, Rulin Shao, Yue Liu, Anuj Kumar, Wen-tau Yih, Xin Luna Dong
- **Year used for thesis:** 2026
- **Venue/status:** ICLR 2026 Poster
- **DOI:** 10.48550/arXiv.2510.01832
- **arXiv ID:** arXiv:2510.01832
- **Venue/status source:** OpenReview ICLR 2026 + arXiv
- **S6 cluster:** RL-trained reusable extraction scripts for semi-structured web data
- **Priority:** P1
- **BibTeX key:** `liu2026scribes`
- **Section role:** RL-based web-scale script extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Trains models to generate reusable extraction scripts for groups of structurally similar webpages, using cross-page layout generalization as a reinforcement learning reward.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Trains models to generate reusable extraction scripts for groups of structurally similar webpages, using cross-page layout generalization as a reinforcement learning reward.

- **Key finding:**  
  Outperforms strong agentic baselines by more than 13% in script quality and boosts downstream QA accuracy by more than 4% for GPT-4o with extracted triples.

- **Limitation connected to thesis:**  
  Targets semi-structured HTML tables/lists/infoboxes and depends on group-level structural similarity; complex/free-form pages and noisy synthetic annotations remain challenging.

- **Connects to:**  
  AutoScraper, WebLists/BardeenAgent, ReaderLM-v2, IndexLM, S5.4 RL, S6 web-scale extraction.

- **Use in thesis:**  
  Use as the strongest S6 P1 method after WebLists for scalable script-based semi-structured data extraction.

---

## Detailed notes

- Extracts triples from semi-structured HTML such as tables, lists, and infoboxes.
- Uses one representative webpage to generate a script that should apply to other pages in the same structural group.
- Reward combines self-score and cross-score across webpages in a group, encouraging generalizable scripts.
- Uses GRPO/RLVR style training with fuzzy triple-level F1 as the training reward.
- Adds CommonCrawl failure-case training with synthetic LLM annotations after initial training on gold annotated data.
- HTML deduplication collapses repeated HTML blocks while preserving structure, reducing token usage from over 114k to under 17k on average in the profiled set.
- Best Q-32B + CC model reaches 33.2 F1_LM overall and 32.4 holdout F1_LM in the reported setting.
- Downstream QA improves when SCRIBES triples are appended to flattened HTML; GPT-4o improves from 82.5 to 86.6.

---

## Figures / tables to remember

- Figure 1 shows training-time script generation, reward calculation across in-group pages, and inference-time generalization to unseen groups.
- Figure 2 shows structurally similar SEC pages under the same website.
- Figure 3 shows the CommonCrawl data pipeline.
- Table 1 reports script generation results; Table 4 shows QA gains from SCRIBES triples.
- Figure 5 and Table 5 show the HTML deduplication mechanism and token reduction.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
RL-based web-scale script extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Targets semi-structured HTML tables/lists/infoboxes and depends on group-level structural similarity; complex/free-form pages and noisy synthetic annotations remain challenging.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

SCRIBES contributes to S6 by addressing RL-based web-scale script extraction. Trains models to generate reusable extraction scripts for groups of structurally similar webpages, using cross-page layout generalization as a reinforcement learning reward. The main result is that Outperforms strong agentic baselines by more than 13% in script quality and boosts downstream QA accuracy by more than 4% for GPT-4o with extracted triples. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Targets semi-structured HTML tables/lists/infoboxes and depends on group-level structural similarity; complex/free-form pages and noisy synthetic annotations remain challenging. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

SCRIBES shows that **Trains models to generate reusable extraction scripts for groups of structurally similar webpages, using cross-page layout generalization as a reinforcement learning reward**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@inproceedings{liu2026scribes,
  title     = {SCRIBES: Web-Scale Script-Based Semi-Structured Data Extraction with Reinforcement Learning},
  author    = {Shicheng Liu, Kai Sun, Lisheng Fu, Xilun Chen, Xinyuan Zhang, Zhaojiang Lin, Rulin Shao, Yue Liu, Anuj Kumar, Wen-tau Yih, Xin Luna Dong},
  booktitle = {International Conference on Learning Representations},
  year      = {2026},
  eprint        = {2510.01832},
  archivePrefix = {arXiv},
  url       = {https://openreview.net/forum?id=gQSnEIA3Z3}
}
```

---

## Source links

- https://openreview.net/forum?id=gQSnEIA3Z3
- https://arxiv.org/abs/2510.01832


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\07 - 2025-12 - An Index-based Approach for Efficient and Effective Web Content Extraction.md

# An Index-based Approach for Efficient and Effective Web Content Extraction

## Metadata

- **Short name:** IndexLM / Index-based Web Content Extraction
- **Authors:** Yihan Chen, Benfeng Xu, Xiaorui Wang, Zhendong Mao
- **Year used for thesis:** 2025
- **Venue/status:** CoRR/arXiv preprint; no final peer-reviewed venue confirmed in this check
- **DOI:** 10.48550/arXiv.2512.06641
- **arXiv ID:** arXiv:2512.06641
- **Venue/status source:** arXiv + DBLP/CoRR result
- **S6 cluster:** index-based query-relevant content extraction for RAG/web agents
- **Priority:** P1
- **BibTeX key:** `chen2025indexwebextraction`
- **Section role:** efficient content extraction / context compression

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Reframes web content extraction from token-by-token generation into discriminative index prediction over structure-aware HTML blocks.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Reframes web content extraction from token-by-token generation into discriminative index prediction over structure-aware HTML blocks.

- **Key finding:**  
  IndexLM improves RAG QA accuracy and is much faster than generative extraction methods; IndexLM-4B reaches 87.40 F1 on main-content extraction and 31.69 F1 on query-relevant extraction in direct evaluation.

- **Limitation connected to thesis:**  
  It extracts relevant content spans rather than schema-bound structured records; it supports context reduction but not full extraction workflows with forms, pagination, provenance, or schema validation.

- **Connects to:**  
  ReaderLM-v2, HtmlRAG, S5.2 context compression, S6 extraction infrastructure, S8 cost/latency.

- **Use in thesis:**  
  Use as the S6 P1 paper for efficient content selection and context compression before extraction or web-agent reasoning.

---

## Detailed notes

- Partitions cleaned HTML into addressable structure-aware blocks with numeric indices.
- IndexLM outputs closed index intervals such as [[1,2],[3,5]] rather than generating extracted content.
- Supports both main content extraction and query-relevant extraction.
- Decouples extraction latency from output content length because the model emits short index intervals.
- Uses Qwen3-based models at 0.6B, 1.7B, and 4B scales.
- Evaluated as a post-retrieval processing module in RAG QA on HotpotQA, NQ, TriviaQA, Musique, and MultiHopRAG.
- IndexLM improves average QA F1 over chunk-rerank, HtmlRAG, ReaderLM-v2, Firecrawl Extract, and prompt-based extraction baselines in the reported settings.
- Useful for agents that must read many long webpages under limited context budgets.

---

## Figures / tables to remember

- Figure 1 plots effectiveness versus latency and shows IndexLM models in the more efficient/effective region.
- Figure 2 compares index-based extraction with heuristic rules, chunk-rerank, and generative extraction.
- Figure 3 shows the full pipeline: index construction, index extraction, post-processing.
- Figure 4 gives a simplified indexed block example.
- Tables 2–3 report RAG QA and direct extraction results.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
efficient content extraction / context compression
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
It extracts relevant content spans rather than schema-bound structured records; it supports context reduction but not full extraction workflows with forms, pagination, provenance, or schema validation.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

IndexLM / Index-based Web Content Extraction contributes to S6 by addressing efficient content extraction / context compression. Reframes web content extraction from token-by-token generation into discriminative index prediction over structure-aware HTML blocks. The main result is that IndexLM improves RAG QA accuracy and is much faster than generative extraction methods; IndexLM-4B reaches 87.40 F1 on main-content extraction and 31.69 F1 on query-relevant extraction in direct evaluation. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, It extracts relevant content spans rather than schema-bound structured records; it supports context reduction but not full extraction workflows with forms, pagination, provenance, or schema validation. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

IndexLM / Index-based Web Content Extraction shows that **Reframes web content extraction from token-by-token generation into discriminative index prediction over structure-aware HTML blocks**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{chen2025indexwebextraction,
  title         = {An Index-based Approach for Efficient and Effective Web Content Extraction},
  author        = {Yihan Chen, Benfeng Xu, Xiaorui Wang, Zhendong Mao},
  journal       = {CoRR/arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year          = {2025},
  doi           = {10.48550/arXiv.2512.06641},
  eprint        = {2512.06641},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2512.06641}
}
```

---

## Source links

- https://arxiv.org/abs/2512.06641
- https://arxiv.org/abs/2512.06641


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\08 - 2026-01 - Beyond BeautifulSoup- Benchmarking LLM-Powered Web Scraping for Everyday Users.md

# Beyond BeautifulSoup: Benchmarking LLM-Powered Web Scraping for Everyday Users

## Metadata

- **Short name:** Beyond BeautifulSoup
- **Authors:** Arth Bhardwaj, Nirav Diwan, Gang Wang
- **Year used for thesis:** 2026
- **Venue/status:** AICS Workshop at AAAI 2026 + arXiv preprint
- **DOI:** 10.48550/arXiv.2601.06301
- **arXiv ID:** arXiv:2601.06301
- **Venue/status source:** arXiv + Gang Wang publications page + AICS 2026 program
- **S6 cluster:** benchmarking LLM-powered scraping accessibility and security tiers
- **Priority:** P1
- **BibTeX key:** `bhardwaj2026beyondbeautifulsoup`
- **Section role:** benchmark / usability / scraping democratization

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Benchmarks what novice users can accomplish with off-the-shelf LLM-assisted scripting and end-to-end LLM agents across 35 websites and five security/complexity tiers.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Benchmarks what novice users can accomplish with off-the-shelf LLM-assisted scripting and end-to-end LLM agents across 35 websites and five security/complexity tiers.

- **Key finding:**  
  Traditional LLM-assisted scripting is fastest for static HTML, while end-to-end agents are more accessible and successful on complex, authenticated, protected, and CAPTCHA-like scenarios.

- **Limitation connected to thesis:**  
  Small benchmark, limited tools, limited hardware/session conditions, and a focus on accessibility rather than extraction correctness, schema adherence, or large-scale scraping reliability.

- **Connects to:**  
  AutoScraper, WebLists, S5.5 reliability, S8 safety/legal/anti-bot implications.

- **Use in thesis:**  
  Use as a S6/S8 bridge paper: it shows how LLM agents change practical scraping capability and risk for everyday users.

---

## Detailed notes

- Defines two workflows: LLM-assisted scripting and end-to-end LLM agents.
- LLM-assisted scripting uses LLM-generated BeautifulSoup/Scrapy scripts but leaves execution and debugging to the user.
- End-to-end agents use Claude and Simular.ai to navigate and extract through integrated tools.
- Benchmarks 35 websites across simple HTML, complex HTML, simple authentication, complex authentication, and CAPTCHA categories.
- Measures extraction success rate, execution time, and manual effort required.
- Traditional tools achieve high success and low latency for static sites.
- Agents are slower but handle authentication, dynamic UI, and protected workflows that basic BeautifulSoup/Scrapy workflows cannot reasonably support for novices.
- Frames LLM-powered scraping as both a benign capability amplifier and an abuse/defense concern.

---

## Figures / tables to remember

- Figure 1 shows the benchmark design for LLM-assisted scripting versus end-to-end LLM agents.
- Table 1 defines the five website difficulty tiers.
- Table 2 reports extraction success rate across categories.
- Table 3 reports manual effort required.
- Figure 2 reports execution time on a log scale.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
benchmark / usability / scraping democratization
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Small benchmark, limited tools, limited hardware/session conditions, and a focus on accessibility rather than extraction correctness, schema adherence, or large-scale scraping reliability.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

Beyond BeautifulSoup contributes to S6 by addressing benchmark / usability / scraping democratization. Benchmarks what novice users can accomplish with off-the-shelf LLM-assisted scripting and end-to-end LLM agents across 35 websites and five security/complexity tiers. The main result is that Traditional LLM-assisted scripting is fastest for static HTML, while end-to-end agents are more accessible and successful on complex, authenticated, protected, and CAPTCHA-like scenarios. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Small benchmark, limited tools, limited hardware/session conditions, and a focus on accessibility rather than extraction correctness, schema adherence, or large-scale scraping reliability. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

Beyond BeautifulSoup shows that **Benchmarks what novice users can accomplish with off-the-shelf LLM-assisted scripting and end-to-end LLM agents across 35 websites and five security/complexity tiers**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@inproceedings{bhardwaj2026beyondbeautifulsoup,
  title     = {Beyond BeautifulSoup: Benchmarking LLM-Powered Web Scraping for Everyday Users},
  author    = {Arth Bhardwaj, Nirav Diwan, Gang Wang},
  booktitle = {Artificial Intelligence for Cyber Security Workshop at AAAI 2026},
  year      = {2026},
  eprint        = {2601.06301},
  archivePrefix = {arXiv},
  url       = {https://arxiv.org/abs/2601.06301}
}
```

---

## Source links

- https://arxiv.org/abs/2601.06301
- https://arxiv.org/abs/2601.06301


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\09 - 2026-02 - ScrapeGraphAI-100k- A Large-Scale Dataset for LLM-Based Web Information Extraction.md

# ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction

## Metadata

- **Short name:** ScrapeGraphAI-100k
- **Authors:** William Brach, Francesco Zuppichini, Marco Vinciguerra, Lorenzo Padoan
- **Year used for thesis:** 2026
- **Venue/status:** arXiv preprint; no final peer-reviewed venue confirmed in this check
- **DOI:** 10.48550/arXiv.2602.15189
- **arXiv ID:** arXiv:2602.15189
- **Venue/status source:** arXiv + Hugging Face / project release
- **S6 cluster:** large-scale real-world LLM extraction dataset
- **Priority:** P1
- **BibTeX key:** `brach2026scrapegraphai100k`
- **Section role:** dataset / schema-constrained extraction

---

## Simple understanding

This paper belongs to **S6 — LLM-Based Web Information Extraction and Aggregation**.

The central idea is:

```text
Introduces a 93,695-example real-world dataset of LLM web extraction events derived from 9M opt-in ScrapeGraphAI telemetry events, including Markdown content, prompt, JSON schema, LLM response, and complexity/validation metadata.
```

For your thesis, this paper helps explain one part of the extraction stack: scraper generation, web information aggregation, HTML cleaning, schema-constrained extraction, executable scripts, efficient content selection, benchmarking, or dataset construction.

---

## Four-note template

- **Core idea:**  
  Introduces a 93,695-example real-world dataset of LLM web extraction events derived from 9M opt-in ScrapeGraphAI telemetry events, including Markdown content, prompt, JSON schema, LLM response, and complexity/validation metadata.

- **Key finding:**  
  Shows that schema complexity drives extraction failures and that fine-tuning a 1.7B model narrows the gap to 30B baselines on structural extraction metrics.

- **Limitation connected to thesis:**  
  Dataset reflects ScrapeGraphAI telemetry and is skewed toward GPT-4o-mini; it uses Markdown rather than raw HTML/DOM/visual inputs and schema validity does not guarantee semantic correctness.

- **Connects to:**  
  ReaderLM-v2, STRUCTSENSE, IndexLM, S5.4 fine-tuning, S6 schema-constrained extraction, S8 reproducibility.

- **Use in thesis:**  
  Use as the S6 P1 dataset paper for training, benchmarking, and failure analysis of schema-constrained LLM web extraction.

---

## Detailed notes

- Starts from about 9M opt-in production telemetry events collected during Q2–Q3 2025.
- After cleaning, deduplication, and balancing by schema, releases 93,695 examples.
- Each example contains source/content, natural-language prompt, JSON schema, LLM response, validation flag, model metadata, execution time, and schema complexity metrics.
- Retains invalid responses, enabling failure-mode analysis.
- Computes schema depth, key count, element count, cyclomatic complexity, and composite complexity score.
- Finds validation declines sharply at high schema complexity thresholds such as depth ≥ 7 and key count ≥ 200.
- Fine-tuned Qwen3-1.7B improves schema compliance and key F1, approaching 30B models on structural metrics.
- Highlights a structural-semantic gap: models can produce correct JSON skeletons while extracting imperfect values.

---

## Figures / tables to remember

- Figure 1 shows schema complexity distributions.
- Figure 2 shows validation rate declines as schema complexity increases.
- Tables 1–2 summarize dataset fields and descriptive statistics.
- Table 3 compares ScrapeGraphAI-100k with existing datasets.
- Table 4 reports fine-tuning results.
- Figures 5–6 in the appendix show metric correlations and language distribution.

---

## Thesis relevance

This paper supports the S6 argument that generalized web data extraction is not one operation. It requires several layers:

```text
content access
HTML/DOM cleaning
interactive navigation
schema binding
selector or script generation
evidence preservation
validation
cost control
legal/ethical awareness
```

The specific contribution of this paper is:

```text
dataset / schema-constrained extraction
```

---

## Limitation as thesis gap

The thesis-relevant limitation is:

```text
Dataset reflects ScrapeGraphAI telemetry and is skewed toward GPT-4o-mini; it uses Markdown rather than raw HTML/DOM/visual inputs and schema validity does not guarantee semantic correctness.
```

This should be used to keep the S6 argument focused on the remaining gap:

```text
web extraction agents need to be robust, schema-aware, source-verifiable,
cost-efficient, and safe under live-web conditions.
```

---

## Cross-links

| Later section | Connection |
|---|---|
| **S5.2** | webpage representation, HTML/DOM/Markdown/JSON conversion, grounding |
| **S5.3** | planning, backtracking, executable workflows, multi-page navigation |
| **S5.4** | training, RL, synthetic data, fine-tuning, datasets |
| **S5.5** | extraction failures, reliability, dynamic web conditions |
| **S7** | verification, provenance, hallucination control, human validation |
| **S8** | deployment, cost, safety, legal and ethical constraints |

---

## Thesis-ready paragraph

ScrapeGraphAI-100k contributes to S6 by addressing dataset / schema-constrained extraction. Introduces a 93,695-example real-world dataset of LLM web extraction events derived from 9M opt-in ScrapeGraphAI telemetry events, including Markdown content, prompt, JSON schema, LLM response, and complexity/validation metadata. The main result is that Shows that schema complexity drives extraction failures and that fine-tuning a 1.7B model narrows the gap to 30B baselines on structural extraction metrics. For the thesis, this paper is important because generalized web automation and data extraction require more than page navigation: the system must transform messy, dynamic, and heterogeneous web content into structured, verifiable, and reusable data. However, Dataset reflects ScrapeGraphAI telemetry and is skewed toward GPT-4o-mini; it uses Markdown rather than raw HTML/DOM/visual inputs and schema validity does not guarantee semantic correctness. Therefore, this paper should be cited as evidence of progress in LLM-based web extraction while preserving the thesis gap around robust, source-grounded, schema-aware extraction.

---

## One-sentence summary

ScrapeGraphAI-100k shows that **Introduces a 93,695-example real-world dataset of LLM web extraction events derived from 9M opt-in ScrapeGraphAI telemetry events, including Markdown content, prompt, JSON schema, LLM response, and complexity/validation metadata**, but generalized web data extraction still requires stronger schema adherence, provenance, verification, and deployment robustness.

---

## BibTeX

```bibtex
@article{brach2026scrapegraphai100k,
  title         = {ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction},
  author        = {William Brach, Francesco Zuppichini, Marco Vinciguerra, Lorenzo Padoan},
  journal       = {arXiv preprint; no final peer-reviewed venue confirmed in this check},
  year          = {2026},
  doi           = {10.48550/arXiv.2602.15189},
  eprint        = {2602.15189},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2602.15189}
}
```

---

## Source links

- https://arxiv.org/abs/2602.15189
- https://arxiv.org/abs/2602.15189


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\S6_P1_reading_index_and_venue_status.md

# S6 P1 — Reading Index and Venue/Status Check

## Corrected corpus status

```text
11 uploaded/listed S6 P1 files
10 unique S6 P1 citation papers
1 duplicate/moved paper archived
```

Archived duplicate/moved paper:

```text
BardeenAgent / WebLists
→ already used as S6 P0
→ do not cite again in S6 P1
```

Version note:

```text
2024-10 Infogent and 2025-05 INFOGEN are the same paper/version line.
Use the final citation: Infogent, Findings of NAACL 2025.
```

## Final reading order

| # | Paper | Venue/status | Role |
|---:|---|---|---|
| 1 | AutoScraper | EMNLP 2024 Main Conference | scraper generation |
| 2 | Infogent | Findings of NAACL 2025 | web information aggregation |
| 3 | ReaderLM-v2 | arXiv preprint | HTML-to-Markdown/JSON |
| 4 | NEXT-EVAL | arXiv preprint; no final accepted venue confirmed | extraction evaluation / record extraction |
| 5 | STRUCTSENSE | arXiv preprint / OpenReview entry | ontology + HITL structured extraction |
| 6 | Systematic Review of Web Scraping | Data & Knowledge Engineering 2026 | survey/background/legal-ethical |
| 7 | SCRIBES | ICLR 2026 Poster | RL-based reusable scripts |
| 8 | IndexLM | arXiv preprint | index-based content extraction |
| 9 | Beyond BeautifulSoup | AICS Workshop at AAAI 2026 + arXiv | practical scraping benchmark |
| 10 | ScrapeGraphAI-100k | arXiv preprint | dataset/schema-constrained extraction |

## Main S6 P1 taxonomy

```text
1. Reusable scraper and script generation
   - AutoScraper
   - SCRIBES

2. Extraction evaluation / record extraction benchmark
   - NEXT-EVAL

3. Web information aggregation
   - Infogent

4. HTML/content extraction infrastructure
   - ReaderLM-v2
   - IndexLM

5. Schema/ontology/HITL extraction
   - STRUCTSENSE
   - ScrapeGraphAI-100k

6. Benchmarking and practical scraping usability
   - Beyond BeautifulSoup

7. Background survey and legal/ethical grounding
   - Systematic Review of Web Scraping
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_deep_verified_markdowns_UPDATED_with_NEXT_EVAL\S6_P1_venue_status_report.md

# S6 P1 — Venue / Journal Status Report

## Status table

| Paper | Final venue/status | Evidence used |
|---|---|---|
| AutoScraper | EMNLP 2024 Main Conference | ACL Anthology + arXiv + official GitHub |
| Infogent | Findings of NAACL 2025 | ACL Anthology + arXiv + project page |
| ReaderLM-v2 | arXiv preprint; no final peer-reviewed venue confirmed in this check | arXiv + Jina AI project/blog |
| STRUCTSENSE | arXiv preprint / OpenReview entry; no final peer-reviewed venue confirmed in this check | arXiv + OpenReview + GitHub |
| Systematic Review of Web Scraping | Data & Knowledge Engineering, Volume 164, July 2026, Article 102598; earlier SSRN preprint posted September 2025 | ScienceDirect search result + SSRN preprint page |
| SCRIBES | ICLR 2026 Poster | OpenReview ICLR 2026 + arXiv |
| IndexLM / Index-based Web Content Extraction | CoRR/arXiv preprint; no final peer-reviewed venue confirmed in this check | arXiv + DBLP/CoRR result |
| Beyond BeautifulSoup | AICS Workshop at AAAI 2026 + arXiv preprint | arXiv + Gang Wang publications page + AICS 2026 program |
| ScrapeGraphAI-100k | arXiv preprint; no final peer-reviewed venue confirmed in this check | arXiv + Hugging Face / project release |

## Important corrections

```text
AutoScraper
→ EMNLP 2024 Main Conference
→ not only arXiv

Infogent
→ Findings of NAACL 2025
→ not only arXiv

SCRIBES
→ ICLR 2026 Poster
→ not only arXiv

Systematic Review of Web Scraping
→ Data & Knowledge Engineering, Volume 164, July 2026, Article 102598
→ SSRN version is only the earlier preprint

Beyond BeautifulSoup
→ AICS Workshop at AAAI 2026 + arXiv

BardeenAgent/WebLists
→ moved to S6 P0 only; not duplicated in S6 P1
```

## Papers with no final peer-reviewed venue confirmed in this check

```text
ReaderLM-v2
STRUCTSENSE
Index-based Web Content Extraction
ScrapeGraphAI-100k
```

These should be cited as arXiv/preprints unless a final venue appears later.


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_reading_index_and_venue_status.md

# S6 P1 — Reading Index and Venue/Status Check

## Corpus status

```text
10 uploaded S6 P1 files in this batch
9 unique S6 P1 citation papers
1 duplicate/moved paper archived
```

Archived duplicate/moved paper:

```text
BardeenAgent / WebLists
→ already used as S6 P0
→ do not cite again in S6 P1
```

## Final reading order

| # | Paper | Year | Venue/status | BibTeX key | Cluster |
|---:|---|---:|---|---|---|
| 1 | AutoScraper | 2024 | EMNLP 2024 Main Conference | `huang2024autoscraper` | LLM-generated reusable web scrapers |
| 2 | Infogent | 2025 | Findings of NAACL 2025 | `reddy2025infogent` | web information aggregation |
| 3 | ReaderLM-v2 | 2025 | arXiv preprint; no final peer-reviewed venue confirmed in this check | `wang2025readerlmv2` | HTML-to-Markdown and schema-guided JSON extraction |
| 4 | STRUCTSENSE | 2025 | arXiv preprint / OpenReview entry; no final peer-reviewed venue confirmed in this check | `chhetri2025structsense` | agentic structured information extraction with ontology and HITL |
| 5 | Systematic Review of Web Scraping | 2026 | Data & Knowledge Engineering, Volume 164, July 2026, Article 102598; earlier SSRN preprint posted September 2025 | `kahlon2026systematicwebscraping` | survey/background: scraping techniques, metrics, legal and ethical issues |
| 6 | SCRIBES | 2026 | ICLR 2026 Poster | `liu2026scribes` | RL-trained reusable extraction scripts for semi-structured web data |
| 7 | IndexLM / Index-based Web Content Extraction | 2025 | CoRR/arXiv preprint; no final peer-reviewed venue confirmed in this check | `chen2025indexwebextraction` | index-based query-relevant content extraction for RAG/web agents |
| 8 | Beyond BeautifulSoup | 2026 | AICS Workshop at AAAI 2026 + arXiv preprint | `bhardwaj2026beyondbeautifulsoup` | benchmarking LLM-powered scraping accessibility and security tiers |
| 9 | ScrapeGraphAI-100k | 2026 | arXiv preprint; no final peer-reviewed venue confirmed in this check | `brach2026scrapegraphai100k` | large-scale real-world LLM extraction dataset |

## Main S6 P1 taxonomy

```text
1. Reusable scraper and script generation
   - AutoScraper
   - SCRIBES

2. Web information aggregation
   - Infogent

3. HTML/content extraction infrastructure
   - ReaderLM-v2
   - IndexLM

4. Schema/ontology/HITL extraction
   - STRUCTSENSE
   - ScrapeGraphAI-100k

5. Benchmarking and practical scraping usability
   - Beyond BeautifulSoup

6. Background survey and legal/ethical grounding
   - Systematic Review of Web Scraping
```

## Main S6 P1 conclusion

```text
S6 P1 expands WebLists from one extraction benchmark into a full extraction stack:
scraper generation + aggregation + HTML cleaning + index-based context selection
+ reusable RL scripts + schema-constrained datasets + HITL/ontology validation
+ legal/ethical/practical scraping constraints.
```

## Central S6 gap preserved

```text
The field now has strong components for extraction,
but no unified system fully solves:
interactive navigation
+ reusable extraction logic
+ schema adherence
+ source provenance
+ field-level verification
+ dynamic website robustness
+ cost efficiency
+ legal/ethical safety.
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\P1\S6_P1_venue_status_report.md

# S6 P1 — Venue / Journal Status Report

## Status table

| Paper | Final venue/status | Evidence used |
|---|---|---|
| AutoScraper | EMNLP 2024 Main Conference | ACL Anthology + arXiv + official GitHub |
| Infogent | Findings of NAACL 2025 | ACL Anthology + arXiv + project page |
| ReaderLM-v2 | arXiv preprint; no final peer-reviewed venue confirmed in this check | arXiv + Jina AI project/blog |
| STRUCTSENSE | arXiv preprint / OpenReview entry; no final peer-reviewed venue confirmed in this check | arXiv + OpenReview + GitHub |
| Systematic Review of Web Scraping | Data & Knowledge Engineering, Volume 164, July 2026, Article 102598; earlier SSRN preprint posted September 2025 | ScienceDirect search result + SSRN preprint page |
| SCRIBES | ICLR 2026 Poster | OpenReview ICLR 2026 + arXiv |
| IndexLM / Index-based Web Content Extraction | CoRR/arXiv preprint; no final peer-reviewed venue confirmed in this check | arXiv + DBLP/CoRR result |
| Beyond BeautifulSoup | AICS Workshop at AAAI 2026 + arXiv preprint | arXiv + Gang Wang publications page + AICS 2026 program |
| ScrapeGraphAI-100k | arXiv preprint; no final peer-reviewed venue confirmed in this check | arXiv + Hugging Face / project release |

## Important corrections

```text
AutoScraper
→ EMNLP 2024 Main Conference
→ not only arXiv

Infogent
→ Findings of NAACL 2025
→ not only arXiv

SCRIBES
→ ICLR 2026 Poster
→ not only arXiv

Systematic Review of Web Scraping
→ Data & Knowledge Engineering, Volume 164, July 2026, Article 102598
→ SSRN version is only the earlier preprint

Beyond BeautifulSoup
→ AICS Workshop at AAAI 2026 + arXiv

BardeenAgent/WebLists
→ moved to S6 P0 only; not duplicated in S6 P1
```

## Papers with no final peer-reviewed venue confirmed in this check

```text
ReaderLM-v2
STRUCTSENSE
Index-based Web Content Extraction
ScrapeGraphAI-100k
```

These should be cited as arXiv/preprints unless a final venue appears later.


---

## Synthesis / Writing Notes (3 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\Writing\S6_P0_synthesis_WebLists.md

# S6 P0 Synthesis — LLM-based Agents for Web Data Extraction

## 1. Purpose of S6

S6 is the most thesis-specific section.

Earlier sections covered:

```text
S2 → LLM/VLM foundations
S3 → general agent reasoning and tool use
S4 → web-agent systems
S5.1 → web-agent benchmarks
S5.2 → perception and grounding
S5.3 → planning and reasoning
S5.4 → training and generalization
S5.5 → failure modes and reliability
```

S6 now answers:

```text
How can LLM-based agents extract structured data from the web?
```

The P0 anchor paper is:

```text
WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents
```

This is the right P0 paper because it directly targets:

```text
interactive schema-bound structured web data extraction
```

---

## 2. Why WebLists changes the discussion

Most web-agent papers evaluate success through tasks like:

```text
navigate to a page
click a button
buy an item
answer a question
fill a form
complete an online workflow
```

WebLists argues that these are not enough for real business extraction.

A data-extraction agent must produce:

```text
complete rows
consistent columns
machine-readable tables
high recall
high precision
low cost per row
schema adherence
repeatable extraction logic
```

This changes the evaluation target from:

```text
Did the agent finish the task?
```

to:

```text
Did the agent extract the complete structured dataset correctly?
```

This is the central S6 shift.

---

## 3. Main S6 P0 narrative

The main narrative from WebLists is:

```text
web data extraction is not only web navigation.
It is interactive, schema-bound, repeatable, and dataset-scale.
```

The agent must combine:

```text
navigation
interaction
DOM understanding
list detection
selector generation
pagination handling
schema mapping
structured output
verification
cost control
```

BardeenAgent proposes that the best way to scale extraction is not to ask the LLM to extract every item. Instead:

```text
use the LLM to discover the extraction program,
then execute the program deterministically.
```

This is the main conceptual bridge between:

```text
LLM-based agents
and
classical web scraping / wrapper induction
```

---

## 4. WebLists benchmark contribution

WebLists contributes:

```text
200 extraction tasks
50 live websites
4 business use cases
deterministic evaluation scripts
schema-bound output
```

The four use cases are:

```text
Blogs / product updates
Testimonials / customer case studies
Jobs
Job categories / filtered jobs
```

This benchmark is important because it tests extraction at dataset scale.

The most important benchmark gap it exposes is:

```text
agents can answer questions better than they can extract complete datasets.
```

For example:

```text
LLM + Search:
  Q&A accuracy: 42.0%
  WebLists recall: 3.3%
```

This shows that web search + answer generation is not equivalent to structured extraction.

---

## 5. BardeenAgent architecture contribution

BardeenAgent introduces the idea of executable LLM agents for extraction.

The pipeline is:

```text
Record:
  navigate
  interact
  identify list
  extract first item
  record actions with CSS selectors

Replay:
  convert recording into executable program
  loop over list items
  handle pagination
  output structured table
```

This is important because it prevents:

```text
LLM output-length bottlenecks
per-item LLM calls
compounding extraction errors
high cost per row
early termination
```

The key insight is:

```text
HTML pages often contain regular repeated structures.
If the agent can extract one item correctly,
a program can extract all similar items.
```

---

## 6. Main empirical result

The key result is recall:

```text
LLM + Search:   3.3
Agent-E:       12.1
Wilbur:        30.5
BardeenAgent:  66.2
```

This shows that general-purpose web agents are not sufficient for structured extraction.

BardeenAgent also improves cost per correct output row:

```text
Agent-E:       3.21 cents
Wilbur:        4.55 cents
BardeenAgent:  1.07 cents
```

This is crucial for deployment because extraction often involves many rows.

---

## 7. Central S6 gap after WebLists

WebLists solves an important part of structured extraction, but the central S6 gap remains:

```text
Current LLM-agent extraction systems still do not fully solve:
robust selector generation
complex widget interaction
dynamic website changes
high-precision filtering
schema-level validation
field-level correctness
source provenance
multi-site generalization
CAPTCHA/authentication issues
legal and ethical constraints
human-in-the-loop validation
```

This gap is exactly aligned with your thesis.

---

## 8. Connection to previous sections

## 8.1 From S5.2 to S6

S5.2 showed that agents need robust perception and grounding.

WebLists shows why:

```text
structured extraction depends on identifying repeated DOM/list structures,
not just clicking the next correct element.
```

## 8.2 From S5.3 to S6

S5.3 showed that agents need planning.

WebLists shows extraction-specific planning:

```text
navigate → configure → enter list mode → extract first item → replay across pages
```

## 8.3 From S5.4 to S6

S5.4 showed training and data generation.

WebLists suggests future training objectives:

```text
selector generation
schema mapping
list detection
pagination handling
extraction completeness
source verification
```

## 8.4 From S5.5 to S6

S5.5 showed failures.

WebLists adds extraction-specific failures:

```text
low recall
missing rows
wrong list selection
wrong filter application
over-generalized selectors
incomplete pagination
missing URLs
LLM output limit
compounding errors
```

---

## 9. Thesis-ready S6 P0 synthesis paragraph

WebLists provides the first strong S6 anchor because it reframes web agents around structured data extraction rather than navigation or question answering. Bohra et al. argue that existing benchmarks underrepresent real business extraction tasks, where the agent must navigate to the appropriate webpage, interact with filters or pagination, and extract complete datasets under a predefined schema. The WebLists benchmark contains 200 tasks across 50 live websites and four use cases: blogs, testimonials, jobs, and filtered job categories. The paper shows that general-purpose approaches struggle: LLM+Search reaches only 3.3% overall recall, Agent-E reaches 12.1%, and Wilbur reaches 30.5%. To address this, BardeenAgent records one successful extraction trajectory, converts it into a reusable executable program, and replays it using CSS selectors, scoped list extraction, and pagination handling. This exploits the regular structure of HTML and reduces repeated LLM calls, allowing BardeenAgent to reach 66.2% recall and reduce cost per correct output row by more than 3×. For the thesis, WebLists is essential because it defines the extraction-specific problem that general web-agent benchmarks miss: complete, schema-bound, source-grounded, scalable extraction from interactive websites. The remaining gap is to improve selector reliability, complex interaction handling, precision, schema validation, provenance tracking, and robust extraction under dynamic live-web conditions.

---

## 10. Final S6 P0 conclusion

The main conclusion is:

```text
WebLists shows that structured web data extraction requires a different agent design
from general web navigation.
```

The S6 thesis argument should therefore be:

```text
LLM-based web agents need an extraction-specific architecture:
perception + planning + executable replay + schema binding + verification.
```

WebLists/BardeenAgent provides the first strong step, but your thesis can build on its gaps:

```text
more robust selectors
visual-DOM alignment
schema-aware verification
source provenance
interactive widget handling
dynamic site adaptation
human-in-the-loop correction
safe and ethical deployment
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\Writing\S6_P1_full_refined_synthesis.md

# S6 P1 Refined Synthesis — LLM-Based Web Information Extraction and Aggregation

## Updated version including NEXT-EVAL

## 1. What S6 P1 adds after S6 P0

S6 P0 was anchored by **WebLists/BardeenAgent**, which established the central thesis problem:

```text
interactive schema-bound structured web data extraction
```

S6 P1 expands this into a full research landscape.

The new picture is:

```text
Web extraction is not a single model call.
It is a pipeline:
access → clean → select → extract → structure → validate → replay → aggregate → evaluate → deploy.
```

The S6 P1 papers cover different parts of this pipeline.

---

## 2. Corrected corpus status

The corrected S6 P1 status is:

```text
11 uploaded/listed S6 P1 files
10 unique S6 P1 citation papers
1 duplicate/moved paper archived
```

Important cleanup:

```text
BardeenAgent / WebLists
→ already used as S6 P0
→ do not cite again in S6 P1
```

Important correction:

```text
NEXT-EVAL was missing from the first S6 P1 synthesis.
It is now included as the extraction-evaluation paper.
```

Infogent note:

```text
2024-10 Infogent and 2025-05 INFOGEN refer to the same paper/version line.
Use the final citation: Infogent, Findings of NAACL 2025.
```

---

## 3. Main S6 P1 taxonomy

| Cluster | Papers | Main idea |
|---|---|---|
| Interactive structured extraction anchor | WebLists/BardeenAgent | S6 P0 anchor; interactive schema-bound extraction from live websites |
| Extraction evaluation / record extraction benchmark | NEXT-EVAL | DOM-grounded, XPath-based, structure-aware evaluation for traditional and LLM web data record extraction |
| Reusable scraper/script generation | AutoScraper, SCRIBES | Generate reusable extraction programs/scripts instead of extracting each page with an LLM |
| Web information aggregation | Infogent | Extract and synthesize information across multiple sources |
| HTML/content extraction infrastructure | ReaderLM-v2, IndexLM | Clean, compress, and transform long messy HTML into Markdown/JSON or relevant content blocks |
| Schema/ontology/HITL extraction | STRUCTSENSE, ScrapeGraphAI-100k | Improve structured extraction with ontologies, schemas, validation, datasets, and human feedback |
| Practical scraping benchmark | Beyond BeautifulSoup | Compare LLM-assisted scripting and end-to-end agents under realistic site complexity |
| Background and ethics | Systematic Review of Web Scraping | Connect LLM scraping to classical techniques, metrics, and legal/ethical issues |

---

## 4. Core narrative

The S6 P1 narrative should be:

```text
LLM-based web extraction is moving from direct per-page generation
toward reusable extraction programs, specialized extraction models,
schema-constrained datasets, structure-aware evaluation,
process validation, and practical deployment analysis.
```

This is a major shift.

Earlier approaches often used:

```text
HTML page + prompt → LLM output
```

S6 P1 shows newer approaches using:

```text
HTML page + task → reusable scraper/script
MHTML snapshot + XPath labels → structure-aware evaluation
HTML page + query → relevant index intervals
HTML page + instruction → Markdown/JSON
multi-source query → Navigator + Extractor + Aggregator
schema + content → validated JSON
website group → reusable script trained by RL
```

---

## 5. Paper cluster synthesis

## 5.1 NEXT-EVAL: extraction evaluation and DOM-grounded record extraction

**NEXT-EVAL** fills an important gap that was missing from the first S6 P1 synthesis: evaluation.

Its core idea is:

```text
web extraction should be evaluated with DOM-grounded,
structure-aware metrics rather than only text-output matching.
```

NEXT-EVAL builds evaluation datasets from:

```text
MHTML snapshots
XPath-based labels
DOM-preserving preprocessing
structure-aware metrics
```

This is highly relevant to S6 because extraction systems often output plausible text or records that may not be grounded in the correct webpage element.

The paper compares different input formats:

```text
Slimmed HTML
Hierarchical JSON
Flat JSON
```

The headline result is:

```text
Flat JSON input achieves F1 = 0.9567
```

The key lesson for the thesis is:

```text
web data extraction evaluation must preserve source structure.
```

NEXT-EVAL complements WebLists:

```text
WebLists = task benchmark for interactive schema-bound extraction
NEXT-EVAL = evaluation framework for DOM-grounded record extraction
```

Its limitation is that it does not fully solve interactive navigation, pagination, filtering, live-web drift, source provenance across multiple pages, or semantic verification of extracted values.

---

## 5.2 AutoScraper and SCRIBES: reusable extraction programs

**AutoScraper** and **SCRIBES** are central because they avoid repeated LLM extraction.

Their shared idea is:

```text
use the LLM to produce extraction logic,
then run that logic repeatedly and cheaply.
```

AutoScraper does this through progressive understanding and scraper synthesis. SCRIBES does this through RL-trained script generation across structurally similar pages.

This cluster connects strongly to WebLists/BardeenAgent.

The core thesis lesson is:

```text
scalable extraction needs executable/reusable logic,
not only one-shot LLM answers.
```

NEXT-EVAL strengthens this cluster because reusable scrapers and scripts need evaluation protocols that check whether extracted records correspond to correct DOM locations, not just whether generated text looks plausible.

---

## 5.3 Infogent: extraction as multi-source aggregation

**Infogent** shifts S6 from page-level extraction to multi-source aggregation.

It decomposes the task into:

```text
Navigator
Extractor
Aggregator
```

This matters because many real extraction tasks require several sources, not one webpage.

For the thesis, Infogent supports the claim that generalized web extraction may require:

```text
backtracking
source selection
coverage monitoring
evidence aggregation
final synthesis
```

Its limitation is that it focuses more on aggregation and final answer quality than complete schema-bound row-level extraction.

---

## 5.4 ReaderLM-v2 and IndexLM: extraction infrastructure

**ReaderLM-v2** and **IndexLM** are not full web agents, but they are crucial infrastructure.

ReaderLM-v2 converts messy HTML into clean Markdown or JSON.

IndexLM extracts relevant indexed HTML blocks instead of generating content token by token.

Together, they address a key practical problem:

```text
webpages are too long, noisy, and low-signal for direct LLM use.
```

The thesis should use them to argue that web extraction agents need a preprocessing and context-management layer.

NEXT-EVAL connects directly here because it shows that representation format matters: Flat JSON can strongly improve extraction performance.

---

## 5.5 STRUCTSENSE and ScrapeGraphAI-100k: schema and validation

**STRUCTSENSE** introduces agentic structured extraction with:

```text
Extractor Agent
Alignment Agent
Judge Agent
Feedback Agent
ontology database
memory
human feedback
```

**ScrapeGraphAI-100k** provides a large real-world dataset of prompt + content + schema + LLM response + validation metadata.

Together, they expose a central S6 issue:

```text
schema validity is not the same as semantic correctness.
```

A model can produce valid JSON while extracting wrong values. This is one of the most important thesis gaps.

NEXT-EVAL adds another angle:

```text
even if output text looks correct, evaluation should check whether the extraction is grounded in the correct DOM/XPath location.
```

So S6 needs both:

```text
schema validation
+ DOM/source grounding
+ semantic value verification
```

---

## 5.6 Beyond BeautifulSoup and the systematic review: practical and ethical framing

**Beyond BeautifulSoup** shows that LLM-powered scraping changes who can scrape the web. It compares LLM-assisted scripting with end-to-end agents across five website complexity tiers.

The **Systematic Review of Web Scraping** gives the broader foundation: classical techniques, tools, metrics, LLM-enhanced approaches, legal and ethical issues.

Together, they connect S6 to deployment:

```text
web extraction is technical, practical, legal, and ethical.
```

This is important because extraction systems must be evaluated not only by technical success, but also by compliance, safety, user effort, cost, and possible misuse.

---

## 6. Refined S6 gap after P1

After adding NEXT-EVAL, the central gap becomes sharper:

```text
Current systems solve parts of LLM-based web extraction,
but no system jointly solves:
interactive navigation
+ robust HTML/DOM understanding
+ reusable extraction programs
+ DOM-grounded evaluation
+ schema-constrained output
+ field-level correctness
+ source provenance
+ semantic validation
+ multi-source aggregation
+ dynamic website robustness
+ cost-efficient deployment
+ legal/ethical compliance.
```

This is the thesis opportunity.

---

## 7. Extraction-specific reliability gap

The extraction-specific gap should be stated explicitly:

```text
Current systems can often extract plausible structured outputs,
but they do not consistently prove that each extracted field is:
1. present on the source page,
2. attached to the correct record,
3. mapped to the correct schema field,
4. semantically correct,
5. complete across pagination or multiple pages,
6. robust to DOM/layout changes,
7. safe and compliant to extract.
```

NEXT-EVAL helps with item 1 and part of item 2 through DOM/XPath-grounded evaluation.

WebLists helps with interactive schema-bound extraction.

AutoScraper and SCRIBES help with reusable extraction logic.

ReaderLM-v2 and IndexLM help with input representation and content selection.

ScrapeGraphAI-100k helps with schema-constrained training and failure analysis.

STRUCTSENSE helps with ontology and human validation.

But the full stack is still missing.

---

## 8. Cross-links to later sections

| Paper / cluster | Feeds |
|---|---|
| WebLists/BardeenAgent | S6 P0 anchor; executable interactive structured extraction |
| NEXT-EVAL | S6 evaluation; S7 provenance/verification; S5.1 benchmark design |
| AutoScraper | S8 cost-efficient automation; S6 executable extraction |
| Infogent | S6 aggregation; S7 verification; S5.7 deep research |
| ReaderLM-v2 | S5.2 representation; S6 preprocessing; RAG grounding |
| STRUCTSENSE | S7 verification; ontology alignment; HITL |
| Systematic Review | S8 legal/ethical issues; S6.1 classical foundations |
| SCRIBES | S5.4 RL; S6 reusable script extraction; S8 web-scale deployment |
| IndexLM | S5.2 context compression; S6 query-relevant extraction |
| Beyond BeautifulSoup | S8 deployment, usability, abuse/anti-bot implications |
| ScrapeGraphAI-100k | S5.4 fine-tuning; S6 schema benchmarking; S7 failure analysis |

---

## 9. Thesis-ready synthesis paragraph

The S6 P1 literature expands the WebLists/BardeenAgent extraction problem into a broader stack for LLM-based web information extraction. NEXT-EVAL adds an essential evaluation layer by showing that web data record extraction should be assessed with DOM-grounded, XPath-based, and structure-aware metrics rather than only text-output matching; its finding that Flat JSON reaches 0.9567 F1 highlights the importance of representation choice for LLM-based extraction. AutoScraper and SCRIBES show that scalable extraction should not rely on repeated per-page LLM inference; instead, LLMs can generate reusable scrapers or scripts that exploit repeated website structure. Infogent broadens extraction from single-page extraction to multi-source web information aggregation through a Navigator–Extractor–Aggregator architecture. ReaderLM-v2 and IndexLM address the input bottleneck by converting noisy HTML into clean Markdown/JSON or by selecting relevant indexed HTML blocks for downstream RAG and agent reasoning. STRUCTSENSE adds ontology grounding, judge agents, and human-in-the-loop feedback for structured extraction, while ScrapeGraphAI-100k contributes a large real-world dataset for schema-constrained LLM extraction and exposes how schema complexity drives failure. Beyond BeautifulSoup evaluates the practical accessibility of LLM-powered scraping for everyday users across static, authenticated, and CAPTCHA-protected websites, while the systematic web scraping review connects these LLM methods to classical scraping techniques, performance metrics, and legal-ethical concerns. Together, these papers show that LLM-based web extraction is evolving from direct generation into a multi-layered system involving executable extraction logic, content cleaning, schema validation, DOM-grounded evaluation, source aggregation, fine-tuning data, and deployment constraints. The remaining thesis gap is to unify these components into a robust extraction agent that can navigate dynamic websites, extract schema-bound data, preserve provenance, verify field-level correctness, and operate safely and efficiently at scale.

---

## 10. Final S6 P1 conclusion

The final conclusion is:

```text
S6 P1 shows that the future of web extraction is hybrid:
LLM reasoning + classical scraping logic + executable scripts
+ DOM-grounded evaluation + schema-constrained validation
+ efficient content selection + human/source-grounded verification.
```

This should lead naturally into the next section:

```text
S7 should focus on verification, provenance, correctness, and trust.
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\Writing\S6_P1_full_refined_synthesis_UPDATED_with_NEXT_EVAL.md

# S6 P1 Refined Synthesis — LLM-Based Web Information Extraction and Aggregation

## Updated version including NEXT-EVAL

## 1. What S6 P1 adds after S6 P0

S6 P0 was anchored by **WebLists/BardeenAgent**, which established the central thesis problem:

```text
interactive schema-bound structured web data extraction
```

S6 P1 expands this into a full research landscape.

The new picture is:

```text
Web extraction is not a single model call.
It is a pipeline:
access → clean → select → extract → structure → validate → replay → aggregate → evaluate → deploy.
```

The S6 P1 papers cover different parts of this pipeline.

---

## 2. Corrected corpus status

The corrected S6 P1 status is:

```text
11 uploaded/listed S6 P1 files
10 unique S6 P1 citation papers
1 duplicate/moved paper archived
```

Important cleanup:

```text
BardeenAgent / WebLists
→ already used as S6 P0
→ do not cite again in S6 P1
```

Important correction:

```text
NEXT-EVAL was missing from the first S6 P1 synthesis.
It is now included as the extraction-evaluation paper.
```

Infogent note:

```text
2024-10 Infogent and 2025-05 INFOGEN refer to the same paper/version line.
Use the final citation: Infogent, Findings of NAACL 2025.
```

---

## 3. Main S6 P1 taxonomy

| Cluster | Papers | Main idea |
|---|---|---|
| Interactive structured extraction anchor | WebLists/BardeenAgent | S6 P0 anchor; interactive schema-bound extraction from live websites |
| Extraction evaluation / record extraction benchmark | NEXT-EVAL | DOM-grounded, XPath-based, structure-aware evaluation for traditional and LLM web data record extraction |
| Reusable scraper/script generation | AutoScraper, SCRIBES | Generate reusable extraction programs/scripts instead of extracting each page with an LLM |
| Web information aggregation | Infogent | Extract and synthesize information across multiple sources |
| HTML/content extraction infrastructure | ReaderLM-v2, IndexLM | Clean, compress, and transform long messy HTML into Markdown/JSON or relevant content blocks |
| Schema/ontology/HITL extraction | STRUCTSENSE, ScrapeGraphAI-100k | Improve structured extraction with ontologies, schemas, validation, datasets, and human feedback |
| Practical scraping benchmark | Beyond BeautifulSoup | Compare LLM-assisted scripting and end-to-end agents under realistic site complexity |
| Background and ethics | Systematic Review of Web Scraping | Connect LLM scraping to classical techniques, metrics, and legal/ethical issues |

---

## 4. Core narrative

The S6 P1 narrative should be:

```text
LLM-based web extraction is moving from direct per-page generation
toward reusable extraction programs, specialized extraction models,
schema-constrained datasets, structure-aware evaluation,
process validation, and practical deployment analysis.
```

This is a major shift.

Earlier approaches often used:

```text
HTML page + prompt → LLM output
```

S6 P1 shows newer approaches using:

```text
HTML page + task → reusable scraper/script
MHTML snapshot + XPath labels → structure-aware evaluation
HTML page + query → relevant index intervals
HTML page + instruction → Markdown/JSON
multi-source query → Navigator + Extractor + Aggregator
schema + content → validated JSON
website group → reusable script trained by RL
```

---

## 5. Paper cluster synthesis

## 5.1 NEXT-EVAL: extraction evaluation and DOM-grounded record extraction

**NEXT-EVAL** fills an important gap that was missing from the first S6 P1 synthesis: evaluation.

Its core idea is:

```text
web extraction should be evaluated with DOM-grounded,
structure-aware metrics rather than only text-output matching.
```

NEXT-EVAL builds evaluation datasets from:

```text
MHTML snapshots
XPath-based labels
DOM-preserving preprocessing
structure-aware metrics
```

This is highly relevant to S6 because extraction systems often output plausible text or records that may not be grounded in the correct webpage element.

The paper compares different input formats:

```text
Slimmed HTML
Hierarchical JSON
Flat JSON
```

The headline result is:

```text
Flat JSON input achieves F1 = 0.9567
```

The key lesson for the thesis is:

```text
web data extraction evaluation must preserve source structure.
```

NEXT-EVAL complements WebLists:

```text
WebLists = task benchmark for interactive schema-bound extraction
NEXT-EVAL = evaluation framework for DOM-grounded record extraction
```

Its limitation is that it does not fully solve interactive navigation, pagination, filtering, live-web drift, source provenance across multiple pages, or semantic verification of extracted values.

---

## 5.2 AutoScraper and SCRIBES: reusable extraction programs

**AutoScraper** and **SCRIBES** are central because they avoid repeated LLM extraction.

Their shared idea is:

```text
use the LLM to produce extraction logic,
then run that logic repeatedly and cheaply.
```

AutoScraper does this through progressive understanding and scraper synthesis. SCRIBES does this through RL-trained script generation across structurally similar pages.

This cluster connects strongly to WebLists/BardeenAgent.

The core thesis lesson is:

```text
scalable extraction needs executable/reusable logic,
not only one-shot LLM answers.
```

NEXT-EVAL strengthens this cluster because reusable scrapers and scripts need evaluation protocols that check whether extracted records correspond to correct DOM locations, not just whether generated text looks plausible.

---

## 5.3 Infogent: extraction as multi-source aggregation

**Infogent** shifts S6 from page-level extraction to multi-source aggregation.

It decomposes the task into:

```text
Navigator
Extractor
Aggregator
```

This matters because many real extraction tasks require several sources, not one webpage.

For the thesis, Infogent supports the claim that generalized web extraction may require:

```text
backtracking
source selection
coverage monitoring
evidence aggregation
final synthesis
```

Its limitation is that it focuses more on aggregation and final answer quality than complete schema-bound row-level extraction.

---

## 5.4 ReaderLM-v2 and IndexLM: extraction infrastructure

**ReaderLM-v2** and **IndexLM** are not full web agents, but they are crucial infrastructure.

ReaderLM-v2 converts messy HTML into clean Markdown or JSON.

IndexLM extracts relevant indexed HTML blocks instead of generating content token by token.

Together, they address a key practical problem:

```text
webpages are too long, noisy, and low-signal for direct LLM use.
```

The thesis should use them to argue that web extraction agents need a preprocessing and context-management layer.

NEXT-EVAL connects directly here because it shows that representation format matters: Flat JSON can strongly improve extraction performance.

---

## 5.5 STRUCTSENSE and ScrapeGraphAI-100k: schema and validation

**STRUCTSENSE** introduces agentic structured extraction with:

```text
Extractor Agent
Alignment Agent
Judge Agent
Feedback Agent
ontology database
memory
human feedback
```

**ScrapeGraphAI-100k** provides a large real-world dataset of prompt + content + schema + LLM response + validation metadata.

Together, they expose a central S6 issue:

```text
schema validity is not the same as semantic correctness.
```

A model can produce valid JSON while extracting wrong values. This is one of the most important thesis gaps.

NEXT-EVAL adds another angle:

```text
even if output text looks correct, evaluation should check whether the extraction is grounded in the correct DOM/XPath location.
```

So S6 needs both:

```text
schema validation
+ DOM/source grounding
+ semantic value verification
```

---

## 5.6 Beyond BeautifulSoup and the systematic review: practical and ethical framing

**Beyond BeautifulSoup** shows that LLM-powered scraping changes who can scrape the web. It compares LLM-assisted scripting with end-to-end agents across five website complexity tiers.

The **Systematic Review of Web Scraping** gives the broader foundation: classical techniques, tools, metrics, LLM-enhanced approaches, legal and ethical issues.

Together, they connect S6 to deployment:

```text
web extraction is technical, practical, legal, and ethical.
```

This is important because extraction systems must be evaluated not only by technical success, but also by compliance, safety, user effort, cost, and possible misuse.

---

## 6. Refined S6 gap after P1

After adding NEXT-EVAL, the central gap becomes sharper:

```text
Current systems solve parts of LLM-based web extraction,
but no system jointly solves:
interactive navigation
+ robust HTML/DOM understanding
+ reusable extraction programs
+ DOM-grounded evaluation
+ schema-constrained output
+ field-level correctness
+ source provenance
+ semantic validation
+ multi-source aggregation
+ dynamic website robustness
+ cost-efficient deployment
+ legal/ethical compliance.
```

This is the thesis opportunity.

---

## 7. Extraction-specific reliability gap

The extraction-specific gap should be stated explicitly:

```text
Current systems can often extract plausible structured outputs,
but they do not consistently prove that each extracted field is:
1. present on the source page,
2. attached to the correct record,
3. mapped to the correct schema field,
4. semantically correct,
5. complete across pagination or multiple pages,
6. robust to DOM/layout changes,
7. safe and compliant to extract.
```

NEXT-EVAL helps with item 1 and part of item 2 through DOM/XPath-grounded evaluation.

WebLists helps with interactive schema-bound extraction.

AutoScraper and SCRIBES help with reusable extraction logic.

ReaderLM-v2 and IndexLM help with input representation and content selection.

ScrapeGraphAI-100k helps with schema-constrained training and failure analysis.

STRUCTSENSE helps with ontology and human validation.

But the full stack is still missing.

---

## 8. Cross-links to later sections

| Paper / cluster | Feeds |
|---|---|
| WebLists/BardeenAgent | S6 P0 anchor; executable interactive structured extraction |
| NEXT-EVAL | S6 evaluation; S7 provenance/verification; S5.1 benchmark design |
| AutoScraper | S8 cost-efficient automation; S6 executable extraction |
| Infogent | S6 aggregation; S7 verification; S5.7 deep research |
| ReaderLM-v2 | S5.2 representation; S6 preprocessing; RAG grounding |
| STRUCTSENSE | S7 verification; ontology alignment; HITL |
| Systematic Review | S8 legal/ethical issues; S6.1 classical foundations |
| SCRIBES | S5.4 RL; S6 reusable script extraction; S8 web-scale deployment |
| IndexLM | S5.2 context compression; S6 query-relevant extraction |
| Beyond BeautifulSoup | S8 deployment, usability, abuse/anti-bot implications |
| ScrapeGraphAI-100k | S5.4 fine-tuning; S6 schema benchmarking; S7 failure analysis |

---

## 9. Thesis-ready synthesis paragraph

The S6 P1 literature expands the WebLists/BardeenAgent extraction problem into a broader stack for LLM-based web information extraction. NEXT-EVAL adds an essential evaluation layer by showing that web data record extraction should be assessed with DOM-grounded, XPath-based, and structure-aware metrics rather than only text-output matching; its finding that Flat JSON reaches 0.9567 F1 highlights the importance of representation choice for LLM-based extraction. AutoScraper and SCRIBES show that scalable extraction should not rely on repeated per-page LLM inference; instead, LLMs can generate reusable scrapers or scripts that exploit repeated website structure. Infogent broadens extraction from single-page extraction to multi-source web information aggregation through a Navigator–Extractor–Aggregator architecture. ReaderLM-v2 and IndexLM address the input bottleneck by converting noisy HTML into clean Markdown/JSON or by selecting relevant indexed HTML blocks for downstream RAG and agent reasoning. STRUCTSENSE adds ontology grounding, judge agents, and human-in-the-loop feedback for structured extraction, while ScrapeGraphAI-100k contributes a large real-world dataset for schema-constrained LLM extraction and exposes how schema complexity drives failure. Beyond BeautifulSoup evaluates the practical accessibility of LLM-powered scraping for everyday users across static, authenticated, and CAPTCHA-protected websites, while the systematic web scraping review connects these LLM methods to classical scraping techniques, performance metrics, and legal-ethical concerns. Together, these papers show that LLM-based web extraction is evolving from direct generation into a multi-layered system involving executable extraction logic, content cleaning, schema validation, DOM-grounded evaluation, source aggregation, fine-tuning data, and deployment constraints. The remaining thesis gap is to unify these components into a robust extraction agent that can navigate dynamic websites, extract schema-bound data, preserve provenance, verify field-level correctness, and operate safely and efficiently at scale.

---

## 10. Final S6 P1 conclusion

The final conclusion is:

```text
S6 P1 shows that the future of web extraction is hybrid:
LLM reasoning + classical scraping logic + executable scripts
+ DOM-grounded evaluation + schema-constrained validation
+ efficient content selection + human/source-grounded verification.
```

This should lead naturally into the next section:

```text
S7 should focus on verification, provenance, correctness, and trust.
```


---

## Synthesis / Writing Notes (3 files)

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\writing\S6_P0_synthesis_WebLists.md

# S6 P0 Synthesis — LLM-based Agents for Web Data Extraction

## 1. Purpose of S6

S6 is the most thesis-specific section.

Earlier sections covered:

```text
S2 → LLM/VLM foundations
S3 → general agent reasoning and tool use
S4 → web-agent systems
S5.1 → web-agent benchmarks
S5.2 → perception and grounding
S5.3 → planning and reasoning
S5.4 → training and generalization
S5.5 → failure modes and reliability
```

S6 now answers:

```text
How can LLM-based agents extract structured data from the web?
```

The P0 anchor paper is:

```text
WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents
```

This is the right P0 paper because it directly targets:

```text
interactive schema-bound structured web data extraction
```

---

## 2. Why WebLists changes the discussion

Most web-agent papers evaluate success through tasks like:

```text
navigate to a page
click a button
buy an item
answer a question
fill a form
complete an online workflow
```

WebLists argues that these are not enough for real business extraction.

A data-extraction agent must produce:

```text
complete rows
consistent columns
machine-readable tables
high recall
high precision
low cost per row
schema adherence
repeatable extraction logic
```

This changes the evaluation target from:

```text
Did the agent finish the task?
```

to:

```text
Did the agent extract the complete structured dataset correctly?
```

This is the central S6 shift.

---

## 3. Main S6 P0 narrative

The main narrative from WebLists is:

```text
web data extraction is not only web navigation.
It is interactive, schema-bound, repeatable, and dataset-scale.
```

The agent must combine:

```text
navigation
interaction
DOM understanding
list detection
selector generation
pagination handling
schema mapping
structured output
verification
cost control
```

BardeenAgent proposes that the best way to scale extraction is not to ask the LLM to extract every item. Instead:

```text
use the LLM to discover the extraction program,
then execute the program deterministically.
```

This is the main conceptual bridge between:

```text
LLM-based agents
and
classical web scraping / wrapper induction
```

---

## 4. WebLists benchmark contribution

WebLists contributes:

```text
200 extraction tasks
50 live websites
4 business use cases
deterministic evaluation scripts
schema-bound output
```

The four use cases are:

```text
Blogs / product updates
Testimonials / customer case studies
Jobs
Job categories / filtered jobs
```

This benchmark is important because it tests extraction at dataset scale.

The most important benchmark gap it exposes is:

```text
agents can answer questions better than they can extract complete datasets.
```

For example:

```text
LLM + Search:
  Q&A accuracy: 42.0%
  WebLists recall: 3.3%
```

This shows that web search + answer generation is not equivalent to structured extraction.

---

## 5. BardeenAgent architecture contribution

BardeenAgent introduces the idea of executable LLM agents for extraction.

The pipeline is:

```text
Record:
  navigate
  interact
  identify list
  extract first item
  record actions with CSS selectors

Replay:
  convert recording into executable program
  loop over list items
  handle pagination
  output structured table
```

This is important because it prevents:

```text
LLM output-length bottlenecks
per-item LLM calls
compounding extraction errors
high cost per row
early termination
```

The key insight is:

```text
HTML pages often contain regular repeated structures.
If the agent can extract one item correctly,
a program can extract all similar items.
```

---

## 6. Main empirical result

The key result is recall:

```text
LLM + Search:   3.3
Agent-E:       12.1
Wilbur:        30.5
BardeenAgent:  66.2
```

This shows that general-purpose web agents are not sufficient for structured extraction.

BardeenAgent also improves cost per correct output row:

```text
Agent-E:       3.21 cents
Wilbur:        4.55 cents
BardeenAgent:  1.07 cents
```

This is crucial for deployment because extraction often involves many rows.

---

## 7. Central S6 gap after WebLists

WebLists solves an important part of structured extraction, but the central S6 gap remains:

```text
Current LLM-agent extraction systems still do not fully solve:
robust selector generation
complex widget interaction
dynamic website changes
high-precision filtering
schema-level validation
field-level correctness
source provenance
multi-site generalization
CAPTCHA/authentication issues
legal and ethical constraints
human-in-the-loop validation
```

This gap is exactly aligned with your thesis.

---

## 8. Connection to previous sections

## 8.1 From S5.2 to S6

S5.2 showed that agents need robust perception and grounding.

WebLists shows why:

```text
structured extraction depends on identifying repeated DOM/list structures,
not just clicking the next correct element.
```

## 8.2 From S5.3 to S6

S5.3 showed that agents need planning.

WebLists shows extraction-specific planning:

```text
navigate → configure → enter list mode → extract first item → replay across pages
```

## 8.3 From S5.4 to S6

S5.4 showed training and data generation.

WebLists suggests future training objectives:

```text
selector generation
schema mapping
list detection
pagination handling
extraction completeness
source verification
```

## 8.4 From S5.5 to S6

S5.5 showed failures.

WebLists adds extraction-specific failures:

```text
low recall
missing rows
wrong list selection
wrong filter application
over-generalized selectors
incomplete pagination
missing URLs
LLM output limit
compounding errors
```

---

## 9. Thesis-ready S6 P0 synthesis paragraph

WebLists provides the first strong S6 anchor because it reframes web agents around structured data extraction rather than navigation or question answering. Bohra et al. argue that existing benchmarks underrepresent real business extraction tasks, where the agent must navigate to the appropriate webpage, interact with filters or pagination, and extract complete datasets under a predefined schema. The WebLists benchmark contains 200 tasks across 50 live websites and four use cases: blogs, testimonials, jobs, and filtered job categories. The paper shows that general-purpose approaches struggle: LLM+Search reaches only 3.3% overall recall, Agent-E reaches 12.1%, and Wilbur reaches 30.5%. To address this, BardeenAgent records one successful extraction trajectory, converts it into a reusable executable program, and replays it using CSS selectors, scoped list extraction, and pagination handling. This exploits the regular structure of HTML and reduces repeated LLM calls, allowing BardeenAgent to reach 66.2% recall and reduce cost per correct output row by more than 3×. For the thesis, WebLists is essential because it defines the extraction-specific problem that general web-agent benchmarks miss: complete, schema-bound, source-grounded, scalable extraction from interactive websites. The remaining gap is to improve selector reliability, complex interaction handling, precision, schema validation, provenance tracking, and robust extraction under dynamic live-web conditions.

---

## 10. Final S6 P0 conclusion

The main conclusion is:

```text
WebLists shows that structured web data extraction requires a different agent design
from general web navigation.
```

The S6 thesis argument should therefore be:

```text
LLM-based web agents need an extraction-specific architecture:
perception + planning + executable replay + schema binding + verification.
```

WebLists/BardeenAgent provides the first strong step, but your thesis can build on its gaps:

```text
more robust selectors
visual-DOM alignment
schema-aware verification
source provenance
interactive widget handling
dynamic site adaptation
human-in-the-loop correction
safe and ethical deployment
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\writing\S6_P1_full_refined_synthesis.md

# S6 P1 Refined Synthesis — LLM-Based Web Information Extraction and Aggregation

## Updated version including NEXT-EVAL

## 1. What S6 P1 adds after S6 P0

S6 P0 was anchored by **WebLists/BardeenAgent**, which established the central thesis problem:

```text
interactive schema-bound structured web data extraction
```

S6 P1 expands this into a full research landscape.

The new picture is:

```text
Web extraction is not a single model call.
It is a pipeline:
access → clean → select → extract → structure → validate → replay → aggregate → evaluate → deploy.
```

The S6 P1 papers cover different parts of this pipeline.

---

## 2. Corrected corpus status

The corrected S6 P1 status is:

```text
11 uploaded/listed S6 P1 files
10 unique S6 P1 citation papers
1 duplicate/moved paper archived
```

Important cleanup:

```text
BardeenAgent / WebLists
→ already used as S6 P0
→ do not cite again in S6 P1
```

Important correction:

```text
NEXT-EVAL was missing from the first S6 P1 synthesis.
It is now included as the extraction-evaluation paper.
```

Infogent note:

```text
2024-10 Infogent and 2025-05 INFOGEN refer to the same paper/version line.
Use the final citation: Infogent, Findings of NAACL 2025.
```

---

## 3. Main S6 P1 taxonomy

| Cluster | Papers | Main idea |
|---|---|---|
| Interactive structured extraction anchor | WebLists/BardeenAgent | S6 P0 anchor; interactive schema-bound extraction from live websites |
| Extraction evaluation / record extraction benchmark | NEXT-EVAL | DOM-grounded, XPath-based, structure-aware evaluation for traditional and LLM web data record extraction |
| Reusable scraper/script generation | AutoScraper, SCRIBES | Generate reusable extraction programs/scripts instead of extracting each page with an LLM |
| Web information aggregation | Infogent | Extract and synthesize information across multiple sources |
| HTML/content extraction infrastructure | ReaderLM-v2, IndexLM | Clean, compress, and transform long messy HTML into Markdown/JSON or relevant content blocks |
| Schema/ontology/HITL extraction | STRUCTSENSE, ScrapeGraphAI-100k | Improve structured extraction with ontologies, schemas, validation, datasets, and human feedback |
| Practical scraping benchmark | Beyond BeautifulSoup | Compare LLM-assisted scripting and end-to-end agents under realistic site complexity |
| Background and ethics | Systematic Review of Web Scraping | Connect LLM scraping to classical techniques, metrics, and legal/ethical issues |

---

## 4. Core narrative

The S6 P1 narrative should be:

```text
LLM-based web extraction is moving from direct per-page generation
toward reusable extraction programs, specialized extraction models,
schema-constrained datasets, structure-aware evaluation,
process validation, and practical deployment analysis.
```

This is a major shift.

Earlier approaches often used:

```text
HTML page + prompt → LLM output
```

S6 P1 shows newer approaches using:

```text
HTML page + task → reusable scraper/script
MHTML snapshot + XPath labels → structure-aware evaluation
HTML page + query → relevant index intervals
HTML page + instruction → Markdown/JSON
multi-source query → Navigator + Extractor + Aggregator
schema + content → validated JSON
website group → reusable script trained by RL
```

---

## 5. Paper cluster synthesis

## 5.1 NEXT-EVAL: extraction evaluation and DOM-grounded record extraction

**NEXT-EVAL** fills an important gap that was missing from the first S6 P1 synthesis: evaluation.

Its core idea is:

```text
web extraction should be evaluated with DOM-grounded,
structure-aware metrics rather than only text-output matching.
```

NEXT-EVAL builds evaluation datasets from:

```text
MHTML snapshots
XPath-based labels
DOM-preserving preprocessing
structure-aware metrics
```

This is highly relevant to S6 because extraction systems often output plausible text or records that may not be grounded in the correct webpage element.

The paper compares different input formats:

```text
Slimmed HTML
Hierarchical JSON
Flat JSON
```

The headline result is:

```text
Flat JSON input achieves F1 = 0.9567
```

The key lesson for the thesis is:

```text
web data extraction evaluation must preserve source structure.
```

NEXT-EVAL complements WebLists:

```text
WebLists = task benchmark for interactive schema-bound extraction
NEXT-EVAL = evaluation framework for DOM-grounded record extraction
```

Its limitation is that it does not fully solve interactive navigation, pagination, filtering, live-web drift, source provenance across multiple pages, or semantic verification of extracted values.

---

## 5.2 AutoScraper and SCRIBES: reusable extraction programs

**AutoScraper** and **SCRIBES** are central because they avoid repeated LLM extraction.

Their shared idea is:

```text
use the LLM to produce extraction logic,
then run that logic repeatedly and cheaply.
```

AutoScraper does this through progressive understanding and scraper synthesis. SCRIBES does this through RL-trained script generation across structurally similar pages.

This cluster connects strongly to WebLists/BardeenAgent.

The core thesis lesson is:

```text
scalable extraction needs executable/reusable logic,
not only one-shot LLM answers.
```

NEXT-EVAL strengthens this cluster because reusable scrapers and scripts need evaluation protocols that check whether extracted records correspond to correct DOM locations, not just whether generated text looks plausible.

---

## 5.3 Infogent: extraction as multi-source aggregation

**Infogent** shifts S6 from page-level extraction to multi-source aggregation.

It decomposes the task into:

```text
Navigator
Extractor
Aggregator
```

This matters because many real extraction tasks require several sources, not one webpage.

For the thesis, Infogent supports the claim that generalized web extraction may require:

```text
backtracking
source selection
coverage monitoring
evidence aggregation
final synthesis
```

Its limitation is that it focuses more on aggregation and final answer quality than complete schema-bound row-level extraction.

---

## 5.4 ReaderLM-v2 and IndexLM: extraction infrastructure

**ReaderLM-v2** and **IndexLM** are not full web agents, but they are crucial infrastructure.

ReaderLM-v2 converts messy HTML into clean Markdown or JSON.

IndexLM extracts relevant indexed HTML blocks instead of generating content token by token.

Together, they address a key practical problem:

```text
webpages are too long, noisy, and low-signal for direct LLM use.
```

The thesis should use them to argue that web extraction agents need a preprocessing and context-management layer.

NEXT-EVAL connects directly here because it shows that representation format matters: Flat JSON can strongly improve extraction performance.

---

## 5.5 STRUCTSENSE and ScrapeGraphAI-100k: schema and validation

**STRUCTSENSE** introduces agentic structured extraction with:

```text
Extractor Agent
Alignment Agent
Judge Agent
Feedback Agent
ontology database
memory
human feedback
```

**ScrapeGraphAI-100k** provides a large real-world dataset of prompt + content + schema + LLM response + validation metadata.

Together, they expose a central S6 issue:

```text
schema validity is not the same as semantic correctness.
```

A model can produce valid JSON while extracting wrong values. This is one of the most important thesis gaps.

NEXT-EVAL adds another angle:

```text
even if output text looks correct, evaluation should check whether the extraction is grounded in the correct DOM/XPath location.
```

So S6 needs both:

```text
schema validation
+ DOM/source grounding
+ semantic value verification
```

---

## 5.6 Beyond BeautifulSoup and the systematic review: practical and ethical framing

**Beyond BeautifulSoup** shows that LLM-powered scraping changes who can scrape the web. It compares LLM-assisted scripting with end-to-end agents across five website complexity tiers.

The **Systematic Review of Web Scraping** gives the broader foundation: classical techniques, tools, metrics, LLM-enhanced approaches, legal and ethical issues.

Together, they connect S6 to deployment:

```text
web extraction is technical, practical, legal, and ethical.
```

This is important because extraction systems must be evaluated not only by technical success, but also by compliance, safety, user effort, cost, and possible misuse.

---

## 6. Refined S6 gap after P1

After adding NEXT-EVAL, the central gap becomes sharper:

```text
Current systems solve parts of LLM-based web extraction,
but no system jointly solves:
interactive navigation
+ robust HTML/DOM understanding
+ reusable extraction programs
+ DOM-grounded evaluation
+ schema-constrained output
+ field-level correctness
+ source provenance
+ semantic validation
+ multi-source aggregation
+ dynamic website robustness
+ cost-efficient deployment
+ legal/ethical compliance.
```

This is the thesis opportunity.

---

## 7. Extraction-specific reliability gap

The extraction-specific gap should be stated explicitly:

```text
Current systems can often extract plausible structured outputs,
but they do not consistently prove that each extracted field is:
1. present on the source page,
2. attached to the correct record,
3. mapped to the correct schema field,
4. semantically correct,
5. complete across pagination or multiple pages,
6. robust to DOM/layout changes,
7. safe and compliant to extract.
```

NEXT-EVAL helps with item 1 and part of item 2 through DOM/XPath-grounded evaluation.

WebLists helps with interactive schema-bound extraction.

AutoScraper and SCRIBES help with reusable extraction logic.

ReaderLM-v2 and IndexLM help with input representation and content selection.

ScrapeGraphAI-100k helps with schema-constrained training and failure analysis.

STRUCTSENSE helps with ontology and human validation.

But the full stack is still missing.

---

## 8. Cross-links to later sections

| Paper / cluster | Feeds |
|---|---|
| WebLists/BardeenAgent | S6 P0 anchor; executable interactive structured extraction |
| NEXT-EVAL | S6 evaluation; S7 provenance/verification; S5.1 benchmark design |
| AutoScraper | S8 cost-efficient automation; S6 executable extraction |
| Infogent | S6 aggregation; S7 verification; S5.7 deep research |
| ReaderLM-v2 | S5.2 representation; S6 preprocessing; RAG grounding |
| STRUCTSENSE | S7 verification; ontology alignment; HITL |
| Systematic Review | S8 legal/ethical issues; S6.1 classical foundations |
| SCRIBES | S5.4 RL; S6 reusable script extraction; S8 web-scale deployment |
| IndexLM | S5.2 context compression; S6 query-relevant extraction |
| Beyond BeautifulSoup | S8 deployment, usability, abuse/anti-bot implications |
| ScrapeGraphAI-100k | S5.4 fine-tuning; S6 schema benchmarking; S7 failure analysis |

---

## 9. Thesis-ready synthesis paragraph

The S6 P1 literature expands the WebLists/BardeenAgent extraction problem into a broader stack for LLM-based web information extraction. NEXT-EVAL adds an essential evaluation layer by showing that web data record extraction should be assessed with DOM-grounded, XPath-based, and structure-aware metrics rather than only text-output matching; its finding that Flat JSON reaches 0.9567 F1 highlights the importance of representation choice for LLM-based extraction. AutoScraper and SCRIBES show that scalable extraction should not rely on repeated per-page LLM inference; instead, LLMs can generate reusable scrapers or scripts that exploit repeated website structure. Infogent broadens extraction from single-page extraction to multi-source web information aggregation through a Navigator–Extractor–Aggregator architecture. ReaderLM-v2 and IndexLM address the input bottleneck by converting noisy HTML into clean Markdown/JSON or by selecting relevant indexed HTML blocks for downstream RAG and agent reasoning. STRUCTSENSE adds ontology grounding, judge agents, and human-in-the-loop feedback for structured extraction, while ScrapeGraphAI-100k contributes a large real-world dataset for schema-constrained LLM extraction and exposes how schema complexity drives failure. Beyond BeautifulSoup evaluates the practical accessibility of LLM-powered scraping for everyday users across static, authenticated, and CAPTCHA-protected websites, while the systematic web scraping review connects these LLM methods to classical scraping techniques, performance metrics, and legal-ethical concerns. Together, these papers show that LLM-based web extraction is evolving from direct generation into a multi-layered system involving executable extraction logic, content cleaning, schema validation, DOM-grounded evaluation, source aggregation, fine-tuning data, and deployment constraints. The remaining thesis gap is to unify these components into a robust extraction agent that can navigate dynamic websites, extract schema-bound data, preserve provenance, verify field-level correctness, and operate safely and efficiently at scale.

---

## 10. Final S6 P1 conclusion

The final conclusion is:

```text
S6 P1 shows that the future of web extraction is hybrid:
LLM reasoning + classical scraping logic + executable scripts
+ DOM-grounded evaluation + schema-constrained validation
+ efficient content selection + human/source-grounded verification.
```

This should lead naturally into the next section:

```text
S7 should focus on verification, provenance, correctness, and trust.
```


---

### D:\PhD\myArticlesAndPapers\Literature-review4\markdowns\S6\writing\S6_P1_full_refined_synthesis_UPDATED_with_NEXT_EVAL.md

# S6 P1 Refined Synthesis — LLM-Based Web Information Extraction and Aggregation

## Updated version including NEXT-EVAL

## 1. What S6 P1 adds after S6 P0

S6 P0 was anchored by **WebLists/BardeenAgent**, which established the central thesis problem:

```text
interactive schema-bound structured web data extraction
```

S6 P1 expands this into a full research landscape.

The new picture is:

```text
Web extraction is not a single model call.
It is a pipeline:
access → clean → select → extract → structure → validate → replay → aggregate → evaluate → deploy.
```

The S6 P1 papers cover different parts of this pipeline.

---

## 2. Corrected corpus status

The corrected S6 P1 status is:

```text
11 uploaded/listed S6 P1 files
10 unique S6 P1 citation papers
1 duplicate/moved paper archived
```

Important cleanup:

```text
BardeenAgent / WebLists
→ already used as S6 P0
→ do not cite again in S6 P1
```

Important correction:

```text
NEXT-EVAL was missing from the first S6 P1 synthesis.
It is now included as the extraction-evaluation paper.
```

Infogent note:

```text
2024-10 Infogent and 2025-05 INFOGEN refer to the same paper/version line.
Use the final citation: Infogent, Findings of NAACL 2025.
```

---

## 3. Main S6 P1 taxonomy

| Cluster | Papers | Main idea |
|---|---|---|
| Interactive structured extraction anchor | WebLists/BardeenAgent | S6 P0 anchor; interactive schema-bound extraction from live websites |
| Extraction evaluation / record extraction benchmark | NEXT-EVAL | DOM-grounded, XPath-based, structure-aware evaluation for traditional and LLM web data record extraction |
| Reusable scraper/script generation | AutoScraper, SCRIBES | Generate reusable extraction programs/scripts instead of extracting each page with an LLM |
| Web information aggregation | Infogent | Extract and synthesize information across multiple sources |
| HTML/content extraction infrastructure | ReaderLM-v2, IndexLM | Clean, compress, and transform long messy HTML into Markdown/JSON or relevant content blocks |
| Schema/ontology/HITL extraction | STRUCTSENSE, ScrapeGraphAI-100k | Improve structured extraction with ontologies, schemas, validation, datasets, and human feedback |
| Practical scraping benchmark | Beyond BeautifulSoup | Compare LLM-assisted scripting and end-to-end agents under realistic site complexity |
| Background and ethics | Systematic Review of Web Scraping | Connect LLM scraping to classical techniques, metrics, and legal/ethical issues |

---

## 4. Core narrative

The S6 P1 narrative should be:

```text
LLM-based web extraction is moving from direct per-page generation
toward reusable extraction programs, specialized extraction models,
schema-constrained datasets, structure-aware evaluation,
process validation, and practical deployment analysis.
```

This is a major shift.

Earlier approaches often used:

```text
HTML page + prompt → LLM output
```

S6 P1 shows newer approaches using:

```text
HTML page + task → reusable scraper/script
MHTML snapshot + XPath labels → structure-aware evaluation
HTML page + query → relevant index intervals
HTML page + instruction → Markdown/JSON
multi-source query → Navigator + Extractor + Aggregator
schema + content → validated JSON
website group → reusable script trained by RL
```

---

## 5. Paper cluster synthesis

## 5.1 NEXT-EVAL: extraction evaluation and DOM-grounded record extraction

**NEXT-EVAL** fills an important gap that was missing from the first S6 P1 synthesis: evaluation.

Its core idea is:

```text
web extraction should be evaluated with DOM-grounded,
structure-aware metrics rather than only text-output matching.
```

NEXT-EVAL builds evaluation datasets from:

```text
MHTML snapshots
XPath-based labels
DOM-preserving preprocessing
structure-aware metrics
```

This is highly relevant to S6 because extraction systems often output plausible text or records that may not be grounded in the correct webpage element.

The paper compares different input formats:

```text
Slimmed HTML
Hierarchical JSON
Flat JSON
```

The headline result is:

```text
Flat JSON input achieves F1 = 0.9567
```

The key lesson for the thesis is:

```text
web data extraction evaluation must preserve source structure.
```

NEXT-EVAL complements WebLists:

```text
WebLists = task benchmark for interactive schema-bound extraction
NEXT-EVAL = evaluation framework for DOM-grounded record extraction
```

Its limitation is that it does not fully solve interactive navigation, pagination, filtering, live-web drift, source provenance across multiple pages, or semantic verification of extracted values.

---

## 5.2 AutoScraper and SCRIBES: reusable extraction programs

**AutoScraper** and **SCRIBES** are central because they avoid repeated LLM extraction.

Their shared idea is:

```text
use the LLM to produce extraction logic,
then run that logic repeatedly and cheaply.
```

AutoScraper does this through progressive understanding and scraper synthesis. SCRIBES does this through RL-trained script generation across structurally similar pages.

This cluster connects strongly to WebLists/BardeenAgent.

The core thesis lesson is:

```text
scalable extraction needs executable/reusable logic,
not only one-shot LLM answers.
```

NEXT-EVAL strengthens this cluster because reusable scrapers and scripts need evaluation protocols that check whether extracted records correspond to correct DOM locations, not just whether generated text looks plausible.

---

## 5.3 Infogent: extraction as multi-source aggregation

**Infogent** shifts S6 from page-level extraction to multi-source aggregation.

It decomposes the task into:

```text
Navigator
Extractor
Aggregator
```

This matters because many real extraction tasks require several sources, not one webpage.

For the thesis, Infogent supports the claim that generalized web extraction may require:

```text
backtracking
source selection
coverage monitoring
evidence aggregation
final synthesis
```

Its limitation is that it focuses more on aggregation and final answer quality than complete schema-bound row-level extraction.

---

## 5.4 ReaderLM-v2 and IndexLM: extraction infrastructure

**ReaderLM-v2** and **IndexLM** are not full web agents, but they are crucial infrastructure.

ReaderLM-v2 converts messy HTML into clean Markdown or JSON.

IndexLM extracts relevant indexed HTML blocks instead of generating content token by token.

Together, they address a key practical problem:

```text
webpages are too long, noisy, and low-signal for direct LLM use.
```

The thesis should use them to argue that web extraction agents need a preprocessing and context-management layer.

NEXT-EVAL connects directly here because it shows that representation format matters: Flat JSON can strongly improve extraction performance.

---

## 5.5 STRUCTSENSE and ScrapeGraphAI-100k: schema and validation

**STRUCTSENSE** introduces agentic structured extraction with:

```text
Extractor Agent
Alignment Agent
Judge Agent
Feedback Agent
ontology database
memory
human feedback
```

**ScrapeGraphAI-100k** provides a large real-world dataset of prompt + content + schema + LLM response + validation metadata.

Together, they expose a central S6 issue:

```text
schema validity is not the same as semantic correctness.
```

A model can produce valid JSON while extracting wrong values. This is one of the most important thesis gaps.

NEXT-EVAL adds another angle:

```text
even if output text looks correct, evaluation should check whether the extraction is grounded in the correct DOM/XPath location.
```

So S6 needs both:

```text
schema validation
+ DOM/source grounding
+ semantic value verification
```

---

## 5.6 Beyond BeautifulSoup and the systematic review: practical and ethical framing

**Beyond BeautifulSoup** shows that LLM-powered scraping changes who can scrape the web. It compares LLM-assisted scripting with end-to-end agents across five website complexity tiers.

The **Systematic Review of Web Scraping** gives the broader foundation: classical techniques, tools, metrics, LLM-enhanced approaches, legal and ethical issues.

Together, they connect S6 to deployment:

```text
web extraction is technical, practical, legal, and ethical.
```

This is important because extraction systems must be evaluated not only by technical success, but also by compliance, safety, user effort, cost, and possible misuse.

---

## 6. Refined S6 gap after P1

After adding NEXT-EVAL, the central gap becomes sharper:

```text
Current systems solve parts of LLM-based web extraction,
but no system jointly solves:
interactive navigation
+ robust HTML/DOM understanding
+ reusable extraction programs
+ DOM-grounded evaluation
+ schema-constrained output
+ field-level correctness
+ source provenance
+ semantic validation
+ multi-source aggregation
+ dynamic website robustness
+ cost-efficient deployment
+ legal/ethical compliance.
```

This is the thesis opportunity.

---

## 7. Extraction-specific reliability gap

The extraction-specific gap should be stated explicitly:

```text
Current systems can often extract plausible structured outputs,
but they do not consistently prove that each extracted field is:
1. present on the source page,
2. attached to the correct record,
3. mapped to the correct schema field,
4. semantically correct,
5. complete across pagination or multiple pages,
6. robust to DOM/layout changes,
7. safe and compliant to extract.
```

NEXT-EVAL helps with item 1 and part of item 2 through DOM/XPath-grounded evaluation.

WebLists helps with interactive schema-bound extraction.

AutoScraper and SCRIBES help with reusable extraction logic.

ReaderLM-v2 and IndexLM help with input representation and content selection.

ScrapeGraphAI-100k helps with schema-constrained training and failure analysis.

STRUCTSENSE helps with ontology and human validation.

But the full stack is still missing.

---

## 8. Cross-links to later sections

| Paper / cluster | Feeds |
|---|---|
| WebLists/BardeenAgent | S6 P0 anchor; executable interactive structured extraction |
| NEXT-EVAL | S6 evaluation; S7 provenance/verification; S5.1 benchmark design |
| AutoScraper | S8 cost-efficient automation; S6 executable extraction |
| Infogent | S6 aggregation; S7 verification; S5.7 deep research |
| ReaderLM-v2 | S5.2 representation; S6 preprocessing; RAG grounding |
| STRUCTSENSE | S7 verification; ontology alignment; HITL |
| Systematic Review | S8 legal/ethical issues; S6.1 classical foundations |
| SCRIBES | S5.4 RL; S6 reusable script extraction; S8 web-scale deployment |
| IndexLM | S5.2 context compression; S6 query-relevant extraction |
| Beyond BeautifulSoup | S8 deployment, usability, abuse/anti-bot implications |
| ScrapeGraphAI-100k | S5.4 fine-tuning; S6 schema benchmarking; S7 failure analysis |

---

## 9. Thesis-ready synthesis paragraph

The S6 P1 literature expands the WebLists/BardeenAgent extraction problem into a broader stack for LLM-based web information extraction. NEXT-EVAL adds an essential evaluation layer by showing that web data record extraction should be assessed with DOM-grounded, XPath-based, and structure-aware metrics rather than only text-output matching; its finding that Flat JSON reaches 0.9567 F1 highlights the importance of representation choice for LLM-based extraction. AutoScraper and SCRIBES show that scalable extraction should not rely on repeated per-page LLM inference; instead, LLMs can generate reusable scrapers or scripts that exploit repeated website structure. Infogent broadens extraction from single-page extraction to multi-source web information aggregation through a Navigator–Extractor–Aggregator architecture. ReaderLM-v2 and IndexLM address the input bottleneck by converting noisy HTML into clean Markdown/JSON or by selecting relevant indexed HTML blocks for downstream RAG and agent reasoning. STRUCTSENSE adds ontology grounding, judge agents, and human-in-the-loop feedback for structured extraction, while ScrapeGraphAI-100k contributes a large real-world dataset for schema-constrained LLM extraction and exposes how schema complexity drives failure. Beyond BeautifulSoup evaluates the practical accessibility of LLM-powered scraping for everyday users across static, authenticated, and CAPTCHA-protected websites, while the systematic web scraping review connects these LLM methods to classical scraping techniques, performance metrics, and legal-ethical concerns. Together, these papers show that LLM-based web extraction is evolving from direct generation into a multi-layered system involving executable extraction logic, content cleaning, schema validation, DOM-grounded evaluation, source aggregation, fine-tuning data, and deployment constraints. The remaining thesis gap is to unify these components into a robust extraction agent that can navigate dynamic websites, extract schema-bound data, preserve provenance, verify field-level correctness, and operate safely and efficiently at scale.

---

## 10. Final S6 P1 conclusion

The final conclusion is:

```text
S6 P1 shows that the future of web extraction is hybrid:
LLM reasoning + classical scraping logic + executable scripts
+ DOM-grounded evaluation + schema-constrained validation
+ efficient content selection + human/source-grounded verification.
```

This should lead naturally into the next section:

```text
S7 should focus on verification, provenance, correctness, and trust.
```


---


Total files merged: 33
