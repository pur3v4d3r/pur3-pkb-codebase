---
title: 'Decision Fork: Flat Structure vs. Package Structure'
aliases:
- 'Decision Fork: Flat Structure vs. Package Structure'
- decision-fork-flat-structure-vs-package-structure
type: permanent-note
status: evergreen
confidence: medium
domain: software-engineering
subdomains: []
tags:
- permanent-note
- software-engineering
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
# Decision Fork: Flat Structure vs. Package Structure

> [!definition] Decision Fork: Flat Structure vs. Package Structure
> Decision Fork: Flat Structure vs. Package Structure refers to choosing between organizing Python files in a single directory level or grouping them into subdirectories with `__init__.py` files based on the project's size and complexity.

## Core Explanation

> [!evidence] Decision Fork: Flat Structure vs. Package Structure
> As your project grows, you need to decide how to organize files:
>
> **IF your project has fewer than ~10 Python files:**
> → Keep all `.py` files in the project root (flat structure)
> → Key indicator: You can describe the project's components in a single level of categories
>
> **IF your project has distinct subsystems or layers (e.g., data access, business logic, presentation):**
> → Organize into packages (subdirectories with `__init__.py`):
> ```
> my_project/
> ├── data/
> │   ├── __init__.py
> │   ├── readers.py
> │   └── writers.py
> ├── processing/
> │   ├── __init__.py
> │   ├── transforms.py
> │   └── validators.py
> └── main.py
> ```
> → Key indicator: You have groups of files that relate more to each other than to files in other groups
>
> **IF UNSURE:**
> → Start flat. Restructure into packages when the flat structure becomes hard to navigate. Premature organization is wasted effort.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
