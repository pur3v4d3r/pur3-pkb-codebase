---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Meta-Llama-3-405B-Instruct_Elias
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
date created: Sunday, September 28th 2025, 11:00:51 pm
date modified: Monday, September 29th 2025, 12:21:30 am
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
[^9]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^10]: [[ChatGPT Universal Smart Note Template SOP]]
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

# Master Reference Note: Synergistic Prompts for Copilot in Obsidian

===========================================================

This document serves as a comprehensive collection of powerful, creative, and highly practical prompts for the "Copilot" AI plugin in Obsidian. Each prompt is designed to create synergy between multiple plugins, automating workflows, deepening insights, and solving problems in Personal Knowledge Management (PKM).

## Table of Contents

- [📥 Information Capture & Triage](#information-capture--triage)
- [🧠 Note Processing & Synthesis](#note-processing--synthesis)
- [📈 Project & Task Management](#project--task-management)
- [💡 Creative Ideation & Expansion](#creative-ideation--expansion)
- [🧹 Vault Maintenance & Organization](#vault-maintenance--organization)

### 📥 Information Capture & Triage

#### ✨ **Quick Capture to Pre-Formatted Note with Auto-Generated Tags**

- **🎯 Goal:** To capture a fleeting idea or information snippet and automatically generate a pre-formatted note with relevant tags.
- **⚡ Trigger:** When you need to quickly jot down an idea or information and don't have time to format it properly.
- **🔗 Plugin Synergy:** `Copilot` + `Quick Add`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with a brief description of an idea or information snippet. Your task is to generate a pre-formatted note based on the description and suggest 3-5 relevant tags.
  
  Description: [Insert description here]
  ```

- **💡 Example in Action:**
  Input Text: Create a note about the importance of morning meditation in increasing productivity.

  Expected Output:

  ```markdown
  # Morning Meditation for Productivity
  ## Introduction
  Briefly discuss the benefits of morning meditation in boosting productivity.
  
  ## Benefits
  - Reduces stress and anxiety
  - Improves focus and concentration
  - Enhances creativity
  
  Tags: #productivity #meditation #wellness
  ```

#### ✨ **Generate Daily Note Template with Task List and Priority**

- **🎯 Goal:** To automatically generate a daily note template with a task list and priority levels.
- **⚡ Trigger:** At the start of each day, to plan tasks and prioritize them effectively.
- **🔗 Plugin Synergy:** `Copilot` + `Periodic Notes` + `Tasks`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. Your task is to generate a daily note template with a task list and suggest priority levels for each task.
  
  Date: [Insert date here]
  ```

- **💡 Example in Action:**
  Input Text: Generate daily note template for 2025-09-01.

  Expected Output:

  ```markdown
  # 2025-09-01
  ## Tasks
  - [ ] Review project proposal 📅 2025-09-01 (High)
  - [ ] Attend team meeting 📅 2025-09-01 (Medium)
  - [ ] Respond to emails 📅 2025-09-01 (Low)
  ```

### 🧠 Note Processing & Synthesis

#### ✨ **Summarize Literature Note with Key Points and Actionable Tasks**

- **🎯 Goal:** To summarize a literature note, extract key points, and convert them into actionable tasks.
- **⚡ Trigger:** After reading and highlighting a source (book, article), to process insights into a task management system.
- **🔗 Plugin Synergy:** `Copilot` + `Highlighter` + `Tasks`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with a literature note. Your task is to summarize the note, extract key points, and convert them into actionable tasks.
  
  Note: [Insert note content here]
  ```

- **💡 Example in Action:**
  Input Text: ==Recent studies show the PARA method is effective for project organization.== I should really try to ==refactor my 'Projects' folder using PARA principles by the end of the month.==

  Expected Output:

  ```markdown
  # Summary
  Recent studies demonstrate the effectiveness of the PARA method in project organization.
  
  # Key Points
  - The PARA method improves project organization
  - Refactoring the 'Projects' folder using PARA principles is recommended
  
  # Tasks
  - [ ] Research the PARA method for project organization 📅 2025-10-03
  - [ ] Refactor the 'Projects' folder using PARA principles 📅 2025-09-30
  ```

#### ✨ **Create Mind Map from Note Highlights and Tags**

- **🎯 Goal:** To visually organize note highlights and tags into a mind map.
- **⚡ Trigger:** When reviewing notes and wanting to visualize connections between ideas.
- **🔗 Plugin Synergy:** `Copilot` + `Highlighter` + `Excalidraw`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with a note and its highlights. Your task is to create a mind map from the highlights and tags.
  
  Note: [Insert note content here]
  Highlights: [Insert highlights here]
  Tags: [Insert tags here]
  ```

- **💡 Example in Action:**
  Input Text: Note about morning meditation, highlights: ==meditation improves focus==, ==reduces stress==, tags: #productivity #meditation #wellness

  Expected Output:

  ```markdown
  # Mind Map
  - Morning Meditation
    - Improves Focus
    - Reduces Stress
    - Tags: #productivity #meditation #wellness
  
  [Excalidraw mind map: Morning Meditation → Improves Focus → Reduces Stress → Tags: #productivity #meditation #wellness]
  ```

### 📈 Project & Task Management

#### ✨ **Generate Project Plan with Tasks and Dependencies**

- **🎯 Goal:** To generate a project plan with tasks, dependencies, and due dates.
- **⚡ Trigger:** When starting a new project, to plan tasks and dependencies effectively.
- **🔗 Plugin Synergy:** `Copilot` + `Tasks`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with a project description. Your task is to generate a project plan with tasks, dependencies, and due dates.
  
  Project: [Insert project description here]
  ```

- **💡 Example in Action:**
  Input Text: Create a project plan for launching a new product.

  Expected Output:

  ```markdown
  # Project Plan
  ## Tasks
  - [ ] Define product requirements 📅 2025-09-15
  - [ ] Design product prototype 📅 2025-09-22 (Depends on: Define product requirements)
  - [ ] Develop product 📅 2025-10-06 (Depends on: Design product prototype)
  - [ ] Launch product 📅 2025-10-15 (Depends on: Develop product)
  ```

#### ✨ **Create Gantt Chart from Project Tasks and Dependencies**

- **🎯 Goal:** To visualize project tasks and dependencies in a Gantt chart.
- **⚡ Trigger:** When reviewing project progress, to visualize task dependencies and timelines.
- **🔗 Plugin Synergy:** `Copilot` + `Tasks` + `Excalidraw`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with a project plan. Your task is to create a Gantt chart from the project tasks and dependencies.
  
  Project Plan: [Insert project plan here]
  ```

- **💡 Example in Action:**
  Input Text: Project plan with tasks: Define product requirements, Design product prototype, Develop product, Launch product

  Expected Output:

  ```markdown
  # Gantt Chart
  [Excalidraw Gantt chart: Define product requirements → Design product prototype → Develop product → Launch product]
  ```

### 💡 Creative Ideation & Expansion

#### ✨ **Generate Ideas for Creative Project**

- **🎯 Goal:** To generate ideas for a creative project.
- **⚡ Trigger:** When starting a new creative project, to brainstorm ideas.
- **🔗 Plugin Synergy:** `Copilot`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with a creative project description. Your task is to generate ideas for the project.
  
  Project: [Insert project description here]
  ```

- **💡 Example in Action:**
  Input Text: Create a short story about a character who discovers a hidden world.

  Expected Output:

  ```markdown
  # Ideas
  - The character discovers a hidden world through a magical portal
  - The hidden world is inhabited by magical creatures
  - The character must navigate the hidden world to find a way back home
  ```

#### ✨ **Expand Idea into Detailed Concept**

- **🎯 Goal:** To expand an idea into a detailed concept.
- **⚡ Trigger:** When developing an idea, to flesh out details.
- **🔗 Plugin Synergy:** `Copilot`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with an idea. Your task is to expand the idea into a detailed concept.
  
  Idea: [Insert idea here]
  ```

- **💡 Example in Action:**
  Input Text: Idea about a character who discovers a hidden world.

  Expected Output:

  ```markdown
  # Concept
  ## Story Premise
  The character, a young adult, discovers a hidden world through a magical portal in their backyard.
  
  ## World-Building
  The hidden world is called "Aethoria" and is inhabited by magical creatures such as faeries, unicorns, and dragons.
  
  ## Character Arc
  The character must navigate Aethoria to find a way back home, learning about the world and themselves in the process.
  ```

### 🧹 Vault Maintenance & Organization

#### ✨ **Organize Notes into Folders and Subfolders**

- **🎯 Goal:** To organize notes into folders and subfolders.
- **⚡ Trigger:** When reviewing notes, to organize them for better access.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with a list of notes. Your task is to organize the notes into folders and subfolders.
  
  Notes: [Insert list of notes here]
  ```

- **💡 Example in Action:**
  Input Text: List of notes: Note 1, Note 2, Note 3

  Expected Output:

  ```markdown
  # Folders
  - Folder 1
    - Note 1
    - Note 2
  - Folder 2
    - Note 3
  ```

#### ✨ **Create Custom Note Template with Frontmatter**

- **🎯 Goal:** To create a custom note template with frontmatter.
- **⚡ Trigger:** When creating a new note, to use a custom template.
- **🔗 Plugin Synergy:** `Copilot`
- **📝 The Prompt:**

  ```text
  You are an AI assistant for Obsidian. I will provide you with a note template description. Your task is to create a custom note template with frontmatter.
  
  Template: [Insert template description here]
  ```

- **💡 Example in Action:**
  Input Text: Create a note template for meeting notes.

  Expected Output:

  ```markdown
  # Meeting Notes Template
  ## Frontmatter
  - Date: [Insert date]
  - Attendees: [Insert attendees]
  - Objective: [Insert objective]
  
  ## Meeting Notes
  - [Insert notes here]
  ```
