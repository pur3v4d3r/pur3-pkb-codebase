---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Claude-4.1-Opus_Research_Elias
aliases:
  - Claude AI Prompts for Obsidian
  - Claude Copilot Prompt Library
  - Synergistic Copilot Prompts - Claude
tags:
  - prompt-engineering/llm/library
  - tools/ai/claude
  - tools/obsidian/copilot
  - workflows/pkm/automation
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[[AI Persona Instruction Set -  Elias, the Prompt Architect]]"
related:
  - "[[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]"
date created: Sunday, September 28th 2025, 11:28:16 pm
date modified: Monday, September 29th 2025, 12:20:24 am
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

# 🚀 Master Reference: Synergistic Copilot Prompts for Obsidian PKM

## Purpose

This document serves as your comprehensive command center for AI-driven knowledge management in Obsidian. Each prompt is meticulously crafted to harness the combined power of Copilot with your plugin ecosystem, transforming isolated tools into a unified intelligence amplification system.

## 📑 Table of Contents

- [📥 Information Capture & Triage](https://claude.ai/chat/3cf4e52f-0e26-48bf-a831-e59dbcbdcd02#information-capture--triage)
- [🧠 Note Processing & Synthesis](https://claude.ai/chat/3cf4e52f-0e26-48bf-a831-e59dbcbdcd02#note-processing--synthesis)
- [📈 Project & Task Management](https://claude.ai/chat/3cf4e52f-0e26-48bf-a831-e59dbcbdcd02#project--task-management)
- [💡 Creative Ideation & Expansion](https://claude.ai/chat/3cf4e52f-0e26-48bf-a831-e59dbcbdcd02#creative-ideation--expansion)
- [🧹 Vault Maintenance & Organization](https://claude.ai/chat/3cf4e52f-0e26-48bf-a831-e59dbcbdcd02#vault-maintenance--organization)

---

### 📥 Information Capture & Triage

#### ✨ **Daily Insight Harvester**

- **🎯 Goal:** Transform raw daily notes into structured, actionable insights with automated task extraction.
- **⚡ Trigger:** End of day review when processing scattered thoughts from Periodic Notes.
- **🔗 Plugin Synergy:** `Copilot` + `Periodic Notes` + `Tasks`
- **📝 The Prompt:**

    ```
    Analyze today's daily note and perform these actions:1. Extract all actionable items and format them as Tasks plugin checkboxes with appropriate due dates2. Identify key insights and create a "Key Takeaways" callout block3. Suggest 3 follow-up questions for tomorrow's reflection4. Tag any mentioned topics that don't have existing notes with #seed-ideaDaily note content: {{daily note content}}
    ```

#### ✨ **Quick Capture Contextualizer**

- **🎯 Goal:** Instantly enrich quick captures with relevant context and connections from your vault.
- **⚡ Trigger:** After using Quick Add to capture a fleeting thought or observation.
- **🔗 Plugin Synergy:** `Copilot` + `Quick Add` + `Dataview`
- **📝 The Prompt:**

    ```text
    Take this quick capture and enhance it:1. Generate a Dataview query to find 5 most related existing notes2. Suggest appropriate tags based on similar content in the vault3. Create a "Context" section with links to potentially related concepts4. Add a "Next Actions" section with 2-3 concrete exploration stepsQuick capture: {{captured text}}Current tags in vault: {{list of frequently used tags}}
    ```

#### ✨ **Meeting Note Architect**

- **🎯 Goal:** Convert rough meeting notes into structured documents with automatic action item tracking.
- **⚡ Trigger:** Immediately after capturing meeting notes via Quick Add.
- **🔗 Plugin Synergy:** `Copilot` + `Quick Add` + `Tasks` + `Callout Manager`
- **📝 The Prompt:**

    ```text
    Transform these meeting notes into a structured format:1. Create an "Attendees" callout with participant list2. Generate "Key Decisions" callout with numbered items3. Extract all action items as Tasks with @mentions and due dates4. Create "Open Questions" section for unresolved topics5. Add "Follow-up Required" callout for items needing future discussionRaw meeting notes: {{meeting content}}Default task assignee: {{your name}}
    ```

---

### 🧠 Note Processing & Synthesis

#### ✨ **Zettelkasten Atomic Splitter**

- **🎯 Goal:** Decompose long-form notes into atomic, interlinked zettelkasten notes.
- **⚡ Trigger:** When a note becomes too complex and needs atomization.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview` + `Highlighter`
- **📝 The Prompt:**

    ```text
    Analyze this note and create atomic note suggestions:1. Identify 3-5 core concepts that deserve individual notes2. For each concept, generate a note title following format: "YYYYMMDD-HHMM Concept Name"3. Create bidirectional linking suggestions between the atomic notes4. Highlight the key sentences in the original that should seed each atomic note5. Generate a Dataview query to track all derivative atomic notesOriginal note: {{note content}}Preferred note naming convention: {{your convention}}
    ```

#### ✨ **Cross-Note Pattern Detector**

- **🎯 Goal:** Discover hidden patterns and connections across multiple notes using metadata analysis.
- **⚡ Trigger:** Weekly review to identify emerging themes in your thinking.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview` + `Callout Manager`
- **📝 The Prompt:**

    ```text
    Analyze these Dataview query results to find patterns:1. Identify 3 recurring themes across the notes2. Create a "Pattern Analysis" callout with bullet points for each pattern3. Suggest a new MOC (Map of Content) structure to connect these themes4. Generate linking statements that would connect isolated notes5. Propose 2 synthesis questions that bridge multiple conceptsDataview results: {{query results}}Time period analyzed: {{date range}}
    ```

#### ✨ **Literature Note Synthesizer**

- **🎯 Goal:** Transform highlighted passages from books/articles into permanent notes with personal insights.
- **⚡ Trigger:** After importing highlights from a reading session.
- **🔗 Plugin Synergy:** `Copilot` + `Highlighter` + `Periodic Notes`
- **📝 The Prompt:**

    ```text
    Process these highlights into permanent notes:1. Group related highlights into thematic clusters2. For each cluster, generate a permanent note title and one-paragraph synthesis3. Add a "Personal Reflection" section connecting to your current projects4. Create "Questions for Future Exploration" based on gaps in understanding5. Link to relevant daily notes from the past weekHighlights: {{highlighted text}}Source: {{book/article title}}Current active projects: {{project list}}
    ```

---

### 📈 Project & Task Management

#### ✨ **Project Momentum Dashboard Generator**

- **🎯 Goal:** Create visual project status dashboards with task burndown metrics.
- **⚡ Trigger:** Weekly project review sessions.
- **🔗 Plugin Synergy:** `Copilot` + `Tasks` + `Dataview` + `Excalidraw`
- **📝 The Prompt:**

    ```text
    Generate a project status dashboard:1. Create a Dataview query showing tasks grouped by status (not done, done, cancelled)2. Calculate completion percentage and estimated time to completion3. Identify the 3 most critical blockers based on task dependencies4. Generate Excalidraw diagram code for a simple burndown chart5. Create "This Week's Focus" callout with top 5 priority itemsProject name: {{project}}Task tag: #{{project-tag}}Sprint duration: {{days}}
    ```

#### ✨ **Task Dependency Mapper**

- **🎯 Goal:** Visualize task dependencies and identify critical path bottlenecks.
- **⚡ Trigger:** When planning complex multi-step projects.
- **🔗 Plugin Synergy:** `Copilot` + `Tasks` + `Excalidraw`
- **📝 The Prompt:**

    ```text
    Analyze these tasks and create a dependency map:1. Identify task dependencies based on task descriptions2. Generate Excalidraw flowchart code showing task relationships3. Highlight the critical path in the diagram4. Create a "Parallel Work Streams" section for independent tasks5. Suggest optimal task sequencing to minimize bottlenecksTask list: {{tasks from current note}}Project deadline: {{date}}Available resources: {{team members or time blocks}}
    ```

#### ✨ **Weekly Sprint Architect**

- **🎯 Goal:** Design optimized weekly sprints based on task priorities and energy patterns.
- **⚡ Trigger:** Sunday planning session for the upcoming week.
- **🔗 Plugin Synergy:** `Copilot` + `Tasks` + `Periodic Notes` + `Callout Manager`
- **📝 The Prompt:**

    ```text
    Design next week's sprint based on current tasks:1. Group tasks by estimated effort (Low/Medium/High)2. Distribute tasks across weekdays based on energy patterns3. Create daily "Focus Block" callouts with primary objectives4. Generate a "Week at a Glance" summary with key milestones5. Add "Flexibility Buffer" tasks for unexpected workPending tasks: {{task list}}Energy pattern: {{morning/afternoon/evening preference}}Fixed commitments: {{meetings and appointments}}
    ```

---

### 💡 Creative Ideation & Expansion

#### ✨ **Concept Constellation Builder**

- **🎯 Goal:** Generate networks of related ideas from a single seed concept.
- **⚡ Trigger:** When exploring a new domain or creative project.
- **🔗 Plugin Synergy:** `Copilot` + `Excalidraw` + `Dataview`
- **📝 The Prompt:**

    ```text
    Expand this concept into a constellation of related ideas:1. Generate 7 related sub-concepts with brief descriptions2. Create Excalidraw node-link diagram code showing relationships3. For each sub-concept, suggest a provocative question4. Generate Dataview query to find existing notes that might connect5. Propose 3 unexpected cross-domain connectionsSeed concept: {{your idea}}Domain context: {{field or area of interest}}Creative constraints: {{any boundaries or requirements}}
    ```

#### ✨ **Photography Project Ideation Engine**

- **🎯 Goal:** Generate photography project ideas aligned with Glenn Randall's philosophical approach.
- **⚡ Trigger:** When seeking inspiration for new photographic work.
- **🔗 Plugin Synergy:** `Copilot` + `Quick Add` + `Callout Manager`
- **📝 The Prompt:**

    ```text
    Generate photography project ideas following Randall's philosophy:1. Create 3 project concepts that blend technical mastery with emotional depth2. For each project, add a "Philosophical Anchor" callout explaining its deeper meaning3. Suggest specific technical challenges to push skill boundaries4. Add "Location Scouting" notes for Jacksonville area opportunities5. Create "Visual Metaphor" sections connecting to cosmological themesCurrent skill focus: {{technique you're developing}}Philosophical theme: {{concept from Randall's work}}Time of year: {{season}}
    ```

#### ✨ **Cosmological Connection Weaver**

- **🎯 Goal:** Connect everyday observations to cosmological principles and photographic opportunities.
- **⚡ Trigger:** During philosophical reflection or after astronomy reading.
- **🔗 Plugin Synergy:** `Copilot` + `Highlighter` + `Periodic Notes`
- **📝 The Prompt:**

    ```text
    Connect this observation to cosmological principles:1. Identify 3 cosmological concepts that relate to this experience2. Suggest photographic compositions that would capture these connections3. Create a "Scale Perspective" section (from quantum to cosmic)4. Generate philosophical questions bridging the micro and macro5. Link to this week's daily notes that touched on similar themesObservation: {{your experience or thought}}Recent cosmology learning: {{concept you've been studying}}Current location: Jacksonville, FL
    ```

---

### 🧹 Vault Maintenance & Organization

#### ✨ **Note Taxonomy Optimizer**

- **🎯 Goal:** Analyze and reorganize your tagging system for maximum retrieval efficiency.
- **⚡ Trigger:** Monthly vault maintenance session.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview` + `Linter`
- **📝 The Prompt:**

    ```text
    Analyze vault taxonomy and suggest improvements:1. Generate Dataview query to count all unique tags2. Identify redundant or overlapping tags that should be merged3. Suggest tag hierarchy using nested tags (#parent/child)4. Create Linter rules for enforcing consistent tag formatting5. Generate a "Tag Migration Plan" with search-replace commandsCurrent tag list: {{output from dataview query}}Preferred naming convention: {{your style guide}}Main knowledge domains: {{your focus areas}}
    ```

#### ✨ **Orphan Note Rescue Mission**

- **🎯 Goal:** Identify and integrate isolated notes into your knowledge network.
- **⚡ Trigger:** Weekly vault review to prevent knowledge silos.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview` + `Highlighter`
- **📝 The Prompt:**

    ```text
    Rescue orphaned notes and integrate them:1. For each orphan note, suggest 3 potential connection points2. Generate link phrases that would naturally connect to existing notes3. Highlight key concepts that deserve their own note pages4. Create a "Connection Opportunity" callout for each orphan5. Suggest which existing MOCs could include these notesOrphan notes list: {{dataview query results}}Main MOCs in vault: {{your maps of content}}Recent areas of focus: {{current interests}}
    ```

#### ✨ **Markdown Consistency Auditor**

- **🎯 Goal:** Ensure consistent formatting and structure across all notes.
- **⚡ Trigger:** Before sharing notes or creating published gardens.
- **🔗 Plugin Synergy:** `Copilot` + `Linter` + `Callout Manager`
- **📝 The Prompt:**

    ```text
    Audit and standardize note formatting:1. Identify inconsistent header hierarchies and suggest fixes2. Generate Linter configuration for enforcing style guide3. Standardize callout types across similar use cases4. Create a "Formatting Checklist" for manual review items5. Suggest template improvements based on common patternsSample notes for analysis: {{3-5 representative notes}}Preferred style guide: {{your formatting preferences}}Callout types in use: {{list from Callout Manager}}
    ```

#### ✨ **Knowledge Graph Pruner**

- **🎯 Goal:** Identify and remove outdated or redundant connections in your knowledge graph.
- **⚡ Trigger:** Quarterly deep cleaning of vault relationships.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview` + `Tasks`
- **📝 The Prompt:**

    ```text
    Analyze and optimize the knowledge graph:1. Identify notes with excessive outbound links (>15) that dilute meaning2. Find circular reference chains that don't add value3. Suggest link consolidation into MOC structures4. Create Tasks for reviewing questionable connections5. Generate "Health Metrics" callout with graph statisticsGraph analysis data: {{dataview statistics}}Link threshold: {{max links per note}}Core MOCs: {{your primary maps}}
    ```

---

## 🎯 Usage Guidelines

1. **Copy prompts directly** - Each prompt is ready for immediate use in Copilot
2. **Replace placeholders** - Look for {{variable}} markers and insert your specific content
3. **Chain prompts** - Many prompts generate outputs that can feed into others
4. **Customize freely** - Adapt language and requirements to match your workflow
5. **Track effectiveness** - Mark successful prompts with #proven-prompt tag

## 🔄 Continuous Improvement

This document evolves with your PKM practice. After each use:

- Note which prompts deliver highest value
- Identify gaps where new synergies could emerge
- Experiment with combining 3+ plugins in single prompts
- Share breakthrough prompts with the Obsidian community

Remember: The goal isn't just automation—it's intelligence amplification through strategic tool orchestration.
