---
title: Copilot Placeholder Reference and Strategic Use Cases Table
aliases:
  - Copilot Placeholder Table
  - Copilot Prompting Syntax
  - Obsidian AI Placeholder Reference
  - CPT
tags:
  - llm/prompting/placeholders
  - obsidian/plugins/copilot
  - pkm/workflows
  - reference/table
status: seedling
created: 2025-09-28
updated: 2025-09-28
source:
related:
date created: Sunday, September 28th 2025, 6:16:38 am
date modified: Sunday, September 28th 2025, 6:22:33 am
---

#### Copilot Placeholder Reference and Strategic Use Cases Table

| Placeholder    | Description                                    | Strategic Application                                                                                                                                                                                    | Example Prompt                                                                                                             |
| -------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `{}`           | The currently selected text in the editor.     | **Iterative Refinement & Expansion:** Perfect for rewriting a sentence, expanding a paragraph, or fixing grammar on a specific block of text.                                                            | `Rewrite the following text to be more concise and use an active voice: {}`                                                |
| `{activeNote}` | The entire content of the currently open note. | **Holistic Analysis & Transformation:** Use for summarizing long articles, generating an outline, extracting key entities, or converting prose to a structured format.                                   | `Analyze {activeNote} and generate a summary in three bullet points, followed by a list of key concepts discussed.`        |
| `{\]}`         | The entire content of the specified note.      | **Cross-Note Synthesis:** The primary tool for comparing ideas, creating summaries that draw from multiple sources, or using one note as a template for another.                                         | `Compare the main arguments in {[[Note A]]} with the counterarguments in {]} and identify the key points of disagreement.` |
| `{FolderPath}` | Concatenated content of all notes in a folder. | **Thematic & Project-Level Review:** Ideal for generating a high-level summary of a project, identifying common themes across research papers, or creating a progress report.                            | `Review all meeting notes in {ProjectX/Meetings} and generate a consolidated list of all action items and their owners.`   |
| `{#tag}`       | Concatenated content of all notes with a tag.  | **Conceptual Exploration & Serendipity:** Use to explore a concept across your entire vault, discover hidden connections between seemingly unrelated notes, and synthesize insights on a specific topic. | `Analyze all notes tagged with {#idea/sociology} and identify recurring themes or unanswered questions.`                   |

> [!connections-and-links]
> - [[REF_Gemini-Deep-Research_AI-Augmented-Vault_Strategic-Prompting-Guide-for-Copilot-&-Plugin Synergy_2025-09-28]] 
> 	- This is a link to the original article, written by Gemini.
> - [[Draft_Copilot-Prompt-Aquisition_Pur3v4d3r]] 
> 	- This is a link to original prompt used to create the article and this table.
