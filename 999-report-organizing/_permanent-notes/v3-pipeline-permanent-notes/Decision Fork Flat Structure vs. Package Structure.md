---
title: "Decision Fork: Flat Structure vs. Package Structure"
aliases: []
type: permanent-note
status: evergreen
confidence: medium
domain: software-engineering
subdomains: []
tags: [permanent-note, software-engineering]
created: '2026-04-22'
updated: '2026-04-22'
complexity: intermediate
importance: medium
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: "3.0.0"
  source-reports: [python-development-in-vscode-practitioners-field-guide-2026-04-19]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Decision Fork: Flat Structure vs. Package Structure

> [!definition] Decision Fork: Flat Structure vs. Package Structure
> *Definition pending — derived from 1 source report(s).*

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

**Related:** [[python-interpreter]] · [[integrated-development-environment]] · [[debugging]] · [[virtual-environment]] · [[github-copilot]] · [[mental-model]] · [[script-automation]] · [[automation]] · [[api]] · [[python-interpreter]] · [[command-line]] · [[linting]] · [[debugging]] · [[type-hints]] · [[pip]] · [[virtual-environment]] · [[repl]] · [[virtual-environment]] · [[repl]] · [[mental-model]] · [[virtual-environment]] · [[breakpoint]] · [[virtual-environment]] · [[api]] · [[stack-trace]] · [[problem-solving]] · [[error-handling]] · [[breakpoint]] · [[deliberate-practice]] · [[debugging]] · [[Cognitive-Skill-Acquisition]] · [[api]] · [[pip]] · [[Dependency-Management]] · [[virtual-environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[architecture-patterns]] · [[chunking]] · [[github-copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[active-learning]] · [[cognitive-scaffolding]] · [[api]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[api]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[cognitive-load-theory]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[expertise-reversal-effect]] · [[generation-effect]] · [[scaffolding]] · [[cognitive-load-theory]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[cognitive-load-theory]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[scaffolding]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[Decision Fork Flat Structure vs. Package Structure]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
