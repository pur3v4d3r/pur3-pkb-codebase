---
title: 'SR Seed 5 — Application: Interpreter Mismatch Diagnosis'
aliases:
- 'SR Seed 5 — Application: Interpreter Mismatch Diagnosis'
- sr-seed-5-application-interpreter-mismatch-diagnosis
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
# SR Seed 5 — Application: Interpreter Mismatch Diagnosis

> [!definition] SR Seed 5 — Application: Interpreter Mismatch Diagnosis
> Interpreter mismatch refers to a situation where different Python interpreters are used in VS Code (e.g., from a virtual environment) compared to those invoked through the terminal, leading to discrepancies such as ImportError.

## Flashcards

> [!flashcard] SR Seed 5 — Application: Interpreter Mismatch Diagnosis
> **Q:** If a script runs successfully from the VS Code Run button but produces an ImportError when run from the terminal, what is the most likely cause?
> **A:** Interpreter mismatch — the Run button uses the interpreter selected in VS Code's status bar (which may point to the virtual environment), while the terminal's `python` command resolves through PATH, which may point to a different Python installation without the required packages. Verify by comparing the interpreter paths.
> **Source:** Sections 2-3
> **Difficulty:** Intermediate
> **Tags:** #python, #debugging, #interpreter, #PATH
> *— [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]*

## Connections

**Related:** [[python-fundamentals]] · [[vs-code]] · [[Claude-Code]] · [[software-engineering-principles]] · [[agentic-prompt-engineering-workflows]] · [[cli-tool-proficiency]] · [[command-line]] · [[basic-programming-logic]] · [[AI-Agents]] · [[complete-project-structure]] · [[Data-Visualization]] · [[architecture-patterns]] · [[claude-code-workflows]] · [[git-based-workflow]] · [[fastmcp-development-guide]] · [[Custom-MCP-Server-Development]] · [[software-engineering-workflows]] · [[building-custom-ai-agents-in-obsidian]] · [[YAML]] · [[code-review]] · [[claude-code-basics]] · [[docker-fundamentals]] · [[automation]] · [[API-Fundamentals]] · [[mcp-servers]]
---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
