---
title: "The Situation: \"It Works on My Machine\""
aliases: []
type: permanent-note
status: evergreen
confidence: medium
domain: uncategorized
subdomains: []
tags: [permanent-note, uncategorized]
created: '2026-04-21'
updated: '2026-04-21'
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

# The Situation: "It Works on My Machine"

> [!definition] The Situation: "It Works on My Machine"
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!evidence] The Situation: "It Works on My Machine"
> You have built a Python script that automates a workflow — it reads data from an API, processes it, and generates a report. It works perfectly on your machine. A colleague asks to use it. You send them the `.py` file. They run it and immediately get `ModuleNotFoundError: No module named 'requests'`. You tell them to install requests. They do, but now the script crashes with a different error because they have Python 3.9 and you used a feature introduced in 3.11. You send them a more detailed setup guide, but their IT department has restricted pip access and they cannot install packages freely. The script — which works flawlessly in your environment — is effectively undeliverable because it carries invisible dependencies on your specific machine configuration, your specific Python version, and your specific installed packages.
>
> **The core question:** How does one package a Python project so that it can be reproduced reliably on another machine, and what are the practices that separate a personal script from a shareable tool?
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Python-Interpreter]] · [[Integrated-Development-Environment]] · [[Debugging]] · [[Virtual-Environment]] · [[GitHub-Copilot]] · [[mental-model]] · [[Script-Automation]] · [[automation]] · [[API]] · [[Python-Interpreter]] · [[command-line]] · [[Linting]] · [[Debugging]] · [[Type-Hints]] · [[pip]] · [[Virtual-Environment]] · [[REPL]] · [[Virtual-Environment]] · [[REPL]] · [[mental-model]] · [[Virtual-Environment]] · [[Breakpoint]] · [[Virtual-Environment]] · [[API]] · [[Stack-Trace]] · [[Problem-Solving]] · [[Error-Handling]] · [[Breakpoint]] · [[deliberate-practice]] · [[Debugging]] · [[Cognitive-Skill-Acquisition]] · [[API]] · [[pip]] · [[Dependency-Management]] · [[Virtual-Environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[Architecture-Patterns]] · [[chunking]] · [[GitHub-Copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[Active-Learning]] · [[cognitive-scaffolding]] · [[API]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[API]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[cognitive-load-theory]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[expertise-reversal-effect]] · [[generation-effect]] · [[scaffolding]] · [[cognitive-load-theory]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[cognitive-load-theory]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[scaffolding]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[The Situation It Works on My Machine]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
