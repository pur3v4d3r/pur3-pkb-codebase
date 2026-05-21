---
title: REF_Gemini_Prompts-for-Co-Pilot-AI_2025-09-24
aliases:
  - Gemini Copilot Prompts
  - AI Prompts for Obsidian
  - Obsidian Copilot Prompt Library
tags:
  - prompt-engineering/llm/library
  - tools/obsidian/copilot
  - workflows/pkm
  - type/reference
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[Gemini-2.5-Flash-Preview, Aris Persona]"
related:
  - "[[🪐PKB-Prompts_🗺️MOC]]"
---


> [!the-purpose]
> This is a prompt created using the Elias Prompt Architect Gem, its purpose is to generate Synergistical Prompts using my current Obsidian Plugins.
> - These are some important reference links:
> 
>   - [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]] - This is a link to the original Prompt used.
> 
>   - [[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]- This is a link to Persona that was use to create this. 

---

## Table of Contents

*   [📥 Information Capture & Processing](#-information-capture--processing)
*   [🧠 Synthesis & Connection](#-synthesis--connection)
*   [✍️ Creation & Elaboration](#️-creation--elaboration)
*   [🔍 Review & Resurfacing](#-review--resurfacing)

---

## 📥 Information Capture & Processing

Prompts designed to streamline the intake and initial structuring of new information.

#### **Callout-Formatted Summary Generator**

> **Synergy:** Copilot + Callout Manager + Linter

**🎯 Goal:** To distill a long block of copied text into a concise summary and automatically place it within a pre-defined, standardized Callout block.

**⚡ Trigger:** When pasting a dense article, document section, or meeting transcript into a note that needs rapid summarization and clear visual hierarchy.

**💡 Prompt:**

```
Summarize the following text into 3 key bullet points. Ensure the summary is placed inside a clean, unindented Obsidian Callout of the type `[CALLOUT TYPE, e.g., summary]` with the title "Key Takeaways:". Ensure there are no trailing spaces or unnecessary blank lines, adhering to strict Linter-compatible Markdown formatting.


[PASTE TEXT HERE]


**Example Usage:** The user pastes 5 paragraphs of research. Copilot returns:

> [!summary] Key Takeaways:
> * Point one...
> * Point two...
> * Point three...

```

---

#### **Quick Add Template Data Prep**

> **Synergy:** Copilot + Quick Add + Text Generator

**🎯 Goal:** To transform unstructured input (e.g., a phone call note, a chaotic brainstorm) into a structured JSON or YAML output ready to be ingested by a Quick Add template variable.

**⚡ Trigger:** Immediately after an event (call, meeting, quick thought burst) where the goal is to quickly format the raw notes into a standardized data structure (like a `metadata` block).

**💡 Prompt:**

```
Analyze the following raw notes. Extract the key entities (Person/Contact, Topic/Subject, Urgency Level, Next Step). Format the output as a clean YAML block, suitable for pasting into the frontmatter of a new note.



status: "[[Status/New]]"
date_processed: "{{date:YYYY-MM-DD}}"
contact: "[CONTACT NAME]"
topic: "[TOPIC]"
urgency: "[URGENCY]"
next_step: "[NEXT STEP]"


**Raw Notes:**
[PASTE RAW NOTES HERE]

**Example Usage:** User pastes "Spoke to Sarah about the Q3 budget review. High priority. Need to schedule the follow-up meeting next Monday." Copilot returns the YAML block with the fields filled: `contact: "Sarah"`, `topic: "Q3 budget review"`, `urgency: "High priority"`, etc.

```
---

## 🧠 Synthesis & Connection

Prompts that help uncover hidden connections, synthesize multiple sources, and generate new insights.

#### **Inter-Note Insight Generation**

> **Synergy:** Copilot + Dataview + Tag Wrangler

**🎯 Goal:** To instruct Copilot to analyze a curated set of notes (pulled by Dataview) and identify a non-obvious connection or synthesis point between them that the user may have missed.

**⚡ Trigger:** When you feel you have gathered enough information on a topic across several notes but haven't yet reached a breakthrough idea.

**💡 Prompt:**

```
Execute the following Dataview query to identify the source material:
`$=dv.list(dv.pages("#topic/[TOPIC] and !#status/draft").file.link)`

Now, analyze the linked content of all notes returned by this query. Your task is to identify one key tension, contradiction, or synergistic opportunity that exists across all these separate documents. Present this insight as a single, bolded statement, followed by a brief paragraph of supporting evidence from the notes.
```

**Example Usage:** The Dataview query pulls three notes about "client-X". Copilot returns: **"The core synergy lies in using the design process documented in Note A to streamline the feature delivery schedule outlined in Note C, directly solving the budget overrun mentioned in Note B."**

---

#### **Highlighted Meta-Summary**

> **Synergy:** Copilot + Highlighter + Text Generator

**🎯 Goal:** To isolate all highlighted text within the current note and use the AI to generate a cohesive summary of *only* the emphasized points, filtering out surrounding noise.

**⚡ Trigger:** When reviewing a note where you have extensively used the feature and need to quickly understand the note's argument based on your manual selection of importance.

**💡 Prompt:**

```
Extract all highlighted sections (text enclosed in `==...==`) from this document. Treat the extracted segments as your sole source material. Synthesize these fragments into a single, flowing paragraph that represents the core argument of the highlighted content. Do not introduce any new ideas or context.
```

**Example Usage:** The note is 2000 words, but only 15 sentences are highlighted. Copilot only summarizes the 15 highlighted sentences, resulting in a short, dense summary of the key findings.

---

#### **Excalidraw Concept Outline Prep**

> **Synergy:** Copilot + Excalidraw + Linter

**🎯 Goal:** To convert a complex, descriptive text into a simple, multi-level bulleted outline that can be easily copy-pasted directly into Excalidraw's "Insert from Text" feature to generate a structured diagram.

**⚡ Trigger:** When a brainstorming session or conceptual note needs to be quickly converted into a visual flow chart, mind map, or diagram in Excalidraw.

**💡 Prompt:**

```
Analyze the following block of text, which describes a process or a system. Convert the entire description into a clean, hierarchical Markdown outline (using only `-` or `*` for bullets). The outline must not exceed three levels of depth. Each bullet point should be a concise phrase (max 5 words). Ensure the output is strictly Linter-compliant.

[PASTE TEXT DESCRIBING PROCESS/SYSTEM]

**Example Usage:** User pastes a description of a decision tree. Copilot returns:

- Initial State
    - Condition A Met
        - Result X
    - Condition B Met
        - Result Y
```

This is then copied into Excalidraw to instantly generate linked elements.

---

## ✍️ Creation & Elaboration

Prompts focused on drafting new content, expanding on existing ideas, and overcoming writer's block.

#### **Outline Expansion Draft**

> **Synergy:** Copilot + Text Generator + Custom Frames

**🎯 Goal:** To take a bulleted outline (Level 1, 2, 3 headings) and flesh it out into a detailed, coherent draft, ready for final polish.

**⚡ Trigger:** After completing the planning/outlining phase for a new article, report, or book chapter.

**💡 Prompt:**
```

You are an expert technical writer. Take the following Markdown outline and expand it into a detailed, professional draft. For each Level 2 heading, generate at least two paragraphs of explanatory content. Ensure the tone is authoritative and objective. Maintain the structure and headings exactly as they appear below.



# [Article Title]
## Section 1: [Topic A]
### Subpoint A.1
### Subpoint A.2
## Section 2: [Topic B]
### Subpoint B.1
```

**Example Usage:** User provides the outline. Copilot returns a fully fleshed-out draft with paragraphs inserted under each heading, ready for review.

---

#### **Fictional Scenario Generator (Idea Incubation)**

> **Synergy:** Copilot + Excalidraw + Iconize

**🎯 Goal:** To generate a narrative scenario that illustrates a core concept in the note, helping to make abstract ideas concrete and memorable (often helpful for subsequent Excalidraw concept diagrams).

**⚡ Trigger:** When a note covers a difficult or abstract concept and needs a relatable, real-world example to illustrate the principle.

**💡 Prompt:**

```
The core concept of this note is [INSERT CORE CONCEPT]. Write a short, engaging, 3-paragraph fictional narrative illustrating this concept in a common, everyday setting (e.g., a coffee shop, a garden, a train commute). Use a playful or descriptive tone.
```

**Example Usage:** Core Concept: "The Tragedy of the Commons." Copilot generates a scenario about three roommates sharing a kitchen and how their individual behavior leads to a perpetually dirty sink.

---

#### **Dataview-Informed Status Report**

> **Synergy:** Copilot + Dataview + Periodic Notes

**🎯 Goal:** To automatically draft the *Review* section of the current Weekly Note (a Periodic Note) by summarizing completed tasks and key progress from the past week.

**⚡ Trigger:** At the end of a weekly review session (e.g., Friday afternoon or Monday morning), inside the relevant Weekly Note.

**💡 Prompt:**

```
First, execute this Dataview query to gather all tasks completed in the last 7 days:
`$=dv.taskList(dv.pages("").file.tasks.where(t => t.completed AND t.completion.ts > (Date.now() - 604800000)))`

Now, based on the list of completed tasks, draft a high-level, positive summary paragraph for my "Weekly Progress" section. Focus on achievements, not failures. Identify the three most significant accomplishments from the task list and list them as a bulleted "Highlights" list.
```

**Example Usage:** The Dataview list shows 25 completed items. Copilot drafts a summary like, "This week was highly productive, with several key milestones achieved..." followed by the three most important items extracted from the task list.

---

## 🔍 Review & Resurfacing

Prompts that facilitate the review of old notes, create dynamic summaries, and help retrieve forgotten knowledge.

#### **Forgotten Knowledge Refresher**

> **Synergy:** Copilot + Dataview + Periodic Notes

**🎯 Goal:** To actively pull up and summarize notes that have been neglected (not modified in a long time) to prevent knowledge decay, linking them into the daily review process.

**⚡ Trigger:** Run this prompt inside your Daily Note (a Periodic Note) to surface notes for spaced repetition.

**💡 Prompt:**

```
Execute the following Dataview query to find knowledge that needs refreshing:
`$=dv.list(dv.pages("").where(p => (Date.now() - p.file.mtime) > 90 * 24 * 60 * 60 * 1000).sort(p => p.file.mtime, 'asc').limit(3).file.link)`

Select the oldest note from this list. Write a short, one-sentence summary of its main idea, and then pose one critical, thought-provoking question related to its content to test my current understanding. Use this format: **[LINK TO NOTE]** - [SUMMARY]. **Question:** [QUESTION]
```

**Example Usage:** Dataview finds three old notes. Copilot selects the oldest one and returns: **[[2022-11-04 Project Post-Mortem]]** - This note analyzed the failure points of the 'Phoenix' project. **Question:** Given two years of subsequent experience, what is the single biggest operational change you would implement today to prevent the failure points identified in this note?

---

#### **Task Priority Re-Evaluation**

> **Synergy:** Copilot + Tasks + Dataview

**🎯 Goal:** To review all tasks tagged with a specific priority and have Copilot suggest a revised order based on a comprehensive set of external criteria (e.g., deadlines, project health).

**⚡ Trigger:** When the existing task list feels overwhelming or the current prioritization system seems outdated.

**💡 Prompt:**

```
Execute the following Dataview query to review tasks:
`$=dv.taskList(dv.pages("").file.tasks.where(t => !t.completed AND t.tags.includes("#priority/P1")))`

Analyze the content of these P1 tasks. Based on the implied project deadlines, dependencies on other items, and resource availability (assume low resource availability), re-rank these tasks into a new, suggested order of execution (1 being highest priority). For each task, provide a one-line justification for its new ranking.
```

**Example Usage:** The query pulls 5 high-priority tasks. Copilot returns:
1. [Task A] - *Requires input from Stakeholder X, block must be cleared first.*
2. [Task C] - *No external dependencies, can be worked on while waiting for Task A.*
3. [Task B] - *Deadline is soft, can wait until Task C is complete.*

---

#### **Note Comprehension Test Generator**

> **Synergy:** Copilot + Highlighter + Text Generator

**🎯 Goal:** To instantly generate a set of flashcard-style questions and answers based on the content of the current note to aid in active recall and long-term memory retention.

**⚡ Trigger:** Immediately after completing or extensively reviewing a note (especially educational or technical content) that needs to be committed to memory.

**💡 Prompt:**

```
Read the current note. Generate five distinct "Question/Answer" pairs that test comprehension of the most important concepts. Frame the questions as short, direct recall prompts. The answers should be concise (single sentence).

**Format the output strictly as:**


Q: [Question 1]?
A: [Answer 1].

Q: [Question 2]?
A: [Answer 2].
...
```

**Example Usage:** User runs the prompt on a note about "Object-Oriented Programming Principles." Copilot generates five flashcard-ready pairs, such as "Q: What is polymorphism?" and "A: It is the ability of an object to take on many forms."

# Gemini Thinking Before Responding

**Analyzing Prompt Generation**

I'm focusing on refining the prompt generation process. Currently, I'm dissecting the request for a structured list of Copilot prompts within Obsidian. My main aim is to ensure the prompts are practical, comprehensive, and leverage the power of AI automation for PKM efficiency. I'm trying to narrow in on the essential functionalities to be addressed.


**Outlining the Ecosystem**

I'm now immersed in defining the Obsidian ecosystem specifics, nailing down the crucial plugins and their interplay. The aim is to fully exploit the plugins, ensuring a streamlined workflow. I'm currently structuring each stage, from capture to resurfacing, while brainstorming plugin combinations, focusing on Dataview and Tasks integrations for enhanced note management.


**Structuring the Blueprint**

I'm solidifying the output blueprint now, finalizing the table of contents and refining the prompt entry format. I am creating a standardized title, synergy, goal, trigger, prompt, and example for each Copilot prompt to ensure clarity and usability. I am working to establish the layout, as well as selecting plugins for the structure.


**Formulating Prompt Entries**

I'm now deep into the detailed crafting of each Copilot prompt, building on the plugin combinations. I am striving to ensure each prompt achieves a specific goal and is easy to understand. Refining each section, including Synergy, Goal, Trigger, Prompt, and Example Usage, is the aim. I'm currently focused on the capture and processing stage, with Quick Add and Callout Manager combinations.


**Mapping Potential Synergies**

I'm now expanding on the plugin synergy concepts. I'm brainstorming specific prompt ideas for each stage of the workflow. My focus is on the *Information Capture & Processing* stage. I aim to create prompt examples that leverage the Quick Add and Callout Manager combination for capturing and structuring information efficiently within Obsidian.


**Finalizing Prompt Examples**

I'm now focused on refining the 'Example Usage' sections of the prompt entries to show clear plugin synergy and concrete application. The goal is that each example demonstrates the prompt's function, while adhering to the established output blueprint. I'm aiming for a consistent style, ensuring user-friendliness, while maintaining clarity.


**Reviewing the Framework**

I'm now focused on a final assessment, ensuring all prompts adhere to the output blueprint and guiding principles. I'm checking that each section of the prompt entries is clear. The main aim is practical application, plugin synergy, and comprehensive coverage of all stages of the Obsidian workflow.


As an expert PKM Systems Integrator, I have analyzed your plugin ecosystem and developed a tailored reference guide for your Obsidian Copilot plugin. These prompts are designed to create intelligent workflows by leveraging the specific synergies between your AI engine (Copilot/Text Generator) and your structured data tools (Dataview, Tasks, Callout Manager, Excalidraw).
