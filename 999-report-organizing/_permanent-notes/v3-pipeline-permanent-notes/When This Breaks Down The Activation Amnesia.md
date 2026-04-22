---
title: "When This Breaks Down: The Activation Amnesia"
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

# When This Breaks Down: The Activation Amnesia

> [!definition] When This Breaks Down: The Activation Amnesia
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!evidence] When This Breaks Down: The Activation Amnesia
> **What happens:** You create a virtual environment and install packages into it. Everything works during that session. The next day, you open VS Code, run your script, and get `ModuleNotFoundError` — the packages you installed yesterday seem to have vanished.
> **Why it happens:** Virtual environment activation is session-specific. When you close the terminal, the activation is lost. When VS Code opens a new terminal, it may or may not automatically activate the venv depending on your settings. The packages are still there in the `.venv` directory — but if the terminal is not activated, Python is using the global interpreter, which does not know about those packages.
> **What to do:** Check whether the terminal prompt shows `(.venv)`. If not, activate manually. To make activation automatic, ensure the VS Code setting `"python.terminal.activateEnvironment"` is set to `true` (it is by default), and that the correct interpreter is selected in the status bar. VS Code will then automatically activate the venv when opening new terminals.
> **Prevention:** Always verify the terminal prefix before running `pip install` or scripts. The two-second glance at the prompt prefix prevents the ten-minute diagnostic session that follows from installing packages into the wrong environment.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[python-interpreter]] · [[integrated-development-environment]] · [[debugging]] · [[Virtual Environment]] · [[GitHub Copilot]] · [[mental-model]] · [[script-automation]] · [[automation]] · [[api]] · [[python-interpreter]] · [[command-line]] · [[linting]] · [[debugging]] · [[type-hints]] · [[pip]] · [[Virtual Environment]] · [[repl]] · [[Virtual Environment]] · [[repl]] · [[mental-model]] · [[Virtual Environment]] · [[breakpoint]] · [[Virtual Environment]] · [[api]] · [[stack-trace]] · [[problem-solving]] · [[error-handling]] · [[breakpoint]] · [[deliberate-practice]] · [[debugging]] · [[Cognitive-Skill-Acquisition]] · [[api]] · [[pip]] · [[Dependency-Management]] · [[Virtual Environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[architecture-patterns]] · [[Chunk (Miller, 1956; Chase & Simon, 1973)]] · [[GitHub Copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[active-learning]] · [[Cognitive Scaffolding]] · [[api]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[api]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[Cognitive Load Theory (CLT)]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[Expertise Reversal Effect (Kalyuga, Ayres, Chandler, Sweller, 2003)]] · [[generation-effect]] · [[Scaffolded Fading]] · [[Cognitive Load Theory (CLT)]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[Cognitive Load Theory (CLT)]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[Scaffolded Fading]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[When This Breaks Down The Activation Amnesia]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
