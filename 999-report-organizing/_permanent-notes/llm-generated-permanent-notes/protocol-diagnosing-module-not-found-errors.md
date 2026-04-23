---
title: 'Protocol: Diagnosing "Module Not Found" Errors'
aliases:
- module-not-found-error diagnosis
- diagnosing module not found issues
- 'Protocol: Diagnosing "Module Not Found" Errors'
- protocol-diagnosing-module-not-found-errors
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
# Protocol: Diagnosing "Module Not Found" Errors

> [!definition] Protocol: Diagnosing "Module Not Found" Errors
> Protocol: Diagnosing 'Module Not Found' Errors is a systematic approach to identify and resolve issues where Python modules are not recognized by the interpreter.

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

**Related:** [[python-fundamentals]] · [[vs-code]] · [[Claude-Code]] · [[software-engineering-principles]] · [[agentic-prompt-engineering-workflows]] · [[cli-tool-proficiency]] · [[command-line]] · [[basic-programming-logic]] · [[AI-Agents]] · [[complete-project-structure]] · [[Data-Visualization]] · [[architecture-patterns]] · [[claude-code-workflows]] · [[git-based-workflow]] · [[fastmcp-development-guide]] · [[Custom-MCP-Server-Development]] · [[software-engineering-workflows]] · [[building-custom-ai-agents-in-obsidian]] · [[YAML]] · [[code-review]] · [[claude-code-basics]] · [[docker-fundamentals]] · [[automation]] · [[API-Fundamentals]] · [[mcp-servers]]
---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
