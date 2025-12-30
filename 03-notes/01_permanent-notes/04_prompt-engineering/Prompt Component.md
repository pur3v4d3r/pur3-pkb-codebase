---
title: Prompt-Component
id: 20251109-202223
type: 🧬concept
status: active
rating: ""
source: ""
url: ""
tags:
  - permanent-note
  - permanent-note/project-pur3v4d3r
  - permanent-note/pkb
aliases:
  - prompt component
  - prompt components
  - Prompt-Component
  - Prompt Component
link-up:
  - "[[self-learning-and-cognitive-development-moc]]"
link-related: []
maturity: seedling
confidence: speculative


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

> [!definition]
> - **Key-Term**:: [[Prompt-Component]]
> - [**Definition**:: Is one of several individual elements that can be combined to form an effective prompt (input instruction) for a large language model (LLM) or other generative AI. These components provide structure, clarity, and context to guide the AI in generating a desired response.Used in a prompt [[Prompt Template]]]
> 	- An atomic, standalone markdown file in an Obsidian vault containing a single, discrete piece of a prompt (e.g., a role, a task, a formatting instruction).

> [!equation]
> **Component Architecture Formula**
> $Component = Metadata + Content + Relations + Versioning$
> Where each element contributes to the component's discoverability and usability

> [!core-principle]
> **Fundamental Design Tenet**
> Every component must be **self-contained**, **purpose-driven**, and **composition-ready**—capable of functioning independently while designed for combination with other components.

| Component Type | File Name Example          | Content Example (inside the file)                   | Purpose                                                                 |
| -------------- | -------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------- |
| **Role**       | `role.system_architect.md` | `You are a world-class systems architect…`          | Defines the persona, expertise, and voice of the AI.                    |
| **Task**       | `task.analyze_critique.md` | `Analyze the following text for logical flaws…`     | Provides the primary, high-level instruction or verb.                   |
| **Format**     | `format.json_strict.md`    | `Provide your final output *only* in a valid JSON…` | Constrains the output to a specific, machine-readable format.           |
| **Context**    | `context.style_guide.md`   | `[Company Style Guide Text]…`                       | Provides static, reusable context (e.g., style guides, project briefs). |
| **Meta**       | `meta.chain_of_thought.md` | `Think step-by-step before providing…`              | Injects instructions about the AI's *process*.                          |
| **Variable**   | `var.topic.md`             | `{{TOPIC}}`                                         | A placeholder meant to be replaced by the user during assembly.         |


> [!connections-and-links]
> - [[atomic-notes_moc]]: This is a link to the *Main Hub* for all **Atomic Notes**, from there you will find sections of each of the various *Subjects* I have been **working on**.
