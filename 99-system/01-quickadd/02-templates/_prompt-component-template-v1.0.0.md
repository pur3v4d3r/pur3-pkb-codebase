---
type: "prompt-component"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "<% await tp.system.suggester(
    ["Claude-Sonnet", "Claude-Opus", "Gemini-Pro", "Gemini-Flash", "Pur3v4d3r", "Local-LLM"], 
    ["claude-sonnet", "claude-opus", "gemini-pro", "gemini-flash", "pur3v4d3r", "local-llm"], 
    false, 
    "Source of component?:"
    ) %>"
title: "<% await tp.system.prompt("Title of component for YAML?") %>"
description: "<% await tp.system.prompt("What is this component's purpose?") %>"
key-takeaway: "<% await tp.system.prompt("What is this component's key feature?") %>"
last-used: "[[<% tp.date.now("YYYY-MM-DD") %>]]"
tags:
  - "year/<% tp.date.now("YYYY") %>"
  - "llm-capability/generation"
  - "prompt-workflow/deployment"
  - "prompt-pattern"
  - "prompt-engineering/anatomy"
aliases:
  - <% tp.file.title %>
  - "Prompt-Engineering"
  - "Prompt Component"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
  - "[[<% tp.date.now("gggg-[W]WW") %>|Weekly Review]]"
---




[Initial Creation: [[<% tp.date.now("YYYY-MM-DD") %>|<% tp.date.now("dddd, MMMM Do, YYYY") %>]]]

---

# <% tp.file.title %>

`````prompt-component
----
Prompt-Component-ID: "<% tp.date.now("YYYYMMDDHH") %>"
Prompt-Component-Version: 1.0.0
----

{{PASTE PROMPT-COMPONENT HERE}}

`````
