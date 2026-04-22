---
title: "Master Diagnostic Flow: \"Something Isn't Working\""
aliases: []
type: permanent-note
status: evergreen
confidence: medium
domain: uncategorized
subdomains: []
tags: [permanent-note, uncategorized]
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

# Master Diagnostic Flow: "Something Isn't Working"

> [!definition] Master Diagnostic Flow: "Something Isn't Working"
> *Definition pending — derived from 1 source report(s).*

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

**Related:** [[python-interpreter]] · [[integrated-development-environment]] · [[debugging]] · [[Virtual Environment]] · [[GitHub Copilot]] · [[mental-model]] · [[script-automation]] · [[automation]] · [[api]] · [[python-interpreter]] · [[command-line]] · [[linting]] · [[debugging]] · [[type-hints]] · [[pip]] · [[Virtual Environment]] · [[repl]] · [[Virtual Environment]] · [[repl]] · [[mental-model]] · [[Virtual Environment]] · [[breakpoint]] · [[Virtual Environment]] · [[api]] · [[stack-trace]] · [[problem-solving]] · [[error-handling]] · [[breakpoint]] · [[deliberate-practice]] · [[debugging]] · [[Cognitive-Skill-Acquisition]] · [[api]] · [[pip]] · [[Dependency-Management]] · [[Virtual Environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[architecture-patterns]] · [[Chunk (Miller, 1956; Chase & Simon, 1973)]] · [[GitHub Copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[active-learning]] · [[Cognitive Scaffolding]] · [[api]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[api]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[Cognitive Load Theory (CLT)]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[Expertise Reversal Effect (Kalyuga, Ayres, Chandler, Sweller, 2003)]] · [[generation-effect]] · [[Scaffolded Fading]] · [[Cognitive Load Theory (CLT)]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[Cognitive Load Theory (CLT)]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[Scaffolded Fading]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[Master Diagnostic Flow Something Isn't Working]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
