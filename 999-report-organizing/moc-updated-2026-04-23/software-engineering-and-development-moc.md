---
title: Software Engineering & Development MOC
aliases:
  - Software Engineering MOC
  - Programming MOC
  - Dev Workflows Hub
created: 2026-04-22
modified: 2026-04-22
status: evergreen
type: moc
tags:
  - software-engineering
  - moc
  - knowledge-hub
child-mocs: []
---

# Software Engineering & Development MOC

> [!abstract] Scope
> Software-engineering knowledge captured during cross-disciplinary research where programming and development workflows intersect with cognitive science, PKM, and AI-assisted work. Covers programming fundamentals, Python ecosystem, version control, dev tooling, software-architecture principles, testing/quality practices, and developer cognition.

> [!principle-point] Organizing Principle
> These notes treat programming as a **cognitive activity** subject to working-memory constraints, deliberate-practice principles, and metacognitive monitoring. The cross-references back into cognitive-science MOCs are the most important graph edges.

[**SE-Domain-Function**:: Captures programming and development knowledge as it intersects with the vault's cognitive-science research program.]

---

## 🎯 Core Hub Concepts

- [[software-engineering-workflows]], [[Software-Engineering-Practice]], [[software-engineering-principles]]
- [[Software-Architecture]], [[architecture-patterns]], [[software-design]]
- [[python-fundamentals]], [[Python]], [[programming-concepts]], [[basic-programming-logic]]

## 🐍 Python Ecosystem

- [[Python]], [[python-fundamentals]], [[python-interpreter]], [[Python-Standard-Library]]
- [[Pandas]], [[Python-Data-Analysis-Pipeline-Design]]
- [[Python-Testing-Strategies-and-TDD]], [[Python-Type-System-and-Static-Analysis]]
- [[type-hints]], [[Async-Programming]]
- [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
- [[python-development-in-vscode-with-copilot-annotated-critical-analysis-2026-04-19]]

## 🛠️ Tooling & Workflow

- [[command-line]], [[cli-tool-proficiency]], [[Windows-Terminal]], [[repl]]
- [[Git]], [[git-based-workflow]], [[Version-Control]]
- [[vs-code]], [[integrated-development-environment]]
- [[Continuous-Integration-Continuous-Deployment]]
- [[automation]], [[script-automation]]
- [[debugging]], [[stack-trace]], [[error-handling]], [[Error-Handling-as-Cognitive-Engineering]]
- [[linting]], [[Test-Driven-Development]]
- [[Quality-Assurance]], [[code-review]]
- [[Dependency-Management]], [[Package-Management]], [[pip]]
- [[docker-fundamentals]]
- [[Markdown-Fundamentals]], [[YAML]], [[JSON-RPC]]
- [[Regular-Expressions]]
- [[target-framework]], [[complete-project-structure]]

## 🧱 Architecture & Design

- [[Software-Architecture]], [[architecture-patterns]], [[software-design]]
- [[API-Fundamentals]], [[API-Design-Patterns]], [[API-Cost-Optimization-Strategies]], [[api]]
- [[Client-Server-Architecture]]
- [[Single-Responsibility-Principle]]
- [[user-experience-design]], [[Jakob-Nielsen]], [[progressive-disclosure]]

## 🧠 Developer Cognition

- [[Error-Handling-as-Cognitive-Engineering]]
- [[programming-expertise-metacognitive-component]]
- [[debugging-as-metacognition]]
- [[Engineering-Metrics-and-the-Dark-Side-of-Optimization]]

## 📊 Data & Information

- [[Data-Visualization]], [[Visual-Representation]], [[diagram]]
- [[Data-Literacy]], [[Statistical-Literacy]], [[Numeracy]]
- [[Information-Retrieval]]
- [[natural-language-processing]]
- [[Distribution-Shift]]

## 🌐 Cross-Domain Connections

- [[cognitive-science-moc]] — Programming as constrained cognition
- [[learning-strategies-and-practice-moc]] — Deliberate practice and skill acquisition for developers
- [[pkm-and-knowledge-systems-moc]] — Dev tooling powering knowledge work (Obsidian, MCP, AI agents)
- [[metacognition-moc]] — Debugging, testing, and code-review as metacognitive practices

## 📖 Auto-Indexed Member Notes

```dataview
TABLE referenced-by-count AS "Refs"
FROM "999-report-organizing/_permanent-notes/llm-generated-permanent-notes"
WHERE regextest("(?i)^(api|python|git|docker|linting|debug|stack|error|test|code|software|architecture|client|server|repl|cli|vs-code|automation|script|markdown|yaml|json|regex|type-hint|async|version|dependency|package|pip|pandas|markdown|window|integrated|programming|complete-project|target-framework|abstraction|engineering|jakob-nielsen|progressive-disclosure|data-|statistical-|numeracy|information-retrieval|natural-language|distribution-shift|visual-representation|diagram|user-experience|single-responsibility)", file.name)
SORT referenced-by-count DESC
LIMIT 100
```

---

# 🔗 Related Topics for PKB Expansion

## 🎯 Core Extensions

1. **[[Error-Handling-as-Cognitive-Engineering]]** — Connection: bridges programming to cognitive load · Depth Potential: original synthesis · Knowledge Graph Role: bridge note · Priority: High
2. **[[programming-expertise-metacognitive-component]]** — Connection: programming as metacognitive practice · Depth Potential: extends deliberate-practice literature · Knowledge Graph Role: cross-MOC bridge · Priority: High

## 🌐 Cross-Domain Connections

3. **[[ai-pkb-integration]]** — Connection: AI-augmented developer workflows · Depth Potential: rapidly evolving · Knowledge Graph Role: bridge to PKM MOC · Priority: High
4. **[[Cognitive-Load-Theory]]** — Connection: programming pedagogy applies CLT directly · Depth Potential: SE-education literature · Knowledge Graph Role: bridge to learning strategies · Priority: Medium

## 📚 Foundational Prerequisites

- **[[working-memory]]** — Programming is working-memory-bound
- **[[automaticity]]** — Skill consolidation in dev work

## 🛠️ Practical Applications

- **[[obsidian-pkb-architecture]]** uses many of these tools
- **[[claude-code-workflows]]** treats developer cognition as designable
