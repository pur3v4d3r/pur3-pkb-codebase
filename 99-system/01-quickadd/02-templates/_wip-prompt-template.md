---
type: "prompt"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "<% await tp.system.suggester(
    ["Claude-Sonnet-4.5", "Claude-Opus-4.1", "Gemini-3.0-Pro", "Gemini-3.0-Flash", "Pur3v4d3r", "Other"], 
    ["claude-sonnet-4.5", "claude-opus-4.1", "gemini-3.0-pro", "gemini-3.0-flash", "pur3v4d3r", "other"], 
    false, 
    "Source of prompt?:"
    ) %>"
title: "<% await tp.system.prompt("Title of prompt for YAML?") %>"
description: "<% await tp.system.prompt("What is this prompts purpose?") %>"
key-takeaway: "<% await tp.system.prompt("What is this prompts key feature?") %>"
last-used: "[[<% tp.date.now("YYYY-MM-DD") %>]]"
tags:
  - "year/2025"
  - "prompt-engineering"
  - "llm-capability/generation"
  - "prompt-workflow/deployment"
aliases:
  - "Prompt"
  - "Prompt-Engineering"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
  - "[[<% tp.date.now("gggg-[W]WW") %>|Weekly Review]]"
---



[Initial Creation: [[<% tp.date.now("YYYY-MM-DD") %>|<% tp.date.now("dddd, MMMM Do, YYYY") %>]]]

---

### <% tp.file.title %>

`````prompt
----
Prompt-ID: <% tp.date.now("YYYYMMDDHH") %>
Prompt-Title: [[<% tp.file.title %>]]
Prompt-Version: 1.0.0
Prompt-Rating: 0.0
----

{{PASTE PROMPT HERE}}

# Prompt: <% tp.system.prompt("Enter prompt title or purpose:") %>

## Purpose
<% tp.system.prompt("Describe the purpose or goal of this prompt:") %>

## Role
<% tp.system.prompt("What role should the model assume? (e.g., expert, assistant, critic)") %>

## Context
<% tp.system.prompt("Provide background or context for the prompt:") %>

## Instructions
<% tp.system.prompt("Define the core instructions or task:") %>

## Constraints
<% tp.system.prompt("List any constraints or boundaries (e.g., tone, format, length):") %>

## Output Format
<% tp.system.prompt("Specify the desired output format:") %>

## Examples (Optional)
<% tp.system.prompt("Provide example input/output pairs if applicable:") %>

## Metadata
- **Source Model(s):** <% tp.system.suggester(["claude-sonnet-4.5", "claude-opus-4.1", "gemini-pro-3.0", "gemini-flash-2.5"], ["claude-sonnet-4.5", "claude-opus-4.1", "gemini-pro-3.0", "gemini-flash-2.5"], false, "Select model(s):") %>
- **Status:** Active
- **Maturity:** Seedling

## Next Steps
- [ ] Test with sample inputs
- [ ] Refine based on results
- [ ] Document in [[prompt-engineering-moc]]

`````