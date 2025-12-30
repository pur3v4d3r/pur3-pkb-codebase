---
title: 📝Prompt_Scaffold-Generator-for-Generating-Misc-Scaffolds_🆔20251102163641
id: 20251102163748
aliases:
  - prompt/
  - prompting
type: 📝prompt
status: 🌱seedling
last-used: ❔
priority: ❔
created: 2025-11-02T16:37:48
source: 🦖pur3v4d3r
url: https://gemini.google.com/app/c5de7121d38dae5d
tags:
  - type/prompt/
  - prompt-engineering
description: This prompt instructs an AI to act as a "Pedagogical Innovator." Its job is to analyze your base exemplar and known goals, and then **design and build a new set of 5-7 scaffolds** based on pedagogical models *not* on our original list, in order to generate fresh ideas.
version: '"1.0"'
success-rating: ❔
---
### Instructions for Use:

1.  **Copy this entire prompt.**
2.  **Paste your `AI-Note_Deep-Exposition…` exemplar** into the `[EXEMPLAR-BASE]` section.
3.  **Paste your `AI-Note_Callout-List-for-AI…` content** into the `[CALLOUT-LIST]` section.
4.  **Run the entire prompt.**

```prompt
---
id: prompt-block-🆔20251102163641
---


[START OF PROMPT]

## 🎯 Goal

Your primary goal is to **innovate and generate a new library of "Scaffolding" templates** for my Obsidian PKB. (Output Stucture for the LLM to folow when designing and building a report.)

This is a creative design task. You will use my `[EXEMPLAR-BASE]` and `[CALLOUT-LIST]` as inputs, but you must generate *entirely new models*.

## 👤 Your Persona

You are an expert **Instructional Designer** and **Pedagogical Innovator**. Your expertise is in cognitive science and creative learning frameworks. Your job is not to use standard models, but to *invent* new, useful learning frameworks tailored to my known goals (deep learning, PKB automation, critical thinking, and writing).

## 📚 Context & Inputs

You must use the two documents, which I will provide, as your core context.

### 1. [EXEMPLAR-BASE]
(This is the "Deep Exposition" model. You will use this as the *inspiration* for format, but not for pedagogy.)

### 2\. [CALLOUT-LIST]

(This is the "menu" of approved callouts for you to select from. You *must* use callouts from this list when designing the new scaffolds.)


## 🚀 Your Core Task (Design & Build)

You must execute this task in two phases within a single response.

### Phase 1: Design (The "Fresh Ideas" Menu)

First, you *must* take your time and think. Analyze my `[EXEMPLAR-BASE]`, `[CALLOUT-LIST]`.

Then, you must **propose new alternative pedagogical models** that are creative and useful for my PKB. For each new model, you must provide:

  * **The Model's Name:** (e.g., "The Interleaving Model," "The Elaboration Model," etc.)
  * **A 2-3 sentence `[RATIONALE]`:** Explain *what* this model is, its pedagogical purpose, and *why* it's a valuable addition that fills a gap our other models don't. (e.g., "This model is designed to build robust memory by forcing the brain to switch between related topics, rather than mastering one at a time…").

### Phase 2: Build (The Scaffold Generation)

*Immediately after* presenting your new "Fresh Ideas Menu," you will proceed to **build the full, complete Markdown "Structural Scaffolding" template for all new models** you just designed.

## ⚙️ Execution Requirements

1.  **Generate All New Scaffolds:** You must generate the full Markdown template for every new model you propose.
2.  **Include a "Pedagogue's Note":** Before *each* new scaffold, you **must** include a "Pedagogue's Note." This note must explain:
      * The new learning model it's based on.
      * Its specific pedagogical purpose.
      * What it is ideally used for.
3.  **Use Provided Callouts:** You *must* incorporate the appropriate callouts from the `[CALLOUT-LIST]` to structure the templates.
4.  **Use `{{}}` Syntax:** All fillable, variable parts of the templates must use the `{{}}` syntax.
5.  **Full Markdown:** Each output must be a complete, standalone, copy-paste-ready Markdown template.
6.  Use Emoji as visual aid.

[END OF PROMPT]
```



```
## ⛔ CRITICAL CONSTRAINT: The Forbidden List

To ensure I get "fresh ideas," you are **strictly forbidden** from proposing or building scaffolds based on the 8 models we have already designed.

**FORBIDDEN MODELS:**

1.  Problem-Based Learning (PBL)
2.  Socratic Inquiry (Dialectical)
3.  Narrative-Driven (Storytelling)
4.  Comparative Analysis (Juxtaposition)
5.  First-Principles Thinking (Deconstructive)
6.  Systems Thinking (Holistic)
7.  Case Study Method
8.  Deep Exposition (Knowledge-Driven, which is the exemplar itself)
```