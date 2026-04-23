---
title: 'Protocol: Creating and Managing Virtual Environments in VS Code'
aliases:
- 'Protocol: Creating and Managing Virtual Environments in VS Code'
- protocol-creating-and-managing-virtual-environments-in-vs-code
type: permanent-note
status: evergreen
confidence: medium
domain: coding
subdomains: []
tags:
- permanent-note
- coding
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
# Protocol: Creating and Managing Virtual Environments in VS Code

> [!definition] Protocol: Creating and Managing Virtual Environments in VS Code
> Protocol: Creating and Managing Virtual Environments in VS Code is a set of steps to isolate Python projects by setting up, activating, and configuring virtual environments within VS Code, ensuring reproducibility through dependency management.

## Additional Material

> [!protocol] Protocol: Creating and Managing Virtual Environments in VS Code
> **When to use:** At the start of every new Python project — no exceptions
> **Time required:** 2–5 minutes for initial setup
> **Prerequisites:** Python installed and working in VS Code (Section 1 complete)
>
> 1. **Create the virtual environment:** Open the integrated terminal in your project's root directory. Run: `python -m venv .venv`
>    - This creates a `.venv` directory containing a private Python installation. The name `.venv` is conventional — the leading dot hides it in most file explorers, and VS Code recognizes it automatically.
>    - Watch for: If `python -m venv` fails, you may need `py -m venv .venv` on Windows, or you may need to install the `python3-venv` package on Linux.
>
> 2. **Activate the environment:** On Windows: `.venv\Scripts\activate`. On Mac/Linux: `source .venv/bin/activate`. When active, your terminal prompt will show `(.venv)` as a prefix.
>    - Watch for: If PowerShell blocks activation with a "scripts are disabled" error, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` first. This is a one-time PowerShell security setting, not a Python issue.
>
> 3. **Tell VS Code about the environment:** After creating the venv, VS Code's Python extension should detect it automatically and show a notification asking if you want to use it. Click "Yes." If it does not, click the interpreter selector in the status bar and choose the Python from `.venv/Scripts/python.exe` (Windows) or `.venv/bin/python` (Mac/Linux).
>    - Watch for: If the environment does not appear in the interpreter list, use "Enter interpreter path..." and browse to the Python executable inside the `.venv` directory.
>
> 4. **Install packages into the environment:** With the environment active, `pip install requests` now installs requests into `.venv/lib/site-packages/` instead of the global location. Verify by running `pip list` — you should see only the packages you have explicitly installed (plus their dependencies), not the full global package set.
>    - Watch for: If `pip list` shows hundreds of packages, the environment is not active or VS Code is using the wrong interpreter. Check the terminal prefix for `(.venv)` and the status bar for the correct interpreter.
>
> 5. **Freeze dependencies:** When your project works, capture the exact package versions: `pip freeze > requirements.txt`. This creates a file listing every package and its version, which can be used to recreate the exact environment on another machine or at a later time.
>    - Watch for: Include `requirements.txt` in your project but NOT the `.venv` directory itself. The venv is machine-specific (contains absolute paths); the requirements file is portable.
>
> 6. **Recreate from requirements:** On a new machine or fresh clone, create a new venv (Step 1), activate it (Step 2), then run: `pip install -r requirements.txt`. This installs exactly the same packages at exactly the same versions.
>    - Watch for: If the original requirements file was generated on a different OS, some packages may not be available (particularly those with compiled C extensions on different architectures). This is rare for common packages but worth noting.
>
> **Expected outcome:** An isolated Python environment for each project, with dependencies explicitly tracked and reproducible.
> **If it's not working:** See the failure mode below regarding activation confusion.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
