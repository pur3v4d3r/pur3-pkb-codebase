---
title: "Protocol: Diagnosing \"Module Not Found\" Errors"
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

**Related:** [[Python-Fundamentals]] · [[vs-code]] · [[vs-code]] · [[Claude-Code]] · [[Building-Custom-AI-Agents-in-Obsidian]] · [[vs-code]] · [[vs-code]] · [[Software-Design]] · [[Architecture-Patterns]] · [[CLI-Tool-Proficiency]] · [[command-line]] · [[CLI-Tool-Proficiency]] · [[Python-Fundamentals]] · [[YAML]] · [[Python-Fundamentals]] · [[Basic-Programming-Logic]] · [[command-line]] · [[command-line]] · [[Basic-Programming-Logic]] · [[Software-Engineering-Principles]] · [[Code-Review]] · [[Software-Engineering-Principles]] · [[Python-Fundamentals]] · [[Claude-Code]] · [[claude-code-basics]] · [[AI-Agents]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Claude-Code-Workflows]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Docker-Fundamentals]] · [[Python-Fundamentals]] · [[Software-Engineering-Principles]] · [[complete-project-structure]] · [[git-based-workflow]] · [[complete-project-structure]] · [[automation]] · [[YAML]] · [[API-Fundamentals]] · [[API-Design-Patterns]] · [[Anthropic-API]] · [[Claude-API]] · [[Data-Visualization]] · [[Claude-Code]] · [[mcp-servers]] · [[FastMCP-Development-Guide]] · [[FastMCP]] · [[transfer-of-learning]] · [[ai-pkb-integration]] · [[Building-Custom-AI-Agents-in-Obsidian]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Custom-MCP-Server-Development]] · [[API-Cost-Optimization-Strategies]] · [[AI-Agent-Architecture]] · [[Claude-Code-Workflows]] · [[Claude-Projects]] · [[Data-Visualization]] · [[Claude-Code]] · [[vs-code]] · [[Software-Engineering-Principles]] · [[JSON-RPC]] · [[Client-Server-Architecture]] · [[Architecture-Patterns]] · [[CLI-Tool-Proficiency]] · [[command-line]] · [[Python-Fundamentals]] · [[Docker-Fundamentals]] · [[complete-project-structure]] · [[Software-Engineering-Principles]] · [[Basic-Programming-Logic]] · [[Python-Fundamentals]] · [[Code-Review]] · [[Claude-Code]] · [[AI-Agents]] · [[Agentic-Prompt-Engineering-Workflows]] · [[git-based-workflow]] · [[Software-Engineering-Workflows]] · [[Python-Type-System-and-Static-Analysis]] · [[Python-Fundamentals]] · [[Software-Engineering-Principles]] · [[Python-Testing-Strategies-and-TDD]] · [[Python-Fundamentals]] · [[complete-project-structure]] · [[Software-Engineering-Workflows]] · [[AI-Assisted-Development-Workflows-Comparative-Analysis]] · [[Claude-Code]] · [[AI-Agents]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Python-Data-Analysis-Pipeline-Design]] · [[Python-Fundamentals]] · [[Data-Visualization]] · [[API-Fundamentals]] · [[MCP-Server-Development-with-Python]] · [[FastMCP]] · [[FastMCP-Development-Guide]] · [[mcp-servers]] · [[Custom-MCP-Server-Development]] · [[Python-Fundamentals]] · [[Python-Fundamentals]] · [[CLI-Tool-Proficiency]] · [[Basic-Programming-Logic]] · [[Software-Engineering-Principles]] · [[vs-code]] · [[transfer-of-learning]] · [[FastMCP-Development-Guide]] · [[Custom-MCP-Server-Development]] · [[Claude-Code-Workflows]] · [[Software-Engineering-Workflows]] · [[Data-Visualization]] · [[git-based-workflow]] · [[AI-Agents]] · [[Agentic-Prompt-Engineering-Workflows]] · [[Claude-Code]] · [[Architecture-Patterns]] · [[Continuous-Integration-Continuous-Deployment]] · [[Python-Fundamentals]] · [[vs-code]] · [[claude-code-basics]] · [[automation]]

```dataview
LIST FROM [[Protocol Diagnosing Module Not Found Errors]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-with-copilot-foundational-report-2026-04-19]]
