---
title: Standard Python Project Structure
aliases:
- Python project structure
- PEP 8 recommended structure
- Standard Python Project Structure
- standard-python-project-structure
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
# Standard Python Project Structure

> [!definition] Standard Python Project Structure
> A Standard Python Project Structure is a conventionally organized directory layout that includes source code, tests, configuration files, and documentation, designed to facilitate development and tooling integration.

## Examples

> [!example] Standard Python Project Structure
> A well-organized Python project in VS Code follows a [[complete-project-structure|conventional structure]] that makes the project's organization immediately legible:
> ```
> my-project/
> ├── .venv/                  # Virtual environment (gitignored)
> ├── .vscode/
> │   ├── settings.json       # Workspace settings
> │   └── launch.json         # Debug configurations
> ├── src/                    # Source code
> │   ├── __init__.py         # Package marker
> │   ├── main.py             # Entry point
> │   └── utils.py            # Utility functions
> ├── tests/                  # Test files
> │   └── test_utils.py       # Tests for utils.py
> ├── data/                   # Data files (may be gitignored)
> ├── .gitignore              # Git exclusion rules
> ├── requirements.txt        # Dependency manifest
> └── README.md               # Project documentation
> ```
> Each directory serves a specific function in the project's lifecycle: `src/` contains code, `tests/` contains verification, `.vscode/` contains environment configuration, and the root-level files (`requirements.txt`, `.gitignore`, `README.md`) document the project's dependencies, exclusions, and purpose. This structure is not arbitrary — it reflects conventions that Python tooling (pytest, pip, import resolution) expects, and deviating from it typically requires explicit configuration to compensate.
> *— [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]*

## Connections

**Related:** [[python-fundamentals]] · [[vs-code]] · [[Claude-Code]] · [[software-engineering-principles]] · [[agentic-prompt-engineering-workflows]] · [[cli-tool-proficiency]] · [[command-line]] · [[basic-programming-logic]] · [[AI-Agents]] · [[complete-project-structure]] · [[Data-Visualization]] · [[architecture-patterns]] · [[claude-code-workflows]] · [[git-based-workflow]] · [[fastmcp-development-guide]] · [[Custom-MCP-Server-Development]] · [[software-engineering-workflows]] · [[building-custom-ai-agents-in-obsidian]] · [[YAML]] · [[code-review]] · [[claude-code-basics]] · [[docker-fundamentals]] · [[automation]] · [[API-Fundamentals]] · [[mcp-servers]]
---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
