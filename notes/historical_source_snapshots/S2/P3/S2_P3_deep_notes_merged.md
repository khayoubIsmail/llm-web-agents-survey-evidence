# S2 P3 — Deep Paper Notes + Venue/Status Verification

Project: Literature Review / Survey on LLM-based agents for generalized web automation and data extraction  
Section: S2 — Foundations: LLMs, knowledge, grounding, reasoning, feedback, long context, multimodality  
Priority: P3 supportive/background papers  
Batch status: Complete S2 P3 batch received and processed  
Number of papers/reports: 29

---

## 0. Executive synthesis for S2

The S2 P3 corpus strengthens the foundations section by adding five kinds of support that are useful but not central enough to dominate the main survey narrative.

First, the early LM-as-knowledge-base papers show why relying on model parameters alone is risky for web automation and data extraction. Prompt-based probing, closed-book QA, and LM-as-KB surveys establish that LLMs encode factual knowledge, but that knowledge is prompt-sensitive, incomplete, stale, hard to edit, and difficult to verify. This is directly useful for motivating retrieval, tool use, provenance, and source-grounded extraction.

Second, the grounding and multimodal reasoning papers argue that text-only learning is insufficient for agents that must operate in web or physical environments. Experience Grounds Language, multimodal reasoning surveys, video-as-language, and Visualization-of-Thought all support the claim that web agents require grounded perception, not only linguistic reasoning.

Third, the reasoning papers show a progression from simple Chain-of-Thought to more structured approaches: Selection-Inference, SelfCheck, Chain-of-Verification, RAT, Chain-of-X, Buffer of Thoughts, Thinking LLMs, PRefLexOR, and DeepSeek-R1 Thoughtology. These papers justify discussing reasoning as a design space: decomposition, verification, correction, retrieval-augmented reasoning, thought optimization, and inference-time scaling. They also show that longer thinking is not automatically better and may create cost, rumination, or safety problems.

Fourth, the feedback and alignment papers provide background for why agent models improve through preference optimization, language feedback, simulated feedback, mistake correction, self-refinement, and expert/merged post-training pipelines. This supports later sections on training web agents, learning from trajectories, and human-in-the-loop correction.

Fifth, the long-context and retrieval papers show that web extraction agents should not simply depend on longer context windows. AutoCompressors, Landmark Attention, LC-Boost, FreshLLMs, CoV-RAG, OmniSearch, Command A, and related work show multiple ways to combine retrieval, context compression, dynamic planning, and verification. This is essential for arguing that generalized web extraction requires targeted context access and source verification rather than brute-force page ingestion.

### Best one-sentence addition to S2

Modern LLM foundations increasingly show that parameterized knowledge, long context, and chain-of-thought reasoning are not sufficient on their own: robust web agents require grounded perception, adaptive retrieval, explicit verification, and feedback-driven correction to handle changing web content, ambiguous instructions, and source-verifiable outputs.

---

## 1. Venue/status overview

| # | Paper | Verified status | Citation caution | Best use in S2 |
|---:|---|---|---|---|
| 1 | How Can We Know What Language Models Know? | TACL 2020 | Strong peer-reviewed | LM knowledge probing; prompt sensitivity |
| 2 | How Much Knowledge Can You Pack Into the Parameters of a Language Model? | EMNLP 2020 | Strong peer-reviewed | Closed-book QA; parametric knowledge limits |
| 3 | Experience Grounds Language | EMNLP 2020 | Strong peer-reviewed / position-style | Grounding motivation |
| 4 | A Systematic Evaluation of Large Language Models of Code | DL4C @ ICLR 2022 workshop / arXiv | Workshop; useful but not main evidence | Code LMs and tool/program synthesis foundations |
| 5 | A Review on Language Models as Knowledge Bases | arXiv 2022 | Survey preprint; cite cautiously | LM-as-KB taxonomy |
| 6 | Selection-Inference | ICLR 2023, notable top 5% | Strong peer-reviewed | Modular interpretable reasoning |
| 7 | Training Language Models with Language Feedback at Scale | arXiv 2023/2024 | Preprint; cite cautiously | Language feedback / refinement |
| 8 | Adapting Language Models to Compress Contexts | EMNLP 2023 | Strong peer-reviewed | Context compression |
| 9 | AlpacaFarm | NeurIPS 2023 | Strong peer-reviewed | Feedback simulation and evaluation |
| 10 | Random-Access Infinite Context Length for Transformers | NeurIPS 2023 | Strong peer-reviewed | Long-context architecture |
| 11 | SelfCheck | ICLR 2024 | Strong peer-reviewed | Zero-shot reasoning verification |
| 12 | Chain-of-Verification Reduces Hallucination | Findings of ACL 2024 | Peer-reviewed Findings | Hallucination verification |
| 13 | FreshLLMs | Findings of ACL 2024 | Peer-reviewed Findings | Fresh knowledge + search augmentation |
| 14 | Learning From Mistakes Makes LLM Better Reasoner | arXiv 2023/2024 | Preprint; cite cautiously | Error-correction training |
| 15 | Exploring Reasoning Abilities of MLLMs | arXiv 2024 | Survey preprint | Multimodal reasoning overview |
| 16 | Video as the New Language for Real-World Decision Making | arXiv 2024 | Position preprint | Video/world-model grounding |
| 17 | A Critical Evaluation of AI Feedback | NeurIPS 2024 | Strong peer-reviewed | Limits of RLAIF/AI feedback |
| 18 | RAT: Retrieval Augmented Thoughts | arXiv 2024; workshop evidence only | Preprint/workshop caution | Retrieval-augmented reasoning |
| 19 | Beyond Chain-of-Thought / Chain-of-X Survey | COLING 2025 | Peer-reviewed survey | Taxonomy of CoX paradigms |
| 20 | LM-Guided Chain-of-Thought | LREC-COLING 2024 | Peer-reviewed | Small-model-guided reasoning |
| 21 | Mind's Eye of LLMs / VoT | NeurIPS 2024 | Strong peer-reviewed | Spatial reasoning / visualization |
| 22 | Are Long-LLMs A Necessity? | arXiv 2024 | Preprint; cite cautiously | Short-context solving with adaptive access |
| 23 | Buffer of Thoughts | NeurIPS 2024 | Strong peer-reviewed | Thought templates / memory of reasoning |
| 24 | CoV-RAG | Findings of EMNLP 2024 | Peer-reviewed Findings | Verification-enhanced RAG |
| 25 | Thinking LLMs | ICML 2025 | Strong peer-reviewed | Thought generation for general instruction following |
| 26 | PRefLexOR | npj Artificial Intelligence 2025 | Peer-reviewed journal, domain-specific | Recursive preference-based reasoning |
| 27 | Dyn-VQA / OmniSearch | ICLR 2025 | Strong peer-reviewed | Dynamic multimodal retrieval and planning |
| 28 | Command A | Cohere technical report / arXiv 2025 | Technical report / grey literature | Enterprise RAG, tool use, agents |
| 29 | DeepSeek-R1 Thoughtology | TMLR 2026 | Strong peer-reviewed | LRM reasoning analysis and limits |

---

## 2. Tools, frameworks, datasets, and model/system examples surfaced by this batch

| Type | Examples | How to use in the review |
|---|---|---|
| LM knowledge probing | LAMA, LPAQA | Show prompt sensitivity and lower-bound nature of LM knowledge probing |
| Closed-book QA | T5 closed-book QA | Show limits of parametric-only knowledge |
| Code models | Codex, GPT-J, GPT-Neo, GPT-NeoX, CodeParrot, PolyCoder | Background for code generation and programmatic web automation |
| Feedback/alignment frameworks | ILF, AlpacaFarm, RLAIF, DPO, SRPO, TPO, ORPO, EXO | Foundations for training agents from feedback and preferences |
| Reasoning methods | SI, SelfCheck, CoVe, RAT, CoX, VoT, BoT, PRefLexOR, DeepSeek-R1 thoughts | Foundations for planning, verification, correction, and inference-time reasoning |
| Long-context methods | AutoCompressors, Landmark Attention, LC-Boost | Argue against brute-force long-context processing as the only solution |
| Retrieval/RAG systems | FreshPrompt, CoV-RAG, OmniSearch, Command A RAG/tool pipeline | Support retrieval, grounding, source freshness, and verification |
| Multimodal benchmarks | Dyn-VQA, visual navigation, visual tiling | Support visual grounding and dynamic retrieval for web agents |
| Enterprise agent models | Command A, Command R7B | Grey-literature support for RAG + tool use + enterprise deployment |
| Reasoning model analysis | DeepSeek-R1 Thoughtology | Use to critique long reasoning, rumination, safety, and cost |

---

# 3. Deep notes by paper

---

## 1. How Can We Know What Language Models Know?

### Venue / Status
- Final venue: Transactions of the Association for Computational Linguistics, 2020.
- Status: peer-reviewed journal article.
- Venue verification: ACL Anthology lists it as TACL 2020, volume 8, pages 423–438, DOI 10.1162/tacl_a_00324.
- Citation caution: safe to cite strongly as foundational work on LM knowledge probing and prompt sensitivity.

### Core idea
The paper argues that factual knowledge stored in language models cannot be measured reliably with a single manually written prompt. If a model fails to answer a cloze query, that failure may reflect poor prompt formulation rather than absence of knowledge. The authors therefore develop automatic prompt discovery and prompt ensembling methods to produce a tighter estimate of what language models know.

### Key contribution
The main contribution is LPAQA, a prompt-and-query archive created through mining-based and paraphrasing-based prompt generation. Instead of relying only on manual LAMA prompts, the paper generates multiple relation-specific prompts and combines them through ensemble methods. The key result is that better prompts improve BERT-base accuracy on LAMA from 31.1% to 39.6%, showing that prompt choice substantially affects knowledge retrieval.

### Method / approach
The paper starts from the LAMA benchmark, where relations are queried through cloze-style prompts. It introduces two prompt generation strategies: mining prompts from corpora by observing entity pairs, and paraphrasing existing prompts to increase lexical diversity. It then uses ensemble aggregation over multiple prompts because different templates work better for different subject-object pairs.

### Key findings
The central finding is that manually designed prompts underestimate LM knowledge. Prompt quality changes factual retrieval accuracy significantly, and prompt ensembling gives better performance than relying on a single template. This matters because LM-as-KB evaluation is not equivalent to querying a symbolic KB: the answer is mediated by natural-language access patterns.

### Limitations
The work still evaluates masked LMs under cloze-style relation extraction, which is far simpler than open-ended web data extraction. It measures whether a model can retrieve known relational facts, not whether it can ground answers to live sources, update stale information, or provide provenance. It also remains English-centric and benchmark-specific.

### Relevance to thesis
This paper helps justify a key principle for generalized web extraction: internal model knowledge is prompt-sensitive and cannot be trusted as a complete or auditable source of truth. Web agents must therefore use source-grounded retrieval, explicit extraction, and verification rather than depending on parametric recall.

### How to use it in S2
Use it in a paragraph about LMs as implicit knowledge stores and the limitations of prompt-based knowledge access. It is especially useful before introducing retrieval and source grounding.

### Connects to
- S2: LMs as knowledge bases
- S5.3: reasoning and prompting
- S6: source-verifiable extraction
- S8: benchmark and evaluation gaps

### Sentence to add later
Early LM probing work showed that factual recall is highly prompt-sensitive: Jiang et al. improved LAMA accuracy from 31.1% to 39.6% using automatically generated and ensembled prompts, implying that LM knowledge access is an unreliable lower-bound measurement rather than a deterministic query mechanism.

---

## 2. How Much Knowledge Can You Pack Into the Parameters of a Language Model?

### Venue / Status
- Final venue: EMNLP 2020.
- Status: peer-reviewed conference paper.
- Venue verification: ACL Anthology lists it in Proceedings of EMNLP 2020, pages 5418–5426, DOI 10.18653/v1/2020.emnlp-main.437.
- Citation caution: safe to cite strongly.

### Core idea
This paper investigates whether pretrained language models can answer open-domain questions using only knowledge stored in their parameters. It defines a closed-book QA setting in which the model receives the question but no retrieved documents or external context. The work tests how far parametric memory can go when scaled.

### Key contribution
The paper demonstrates that T5 models can be fine-tuned to perform surprisingly well in closed-book QA, and that performance scales with model size. It is important because it framed language models as possible implicit knowledge stores, while also exposing the core weakness of parametric knowledge: the model has no explicit source access, no update mechanism, and no guarantee of factuality.

### Method / approach
The authors fine-tune T5 models of different sizes on open-domain QA tasks while withholding external evidence. They compare closed-book performance to retrieval-based or open-book QA approaches. The experiment forces the model to answer from memorized knowledge rather than reading a provided passage.

### Key findings
Larger models store and retrieve more factual information. However, closed-book QA remains limited by what was seen during pretraining and fine-tuning. Unlike retrieval-augmented systems, closed-book models cannot dynamically access updated knowledge or cite evidence.

### Limitations
Closed-book QA is fundamentally incompatible with source-verifiable web extraction. It does not address changing web pages, provenance, extraction completeness, or schema adherence. The approach is useful as a baseline for parametric knowledge, but it should not be treated as sufficient for trustworthy agents.

### Relevance to thesis
This paper supports the argument that LLMs have useful background knowledge but cannot be the sole knowledge substrate for web automation. Web extraction agents need to query, inspect, and verify external web sources because web data changes continuously and must be attributable.

### How to use it in S2
Use it to contrast parametric memory with retrieval-grounded and web-grounded systems. It can introduce the difference between closed-book knowledge and open-world web evidence.

### Connects to
- S2: parametric knowledge
- S5.1: evaluation of knowledge freshness
- S6: provenance and extraction reliability
- S7: hallucination and stale knowledge risks

### Sentence to add later
Closed-book QA showed that larger LMs can store substantial factual information in their parameters, but this paradigm remains unsuitable for generalized web extraction because it lacks freshness, provenance, and auditable source grounding.

---

## 3. Experience Grounds Language

### Venue / Status
- Final venue: EMNLP 2020.
- Status: peer-reviewed conference paper; position/synthesis style.
- Venue verification: ACL Anthology lists it in EMNLP 2020, pages 8718–8735.
- Citation caution: safe to cite as conceptual grounding motivation.

### Core idea
The paper argues that language understanding cannot be fully learned from text alone because language depends on shared experience of the physical and social world. It introduces the World Scope framework, from corpus-level learning to internet text, perception, embodiment, and social interaction.

### Key contribution
The key contribution is the World Scope framing: WS1 corpus, WS2 internet-scale text, WS3 perception, WS4 embodiment, and WS5 social context. This framework is useful for explaining why web agents need more than static text representations. The web is not only text; it is an interactive, multimodal, dynamic environment.

### Method / approach
This is a conceptual and survey-like paper rather than a method paper. It synthesizes NLP, cognitive science, linguistics, multimodal learning, embodied AI, and social communication to argue that language meaning is grounded in use and experience.

### Key findings
The paper does not provide a single benchmark result; its contribution is argumentative. It shows that text-only systems can perform well on benchmarks while still lacking grounded understanding. This is highly relevant for web automation, where an agent must connect language instructions to visual layouts, interface states, affordances, actions, and feedback.

### Limitations
Because the paper is conceptual, it does not provide an operational benchmark for grounding or a direct web-agent architecture. It also does not address LLM-era agents directly, since it predates the current wave of multimodal web agents.

### Relevance to thesis
This paper supports the foundational claim that generalized web automation requires grounding. For web data extraction, the agent must ground schema fields and values in page structure, visual layout, DOM nodes, and interaction results, not only in text tokens.

### How to use it in S2
Use it near the transition from language models to grounded/multimodal agents. It is especially useful for motivating why visual and DOM grounding become central later in S5.2.

### Connects to
- S2: grounding foundations
- S5.2: web perception and representation
- S5.5: grounding failure modes
- S6: field-level extraction grounding

### Sentence to add later
Bisk et al.'s World Scope framework helps explain why text-only LMs are insufficient for web automation: meaningful interaction requires grounding language in perception, embodiment, and feedback from the environment.

---

## 4. A Systematic Evaluation of Large Language Models of Code

### Venue / Status
- Final venue: DL4C @ ICLR 2022 workshop; arXiv version available.
- Status: workshop paper / preprint.
- Venue verification: PDF states “Published as a workshop paper at DL4C @ ICLR 2022”; arXiv version is 2202.13169.
- Citation caution: cite as workshop/supporting evidence, not as a top-tier main-track result.

### Core idea
The paper evaluates large language models of code and introduces PolyCoder, an open-source 2.7B-parameter code model trained on 249GB of code across 12 programming languages. It asks how open-source code LMs compare to closed models like Codex across languages.

### Key contribution
The paper contributes both an evaluation and an open model. It compares Codex, GPT-J, GPT-Neo, GPT-NeoX, CodeParrot, and PolyCoder. It highlights that model availability matters: black-box code models limit research on fine-tuning, interpretability, distillation, retrieval integration, and domain adaptation.

### Method / approach
The authors evaluate models on HumanEval and on multilingual code perplexity across 12 programming languages. PolyCoder is trained from a GPT-2-style architecture exclusively on code data. The comparison emphasizes multilingual generalization and open access.

### Key findings
Although Codex is strong across many programming languages, PolyCoder performs competitively and even outperforms Codex in C perplexity. The result suggests that targeted code training can outperform general or private models in specific languages and motivates open code models for academic research.

### Limitations
The work is older and predates modern code models such as Code Llama, DeepSeek-Coder, StarCoder, Qwen-Coder, and GPT-4-level coding systems. It focuses on code generation/perplexity, not web automation directly. It also evaluates code modeling rather than tool use or browser-control programs.

### Relevance to thesis
This paper is useful background for programmatic web automation and extraction. LLM agents often generate scripts, selectors, API calls, or browser-control code. Code LMs are therefore part of the foundation for agents that synthesize automation logic, especially when comparing reusable scraper generation against direct LLM extraction.

### How to use it in S2
Use it briefly in the foundation subsection on code models and tool/program synthesis. It should remain P3 because newer code-agent papers are more directly relevant.

### Connects to
- S2: code LMs
- S3: tool-using agents
- S6: scraper/program generation
- S8: open-source reproducibility

### Sentence to add later
Early evaluations of code LMs such as PolyCoder showed the importance of open, multilingual code models for reproducible research, a foundation later inherited by agents that generate browser scripts, extraction programs, and tool calls.

---

## 5. A Review on Language Models as Knowledge Bases

### Venue / Status
- Final venue: arXiv preprint, 2022.
- Status: survey preprint; no confirmed peer-reviewed venue found in this verification pass.
- Venue verification: arXiv 2204.06031; secondary sources cite it as arXiv.
- Citation caution: useful as a survey/taxonomy, but cite cautiously because it is not confirmed peer-reviewed.

### Core idea
The paper reviews the idea that pretrained language models can function as knowledge bases. It organizes the literature around properties that language models would need to behave like KBs: access, consistency, editability, reasoning, and explainability.

### Key contribution
The paper's main value is its taxonomy. It makes explicit that LMs differ from symbolic KBs because knowledge is distributed, difficult to access directly, inconsistent across prompts, hard to edit, and weakly explainable. This taxonomy maps well onto the limitations of LLM-based web extraction.

### Method / approach
The authors synthesize literature on LM probing, knowledge editing, consistency, reasoning, explainability, and comparison with symbolic KBs. The paper frames LMs-as-KBs as an aspiration rather than a solved capability.

### Key findings
The survey emphasizes that LMs contain useful factual and relational knowledge, but they lack the controllability of KBs. In KBs, facts are explicit and schema-governed; in LMs, facts are implicit, diffuse, and prompt-dependent. This explains why LLMs hallucinate and why extraction systems need external verification.

### Limitations
As a survey preprint, it does not introduce new empirical results. It also focuses on LM knowledge rather than web interaction, multimodal grounding, or source-level provenance. It should not be used as the primary source for claims already supported by peer-reviewed papers.

### Relevance to thesis
The taxonomy directly supports your argument that generalized web extraction needs schema, consistency, editability, explainability, and access to source evidence. LLMs alone do not provide those properties; agentic extraction systems must add them through retrieval, grounding, validation, and provenance.

### How to use it in S2
Use it as a bridging survey between parametric knowledge and structured KBs. It can help motivate why extraction must output structured, verifiable records rather than ungrounded text.

### Connects to
- S2: LM-as-KB limitations
- S6: schema-guided extraction
- S7: hallucination and controllability
- S8: verification-level generalization

### Sentence to add later
LM-as-KB surveys emphasize that although LMs encode factual knowledge, they lack KB-like access, consistency, editability, reasoning guarantees, and explainability, which motivates source-grounded extraction rather than parametric recall.

---

## 6. Selection-Inference: Exploiting Large Language Models for Interpretable Logical Reasoning

### Venue / Status
- Final venue: ICLR 2023.
- Status: peer-reviewed main conference paper, notable top 5%.
- Venue verification: OpenReview lists it under ICLR 2023 and marks it notable top 5%.
- Citation caution: safe to cite strongly.

### Core idea
Selection-Inference decomposes logical reasoning into two explicit modules: a selection module that chooses relevant premises and an inference module that derives one new fact from those premises. The process repeats iteratively to produce a causal and interpretable reasoning trace.

### Key contribution
The key contribution is showing that modular decomposition can make a smaller LLM outperform much larger vanilla baselines on multi-step logical reasoning. A 7B model inside the Selection-Inference framework improves by more than 100% over the equivalent vanilla baseline and can outperform a 280B model on the evaluated logical reasoning suite.

### Method / approach
The framework alternates selection and inference. Selection identifies the subset of facts needed for one step. Inference only sees the selected facts and generates an intermediate conclusion, which is added back to the context. This creates a causal chain of reasoning, unlike post-hoc explanations.

### Key findings
LLMs are better at single-step inference than long multi-step reasoning. Decomposing reasoning into smaller, verifiable steps improves performance and interpretability. The reasoning trace is also more useful for debugging because each inference depends on selected evidence.

### Limitations
The tasks are mostly formal/logical reasoning benchmarks, not dynamic web environments. The approach assumes that relevant facts are available in the context and does not solve retrieval, grounding, or interaction. Error propagation remains possible if selection or inference is wrong early.

### Relevance to thesis
Selection-Inference is relevant because web extraction often requires selecting relevant page evidence before inferring field values. It supports a design principle for extraction agents: separate evidence selection from field inference, and preserve the trace for verification.

### How to use it in S2
Use it in the reasoning foundations subsection to show the shift from monolithic CoT to modular, evidence-constrained reasoning.

### Connects to
- S2: reasoning foundations
- S5.3: planning and decomposition
- S6: evidence-grounded field extraction
- S8: provenance-aware evaluation

### Sentence to add later
Selection-Inference shows that decomposing reasoning into evidence selection and local inference can improve both accuracy and interpretability, a principle directly relevant to schema-guided extraction where each field should be inferred from selected source evidence.

---

## 7. Training Language Models with Language Feedback at Scale

### Venue / Status
- Final venue: arXiv preprint, 2023/2024.
- Status: preprint; no confirmed main conference/journal venue found in this verification pass.
- Venue verification: arXiv 2303.16755.
- Citation caution: cite as preprint and avoid treating results as established peer-reviewed evidence.

### Core idea
The paper proposes Imitation Learning from Language Feedback (ILF), where a model improves by generating refinements conditioned on free-form human language feedback. This differs from standard RLHF that mainly uses pairwise comparisons.

### Key contribution
The main contribution is showing that language feedback can be used as a richer training signal than binary preference comparisons. ILF generates multiple refinements, selects the one that best incorporates the feedback, and fine-tunes the model on that refinement. The paper also frames ILF as related to Bayesian inference and reward-based optimization.

### Method / approach
The algorithm has three steps: generate an initial output, receive natural-language feedback, generate refinements conditioned on the feedback, select the best refinement with a reward or judge model, and fine-tune on the selected refinement. Experiments include a controlled toy task and summarization.

### Key findings
The paper reports that large models can incorporate feedback effectively, that ILF scales with data size, and that combining language feedback with comparison feedback performs better than either alone. On summarization, the hybrid approach reaches human-level performance under the authors' evaluation setup.

### Limitations
The work depends heavily on strong LMs for refinement and selection. The evidence is not from web-agent tasks, and it does not address action trajectories, browser state, or extraction correctness. Since it is a preprint, use it as a conceptual support for language-feedback training, not as a definitive benchmark result.

### Relevance to thesis
This paper supports the idea that extraction agents can improve from human correction comments, not only binary success/failure labels. For web data extraction, annotators often provide natural-language explanations such as “this field is from the wrong card” or “pagination was incomplete”; ILF-like methods are relevant for converting such feedback into training data.

### How to use it in S2
Use it briefly in the feedback/alignment foundations subsection. It can later connect to training strategies in S5.4.

### Connects to
- S2: feedback learning
- S5.4: training strategies
- S6: correction of extraction errors
- S8: human-in-the-loop evaluation

### Sentence to add later
Language-feedback training suggests that free-form corrections can provide richer supervision than pairwise preferences, which is useful for web extraction agents because many failures require explanatory feedback about wrong fields, missing records, or incorrect provenance.

---

## 8. Adapting Language Models to Compress Contexts

### Venue / Status
- Final venue: EMNLP 2023.
- Status: peer-reviewed conference paper.
- Venue verification: ACL Anthology lists it in EMNLP 2023, pages 3829–3846, DOI 10.18653/v1/2023.emnlp-main.232.
- Citation caution: safe to cite strongly.

### Core idea
The paper introduces AutoCompressors, which adapt pretrained language models to compress long contexts into compact summary vectors. These vectors act as soft prompts that preserve useful information while reducing inference cost.

### Key contribution
The main contribution is showing that models can learn to create reusable summary vectors for long documents. These vectors can substitute for plain text demonstrations in in-context learning and can be precomputed for retrieval-augmented use cases.

### Method / approach
The model processes long documents segment by segment. It appends special summary tokens, uses their hidden states as soft summary vectors, and passes accumulated summaries to future segments. The model is trained with an unsupervised language modeling objective over segmented long contexts.

### Key findings
AutoCompressors improve long-context perplexity, help compress in-context demonstrations, and improve inference efficiency. The method also supports precomputing vectors for large corpora, making it relevant to retrieval-augmented language modeling and passage reranking.

### Limitations
Soft summary vectors are not human-readable, which limits provenance and auditability. Compression may discard details important for extraction, especially rare fields or exact values. The method is more useful for efficient context handling than for source-verifiable extraction unless paired with explicit provenance tracking.

### Relevance to thesis
This paper supports a key design trade-off: web agents need to manage long pages and multi-page contexts efficiently, but compression must not destroy field-level evidence. It motivates separating context compression for reasoning from exact source retention for extraction verification.

### How to use it in S2
Use it in the long-context foundations subsection to show that long-context capacity can be extended through compression, not only by scaling attention windows.

### Connects to
- S2: long-context foundations
- S5.2: representation compression
- S6: extraction from long pages
- S8: cost-aware evaluation

### Sentence to add later
AutoCompressors show that long-context processing can be improved by learned context compression, but extraction systems must still preserve exact source evidence because compressed vectors alone cannot provide auditable provenance.

---

## 9. AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback

### Venue / Status
- Final venue: NeurIPS 2023.
- Status: peer-reviewed main conference paper.
- Venue verification: OpenReview lists AlpacaFarm under NeurIPS 2023; NeurIPS proceedings references it in volume 36.
- Citation caution: safe to cite strongly.

### Core idea
AlpacaFarm is a low-cost simulation environment for studying methods that learn from human feedback. It replaces expensive human pairwise feedback with LLM-simulated feedback and provides validated evaluation and reference implementations.

### Key contribution
The paper contributes a reproducible sandbox for feedback-based instruction tuning. It claims simulated feedback is around 45–50x cheaper than crowdworker feedback and that model rankings developed in AlpacaFarm correlate strongly with rankings from human-feedback development.

### Method / approach
AlpacaFarm has three parts: simulated pairwise feedback using API LLMs, automatic evaluation by model-vs-baseline win rate, and reference implementations for learning from pairwise feedback, including PPO, best-of-N, expert iteration, and related methods.

### Key findings
The framework enables fast experimentation on alignment algorithms. The authors report that method rankings in simulation align closely with rankings from real human feedback, and that PPO with a reward model improves an instruction-tuned LLaMA 7B model against Davinci003.

### Limitations
Simulated feedback can inherit the biases and blind spots of the oracle LLM. The framework evaluates instruction-following, not web-agent interaction or extraction. Transfer from simulated feedback to real user needs remains task-dependent.

### Relevance to thesis
AlpacaFarm is useful for thinking about low-cost evaluation and development of extraction agents. For web extraction, human annotations are expensive; simulated feedback could help develop methods before final human validation. However, extraction requires stricter ground truth than general instruction following.

### How to use it in S2
Use it in the feedback learning subsection as a foundation for scalable feedback experimentation.

### Connects to
- S2: feedback-based model development
- S5.4: training web agents
- S8: evaluation cost and reproducibility

### Sentence to add later
AlpacaFarm shows how simulated feedback can reduce the cost of alignment-method development, but extraction agents still require task-specific validation because general preference signals do not guarantee field-level correctness or provenance.

---

## 10. Random-Access Infinite Context Length for Transformers

### Venue / Status
- Final venue: NeurIPS 2023.
- Status: peer-reviewed main conference paper.
- Venue verification: NeurIPS proceedings list it in Advances in Neural Information Processing Systems 36, Main Conference Track.
- Citation caution: safe to cite strongly.

### Core idea
The paper introduces Landmark Attention, a method for allowing transformers to access arbitrarily long contexts by using landmark tokens that represent blocks of input and guide retrieval of relevant blocks through attention itself.

### Key contribution
The contribution is an architecture-level method that preserves random-access flexibility better than recurrent memory while reducing cost. Landmark tokens act as gates for selecting relevant input blocks. The method extends LLaMA 7B to contexts over 32k tokens and reduces attention computation by the block size in the authors' setup.

### Method / approach
The input is divided into blocks, and each block receives a landmark token. During inference, the model attends to landmarks to decide which blocks should be loaded into attention. This allows the model to retrieve past blocks through the attention mechanism rather than relying on a separate retriever.

### Key findings
Landmark Attention can process contexts longer than the training context and achieve performance comparable to memory-based approaches while using fewer retrieved tokens. It can also integrate with memory hierarchies and nearest-neighbor data structures.

### Limitations
The method improves access to long input, but it does not solve reasoning, factuality, or provenance on its own. It also remains a model-architecture solution rather than an agent-level context-management strategy. For extraction, selecting a relevant block is not enough; the agent must still extract exact values and cite source locations.

### Relevance to thesis
This paper provides foundation for efficient long-page and multi-page processing. Web pages can be long, noisy, and dynamic. Landmark-style access suggests that agent systems should selectively access relevant parts rather than process everything at full attention cost.

### How to use it in S2
Use it in the long-context model foundations subsection.

### Connects to
- S2: long-context architectures
- S5.2: web representation pruning
- S6: long document/page extraction
- S8: cost-aware benchmarks

### Sentence to add later
Landmark Attention shows that long-context access can be made more efficient by selecting relevant blocks through attention, reinforcing the broader principle that web agents should use selective context access rather than brute-force full-page processing.

---

## 11. SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning

### Venue / Status
- Final venue: ICLR 2024.
- Status: peer-reviewed main conference paper.
- Venue verification: OpenReview and Oxford records list it as ICLR 2024.
- Citation caution: safe to cite strongly.

### Core idea
SelfCheck asks whether LLMs can detect errors in their own step-by-step reasoning without training data, examples, or external verifiers. It proposes a zero-shot verification scheme that checks each reasoning step by extracting its target, regenerating an independent alternative step, and comparing the result.

### Key contribution
The contribution is a general-purpose verification strategy for reasoning chains. Instead of directly asking “is this step correct?”, SelfCheck decomposes checking into subtasks that reduce correlation between generation and verification errors.

### Method / approach
For each reasoning chain, SelfCheck checks individual steps conditioned on previous steps. It extracts the target and relevant context, independently regenerates the step, compares it with the original step, and aggregates step-level confidence into a solution-level confidence score. It then uses weighted voting over multiple solutions.

### Key findings
SelfCheck improves answer accuracy on GSM8K, MathQA, and MATH compared with majority voting and other baselines. It also identifies low-confidence solutions and reduces the proportion of incorrect outputs after filtering.

### Limitations
The paper focuses mainly on mathematical reasoning. Self-verification can still fail if the model shares the same blind spot in generation and checking. It does not use external evidence, so it is insufficient for factual web extraction where source verification is required.

### Relevance to thesis
SelfCheck supports the idea of step-level verification. In web extraction, each extracted field, navigation step, or reasoning step can be checked independently. However, unlike math, web extraction must verify against external page evidence, not just internal consistency.

### How to use it in S2
Use it in the reasoning verification subsection after CoT and before CoVe/CoV-RAG.

### Connects to
- S2: self-verification
- S5.3: planning verification
- S6: field-level checking
- S8: provenance accuracy metrics

### Sentence to add later
SelfCheck demonstrates that step-level verification can improve LLM reasoning without additional training, but web extraction requires a stronger variant in which each step is checked against external page evidence rather than only internal consistency.

---

## 12. Chain-of-Verification Reduces Hallucination in Large Language Models

### Venue / Status
- Final venue: Findings of ACL 2024.
- Status: peer-reviewed Findings paper.
- Venue verification: ACL Anthology lists it in Findings of ACL 2024, pages 3563–3578.
- Citation caution: safe to cite, but note it is Findings rather than main conference.

### Core idea
Chain-of-Verification (CoVe) reduces hallucination by forcing the model to draft an answer, generate verification questions, answer them independently, and then produce a revised final response.

### Key contribution
The key contribution is a structured generation-time verification procedure for hallucination reduction. It separates answer generation from fact-checking questions and shows that independent verification can reduce factual errors in list-based, closed-book QA, and long-form generation tasks.

### Method / approach
The CoVe pipeline consists of four stages: baseline response, verification planning, independent execution of verification questions, and final verified response. The factored variant prevents the verification answerer from conditioning on the original hallucinated response, reducing repetition of errors.

### Key findings
CoVe decreases hallucinations across several tasks. The paper shows that models often answer targeted verification questions more accurately than they produce all facts in a long-form answer. This supports the principle of decomposed fact-checking.

### Limitations
CoVe often still relies on the model’s parametric knowledge unless connected to retrieval or tools. It is not a full source-grounded verification framework. For dynamic web extraction, verification questions must be answered from retrieved or observed page evidence.

### Relevance to thesis
CoVe is important because generalized web extraction needs verification chains: identify extracted claims, ask source-check questions, verify values against DOM/visual evidence, and revise outputs. The method also connects directly to CoV-RAG and provenance-aware extraction.

### How to use it in S2
Use it in the hallucination and verification foundations subsection.

### Connects to
- S2: hallucination mitigation
- S5.3: verification planning
- S6: source-grounded extraction verification
- S7: hallucination as security/data-quality risk

### Sentence to add later
Chain-of-Verification shows that LLM hallucinations can be reduced by explicitly planning and answering verification questions, suggesting that extraction agents should verify each extracted field before committing structured outputs.

---

## 13. FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation

### Venue / Status
- Final venue: Findings of ACL 2024.
- Status: peer-reviewed Findings paper.
- Venue verification: ACL Anthology lists it in Findings of ACL 2024, pages 13697–13720.
- Citation caution: safe to cite, with note that it is Findings.

### Core idea
FreshLLMs studies LLM factuality under fast-changing world knowledge and false-premise questions. It introduces FreshQA and FreshPrompt, showing that search engine augmentation can improve answers to dynamic questions.

### Key contribution
The paper contributes FreshQA, a dynamic QA benchmark with never-changing, slow-changing, fast-changing, and false-premise questions, plus FreshPrompt, a prompting method that incorporates search results and related snippets into the context. It also uses relaxed and strict evaluation to distinguish main-answer correctness from hallucination-free factuality.

### Method / approach
The authors collect 600 natural questions, perform over 50k human judgments, evaluate multiple open and closed LLMs, and test search-augmented prompting methods. FreshPrompt injects up-to-date search evidence and encourages concise, direct answers.

### Key findings
All models struggle with fast-changing knowledge and false premises. Scaling model size alone does not solve freshness. FreshPrompt substantially improves GPT-4 performance on FreshQA, and the number/order of retrieved evidences affects correctness.

### Limitations
The benchmark is QA-oriented, not extraction-oriented. Search snippets are not equivalent to structured evidence from arbitrary webpages. It does not solve pagination, schema adherence, or field-level provenance.

### Relevance to thesis
FreshLLMs directly supports the claim that parametric knowledge is stale and that web agents need retrieval from live sources. It is especially useful when motivating source freshness and false-premise handling in web automation.

### How to use it in S2
Use it after closed-book QA to show why retrieval/search augmentation is necessary.

### Connects to
- S2: freshness and retrieval
- S5.1: dynamic evaluation
- S6: live web extraction
- S7: false-premise and hallucination risks

### Sentence to add later
FreshQA shows that LLMs struggle with fast-changing and false-premise questions, reinforcing that generalized web extraction must access current web evidence rather than rely on stale parametric knowledge.

---

## 14. Learning From Mistakes Makes LLM Better Reasoner

### Venue / Status
- Final venue: arXiv preprint, 2023/2024.
- Status: preprint; no confirmed peer-reviewed venue found in this pass.
- Venue verification: arXiv 2310.20689; references and secondary results treat it as arXiv.
- Citation caution: cite as preprint and avoid over-weighting.

### Core idea
The paper proposes LEMA, a training approach where LLMs learn from mistake-correction data. Instead of only training on correct chain-of-thought solutions, it collects erroneous reasoning paths and uses GPT-4 to identify the mistake, explain it, correct it, and generate the final answer.

### Key contribution
The main contribution is the idea that correction data is complementary to standard CoT data. The paper argues that learning from mistakes mimics human learning: a model benefits from seeing where reasoning fails and how to repair it.

### Method / approach
The method samples incorrect reasoning paths from LLMs, filters for wrong final answers, uses GPT-4 as a corrector, and generates mistake-correction pairs. It also proposes correction-centric evolution to expand the question set around moderately difficult examples. These data are mixed with CoT data for fine-tuning.

### Key findings
The paper reports consistent improvements over CoT-only fine-tuning on math and commonsense reasoning tasks. It also reports that mixing CoT and correction data performs better than either alone under controlled training sizes.

### Limitations
The method depends on GPT-4 correction quality and focuses mainly on reasoning benchmarks. It does not prove that correction data transfers to web agents, where mistakes may involve visual grounding, interaction state, or incomplete extraction rather than pure reasoning. Since it is a preprint, results should be treated as suggestive.

### Relevance to thesis
LEMA is relevant for training extraction agents from failed trajectories. A failed web extraction attempt can be converted into correction data: wrong field, reason for error, corrected field, and evidence location. This is especially useful for failure-mode learning.

### How to use it in S2
Use it in the feedback/correction foundations subsection, but do not make it a central citation.

### Connects to
- S2: correction-based learning
- S5.4: training from failed trajectories
- S5.5: failure modes
- S6: field-error correction

### Sentence to add later
Mistake-correction training suggests that failed reasoning traces can become useful supervision, a principle that can be adapted to web extraction by converting wrong fields or missed records into explicit correction examples.

---

## 15. Exploring the Reasoning Abilities of Multimodal Large Language Models: A Comprehensive Survey on Emerging Trends in Multimodal Reasoning

### Venue / Status
- Final venue: arXiv preprint, 2024.
- Status: survey preprint; no confirmed peer-reviewed venue found in this pass.
- Venue verification: arXiv 2401.06805.
- Citation caution: cite cautiously as a survey preprint.

### Core idea
This survey reviews multimodal reasoning in MLLMs, including definitions, evaluation protocols, training practices, benchmarks, embodied applications, and tool usage. It argues that multimodal reasoning has not been systematically understood despite rapid progress.

### Key contribution
The paper is useful as a broad map of multimodal reasoning tasks and reasoning types: deductive, inductive, abductive, analogical, mathematical, commonsense, symbolic, and environment-interaction reasoning. It also links MLLMs to embodied AI and tool use.

### Method / approach
The authors survey multimodal reasoning benchmarks, MLLM architectures, multimodal instruction tuning, reasoning-intensive applications, embodied AI, tool usage, and benchmark results.

### Key findings
The survey emphasizes that current MLLMs show impressive benchmark performance but still struggle with true reasoning, hallucination, multimodal integration, and robust evaluation. It also notes that reasoning over multiple modalities requires selecting, integrating, and verifying information across text, images, and other inputs.

### Limitations
As a broad arXiv survey, it may overlap with other MLLM surveys and does not focus on web agents or data extraction. It should be used as background rather than evidence for specific benchmark claims.

### Relevance to thesis
This paper supports the role of multimodal reasoning in web agents. Many webpages require understanding screenshots, icons, layout, charts, and visual relationships. For generalized extraction, multimodal reasoning matters when the DOM is incomplete, hidden, or misleading.

### How to use it in S2
Use it in a short paragraph introducing multimodal reasoning foundations.

### Connects to
- S2: multimodal reasoning
- S5.2: web perception
- S5.3: multimodal planning
- S6: visual-field extraction

### Sentence to add later
Multimodal reasoning surveys show that MLLMs require not only visual recognition but also integration and inference across modalities, which is essential for web agents operating over screenshots, DOM structure, and interactive page states.

---

## 16. Video as the New Language for Real-World Decision Making

### Venue / Status
- Final venue: arXiv preprint, 2024.
- Status: position/vision preprint; no confirmed peer-reviewed venue found in this pass.
- Venue verification: arXiv 2402.17139.
- Citation caution: cite as position paper / grey literature support.

### Core idea
The paper argues that video can become a general representation and interface for real-world decision making, analogous to how text acts as a general interface for LLMs. Video generation models could serve as planners, agents, simulators, and compute engines for physical-world tasks.

### Key contribution
The contribution is conceptual: it reframes video not merely as media generation but as a possible world-model substrate for planning and decision making. This expands the grounding discussion from static images and text to temporal, embodied, and action-conditioned representations.

### Method / approach
The paper synthesizes literature on conditional video generation, robotics, world models, visual planning, reinforcement learning, and simulation. It enumerates ways video models can be conditioned on text, images, actions, or prior frames.

### Key findings
The paper argues that video data contains information about physical dynamics that text cannot easily encode. Video generation may support planning, policies, environment simulation, and action optimization in domains like robotics and self-driving.

### Limitations
The paper is a position/vision paper rather than a benchmarked method. It is mostly about the physical world, not web environments. It should not be used as core evidence for web extraction, but it can support the broader grounding narrative.

### Relevance to thesis
For web automation, the relevant lesson is that action-conditioned visual state transitions matter. A browser agent also needs to predict how actions change the environment, although the environment is digital rather than physical. Video-style or trajectory-style modeling can inspire future web-agent training from screen recordings.

### How to use it in S2
Use only briefly in the grounding/multimodal foundations subsection.

### Connects to
- S2: embodied/multimodal grounding
- S5.2: screen perception
- S5.3: action planning
- S5.4: trajectory learning

### Sentence to add later
Recent position work on video models argues that temporally grounded visual data can support planning and decision making, suggesting an analogous role for browser trajectories and screen recordings in training web agents.

---

## 17. A Critical Evaluation of AI Feedback for Aligning Large Language Models

### Venue / Status
- Final venue: NeurIPS 2024.
- Status: peer-reviewed main conference paper.
- Venue verification: OpenReview and NeurIPS proceedings list it as NeurIPS 2024.
- Citation caution: safe to cite strongly.

### Core idea
The paper questions whether reinforcement learning from AI feedback (RLAIF/LAIF) is always necessary when using strong LLMs as feedback providers. It argues that much of the apparent gain from AI feedback comes from comparing weak-teacher SFT to strong-critic feedback, rather than from the RL stage itself.

### Key contribution
The central contribution is a careful evaluation showing that supervised fine-tuning on GPT-4-generated completions can outperform common RLAIF pipelines that use weaker SFT data plus stronger critic feedback. It identifies conditions under which AI feedback helps: strong base model, capability mismatch between teacher and critic, and careful evaluation setup.

### Method / approach
The authors align several base models with SFT and RLAIF using teacher completions from GPT-3.5, GPT-4, and Claude, and critic feedback from GPT-4 and Claude. They evaluate with AlpacaEval and provide a mechanistic explanation in a simplified setting.

### Key findings
RLAIF gains are not universal. If the SFT teacher is already strong, the RL feedback stage may add little or no benefit. Performance varies by base model family, critic model, and evaluation protocol. The paper recommends accounting for the distribution and quality of SFT completions before attributing gains to AI feedback.

### Limitations
The paper focuses on general instruction-following, not agents or web extraction. It does not resolve how feedback should be structured for action trajectories, tool use, or field-level extraction. However, its methodological caution is important.

### Relevance to thesis
This paper warns against assuming that RL or AI feedback will automatically improve web agents. For extraction agents, high-quality demonstrations, task-specific corrections, and verified labels may matter more than generic preference feedback.

### How to use it in S2
Use it in the alignment/feedback foundations subsection to give a balanced view.

### Connects to
- S2: feedback and alignment
- S5.4: training strategies
- S8: evaluation methodology

### Sentence to add later
Recent evaluations of AI feedback show that improvements attributed to RLAIF may largely come from teacher/critic quality mismatch, cautioning that web-agent training must distinguish the value of demonstrations, feedback, and reward optimization.

---

## 18. RAT: Retrieval Augmented Thoughts Elicit Context-Aware Reasoning in Long-Horizon Generation

### Venue / Status
- Final venue: arXiv preprint, 2024; secondary evidence suggests workshop usage, but no confirmed main conference/journal acceptance in this pass.
- Status: preprint / possible workshop.
- Venue verification: arXiv 2403.05313.
- Citation caution: cite cautiously as preprint unless later accepted version is confirmed.

### Core idea
RAT combines retrieval-augmented generation with chain-of-thought by iteratively revising each reasoning step using retrieved external information. Instead of generating a full CoT and final answer at once, it revises thoughts step by step with relevant knowledge.

### Key contribution
The paper contributes a reasoning-time retrieval strategy for long-horizon generation. It argues that hallucination in intermediate thoughts can be mitigated by retrieving evidence for the current and previous reasoning steps and revising them progressively.

### Method / approach
RAT first generates an initial zero-shot CoT. Then, for each thought step, it retrieves relevant information using the original prompt and current/past thoughts, revises the step with the retrieved context, and continues progressively. It evaluates on code generation, math reasoning, creative writing, and embodied task planning.

### Key findings
The paper reports relative improvements across several long-horizon tasks, including code generation, math, creative writing, and Minecraft planning. The strongest thesis-relevant idea is not the exact numbers but the architecture: retrieval should be interleaved with reasoning, not simply prepended once.

### Limitations
The work is preprint status and evaluations include subjective tasks. It does not prove extraction-specific correctness. Retrieval quality and evidence relevance remain crucial. In web extraction, retrieval must be replaced or complemented by exact page observation and provenance.

### Relevance to thesis
RAT supports a design pattern for web agents: interleave reasoning with evidence acquisition. A web extraction agent should not plan once and extract blindly; it should retrieve/observe, reason, verify, and revise iteratively.

### How to use it in S2
Use it as supporting evidence in the retrieval-augmented reasoning subsection.

### Connects to
- S2: RAG + reasoning
- S5.3: long-horizon planning
- S6: iterative extraction and verification

### Sentence to add later
Retrieval-Augmented Thoughts illustrates a useful pattern for web agents: reasoning should be interleaved with evidence retrieval and revision, rather than relying on a single initial context injection.

---

## 19. Beyond Chain-of-Thought: A Survey of Chain-of-X Paradigms for LLMs

### Venue / Status
- Final venue: COLING 2025.
- Status: peer-reviewed conference survey.
- Venue verification: ACL Anthology lists it in Proceedings of COLING 2025, pages 10795–10809.
- Citation caution: safe to cite.

### Core idea
The paper surveys Chain-of-X methods that generalize Chain-of-Thought beyond reasoning traces. It categorizes chain nodes as intermediates, augmentation, feedback, and models, and surveys applications across multimodal interaction, factuality, agents, instruction following, and evaluation.

### Key contribution
The main contribution is a taxonomy of chain structures. It shows that “chain” methods are not limited to thoughts; they can include retrieval steps, feedback, model calls, tool outputs, histories, actions, and verification nodes.

### Method / approach
The survey organizes CoX methods by node type and by task domain. It defines Chain-of-X as an input followed by a sequence of problem-related components and output. This makes it useful for interpreting many reasoning-agent methods under one umbrella.

### Key findings
The survey shows that CoX methods are widely used to decompose, augment, verify, refine, or orchestrate LLM outputs. It also points to future directions in agentic reasoning, evaluation, and multimodal interaction.

### Limitations
It is broad and not specific to web agents or extraction. Since it surveys many methods, individual claims should still be traced to original papers when central. For your review, it is best used as taxonomy background.

### Relevance to thesis
This paper can help organize reasoning techniques in your foundations section. Web agents naturally use Chain-of-X patterns: chain-of-thought, chain-of-actions, chain-of-observations, chain-of-verification, and chain-of-extraction.

### How to use it in S2
Use it to introduce the broader reasoning-design space after basic CoT.

### Connects to
- S2: reasoning paradigms
- S3: agent architectures
- S5.3: planning and action chains
- S6: extraction/verification chains

### Sentence to add later
The Chain-of-X literature generalizes CoT into chains of augmentation, feedback, model calls, and actions, providing a useful vocabulary for web agents whose reasoning involves observations, tool calls, and verification steps.

---

## 20. Can Small Language Models Help Large Language Models Reason Better?: LM-Guided Chain-of-Thought

### Venue / Status
- Final venue: LREC-COLING 2024.
- Status: peer-reviewed conference paper.
- Venue verification: ACL Anthology lists it in LREC-COLING 2024, pages 2835–2843.
- Citation caution: safe to cite.

### Core idea
LM-Guided CoT uses a small language model to generate rationales that guide a frozen large model in multi-hop QA. The method separates rationale generation from answer prediction: the small model is trained and optimized, while the large model remains black-box/frozen.

### Key contribution
The paper contributes a resource-efficient framework where a lightweight model acts as a reasoning guide for a larger model. It uses knowledge distillation and reinforcement learning from rationale-oriented and task-oriented rewards to improve rationale quality.

### Method / approach
The small model generates a rationale for each input. The large model receives the question, context, and generated rationale, then predicts the answer. Training includes rationale distillation from the large model and RL refinement based on rationale quality dimensions and task accuracy. Experiments use HotpotQA and 2WikiMultiHopQA.

### Key findings
The method outperforms standard prompting and original CoT baselines on multi-hop extractive QA. RL slightly improves rationale quality and QA performance. The paper also finds that higher-rated rationales do not always produce better answer accuracy, indicating misalignment between rationale quality and task utility.

### Limitations
The method is evaluated on QA, not browser agents. It assumes access to a context and does not solve source discovery or web interaction. The split between small rationale model and large answer model may complicate end-to-end accountability.

### Relevance to thesis
The paper supports the idea that smaller models can guide larger models or reduce cost. For web extraction, lightweight models could generate extraction plans, selectors, or rationales, while larger models perform difficult interpretation only when needed.

### How to use it in S2
Use it as a P3 example in the efficient reasoning subsection.

### Connects to
- S2: efficient reasoning
- S5.3: planning support
- S8: cost-aware agent design

### Sentence to add later
LM-Guided CoT suggests that reasoning can be modularized across model sizes, with smaller models generating rationales or plans that guide larger models, a pattern relevant to cost-aware web agents.

---

## 21. Mind's Eye of LLMs: Visualization-of-Thought Elicits Spatial Reasoning in Large Language Models

### Venue / Status
- Final venue: NeurIPS 2024.
- Status: peer-reviewed main conference paper.
- Venue verification: NeurIPS proceedings list it in Advances in Neural Information Processing Systems 37, Main Conference Track.
- Citation caution: safe to cite strongly.

### Core idea
The paper introduces Visualization-of-Thought (VoT), a prompting method where LLMs visualize intermediate reasoning states as text-form mental images. It targets spatial reasoning tasks such as natural-language navigation, visual navigation, and visual tiling.

### Key contribution
The contribution is showing that text-only LLMs can improve spatial reasoning by explicitly generating intermediate visual states. VoT interleaves reasoning steps and visualizations, resembling a visuospatial sketchpad.

### Method / approach
The prompt instructs the model to “visualize the state after each reasoning step.” For spatial tasks, the model generates 2D grid-like visualizations using text/special characters. The next reasoning step conditions on both previous reasoning and visual state.

### Key findings
VoT improves spatial reasoning performance and can outperform some multimodal baselines in the evaluated synthetic tasks. The paper also introduces visual navigation and visual tiling datasets.

### Limitations
The environments are synthetic 2D grids, not real webpages. The method depends on the model’s ability to maintain accurate text-based visualizations, which can fail in larger or noisier settings. It is a prompting technique, not a trained web-agent system.

### Relevance to thesis
VoT is relevant because web agents require spatial layout reasoning: where elements are, what is visible, what changed after a click, and which records belong to which card or row. The idea of maintaining a visual state can inform web-agent perception and planning.

### How to use it in S2
Use it in the multimodal/spatial reasoning foundations subsection and later connect to S5.2.

### Connects to
- S2: spatial reasoning foundations
- S5.2: visual grounding
- S5.3: navigation planning
- S6: layout-aware extraction

### Sentence to add later
Visualization-of-Thought shows that explicit visual state tracking can improve spatial reasoning, which is relevant to web agents that must reason over page layout, element positions, and visual grouping before extracting structured data.

---

## 22. Are Long-LLMs A Necessity For Long-Context Tasks?

### Venue / Status
- Final venue: arXiv preprint, 2024.
- Status: preprint; no confirmed peer-reviewed main venue found in this pass.
- Venue verification: arXiv 2405.15318.
- Citation caution: cite cautiously as preprint.

### Core idea
The paper argues that many long-context tasks are short-context solvable if the model can strategically access and use the relevant parts of the long input. It proposes LC-Boost, a framework that lets a short-context LLM reason about how to access and utilize context.

### Key contribution
The key contribution is challenging the assumption that long-context tasks require long-context models. LC-Boost separates two decisions: access, meaning how to locate relevant context; and utilize, meaning how to process the retrieved or scanned context.

### Method / approach
LC-Boost uses a short-context LLM to plan context access strategies. Depending on the task, it may use retrieval, divide-and-conquer scanning, aggregation, or other context access mechanisms. The paper compares brute-force long-context processing with short-context adaptive processing.

### Key findings
The paper reports that LC-Boost can match or outperform long-context brute-force processing while using fewer resources. It emphasizes that irrelevant context can distract long-context models and that task-specific context access can improve both efficiency and quality.

### Limitations
The paper is a preprint. The claim that most long-context tasks are short-context solvable may not hold for all web extraction tasks, especially those requiring complete pagination or exhaustive record collection. The framework also depends on effective access decisions.

### Relevance to thesis
This paper is highly relevant to cost-efficient web extraction. Web pages and sites can be huge, but extraction often needs specific fields and records. Agents should use adaptive access rather than feed full pages blindly into long-context models.

### How to use it in S2
Use it in the long-context efficiency subsection as a conceptual support for adaptive context access.

### Connects to
- S2: long-context alternatives
- S5.2: page pruning and representation
- S6: pagination and completeness
- S8: cost/energy-aware extraction metrics

### Sentence to add later
LC-Boost challenges brute-force long-context processing by showing that many tasks can be solved through adaptive context access and utilization, a principle directly applicable to efficient web extraction over long or multi-page sources.

---

## 23. Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models

### Venue / Status
- Final venue: NeurIPS 2024.
- Status: peer-reviewed main conference paper.
- Venue verification: NeurIPS proceedings list it in Advances in Neural Information Processing Systems 37.
- Citation caution: safe to cite strongly.

### Core idea
Buffer of Thoughts (BoT) stores high-level thought templates distilled from previous problem-solving processes and retrieves them for new tasks. The goal is to improve reasoning accuracy, efficiency, and robustness without expensive multi-query search.

### Key contribution
The key contribution is the meta-buffer: a lightweight library of reusable thought templates. Instead of exploring a new reasoning tree for every problem, the model retrieves a relevant template and instantiates it for the current task. A buffer manager updates the buffer as more tasks are solved.

### Method / approach
BoT uses a problem distiller to extract key task information, retrieves a thought template from the meta-buffer, instantiates it into a task-specific reasoning structure, and solves the problem. After solving, the buffer manager distills high-level thoughts from the process and updates the memory.

### Key findings
The paper reports improvements over prior methods on reasoning-intensive tasks, including Game of 24, Geometric Shapes, and Checkmate-in-One, while using only around 12% of the cost of multi-query prompting methods on average. It also reports robustness and generalization benefits.

### Limitations
The tasks are reasoning benchmarks, not web automation tasks. Template retrieval can fail if the task is novel or if the retrieved template is misleading. Maintaining a high-quality buffer requires careful update policies.

### Relevance to thesis
BoT supports the idea of reusable reasoning templates for web agents. Extraction agents could store successful extraction patterns, pagination strategies, login workflows, or schema-mapping templates and retrieve them for similar websites.

### How to use it in S2
Use it in the reasoning-memory subsection and later connect to agent memory.

### Connects to
- S2: thought templates and reasoning memory
- S3: agent memory
- S5.3: planning templates
- S6: reusable extraction strategies

### Sentence to add later
Buffer of Thoughts suggests that reusable high-level reasoning templates can improve efficiency and robustness, pointing toward web agents that store and retrieve extraction or navigation strategies rather than planning from scratch for every site.

---

## 24. Retrieving, Rethinking and Revising: The Chain-of-Verification Can Improve Retrieval Augmented Generation

### Venue / Status
- Final venue: Findings of EMNLP 2024.
- Status: peer-reviewed Findings paper.
- Venue verification: ACL Anthology lists it in Findings of EMNLP 2024, pages 10371–10393.
- Citation caution: safe to cite, with Findings note.

### Core idea
CoV-RAG integrates Chain-of-Verification into retrieval-augmented generation to correct both retrieval errors and generation errors. It verifies references and answers, revises the query when necessary, retrieves again, and regenerates the answer.

### Key contribution
The paper separates two RAG failure modes: external retrieval error and internal generation error. It introduces verification scoring and judgment dimensions such as reference correctness, answer correctness, citation accuracy, truthfulness, bias, and conciseness.

### Method / approach
During inference, the model retrieves top references, generates an answer, predicts verification results, decides whether re-retrieval is needed, revises the query if necessary, retrieves new references, and regenerates the answer. During training, it synthesizes positive and negative RAG examples with verification rationales.

### Key findings
The paper reports improvements over RAG baselines across QA datasets and model backbones. The important idea is that verification can guide both retrieval repair and generation repair, rather than only scoring the final answer.

### Limitations
It is still QA-focused, not web extraction-focused. It assumes retrievable text references and does not handle browser interaction, visual grounding, pagination, or structured schemas. GPT-4-based data synthesis may introduce judge bias.

### Relevance to thesis
CoV-RAG is directly useful for your argument about source-verifiable extraction. A web extraction agent needs a similar loop: extract, verify source correctness, revise query/navigation, re-observe, and regenerate structured output.

### How to use it in S2
Use it in the retrieval + verification foundations subsection and connect later to S6/S8.

### Connects to
- S2: RAG verification
- S5.3: iterative planning
- S6: source-verifiable extraction
- S8: verification metrics

### Sentence to add later
CoV-RAG shows that retrieval-augmented systems can be improved by explicitly verifying both retrieved references and generated answers, a design principle that maps naturally to source-verifiable web extraction.

---

## 25. Thinking LLMs: General Instruction Following with Thought Generation

### Venue / Status
- Final venue: ICML 2025.
- Status: peer-reviewed conference paper.
- Venue verification: OpenReview lists it under ICML 2025.
- Citation caution: safe to cite, especially for post-2024 reasoning-model context.

### Core idea
The paper trains instruction-following LLMs to generate internal thoughts before responses, not only for math or logic tasks but for general instruction following. It introduces Thought Preference Optimization (TPO), which optimizes thoughts indirectly by judging only the final response.

### Key contribution
The main contribution is showing that thought generation can help general instruction following, including categories not traditionally considered reasoning tasks, such as marketing, health, and general knowledge. It argues that thinking can function as additional inference-time compute.

### Method / approach
The model is prompted to produce a thought part and a response part. Multiple outputs are sampled. A judge model evaluates only the response part, and preference pairs are constructed from the full outputs. DPO-like optimization then trains the model to produce thoughts that lead to better responses.

### Key findings
TPO improves over direct-response baselines on AlpacaEval and Arena-Hard. The paper also shows that merely prompting an instruction-tuned model to think may hurt performance unless thought generation is optimized.

### Limitations
The thoughts are hidden/internal and not necessarily faithful. Evaluation depends on judge models and general instruction-following benchmarks. It does not address source grounding, web interaction, or extraction-specific metrics.

### Relevance to thesis
Thinking LLMs supports the idea that agent models may need explicit internal planning before action. However, web extraction requires those thoughts to be tied to observations and verifiable evidence, not just hidden reasoning.

### How to use it in S2
Use it in the modern reasoning/post-training foundations subsection.

### Connects to
- S2: thinking/reasoning post-training
- S3: agent planning
- S5.3: thought-action loops
- S8: inference cost and thought length

### Sentence to add later
Thinking LLMs shows that thought generation must be trained or optimized to be useful, suggesting that web-agent planning traces should be learned from task feedback rather than added only through prompting.

---

## 26. PRefLexOR: Preference-based Recursive Language Modeling for Exploratory Optimization of Reasoning and Agentic Thinking

### Venue / Status
- Final venue: npj Artificial Intelligence, 2025.
- Status: peer-reviewed open-access journal article; earlier arXiv preprint from 2024.
- Venue verification: Nature page lists publication on 14 May 2025 in npj Artificial Intelligence.
- Citation caution: peer-reviewed, but domain-specific and highly conceptual; use selectively.

### Core idea
PRefLexOR combines preference optimization, recursive reasoning, retrieval-augmented data generation, thinking tokens, and self-refinement to train small models to reason more deeply, especially in scientific/materials domains.

### Key contribution
The paper contributes a recursive preference-based framework where models generate, revisit, and refine reasoning steps during training and inference. It uses on-the-fly dataset generation from raw corpora, knowledge-graph-like retrieval, and special thinking/reflection tokens.

### Method / approach
The framework has multiple phases: structured thought integration using preference optimization, independent reasoning development where reasoning tokens may be masked, and recursive inference with self-reflection. The training pipeline uses dynamically generated question-answer pairs from scientific corpora and preferred/rejected responses.

### Key findings
The paper argues that even small models can improve scientific reasoning through recursive self-teaching. It demonstrates case studies in biological materials science and positions recursive reasoning as analogous to RL-style iterative policy refinement.

### Limitations
The paper is domain-specific and broad in ambition. Its evaluation may not generalize to web automation. Some claims are conceptual and should not be transferred directly to general agents without caution. The system is also complex, combining many components.

### Relevance to thesis
PRefLexOR is useful as an example of recursive reasoning and preference-based self-improvement. For web extraction, similar ideas could train agents to revise extraction plans and outputs based on evidence and preference/correction signals.

### How to use it in S2
Use it as a P3 example in the recursive reasoning and self-improvement subsection.

### Connects to
- S2: recursive reasoning
- S5.4: self-improvement training
- S6: iterative extraction refinement
- S8: agentic research agenda

### Sentence to add later
Recursive preference-based frameworks such as PRefLexOR illustrate a broader trend toward models that refine their reasoning over multiple cycles, although extraction agents still require grounding those cycles in observable web evidence.

---

## 27. Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent

### Venue / Status
- Final venue: ICLR 2025.
- Status: peer-reviewed main conference paper/poster.
- Venue verification: OpenReview lists it as ICLR 2025 Poster.
- Citation caution: safe to cite strongly.

### Core idea
The paper introduces Dyn-VQA, a dynamic multimodal VQA benchmark for multimodal RAG, and OmniSearch, a self-adaptive planning agent for multimodal retrieval. It argues that existing mRAG benchmarks are too static and too easy for fixed retrieval pipelines.

### Key contribution
The paper contributes both a benchmark and an agentic retrieval method. Dyn-VQA contains questions with rapidly changing answers, questions requiring multimodal knowledge, and multi-hop questions. OmniSearch dynamically decomposes complex multimodal questions into sub-question chains with retrieval actions.

### Method / approach
Dyn-VQA is built through textual question writing, multimodal rewriting with images, and Chinese-English translation. OmniSearch plans retrieval actions step by step, selecting tools and queries based on intermediate retrieved content and question-solving state.

### Key findings
Existing heuristic mRAG methods struggle with dynamic questions because their retrieval process is rigid. OmniSearch improves performance by adaptively choosing retrieval actions, tools, and subquestions. The benchmark includes 1,452 questions across domains and requires web/image search more heavily than prior VQA datasets.

### Limitations
Dyn-VQA is still VQA, not web extraction. It evaluates answer accuracy, not structured record extraction, pagination completeness, or schema adherence. OmniSearch depends on search tools and does not fully address page-level interaction.

### Relevance to thesis
This paper is very relevant for dynamic retrieval and multimodal planning. It supports your argument that real web agents cannot rely on fixed retrieval or fixed observation pipelines; they need adaptive planning across tools, modalities, and time.

### How to use it in S2 or later
Use in S2 as a foundation for dynamic multimodal retrieval, then later in S5.1/S5.2 when discussing benchmarks and multimodal web perception.

### Connects to
- S2: multimodal RAG foundations
- S5.1: benchmark gaps
- S5.2: multimodal retrieval/perception
- S6: live web evidence acquisition

### Sentence to add later
Dyn-VQA and OmniSearch show that dynamic multimodal questions require adaptive retrieval over query, tool, and time, a capability that generalized web extraction agents also need when evidence is distributed across changing web pages and modalities.

---

## 28. Command A: An Enterprise-Ready Large Language Model

### Venue / Status
- Final venue: Cohere technical report / arXiv 2025.
- Status: technical report / grey literature; not a peer-reviewed conference or journal paper.
- Venue verification: arXiv 2504.00698 and Cohere technical report PDF.
- Citation caution: cite as technical report, mostly for system/deployment examples, not as independent scientific proof.

### Core idea
Command A is an enterprise-oriented LLM designed for RAG, tool use, multilingual business use, long context, safety, and agentic workflows. The report describes the model architecture, pretraining, post-training, expert merging, RL, self-refinement, and evaluation.

### Key contribution
The key value for your review is not a single algorithm but an industrial blueprint: enterprise LLMs are being optimized specifically for RAG, tool use, agents, multilinguality, and efficient deployment. Command A reports a 111B parameter model and Command R7B, with support for 23 business languages and efficient serving claims.

### Method / approach
The report describes a decoder-only transformer with interleaved sliding-window and full attention, grouped-query attention, large multilingual tokenizer, long-context training stages, and a decentralized post-training pipeline. Post-training includes expert models for code, safety, RAG, math, multilingual, long-context, and instruction-following, then model merging and polishing.

### Key findings
The report claims strong performance on enterprise-relevant tasks, RAG, tool use, agentic benchmarks such as TauBench and BFCL, multilingual benchmarks, code, and long-context evaluation. It also emphasizes on-prem/enterprise efficiency and serving footprint.

### Limitations
This is a company technical report with potential commercial bias. The evaluation is not fully independent, and many training/data details are not reproducible. It should be separated from peer-reviewed literature.

### Relevance to thesis
Command A is useful grey literature showing that industry is converging on the same capabilities your thesis studies: RAG, tool use, agentic workflows, multilinguality, long context, safety, and enterprise deployment. It supports the practical relevance of web automation and extraction.

### How to use it in S2 or grey-literature section
Use it in a small “industrial systems and grey literature” paragraph or table, not as core academic evidence.

### Connects to
- S2: modern LLM capabilities
- S3: tool/agent systems
- S5.4: post-training pipelines
- S8: deployment constraints

### Sentence to add later
Enterprise technical reports such as Command A indicate that industrial LLM development is increasingly centered on RAG, tool use, agentic workflows, multilinguality, long context, and deployment efficiency, aligning with the practical requirements of web automation systems.

---

## 29. DeepSeek-R1 Thoughtology: Let's think about LLM reasoning

### Venue / Status
- Final venue: Transactions on Machine Learning Research, January 2026.
- Status: peer-reviewed journal article.
- Venue verification: OpenReview lists it as accepted by TMLR; PDF states “Published in Transactions on Machine Learning Research (01/2026).”
- Citation caution: safe to cite strongly, especially for reasoning-model limitations.

### Core idea
The paper systematically studies DeepSeek-R1’s reasoning chains, calling this analysis “Thoughtology.” It analyzes reasoning structure, thought length, long-context behavior, context faithfulness, safety vulnerabilities, cultural differences, human-like processing, and visual reasoning.

### Key contribution
The paper provides a detailed taxonomy of large reasoning model behavior. It identifies stages such as problem definition, blooming cycle, reconstruction cycles, and final decision. It also introduces the important idea that there is a “sweet spot” of reasoning length: more thinking is not always better.

### Method / approach
The authors analyze DeepSeek-R1 outputs across tasks including math, long-context recall, context faithfulness, harmful QA, moral reasoning, multilingual/cultural prompts, psycholinguistic stimuli, and visual/physical reasoning. They annotate reasoning chains and study length, rumination, and performance relationships.

### Key findings
DeepSeek-R1 often reasons through decomposition and repeated reconstruction, but these reconstructions can become rumination. Longer reasoning can reduce performance beyond an optimal range. The model struggles with controlling thought length, can become overwhelmed by long contexts, and exhibits stronger safety vulnerabilities than its non-reasoning counterpart.

### Limitations
The study focuses heavily on DeepSeek-R1, so findings may not generalize to all reasoning models. Since reasoning chains are generated text, faithfulness remains uncertain. The paper is not about web agents directly, but its lessons transfer strongly to agent reasoning.

### Relevance to thesis
This paper is important for critiquing reasoning-heavy web agents. It shows that longer or more explicit reasoning is not automatically better and can introduce cost, rumination, safety vulnerabilities, and context overwhelm. For web extraction, reasoning must be bounded, evidence-grounded, and evaluated by outcome correctness.

### How to use it in S2
Use it near the end of S2 as a modern cautionary note on large reasoning models.

### Connects to
- S2: large reasoning models
- S5.3: planning and reasoning
- S7: safety risks
- S8: cost/energy metrics and thought budget

### Sentence to add later
DeepSeek-R1 Thoughtology shows that large reasoning models have a problem-specific “sweet spot” of reasoning and can suffer from rumination, context overwhelm, and safety vulnerabilities, cautioning against treating longer reasoning traces as inherently better for web agents.

---

# 4. Section-level synthesis to add to S2

## S2.1 Parametric knowledge is useful but insufficient

The LM-as-KB and closed-book QA papers should be used to make a compact argument: LLMs encode useful background knowledge, but this knowledge is prompt-sensitive, stale, and non-auditable. Jiang et al. show prompt choice changes apparent factual recall; Roberts et al. show closed-book QA scales with model size but lacks evidence access; AlKhamissi et al. summarize the missing KB properties of LMs: access, editability, consistency, reasoning, and explainability. This directly motivates retrieval and source grounding for web extraction.

Ready sentence:
> Early LM-as-knowledge-base work demonstrates that LLMs contain useful factual knowledge, but because this knowledge is prompt-sensitive, stale, difficult to edit, and not source-attributed, generalized web extraction cannot rely on parametric recall alone.

## S2.2 Grounding is a foundation, not an optional add-on

Experience Grounds Language, multimodal reasoning surveys, Video as Language, and VoT collectively support the claim that agents require grounded perception. For your thesis, the most important bridge is from world grounding to web grounding: web agents need to ground instructions and schemas in screenshots, DOM nodes, page layout, visual grouping, and action feedback.

Ready sentence:
> Grounding-oriented work argues that language understanding depends on perception, interaction, and environment feedback; in the web setting, this translates into grounding user goals and extraction schemas in DOM structure, screenshots, layout, and browser state transitions.

## S2.3 Reasoning is moving from CoT to structured, verifiable chains

Selection-Inference, SelfCheck, CoVe, CoV-RAG, RAT, Chain-of-X, BoT, Thinking LLMs, PRefLexOR, and DeepSeek-R1 Thoughtology show that the field is moving beyond simple CoT. The trend is toward modular reasoning, retrieval-augmented reasoning, verification, mistake correction, reusable thought templates, and inference-time scaling. However, DeepSeek-R1 Thoughtology and AI feedback evaluation papers show that reasoning and feedback can introduce cost, bias, rumination, and safety risks.

Ready sentence:
> Recent reasoning research has shifted from simple CoT prompting toward structured chains involving selection, retrieval, verification, feedback, and self-correction, but these mechanisms must be bounded and evidence-grounded because longer reasoning can increase cost, rumination, and safety risk.

## S2.4 Long context should be treated as an efficiency problem

AutoCompressors, Landmark Attention, LC-Boost, FreshLLMs, and Command A show different solutions to the context problem: learned compression, efficient attention, adaptive short-context access, search augmentation, and enterprise long-context post-training. For your thesis, the key point is that long context does not solve extraction by itself. Extraction needs exact source retention and field-level verification.

Ready sentence:
> Long-context research shows that larger windows, compression, and selective access can help process large inputs, but web extraction additionally requires retaining exact evidence locations for each field rather than only compressing pages into latent summaries.

## S2.5 Feedback and correction matter for training agents

Training with Language Feedback, AlpacaFarm, LEMA, AI Feedback evaluation, Thinking LLMs, PRefLexOR, and Command A all show different forms of feedback-based improvement. For web extraction agents, the most relevant form of feedback is not generic preference but structured correction: wrong field, missing record, wrong source, incomplete pagination, or unsafe action.

Ready sentence:
> Feedback-based training is increasingly central to LLM development, but web extraction requires task-specific correction signals—wrong fields, missing records, incorrect provenance, or failed navigation—rather than only generic preference judgments.

---

# 5. What to include in final thesis/survey from S2 P3

## Strongly include as academic support

- How Can We Know What Language Models Know?
- How Much Knowledge Can You Pack Into the Parameters of a Language Model?
- Experience Grounds Language
- Selection-Inference
- Adapting Language Models to Compress Contexts
- AlpacaFarm
- Random-Access Infinite Context Length for Transformers
- SelfCheck
- Chain-of-Verification
- FreshLLMs
- A Critical Evaluation of AI Feedback
- Chain-of-X Survey
- LM-Guided CoT
- Mind's Eye / VoT
- Buffer of Thoughts
- CoV-RAG
- Dyn-VQA / OmniSearch
- DeepSeek-R1 Thoughtology

## Include selectively / cite cautiously

- A Review on Language Models as Knowledge Bases
- Training Language Models with Language Feedback at Scale
- Learning From Mistakes Makes LLM Better Reasoner
- Exploring Reasoning Abilities of MLLMs
- Video as the New Language
- RAT
- Are Long-LLMs A Necessity?
- PRefLexOR
- Command A

## Best candidates to remove or footnote in ACM version if space is limited

- Video as the New Language: too physical-world focused.
- PRefLexOR: interesting but domain-specific and long.
- Command A: grey literature; useful in ecosystem table only.
- MLLM reasoning survey: broad survey, can be replaced by more direct web-perception papers.
- Learning From Mistakes / Training Language Feedback: useful but preprint; use only if training subsection needs extra support.

---

# 6. Final critique for S2 integration

The S2 P3 batch is useful, but it should not make S2 longer. Most of these papers are supporting foundations, not central web-agent papers. Use them to sharpen the theoretical base, then move quickly toward web-agent-specific sections.

The best revised S2 structure after incorporating P3 is:

1. LLMs as parametric knowledge stores and their limits
2. Instruction following, alignment, and feedback learning
3. Reasoning beyond CoT: decomposition, verification, and correction
4. Retrieval, freshness, and source grounding
5. Long-context processing and selective access
6. Multimodal/spatial grounding for interactive agents
7. Open foundation gap: LLM capabilities are necessary but insufficient for generalized web extraction

Most important message to preserve:

> LLMs provide the linguistic, reasoning, and instruction-following substrate for web agents, but generalized web data extraction requires capabilities that base LLMs do not guarantee: grounded perception, adaptive retrieval, explicit verification, source attribution, structured output control, and cost-aware operation.

