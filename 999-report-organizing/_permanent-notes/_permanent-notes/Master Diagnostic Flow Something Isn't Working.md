---
title: "Master Diagnostic Flow: \"Something Isn't Working\""
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

**Related:** [[Python-Interpreter]] · [[Integrated-Development-Environment]] · [[Debugging]] · [[Virtual-Environment]] · [[GitHub-Copilot]] · [[mental-model]] · [[Script-Automation]] · [[automation]] · [[API]] · [[Python-Interpreter]] · [[command-line]] · [[Linting]] · [[Debugging]] · [[Type-Hints]] · [[pip]] · [[Virtual-Environment]] · [[REPL]] · [[Virtual-Environment]] · [[REPL]] · [[mental-model]] · [[Virtual-Environment]] · [[Breakpoint]] · [[Virtual-Environment]] · [[API]] · [[Stack-Trace]] · [[Problem-Solving]] · [[Error-Handling]] · [[Breakpoint]] · [[deliberate-practice]] · [[Debugging]] · [[Cognitive-Skill-Acquisition]] · [[API]] · [[pip]] · [[Dependency-Management]] · [[Virtual-Environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[Architecture-Patterns]] · [[chunking]] · [[GitHub-Copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[Active-Learning]] · [[cognitive-scaffolding]] · [[API]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[API]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[cognitive-load-theory]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[expertise-reversal-effect]] · [[generation-effect]] · [[scaffolding]] · [[cognitive-load-theory]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[cognitive-load-theory]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[scaffolding]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[Master Diagnostic Flow Something Isn't Working]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
