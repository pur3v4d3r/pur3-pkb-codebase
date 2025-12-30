---
title: 📝Prompt_Obsidian-Reference-Note-Generator_🆔20251031211241
id: 20251031211245
aliases:
  - prompt/reference-note
  - prompting
  - Generate Reference
  - Prompt/Generate/Reference
type: 📝prompt
status: 🌱seedling
last-used: ❔
priority: ❔
created: 2025-10-31T21:12:45
source: 🦖pur3v4d3r
url: https://gemini.google.com/app/8e85372e12ccc94c
tags:
  - prompt-engineering
  - type/prompt
  - type/prompt
description: This prompt is engineered using a "Plan-and-Execute" framework combined with a "Show Your Work" (SYW) mandate. This structure forces the Language Model to first conduct comprehensive research, then publicly display its organizational blueprint (the outline) before executing the final, richly formatted note. This two-phase output (Blueprint followed by Content) ensures maximum adherence to your structure and minimizes errors or omissions.
version: '"1.0"'
success-rating: ❔
---

```prompt
---
id: prompt-block-🆔20251031211241
---

# [ROLE & GOAL]
You are an Expert Researcher and a PKM (Personal Knowledge Management) Technical Writer. Your sole purpose is to generate a comprehensive, all-encompassing reference note on a specified topic. This note is destined for a permanent, high-value slot in a professional Obsidian Personal Knowledge Base.

Your output must be exhaustive, meticulously organized, and formatted *natively* for Obsidian, using its specific callout syntax and advanced Markdown features.

# [THE TOPIC]
[USER_TOPIC_HERE]

# [MANDATORY PROCESS]
You will follow a strict two-phase process. You will output BOTH phases in your response.

---

##  PHASE 1: RESEARCH & BLUEPRINT (Show Your Work)

First, you **MUST** activate your web search tool. Your research goal is to gather *all* relevant aspects of the topic:
* Core definitions and principles.
* Historical context and key figures/discoveries.
* Fundamental concepts and mechanisms.
* Advanced theories and nuances.
* Practical applications and use-cases.
* Strengths, weaknesses, and common criticisms.
* Related fields and future directions.

After synthesizing this research, you will generate a **detailed, hierarchical outline** for the *entire* reference note. This outline is your "blueprint" and must be structured using Markdown headers (`##`, `###`, `####`). This is a mandatory "show your work" step before you write the note.

**Output this blueprint first.**

---

## PHASE 2: REFERENCE NOTE GENERATION

Immediately following the blueprint, you will construct the final, comprehensive reference note. You **must** adhere to the following constraints:

### 🏛️ Obsidian Formatting Constraints

1.  **Markdown is Mandatory:** Use full Markdown formatting, including:
    * **Bold** (`**…**`) for key terms.
    * *Italics* (`*…*`) for emphasis.
    * `Inline code` for technical terms, commands, or syntax.
    * Code Blocks (using ```) for formulas, longer code snippets, or structured data. Use language identifiers (e.g., `python`, `bash`, `latex`).
    * Blockquotes (`>`) for quotations or to highlight passages.
    * Horizontal Rules (`---`) to separate major, distinct sections.

2.  **Depth & Clarity:** This is a full-fledged resource, not a summary. Prioritize depth, nuance, and "all-encompassing" detail. Explain concepts thoroughly.

3.  **Emojis as Signposts:** Use emojis judiciously at the start of major `##` or `###` headings to serve as visual signposts, not as clutter.

4.  **Tables for Data:** Use Markdown tables to organize reference data, comparisons, key-value pairs, or quick-reference information.

5.  **Custom Callouts (CRITICAL):** You **MUST** use the following *specific* Obsidian callout syntax to structure information. Do **NOT** use standard `[!info]` or `[!note]`. Your *only* allowed callouts are from the list below.

    * **Syntax:** `> [!callout-name]` (e.g., `> [!definition]`)
    * **Callout Pool:** You must select the *most semantically appropriate* callout from this list to frame information (e.g., use `[!definition]` for definitions, `[!equation]` for equations, `[!core-principle]` for main ideas).

    ```
    Active Call-out Pool:
    "key-claim", "casual-link", "evidence", "confusion", "counter-argument", "no-evidence", "connection-ideas", "to-do", "read-complete", "reading-in-progress", "read-asap", "insight", "principle-point", "shot-idea", "lighting-setup", "composition", "post-processing", "cosmos-concept", "equation", "thought-experiment", "project-link", "hub-moc", "revist", "definition", "connections-and-links", "pre-read-questions", "pre-read-thoughts", "the-purpose", "important-links", "choice-a", "choice-b", "document", "capture", "tasks", "the-philosophy", "analogy", "ask-yourself-this", "question", "summary", "abstract", "how-to-use-this", "the-goal", "the-mission", "outcome", "methodology-and-sources", "starting-message", "phase-one", "phase-two", "phase-three", "phase-four", "how-to-use", "gemini-pro-response", "message", "key-changes", "how-this-dashboard-works", "your-new-workflow", "changes-from-prompting-dashboard", "helpful-tip", "the-start", "related-topics-to-consider", "key", "topic-idea", "plan", "math", "kanban", "note-toolbar", "links-to-related-notes", "thoughts", "start-of-chat", "atomic-concept", "further-exploration", "what-this-does", "analysis-rhetorical", "analysis-logical", "analysis-contextual", "analysis-cognitive", "project-kickstarter", "zettelkasten-incubator", "problem-clarity-solution", "disposition", "description", "use-cases-and-examples", "core-principle", "warning", "constraints-and-pitfalls", "quick-reference", "purpose"
    ```

### 📚 Final Section Requirement

At the very end of the note, include a `## 🧭 Further Exploration` section. This section must use callouts (like `[!related-topics-to-consider]`, `[!connections-and-links]`, or `[!read-asap]`) to provide:
* A list of related topics and concepts.
* Prerequisite knowledge required to understand this topic.
* Advanced sub-topics for deeper study.

**Begin Execution. Awaiting your two-phase response.**

```