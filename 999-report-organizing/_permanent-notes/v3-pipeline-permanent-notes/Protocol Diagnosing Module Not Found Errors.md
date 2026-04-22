---
title: "Protocol: Diagnosing \"Module Not Found\" Errors"
aliases: [module-not-found-error diagnosis, diagnosing module not found issues]
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

# Protocol: Diagnosing "Module Not Found" Errors

> [!definition] Protocol: Diagnosing "Module Not Found" Errors
> *Definition pending — derived from 1 source report(s).*

## Additional Material

> [!protocol] Protocol: Diagnosing "Module Not Found" Errors
> 1. **Read the error** — Note the exact module name from the `ModuleNotFoundError` traceback.
> 2. **Check active interpreter** — Look at the VS Code status bar (bottom-left) to verify which interpreter is selected. Does it point to your project's `.venv`?
> 3. **Check terminal environment** — In the terminal, run `which python` (macOS/Linux) or `where python` (Windows). Does it match the VS Code interpreter?
> 4. **Check installed packages** — Run `pip list` in the terminal. Is the missing module listed?
> 5. **If not listed** — Run `pip install module_name`, then `pip freeze > requirements.txt` to update the manifest.
> 6. **If listed but still failing** — The interpreter mismatch is the most likely cause. Ensure the terminal is using the activated virtual environment (check for the `(.venv)` prefix) and that VS Code's selected interpreter matches.
> 7. **If using a different name** — Some packages have different install names and import names (e.g., `pip install Pillow` but `import PIL`). Check the package documentation.
> *— [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]*

## Connections

**Related:** [[python-fundamentals]] · [[vs-code]] · [[vs-code]] · [[Claude-Code]] · [[building-custom-ai-agents-in-obsidian]] · [[vs-code]] · [[vs-code]] · [[software-design]] · [[architecture-patterns]] · [[cli-tool-proficiency]] · [[command-line]] · [[cli-tool-proficiency]] · [[python-fundamentals]] · [[YAML]] · [[python-fundamentals]] · [[basic-programming-logic]] · [[command-line]] · [[command-line]] · [[basic-programming-logic]] · [[software-engineering-principles]] · [[code-review]] · [[software-engineering-principles]] · [[python-fundamentals]] · [[Claude-Code]] · [[claude-code-basics]] · [[AI-Agents]] · [[agentic-prompt-engineering-workflows]] · [[claude-code-workflows]] · [[agentic-prompt-engineering-workflows]] · [[docker-fundamentals]] · [[python-fundamentals]] · [[software-engineering-principles]] · [[complete-project-structure]] · [[git-based-workflow]] · [[complete-project-structure]] · [[automation]] · [[YAML]] · [[API-Fundamentals]] · [[API-Design-Patterns]] · [[Anthropic-API]] · [[Claude-API]] · [[Data-Visualization]] · [[Claude-Code]] · [[mcp-servers]] · [[fastmcp-development-guide]] · [[FastMCP]] · [[transfer-of-learning]] · [[ai-pkb-integration]] · [[building-custom-ai-agents-in-obsidian]] · [[agentic-prompt-engineering-workflows]] · [[Custom-MCP-Server-Development]] · [[API-Cost-Optimization-Strategies]] · [[AI-Agent-Architecture]] · [[claude-code-workflows]] · [[Claude-Projects]] · [[Data-Visualization]] · [[Claude-Code]] · [[vs-code]] · [[software-engineering-principles]] · [[JSON-RPC]] · [[Client-Server-Architecture]] · [[architecture-patterns]] · [[cli-tool-proficiency]] · [[command-line]] · [[python-fundamentals]] · [[docker-fundamentals]] · [[complete-project-structure]] · [[software-engineering-principles]] · [[basic-programming-logic]] · [[python-fundamentals]] · [[code-review]] · [[Claude-Code]] · [[AI-Agents]] · [[agentic-prompt-engineering-workflows]] · [[git-based-workflow]] · [[software-engineering-workflows]] · [[Python-Type-System-and-Static-Analysis]] · [[python-fundamentals]] · [[software-engineering-principles]] · [[Python-Testing-Strategies-and-TDD]] · [[python-fundamentals]] · [[complete-project-structure]] · [[software-engineering-workflows]] · [[AI-Assisted-Development-Workflows-Comparative-Analysis]] · [[Claude-Code]] · [[AI-Agents]] · [[agentic-prompt-engineering-workflows]] · [[Python-Data-Analysis-Pipeline-Design]] · [[python-fundamentals]] · [[Data-Visualization]] · [[API-Fundamentals]] · [[MCP-Server-Development-with-Python]] · [[FastMCP]] · [[fastmcp-development-guide]] · [[mcp-servers]] · [[Custom-MCP-Server-Development]] · [[python-fundamentals]] · [[python-fundamentals]] · [[cli-tool-proficiency]] · [[basic-programming-logic]] · [[software-engineering-principles]] · [[vs-code]] · [[transfer-of-learning]] · [[fastmcp-development-guide]] · [[Custom-MCP-Server-Development]] · [[claude-code-workflows]] · [[software-engineering-workflows]] · [[Data-Visualization]] · [[git-based-workflow]] · [[AI-Agents]] · [[agentic-prompt-engineering-workflows]] · [[Claude-Code]] · [[architecture-patterns]] · [[Continuous-Integration-Continuous-Deployment]] · [[python-fundamentals]] · [[vs-code]] · [[claude-code-basics]] · [[automation]]

```dataview
LIST FROM [[Protocol Diagnosing Module Not Found Errors]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
