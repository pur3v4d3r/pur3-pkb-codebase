---
title: 'Master Diagnostic Flow: "Something Isn''t Working"'
aliases:
- 'Master Diagnostic Flow: "Something Isn''t Working'
- master-diagnostic-flow-something-isnt-working
type: permanent-note
status: evergreen
confidence: medium
domain: uncategorized
subdomains: []
tags:
- permanent-note
- uncategorized
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
# Master Diagnostic Flow: "Something Isn't Working"

> [!definition] Master Diagnostic Flow: "Something Isn't Working"
> Master Diagnostic Flow: 'Something Isn't Working' is a structured approach to troubleshooting issues in Python development, covering steps such as checking Python installation, interpreting error messages, verifying environment configurations, and ensuring reproducibility.

## Core Explanation

> [!evidence] Master Diagnostic Flow: "Something Isn't Working"
> ```
> Something isn't working
> │
> ├── "Python not found" / "command not recognized"
> │   └── → Section 1: Setup Protocol
> │       ├── Check: Is Python installed? (python --version)
> │       ├── Check: Is it in PATH? (where python)
> │       └── Check: Does VS Code see it? (status bar)
> │
> ├── Script won't run / wrong behavior
> │   ├── Red error text (traceback)?
> │   │   └── → Section 3: Traceback Reading Protocol
> │   │       ├── Read last line (error type)
> │   │       ├── Find your code (file path)
> │   │       └── If unclear → Debugger Protocol
> │   │
> │   ├── "ModuleNotFoundError"?
> │   │   └── → Section 4: Environment Check
> │   │       ├── Is venv active? (terminal prefix)
> │   │       ├── Is package installed? (pip list)
> │   │       └── Does VS Code use the right interpreter? (status bar)
> │   │
> │   ├── "FileNotFoundError"?
> │   │   └── → Section 2: Working Directory Trap
> │   │       ├── Check working directory (os.getcwd())
> │   │       └── Align execution method with file location
> │   │
> │   └── No error but wrong results?
> │       └── → Section 3: Debugger Protocol
> │           ├── Set breakpoint before suspect logic
> │           ├── Step through, watching variables
> │           └── Find the divergence point
> │
> ├── "Import won't resolve" / VS Code shows red squiggles
> │   ├── Module exists but VS Code doesn't find it?
> │   │   └── → Check interpreter selection (Section 1, Step 5)
> │   └── Module is in subdirectory?
> │       └── → Section 5: Package structure (__init__.py)
> │
> └── "It works on my machine but not on theirs"
>     └── → Section 8: Reproducibility Protocol
>         ├── requirements.txt up to date?
>         ├── Python version documented?
>         ├── Secrets in environment variables?
>         └── Test-from-scratch verification
> ```
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
