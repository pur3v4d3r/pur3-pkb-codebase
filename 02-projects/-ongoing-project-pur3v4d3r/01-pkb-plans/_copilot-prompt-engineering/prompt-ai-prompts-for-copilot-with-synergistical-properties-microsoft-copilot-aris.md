---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Microsoft-Copilot_Aris
aliases:
  - AI Prompts for Obsidian - Microsoft Copilot Aris
  - Microsoft Copilot Prompt Library - Aris
  - Synergistic Copilot Prompts - Microsoft Aris
tags:
  - prompt-engineering/llm/library
  - tools/ai/microsoft-copilot
  - tools/obsidian/copilot
  - workflows/pkm/automation
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]"
related:
  - "[[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]"
date created: Monday, September 29th 2025, 12:02:39 am
date modified: Monday, September 29th 2025, 12:17:55 am
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
[^20]: [[ref_gemini-prompt_guide-to-obsidian-plug-in-quickadd_2025-09-24]]

> [!the-purpose]
> This is a prompt created using the Elias Prompt Architect Gem, its purpose is to generate Synergistical Prompts using my current Obsidian Plugins.
> - These are some important reference links:
> 
>   - [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]] - This is a link to the original Prompt used.
> 
>   - [[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]- This is a link to Persona that was use to create this. 

# Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Microsoft-Copilot_Aris

# 🧠 Obsidian Copilot Prompt Library

### _Intelligent Workflows for Personal Knowledge Management_

---

## 📚 Table of Contents

- 📥 Information Capture & Processing
- 🧠 Synthesis & Connection
- ✍️ Creation & Elaboration
- 🔍 Review & Resurfacing

---

## 📥 Information Capture & Processing

---

#### **Smart Source Summarizer**

> **Synergy:** Copilot + Highlighter + Text Generator

**🎯 Goal:** To quickly summarize highlighted sections of a dense article or research paper.

**⚡ Trigger:** When processing a dense article and you've highlighted key sections using the Highlighter plugin.

**💡 Prompt:**

```
Summarize the following highlighted content into a concise overview. Focus on key arguments, evidence, and implications.

{{selection}}
```

**Example Usage:** After highlighting several paragraphs in a research note, the user runs this prompt. Copilot returns a 3-paragraph summary capturing the main ideas and conclusions.

---

#### **Contextual Note Generator**

> **Synergy:** Copilot + QuickAdd + Periodic Notes

**🎯 Goal:** To generate a context-aware note based on the current day’s focus or reading.

**⚡ Trigger:** When creating a new daily note and want to capture insights from recent readings or meetings.

**💡 Prompt:**

```
Create a new note titled "[TOPIC]" using today's periodic note as context. Include a summary of recent related notes and suggest 2 follow-up questions.

Today's context:
{{selection}}
```

**Example Usage:** On September 29th, the user runs this prompt with a selection from the daily note. Copilot creates a new note titled "AI Ethics" with a summary of recent discussions and two questions for further exploration.

---

#### **Tag-Based Intake Organizer**

> **Synergy:** Copilot + Tag Wrangler + Dataview

**🎯 Goal:** To organize newly captured notes based on their tags and suggest appropriate folders or links.

**⚡ Trigger:** After importing or writing several new notes that need to be categorized.

**💡 Prompt:**

```
Analyze the following notes and their tags. Suggest appropriate folders, backlinks, and related notes from the vault.

{{selection}}
```

**Example Usage:** The user selects 3 new notes tagged with `#philosophy`, `#AI`, and `#ethics`. Copilot suggests placing them in the "AI Ethics" folder and links them to existing notes on "Moral Machines" and "Turing Test".

---

#### **Visual Capture Companion**

> **Synergy:** Copilot + Excalidraw + Custom Frames

**🎯 Goal:** To generate a textual summary or outline from a visual diagram.

**⚡ Trigger:** After creating a mind map or flowchart in Excalidraw.

**💡 Prompt:**

```
Interpret the following Excalidraw diagram and generate a structured outline or summary. Focus on relationships and key nodes.

{{selection}}
```

**Example Usage:** The user selects a flowchart showing a decision-making process. Copilot returns a bullet-point outline summarizing each step and its dependencies.

---

## 🧠 Synthesis & Connection

---

#### **Insight Synthesizer**

> **Synergy:** Copilot + Dataview + Periodic Notes

**🎯 Goal:** To synthesize insights from multiple notes over a time period.

**⚡ Trigger:** At the end of a week or month to reflect on accumulated knowledge.

**💡 Prompt:**

```
Review all notes created in the past [TIMEFRAME] using Periodic Notes. Identify recurring themes, surprising insights, and unanswered questions.

Use this Dataview query:
`$=dv.pages('"[TIMEFRAME]"').where(p => p.file.name != null)`

Summarize findings in 3 sections: Themes, Insights, Questions.
```

**Example Usage:** At the end of September, the user runs this prompt. Copilot returns a synthesis of themes like "AI Ethics", insights such as "Bias in LLMs", and questions like "How can transparency be enforced?"

---

#### **Connection Mapper**

> **Synergy:** Copilot + Dataview + Tasks

**🎯 Goal:** To uncover hidden connections between notes based on shared tags and incomplete tasks.

**⚡ Trigger:** When exploring a topic with scattered notes and tasks.

**💡 Prompt:**

```
Find all notes tagged with [TAG] and list any incomplete tasks. Then, identify connections between these notes based on shared keywords or linked mentions.

Suggest a new note that could unify these ideas.
```

**Example Usage:** The user inputs `#creativity`. Copilot finds 5 notes with open tasks and suggests a new note titled "Creative Flow Systems" linking them together.

---

#### **Idea Expansion Engine**

> **Synergy:** Copilot + Text Generator + Callout Manager

**🎯 Goal:** To expand on a brief idea or note into a more developed concept.

**⚡ Trigger:** When you have a short note or fleeting idea that needs elaboration.

**💡 Prompt:**

```
Expand the following idea into a detailed concept note. Use callouts to highlight key points, examples, and potential applications.

{{selection}}
```

**Example Usage:** The user selects a note titled "Digital Mind Gardens". Copilot returns a 500-word elaboration with callouts for "Growth", "Pruning", and "Cross-Pollination".

---

## ✍️ Creation & Elaboration

---

#### **Writer’s Block Breaker**

> **Synergy:** Copilot + Text Generator + Style Settings

**🎯 Goal:** To overcome writer’s block by generating multiple stylistic drafts.

**⚡ Trigger:** When stuck on how to start or continue writing a note.

**💡 Prompt:**

```
Generate 3 stylistic variations of the following paragraph. Use different tones: academic, conversational, and poetic.

{{selection}}
```

**Example Usage:** The user selects a paragraph on "AI and Consciousness". Copilot returns three versions: one citing research, one using metaphors, and one with a casual tone.

---

#### **Structured Note Composer**

> **Synergy:** Copilot + QuickAdd + Linter

**🎯 Goal:** To create a clean, well-structured note from a rough draft.

**⚡ Trigger:** After dumping raw thoughts into a note.

**💡 Prompt:**

```
Clean up and structure the following rough note. Apply markdown formatting, headings, and linting rules.

{{selection}}
```

**Example Usage:** The user selects a messy note on "PKM Workflows". Copilot returns a clean version with sections like "Capture", "Synthesis", and "Review".

---

#### **Callout-Based Argument Builder**

> **Synergy:** Copilot + Callout Manager + Text Generator

**🎯 Goal:** To build a persuasive argument using structured callouts.

**⚡ Trigger:** When drafting an essay or opinion piece.

**💡 Prompt:**

```
Construct a persuasive argument on [TOPIC] using callouts for each of the following: Claim, Evidence, Counterpoint, Rebuttal, Conclusion.
```

**Example Usage:** The user inputs "AI Regulation". Copilot returns a note with callouts for each argument component, ready for refinement.

---

## 🔍 Review & Resurfacing

---

#### **Forgotten Note Resurrector**

> **Synergy:** Copilot + Dataview + Homepage

**🎯 Goal:** To surface old notes that haven’t been modified recently but are still relevant.

**⚡ Trigger:** When refreshing your homepage or dashboard.

**💡 Prompt:**

```
Find notes not modified in the last [X] days but tagged with [TAG]. Summarize each and suggest how they could be updated or linked to current work.

Use this Dataview query:
`$=dv.pages('#[TAG]').where(p => p.file.mtime < dv.date("today") - [X])`
```

**Example Usage:** The user inputs `#philosophy` and `30`. Copilot returns 3 notes with summaries and suggestions like "Link to recent AI ethics note".

---

#### **Task-Based Review Companion**

> **Synergy:** Copilot + Tasks + Periodic Notes

**🎯 Goal:** To review completed and pending tasks from a specific time period.

**⚡ Trigger:** At the end of a week or month.

**💡 Prompt:**

```
Review all tasks from the past [TIMEFRAME]. List completed tasks, pending ones, and suggest 2 priorities for next week.

Use this Tasks query:
`task from "[TIMEFRAME]"`
```

**Example Usage:** The user inputs "Week of Sept 22–28". Copilot returns a task summary and suggests focusing on "Finalize Q4 Report" and "Review AI Ethics draft".

---

#### **Note Summary Generator**

> **Synergy:** Copilot + Dataview + Text Generator

**🎯 Goal:** To generate summaries for a batch of notes for easier review.

**⚡ Trigger:** When preparing for a knowledge review session.

**💡 Prompt:**

```
Summarize the following notes. For each, provide a 2-sentence summary and list 3 keywords.

{{selection}}
```

**Example Usage:** The user selects 5 notes. Copilot returns summaries like:

- "Digital Mind Gardens": A metaphor for PKM systems. Keywords: growth, pruning, emergence.

---

Would you like this exported as a Markdown file for direct use in your vault? Or should we expand this library with even more advanced workflows?
