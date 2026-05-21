---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Gemini-2.5-Pro_2025-09-28_Elias
aliases: [Gemini Copilot Prompt Generation, Meta-Prompt for Obsidian AI Workflows, Synergistic AI Copilot Prompts]
tags: [prompt-engineering/llm, tools/ai/gemini, tools/obsidian/copilot, workflows/pkm/automation]
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: 
related:

date created: Sunday, September 28th 2025, 10:22:00 pm
date modified: Monday, September 29th 2025, 12:22:33 am
---

#### Sources:

[^1]: [[PKB]]
[^2]: [[Types of Notes]]
[^3]: [[Note-Taking for Different Subjects and Contexts]]
[^4]: [[Outline Note Method]]
[^5]: [[Visual and Associative Methods for Note Taking]]
[^6]: [[How to Properly Cite a Source]]
[^7]: [[Advanced Search Engine Use]]
[^8]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^9]: [[ChatGPT Universal Smart Note Template SOP]]
[^10]: [[Workflow for Evaluating Sources and Information]]
[^11]: [[Source Evaluation - A Three Tiered Approach]]
[^12]: [[Common Logical Fallacies]]
[^13]: [[REF_Notes_Guide-to-Active-Reading-by-AI's_2024-09-24]]
[^14]: [[Function of Notes is Important]]
[^15]: [[S I F T - Lateral Reading for Source Verification]]
[^16]: [[The Toulmin Model]]
[^17]: [[Document Your Searches during Research]]
[^18]: [[REF_Gemini-Chat_Response-to-Note_Researching Material for use in Vault_2025-09-12]]

> [!the-purpose]
> This is a prompt created using the Elias Prompt Architect Gem, its purpose is to generate Synergistical Prompts using my current Obsidian Plugins.
> - These are some important reference links:
> 
>   - [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]] - This is a link to the original Prompt used.
> 
>   - [[AI Persona Instruction Set -  Elias, the Prompt Architect]] - This is a link to Persona that was use to create this. 

***

## PKM Copilot Synergy Prompt Compendium

[[#📥 Information Capture & Triage]]

[[#🧠 Note Processing & Synthesis]]

[[#📈 Project & Task Management]]

[[#💡 Creative Ideation & Expansion]]

[[#🧹 Vault Maintenance & Organization]]

***

### 📥 Information Capture & Triage

#### ✨ **Structured Literature Review Template Generator**

- **🎯 Goal:** Automatically generate a detailed, pre-formatted note template tailored for a specific type of source material, complete with relevant metadata fields.
- **⚡ Trigger:** Used when capturing a new piece of research or literature via Quick Add, where only the source title and type (e.g., "Podcast," "Academic Paper") are initially input.
- **🔗 Plugin Synergy:** `Copilot` + `Quick Add` + `Dataview`
- **📝 The Prompt:**
 ```text
 I am using Quick Add to generate a new note titled "{Source Title}". The source type is "{Source Type, e.g., Academic Paper}". Generate the following content for the note: 1. A Dataview frontmatter block including 'type: {Source Type}', 'status: intake', 'author: ', and 'date_read: '. 2. A section called '## Key Thesis' followed by a '>[!abstract] Abstract Summary' callout. 3. A section '## Discussion Points' pre-formatted with three bullet points using ' - [ ] ' for initial task creation. Ensure the output is pure Markdown.
 ```

#### ✨ **Highlight Triage and Insight Synthesis**

- **🎯 Goal:** Review all highlighted text within a note and synthesize the core argument into a prominent, styled Callout box, preparing the note for linkage.
- **⚡ Trigger:** Run immediately after finishing a heavy reading session on a source note (containing `==highlighted text==`).
- **🔗 Plugin Synergy:** `Copilot` + `Highlighter` + `Callout Manager`
- **📝 The Prompt:**
 ```text
 Analyze the current note. Extract all highlighted text chunks. Based only on these highlighted segments, synthesize a concise, insightful summary that captures the main arguments and conclusions. Format this summary using the 'important' callout type defined by Callout Manager, starting with '> [!important] Core Insight'. Do not include any text outside the callout block.
 ```

***

### 🧠 Note Processing & Synthesis

#### ✨ **Dataview Concept Cluster Summarizer**

- **🎯 Goal:** Query a cluster of related notes identified by Dataview and generate a higher-level summary note that identifies common themes and contradictions.
- **⚡ Trigger:** Used when viewing a note that uses a Dataview query to list related concepts (e.g., all notes linked by `[[#Concept X]]`). The query results are pasted as context.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview`
- **📝 The Prompt:**
 ```text
 I have pasted the raw content from a Dataview query below. This query lists the file names and the 'summary' metadata field for notes tagged #[[System Design]]. Analyze the titles and summaries provided, focusing on identifying overlapping ideas and points of conflict. Generate a synthesis report structured with: 1. '## Major Themes Identified' (list). 2. '## Latent Conflicts' (short paragraph). 3. A suggested title for a new Synthesis Note based on this content.
 
 [PASTE DATAVIEW QUERY RESULTS HERE]
 ```

#### ✨ **Process Flow to Excalidraw Syntax Converter**

- **🎯 Goal:** Convert a complex textual description of a workflow or system into visualization code (Mermaid syntax), ready for embedding or use in an Excalidraw diagram.
- **⚡ Trigger:** After drafting a step-by-step process description in a project note.
- **🔗 Plugin Synergy:** `Copilot` + `Excalidraw` (via Mermaid)
- **📝 The Prompt:**
 ```text
 Analyze the following text which describes a step-by-step decision process. Convert this process into a standard Mermaid flowchart diagram code block. Use only basic nodes (A, B, C) and clear directional arrows (-->). The diagram should start with 'graph TD' and include a maximum of 7 steps.

 [PASTE PROCESS DESCRIPTION HERE]

 ```

***

### 📈 Project & Task Management

#### ✨ **Periodic Note Weekly Task Extraction and Prioritization**

- **🎯 Goal:** Review the previous week's daily notes (accessible via Periodic Notes structure) and a master task list, then generate a prioritized task list for the current week.
- **⚡ Trigger:** Run at the beginning of the Weekly Note generation (using Periodic Notes). Requires pasting the list of completed and remaining tasks from the previous week.
- **🔗 Plugin Synergy:** `Copilot` + `Periodic Notes` + `Tasks`
- **📝 The Prompt:**
 ```text
 I have pasted the raw output of my completed tasks from last week's Dataview Tasks query, and a separate list of tasks that remain open. Based on the open tasks, assign a priority (P1, P2, P3) to each and rewrite them using the Obsidian Tasks syntax (including priority `(P1)`, due date `YYYY-MM-DD`, and project tag `#projectname`). Group the final output under the heading '## This Week's Focus'.
 
 [PASTE RAW TASK LISTS HERE]
 ```

#### ✨ **Task Backlog Categorizer and Metadata Generator**

- **🎯 Goal:** Take a messy list of conceptual to-dos and structure them into formal tasks, automatically adding necessary Dataview metadata tags (like `status:: waiting` or `project:: Alpha`).
- **⚡ Trigger:** When processing a brain dump list of actions captured quickly.
- **🔗 Plugin Synergy:** `Copilot` + `Tasks` + `Dataview`
- **📝 The Prompt:**
 ```text
 Analyze the unstructured list of actions below. Convert each action into a formal Obsidian Task checklist item (`- [ ] `). For each task, automatically determine and append appropriate Dataview inline fields for categorization: 1. `area:: [select area, e.g., Work, Personal, Learning]` 2. `due:: [YYYY-MM-DD, estimate a date 3 days out]` 3. `priority:: [P2]`.

 [PASTE UNSTRUCTURED TASK LIST HERE]

 ```

***

### 💡 Creative Ideation & Expansion

#### ✨ **Problem/Solution Callout Matrix Generator**

- **🎯 Goal:** Analyze a problem description and instantly structure the resulting solution space using distinct Callout types for clarity and visual separation.
- **⚡ Trigger:** When detailing a complex problem in a project note and needing to separate the problem, proposed solution, and risk assessment clearly.
- **🔗 Plugin Synergy:** `Copilot` + `Callout Manager`
- **📝 The Prompt:**
 ```text
 Analyze the problem description below. Generate three consecutive, distinct Callout blocks based on this input: 1. A 'danger' Callout titled 'Problem Statement'. 2. A 'success' Callout titled 'Proposed Solution and Next Steps'. 3. A 'warning' Callout titled 'Identified Risks'. Ensure the content for each is substantial and directly addresses the input.

 [PASTE PROBLEM DESCRIPTION HERE]

 ```

#### ✨ **Idea Expansion via Tag Prompts**

- **🎯 Goal:** Take a nascent idea (tagged with specific concepts) and expand it into a detailed structure, suggesting new, related Dataview tags that could connect it to other vault ideas.
- **⚡ Trigger:** Used on a note that contains only a few sentences and several concept tags (e.g., #llm #Ethics).
- **🔗 Plugin Synergy:** `Copilot` + `Dataview`
- **📝 The Prompt:**
 ```text
 Expand the current idea by generating three distinct conceptual sections: 'Arguments For', 'Counter-Arguments', and 'Implementation Strategy'. After the new content, provide a suggested Dataview frontmatter block containing five new, relevant tags (e.g., tags: [tag1, tag2, ...]) that would broaden the connection of this note within the vault. Ensure the new content relates directly to the existing tags: [LIST EXISTING TAGS HERE].
 ```

***

### 🧹 Vault Maintenance & Organization

#### ✨ **Metadata Compliance Checker and Generator**

- **🎯 Goal:** Scan the current note for required Dataview frontmatter fields and, if missing, generate a complete, compliant block based on the note’s content.
- **⚡ Trigger:** Used during vault review on older notes known to lack standardized metadata.
- **🔗 Plugin Synergy:** `Copilot` + `Dataview`
- **📝 The Prompt:**
 ```text
 Review the content of this note. If a YAML frontmatter block containing 'type:' and 'status:' is not present, generate one at the top. Based on the note's text, determine the most fitting category for the 'type:' field (e.g., 'concept', 'meeting', 'project') and set 'status: organized'. If a frontmatter block already exists, check if 'type:' and 'status:' are present and append them if missing, intelligently selecting the values based on content analysis.
 ```

#### ✨ **Style Guide Enforcement and Linter Rationale**

- **🎯 Goal:** Review the current note against basic Linter style rules (e.g., passive voice, header hierarchy) and provide not only the suggested fix but also a brief rationale for the change.
- **⚡ Trigger:** Used after importing text from an external source or running Linter, to understand and manually apply complex formatting fixes.
- **🔗 Plugin Synergy:** `Copilot` + `Linter`
- **📝 The Prompt:**
 ```text
 Act as a writing editor and Linter analyst. Review the text below for adherence to clear, concise technical writing standards. Identify two specific sections containing either passive voice or overly complex sentence structure. For each section, provide two outputs: 1. The corrected, simplified, and active-voice version. 2. A brief, one-sentence rationale explaining the specific Linter rule that necessitated the change (e.g., "Corrected to active voice for clarity.").

 [PASTE SECTION OF TEXT TO LINT HERE]

 ```

# Gemini Thinking Before Responding

**Refining the Goal**

I'm refining the goal. The focus is now on a master reference note, specifically for synergistic prompts within Obsidian. The persona remains the same - a PKM Systems Architect and AI Integration Specialist - with a focus on structure, synergy, and precision.

**Identifying Interconnections**

I'm diving deeper into the plugin connections. I'm brainstorming how Copilot can work with each plugin, mapping out potential synergies. I'm focusing on practical applications, and refining the prompt templates. I'm prioritizing utility and efficiency in this iteration.

**Developing Prompt Templates**

I'm now building out prompt templates based on the plugin connections. I'm working on the Copilot prompts themselves, defining the goal, trigger, and synergy aspects within each. I'm prioritizing the "Information Capture & Triage" category now. I'm testing the outputs from Copilot and adjusting for optimal results.

**Prioritizing Plugin Synergies**

I've shifted from template creation to concentrating on the interconnections. I'm now assessing how to best leverage Dataview for data analysis and extracting insights. Focusing on how Copilot can analyze and transform Dataview query results. I'm refining the prompt framework to specifically address this.

**Prioritizing Information Capture**

I'm shifting the focus again, now prioritizing "Information Capture & Triage." I'm constructing a structured literature note template using Copilot and Quick Add. I'm working to define clear triggers and refine the prompts to ensure the structure's consistency. Then, I'll address the second prompt using Copilot, Highlighter, and Callout Manager.

**Focusing on Dataview**

I'm deeply immersed in crafting prompts that leverage Dataview. I'm concentrating on crafting a summary of Dataview query results. I want Copilot to perform data analysis on Dataview results, generating a summary. I'm now building prompt templates.

The following document serves as the master reference note for high-leverage, synergistic prompts designed for the **Copilot** AI integration within your Obsidian PKB.

As a PKM Systems Architect, I have designed these prompts not just for generation, but for systemic automation and insight extraction, explicitly leveraging the combined capabilities of your specific plugin stack. Employing these prompts will transform your vault from a repository of notes into a dynamic, interconnected knowledge machine.
