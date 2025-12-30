---
title: Report_RAG-Augmented-Curation-Loop-(RACL)_API
aliases:
  - RACL API Specification
  - RACL Implementation Guide
  - RAG Workflow API
tags:
  - prompt-engineering
  - workflow
  - pkb
  - workflow
status: 🌱 seedling
created: 2025-10-10T01:23:58.988Z
updated: 2025-10-10T01:26:23.133Z
source: "[Gemini-2.5-Pro]"
related:
  - "[[📝Prompt_Imporve-existing-SOP-for-Semantic-Search_6LGNTFOTVN]]"
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
date created: 2025-10-09T21:23:58.000-04:00
date modified: 2025-10-09T21:35:01.426-04:00
---

# Report_RAG-Augmented-Curation-Loop-(RACL)_API

## Deliverable 1: The RAG-Augmented Curation Loop (RACL) Workflow

The RACL is an 8-phase workflow designed to operationalize your `REFERENCE SOP` directly within Obsidian. Each phase is a distinct step in the lifecycle of a knowledge artifact, from initial query to final assimilation.

---

### **Phase 1: RAG-Powered Contextualization**

* **Action:** Create a new, blank note. In this note, type your initial, high-level query or concept (e.g., "Analyze the primary critiques of the Zettelkasten method for creative writing"). The **Smart Connections** plugin will automatically populate its side panel with the most semantically relevant notes from your entire vault.
* **Maps to:** `Phase I, Step 1.0: Intent Formulation and Personal Knowledge Base Contextualization`.
* **Advancement:** This phase fully automates the context discovery process. Instead of manually searching for relevant notes, the RAG-based engine surfaces them for you, ensuring that even forgotten connections are brought forward as foundational context.
* **Plugin(s) & Justification:**
    * **Smart Connections:** **Non-negotiable.** This is the core RAG engine of the workflow. Its ability to perform semantic search is what automates context retrieval, fulfilling the primary mandate of the RACL.

---

### **Phase 2: Automated Prompt Assembly**

* **Action:** With your initial query typed, trigger a **QuickAdd** command (e.g., `Ctrl+Shift+P`). This command will capture your query and embed it within the **Master Prompt Template** (see Deliverable 3). The template automatically adds the role, constraints, Chain-of-Thought instructions, and the required YAML/Markdown output structure.
* **Maps to:** `Phase I, Step 1.1: Advanced Prompt Structuring` & `Phase II, Step 2.0: Initial Generation with CoT Prompting`.
* **Advancement:** This eliminates manual prompt construction. By using a template, you guarantee that every single query sent to the LLM adheres to your rigorous standards for role-playing, CoT reasoning, and structured output, preventing "lazy" prompting.
* **Plugin(s) & Justification:**
    * **QuickAdd:** **Non-negotiable.** It acts as the primary user interface for the workflow, capturing the user's intent and wrapping it in the complex prompt structure. This ensures consistency and dramatically reduces cognitive load.
    * **Templater:** **Non-negotiable.** It provides the dynamic logic for the prompt, inserting dates, cursor positions, and other variables, making the prompt a living, intelligent document.

---

### **Phase 3: Context-Aware Generation**

* **Action:** Copy the fully assembled prompt from the note. Open **Smart Chat**. Ensure the "context from current note" toggle is enabled. Paste the prompt and execute it. **Smart Connections** will automatically inject the relevant notes identified in Phase 1 as context for the LLM, right before executing your detailed instructions.
* **Maps to:** `Phase II, Step 2.0: Initial Generation`.
* **Advancement:** This step operationalizes the RAG framework. The LLM receives not only your expert-crafted prompt but also a payload of your own verified, personal knowledge, grounding the generation in your existing intellectual framework.
* **Plugin(s) & Justification:**
    * **Smart Chat / Smart Connections:** **Non-negotiable.** This combination is the heart of the generation engine, allowing the local LLM to receive both the sophisticated prompt (from QuickAdd/Templater) and the semantic context (from Smart Connections' RAG capability).

---

### **Phase 4: Structured Ingestion & Factual Verification**

* **Action:** Copy the LLM's structured Markdown output from Smart Chat and paste it into the note body, replacing the prompt text. The note now has a complete YAML frontmatter block and organized headers. Manually verify all key factual claims, statistics, and citations against trusted external sources.
* **Maps to:** `Phase III, Step 3.0: Factual Verification and Source Traceability`.
* **Advancement:** The LLM-generated output is already in the final note format, including the YAML needed for `Dataview`. This removes all friction related to reformatting and immediately presents the content in a "ready-to-critique" state.
* **Plugin(s) & Justification:**
    * **N/A:** This is a mandatory human-in-the-loop phase that cannot be automated. Its value lies in the researcher's critical judgment.

---

### **Phase 5: In-Situ Adversarial Critique**

* **Action:** Highlight a key claim or the entire generated text within the note. Use a secondary **QuickAdd** command or a dedicated **Smart Chat** prompt (e.g., "Critically evaluate the selected text for logical fallacies, unstated assumptions, and potential bias. Present a concise counter-argument."). Paste the critique back into the note under a temporary `## Adversarial Critique` section.
* **Maps to:** `Phase III, Step 3.1: Adversarial Critique`.
* **Advancement:** This brings the adversarial process directly into the note being curated. It's no longer an abstract external step but an integrated part of the document's history, allowing you to see the original generation and its critique side-by-side.
* **Plugin(s) & Justification:**
    * **Smart Chat:** **Non-negotiable.** It provides the interface to run the secondary, adversarial prompt against the initial output.
    * **QuickAdd (Optional but Recommended):** Can be used to store and quickly fire pre-defined adversarial prompts for consistency.

---

### **Phase 6: Finalization & Metadata Scoring**

* **Action:** Based on the factual verification (Phase 4) and the adversarial critique (Phase 5), complete the YAML frontmatter. Assign a `critique_score` from 0-5. Fill in the `llm_model`, `temperature`, and set a `review_date`. Delete the temporary adversarial critique section. The note is now a validated, auditable knowledge artifact.
* **Maps to:** `Phase III, Step 3.2: Human Quality Assessment and Meta-Data Scoring`.
* **Advancement:** This step transforms a qualitative assessment into quantitative, machine-readable data. The `critique_score` is not just a personal judgment; it is now a queryable data point for future analysis.
* **Plugin(s) & Justification:**
    * **Dataview:** **Non-negotiable.** While not active in this step, this entire phase is designed to produce clean YAML *for Dataview*. Without Dataview, the metadata scoring is unactionable. This step closes the quality loop.

---

### **Phase 7: Atomic Assimilation & Linking**

* **Action:** Review the finalized note. If it represents a single, cohesive idea, leave it as is. If it contains multiple concepts, decompose it into several atomic notes. In either case, link the note(s) to relevant concepts and Maps of Content (MOCs) using `[[bidirectional links]]`.
* **Maps to:** `Phase IV, Step 4.0: Atomic Decomposition and Linking` & `Step 4.1: Structured Assimilation`.
* **Advancement:** This is the core intellectual synthesis step, but it's made more efficient because the note is already validated, structured, and trustworthy. You can focus purely on connection and integration rather than cleaning up the content.
* **Plugin(s) & Justification:**
    * **Obsidian Core:** The platform's native linking functionality is all that is required.

---

### **Phase 8: Action & Review Automation**

* **Action:** Within the note, create at least one actionable task using the `Tasks` plugin format (e.g., `- [ ] Draft a counter-argument based on the new insights for Project X due:YYYY-MM-DD`). The `review_date` set in Phase 6 now automatically enrolls this note into your spaced repetition/review system.
* **Maps to:** `Phase IV, Step 4.2: Actionable Application and Review Scheduling`.
* **Advancement:** This makes knowledge immediately actionable. Using the `Tasks` plugin syntax makes the task discoverable across your entire vault. The `review_date` and `Dataview` combine to create an automated, dynamic review dashboard, ensuring no validated knowledge is ever lost to the forgetting curve.
* **Plugin(s) & Justification:**
    * **Tasks:** **Non-negotiable.** It transforms a line of text into a queryable, trackable task, integrating knowledge work with project management.
    * **Dataview:** **Non-negotiable.** It is the engine that reads the `review_date` and powers the automated review dashboard (e.g., a table of all notes where `review_date` is today).

***

## Deliverable 2: Plugin Implementation Strategy

This is integrated directly into the 8-Phase workflow above, with the "Plugin(s) & Justification" section for each phase explaining *why* each tool is critical to maintaining the integrity and efficiency of the loop.

***

## Deliverable 3: The Master Prompt Template

This is the parameterized text designed for use with **QuickAdd** and **Templater**.

**Instructions for Implementation:**
1. Save this entire code block as a new template file in your designated Templater folder (e.g., `Templates/RACL_Master_Prompt.md`).
2. Create a new **QuickAdd** "Capture" choice.
3. Configure it to "Capture to active file."
4. Enable the "Write to file" option and select the template file you just created (`RACL_Master_Prompt.md`).
5. Ensure the "Create file if it doesn't exist" option is off.
6. Assign a hotkey to this QuickAdd choice (e.g., `Ctrl+Shift+P`).

Now, when you invoke the QuickAdd hotkey in a new note, it will insert this template, ready for Phase 3.

```markdown
---
# METADATA - DO NOT EDIT SCHEMA
uid: <% tp.date.now("YYYYMMDDHHmmss") %>
creation_date: <% tp.date.now("YYYY-MM-DD") %>
status: "pending_review"
tags: [llm-generated, zettel]
llm_model: "local-model-name"
temperature: 0.5
critique_score: 
review_date: <% tp.date.now("YYYY-MM-DD", "+1d") %>
moc: 
---
# LLM PROMPT - COPY AND PASTE INTO SMART CHAT

You are an **expert academic researcher** and **methodology designer** with deep expertise in [Specify Domain 1, e.g., knowledge management] and [Specify Domain 2, e.g., cognitive science]. Your task is to analyze the provided query and context to generate a structured, atomic note.

**CONTEXT FROM MY PERSONAL KNOWLEDGE BASE (Provided by RAG):**
{Smart Connections will automatically inject the most relevant notes from my vault here. Your analysis MUST prioritize and reference this context.}

**PRIMARY TASK (User Query):**
{{VALUE:Initial Query}}

**EXECUTION INSTRUCTIONS (Chain-of-Thought):**
1.  **Deconstruct:** First, break down the user's query into its fundamental principles.
2.  **Analyze & Synthesize:** Second, analyze these principles in light of the provided RAG context. Synthesize the key insights, identifying connections, contradictions, or novel implications.
3.  **Structure:** Third, structure the synthesized knowledge according to the precise `OUTPUT SCHEMA` defined below. Do not deviate from this format.
4.  **Critique:** Fourth, generate a brief, objective counter-argument or identify the primary limitation of the main conclusion.

**CONSTRAINTS:**
-   Output must be in English.
-   Writing style must be academic, clear, and concise.
-   Avoid platitudes and verbose introductions.
-   All key claims must be logically sound and directly supported by the reasoning process.

**OUTPUT SCHEMA (Strictly Adhere to this Markdown Format):**

### Abstract
A one-sentence summary of the core concept.

### Key Insights
-   Use a bulleted list for the main points.
-   Each point must be a complete, well-reasoned statement.
-   Focus on clarity and depth.

### Counter-Argument / Limitations
A concise paragraph identifying the primary weakness, alternative perspective, or limitation of the key insights.

### Connections
-   [[Concept 1]]
-   [[Concept 2]]

---
> [!info]
> After generation, paste the LLM output below this line, replacing this prompt.
> Then, proceed to Phase 4: Factual Verification.

```
