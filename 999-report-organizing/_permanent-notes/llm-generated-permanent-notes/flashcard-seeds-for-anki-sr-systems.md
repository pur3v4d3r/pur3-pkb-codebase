---
title: Flashcard Seeds for Anki/SR Systems
aliases:
- Anki flashcard seeds
- Spaced Repetition System (SRS) flashcard seeds
- Flashcard Seeds for Anki/SR Systems
- flashcard-seeds-for-anki-sr-systems
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
# Flashcard Seeds for Anki/SR Systems

> [!definition] Flashcard Seeds for Anki/SR Systems
> Flashcard Seeds for Anki/SR Systems are structured question-answer pairs designed to aid in spaced repetition learning, often used for technical skills like programming or software development.

## Flashcards

> [!flashcard] Flashcard Seeds for Anki/SR Systems
> **Card 1:**
> Q: What is the single most important checkbox during Python installation on Windows, and what does it control?
> A: "Add Python to PATH" — it adds the Python installation directory to the system PATH environment variable, allowing the `python` command to be found when typed in any terminal. Without it, the system cannot locate the Python executable unless the full path is specified.
>
> **Card 2:**
> Q: What is a virtual environment in Python, and why is it used?
> A: An isolated Python installation directory (`.venv/`) with its own interpreter and packages. Used to prevent dependency conflicts between projects — each project can have different package versions without interfering with other projects or the system Python installation. Created with `python -m venv .venv`.
>
> **Card 3:**
> Q: What is the difference between `F5` and `Ctrl+F5` in VS Code for Python development?
> A: `F5` runs the script with the debugger attached (breakpoints are active, execution can be paused and inspected). `Ctrl+F5` runs the script without the debugger (faster but no breakpoints, no state inspection). For learning, `F5` is generally more valuable.
>
> **Card 4:**
> Q: What is "cargo-cult coding" in the context of Copilot use?
> A: Accepting and using Copilot-generated code that works without understanding why it works. Named after Feynman's "cargo cult science." Produces fragile competence that breaks when code needs modification, debugging, or extension. Mitigated by deliberately modifying generated code and verifying the modifications work.
>
> **Card 5:**
> Q: What is the "Intent-Code-Understanding Cycle" and what is its critical step?
> A: A five-step learning cycle: (1) formulate intent in natural language, (2) receive Copilot-generated code, (3) encounter unfamiliar constructs, (4) develop understanding via /explain or docs, (5) MODIFY the code. Step 5 (modification) is critical because it forces active application rather than passive acceptance, converting Copilot from dependency to scaffolding.
>
> **Card 6:**
> Q: Why should API keys never be hard-coded in Python scripts?
> A: Hard-coded keys become part of the source code, which means they can be accidentally committed to Git repositories, shared with collaborators, or exposed through code sharing. Store them in environment variables or `.env` files (listed in `.gitignore`), and access them with `os.environ.get('API_KEY')` or `python-dotenv`.
>
> **Card 7 (Annotation Methodology):**
> Q: What is the purpose of an inline annotation (`[!annotation]`) in an Annotated Critical Analysis report?
> A: To make the reasoning behind a claim explicitly visible by documenting: (a) the source basis (what evidence supports the claim), (b) the confidence level (1-5), (c) alternatives considered (what other interpretations were weighed), and (d) selection reasoning (why this interpretation was chosen). The annotation enables the reader to independently evaluate claim quality.
>
> **Card 8 (Annotation Methodology):**
> Q: What does a confidence rating of 3/5 mean in the annotation system, and how does it differ from 4/5?
> A: 3/5 (Mixed evidence): Supported but with meaningful counter-evidence or methodological concerns — the claim is well-motivated but not conclusive. 4/5 (Well-supported): Strong evidence with only minor caveats or boundary conditions — the claim is reliable for most practical purposes. The difference is between "plausible and worth taking seriously" (3/5) and "reliable enough to act on" (4/5).
>
> **Card 9:**
> Q: What are the four stepping controls in VS Code's debugger, and what cognitive question does each answer?
> A: Step Over (F10): "What happens next?" (executes current line, moves to next). Step Into (F11): "What happens inside this?" (follows execution into a function call). Step Out (Shift+F11): "Get me back to the bigger picture" (completes current function, returns to caller). Continue (F5): "Skip to the next breakpoint."
>
> **Card 10:**
> Q: What is the `[!epistemic-status]` marker used for in an Annotated Critical Analysis?
> A: It opens each section with an overall assessment of that section's evidential standing — indicating which claims are established vs. interpretive vs. speculative, and providing a section-level confidence rating. This allows the reader to calibrate their trust before engaging with the section's detailed arguments.
> *— [[python-development-in-vscode-with-copilot-annotated-critical-analysis-2026-04-19]]*

## Connections

**Related:** [[python-fundamentals]] · [[vs-code]] · [[AI-Agents]] · [[command-line]] · [[API-Fundamentals]] · [[git-based-workflow]] · [[working-memory]] · [[active-learning]] · [[automation]] · [[Cognitive Load Theory (CLT)]] · [[cli-tool-proficiency]] · [[Cognitive Scaffolding]] · [[personal-workflow-architecture]] · [[conceptual-change-theory-and-schema-restructuring]] · [[Obsidian-Automation]] · [[Windows-Terminal]] · [[self-efficacy-for-learning-and-performance]] · [[agentic-prompt-engineering-workflows]] · [[Metacognitive Scaffolding]] · [[Overconfidence-Bias]] · [[elaborative-encoding]] · [[PKB-Automation]] · [[Template-Engineering]] · [[Hypothesis-Testing]] · [[evidence-based-practice]]
---

**Sources:** [[python-development-in-vscode-with-copilot-annotated-critical-analysis-2026-04-19]]
