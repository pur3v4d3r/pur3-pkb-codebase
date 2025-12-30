---
title: Context Windows
id: 20251111-014526
type: 🧬concept
status: active
rating: ""
source: ""
url: ""
tags:
  - permanent-note
  - permanent-note/pkb
aliases:
  - context windows
  - Context Windows
link-up:
  - "[[self-learning-and-cognitive-development-moc]]"
link-related:
  - "[[Generative Ai]]"
  - "[[Large Language Models]]"
  - "[[Prompt Engineering]]"
maturity: seedling
confidence: speculative


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

> [!definition]
> - **Key-Term**:: [[Context Windows]]
> - [**Definition**:: In the context of large language models (LLMs), this refers to the fixed-size input buffer that determines how much preceding text the model can consider when generating the next part of the sequence.]

> [!warning]
> **Critical Constraint: Context Window Limitations**
> When you enter a new prompt in a continuing conversation, the model actually reads the whole conversation from the start, assigning new weights to each token, and then formulates a response based on this new appraisal—this is how it gives the impression of being able to recall something said earlier. However, transformers have finite [[Context Windows]] that limit the total amount of text they can process. Once this limit is reached, earlier portions of the conversation are truncated, effectively causing the model to "forget" information. Effective prompt engineering must account for these memory constraints through strategic information compression and relevance prioritization.

> [!connections-and-links]
> - [[atomic-notes_moc]]: This is a link to the *Main Hub* for all **Atomic Notes**, from there you will find sections of each of the various *Subjects* I have been **working on**.
