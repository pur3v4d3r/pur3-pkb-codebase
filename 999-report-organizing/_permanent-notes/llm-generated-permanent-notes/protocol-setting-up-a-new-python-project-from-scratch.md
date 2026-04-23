---
title: 'Protocol: Setting Up a New Python Project from Scratch'
aliases:
- initializing a new python project
- python project setup
- 'Protocol: Setting Up a New Python Project from Scratch'
- protocol-setting-up-a-new-python-project-from-scratch
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
# Protocol: Setting Up a New Python Project from Scratch

> [!definition] Protocol: Setting Up a New Python Project from Scratch
> Protocol: Setting Up a New Python Project from Scratch is a series of steps to initialize a project in VS Code with a virtual environment, basic directory structure, version control setup, and initial configuration for development.

## Additional Material

> [!protocol] Protocol: Setting Up a New Python Project from Scratch
> 1. **Create project directory** — Create a new folder with a descriptive kebab-case name. Open it in VS Code with `File > Open Folder`.
> 2. **Create virtual environment** — Open the integrated terminal (`Ctrl+`` `) and run `python -m venv .venv`.
> 3. **Activate the environment** — Run `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux). Verify the `(.venv)` prompt prefix appears.
> 4. **Select interpreter in VS Code** — Press `Ctrl+Shift+P`, type "Python: Select Interpreter", choose the `.venv` interpreter. This connects Pylance's analysis to the project's environment.
> 5. **Create project structure** — Create `src/`, `tests/`, and `data/` directories as needed.
> 6. **Initialize Git** — Run `git init`, create a `.gitignore` file with `.venv/`, `__pycache__/`, `*.pyc`, and any platform-specific entries.
> 7. **Install dependencies** — Use `pip install package_name` for each required library, then `pip freeze > requirements.txt` to capture the dependency state.
> 8. **Create initial files** — Start with `src/main.py` as the entry point. Write a descriptive comment or docstring as the first content to establish Copilot context.
> 9. **Configure debugging** — Create `.vscode/launch.json` with a "Python: Current File" configuration (VS Code can generate this automatically via the Run and Debug sidebar).
> 10. **First commit** — Stage all files in Source Control, write a descriptive commit message, commit.
> *— [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]*

## Connections

**Related:** [[python-fundamentals]] · [[vs-code]] · [[Claude-Code]] · [[software-engineering-principles]] · [[agentic-prompt-engineering-workflows]] · [[cli-tool-proficiency]] · [[command-line]] · [[basic-programming-logic]] · [[AI-Agents]] · [[complete-project-structure]] · [[Data-Visualization]] · [[architecture-patterns]] · [[claude-code-workflows]] · [[git-based-workflow]] · [[fastmcp-development-guide]] · [[Custom-MCP-Server-Development]] · [[software-engineering-workflows]] · [[building-custom-ai-agents-in-obsidian]] · [[YAML]] · [[code-review]] · [[claude-code-basics]] · [[docker-fundamentals]] · [[automation]] · [[API-Fundamentals]] · [[mcp-servers]]
---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
