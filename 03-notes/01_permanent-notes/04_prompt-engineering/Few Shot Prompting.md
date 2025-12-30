---
title: Few-Shot Prompting
id: 20251111-024357
type: 🧬concept
status: active
rating: ""
source: ""
url: ""
tags:
  - permanent-note
  - permanent-note/pkb
aliases:
  - Few-Shot Prompting
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
> - **Key-Term**:: [[Few-Shot Prompting]]
> - [**Definition**:: Few-shot prompting is a technique for providing LLMs with a few examples of the desired output in addition to the prompt, helping the model better understand the task and generate more accurate and informative responses.]

By including exemplars within the prompt itself, practitioners can demonstrate the specific format, style, tone, or reasoning pattern they expect the model to replicate. This approach leverages the [[In-Context Learning]] capabilities of large language models—their ability to adapt behavior based on examples provided within the input context without requiring parameter updates.

Example construction follows specific best practices. Each example should be complete and well-formed, demonstrating the full transformation from input to output. Examples should progress from simpler to more complex instances when possible, allowing the model to build understanding incrementally. We should provide vast and different examples to the model instead of multiple similar examples, ensuring the model learns as much as possible about the task. When examples include edge cases or potential error modes, explicitly showing how these should be handled proves particularly valuable for improving model robustness.

> [!use-cases-and-examples]
> **Real-World Application: Few-Shot for Specialized Formatting**
> 1. **Context**: A research organization needs to extract structured data from academic papers into a standardized JSON format.
> 2. **Application**: The prompt includes 3-4 complete examples showing papers with varying structures and their corresponding JSON representations, demonstrating how to handle missing fields, multiple authors, and different citation formats.
> 3. **Outcome**: The model reliably produces correctly structured JSON outputs even for novel paper formats not explicitly demonstrated, having learned the underlying structural logic from the examples.

> [!connections-and-links]
> - [[atomic-notes_moc]]: This is a link to the *Main Hub* for all **Atomic Notes**, from there you will find sections of each of the various *Subjects* I have been **working on**.
