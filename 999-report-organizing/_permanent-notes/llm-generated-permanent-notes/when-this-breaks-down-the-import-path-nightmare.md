---
title: 'When This Breaks Down: The Import Path Nightmare'
aliases:
- 'When This Breaks Down: The Import Path Nightmare'
- when-this-breaks-down-the-import-path-nightmare
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
# When This Breaks Down: The Import Path Nightmare

> [!definition] When This Breaks Down: The Import Path Nightmare
> When This Breaks Down: The Import Path Nightmare refers to the issue where Python import statements fail when scripts are run from directories other than their intended root due to differences in `sys.path`.

## Core Explanation

> [!evidence] When This Breaks Down: The Import Path Nightmare
> **What happens:** Your project has subdirectories, and `from data.readers import read_csv` works when you run `python main.py` from the project root but fails with `ModuleNotFoundError` when you run the script from a different directory, or when VS Code runs it with a different working directory configuration.
> **Why it happens:** Python's import system resolves relative to `sys.path`, which includes the directory of the script being run. If you run `python main.py` from the project root, the project root is in `sys.path`, and `data/` is findable. If you run from inside the `data/` directory, the project root is not in `sys.path`, and the import fails.
> **What to do:** Always run scripts from the project root. In VS Code, ensure `"python.terminal.executeInFileDir"` is set to `false` (the default) so that the Run button executes from the workspace root. If you must support execution from arbitrary directories, add the project root to `sys.path` at the top of the entry-point script: `import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))`.
> **Prevention:** Open your project folder as the VS Code workspace (File → Open Folder). This sets the default working directory for all terminal sessions and run commands, which keeps `sys.path` consistent.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
