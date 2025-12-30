---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Meta-Llama-4-Maverick-Instruct_Elias
aliases:
  - Llama Copilot Prompt Library
  - Meta-Llama AI Prompts for Obsidian
  - Synergistic Copilot Prompts - Llama
tags:
  - prompt-engineering/llm/library
  - tools/ai/llama
  - tools/obsidian/copilot
  - workflows/pkm/automation
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[[AI Persona Instruction Set -  Elias, the Prompt Architect]]"
related:
  - "[[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]"
date created: Sunday, September 28th 2025, 10:44:49 pm
date modified: Monday, September 29th 2025, 12:22:01 am
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
[^20]: [[MLA Citation Style (Modern Language Association)]]

> [!the-purpose]
> This is a prompt created using the Elias Prompt Architect Gem, its purpose is to generate Synergistical Prompts using my current Obsidian Plugins.
> - These are some important reference links:
> 
>   - [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]] - This is a link to the original Prompt used.
> 
>   - [[AI Persona Instruction Set -  Elias, the Prompt Architect]] - This is a link to Persona that was use to create this. 

# Master Reference Note for Copilot Prompts in Obsidian

## Unlocking Synergies Across Your PKM Toolkit

This document is a comprehensive collection of powerful prompts designed for the Copilot AI plugin within the Obsidian ecosystem. By leveraging the combined capabilities of your installed plugins, these prompts aim to streamline your Personal Knowledge Management (PKM) workflows, enhance productivity, and foster creative insights.

## Table of Contents

- [📥 Information Capture & Triage](#-information-capture--triage)
- [🧠 Note Processing & Synthesis](#-note-processing--synthesis)
- [📈 Project & Task Management](#-project--task-management)
- [💡 Creative Ideation & Expansion](#-creative-ideation--expansion)
- [🧹 Vault Maintenance & Organization](#-vault-maintenance--organization)

### 📥 Information Capture & Triage

#### ✨ **Smart Daily Note Summary with Quick Capture**

- **🎯 Goal:** To automatically summarize daily notes into key points, leveraging Quick Add captures for context.
- **⚡ Trigger:** At the end of each day, to summarize the key events, tasks, and insights captured.
- **🔗 Plugin Synergy:** `Copilot` + `Quick Add` + `Periodic Notes`
- **📝 The Prompt:**

  ```text
  Summarize the following daily note, highlighting key tasks, events, and insights. Incorporate relevant Quick Add captures from today into the summary. Format the output for readability.
  
  Daily Note Content:
  [Paste daily note content here]
  Quick Add Captures:
  [Paste Quick Add captures here]
  ```

- **💡 Example in Action:**
  Input: Daily note with various tasks and insights, along with Quick Add captures for ideas.
  Expected Output: A concise summary highlighting key points, formatted for easy review.

#### ✨ **Triage Inbox Notes with Dataview Insights**

- **🎯 Goal:** To analyze inbox notes using Dataview queries and provide a prioritized list for processing.
- **⚡ Trigger:** When the inbox contains a significant number of notes to be triaged.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview`
- **📝 The Prompt:**

  ```text
  Analyze the following inbox notes using the available Dataview metadata. Provide a prioritized list for triage, suggesting tags, and potential actions.
  
  Inbox Notes:
  [List or query results here]
  ```

- **💡 Example in Action:**
  Input: List of inbox notes with their metadata.
  Expected Output: A prioritized list with suggested actions and tags.

### 🧠 Note Processing & Synthesis

#### ✨ **Generate Actionable Tasks from Literature Note Highlights**

- **🎯 Goal:** To automatically extract highlighted key points from a literature note and convert them into actionable tasks with due dates.
- **⚡ Trigger:** After reading and highlighting a source (book, article), you want to process your insights into your task management system without manual copy-pasting.
- **🔗 Plugin Synergy:** `Copilot` + `Highlighter` + `Tasks`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with the highlighted text from a literature note. Your task is to analyze each highlight and convert it into a concise, actionable to-do item. For each to-do, format it according to the Obsidian Tasks plugin syntax. If a highlight suggests a deadline, use it; otherwise, schedule it for this upcoming Friday.
  
  Here are the highlights:
  [Paste highlighted text here]
  ```

- **💡 Example in Action:**
  Input Text: ==Recent studies show the PARA method is effective for project organization.== I should really try to ==refactor my 'Projects' folder using PARA principles by the end of the month.==
  Expected Output:

  ```
  - [ ] Research the PARA method for project organization 📅 2025-10-03
  - [ ] Refactor the 'Projects' folder using PARA principles 📅 2025-09-30
  ```

#### ✨ **Synthesize Weekly Review Notes**

- **🎯 Goal:** To compile a comprehensive weekly review note by synthesizing insights from daily and weekly notes.
- **⚡ Trigger:** During the weekly review process.
- **🔗 Plugin Synergy:** `Copilot` + `Periodic Notes`
- **📝 The Prompt:**

  ```text
  Compile a detailed weekly review note by synthesizing key insights, tasks completed, and tasks pending from the daily notes of the past week. Include an analysis of progress toward weekly goals.
  
  Daily Notes Content:
  [Paste or link to relevant daily notes]
  Weekly Goals:
  [List weekly goals here]
  ```

- **💡 Example in Action:**
  Input: Content from daily notes and a list of weekly goals.
  Expected Output: A comprehensive weekly review note highlighting achievements, pending tasks, and insights.

### 📈 Project & Task Management

#### ✨ **Task Prioritization with Dataview Query Results**

- **🎯 Goal:** To analyze tasks from the Tasks plugin using Dataview queries and provide a prioritized task list.
- **⚡ Trigger:** When you need to prioritize tasks based on certain criteria (due date, priority, project).
- **🔗 Plugin Synergy:** `Copilot` + `Tasks` + `Dataview`
- **📝 The Prompt:**

  ```text
  Analyze the following tasks retrieved via a Dataview query. Prioritize them based on urgency and importance. Suggest a daily/weekly plan for tackling these tasks.
  
  Tasks Query Results:
  [Paste Dataview query results here]
  ```

- **💡 Example in Action:**
  Input: List of tasks with their metadata from a Dataview query.
  Expected Output: A prioritized task list with a suggested plan.

#### ✨ **Automate Project Status Reports**

- **🎯 Goal:** To generate comprehensive project status reports by analyzing tasks and notes related to a project.
- **⚡ Trigger:** When you need to report on project status to stakeholders.
- **🔗 Plugin Synergy:** `Copilot` + `Tasks` + `Dataview`
- **📝 The Prompt:**

  ```text
  Generate a detailed project status report by analyzing the tasks and related notes for [Project Name]. Include progress, upcoming milestones, and potential roadblocks.
  
  Project Tasks:
  [List or query results for project tasks]
  Related Notes:
  [List or link to related notes]
  ```

- **💡 Example in Action:**
  Input: Tasks and notes related to a specific project.
  Expected Output: A comprehensive project status report.

### 💡 Creative Ideation & Expansion

#### ✨ **Brainstorm with Excalidraw Diagrams**

- **🎯 Goal:** To generate ideas and expand on concepts by analyzing an Excalidraw diagram.
- **⚡ Trigger:** When you have an Excalidraw diagram that needs further brainstorming or expansion.
- **🔗 Plugin Synergy:** `Copilot` + `Excalidraw`
- **📝 The Prompt:**

  ```text
  Analyze the following Excalidraw diagram and generate ideas or expansions on the concepts presented. Provide a list of potential next steps or related ideas.
  
  Excalidraw Diagram Description:
  [Describe or paste the diagram content here]
  ```

- **💡 Example in Action:**
  Input: Description of an Excalidraw diagram.
  Expected Output: A list of ideas and potential next steps related to the diagram.

#### ✨ **Enhance Note with Creative Callouts**

- **🎯 Goal:** To enhance a note by suggesting creative callouts for emphasis and readability.
- **⚡ Trigger:** When you want to make a note more engaging or highlight key points.
- **🔗 Plugin Synergy:** `Copilot` + `Callout Manager`
- **📝 The Prompt:**

  ```text
  Suggest creative callouts to enhance the following note. Use the Callout Manager plugin syntax for formatting.
  
  Note Content:
  [Paste note content here]
  ```

- **💡 Example in Action:**
  Input: A plain note without callouts.
  Expected Output: The note with suggested callouts for emphasis.

### 🧹 Vault Maintenance & Organization

#### ✨ **Linter Suggestions for Markdown Consistency**

- **🎯 Goal:** To analyze notes for Markdown consistency and provide Linter suggestions.
- **⚡ Trigger:** During vault maintenance to ensure consistency across notes.
- **🔗 Plugin Synergy:** `Copilot` + `Linter`
- **📝 The Prompt:**

  ```text
  Analyze the following note for Markdown consistency and provide suggestions according to the Linter rules. Format the suggestions for easy application.
  
  Note Content:
  [Paste note content here]
  Linter Rules:
  [List or describe Linter rules in use]
  ```

- **💡 Example in Action:**
  Input: A note with inconsistent Markdown formatting.
  Expected Output: Suggestions for fixing the inconsistencies.

#### ✨ **Tagging Strategy Optimization with Dataview**

- **🎯 Goal:** To analyze the current tagging strategy using Dataview and suggest optimizations.
- **⚡ Trigger:** When reviewing the vault's tagging strategy.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview`
- **📝 The Prompt:**

  ```text
  Analyze the current tagging strategy in the vault using Dataview. Suggest optimizations for tag usage, consolidation, or creation.
  
  Dataview Query Results:
  [Paste Dataview query results showing tag usage]
  ```

- **💡 Example in Action:**
  Input: Dataview query results showing tag distribution and usage.
  Expected Output: Suggestions for optimizing the tagging strategy.
