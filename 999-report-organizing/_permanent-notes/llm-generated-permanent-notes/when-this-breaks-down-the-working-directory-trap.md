---
title: 'When This Breaks Down: The Working Directory Trap'
aliases:
- 'When This Breaks Down: The Working Directory Trap'
- when-this-breaks-down-the-working-directory-trap
type: permanent-note
status: evergreen
confidence: medium
domain: programming
subdomains: []
tags:
- permanent-note
- programming
created: '2026-04-22'
updated: '2026-04-22'
complexity: intermediate
importance: medium
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: 3.0.0
  source-reports:
  - python-development-in-vscode-practitioners-field-guide-2026-04-19
  extraction-method: pkb-extractor-v1 → pipeline-v3
  definition-source: llm-filled
  definition-model: qwen2.5:7b-instruct-q5_K_M
  definition-filled-at: '2026-04-23'
---
# When This Breaks Down: The Working Directory Trap

> [!definition] When This Breaks Down: The Working Directory Trap
> When This Breaks Down: The Working Directory Trap refers to the issue where a script functions correctly when run from one directory but fails due to file path resolution errors when executed from another directory.

## Core Explanation

> [!evidence] When This Breaks Down: The Working Directory Trap
> **What happens:** Your script runs fine when you execute it from one location but fails with `FileNotFoundError` when you execute it from another. Or a script that reads `data.csv` works when you run it by right-clicking the file but fails when you use the terminal.
> **Why it happens:** Python resolves relative file paths — paths like `data.csv` or `./config/settings.json` — relative to the **current working directory**, which is the directory the terminal is "in" when the script runs. When you use the Run button, VS Code typically sets the working directory to the file's own directory or the workspace root (depending on your settings). When you use the terminal, the working directory is wherever the terminal prompt is currently pointing, which may be a completely different directory.
> **What to do:** Check the current working directory by adding `import os; print(os.getcwd())` at the top of your script. If it is wrong, either `cd` to the correct directory before running, or use the VS Code setting `"python.terminal.executeInFileDir": true` in your settings.json to make the Run button always execute from the file's own directory.
> **Prevention:** Adopt the practice of using absolute paths or paths relative to the script's own location (`os.path.dirname(os.path.abspath(__file__))`) rather than relative paths that depend on the working directory. This makes scripts portable across execution methods.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
