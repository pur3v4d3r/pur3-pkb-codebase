---
title: "Spaced Repetition Seeds for Active Recall"
aliases: [SRS for AR, Active Recall via Spaced Repetition]
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

# Spaced Repetition Seeds for Active Recall

> [!definition] Spaced Repetition Seeds for Active Recall
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!evidence] Spaced Repetition Seeds for Active Recall
> **Factual:**
>
> *Q: What are the three layers that must agree for Python to work correctly in VS Code?*
> A: The operating system's PATH, the VS Code Python extension's interpreter selection, and the terminal session's inherited environment. All three must point to the same Python installation.
>
> *Q: In what order should you read a Python traceback?*
> A: Bottom to top. Read the last line first (error type and message), then find your own code in the chain (last entry pointing to your files), then trace upward to understand the causal chain.
>
> *Q: What does the `if __name__ == "__main__":` guard do?*
> A: It ensures the indented code runs only when the file is executed directly (e.g., `python main.py`), not when the file is imported as a module by another script.
>
> **Process:**
>
> *Q: What are the steps to create and activate a virtual environment in VS Code on Windows?*
> A: (1) `python -m venv .venv` in the project root, (2) `.venv\Scripts\activate` in the terminal, (3) Select the `.venv` interpreter in the VS Code status bar, (4) Verify with `pip list` showing a clean environment.
>
> *Q: What is the Copilot Collaboration Workflow's five-step protocol?*
> A: (1) Write the intent comment first, (2) Accept and READ the suggestion immediately, (3) Verify with a test case, (4) Modify something to verify understanding, (5) Add comments explaining WHY.
>
> **Application:**
>
> *Q: You run a script and get `ModuleNotFoundError: No module named 'requests'`. The script worked yesterday. What is the most likely cause and how do you diagnose it?*
> A: The virtual environment is not activated. Check the terminal prompt for the `(.venv)` prefix. If absent, activate the venv. If present, check `pip list` to confirm requests is installed in this environment. If not, `pip install requests` in the active venv.
>
> *Q: Copilot generates a 15-line function using pandas methods you don't recognize. Using the Three Modes framework, what mode should you be in and what should you do?*
> A: Mode 2 (Scaffolding). Accept the code, read each line, ask Copilot Chat to explain unfamiliar methods, test with a small known input, then modify one aspect (e.g., add a filter condition) to verify understanding. If modification feels risky, shift to Mode 3 (Dialogue).
>
> *Q: You have a project that uses `requests` and `pandas`. A colleague tries to run it and gets errors. What minimum set of artifacts should you have provided?*
> A: (1) `requirements.txt` with pinned versions, (2) README.md with setup steps (create venv, activate, pip install -r requirements.txt, how to run), (3) `.gitignore` excluding `.venv/`, (4) `.env.example` if any environment variables are needed.
>
> **Conceptual:**
>
> *Q: Why is the "divergence point" often different from the "crash point" in a Python error?*
> A: The crash point is where Python can no longer continue — the symptom. The divergence point is where program state first departed from expectations — the cause. These are often separated because a wrong value (divergence) can propagate through several lines of code before triggering an operation that fails (crash). The debugger finds the divergence point; the traceback shows only the crash point.
>
> *Q: What is the fundamental problem that virtual environments solve, and why does this problem exist in the first place?*
> A: Virtual environments solve dependency conflicts between projects. The problem exists because Python's default `pip install` places packages in a shared global directory that all projects use. When two projects need different versions of the same package (or packages with conflicting sub-dependencies), the shared pool cannot satisfy both. Virtual environments give each project its own isolated package directory, eliminating the shared state that causes conflicts.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[python-interpreter]] · [[integrated-development-environment]] · [[debugging]] · [[virtual-environment]] · [[github-copilot]] · [[mental-model]] · [[script-automation]] · [[automation]] · [[api]] · [[python-interpreter]] · [[command-line]] · [[linting]] · [[debugging]] · [[type-hints]] · [[pip]] · [[virtual-environment]] · [[repl]] · [[virtual-environment]] · [[repl]] · [[mental-model]] · [[virtual-environment]] · [[breakpoint]] · [[virtual-environment]] · [[api]] · [[stack-trace]] · [[problem-solving]] · [[error-handling]] · [[breakpoint]] · [[deliberate-practice]] · [[debugging]] · [[Cognitive-Skill-Acquisition]] · [[api]] · [[pip]] · [[Dependency-Management]] · [[virtual-environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[architecture-patterns]] · [[chunking]] · [[github-copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[active-learning]] · [[cognitive-scaffolding]] · [[api]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[api]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[cognitive-load-theory]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[expertise-reversal-effect]] · [[generation-effect]] · [[scaffolding]] · [[cognitive-load-theory]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[cognitive-load-theory]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[scaffolding]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[Spaced Repetition Seeds for Active Recall]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
