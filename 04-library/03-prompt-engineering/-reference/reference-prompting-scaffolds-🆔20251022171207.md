---
title: Reference_Prompting-Scaffolds_🆔20251022171207
id: 20251022171224
aliases:
  - ai/note
  - ai/educational
  - llm/prompt-engineering
  - education/llm/prompting
  - llm/prompting
type: ⚙️reference
status: 🔍⁉️needs-review
priority: 🔼medium
created: 2025-10-22T17:12:24
source: 🦈ChatGPT
url: https://chatgpt.com/c/68f8852f-eba4-832b-bb23-d9099189e92d
tags:
  - prompt-engineering
  - llm
  - prompt-engineering
  - prompt-engineering
  - prompt-engineering/educational
  - prompt-engineering
---
# Prompting Scaffolds & Frameworks — Master Reference (2025-10-22)

> [!the-purpose] 
> **What this note is**
> A PKB-ready, living catalogue of the most useful **prompting / context-engineering scaffolds**. It blends peer-reviewed methods with widely-adopted practitioner frameworks, each given a compact “technique card,” persona and task frames you can paste into `[[obsidian]]`, and links to source literature for verification and deeper study.

---

## Plan of Attack (Deconstruct → Research → Synthesize → Compose)

> [!plan] **How I built this**
> **Deconstruct.** I mapped the space into families: Reasoning & Search; Planning & Decomposition; Acting with Tools; Retrieval & Grounding; Critique & Verification; Structured Output & Guardrails; Community prompt patterns.
> **Research.** I pulled primary papers and official docs for each family (arXiv/NeurIPS/ICLR, Anthropic/OpenAI docs), favoring methods with reproducible gains or broad adoption. ([arXiv][1])
> **Synthesize.** I normalized each method into a **Technique Card** (what/why/how + best practices), plus drop-in scaffolds and persona frames.
> **Compose.** Everything here is **PKB-ready Markdown** with `[[wiki-links]]`, callouts, and a small `mermaid` map to keep it navigable.

---

## Literature & Source Backbone (for verification)

> [!abstract] **Core references (representative, not exhaustive)**
> • **RAG** (retrieval-augmented generation): Lewis et al. (NeurIPS 2020). ([arXiv][1])
> • **ReAct** (reason+act loops): Yao et al. (ICLR 2023).
> • **Chain-of-Thought** (CoT): Wei et al. (2022). **Self-Consistency**: Wang et al. (ICLR 2023). ([arXiv][2])
> • **Tree-of-Thoughts** (ToT) and **Graph-of-Thoughts** (GoT): 2023–2024. 
> • **Self-Ask with Search** (decomposed Q→sub-Q): Press et al. (EMNLP Findings 2023). ([arXiv][3])
> • **Least-to-Most Prompting** (LtM): Zhou et al. (ICLR 2023). ([arXiv][4])
> • **Reflexion** (self-reflection RL without weight updates): Shinn et al. (2023/2024). ([arXiv][5])
> • **PAL / PoT** (program-aided reasoning): Gao et al. (2022/2023). ([arXiv][6])
> • **HyDE** (hypothetical documents for retrieval): Gao et al. (2022), plus practical docs. ([arXiv][7])
> • **Constitutional AI** (principle-guided self-critique): Anthropic research posts (2022–2024+). ([Anthropic][8])
> • **Structured Output / Function Calling** (schema-guided generation): OpenAI docs. ([OpenAI Platform][9])
> • **Guardrails** (Llama Guard; policy classifiers): Meta/FAIR (2023). ([arXiv][10])



>
>
>



>[!definition]
> Contents
---

## Visual Map of the Space

```mermaid
mindmap
  root((Prompting & Context Engineering))
    Reasoning & Search
      CoT
      Self-Consistency
      Self-Ask
      ToT
      GoT
    Planning & Decomposition
      Least-to-Most
      Plan-and-Solve
      ReWOO
    Acting w/ Tools
      ReAct
      Function Calling
      PAL / PoT
    Retrieval & Grounding
      RAG
      HyDE
      Self-RAG*
    Critique & Verification
      Reflexion
      Chain-of-Verification*
      Multi-Agent Debate*
      Constitutional AI (style)
    Structured Output & Guardrails
      JSON/Schema
      Llama Guard
      Checklists/Rubrics
```

> [!note] *Asterisks mark areas with multiple competing variants or active research lines; your `[[obsidian]]` notes can branch these further.*

---

# Drop-in Scaffolds (Paste into your prompts)

```markdown
## Scaffold (ReAct-Loop)

**THINK-1**: Draft a brief plan; list unknowns.  
**ACT-1**: Call tools or search to resolve top unknown.  
**OBSERVE-1**: Integrate results; update plan.  
**THINK-2**: Expand reasoning; check against success criteria.  
**ACT-2**: Fill remaining gaps via tools.  
**OBSERVE-2**: Consolidate evidence; prepare candidate draft.
```

```markdown
## Task Frame (SCQA-T)

**Situation**: Summarize the user’s context and objective in 2–3 sentences.  
**Complication**: Name the key uncertainty, constraint, or risk.  
**Question**: State the central question(s) to be answered.  
**Answer Plan**: Outline the method and checkpoints.  
**Tools**: List allowed tools/functions and selection heuristics.  
**Success Criteria**: Define verifiable deliverables, format, and evaluation rubric.
```

```markdown
# Persona Card: 
**Persona Name:** {{*Insert Persona Name Here*}}

## Role
**You are** {{*Insert The defined Role of the Persona*}}

## Directive
**Default to the method:** {{*Insert Method of Approach to Data and/or Information*}}

## Constraints
**You Do not** {{*Insert any constraint you want the persona to follow*}}
```

> [!tip] **Paste-ready**: Combine a **Persona Card** + **SCQA-T** + one **Technique Card** below to build robust, reusable prompts.

---

# Technique Cards (what it is • how it works • how to use)

> [!hint] **Format**
> *Technique:* `[[Name (Acronym)]]`
> *Description:* 4–5 sentences on mechanism and use.
> *Best Practices:* Concrete heuristics you can operationalize.

---

## Reasoning & Search

```
**Technique:** `[[Chain-of-Thought (CoT)]]`
**Description:** CoT elicits step-by-step intermediate reasoning before the final answer, improving performance on arithmetic, commonsense, and symbolic tasks. It works by **demonstrating** or **requesting** explicit reasoning traces, letting the model decompose a problem into atomic steps. Zero-shot CoT can be triggered with instructions like “Let’s think step by step,” while few-shot CoT seeds the pattern with exemplars. CoT is foundational and composes with most other scaffolds.
**Best Practices:** Use **few-shot** exemplars that mirror target difficulty; include **success criteria** and units; cap reasoning length; combine with **self-consistency** for robustness.
```

```
**Technique:** `[[Self-Consistency (SC)]]`
**Description:** Rather than trusting a single chain, SC samples **multiple reasoning paths**, then **majority-votes** the final answer by marginalizing over chains. This stabilizes brittle single-trajectory errors and boosts accuracy across GSM8K, SVAMP, StrategyQA, etc. SC is a **decoding strategy**, not a prompt; pair it with CoT prompts. ([arXiv][2])
**Best Practices:** Generate 5–20 independent chains with mild temperature; majority-vote the **final answer** (not the paths); filter obviously invalid units before voting.
```

```
**Technique:** `[[Self-Ask with Search]]`
**Description:** The model first **asks itself** sub-questions (Q→q₁…qₙ), answers them (optionally via a search tool), then composes a final answer. This narrows the “compositionality gap” by enforcing modular reasoning. It’s a structured prompt pattern that plays well with external search. ([arXiv][3])
**Best Practices:** Constrain sub-question count; define which sub-Qs **must** hit tools; log citations per sub-Q; end with a **synthesis** that cites supporting sub-answers.
```

```
**Technique:** `[[Tree-of-Thoughts (ToT)]]`
**Description:** ToT generalizes CoT from a single chain to a **search over multiple thought branches** with lookahead and backtracking, guided by an evaluator. It shines where early choices strongly affect outcomes (planning, puzzles). Expect higher cost than single-chain CoT due to branching. 
**Best Practices:** Limit branching factor & depth; score partial thoughts against a rubric; prune aggressively; checkpoint intermediate states you could reuse.
```

```
**Technique:** `[[Graph-of-Thoughts (GoT)]]`
**Description:** GoT replaces trees with **arbitrary graphs** of thoughts, allowing merges, re-use, and feedback cycles. It improves tasks like sorting and complex synthesis by **linking** and **ranking** thought nodes with evaluators. Best for multi-source synthesis and workflows that benefit from DAG-like reuse. 
**Best Practices:** Model thoughts as nodes with typed edges (supports/contradicts/depends); attach evaluators; periodically **distill** subgraphs into summaries to control context bloat.
```

---

## Planning & Decomposition

```
**Technique:** `[[Least-to-Most Prompting (LtM)]]`
**Description:** LtM decomposes a complex task into a **curriculum of simpler sub-tasks**, solving them sequentially from easy→hard. Each solved sub-step informs the next, enabling generalization to problems **harder** than the examples given. Excellent for compositional math/program transformations. ([arXiv][4])
**Best Practices:** Force the model to **list sub-problems** first; pin the **ordering**; cache outputs of early steps; keep each step’s acceptance criteria crisp.
```

```
**Technique:** `[[Plan-and-Solve / ReWOO-style]]`
**Description:** Variants like Plan-and-Solve or ReWOO separate **planning**, **evidence gathering**, and **final writing**. The model **plans first**, then executes tool calls, then drafts with citations. This separation reduces tool thrashing and hallucination. ([arXiv][11])
**Best Practices:** Freeze the plan before tools; log each retrieval with purpose; require a post-hoc **evidence table** prior to the final answer.
```

---

## Acting with Tools & Code

```
**Technique:** `[[ReAct]]`
**Description:** ReAct interleaves **reasoning tokens** (“Thought: …”) with **action tokens** (“Action: Search[…]”) and **observations**, producing a readable trace and tighter tool coupling. It is a robust default for agentic tasks that require alternating **thinking and doing**.
**Best Practices:** Keep a fixed syntax (`Thought/Action/Obs`); constrain allowed tools and selection rules; add a “Stop if success criteria met” guard.
```

```
**Technique:** `[[Function Calling / Tools (Structured APIs)]]`
**Description:** Modern APIs let you specify **JSON-schema-like tool signatures**; the model decides when to call them and must return **schema-valid** JSON. This enforces structure, improves reliability, and supports multi-tool workflows and “Agents” patterns. ([OpenAI Platform][9])
**Best Practices:** Design **narrow, single-intent** tools; include **selection heuristics** in the prompt; require a **final natural-language summary** after all tool calls.
```

```
**Technique:** `[[PAL (Program-Aided LMs) / PoT]]`
**Description:** Offload arithmetic/logic to a **Python interpreter** (or other runtime). The model writes small, executable programs as the reasoning substrate, then reports results. This reduces logical slips versus free-text CoT. ([arXiv][6])
**Best Practices:** Enforce **pure functions** with clear IO; run then **explain**; store code + output snippets in `[[obsidian]]` for reproducibility.
```

---

## Retrieval & Grounding

```
**Technique:** `[[RAG (Retrieval-Augmented Generation)]]`
**Description:** Combine a parametric LM with **non-parametric memory** via dense retrieval, feeding passages into the context window to ground answers and provide provenance. RAG improves specificity and factuality on knowledge-intensive tasks and remains the canonical grounding pattern. ([arXiv][1])
**Best Practices:** Normalize queries; **de-dupe** similar chunks; enforce a **cite-then-write** loop; add a **“No evidence → say so”** clause.
```

```
**Technique:** `[[HyDE (Hypothetical Document Embeddings)]]`
**Description:** Before retrieval, prompt the model to write a **hypothetical answer document**, embed that document, and use it to retrieve real neighbors; average multiple hypotheticals for robustness. HyDE is powerful for **zero-shot** retrieval in new domains. ([arXiv][7])
**Best Practices:** Generate 3–5 hypotheticals; **average** embeddings; keep hypotheticals concise and on-topic to avoid drifting retrieval.
```

> [!warning] **On Self-RAG / Corrective-RAG**
> Research-grade variants that add **critique/retrieve/rewrite** cycles or retrieval **self-grading** can reduce hallucinations, but require extra plumbing. Treat them as extensions to your base `[[RAG]]` note and log settings as part of your SOPs.

---

## Critique, Verification & Multi-Agent Patterns

```
**Technique:** `[[Reflexion]]`
**Description:** Agents generate outcomes, **reflect** on feedback (scores or free-form critique), store a **verbal memory**, then redo the task leveraging that memory. It’s like lightweight RL where the “policy update” lives in **language** rather than weights. Works well for coding and game-like tasks. ([arXiv][5])
**Best Practices:** Bound episodes; structure reflection prompts (“What went wrong? Why? Fix?”); persist **episodic memory** per task family.
```

```
**Technique:** `[[Constitutional AI (Prompt-Style Variant)]]`
**Description:** Although originally a **training** method, you can adapt the idea at prompt-time: provide a short **constitution** of principles, ask the model to **self-critique** an answer against them, then revise. It yields safer, more policy-consistent outputs. ([Anthropic][8])
**Best Practices:** Keep the constitution 5–12 short clauses; separate **Draft → Critique → Revision**; require the critique to quote the clause it invokes.
```

```
**Technique:** `[[LLM-as-a-Judge / Rubric Grading]]`
**Description:** Use a second model (or pass) to **grade** an output against a rubric and request **targeted edits**. Works as a plug-in verifier and for A/B comparison. Pairs nicely with SCQA-T success criteria. (General evaluation pattern; numerous implementations in literature.)
**Best Practices:** Make rubrics **behavioral and measurable**; demand **evidence-linked** critiques; apply **edits-only** in the revision pass.
```

```
**Technique:** `[[Multi-Agent Debate / Deliberation]]`
**Description:** Spawn two or more agents with distinct priors or roles; have them **debate** with a moderator that enforces citation and resolution. Debate can surface blind spots and improve final answers on reasoning tasks. (Multiple 2023+ studies; outcomes task-dependent.)
**Best Practices:** Cap rounds (2–3); enforce **turn budgets**; require **final synthesis** that resolves conflicts or flags irresolvable disagreements.
```

```
**Technique:** `[[Chain-of-Verification (CoVe)]]`
**Description:** Add a final pass that **lists claims**, then **verifies** each against sources (or recalculates) before publishing. Reduces factual slips in long outputs. (Multiple implementations; closely related to “verify-then-write” like ReWOO.)
**Best Practices:** Require a **claims table**; re-query or re-compute **only** flagged claims; show a **diff** if any edits occur.
```

---

## Structured Output & Guardrails

```
**Technique:** `[[Structured Output (JSON/Schemas)]]`
**Description:** Constrain outputs to **schemas** (JSON, Pydantic-like) using models’ structured output modes; combine with **function calling** so tools consume outputs deterministically. This reduces post-processing and failure modes in automation. ([OpenAI Platform][9])
**Best Practices:** Provide the **exact schema**; add **enum** values and regexes; return a **human summary** alongside the JSON for review.
```

```
**Technique:** `[[Guardrails: Llama Guard / Policy Classifiers]]`
**Description:** Run prompts and/or model outputs through a **policy classifier** (e.g., Llama Guard) that maps them to safety taxonomies and allows/blocks based on risk. Use as **input filter**, **output filter**, or **advisor** in a chain. ([arXiv][10])
**Best Practices:** Log decisions with **taxonomy labels**; keep a **human-override** path; tune for your domain to reduce over-refusals.
```

---

## Practitioner Frameworks (community patterns you’ll see in the wild)

> [!info] These are not research papers but **widely used prompt shapes** that help you structure instructions and context. Treat them as **starter templates** you customize per task.

```
**Technique:** `[[CRISPE]]`
**Description:** A mnemonic frame: **Context, Role, Intent, Style, Persona, Examples**. It reminds you to specify **who** the model is, **what** to do, **how** to speak, and to ground with exemplars. Useful for instruction-following chats and content generation. (Community framework; origin varies.)
**Best Practices:** Keep each field to 1–3 sentences; never skip **Context** or **Examples**; finish with **Success Criteria** even if CRISPE doesn’t name it.
```

```
**Technique:** `[[RICCE / RICES / RICCE-T]]`
**Description:** Variants like **Role, Instructions, Context, Constraints, Examples** (+**Tone/Tests**) focus on **constraints** and **negatives** (“Do not …”), which reduces drift in long generations. Great for SOPs and templatized content. (Community framework.)
**Best Practices:** Write **“must/should/must-not”** lines; include **counter-examples**; add a **short checklist** the model must tick before finalizing.
```

```
**Technique:** `[[SCQA (Minto Pyramid)]]`
**Description:** Structure the narrative as **Situation → Complication → Question → Answer**, then attach a plan and rubric. SCQA turns vague asks into solvable tasks and pairs cleanly with any of the reasoning methods above.
**Best Practices:** Keep **Situation** factual; make the **Question** decision-ready; tie **Answer** to explicit deliverables and evaluation.
```

---

# Paste-Ready Examples (Persona + Frame + Technique)

> [!example] **Persona + SCQA-T + ReAct (tools)**
> Use this when you need **search/tool** work plus visible reasoning.

```markdown
# Persona Card:
**Persona Name:** Research Ops Engineer

## Role
**You are** a research operations engineer who turns ambiguous questions into tool-driven, evidence-based answers with citations.

## Directive
**Default to the method:** ReAct with SCQA-T; plan first, then act; always log tool I/O and sources.

## Constraints
**You Do not** invent citations; if no evidence, you say so and propose next steps.
```

```markdown
## Task Frame (SCQA-T)

**Situation**: The user needs an up-to-date overview of X.  
**Complication**: The domain changes rapidly; hallucination and stale sources are risks.  
**Question**: What are the most credible, recent sources and what do they say?  
**Answer Plan**: Use ReAct to search → shortlist → extract claims → synthesize with citations.  
**Tools**: Web search, PDF reader, calculator.  
**Success Criteria**: 5–8 high-quality citations; claim→source mapping; a concise final summary.
```

```markdown
*Technique:* `ReAct`
*Description:* Interleave "Thought", "Action(tool)", and "Observation" to plan, execute, and integrate evidence before drafting the final answer. Ideal for workflows that alternate search with synthesis. 
*Best Practices:* Fix the `Thought/Action/Observation` tags; decide tool selection heuristics; cap to 2–3 tool rounds; end with a verification sweep against the success criteria.
```

---

## More Technique Cards (compact set you can slot anywhere)

```
**Technique:** `[[Zero-Shot CoT (“Let’s think step by step”)]]` — Trigger CoT without exemplars; add **units and constraints** to reduce rambling.
```

```
**Technique:** `[[Algorithm-of-Thought (AoT)]]` — Prompt the model to follow algorithmic sketches (search, DP) rather than prose; good with code or PAL. (DeepMind 2023; see also ToT/GoT family.) ([Parametric Pro Consulting][12])
```

```
**Technique:** `[[Plan → Execute → Verify (PEV)]]` — Three-pass pattern where verification is an explicit checklist (CoVe-style). (Practice-driven; aligns with ReWOO.) ([OpenReview][13])
```

```
**Technique:** `[[JSON-First Answer]]` — Ask for a structured **decision record** first (schema), then the human-readable narrative. Reduces post-hoc parsing. ([OpenAI Platform][9])
```

```
**Technique:** `[[Safety Pass / Constitutional Critique]]` — Insert a short **principles** list, have the model critique its own draft, and revise. Useful in regulated content. ([Anthropic][8])
```

```
**Technique:** `[[Guarded I/O]]` — Run inputs/outputs through a **policy classifier**; block/soften high-risk content; log taxonomy labels. ([arXiv][10])
```

---

## Operational “How-To” Notes (turning methods into SOPs)

> [!tip] **Choosing a scaffold**
> Start simple (CoT → SC) → add **planning** (LtM) → add **tools** (ReAct/Function Calling) → add **grounding** (RAG/HyDE) → add **verification** (CoVe/Reflexion) → wrap with **schemas & guardrails** (JSON/Policies).

> [!example] **Minimal HyDE-RAG capture (for your vault)**
>
> 1. Generate 3 concise hypotheticals ≤200 words each; 2) embed & average; 3) retrieve top-k; 4) write with **inline citations**; 5) `Chain-of-Verification`. ([arXiv][7])

> [!warning] **Common failure modes**
> Over-branching (ToT/GoT) → cost blow-ups; missing **acceptance criteria** (LtM/Plan-and-Solve); unvalidated tool outputs (ReAct/PAL); schema drift (JSON/Functions) if enums/regex aren’t enforced.

---

## Reusable Snippets (drop into templates)

```markdown
> [!check] Acceptance Criteria
> - All numeric claims recomputed or cited.
> - Each section mapped to at least one source (or marked "no evidence").
> - Final JSON validates against schema; include human-readable summary.
```

```markdown
> [!quote] Constitution (short)
> 1) Be accurate and cite sources. 2) Avoid speculation; label uncertainty. 3) Prefer primary literature. 4) Respect safety guidelines. 5) If unsure, propose tests. 6) No fabricated citations.
```

```markdown
> [!summary] Self-Reflection (Reflexion)
> What failed? Why? What change will prevent recurrence next time? One concrete rule to add to memory.
```

---

## Cross-links (create these notes in your PKB)

`[[Chain-of-Thought (CoT)]]` • `[[Self-Consistency]]` • `[[Self-Ask with Search]]` • `[[Tree-of-Thoughts]]` • `[[Graph-of-Thoughts]]` • `[[Least-to-Most Prompting]]` • `[[Plan-and-Solve]]` • `[[ReWOO]]` • `[[ReAct]]` • `[[Function Calling / Tools]]` • `[[PAL / Program-of-Thoughts]]` • `[[RAG]]` • `[[HyDE]]` • `[[Reflexion]]` • `[[Constitutional AI (Prompt style)]]` • `[[LLM-as-a-Judge]]` • `[[Multi-Agent Debate]]` • `[[Chain-of-Verification]]` • `[[Structured Output (JSON/Schemas)]]` • `[[Guardrails / Llama Guard]]` • `[[SCQA]]` • `[[CRISPE]]` • `[[RICCE]]`

---

## Citations (anchor points for each family)

* RAG & grounding: Lewis et al., *Retrieval-Augmented Generation*, 2020. ([arXiv][1])
* CoT & SC: Wei et al., 2022; Wang et al., ICLR 2023. ([arXiv][2])
* ToT / GoT: Yao et al., 2023; Besta et al., 2024. 
* Self-Ask: Press et al., EMNLP Findings 2023. ([arXiv][3])
* LtM: Zhou et al., ICLR 2023. ([arXiv][4])
* Reflexion: Shinn et al., 2023/2024. ([arXiv][5])
* PAL / PoT: Gao et al., 2022. ([arXiv][6])
* HyDE: Gao et al., 2022; practical docs (Haystack). ([arXiv][7])
* Constitutional AI (prompt-style variant): Anthropic research posts. ([Anthropic][8])
* Structured outputs & tools: OpenAI docs (prompt engineering, advanced usage, agents). ([OpenAI Platform][9])
* Guardrails: Llama Guard (Meta). ([arXiv][10])
* SCQA (Minto Pyramid): Minto’s Pyramid Principle lineage.

> [!info] **Scope note**
> This note intentionally prioritizes **load-bearing methods** with research or wide adoption. If you want an **exhaustive** long-tail list (e.g., PromptBreeder/GRIPS/DSPy learning loops), say the word and I’ll add an appendix with implementation-level guidance and Obsidian templates.

---

### 🔗 Related Topics for PKB Expansion

* `[[RAG Architecture Patterns (Indices, Chunking, Caching)]]`
* `[[Evaluation Harnesses for Prompts (Rubrics, Benchmarks, Human-in-the-Loop)]]`
* `[[Agentic Workflows in Obsidian (Dataview logs, Reflexion memories)]]`

[1]: https://arxiv.org/abs/2005.11401 "[2005.11401] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
[2]: https://arxiv.org/abs/2203.11171 "[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models"
[3]: https://arxiv.org/abs/2210.03350 "[2210.03350] Measuring and Narrowing the Compositionality Gap in Language Models"
[4]: https://arxiv.org/abs/2205.10625 "[2205.10625] Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
[5]: https://arxiv.org/abs/2303.11366 "[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning"
[6]: https://arxiv.org/abs/2211.10435 "[2211.10435] PAL: Program-aided Language Models"
[7]: https://arxiv.org/abs/2212.10496?utm_source=chatgpt.com "Precise Zero-Shot Dense Retrieval without Relevance Labels"
[8]: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback?utm_source=chatgpt.com "Constitutional AI: Harmlessness from AI Feedback"
[9]: https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results?utm_source=chatgpt.com "Prompt engineering - OpenAI API"
[10]: https://arxiv.org/abs/2312.06674 "[2312.06674] Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations"
[11]: https://arxiv.org/abs/2310.06117?utm_source=chatgpt.com "Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models"
[12]: https://parametricpro.com/blog/scqa-framework?utm_source=chatgpt.com "The SCQA Framework"
[13]: https://openreview.net/pdf?id=_3ELRdg2sgI&utm_source=chatgpt.com "STaR: Self-Taught Reasoner"
