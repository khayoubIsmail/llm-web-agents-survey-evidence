# S6 P3 Deep Notes — Web Data Extraction, Data Preparation, Data Analysis, and Agentic Information Updating

**Thesis topic:** LLM-based agents for generalized web automation and data extraction  
**Section:** S6 — Web Data Extraction  
**Priority:** P3 supporting / contextual / systems / grey-literature-adjacent papers  
**Batch size:** 9 papers  
**Purpose of this file:** preserve deep notes for later selective integration into the PhD literature review, ACM Computing Surveys version, and shorter 6–8 page conference papers.

---

## 0. High-level S6 P3 synthesis

The S6 P3 batch is not only about classical “web scraping.” It extends the S6 narrative from **extracting data from webpages** toward a broader pipeline of **web-to-data-to-knowledge workflows**:

1. **Interaction with existing webpages**: Reagent shows an early form of turning ordinary structured webpages into interactive agents without manually instrumenting each webpage.
2. **Natural-language data analysis agents**: DataAgent, GeoAgent, DataLab, and AutoPrep show how LLMs can transform natural-language analytical intent into code, workflows, or table transformations.
3. **Data preparation and cleaning as a prerequisite for extraction**: AutoDCWorkflow and AutoPrep are especially important because extracted web data is rarely analysis-ready; it often needs normalization, column derivation, filtering, deduplication, and purpose-aware cleaning.
4. **Agentic search and continuous updating**: Towards AI Search Paradigm and WINELL move beyond one-shot extraction toward iterative web information seeking, evidence aggregation, synthesis, and knowledge-base updating.
5. **Tooling and implementation reality**: The web-crawling prompt-engineering paper is weak as a research contribution, but useful as grey-literature support for the practical stack around BeautifulSoup, Selenium, anti-scraping workarounds, and LLM-generated crawling code.

### Main critique for your thesis

These P3 papers make S6 richer, but they also reveal a strong gap for your thesis:

> Existing LLM-based data agents increasingly automate analysis, preparation, and search, but they rarely solve the full generalized web extraction problem: robust navigation across heterogeneous websites, schema-guided extraction, provenance preservation, source verification, dynamic-content handling, and reproducible evaluation under real web conditions.

This is exactly where your thesis can position itself: not simply as “LLM for scraping,” but as **LLM-based agentic extraction that connects web interaction, structured extraction, cleaning, verification, and repeatable automation**.

---

## 1. Venue / status verification summary

| # | Paper | Status to use | Citation strength | Notes |
|---|---|---|---|---|
| 1 | Reagent: Converting Ordinary Webpages into Interactive Software Agents | IJCAI 2019 Demo / conference paper | Medium | Strong historical system precedent, but not modern LLM-agent work. |
| 2 | DataAgent: Evaluating LLMs’ Ability to Answer Zero-Shot Natural Language Queries | IEEE ICAIC 2024 + arXiv | Medium | Small/early paper; useful as example of zero-shot data analysis via LLM-generated plans/code. |
| 3 | An LLM Agent for Automatic Geospatial Data Analysis / GeoAgent | arXiv 2024; later version appears as ECML-PKDD 2025 under related/revised title | Medium-High after final title check | Important domain-specific data-analysis agent; verify final title before BibTeX freeze. |
| 4 | AutoDCWorkflow | Findings of EMNLP 2025 | High | Strong for purpose-driven data cleaning workflows and evaluation metrics. |
| 5 | DataLab | IEEE ICDE 2025 | High | Strong for unified BI, multi-agent workflow, notebook context management, and enterprise data analysis. |
| 6 | The Synergy of Automated Pipelines with Prompt Engineering and Generative AI in Web Crawling | arXiv 2025 only | Low | Use as grey literature / practical example only, not core evidence. |
| 7 | AutoPrep | PVLDB 18(10), 2025 / VLDB 2025 | High | Very relevant to question-aware table preparation and TQA. |
| 8 | Towards AI Search Paradigm | arXiv 2025 blueprint | Medium-Low | Useful for framing agentic search architecture; cite cautiously as industry/preprint blueprint. |
| 9 | WINELL | ACM Web Conference / WWW 2026 + arXiv | High | Strong for continuous web information aggregation and Wikipedia updating. |

---

## 2. Recommended use in final S6

| Use level | Papers |
|---|---|
| Strongly include in S6 | AutoPrep, AutoDCWorkflow, DataLab, WINELL |
| Include as supporting system examples | Reagent, GeoAgent, DataAgent |
| Use briefly / grey-literature caution | Towards AI Search Paradigm, Web Crawling prompt-engineering paper |
| Good for ACM survey tables | All 9, but separate peer-reviewed papers from arXiv/grey-literature examples |

---

## 3. Where these papers fit inside S6

Suggested S6 substructure after adding these P3 papers:

```text
S6 Web Data Extraction and Web-to-Data Pipelines
  S6.1 Classical web data extraction: wrappers, DOM parsing, tables, semi-structured data
  S6.2 LLM-assisted web crawling and scraping code generation
  S6.3 Agentic extraction from structured and semi-structured webpages
  S6.4 Table-centric extraction, preparation, and question-aware transformation
  S6.5 Data cleaning, workflow generation, and provenance-preserving preparation
  S6.6 Domain-specific data agents: BI, geospatial, scientific/enterprise data
  S6.7 Agentic search, continuous updating, and knowledge-base maintenance
  S6.8 Gaps: generalization, source verification, schema control, reproducibility, and safety
```

---

# 4. Deep paper notes

---

# 4.1 Reagent: Converting Ordinary Webpages into Interactive Software Agents

## Venue / Status

- **Uploaded file:** `2018-12 - Reagent- Converting Ordinary Webpages into Interactive Software Agents.pdf`
- **Verified status:** IJCAI 2019 demo / conference paper.
- **Citation strength:** Medium.
- **Citation caution:** This is not an LLM-agent paper. It predates the current LLM-agent wave and should be used as historical context for interactive webpage-to-agent systems.

## Core idea

Reagent proposes a system that converts ordinary webpages containing structured data into interactive software agents. Instead of requiring webpages to be specially instrumented, it automatically parses webpage structure, captures semantically meaningful mouse events, combines them with speech/text commands, and executes user requests such as filtering, sorting, extracting, visualizing, or analyzing data.

## Key contribution

The paper contributes an early interactive-agent perspective on webpages: a webpage can become an executable interface for data manipulation. This is important for S6 because it shows that the idea of turning existing webpages into interactive agents did not begin with LLMs. Earlier systems already tried to bridge webpage content, user intent, semantic event capture, and data operations.

## Method / approach

Reagent is built on Electron. When a webpage loads, Reagent injects code into the webview, detects major HTML structures such as tables or plots, assigns identifiers to elements, binds event listeners, and monitors DOM mutations to keep instrumentation synchronized. User speech is transcribed, and an intent/parser module combines linguistic commands with recent pointing events to generate JSON-like executable commands. If terminology is ambiguous, Reagent asks the user for clarification and stores the mapping in a dictionary.

## Key findings / evidence

The demonstration uses football statistics webpages. The system can interpret requests such as showing rows where a statistic exceeds a threshold, using either explicit speech (“appearances greater than 35”) or deictic references (“this column greater than this”) combined with pointing.

## Limitations

- The system assumes structured webpage regions such as tables or plots.
- It is not designed for arbitrary web navigation, dynamic multi-page tasks, or extraction from highly heterogeneous sites.
- It depends on event instrumentation and intent parsing rather than general LLM reasoning.
- It does not provide modern notions of provenance, schema-guided extraction, or benchmarked generalization.

## Relevance to my thesis

Reagent gives historical grounding for the idea that webpages can be treated as interactive, agent-operable data surfaces. For your thesis, it can be used to argue that generalized web extraction has long required more than HTML parsing: it needs semantic grounding, user-intent interpretation, interactive disambiguation, and robust mapping between page elements and human concepts.

## How to use it in the literature review

Use this paper in S6.1 or S6.3 as an early precedent for interactive webpage agents. It should not be a central modern benchmark paper, but it can strengthen the historical bridge between classical web automation and modern LLM-based web agents.

## Connects to

- S4 Web agents foundations
- S5.2 Web perception and representation
- S6 Web data extraction
- S8 Open challenges: human-in-the-loop disambiguation and semantic grounding

## Sentence to add later

> Earlier systems such as Reagent already framed structured webpages as interactive data agents by combining semantic DOM instrumentation, pointing events, and natural-language commands, anticipating later LLM-agent work on web interaction while still relying on manually engineered parsing and intent modules.

---

# 4.2 DataAgent: Evaluating Large Language Models’ Ability to Answer Zero-Shot Natural Language Queries

## Venue / Status

- **Uploaded file:** `2024-03-DataAgent Evaluating Large Language Models Ability to Answer Zero-Shot Natural Language Queries.pdf`
- **Verified status:** IEEE ICAIC 2024; also available as arXiv 2024.
- **Citation strength:** Medium.
- **Citation caution:** The paper is short and early; use as a supporting example of LLM-based data analysis agents, not as a definitive benchmark.

## Core idea

DataAgent evaluates whether an LLM can act as a “Language Data Scientist” that answers natural-language questions over datasets in a zero-shot setting. The system uses natural-language query understanding, dataset inspection, action-plan generation, and code execution to produce answers.

## Key contribution

The paper contributes an early workflow for natural-language-to-data-analysis automation. It highlights the role of action plans, code generation, and dataset-context gathering as a bridge between user questions and executable data operations.

## Method / approach

The system proceeds in three stages:

1. Gather background information about the dataset using Pandas-style inspection functions such as `head`, `info`, and `describe`.
2. Generate a natural-language action plan using GPT-3.5, with prompting techniques such as Chain-of-Thought and SayCan-style structure.
3. Translate plan steps into executable code and run them through a local executor to compute the answer.

The benchmark uses synthetic tabular datasets with manually created questions and ground-truth answers.

## Key findings / evidence

The paper reports that GPT-3.5 can successfully answer many low-level data-science questions when supported by action planning and code execution. The main claim is that LLMs can reduce repetitive data-analysis work when the task is well-scoped and the dataset is available for programmatic inspection.

## Limitations

- Dataset scale and benchmark realism are limited.
- It focuses on data analysis over available datasets, not extraction from live web sources.
- It does not address page navigation, dynamic DOMs, anti-bot mechanisms, provenance, or source verification.
- Evaluation is narrower than modern agent benchmarks.

## Relevance to my thesis

DataAgent helps connect web extraction to downstream analysis. It shows why extraction alone is insufficient: once data is obtained, users often want to ask natural-language questions and receive computed answers. Your thesis can use it to motivate an end-to-end web extraction pipeline where agents not only scrape but also structure, validate, and analyze extracted data.

## How to use it in the literature review

Use briefly in S6.4 or S6.6 as a supporting example of natural-language data analysis agents. It can help explain the transition from raw extraction toward analysis-ready data workflows.

## Connects to

- S3 Agent architecture: planning + execution
- S5.3 Planning and reasoning
- S6 Data extraction and analysis
- S8 Open challenge: grounding generated code in reliable, source-linked data

## Sentence to add later

> DataAgent illustrates an early natural-language-to-data-analysis workflow in which an LLM gathers dataset context, generates an action plan, and executes code, but it assumes the dataset is already available and therefore does not address the harder problem of robust web-scale data acquisition and provenance-preserving extraction.

---

# 4.3 An LLM Agent for Automatic Geospatial Data Analysis / GeoAgent

## Venue / Status

- **Uploaded file:** `2024-10-An LLM Agent for Automatic Geospatial Data Analysis.pdf`
- **Verified status:** arXiv 2024 version; later version appears to be associated with ECML-PKDD 2025 under a related/revised title, “Automating Geospatial Vision Tasks with a Large Language Model Agent.”
- **Citation strength:** Medium to high after final version verification.
- **Citation caution:** Before final thesis/survey submission, verify the final accepted title and BibTeX because the arXiv title and later venue title may differ.

## Core idea

GeoAgent is an LLM-based agent for geospatial data analysis. It integrates code generation, retrieval-augmented generation over geospatial library documentation, static analysis, a code interpreter, and Monte Carlo Tree Search to improve multi-step geospatial task programming.

## Key contribution

The paper contributes a domain-specific agent architecture for geospatial data analysis and introduces GeoCode, an execution-based benchmark with many single-turn and multi-turn geospatial tasks. Its key value for S6 is that it shows how extraction/data-analysis agents must often handle domain-specific libraries, specialized APIs, and iterative execution feedback.

## Method / approach

GeoAgent includes:

- **Retriever:** retrieves relevant API documentation, tutorials, and solution examples.
- **Code interpreter:** executes generated code and captures runtime feedback.
- **Static analysis:** detects undefined variables, missing APIs, and code-level inconsistencies.
- **MCTS refinement:** explores alternative code candidates and incrementally refines multi-step solutions.
- **Human intervention mode:** supports interaction when automatic refinement fails.

The benchmark includes geospatial tasks involving data acquisition, analysis, and visualization across multiple Python libraries.

## Key findings / evidence

The paper argues that relying only on the LLM’s internal knowledge is insufficient for geospatial task programming. GeoAgent improves function-call accuracy and task-completion performance by grounding code generation in retrieved documentation and execution feedback.

## Limitations

- Domain-specific to geospatial analysis; not directly a general web extraction framework.
- It assumes executable programming environments and library documentation are available.
- It does not solve arbitrary website navigation or extraction from heterogeneous web interfaces.
- MCTS and execution feedback may increase cost and latency.
- RAG quality depends on documentation retrieval quality.

## Relevance to my thesis

GeoAgent is useful because your thesis also needs to move beyond simple prompting. Generalized web data extraction requires external documentation, tool retrieval, execution feedback, and iterative repair. GeoAgent offers a strong architectural analogy: for web extraction, agents may need retrieval over site schemas, APIs, page documentation, prior crawl traces, or extraction examples.

## How to use it in the literature review

Use in S6.6 as a domain-specific data-agent example. It also supports S5.3 planning and S5.4 training/refinement because it uses MCTS and iterative execution feedback.

## Connects to

- S3 agent architecture
- S5.3 planning and search
- S5.4 training/refinement strategies
- S6 domain-specific data agents
- S8 open challenge: cost-efficient iterative repair

## Sentence to add later

> GeoAgent demonstrates that domain-specific data analysis often requires retrieval over external documentation, executable feedback, static analysis, and iterative search, suggesting that generalized web extraction agents similarly need tool-aware and feedback-grounded architectures rather than one-shot prompting.

---

# 4.4 AutoDCWorkflow: LLM-based Data Cleaning Workflow Auto-Generation and Benchmark

## Venue / Status

- **Uploaded file:** `2024-12 - AutoDCWorkflow- LLM-based Data Cleaning Workflow Auto-Generation and Benchmark.pdf`
- **Verified status:** Findings of EMNLP 2025.
- **Citation strength:** High.
- **Citation caution:** Strong paper for data cleaning and workflow generation; not directly a web-navigation paper.

## Core idea

AutoDCWorkflow uses LLM agents to automatically generate purpose-driven data-cleaning workflows. Given a raw table and a data-analysis purpose, it generates a sequence of OpenRefine operations that produce a minimal cleaned table sufficient for the intended analysis.

## Key contribution

The paper contributes both a framework and a benchmark for evaluating generated data-cleaning workflows. It is especially valuable for S6 because web-extracted data often needs downstream cleaning before it becomes useful. The work formalizes cleaning not as generic preprocessing, but as **purpose-driven transformation**.

## Method / approach

The pipeline has three iterative LLM-agent stages:

1. **Select Target Columns:** identify columns relevant to the analysis purpose.
2. **Inspect Column Quality:** assess accuracy, relevance, completeness, and conciseness.
3. **Generate Operations & Arguments:** predict OpenRefine operations and parameters.

The system executes operations through OpenRefine and iterates until target columns satisfy the required quality dimensions. Operations include uppercase conversion, trimming, numeric conversion, date normalization, mass edit, and regex transformation.

## Key findings / evidence

The benchmark includes 142 purposes, 96 tables, and 142 workflows across six data topics. Evaluation covers:

- **Purpose Answer:** can the cleaned table answer the user’s analytical purpose?
- **Column Value:** how close is the generated cleaned table to the ground truth?
- **Workflow Operations:** how close is the generated workflow to human-curated workflows?

The paper reports that tested LLMs improve data quality and that Gemma variants perform strongly in generating useful tables, answers, or human-like workflows.

## Limitations

- Focuses on tabular data cleaning after data acquisition, not live web extraction.
- Uses a limited set of OpenRefine operations.
- Evaluation depends on curated tables and purposes, which may not fully cover messy web data.
- The framework does not address extraction provenance or source-level uncertainty.

## Relevance to my thesis

This paper is highly relevant because generalized web extraction should not end at retrieving data. Extracted web data often contains inconsistent formats, duplicates, noise, and irrelevant columns. AutoDCWorkflow supports your argument that future web extraction agents should integrate extraction with cleaning workflows and evaluate whether extracted data supports a downstream purpose.

## How to use it in the literature review

Use strongly in S6.5. It can support a subsection on **data preparation and cleaning after extraction**.

## Connects to

- S6 Web data extraction
- S6.5 data cleaning and workflow generation
- S8 evaluation gaps: answer-level vs workflow-level evaluation
- Tools section: OpenRefine, Trifacta, Pandas, data-cleaning workflow systems

## Sentence to add later

> AutoDCWorkflow reframes data cleaning as purpose-driven workflow generation, showing that LLM agents can select relevant columns, inspect quality dimensions, and generate executable OpenRefine operations; this is directly relevant to web extraction because extracted data must often be transformed into analysis-ready tables before it can support reliable downstream answers.

---

# 4.5 DataLab: A Unified Platform for LLM-Powered Business Intelligence

## Venue / Status

- **Uploaded file:** `2024-12 - DataLab- A Unified Platform for LLM-Powered Business Intelligence.pdf`
- **Verified status:** IEEE ICDE 2025.
- **Citation strength:** High.
- **Citation caution:** Strong for BI/data-agent systems, but the focus is enterprise analytics rather than open-web extraction.

## Core idea

DataLab is a unified LLM-powered business intelligence platform that integrates multiple BI tasks—data preparation, analysis, and visualization—inside an augmented computational notebook. It combines a one-stop LLM-agent framework with user customization.

## Key contribution

DataLab is valuable for S6 because it demonstrates a mature architecture for LLM-based data work: domain knowledge incorporation, inter-agent communication, cell-based context management, and notebook-based human intervention. It moves beyond single-task agents such as NL2SQL or NL2VIS toward a unified workflow for enterprise data analysis.

## Method / approach

DataLab includes:

- **LLM-based agent framework:** specialized agents for SQL, cleaning, imputation, EDA, insight discovery, ML, chart generation, report generation, and chart QA.
- **Computational notebook interface:** SQL, Python/PySpark, Markdown, and chart cells.
- **Domain knowledge incorporation:** uses schema, script history, data lineage, and metadata to build a knowledge graph/search index.
- **Inter-agent communication:** structured information buffer and finite-state-machine-based information flow.
- **Cell-based context management:** DAG dependencies among notebook cells for context retrieval and pruning.

## Key findings / evidence

The paper reports state-of-the-art performance on multiple BI benchmarks and strong enterprise results from Tencent datasets, including improved accuracy and reduced token cost. The key empirical lesson is that context management and domain knowledge are not optional in realistic data-agent systems.

## Limitations

- Enterprise BI setting differs from the open web.
- The system assumes access to internal data schemas, processing scripts, and lineage metadata.
- It focuses on data analysis and visualization rather than external web navigation and extraction.
- Practical deployment details may be enterprise-specific.

## Relevance to my thesis

DataLab can help you frame the **post-extraction workflow**. Once a web agent extracts data, users need to analyze, clean, visualize, and reuse it. DataLab also supports your argument that robust agentic data systems need structured inter-agent communication and context management, not only a single browser-control agent.

## How to use it in the literature review

Use strongly in S6.6 and in a tools/frameworks ecosystem table. DataLab can be used as an example of unified LLM-powered data systems.

## Connects to

- S3 multi-agent architectures
- S6 data workflows
- S8 open challenges: context management, cost, enterprise deployment, provenance
- Tools: notebooks, SQL/Python cells, BI dashboards, knowledge graphs

## Sentence to add later

> DataLab demonstrates that practical LLM-powered data systems require unified workflows, domain-knowledge incorporation, structured inter-agent communication, and adaptive context management, suggesting that generalized web extraction should be integrated with downstream preparation, analysis, and visualization environments rather than treated as an isolated scraping task.

---

# 4.6 The Synergy of Automated Pipelines with Prompt Engineering and Generative AI in Web Crawling

## Venue / Status

- **Uploaded file:** `2024-12 - The Synergy of Automated Pipelines with Prompt Engineering and Generative AI in Web Crawling.pdf`
- **Verified status:** arXiv 2025 only.
- **Citation strength:** Low.
- **Citation caution:** Treat as grey literature / practical example. Do not rely on it as strong academic evidence.

## Core idea

The paper studies whether generative AI tools such as Claude Sonnet 3.5 and ChatGPT-4.0 can generate web-scraping scripts from prompts. It compares general prompts with element-specific prompts and evaluates generated code using criteria such as functionality, readability, modularity, and robustness.

## Key contribution

The paper’s main value is not theoretical novelty but practical relevance: it reflects how developers increasingly use LLMs to generate BeautifulSoup, requests, Selenium, and anti-scraping code for web crawling tasks.

## Method / approach

The paper compares two prompt styles:

1. **General inference prompt:** asks the model to infer webpage structure.
2. **Element-specific prompt:** provides target HTML elements such as `<h1>` or `<div class="content">`.

The experiments involve Yahoo News and Coupons.com examples. The workflow includes common scraping tools and anti-scraping libraries such as Selenium, undetected_chromedriver, and fake_useragent.

## Key findings / evidence

The paper claims Claude outperformed ChatGPT-4.0 in code structure, robustness, and adaptability, especially for element-specific prompts. It also argues that element-specific prompting is more precise than general inference prompting.

## Limitations

- Very small empirical scope.
- Manual scoring and limited test cases.
- Does not offer a rigorous benchmark.
- Does not address extraction correctness at scale, provenance, site changes, or compliance.
- Overemphasizes code generation without evaluating long-term scraper maintenance.

## Relevance to my thesis

Use this paper only as a supporting example of practical LLM-assisted scraping. It helps show the current “developer workflow” where users ask LLMs to generate ad hoc scrapers. Your thesis can critique this as insufficient for generalized web automation because one-off code generation does not solve generalization, monitoring, schema adaptation, or source verification.

## How to use it in the literature review

Use briefly in S6.2 or in the tools/frameworks table under “LLM-assisted scraping script generation.”

## Connects to

- S6.2 LLM-assisted crawling/scraping code generation
- S7 security/ethics: anti-scraping, compliance, robots.txt, rate limits
- S8 open challenge: maintainability and responsible crawling

## Sentence to add later

> Recent prompt-based scraping examples show that LLMs can generate useful BeautifulSoup or Selenium scripts from natural-language instructions, but these ad hoc workflows remain brittle because they lack rigorous evaluation, provenance guarantees, long-term maintenance, and robust adaptation to dynamic webpages.

---

# 4.7 AutoPrep: Natural Language Question-Aware Data Preparation with a Multi-Agent Framework

## Venue / Status

- **Uploaded file:** `2024-12-AutoPrep Natural Language Question-Aware Data Preparation with a Multi-Agent Framework.pdf`
- **Verified status:** PVLDB 18(10), 2025 / VLDB 2025.
- **Citation strength:** High.
- **Citation caution:** Strong paper for table preparation and TQA; use specifically for question-aware data preparation, not general browser automation.

## Core idea

AutoPrep introduces question-aware data preparation for tabular question answering. Given a natural-language question over a table, it prepares the table through operations such as column derivation, normalization, and filtering so that the question can be answered more accurately.

## Key contribution

The paper identifies that many LLM-based TQA failures come from inadequate table preparation. It contributes a multi-agent architecture with a Planner, Programmer, and Executor, plus a Chain-of-Clauses reasoning mechanism for selecting high-level data-preparation operations.

## Method / approach

AutoPrep separates data preparation into:

1. **Planning stage:** the Planner creates a logical plan of high-level operations.
2. **Programming stage:** Programmer agents translate logical operations into executable Python code.
3. **Execution stage:** the Executor runs the code and sends errors back for debugging.

The main logical operations are:

- **Derive:** create missing semantic columns.
- **Normalize:** standardize or convert values according to the question.
- **Filter:** remove irrelevant columns.

## Key findings / evidence

The paper’s error analysis shows that a large share of LLM-based TQA failures on WikiTQ and TabFact are linked to data-preparation issues such as missing semantics, inconsistent values, and irrelevant columns. Experiments report improvements over prior TQA methods with and without data preparation.

## Limitations

- Focused on tabular QA, not end-to-end web extraction.
- Works after a table is already available.
- Main operations are tailored to TQA benchmark errors; broader real-world web data issues may require more operation types.
- Does not address provenance, live web changes, or extraction uncertainty.

## Relevance to my thesis

AutoPrep is one of the strongest S6 P3 papers for your thesis because generalized web extraction often produces tables that are not directly answerable. This paper gives you language to argue that extraction must be **question-aware** and **purpose-aware**, not merely schema extraction.

## How to use it in the literature review

Use strongly in S6.4 and S6.5. It is also useful for your ACM survey because it gives a clean taxonomy of data-preparation operations: derive, normalize, and filter.

## Connects to

- S6 web tables and tabular QA
- S6 data preparation
- S5.3 planning and reasoning
- S5.5 failure modes: irrelevant columns, missing semantics, inconsistent values
- S8 open challenge: extraction-to-answer alignment

## Sentence to add later

> AutoPrep shows that many table-question-answering errors arise not from reasoning alone but from missing semantics, inconsistent values, and irrelevant columns, motivating question-aware data preparation as a necessary bridge between web-extracted tables and reliable downstream answers.

---

# 4.8 Towards AI Search Paradigm

## Venue / Status

- **Uploaded file:** `2025-06 - Towards AI Search Paradigm.pdf`
- **Verified status:** arXiv 2025 preprint / industry-style blueprint from Baidu Search.
- **Citation strength:** Medium-low.
- **Citation caution:** Useful for conceptual framing of agentic search, but cite cautiously because it is a broad blueprint rather than a conventional peer-reviewed experimental paper.

## Core idea

The paper proposes an AI Search Paradigm: a multi-agent architecture for next-generation search systems. It uses four LLM-powered agents—Master, Planner, Executor, and Writer—to analyze query complexity, decompose tasks, select tools, execute subtasks, and synthesize answers.

## Key contribution

The paper contributes a broad architecture for agentic search. For S6, it is relevant because generalized web extraction increasingly overlaps with search: finding relevant sources, decomposing information needs, selecting tools, executing retrieval/extraction, and synthesizing results.

## Method / approach

The proposed system includes:

- **Master Agent:** evaluates query complexity and selects agent configuration.
- **Planner Agent:** decomposes complex queries into DAG-based subtasks and selects tools from an MCP-like platform.
- **Executor Agent:** invokes tools and evaluates whether subtask output is sufficient.
- **Writer Agent:** synthesizes final answers from subtask results.

The paper discusses dynamic capability boundaries, MCP-style tool abstractions, tool retrieval, DAG planning, robust RAG, user-feedback optimization, multi-agent training, and efficient LLM inference.

## Key findings / evidence

The work presents case studies and discusses deployment-oriented considerations for AI search. The central insight is that search is moving from ranked-document retrieval to agentic task planning and execution.

## Limitations

- Broad blueprint; not a focused benchmark paper.
- Some claims are system-level and difficult to compare directly with academic benchmarks.
- Does not focus specifically on structured data extraction.
- Need caution around MCP/agent architecture claims because terminology and standards are still evolving.

## Relevance to my thesis

This paper is useful for framing your thesis at a higher level. Generalized web data extraction can be described as a specialized form of agentic search where the final output is not only an answer but a structured, schema-conformant, source-linked dataset.

## How to use it in the literature review

Use in S6.7 or S8 as conceptual framing. Do not rely on it as the strongest empirical evidence.

## Connects to

- S3 agent architecture
- S5.1 benchmarks/evaluation
- S5.3 planning
- S6 information extraction and search
- S8 future systems: MCP, dynamic tools, agentic search

## Sentence to add later

> The AI Search Paradigm frames search as a multi-agent process of query analysis, DAG planning, tool execution, and answer synthesis, suggesting that generalized web extraction can be viewed as a structured-output variant of agentic search where evidence must be retrieved, transformed, verified, and preserved with provenance.

---

# 4.9 WINELL: Wikipedia Never-Ending Updating with LLM Agents

## Venue / Status

- **Uploaded file:** `2025-08 - WINELL- Wikipedia Never-Ending Updating with LLM Agents.pdf`
- **Verified status:** ACM Web Conference / WWW 2026; arXiv 2025 version also exists.
- **Citation strength:** High.
- **Citation caution:** Cite the ACM Web Conference version when available. The arXiv version is useful for early access, but the final version should be preferred in formal bibliography.

## Core idea

WINELL is an agentic framework for continuously updating Wikipedia articles. It monitors online sources, identifies relevant factual updates for a target article, aggregates non-redundant information, and generates precise edit suggestions with citations for human review.

## Key contribution

WINELL is highly relevant to S6 because it connects web information extraction with knowledge-base maintenance. Unlike one-shot QA or scraping, it addresses continuous updating, online source monitoring, fact selection, citation-aware editing, and human-in-the-loop review.

## Method / approach

WINELL includes:

1. **Section criteria induction:** analyzes a Wikipedia article’s structure and generates section-specific content criteria.
2. **Agentic update aggregation:** iteratively searches the web, extracts potential updates, and decides whether to add, ignore, or replace information.
3. **Fine-grained editing:** trains editing models on Wikipedia’s historical human edits to incorporate new information into the correct article section.
4. **Automatic historical evaluation:** compares generated updates against factual human edits from a historical interval.

The multi-agent aggregation process uses roles similar to Navigator, Extractor, and Aggregator.

## Key findings / evidence

The paper reports that WINELL’s editor models outperform open-source instruction-following baselines and closed-source LLMs such as GPT-4o in key-information coverage and editing efficiency. The end-to-end evaluation on high-activity Wikipedia pages suggests that the framework can identify timely factual updates.

## Limitations

- Focused on Wikipedia article updating, not arbitrary web data extraction.
- Requires reliable source discovery and historical-edit-based training/evaluation.
- Human review remains necessary for quality and safety.
- Evaluation uses historical human edits as a proxy for ground truth, which may miss valid updates not chosen by human editors.
- Not designed for structured schema extraction from commercial or dynamic websites.

## Relevance to my thesis

WINELL is very useful because your thesis can learn from its continuous, citation-aware, human-in-the-loop design. It shows a mature direction for web extraction agents: not just scrape once, but monitor, detect updates, filter significance, preserve citations, and propose structured changes for review.

## How to use it in the literature review

Use strongly in S6.7 and S8. It also provides a bridge to S7 because Wikipedia updating raises trust, provenance, and human-review issues.

## Connects to

- S6 web information extraction
- S7 safety, provenance, and verification
- S8 open challenges: continuous extraction, update detection, source reliability
- Related concepts: NELL, knowledge-base population, Wikipedia bots, agentic search

## Sentence to add later

> WINELL extends web extraction toward continuous knowledge-base maintenance by combining agentic web search, factual update aggregation, citation-aware editing, and human review, illustrating how future extraction agents may move from one-shot scraping to never-ending, provenance-preserving information updating.

---

# 5. S6 section-level synthesis to insert later

## 5.1 Suggested paragraph: from scraping to agentic data workflows

Recent work suggests that web data extraction is evolving from static scraping scripts toward agentic workflows that combine interaction, planning, code execution, data preparation, and source-aware updating. Earlier systems such as Reagent converted structured webpages into interactive agents through semantic DOM instrumentation and multimodal commands, while newer LLM-based systems automate natural-language data analysis, workflow generation, and domain-specific processing. However, many of these systems assume that data is already available in tabular or database form. This leaves a gap for generalized web extraction agents that can navigate heterogeneous websites, identify relevant sources, extract schema-conformant data, clean and normalize it, and preserve provenance for downstream verification.

## 5.2 Suggested paragraph: data preparation is part of extraction

A recurring lesson from AutoPrep and AutoDCWorkflow is that extraction quality cannot be evaluated only by whether some fields were captured. Extracted data must be fit for a downstream question or analysis purpose. AutoPrep shows that table QA failures often arise from missing semantics, inconsistent values, and irrelevant columns, while AutoDCWorkflow formalizes purpose-driven cleaning as executable workflow generation. These works motivate a broader view of web extraction in which agents must perform not only acquisition but also question-aware transformation, normalization, and cleaning.

## 5.3 Suggested paragraph: continuous extraction and updating

Agentic search and updating systems such as WINELL show that web information extraction can also be continuous. Instead of treating web extraction as a one-shot crawl, WINELL monitors online sources, identifies new factual updates, filters redundancy, and proposes citation-backed edits for human review. This direction is directly relevant to dynamic web data extraction, where sources change over time and agents must detect, validate, and incorporate updates while preserving evidence trails.

---

# 6. Tools and frameworks examples for S6

## Browser automation and crawling

| Category | Examples | Use in S6 |
|---|---|---|
| Browser automation | Selenium, Playwright, Puppeteer | Dynamic webpages, forms, JavaScript-rendered pages, interaction traces. |
| HTML parsing | BeautifulSoup, lxml, Cheerio | Static page parsing, lightweight extraction. |
| Crawling frameworks | Scrapy, Heritrix, Apache Nutch | Large-scale crawling and link traversal. |
| LLM-focused crawling/extraction | Firecrawl, Crawl4AI, Jina Reader, Browser-use-style tools | LLM-ready page extraction and agentic crawling. |
| Anti-bot / browser-control tools | undetected_chromedriver, fake_useragent | Practical but ethically sensitive; discuss under responsible crawling. |
| Cloud browser infrastructure | Browserbase, Steel.dev, Hyperbrowser | Scalable browser sessions for agents. |

## Data preparation and cleaning

| Category | Examples | Use in S6 |
|---|---|---|
| Data cleaning tools | OpenRefine, Trifacta, Pandas | Cleaning and transforming extracted data. |
| Workflow systems | OpenRefine operation histories, data pipelines, notebooks | Reproducible transformation and provenance. |
| Table understanding | Pandas, SQL, DuckDB, Polars | Post-extraction analysis and querying. |
| Data-quality dimensions | accuracy, completeness, relevance, conciseness, consistency | Evaluation of extracted/cleaned data. |

## Agentic data and search frameworks

| Category | Examples | Use in S6 |
|---|---|---|
| Agent frameworks | LangChain, LlamaIndex, AutoGen, CrewAI, OpenAgents | Planning, tool use, orchestration, memory. |
| Tool protocols | MCP, OpenAPI/function calling | Tool discovery and invocation. |
| Retrieval and RAG | vector databases, documentation retrieval, web search APIs | Grounding code generation and evidence collection. |
| Code execution | Python sandbox, Jupyter, notebooks, code interpreters | Executable data analysis and transformation. |
| Observability | OpenTelemetry, LangSmith, AgentOps | Tracking agent trajectories and extraction failures. |

---

# 7. Cross-links to other sections

| S6 P3 idea | Link to section | Why |
|---|---|---|
| Reagent semantic DOM instrumentation | S5.2 | Connects to perception and representation of web elements. |
| DataAgent action-plan generation | S5.3 | Shows planning-to-code execution for data analysis. |
| GeoAgent MCTS + execution feedback | S5.3 / S5.4 | Connects to search-based planning and refinement. |
| AutoDCWorkflow data-cleaning workflows | S6 / S8 | Supports extraction-to-cleaning pipeline and evaluation gaps. |
| DataLab inter-agent communication | S3 / S6 | Shows mature multi-agent architecture for data workflows. |
| Web crawling prompt engineering | S6 / S7 | Practical scraping and responsible crawling issues. |
| AutoPrep question-aware data preparation | S6 / S5.5 | Connects data-prep errors to failure modes. |
| AI Search Paradigm | S3 / S8 | Agentic search and dynamic tool boundaries. |
| WINELL continuous updating | S6 / S7 / S8 | Provenance, citation, continuous extraction, human review. |

---

# 8. Strongest ideas to keep for final thesis / ACM survey

## Must keep

1. **Extraction must be purpose-aware.** AutoPrep and AutoDCWorkflow both support this.
2. **Extraction must include cleaning and transformation.** Raw data is rarely ready for use.
3. **Extraction must preserve provenance.** WINELL strongly supports citation-aware updating.
4. **Extraction needs tool-aware execution.** GeoAgent and DataLab show why code interpreters, RAG, and context management matter.
5. **Open-web extraction is harder than tabular QA or BI.** Many systems assume data already exists in tables/databases.

## Good critique sentence

> The current literature is rich in LLM-based data analysis, cleaning, and agentic search systems, but comparatively weaker on generalized, reproducible, source-verifiable web extraction from heterogeneous live websites.

---

# 9. Final recommendation for S6 P3 integration

For the final thesis chapter, do not insert all nine papers with equal weight. Use them strategically:

- Use **AutoPrep**, **AutoDCWorkflow**, **DataLab**, and **WINELL** as the main S6 P3 support.
- Use **Reagent** as a historical bridge.
- Use **GeoAgent** as a domain-specific data-agent architecture example.
- Use **DataAgent** briefly as early natural-language data-analysis support.
- Use **Towards AI Search Paradigm** to frame future agentic search but label it as preprint/blueprint.
- Use the **Web Crawling prompt-engineering** paper only as a practical/grey-literature example, not as strong academic evidence.

