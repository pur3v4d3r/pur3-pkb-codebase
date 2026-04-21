---
title: "Protocol: Setting Up a New Python Project from Scratch"
aliases: []
type: permanent-note
status: evergreen
confidence: high
domain: Software Engineering
subdomains: [Python Development, Development Environments, AI-Augmented Programming]
tags: [permanent-note, software-engineering, python-development, development-environments, ai-augmented-programming]
created: '2026-04-21'
updated: '2026-04-21'
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

# Protocol: Setting Up a New Python Project from Scratch

> [!definition] Protocol: Setting Up a New Python Project from Scratch
> *Definition pending — derived from 1 source report(s).*

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

**Related:** [[Python-Fundamentals]] · [[vs-code]] · [[vs-code]] · [[Claude-Code]] · [[Building-Custom-AI-Agents-in-Obsidian]] · [[vs-code]] · [[vs-code]] · [[Software-Design]] · [[Architecture-Patterns]] · [[CLI-Tool-Proficiency]] · [[command-line]] · [[CLI-Tool-Proficiency]] · [[Python-Fundamentals]] · [[YAML]] · [[Python-Fundamentals]] · [[Basic-Programming-Logic]] · [[command-line]] · [[command-line]] · [[Basic-Programming-Logic]] · [[Software-Engineering-Principles]] · [[Code-Review]] · [[Software-Engineering-Principles]] · [[Python-Fundamentals]] · [[Claude-Code]] · [[claude-code-basics]] · [[AI-Agents]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Claude-Code-Workflows]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Docker-Fundamentals]] · [[Python-Fundamentals]] · [[Software-Engineering-Principles]] · [[complete-project-structure]] · [[git-based-workflow]] · [[complete-project-structure]] · [[automation]] · [[YAML]] · [[API-Fundamentals]] · [[API-Design-Patterns]] · [[Anthropic-API]] · [[Claude-API]] · [[Data-Visualization]] · [[Claude-Code]] · [[mcp-servers]] · [[FastMCP-Development-Guide]] · [[FastMCP]] · [[transfer-of-learning]] · [[ai-pkb-integration]] · [[Building-Custom-AI-Agents-in-Obsidian]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Custom-MCP-Server-Development]] · [[API-Cost-Optimization-Strategies]] · [[AI-Agent-Architecture]] · [[Claude-Code-Workflows]] · [[Claude-Projects]] · [[Data-Visualization]] · [[Claude-Code]] · [[vs-code]] · [[Software-Engineering-Principles]] · [[JSON-RPC]] · [[Client-Server-Architecture]] · [[Architecture-Patterns]] · [[CLI-Tool-Proficiency]] · [[command-line]] · [[Python-Fundamentals]] · [[Docker-Fundamentals]] · [[complete-project-structure]] · [[Software-Engineering-Principles]] · [[Basic-Programming-Logic]] · [[Python-Fundamentals]] · [[Code-Review]] · [[Claude-Code]] · [[AI-Agents]] · [[Agentic-Prompt-Engineering-Workflows]] · [[git-based-workflow]] · [[Software-Engineering-Workflows]] · [[Python-Type-System-and-Static-Analysis]] · [[Python-Fundamentals]] · [[Software-Engineering-Principles]] · [[Python-Testing-Strategies-and-TDD]] · [[Python-Fundamentals]] · [[complete-project-structure]] · [[Software-Engineering-Workflows]] · [[AI-Assisted-Development-Workflows-Comparative-Analysis]] · [[Claude-Code]] · [[AI-Agents]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Python-Data-Analysis-Pipeline-Design]] · [[Python-Fundamentals]] · [[Data-Visualization]] · [[API-Fundamentals]] · [[MCP-Server-Development-with-Python]] · [[FastMCP]] · [[FastMCP-Development-Guide]] · [[mcp-servers]] · [[Custom-MCP-Server-Development]] · [[Python-Fundamentals]] · [[Python-Fundamentals]] · [[CLI-Tool-Proficiency]] · [[Basic-Programming-Logic]] · [[Software-Engineering-Principles]] · [[vs-code]] · [[transfer-of-learning]] · [[FastMCP-Development-Guide]] · [[Custom-MCP-Server-Development]] · [[Claude-Code-Workflows]] · [[Software-Engineering-Workflows]] · [[Data-Visualization]] · [[git-based-workflow]] · [[AI-Agents]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Claude-Code]] · [[Architecture-Patterns]] · [[Continuous-Integration-Continuous-Deployment]] · [[Python-Fundamentals]] · [[vs-code]] · [[claude-code-basics]] · [[automation]]

```dataview
LIST FROM [[Protocol Setting Up a New Python Project from Scratch]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
