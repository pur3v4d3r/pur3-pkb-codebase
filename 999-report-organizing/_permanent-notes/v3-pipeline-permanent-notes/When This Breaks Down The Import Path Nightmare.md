---
title: "When This Breaks Down: The Import Path Nightmare"
aliases: []
type: permanent-note
status: evergreen
confidence: medium
domain: programming
subdomains: []
tags: [permanent-note, programming]
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

# When This Breaks Down: The Import Path Nightmare

> [!definition] When This Breaks Down: The Import Path Nightmare
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!evidence] When This Breaks Down: The Import Path Nightmare
> **What happens:** Your project has subdirectories, and `from data.readers import read_csv` works when you run `python main.py` from the project root but fails with `ModuleNotFoundError` when you run the script from a different directory, or when VS Code runs it with a different working directory configuration.
> **Why it happens:** Python's import system resolves relative to `sys.path`, which includes the directory of the script being run. If you run `python main.py` from the project root, the project root is in `sys.path`, and `data/` is findable. If you run from inside the `data/` directory, the project root is not in `sys.path`, and the import fails.
> **What to do:** Always run scripts from the project root. In VS Code, ensure `"python.terminal.executeInFileDir"` is set to `false` (the default) so that the Run button executes from the workspace root. If you must support execution from arbitrary directories, add the project root to `sys.path` at the top of the entry-point script: `import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))`.
> **Prevention:** Open your project folder as the VS Code workspace (File → Open Folder). This sets the default working directory for all terminal sessions and run commands, which keeps `sys.path` consistent.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[python-interpreter]] · [[integrated-development-environment]] · [[debugging]] · [[virtual-environment]] · [[github-copilot]] · [[mental-model]] · [[script-automation]] · [[automation]] · [[api]] · [[python-interpreter]] · [[command-line]] · [[linting]] · [[debugging]] · [[type-hints]] · [[pip]] · [[virtual-environment]] · [[repl]] · [[virtual-environment]] · [[repl]] · [[mental-model]] · [[virtual-environment]] · [[breakpoint]] · [[virtual-environment]] · [[api]] · [[stack-trace]] · [[problem-solving]] · [[error-handling]] · [[breakpoint]] · [[deliberate-practice]] · [[debugging]] · [[Cognitive-Skill-Acquisition]] · [[api]] · [[pip]] · [[Dependency-Management]] · [[virtual-environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[architecture-patterns]] · [[chunking]] · [[github-copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[active-learning]] · [[cognitive-scaffolding]] · [[api]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[api]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[cognitive-load-theory]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[expertise-reversal-effect]] · [[generation-effect]] · [[scaffolding]] · [[cognitive-load-theory]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[cognitive-load-theory]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[scaffolding]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[When This Breaks Down The Import Path Nightmare]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
