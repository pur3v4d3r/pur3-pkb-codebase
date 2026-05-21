---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Microsoft-Copilot_Elias
aliases:
  - AI Prompts for Obsidian - Microsoft Copilot
  - Microsoft Copilot Prompt Library for Obsidian
  - Synergistic Copilot Prompts - Microsoft
tags:
  - prompt-engineering/llm/library
  - tools/ai/microsoft-copilot
  - tools/obsidian/copilot
  - workflows/pkm/automation
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[[AI Persona Instruction Set -  Elias, the Prompt Architect]]"
related:
  - "[[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]"
date created: Sunday, September 28th 2025, 11:10:28 pm
date modified: Monday, September 29th 2025, 12:20:58 am
---

#### Sources:

[^1]: [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]
[^2]: [[AI Persona Instruction Set -  Elias, the Prompt Architect]]
[^3]: [[Types of Notes]]
[^4]: [[Note-Taking for Different Subjects and Contexts]]
[^5]: [[Outline Note Method]]
[^6]: [[Visual and Associative Methods for Note Taking]]
[^7]: [[How to Properly Cite a Source]]
[^8]: [[Advanced Search Engine Use]]
[^9]: [[ChatGPT Universal Smart Note Template SOP]]
[^10]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^11]: [[Workflow for Evaluating Sources and Information]]
[^12]: [[Source Evaluation - A Three Tiered Approach]]
[^13]: [[ref_notes_guide-to-active-reading-by-ai's_2025-09-24]]
[^14]: [[Common Logical Fallacies]]
[^15]: [[Function of Notes is Important]]
[^16]: [[S I F T - Lateral Reading for Source Verification]]
[^17]: [[The Toulmin Model]]
[^18]: [[Document Your Searches during Research]]
[^19]: [[REF_Gemini-Chat_Response-to-Note_Researching Material for use in Vault_2025-09-12]]
[^20]: [[ref_gemini-prompt_guide-to-obsidian-plug-in-quickadd_2025-09-24]]

> [!the-purpose]
> This is a prompt created using the Elias Prompt Architect Gem, its purpose is to generate Synergistical Prompts using my current Obsidian Plugins.
> - These are some important reference links:
> 
>   - [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]] - This is a link to the original Prompt used.
> 
>   - [[AI Persona Instruction Set -  Elias, the Prompt Architect]] - This is a link to Persona that was use to create this. 

# 🧠 Master Reference Note: Synergistic Copilot Prompts for Obsidian

Welcome to your master reference note for **AI-powered workflows** in Obsidian. This document contains a curated collection of **synergistic prompts** designed for the **Copilot plugin**, each crafted to integrate seamlessly with other plugins in your PKM stack. These prompts go beyond basic automation—they unlock latent potential across your vault by combining metadata, task management, visual thinking, and formatting into intelligent, context-aware workflows.

Use this note as a launchpad for creative ideation, deep synthesis, and frictionless productivity.

---

## 📚 Table of Contents

	
- 📥 Information Capture & Triage
- 🧠 Note Processing & Synthesis
- 📈 Project & Task Management
- 💡 Creative Ideation & Expansion
- 🧹 Vault Maintenance & Organization

---

## 📥 Information Capture & Triage

#### ✨ Smart Daily Note Summarizer

- **🎯 Goal:** Automatically summarize the most important highlights, tasks, and ideas from today's daily note.
- **⚡ Trigger:** At the end of the day, during daily review.
- **🔗 Plugin Synergy:** `Copilot` + `Periodic Notes` + `Dataview`
- **📝 The Prompt:**

```
	- Summarize the key highlights, decisions, and open tasks from today's daily note. Use Dataview to extract all tasks and callouts from the current daily note, and synthesize them into a concise summary with actionable next steps.
```

#### ✨ Context-Aware Quick Capture

- **🎯 Goal:** Capture a fleeting idea with relevant metadata and context-aware suggestions.
- **⚡ Trigger:** When using Quick Add to jot down a new idea.
- **🔗 Plugin Synergy:** `Copilot` + `Quick Add` + `Dataview`
- **📝 The Prompt:**

```
	- Based on the note title "{{noteTitle}}" and tags {{tags}}, suggest a refined version of this idea: "{{rawIdea}}". Include related notes from the vault and propose a category or project it might belong to.
```

---

## 🧠 Note Processing & Synthesis

#### ✨ Insight Synthesizer from Highlights

- **🎯 Goal:** Transform raw highlights into structured insights and thematic summaries.
- **⚡ Trigger:** After highlighting key passages in a note.
- **🔗 Plugin Synergy:** `Copilot` + `Highlighter` + `Callout Manager`
- **📝 The Prompt:**

```
	- Review all highlighted text in this note and synthesize the main themes. Organize insights into callout blocks labeled "Key Insight", "Open Question", and "Actionable Idea".
```

#### ✨ Multi-Note Concept Merger

- **🎯 Goal:** Merge concepts from multiple notes into a unified synthesis.
- **⚡ Trigger:** When exploring connections between notes on a shared topic.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview` + `Callout Manager`
- **📝 The Prompt:**

```
	- Using Dataview, find all notes tagged with "{{topicTag}}". Extract their main ideas and synthesize them into a single cohesive summary. Use callouts to distinguish between perspectives, contradictions, and synthesis points.
```

---

## 📈 Project & Task Management

#### ✨ Task Prioritization Assistant

- **🎯 Goal:** Prioritize tasks based on urgency, importance, and context.
- **⚡ Trigger:** During weekly planning or task review.
- **🔗 Plugin Synergy:** `Copilot` + `Tasks` + `Periodic Notes`
- **📝 The Prompt:**

```
	- Review all incomplete tasks from the past 7 days using the Tasks plugin. Categorize them into "Urgent", "Important", and "Optional", and suggest a plan for the upcoming week.
```

#### ✨ Project Kickoff Blueprint

- **🎯 Goal:** Generate a structured project note with tasks, milestones, and linked resources.
- **⚡ Trigger:** When starting a new project.
- **🔗 Plugin Synergy:** `Copilot` + `Quick Add` + `Tasks`
- **📝 The Prompt:**

```
	- Create a project blueprint for "{{projectName}}". Include sections for goals, milestones, key resources, and a task list. Use markdown checkboxes for tasks and link to any existing related notes.
```

---

## 💡 Creative Ideation & Expansion

#### ✨ Visual Brainstorm Companion

- **🎯 Goal:** Generate visual brainstorming prompts and diagrams.
- **⚡ Trigger:** When ideating on a new concept or problem.
- **🔗 Plugin Synergy:** `Copilot` + `Excalidraw` + `Callout Manager`
- **📝 The Prompt:**

```
	- Based on the concept "{{idea}}", generate a visual brainstorming map with 3–5 branches. Suggest an Excalidraw layout and include callouts for each branch with questions or subtopics to explore.
```

#### ✨ Idea Expansion Engine

- **🎯 Goal:** Expand a seed idea into multiple creative directions.
- **⚡ Trigger:** When developing a new note or concept.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview` + `Quick Add`
- **📝 The Prompt:**

```
	- Take the idea "{{seedIdea}}" and generate 5 creative expansions. For each, suggest a note title, tags, and a brief summary. Use Dataview to check for existing related notes and avoid duplication.
```

---

## 🧹 Vault Maintenance & Organization

#### ✨ Markdown Style Auditor

- **🎯 Goal:** Audit and clean up markdown formatting across selected notes.
- **⚡ Trigger:** During periodic vault maintenance.
- **🔗 Plugin Synergy:** `Copilot` + `Linter` + `Dataview`
- **📝 The Prompt:**

```
	- Use Dataview to find all notes modified in the last 30 days. For each, check for inconsistent markdown formatting and suggest corrections using Linter rules. Summarize the most common issues found.
```

#### ✨ Tag Refactoring Assistant

- **🎯 Goal:** Refactor and consolidate tags across the vault.
- **⚡ Trigger:** When tag sprawl becomes unmanageable.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview`
- **📝 The Prompt:**

```
	- Analyze all tags used across the vault. Identify redundant or overlapping tags and suggest a refactored tag taxonomy. Include a mapping of old tags to new ones.
```

---

Would you like me to generate additional prompts for specific workflows, or tailor this document to a particular use case (e.g., academic research, creative writing, business strategy)?
