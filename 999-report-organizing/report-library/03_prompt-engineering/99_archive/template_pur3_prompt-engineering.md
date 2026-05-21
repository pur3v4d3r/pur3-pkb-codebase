---
title: <% tp.file.title %>
id: <% tp.date.now("YYYYMMDDHHmmss") %>
aliases:
  - prompt-engineering
type: <%* const type = tp.file.title.split('_')[0].split(' ')[1]; tR += type %>
created: <% tp.date.now("YYYYMMDDHHmmss") %>
url: 
tags:
  - prompt-engineering
summary: 
model-parameters: 
version: 
success-rating:
output-link: 
---

# <% tp.file.title %>

> [!the-purpose]
> **Purpose:** A brief, one-sentence description of what this  <% tp.frontmatter.type %> does.
> *Example: This Gem generates a detailed academic analysis of a scientific paper.*

> [!important] Core Components & Metadata
>- **Model:** `model:: <%* const model = tp.frontmatter.model; if (model) { tR += `[[${model}]]`; } %>`
>- **Primary Goal:** `summary:: <% tp.frontmatter.summary %>`
>- **Topic Area:** `topic:: <%* const topic = tp.frontmatter.topic; if (topic) { tR += `[[${topic}]]`; } %>`
>- **ID:** `id:: <%* const emoji = tp.file.title.split('_')[0].split(' ')[0]; const id = tp.file.title.split('_').pop(); if (emoji && id) { tR += `${emoji}_${id}`; } %>` 
>- **Version:** `version:: <%* if (tp.frontmatter.type === "Gem") { tR += "v" + tp.frontmatter.version; } %>` 
>- **Status:** `status:: <%* const status = tp.frontmatter.status; if (status) { tR += `[[${status}]]`; } %>` 

---
# <% tp.file.title %>

```prompt
---
id: prompt-block-<% tp.file.title.split('_').pop() %>
---

PASTE YOUR PROMPT OR GEM INSTRUCTION SET HERE

```

## ✍️Usage Notes & Context

- **Required Context:** What information must be provided for this prompt to work effectively? 
	
	1. 
	2. 

- **Variables:** Are there any placeholders like `{TOPIC}` or `{TONE}` that need to be replaced?
	
	1. 
	2. 

# ⌛Iteration & Test Log


## v1.0 (Initial Draft) - <% tp.date.now("YYYY-MM-DD") %>

### **Result Quality (1-5):**

- [ ] Result: 1/5
- [ ] Result: 2/5
- [ ] Result: 3/5
- [ ] Result: 4/5
- [ ] Result: 5/5

### **Observations:** What worked well? What failed?

1. 
2. 

### **Changes for next version:**

1. 
2. 

---

# 📋Execution Checklist: Deep Prompt Engineering and Curation

## 🔧1.0 Dynamic Progress Dashboard (Incomplete Steps)

```dataview
TASK
FROM "<% tp.file.path(true) %>"
WHERE !completed
  AND contains(text, "#sop/")
SORT line ASC
LIMIT 100
```

---

## ✅ 2.0 Master Task List (The Source of Truth)

**Phase 1.0:** *Strategic Preparation (Discovery & Intent)*
  - [ ] `P1/S1.0` Intent & Context: Define the specific knowledge artifact being created (e.g., Atomic Note on X). #workflow
  - [ ] `P1/S1.0` Contextualization: Identify and select existing PKB notes to serve as contextual grounding data for the prompt (RAG). #workflow
  - [ ] `P1/S1.1` Role Structuring: Assign the prompt a detailed Role (e.g., specialized scientist) and Tone. #workflow
  - [ ] `P1/S1.1` Constraint Setting: Define explicit Constraints (e.g., word count, reading level, citation requirements). #workflow
  - [ ] `P1/S1.1` Output Schema: Demand the output in a precise, structured data format (e.g., JSON/YAML/specific Markdown). #workflow

**Phase 2.0:** *Generative Iteration (Capture & Refinement)***
  - [ ] `P2/S2.0` CoT Prompting: Embed mandatory Chain-of-Thought (CoT) instructions (e.g., "First, Define... Second, Analyze..."). #workflow
  - [ ] `P2/S2.0` Temperature Check: Select and register the appropriate Temperature setting in the YAML header (e.g., 0.1 for fact). #workflow
  - [ ] `P2/S2.1` Initial Assessment: Check the first generation for Accuracy, Relevance, Format, and Completeness. #workflow
  - [ ] `P2/S2.1` Refinement Cycle: If deficient, Refine the Prompt (not the output text) and re-test. #workflow
  - [ ] `P2/S2.1` Complexity Check: If refinement is excessive, implement Sequential Prompts (break into smaller queries). #workflow

**Phase 3.0:** *Curatorial Validation (Organize & Critique)*
  - [ ] `P3/S3.0` Factual Verification: Manually validate all key factual assertions against trusted external sources. #workflow
  - [ ] `P3/S3.0` Source Traceability: Trace and verify the legitimacy and currency of any LLM-cited sources. #workflow
  - [ ] `P3/S3.1` Adversarial Critique: Generate a second prompt to challenge the output's integrity (e.g., check for bias or counter-arguments). #workflow
  - [ ] `P3/S3.2` Quality Scoring: Assign a definitive success_rating (0-5) in the YAML front matter. #workflow
  - [ ] `P3/S3.2` Meta-Data Registration: Ensure all tracking parameters (model, etc.) are filled in the YAML. #workflow

**Phase 4.0:** *Assimilation & Synthesis (Use & Optimize)*
  - [ ] `P4/S4.0` Atomic Decomposition: Break the validated output into concise, granular Atomic Notes (Zettels). #workflow
  - [ ] `P4/S4.0` Linking: Link each new note (via bidirectional links) to at least three existing relevant concepts. #workflow
  - [ ] `P4/S4.1` Structured Assimilation: Integrate the new notes into an existing Map of Content (MOC), or create a new MOC. #workflow
  - [ ] `P4/S4.2` Deep Synthesis: Perform deep synthesis (e.g., Feynman Technique) on the new knowledge. #workflow
  - [ ] `P4/S4.2` Actionable Application: Extract at least one verb-first, actionable task from the content. #workflow
  - [ ] `P4/S4.2` Review Scheduling: Set the review_date property in the YAML front matter for spaced repetition. #workflow

---