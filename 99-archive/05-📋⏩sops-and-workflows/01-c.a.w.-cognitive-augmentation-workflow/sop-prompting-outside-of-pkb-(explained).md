---
title: SOP_Deep-Prompt-Engineering-and-Curation_2025-10-09
aliases:
  - 4-Phase Prompt Engineering
  - AI Curation Workflow
  - Deep Prompt SOP
tags:
  - pkb
status: seedling
created: 2025-10-09T23:48:57.449Z
updated: 2025-10-09T23:51:06.193Z
source: "[Gemini-Deep-Research]"
related:
  - "[[📝Prompt_Refine-current-Workflow-into-Advanced-SOP_RCKAZZ7E9G]]"
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[📙🧠Report_Prompting_Outside-of-PKB]]"
date created: 2025-10-09T19:48:57.000-04:00
date modified: 2025-10-09T19:56:42.725-04:00
---

# SOP_Deep-Prompt-Engineering-and-Curation_2025-10-09

## 0.0 The Deep Prompt Engineering and Curation Standard Operating Procedure (4-Phase Model)

> [!the-purpose]
> This advanced Standard Operating Procedure reframes the process of utilizing generative AI into a structured, four-phase system: Strategic Preparation, Generative Iteration, Curatorial Validation, and Assimilation & Synthesis. This architecture aligns with established knowledge management principles (Discovery, Capture, Organize, Use, and Optimize) while prioritizing depth and critical review.15

### 0.1. Standard Operating Procedure Phase I: Strategic Preparation (Discovery & Intent)

> [!phase-one]
> This phase establishes the intellectual context and required structure before communicating with the LLM, treating the prompt as a schematic blueprint for the desired knowledge artifact.

#### Step 1.0: Intent Formulation and Personal Knowledge Base Contextualization

Action: The user must define the specific knowledge artifact being created (e.g., a permanent atomic note on a specific concept, a summary for a new Map of Content (MOC), or a comparative analysis). The prompt preparation should actively identify and select relevant existing Personal Knowledge Base notes to serve as contextual data or grounding material for the prompt.

WHY: This step prevents "generation drift," ensuring the output is immediately focused and connectable to the existing intellectual framework. Leveraging existing Personal Knowledge Base notes as context mirrors the Retrieval Augmented Generation (RAG) framework, extending the foundation model to use relevant sources outside its training data, which enhances factual relevance and transparency.17

#### Step 1.1: Advanced Prompt Structuring (Role, Constraint, and Output Schema)

Action: The prompt must employ advanced techniques such as Role Assignment (e.g., "Act as a specialized materials scientist and philosophical expert") to inject the required domain expertise and tone.10 Explicit constraints must be defined (e.g., word count limitations, reading difficulty level, specific required citations, or prohibition of passive voice). Crucially, the prompt must demand the output in a precise, structured data format (e.g., JSON or a specific Markdown structure) that mirrors the final Obsidian note template.

WHY: Prompt engineers require deep linguistic mastery to manage nuance, context, and phrasing.9 Specifying the output format forces the model away from verbosity and toward precision, making subsequent curation easier. Structured output generation (e.g., JSON/YAML) enhances the model's ability to follow complex constraints and ensures the content is immediately machine-readable and ready for Personal Knowledge Base integration.18

### 0.2 Standard Operating Procedure Phase II: Generative Iteration (Capture & Refinement)

> [!phase-two]
> This phase focuses on eliciting the best possible response through iterative and strategic communication with the model.

#### Step 2.0: Initial Generation with Chain-of-Thought (CoT) Prompting

Action: The user must embed mandatory Chain-of-Thought (CoT) instructions within the prompt. These instructions break down the complex task into verifiable, intermediate steps (e.g., "First, define the core variables. Second, analyze the causal relationship. Third, synthesize the conclusion"). The user must select and register the appropriate temperature setting (e.g., 0.1 for high determinism/fact retrieval; 0.7 for creative synthesis/analogy creation).20

WHY: CoT improves the model's language understanding and ability to achieve accurate, complex outputs by externalizing its reasoning process.9 Tracking the temperature is essential because LLM performance, even with advanced models, can vary significantly depending on this parameter. Understanding the impact of temperature allows the user to audit the content's volatility and ensures the prompt is optimized for either creative or factual tasks.20

#### Step 2.1: Iterative Refinement Cycle

Action: The generated content must be methodically assessed against four key criteria: Accuracy (factual correctness), Relevance (alignment with the initial intent), Format (adherence to the specified output schema), and Completeness (inclusion of all required constraints).21 If the output falls short—for instance, if it shows misinterpretations or missing details—the user must refine the prompt (not the output text) by adding constraints, clarifying terms, or providing additional context, then re-test.21 This process is repeated until criteria are consistently met.

WHY: Quality is achieved through structured experimentation and continuous feedback, transforming prompt engineering from a static task into a dynamic process.22 If this iterative refinement process proves excessively long, it is indicative that the initial Phase I design was flawed, or the single prompt was attempting to resolve too great a complexity. This failure signals the need to implement Sequential Prompts, breaking the complex query into smaller, manageable parts to ensure deeper clarity and successful execution.10

### 0.3. Standard Operating Procedure Phase III: Curatorial Validation (Organize & Critique)

> [!phase-three]
> This phase serves as the non-negotiable human quality gate, ensuring epistemic rigor before assimilation into the Personal Knowledge Base.

#### Step 3.0: Factual Verification and Source Traceability

Action: All key factual assertions, definitions, or numerical data within the generated output must be manually validated against trusted external sources. If the LLM was designed to cite its sources, the user must trace and verify the legitimacy and currency of those cited sources.17

WHY: Preventing the introduction of inaccurate information (hallucinations) is the primary objective of deep curation. The PKB’s value is predicated on holding distilled, verified knowledge.3

#### Step 3.1: Adversarial Critique (Bias and Integrity Check)

Action: The user must employ Adversarial Prompting as a critical quality assurance tool. This involves generating a second prompt designed specifically to challenge the first output's integrity. Examples include "Critically evaluate the preceding text for any underlying biases against," or "Generate an evidence-based counter-argument to the core claim of this text, focusing on rhetorical weaknesses".23 The LLM can also be directed to detect media bias or ethical vulnerabilities in its own content.12

WHY: Traditional adversarial techniques (jailbreaking, prompt injection) exploit model vulnerabilities to produce harmful content.11 In this deep curation process, the inverse application—the critique model—proactively tests the robustness and ethical alignment of the output, exposing weaknesses, logical fallacies, or undisclosed biases that might otherwise be integrated into the Personal Knowledge Base.26 The ability to generate a stylized, persuasive counter-argument demonstrates a superior level of critical understanding of the topic.23

#### Step 3.2: Human Quality Assessment and Meta-Data Scoring

Action: Following verification and critique, the user must assign a definitive critique_score (on a scale of 0 to 5) reflecting the content's factual accuracy, fulfillment of constraints, and integrity after the bias check.28 Simultaneously, all tracking parameters (model name, temperature, prompt status, prompt identifier) must be registered in the note's YAML front matter.

WHY: This step formalizes the knowledge into an auditable artifact. Quantifying quality provides data essential for future prompt optimization, allowing the user to filter high-quality notes using Dataview queries.28 Furthermore, tracking the llm_model and temperature is necessary documentation because LLM performance is known to be highly sensitive to model variations and configurations.19

### 04. Standard Operating Procedure Phase IV: Assimilation & Synthesis (Use & Optimize)

This final phase focuses on structuring the validated output into the Personal Knowledge Base, ensuring long-term retention, synthesis, and application. This stage is further elaborated in Section IV.

#### Step 4.0: Atomic Decomposition and Linking

Action: The highly refined and validated LLM output is broken down into concise, granular, and focused atomic notes (Zettels).6 Each resulting note is then linked (via bidirectional links) to at least three existing relevant concepts within the vault.

WHY: This enforces Zettelkasten principles, maximizing the modularity and reusability of the knowledge. Granular notes are easier to link and contribute directly to the emergent structure of the knowledge graph.5

#### Step 4.1: Structured Assimilation and MOC Creation

Action: The new atomic notes are immediately integrated into an existing Map of Content (MOC), or a new MOC is created if the emergent conceptual cluster warrants it.

WHY: MOCs provide structural flexibility, serving as curated hierarchical indexes over the free-form knowledge graph. This structure allows the user to navigate the knowledge using both bottom-up (atomic notes feeding the MOC) and top-down (MOC guiding future note creation) methodologies, optimizing both discovery and retrieval.30

#### Step 4.2: Actionable Application and Review Scheduling

Action: The user must perform deep synthesis (via the Feynman Technique—see Section IV) and extract at least one verb-first, actionable task from the synthesized content. The note must then be scheduled for future review using a specific review_date property.14

WHY: Knowledge is only truly internalized when it guides practical action and can be recalled efficiently. Scheduling reviews using spaced repetition counters the natural forgetting curve and ensures the knowledge remains evergreen and accessible.32
