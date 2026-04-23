---
title: 'The Situation: "It Works on My Machine"'
aliases:
- IWMOM
- works-on-my-machine
- 'The Situation: "It Works on My Machine'
- the-situation-it-works-on-my-machine
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
# The Situation: "It Works on My Machine"

> [!definition] The Situation: "It Works on My Machine"
> "The Situation: 'It Works on My Machine'" refers to a scenario where software developed on one specific machine fails when run on another due to differences in environment configurations, such as installed packages or Python versions.

## Core Explanation

> [!evidence] The Situation: "It Works on My Machine"
> You have built a Python script that automates a workflow — it reads data from an API, processes it, and generates a report. It works perfectly on your machine. A colleague asks to use it. You send them the `.py` file. They run it and immediately get `ModuleNotFoundError: No module named 'requests'`. You tell them to install requests. They do, but now the script crashes with a different error because they have Python 3.9 and you used a feature introduced in 3.11. You send them a more detailed setup guide, but their IT department has restricted pip access and they cannot install packages freely. The script — which works flawlessly in your environment — is effectively undeliverable because it carries invisible dependencies on your specific machine configuration, your specific Python version, and your specific installed packages.
>
> **The core question:** How does one package a Python project so that it can be reproduced reliably on another machine, and what are the practices that separate a personal script from a shareable tool?
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
