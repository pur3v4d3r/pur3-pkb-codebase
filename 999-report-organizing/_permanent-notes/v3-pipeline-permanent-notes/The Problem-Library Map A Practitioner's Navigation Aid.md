---
title: "The Problem-Library Map: A Practitioner's Navigation Aid"
aliases: [problem-library-mapping, library-navigation-map]
type: permanent-note
status: evergreen
confidence: medium
domain: pedagogy
subdomains: []
tags: [permanent-note, pedagogy]
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

# The Problem-Library Map: A Practitioner's Navigation Aid

> [!definition] The Problem-Library Map: A Practitioner's Navigation Aid
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!analytical-insight] The Problem-Library Map: A Practitioner's Navigation Aid
> Instead of learning libraries and then finding problems for them, start from the problem you face and trace to the tool:
>
> **"I need to work with files and directories"** → `os`, `pathlib`, `shutil` (standard library — no install needed). `pathlib` is the modern approach and reads more naturally than `os.path`.
>
> **"I need to process CSV, JSON, or XML data"** → `csv`, `json`, `xml.etree` (standard library) for small files; `pandas` (PyPI) for anything complex or large. If Copilot generates `pandas` code for a file with 20 rows, consider whether the standard `csv` module would be simpler.
>
> **"I need to call a web API or download data from the internet"** → `requests` (PyPI) for HTTP calls; `urllib` (standard library) as a more verbose alternative. For [[api|REST APIs]], `requests` plus `json` is the standard combination.
>
> **"I need to scrape a website"** → `requests` + `beautifulsoup4` (PyPI) for HTML parsing; `selenium` or `playwright` (PyPI) for JavaScript-rendered pages that `requests` alone cannot handle.
>
> **"I need to automate file management, renaming, or batch operations"** → `pathlib`, `shutil`, `glob` (standard library); `watchdog` (PyPI) for monitoring file changes. This is one of Python's most accessible use cases — a script that renames 500 files according to a pattern replaces an hour of manual work with 30 seconds of execution.
>
> **"I need to work with dates, times, or scheduling"** → `datetime`, `time` (standard library); `schedule` (PyPI) for periodic task execution; `APScheduler` (PyPI) for more complex scheduling.
>
> **"I need to automate desktop tasks (clicking, typing, screenshots)"** → `pyautogui` (PyPI) for GUI automation; `pyperclip` for clipboard access; `Pillow` for screenshots and image manipulation.
>
> **"I need to interact with a database"** → `sqlite3` (standard library) for local databases requiring no server; `psycopg2` or `asyncpg` for PostgreSQL; `mysql-connector-python` for MySQL; `SQLAlchemy` (PyPI) as a cross-database abstraction layer.
>
> **"I need to analyze data or create charts"** → `pandas` + `matplotlib` or `plotly` (all PyPI). This is the data science entry point — `pandas` for manipulation, `matplotlib` for static charts, `plotly` for interactive visualizations.
>
> **"I need to work with text — searching, replacing, extracting patterns"** → `re` (standard library) for [[Regular-Expressions|regular expressions]]; `string` (standard library) for basic operations. For complex NLP, `spacy` or `nltk` (PyPI).
>
> **"I need to send emails or notifications"** → `smtplib`, `email` (standard library) for email; `requests` to POST to webhook endpoints (Slack, Discord, Teams).
>
> **"I need to build a command-line tool"** → `argparse` (standard library) for argument parsing; `click` or `typer` (PyPI) for more ergonomic CLI frameworks.
>
> **"I need to run tasks in parallel or handle long-running operations"** → `threading`, `multiprocessing` (standard library); `asyncio` (standard library) for [[Async-Programming|asynchronous I/O]]; `concurrent.futures` for high-level parallel execution.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[python-interpreter]] · [[integrated-development-environment]] · [[debugging]] · [[virtual-environment]] · [[github-copilot]] · [[mental-model]] · [[script-automation]] · [[automation]] · [[api]] · [[python-interpreter]] · [[command-line]] · [[linting]] · [[debugging]] · [[type-hints]] · [[pip]] · [[virtual-environment]] · [[repl]] · [[virtual-environment]] · [[repl]] · [[mental-model]] · [[virtual-environment]] · [[breakpoint]] · [[virtual-environment]] · [[api]] · [[stack-trace]] · [[problem-solving]] · [[error-handling]] · [[breakpoint]] · [[deliberate-practice]] · [[debugging]] · [[Cognitive-Skill-Acquisition]] · [[api]] · [[pip]] · [[Dependency-Management]] · [[virtual-environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[architecture-patterns]] · [[chunking]] · [[github-copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[active-learning]] · [[cognitive-scaffolding]] · [[api]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[api]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[cognitive-load-theory]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[expertise-reversal-effect]] · [[generation-effect]] · [[scaffolding]] · [[cognitive-load-theory]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[cognitive-load-theory]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[scaffolding]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[The Problem-Library Map A Practitioner's Navigation Aid]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
