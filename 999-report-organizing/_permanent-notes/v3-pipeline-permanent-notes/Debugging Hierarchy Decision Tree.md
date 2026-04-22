---
title: "Debugging Hierarchy Decision Tree"
aliases: []
type: permanent-note
status: evergreen
confidence: high
domain: Software Engineering
subdomains: [Python Development, Development Environments, AI-Augmented Programming]
tags: [permanent-note, software-engineering, python-development, development-environments, ai-augmented-programming]
created: '2026-04-22'
updated: '2026-04-22'
complexity: comprehensive foundational treatment
importance: critical
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: "3.0.0"
  source-reports: [python-development-in-vscode-with-copilot-foundational-report-2026-04-19]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Debugging Hierarchy Decision Tree

> [!definition] Debugging Hierarchy Decision Tree
> *Definition pending — derived from 1 source report(s).*

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

**Related:** [[python-fundamentals]] · [[vs-code]] · [[vs-code]] · [[Claude-Code]] · [[building-custom-ai-agents-in-obsidian]] · [[vs-code]] · [[vs-code]] · [[software-design]] · [[architecture-patterns]] · [[cli-tool-proficiency]] · [[command-line]] · [[cli-tool-proficiency]] · [[python-fundamentals]] · [[YAML]] · [[python-fundamentals]] · [[basic-programming-logic]] · [[command-line]] · [[command-line]] · [[basic-programming-logic]] · [[software-engineering-principles]] · [[code-review]] · [[software-engineering-principles]] · [[python-fundamentals]] · [[Claude-Code]] · [[claude-code-basics]] · [[AI-Agents]] · [[agentic-prompt-engineering-workflows]] · [[claude-code-workflows]] · [[agentic-prompt-engineering-workflows]] · [[docker-fundamentals]] · [[python-fundamentals]] · [[software-engineering-principles]] · [[complete-project-structure]] · [[git-based-workflow]] · [[complete-project-structure]] · [[automation]] · [[YAML]] · [[API-Fundamentals]] · [[API-Design-Patterns]] · [[Anthropic-API]] · [[Claude-API]] · [[Data-Visualization]] · [[Claude-Code]] · [[mcp-servers]] · [[fastmcp-development-guide]] · [[FastMCP]] · [[transfer-of-learning]] · [[ai-pkb-integration]] · [[building-custom-ai-agents-in-obsidian]] · [[agentic-prompt-engineering-workflows]] · [[Custom-MCP-Server-Development]] · [[API-Cost-Optimization-Strategies]] · [[AI-Agent-Architecture]] · [[claude-code-workflows]] · [[Claude-Projects]] · [[Data-Visualization]] · [[Claude-Code]] · [[vs-code]] · [[software-engineering-principles]] · [[JSON-RPC]] · [[Client-Server-Architecture]] · [[architecture-patterns]] · [[cli-tool-proficiency]] · [[command-line]] · [[python-fundamentals]] · [[docker-fundamentals]] · [[complete-project-structure]] · [[software-engineering-principles]] · [[basic-programming-logic]] · [[python-fundamentals]] · [[code-review]] · [[Claude-Code]] · [[AI-Agents]] · [[agentic-prompt-engineering-workflows]] · [[git-based-workflow]] · [[software-engineering-workflows]] · [[Python-Type-System-and-Static-Analysis]] · [[python-fundamentals]] · [[software-engineering-principles]] · [[Python-Testing-Strategies-and-TDD]] · [[python-fundamentals]] · [[complete-project-structure]] · [[software-engineering-workflows]] · [[AI-Assisted-Development-Workflows-Comparative-Analysis]] · [[Claude-Code]] · [[AI-Agents]] · [[agentic-prompt-engineering-workflows]] · [[Python-Data-Analysis-Pipeline-Design]] · [[python-fundamentals]] · [[Data-Visualization]] · [[API-Fundamentals]] · [[MCP-Server-Development-with-Python]] · [[FastMCP]] · [[fastmcp-development-guide]] · [[mcp-servers]] · [[Custom-MCP-Server-Development]] · [[python-fundamentals]] · [[python-fundamentals]] · [[cli-tool-proficiency]] · [[basic-programming-logic]] · [[software-engineering-principles]] · [[vs-code]] · [[transfer-of-learning]] · [[fastmcp-development-guide]] · [[Custom-MCP-Server-Development]] · [[claude-code-workflows]] · [[software-engineering-workflows]] · [[Data-Visualization]] · [[git-based-workflow]] · [[AI-Agents]] · [[agentic-prompt-engineering-workflows]] · [[Claude-Code]] · [[architecture-patterns]] · [[Continuous-Integration-Continuous-Deployment]] · [[python-fundamentals]] · [[vs-code]] · [[claude-code-basics]] · [[automation]]

```dataview
LIST FROM [[Debugging Hierarchy Decision Tree]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
