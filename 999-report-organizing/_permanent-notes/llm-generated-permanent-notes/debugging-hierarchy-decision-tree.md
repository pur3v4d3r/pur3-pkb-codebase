---
title: Debugging Hierarchy Decision Tree
aliases:
- Debugging Hierarchy Decision Tree
- debugging-hierarchy-decision-tree
type: permanent-note
status: evergreen
confidence: high
domain: Software Engineering
subdomains:
- Python Development
- Development Environments
- AI-Augmented Programming
tags:
- permanent-note
- software-engineering
- python-development
- development-environments
- ai-augmented-programming
created: '2026-04-22'
updated: '2026-04-22'
complexity: comprehensive foundational treatment
importance: critical
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: 3.0.0
  source-reports:
  - python-development-in-vscode-with-copilot-foundational-report-2026-04-19
  extraction-method: pkb-extractor-v1 → pipeline-v3
  definition-source: llm-filled
  definition-model: qwen2.5:7b-instruct-q5_K_M
  definition-filled-at: '2026-04-23'
---
# Debugging Hierarchy Decision Tree

> [!definition] Debugging Hierarchy Decision Tree
> Debugging Hierarchy Decision Tree is a structured approach to identifying and fixing errors in code by systematically narrowing down the source of issues through a series of yes/no questions and actions.

## Additional Material

> [!diagram] Debugging Hierarchy Decision Tree
> ```
> Script produces unexpected behavior
>           │
>           ▼
>   Is there an error message?
>      │              │
>      YES            NO (wrong output)
>      │              │
>      ▼              ▼
>   Read traceback    Set breakpoint at
>   bottom-up         suspected location
>      │              │
>      ▼              ▼
>   Identify          Run debugger (F5)
>   exception type    │
>      │              ▼
>      ▼          Inspect Variables
>   ┌──────────┐  at breakpoint
>   │SyntaxError│     │
>   │→ structure│     ▼
>   │NameError  │  Step through code
>   │→ typo/    │  watching state
>   │  import   │     │
>   │TypeError  │     ▼
>   │→ types    │  Find divergence
>   │ImportError│  between expected
>   │→ packages │  and actual values
>   └──────────┘     │
>      │              │
>      ▼              ▼
>   Fix identified cause
>      │
>      ▼
>   Re-run to verify
> ```
> *— [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]*

## Connections

**Related:** [[python-fundamentals]] · [[vs-code]] · [[Claude-Code]] · [[software-engineering-principles]] · [[agentic-prompt-engineering-workflows]] · [[cli-tool-proficiency]] · [[command-line]] · [[basic-programming-logic]] · [[AI-Agents]] · [[complete-project-structure]] · [[Data-Visualization]] · [[architecture-patterns]] · [[claude-code-workflows]] · [[git-based-workflow]] · [[fastmcp-development-guide]] · [[Custom-MCP-Server-Development]] · [[software-engineering-workflows]] · [[building-custom-ai-agents-in-obsidian]] · [[YAML]] · [[code-review]] · [[claude-code-basics]] · [[docker-fundamentals]] · [[automation]] · [[API-Fundamentals]] · [[mcp-servers]]
---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
