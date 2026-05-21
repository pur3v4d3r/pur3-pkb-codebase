---
title: Checklist_(C.A.W.)
aliases:
  - Reference_Checklist_Gemini-2.5-Flash_CAG
  - CAG Step-by-Step
  - Cognitive Augmentation Checklist
  - Workflow Verification Guide
tags:
  - prompt-engineering
  - project/prompt_engineering
status: 🪴 seedling
created: 2025-10-09T05:20:35.564Z
updated: 2025-10-09T06:02:49.421Z
source: "[Gemini-2.5-Flash]"
related:
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[report_the-cognitive-augmentation-workflow_(c.a.w.)]]"
date created: 2025-10-09T01:20:35.000-04:00
date modified: 2025-10-10T00:20:37.233-04:00
---

# Reference_Checklist_Gemini-2.5-Flash_CAG

> [!the-purpose]
> - Here is a comprehensive checklist, structured by the four phases, to guide you through the **Cognitive Augmentation Workflow**. I've designed it to be used as a step-by-step verification tool for each research note you generate.

---

## Personal Knowledge Base Reference Note: The Cognitive Augmentation Workflow Checklist

> [!the-philosophy]
> - This checklist is a mandatory reference guide for transforming LLM outputs into high-utility, trustworthy scholarly assets within the Obsidian Personal Knowledge Base (Personal Knowledge Base). Follow these steps sequentially to maximize intellectual depth, verifiability, and long-term conceptual synthesis.

---

### **Phase I: Architectural Scaffolding (Preparation & Structure)**

Before generating content, the system must be prepared to receive, track, and manage trustworthiness.

#### **✅ 1. Implement Mandatory Front Matter (YAML) Schema**

**Mandate:** Ensure the following fields are present in the YAML block of the resulting note to transform the Personal Knowledge Base into a "Trust Ledger."

| Field Name | Data Type | Requirement | Actionable Checklist |
| :--- | :--- | :--- | :--- |
| `ai_source_model` | String | **Mandatory** | `[ ]` Record the specific LLM/Agent used (e.g., `GPT-4o-AMPF`). |
| `gen_date` | Timestamp | **Mandatory** | `[ ]` Record the exact timestamp of content generation. |
| `coherence_score` | Decimal (0.0-1.0) | **Mandatory** | `[ ]` Record the score for thematic and logical consistency (from LLM-as-a-judge/DeepEval). |
| `semantic_density` | Decimal (0.0-1.0) | **Mandatory** | `[ ]` Record the metric for evidential depth/trustworthiness. |
| `citation_check_status` | Enum | **Mandatory** | `[ ]` Initial Status: `Pending` or `RAG-Grounding`. Must be updated to `Verified` post-audit. |
| `data_provenance_method` | String | **Mandatory** | `[ ]` Record the generation process (e.g., `Meta Prompting`, `RAG-enabled`). |
| `is_contradictory` | Boolean | *Optional* | `[ ]` Use this flag if the note was intentionally generated to capture an opposing argument for the CMS. |
| `parent_hypothesis` | Link/String | *Optional* | `[ ]` Link the note to the initiating research question or hypothesis. |

#### **✅ 2. Conceptual Coherence & Linking Preparation**

| Task | Actionable Checklist |
| :--- | :--- |
| **Zettelkasten Atomic Principle** | `[ ]` Ensure the prompt directs the LLM to output content that can be easily parsed into atomic notes (single idea per note). |
| **Heterarchical Linking** | `[ ]` Design the prompt to generate complex relationship mapping to support web-like (`heterarchical`) links, not just simple hierarchical (`tree-based`) structures. |
| **Contradiction Management System (CMS)** | `[ ]` If relevant, prepare to create an `is_contradictory: true` note to deliberately capture an opposing viewpoint. |

---

### **Phase II: Generative Execution (The AMP-F Prompt)**

The prompt must transition from simple input to the structured **Agentic Meta-Prompting Framework (AMP-F)**.

#### **✅ 3. Structure the Meta-Prompt (AMP-F)**

| Layer/Role | Actionable Checklist |
| :--- | :--- |
| **System Role** | `[ ]` Define a precise persona (e.g., "Highly Accomplished Research Director specializing in X"). |
| **System Role** | `[ ]` Define all non-negotiable global constraints (tone, output style, minimum factual density). |
| **Conductor LLM** | `[ ]` Explicitly instruct the Conductor to employ a **Tree-of-Thoughts (ToT)** strategy for exploration and self-evaluation. |
| **Expert LLMs** | `[ ]` Instruct specialized agents for tasks like **Retrieval Augmented Generation (RAG)** lookups and counter-argument generation. |
| **Output Layer** | `[ ]` Mandate the final output format: Markdown with the precise YAML structure defined in Phase I. |

#### **✅ 4. Constraint and Grounding Mandates**

| Constraint Type | Actionable Checklist |
| :--- | :--- |
| **RAG Grounding** | `[ ]` Specify the curated, proprietary vector database as the *only* acceptable source for factual claims requiring citation. |
| **Positive Constraints** | `[ ]` Prioritize *positive* phrasing (e.g., "Must cite all RAG context") over negative phrasing (e.g., "Do not plagiarize"). |
| **Citation Integration** | `[ ]` Instruct the RAG-enabled LLM to cite claims using the internal document index (e.g., `[j]`) for later automated checking. |

---

### **Phase III: Validation and Rigor Assessment (Quantification)**

This phase is critical for moving the note from speculative text to a reliable, scholarly asset.

#### **✅ 5. Score and Flag the Note**

| Metric | Actionable Checklist |
| :--- | :--- |
| **Metric Logging** | `[ ]` Record the **Coherence Score** and **Semantic Density (SD)** in the note's Front Matter. |
| **Rigor Threshold** | `[ ]` If the **Semantic Density** score is below your defined threshold (e.g., `< 0.8`), immediately flag the note for **extensive human verification.** |

#### **✅ 6. Execute the Citation Rigor Protocol (Human Audit)**

| Step | Actionable Checklist |
| :--- | :--- |
| **Automated Check** | `[ ]` (System Check) Confirm the internal citation link points back to a verifiable RAG document. |
| **Selective Human Audit** | `[ ]` Manually verify all high-impact or suspicious claims against the *original source text*. |
| **Metadata Update** | `[ ]` **Crucial:** Only after the manual audit is complete, update the Front Matter field to `citation_check_status: Verified`. |

---

### **Phase IV: Conceptual Integration and Synthesis (Active Learning Loop)**

This phase converts the explicit LLM knowledge into durable, tacit knowledge and drives continuous learning.

#### **✅ 7. Perform the After Action Review (AAR)**

| AAR Question | Actionable Checklist |
| :--- | :--- |
| **Intended vs. Actual** | `[ ]` Document the intended outcome (from the Meta Prompt). |
| **Intended vs. Actual** | `[ ]` Document the actual outcome (report content and metrics). |
| **Cause of Difference** | `[ ]` Analyze what caused any gap (e.g., low SD, RAG failure, misinterpreted constraint). |
| **Next Iteration** | `[ ]` Determine what must be modified in the next prompt or workflow iteration. |

#### **✅ 8. Final Personal Knowledge Base Integration**

| Task                | Actionable Checklist                                                                                                                                            |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zettel Creation** | `[ ]` Break down the LLM report content into **atomic notes** (single idea, unique identifier).                                                                 |
| **Deep Linking**    | `[ ]` Create robust internal links, connecting the new atomic note to at least two existing concepts in your Personal Knowledge Base.                                               |
| **Knowledge Gaps**  | `[ ]` Create a dedicated **"Knowledge Gap Note"** to capture information the LLM failed to query or synthesize (from AAR).                                      |
| **Reconciliation**  | `[ ]` If the note was `is_contradictory: true`, create a **"Contradiction Synthesis Note"** that captures your meta-level resolution of the opposing arguments. |
| **Application**     | `[ ]` Based on the AAR and synthesis, formulate a new hypothesis or prompt (to immediately initiate the next AMP-F cycle).                                      |
