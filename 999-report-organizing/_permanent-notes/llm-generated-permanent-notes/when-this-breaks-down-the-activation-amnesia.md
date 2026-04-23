---
title: 'When This Breaks Down: The Activation Amnesia'
aliases:
- 'When This Breaks Down: The Activation Amnesia'
- when-this-breaks-down-the-activation-amnesia
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
# When This Breaks Down: The Activation Amnesia

> [!definition] When This Breaks Down: The Activation Amnesia
> When This Breaks Down: The Activation Amnesia refers to the situation where a virtual environment appears to lose its activated state after closing the terminal session, leading to `ModuleNotFoundError` when attempting to run scripts in an unactivated terminal.

## Core Explanation

> [!evidence] When This Breaks Down: The Activation Amnesia
> **What happens:** You create a virtual environment and install packages into it. Everything works during that session. The next day, you open VS Code, run your script, and get `ModuleNotFoundError` — the packages you installed yesterday seem to have vanished.
> **Why it happens:** Virtual environment activation is session-specific. When you close the terminal, the activation is lost. When VS Code opens a new terminal, it may or may not automatically activate the venv depending on your settings. The packages are still there in the `.venv` directory — but if the terminal is not activated, Python is using the global interpreter, which does not know about those packages.
> **What to do:** Check whether the terminal prompt shows `(.venv)`. If not, activate manually. To make activation automatic, ensure the VS Code setting `"python.terminal.activateEnvironment"` is set to `true` (it is by default), and that the correct interpreter is selected in the status bar. VS Code will then automatically activate the venv when opening new terminals.
> **Prevention:** Always verify the terminal prefix before running `pip install` or scripts. The two-second glance at the prompt prefix prevents the ten-minute diagnostic session that follows from installing packages into the wrong environment.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
