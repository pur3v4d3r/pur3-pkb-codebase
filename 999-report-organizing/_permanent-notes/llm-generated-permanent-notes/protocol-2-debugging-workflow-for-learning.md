---
title: 'Protocol 2: Debugging Workflow for Learning'
aliases:
- 'Protocol 2: Debugging Workflow for Learning'
- protocol-2-debugging-workflow-for-learning
type: permanent-note
status: evergreen
confidence: medium
domain: pedagogy
subdomains: []
tags:
- permanent-note
- pedagogy
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
  - python-development-in-vscode-with-copilot-annotated-critical-analysis-2026-04-19
  extraction-method: pkb-extractor-v1 → pipeline-v3
  definition-source: llm-filled
  definition-model: qwen2.5:7b-instruct-q5_K_M
  definition-filled-at: '2026-04-23'
---
# Protocol 2: Debugging Workflow for Learning

> [!definition] Protocol 2: Debugging Workflow for Learning
> Protocol 2: Debugging Workflow for Learning is a structured approach to using a debugger in Python development with Visual Studio Code, involving setting breakpoints, making predictions about variable values, and stepping through code to refine understanding and improve mental models.

## Methodology & Sources

> [!methodology-and-sources] Protocol 2: Debugging Workflow for Learning
> 1. Write or obtain a working Python script
> 2. Set breakpoints at key decision points (before loops, conditionals, function calls)
> 3. Start debugger: press `F5` (not `Ctrl+F5` which runs without debugging)
> 4. At each breakpoint: predict what the next variable values will be
> 5. Step Over (`F10`) and compare prediction with observed values
> 6. If prediction was wrong: investigate why using Debug Console
> 7. Use Step Into (`F11`) for function calls you want to understand internally
> 8. Use Step Out (`Shift+F11`) to return to the calling context
> 9. If confused: select code → ask Copilot `/explain`
> 10. After session: note which predictions were wrong and what they revealed about your mental model
> *— [[python-development-in-vscode-with-copilot-annotated-critical-analysis-2026-04-19]]*

## Connections

**Related:** [[python-fundamentals]] · [[vs-code]] · [[AI-Agents]] · [[command-line]] · [[API-Fundamentals]] · [[git-based-workflow]] · [[working-memory]] · [[active-learning]] · [[automation]] · [[Cognitive Load Theory (CLT)]] · [[cli-tool-proficiency]] · [[Cognitive Scaffolding]] · [[personal-workflow-architecture]] · [[conceptual-change-theory-and-schema-restructuring]] · [[Obsidian-Automation]] · [[Windows-Terminal]] · [[self-efficacy-for-learning-and-performance]] · [[agentic-prompt-engineering-workflows]] · [[Metacognitive Scaffolding]] · [[Overconfidence-Bias]] · [[elaborative-encoding]] · [[PKB-Automation]] · [[Template-Engineering]] · [[Hypothesis-Testing]] · [[evidence-based-practice]]
---

**Sources:** [[python-development-in-vscode-with-copilot-annotated-critical-analysis-2026-04-19]]
