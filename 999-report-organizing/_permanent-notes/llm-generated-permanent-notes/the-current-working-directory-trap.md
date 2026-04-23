---
title: The Current Working Directory Trap
aliases:
- The Current Working Directory Trap
- the-current-working-directory-trap
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
# The Current Working Directory Trap

> [!definition] The Current Working Directory Trap
> The Current Working Directory Trap refers to unexpected behavior in script execution due to differences in the directory from which a script is run, affecting how relative file paths are resolved.

## Practical Implications

> [!warning] The Current Working Directory Trap
> A subtle but consequential aspect of script execution is the current working directory — the directory from which the script is invoked, which determines how relative file paths are resolved. When one runs a script via the Run button, VS Code typically sets the working directory to the workspace folder root. When one runs the same script from a terminal that has navigated to a different directory, relative paths like `open("data/input.csv")` may resolve differently, producing `FileNotFoundError` exceptions that seem inexplicable because the file "is right there." The diagnostic habit to develop is: before debugging a file-path error, always check *from where* the script is being run, not just *what* path the script is trying to open. The terminal command `pwd` (on macOS/Linux) or `cd` (on Windows, with no arguments) reveals the current working directory.
> *— [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]*

## Connections

**Related:** [[python-fundamentals]] · [[vs-code]] · [[Claude-Code]] · [[software-engineering-principles]] · [[agentic-prompt-engineering-workflows]] · [[cli-tool-proficiency]] · [[command-line]] · [[basic-programming-logic]] · [[AI-Agents]] · [[complete-project-structure]] · [[Data-Visualization]] · [[architecture-patterns]] · [[claude-code-workflows]] · [[git-based-workflow]] · [[fastmcp-development-guide]] · [[Custom-MCP-Server-Development]] · [[software-engineering-workflows]] · [[building-custom-ai-agents-in-obsidian]] · [[YAML]] · [[code-review]] · [[claude-code-basics]] · [[docker-fundamentals]] · [[automation]] · [[API-Fundamentals]] · [[mcp-servers]]
---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
