---
title: 📝Prompt_Generate-Emoji-Reference-List_🆔20251019185235
id: 20251019185257
aliases:
  - prompt
  - prompt-engineering
  - prompting
  - prompts
type: 📝prompt
status: ⚡active
priority: ⁉️
created: 2025-10-19T18:52:57
source: gemini-2.5-pro
url: https://chatgpt.com/c/68f56c2a-aeb8-8325-9b16-f5010a7509e6
tags:
  - type/prompt
  - prompt-engineering
  - prompt-engineering
  - type/prompt
description: Generate a useful emoji reference table for use inside of the PKB. There is a section that explains how to make this prompt reusable as well.
version: "1.0"
success-rating: "10.0"
date created: 2025-10-19T18:52:56.000-04:00
date modified: 2025-10-19T19:12:17.971-04:00
---

> [!insight]
> **How to Make it Reusable:** This prompt is now a template. You can easily adapt it to create other reference documents. Simply change the content in the `Task` section. For example, you could replace "emojis" with "keyboard shortcuts for my top 5 apps" or "a list of special characters (like Greek letters or mathematical symbols)" and the prompt's structure would generate an equally useful, searchable reference note for that topic.

```prompt
---
id: prompt-block-🆔20251019185235
---

# Role: Information Architect

You are an expert Information Architect specializing in designing clear, functional, and user-friendly reference documents for digital knowledge management systems like Obsidian.

# Context:

I am building a Personal Knowledge Base (PKB) in Obsidian. I need a single, comprehensive reference note containing a list of commonly used emojis. The goal is to keep this note open in a sidebar and quickly find/copy emojis for my notes.

The document must be highly scannable, well-organized, and easily searchable using Obsidian's built-in find function (`Ctrl+F`). It should also be designed so I can easily add my own frequently used emojis to a dedicated section at the top.

# Task:

Create a comprehensive emoji reference guide formatted in clean, Obsidian-ready Markdown. Fulfill the following steps precisely:

1.  **Create a "User Favorites" Section:**
    * Start the document with a level 2 heading: `## My Favorites`.
    * Under this heading, create an empty Markdown table with the columns: `| Emoji | My Keyword |`.
    * Populate the table with 5 empty rows as a template for me to fill in later.

2.  **Create Comprehensive Emoji Categories:**
    * Create a level 2 heading for the main list: `## Emoji Reference`.
    * Generate a comprehensive list of emojis organized into logical categories. Each category must be a level 3 heading (e.g., `### Smileys & People`, `### Animals & Nature`, `### Food & Drink`, `### Activities`, `### Travel & Places`, `### Objects`, `### Symbols`, `### Flags`).

3.  **Format Each Category as a Table:**
    * Under each category heading, present the emojis in a Markdown table.
    * The table must have exactly three columns: `Emoji`, `Unicode Name`, and `Keywords`.
    * The `Keywords` column is crucial. It should contain a comma-separated list of 3-5 relevant, searchable keywords for each emoji (e.g., for `🚀`, keywords could be `rocket, space, launch, ship, fast`).

# Constraints:

* The entire output must be in Markdown format.
* Do not include any introductory or concluding text outside of the document itself.
* Ensure all emojis render correctly.
* Use `##` for top-level sections and `###` for emoji categories.

# Example of a Correctly Formatted Table Row:

| Emoji | Unicode Name      | Keywords                         |
| :---: | :---------------- | :------------------------------- |
| ✨    | Sparkles          | magic, glitter, star, shiny, new |

Begin generating the document now.

```
