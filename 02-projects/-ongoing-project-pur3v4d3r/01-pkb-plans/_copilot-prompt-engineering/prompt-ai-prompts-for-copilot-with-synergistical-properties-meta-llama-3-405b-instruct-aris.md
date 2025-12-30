---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Meta-Llama-3-405B-Instruct_Aris
aliases:
  - Llama Aris Copilot Prompt Library
  - Meta-Llama AI Prompts for Obsidian - Aris Persona
  - Synergistic Copilot Prompts - Llama Aris
tags:
  - prompt-engineering/llm/library
  - tools/ai/llama
  - tools/obsidian/copilot
  - workflows/pkm/automation
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]"
related:
  - "[[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]"
date created: Sunday, September 28th 2025, 11:59:44 pm
date modified: Monday, September 29th 2025, 12:18:41 am
---

#### Sources:

[^1]: [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]
[^2]: [[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]
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
>   - [[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]- This is a link to Persona that was use to create this. 

# Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Meta-Llama-3-405B-Instruct_Aris

**Table of Contents**

* [📥 Information Capture & Processing](#-information-capture--processing)
* [🧠 Synthesis & Connection](#-synthesis--connection)
* [✍️ Creation & Elaboration](#-creation--elaboration)
* [🔍 Review & Resurfacing](#-review--resurfacing)

## 📥 Information Capture & Processing

#### **Auto-Notebook Creation**

> **Synergy:** Copilot + Periodic Notes + Quick Add

**🎯 Goal:** To automatically create and configure a new notebook for a project or topic, including essential templates and initial structure.

**⚡ Trigger:** When starting a new project or diving into an unfamiliar topic to efficiently establish a foundation for note-taking.

**💡 Prompt:**

```
Act as a personal assistant. I'm starting a new notebook for "[NOTEBOOK TOPIC]".

First, create a new folder named `#[NOTEBOOK TOPIC]`.

Next, using Quick Add, generate a template for a table of contents note that lists the following initial sections:
- Overview
- Literature Review
- Notes
- Resources
- Todo

Then, suggest 5-7 essential tags related to the topic that I should use for notes in this notebook.

**Example Usage:** The user runs this prompt with the topic "Neuro-Linguistic Programming". Copilot sets up the notebook, creates the foundational structure, and proposes relevant tags such as `#NLP`, `#NeuroScience`, `#PersonalDevelopment`.

#### **Smart Meeting Notes**

> **Synergy:** Copilot + Dataview + Tasks

**🎯 Goal:** To generate and organize meeting notes that automatically pull in relevant tasks and information, including attendees, discussions, and action items.

**⚡ Trigger:** Immediately after a meeting to capture important points and ensure action items are clearly assigned.

**💡 Prompt:**
```

Assist me in documenting a meeting about "[MEETING SUBJECT]".

First, create a note with the title format "YYYY-MM-DD - [MEETING SUBJECT]" and tag it with `#meeting`.

Next, execute the following Dataview query to list all attendees from invited contacts tagged with `#people`:

`$=dv.list(dv.pages('#people').file.inlinks.map(l => l.path).where(l => l.includes("Contact/") && l.contains("[MEETING INVITEES]")))`

Then, extract action items discussed during the meeting by analyzing the conversation, and automatically add them as tasks assigned to the relevant individuals using Tasks.

Finally, summarize the main discussion points in a bullet list.

**Example Usage:** After a meeting on "Project Velocity", the user runs this prompt. Copilot compiles the note, including a list of attendees, a bullet list of key discussion points, and a set of action items automatically added as tasks.

#### **Web Article Summarizer**

> **Synergy:** Copilot + Highlighter + Iconize

**🎯 Goal:** To summarize a web article into a concise, visually appealing note, highlighting key points and automatically extracting essential metadata.

**⚡ Trigger:** When processing a dense or lengthy article to quickly grasp the main ideas and relevant details.

**💡 Prompt:**

```
Summarize this article about "[ARTICLE SUBJECT]" in a concise note format.

Use the Highlighter plugin to emphasize the main points, and include an abstract of no more than 100 words.

Next, automatically identify and list key terms from the article using an inline list.

Iconize the note using `?:`, marking the key terms.

Finally, suggest relevant tags for the note, ensuring they are also added to the metadata.

**Example Usage:** The user uses this prompt with an article about "Habit Formation". Copilot produces a summarized note with highlighted main points, a list of key terms such as `habit`, `routine`, `motivation`, and relevant tags like `#habitFormation`, `#personalGrowth`.

## 🧠 Synthesis & Connection

#### **Mindmap Connection Visualizer**

> **Synergy:** Copilot + Excalidraw + Tag Wrangler

**🎯 Goal:** To visually represent connections between ideas by generating a mind map based on tag associations and concepts found within notes.

**⚡ Trigger:** When trying to see the bigger picture of how different ideas or concepts relate to each other.

**💡 Prompt:**
```

Visualize connections for me between the concepts of "[TOPIC 1]" and "[TOPIC 2]".

First, use Tag Wrangler to extract relevant tags from notes related to both topics.

Next, using Excalidraw, generate a mind map that starts with these two topics at its core and branches out into associated ideas and concepts based on the extracted tags.

Highlight overlapping concepts between the two topics using different colors for distinction.

**Example Usage:** The user explores the connection between "Project Management" and "Leadership Skills". Copilot produces a visual mind map showing the central topics branching into ideas like "task delegation", "communication", and "decision-making", highlighting areas of overlap.

#### **Article Cross-Reference**

> **Synergy:** Copilot + Dataview + Highlighter

**🎯 Goal:** To automatically identify and cross-reference related articles or sources across notes, highlighting areas of overlap and suggesting further reading.

**⚡ Trigger:** When conducting research and wanting to understand how different sources relate to or build upon one another.

**💡 Prompt:**

```
Analyze this note on "[ARTICLE SUBJECT]" and find related articles or sources across my notes.

First, use Dataview to search for notes that mention key terms or concepts from this article.

Next, employing the Highlighter, mark sections within these related articles that discuss the same or similar topics.

Suggest 2-3 further readings based on these connections.

Finally, compile a list of unique sources from the highlighted sections.

**Example Usage:** The user requests an analysis of an article on "Innovation in Tech". Copilot identifies relevant notes discussing topics like "disruption", "startups", and "scaled growth", highlighting areas of overlap and recommending additional readings on these subjects.

## ✍️ Creation & Elaboration

#### **Draft Assistant**

> **Synergy:** Copilot + Text Generator + Quick Add

**🎯 Goal:** To assist in drafting a piece of writing (e.g., article, essay, proposal) by providing an outline, generating initial content, and suggesting improvements.

**⚡ Trigger:** When faced with a writing project and looking for a structured approach to get started and maintain momentum.

**💡 Prompt:**
```

Assist me in drafting an outline for "[WRITING SUBJECT]".

First, using Quick Add, generate a template for an outline that includes sections such as introduction, body, and conclusion.

Next, employing Text Generator, create initial content for each section based on my writing style and preferences.

Finally, review the generated content and suggest improvements, focusing on clarity, coherence, and overall flow.

**Example Usage:** The user requests assistance with an essay on "The Impact of AI on Society". Copilot produces an outline, fills in the sections with initial content, and offers suggestions for refining the argument and enhancing readability.

#### **Expanded Idea Generation**

> **Synergy:** Copilot + Tag Wrangler + Iconize

**🎯 Goal:** To expand on an idea by generating related concepts, providing examples, and suggesting new directions for exploration.

**⚡ Trigger:** When brainstorming and needing help to flesh out an idea or concept.

**💡 Prompt:**

```
Help me expand on the idea of "[IDEA SUBJECT]".

First, use Tag Wrangler to find related concepts and tags from my existing notes.

Next, employing the Iconize plugin, generate a visually appealing list of these related concepts, marked with distinct icons for easy identification.

For each concept, provide a brief explanation and an example of how it relates to the original idea.

Finally, suggest 2-3 new directions for exploring the idea further.

**Example Usage:** The user seeks to expand on the concept of "Remote Team Productivity". Copilot identifies related concepts such as "time zone management", "communication strategies", and "virtual collaboration tools", providing explanations, examples, and new areas for exploration.

## 🔍 Review & Resurfacing

#### **Notebook Refresh**

> **Synergy:** Copilot + Dataview + Callout Manager

**🎯 Goal:** To review and refresh a notebook by updating task lists, highlighting unresolved questions, and suggesting next steps.

**⚡ Trigger:** Periodically to maintain the organization and relevance of notebooks.

**💡 Prompt:**
```

Refresh my notebook on "[NOTEBOOK SUBJECT]".

First, using Dataview, list all open tasks from notes within the notebook and categorize them by priority.

Next, employing the Callout Manager, highlight unresolved questions and areas needing further research.

Finally, based on the tasks and questions, suggest 2-3 next steps for advancing knowledge or resolving open items in the notebook.

**Example Usage:** The user requests a refresh of their "Project Management" notebook. Copilot updates the task list, highlights questions related to resource allocation and risk management, and recommends next steps such as researching agile methodologies and re-evaluating project timelines.

#### **Knowledge Review Digest**

> **Synergy:** Copilot + Dataview + Homepage

**🎯 Goal:** To create a digest of key knowledge points from recent notes, highlighting important insights and reminding the user of crucial information.

**⚡ Trigger:** Regularly, such as weekly or monthly, to reflect on recent learnings and insights.

**💡 Prompt:**

```
Prepare a digest of the most significant insights from my recent notes.

First, using Dataview, find notes tagged with `#insight` from the past `[PERIOD]`.

Next, generate a concise summary of these insights, focusing on the main points and why they are important.

Finally, add this digest to the Homepage for easy review.

**Example Usage:** The user runs this prompt to review insights from the past month. Copilot compiles a digest summarizing key findings on topics such as "team motivation", "decision-making biases", and "project estimation techniques", making these insights readily available on the Homepage for future reference.
