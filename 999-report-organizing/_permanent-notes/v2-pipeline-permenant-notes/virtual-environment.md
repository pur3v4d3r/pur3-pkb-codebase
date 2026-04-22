---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Virtual Environment"
aliases:
  - "Virtual Environment"
type: permanent-note
status: evergreen
confidence: medium

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - other
  - #python
  - #vs-code
  - #development-environment
  - #practitioners-field-guide
  - #ai-assisted-development

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-04-21
updated: 2026-04-21

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "python-development-in-vscode-practitioners-field-guide-2026-04-19"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"
pipeline-version: "2.1.0"
extraction-date: "2026-04-21"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  []

related:
  []

broader:
  []

narrower:
  []

see-also:
  - "[[python-interpreter|Python-Interpreter]]"
  - "[[integrated-development-environment|Integrated-Development-Environment]]"
  - "[[debugging|Debugging]]"
  - "[[virtual-environment|Virtual-Environment]]"
  - "[[github-copilot|GitHub-Copilot]]"
  - "[[mental-model]]"
  - "[[script-automation|Script-Automation]]"
  - "[[automation]]"
  - "[[api|API]]"
  - "[[python-interpreter|Python-Interpreter]]"
  - "[[command-line]]"
  - "[[linting|Linting]]"
  - "[[debugging|Debugging]]"
  - "[[type-hints|Type-Hints]]"
  - "[[pip]]"
  - "[[virtual-environment|Virtual-Environment]]"
  - "[[repl|REPL]]"
  - "[[virtual-environment|Virtual-Environment]]"
  - "[[repl|REPL]]"
  - "[[mental-model]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  []

enables:
  []

expansion-topics:
  []

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# Virtual Environment

> [!definition] **Virtual Environment** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> A virtual environment is an isolated Python installation — a self-contained directory that has its own copy of the Python interpreter, its own `pip`, and its own `site-packages` directory, completely independent of the global installation and of every other virtual environment. When a [[virtual-environment|virtual environment]] is active, all `pip install` commands install packages into that environment's private directory, and all `import` statements resolve from that private directory, which means that each project can have its own set of packages at its own versions without any possibility of conflict with other projects. The virtual environment is not a container or a virtual machine — it is simply a directory structure with a few scripts that redirect Python's package-lookup behavior to point at the local directory instead of the global one.

## Core Explanation

<!-- Expand this section with deeper explanation -->

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

## Conceptual Tensions

> [!tension] **Tension 1: Simplicity vs. Explicitness in Environment Management** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Python's design philosophy favors simplicity — `pip install` should just work. But the reality of dependency management requires explicitness — virtual environments, requirements files, version pinning. The tension manifests as: should the default `pip install` behavior install globally (simple but fragile) or require an active environment (explicit but adding friction)? Python currently defaults to global installation, and the practitioner must manually adopt the explicit pattern. This tension is being slowly resolved as tools like `pipx` and `uv` make per-project isolation more automatic,…

> [!tension] **Tension 2: AI Speed vs. Practitioner Understanding** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Copilot can generate correct code faster than a practitioner can learn to write it, creating a tension between productivity (let the AI do it) and [[Cognitive-Skill-Acquisition|skill development]] (learn to do it yourself). The Three Modes framework (Section 6) acknowledges that this tension has no single resolution — the right balance depends on the task, the stakes, and the practitioner's development goals. But the tension is real: every hour spent in Delegation mode is an hour not spent building the understanding that makes future Delegation safe.

> [!tension] **Tension 3: Convention vs. Configuration in Project Structure** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Python does not enforce a project structure the way frameworks like Rails or Django do. This flexibility means practitioners must decide how to organize their code, which requires judgment that beginners do not yet have. The tension is between Python's "we're all adults here" philosophy (trust the developer to make good structural choices) and the practical reality that beginners need structural guidance precisely because they lack the experience to make those choices well. Section 5 resolves this by providing an opinionated default structure while acknowledging that alternatives exist.

> [!tension] **Tension 4: VS Code Magic vs. Terminal Transparency** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> VS Code's Python extension automates many tasks — interpreter discovery, environment activation, launch configuration — that would otherwise require manual terminal commands. This automation reduces friction but also reduces transparency: when the automation works, the practitioner may not understand what it does; when it fails, the practitioner cannot diagnose the failure because they do not know what the automation was supposed to do. The guide addresses this by teaching the manual approach (terminal commands) as the foundation, then introducing VS Code automation as a convenience layer —…

## Reflection Prompts

> [!reflection] **Reflect** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Open your VS Code right now and check the bottom-right status bar. Does it show a Python interpreter? If so, open the integrated terminal and type `python --version`. Do the versions match? If you have never checked this correspondence before, you may discover that your environment has been silently misconfigured — a situation that produces no errors until you try to use a package that is installed in one Python but not the other.

> [!reflection] **Reflect** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Take a script you have — any Python file, even a simple one — and run it using each of the four methods described. Notice the differences: Does the working directory change? Does the terminal show different interpreter paths? Try adding `import sys; print(sys.executable)` to the script and observe whether all four methods use the same Python interpreter. This exercise builds the proprioceptive sense of your development environment that no amount of reading can substitute.

> [!reflection] **Reflect** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Think of the last time you encountered a Python error. How did you respond? Did you read the traceback systematically (bottom line first, then trace the chain) or reactively (scanning for familiar words or line numbers)? Next time an error appears, deliberately practice the three-step protocol: last line, your code, the "why" question. Notice whether this changes the speed and accuracy of your diagnosis compared to your habitual approach.

> [!reflection] **Reflect** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Examine your current Python projects. How many of them have their own virtual environment? If any use the global Python installation, consider the risk: every future `pip install` for any project could potentially break them. As an exercise, take one of these projects, create a `.venv`, install its dependencies inside it, and verify that it still runs. Notice the peace of mind that comes from knowing this project's environment is immune to changes made elsewhere.

> [!reflection] **Reflect** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Look at the longest Python file you currently have. Can you identify three distinct responsibilities within it — three groups of functions that serve different purposes? If so, imagine splitting them into separate files. What would you name each file? What functions would go into each? Try sketching the directory structure on paper before touching the code. This [[chunking|chunking]] exercise — decomposing a monolith into named components — is itself a transferable cognitive skill that applies…

> [!reflection] **Reflect** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Think of the last time you used Copilot or a similar assistant to generate Python code. Which of the three modes were you operating in? Did you read the code before running it? Could you modify it now, from memory, to handle a case it does not currently handle? If you are honest with yourself about these questions, the answers will tell you whether your AI-assisted workflow is building or eroding your skills. As an experiment, next time Copilot generates code, try Step 4 of the protocol —…

> [!reflection] **Reflect** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Think of three tasks you perform manually on a regular basis that involve files, data, or communication between systems. For each, consult the Problem-Library Map above. Could any of them be automated with a Python script? Pick the simplest one and describe it to Copilot as an intent comment: `# Script to [your task description]`. Let it generate a first draft. Even if you do not run it immediately, the exercise of mapping a real problem to a Python solution builds the problem-library mapping…

> [!reflection] **Reflect** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Take one of your existing Python projects and attempt the test-from-scratch protocol: copy it to a new directory, create a fresh virtual environment, install only from `requirements.txt`, and try to run it. How many steps fail? Each failure is a piece of implicit knowledge that exists only in your head — knowledge that must be made explicit before the project can live beyond your machine. This exercise develops the crucial [[metacognition|metacognitive]] skill of seeing your own assumptions…

## Far Transfer Applications

> [!far-transfer] **Transfer Domain 1: Any Command-Line Tool Ecosystem** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> The three-layer architecture from Section 1 — operating system PATH, tool-specific configuration, terminal session context — applies to every command-line tool ecosystem, not just Python. Node.js developers face the same "which node" problem with multiple versions; Ruby developers manage identical challenges with `rbenv` and `rvm`; even system administrators managing tools like Docker, kubectl, or Terraform must reason about which version their terminal session is actually invoking. The diagnostic protocol is identical: verify the tool's version, check `where`/`which` to confirm the…

> [!far-transfer] **Transfer Domain 2: Dependency Management in Any Language** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> The virtual environment and requirements.txt pattern (Section 4) is Python's specific implementation of a universal software engineering principle: [[Abstraction|dependency isolation]]. JavaScript achieves this through `package.json` and `node_modules/`; Ruby through `Gemfile` and Bundler; Rust through `Cargo.toml`; Java through Maven or Gradle. The specific commands differ, but the underlying architecture is identical: declare dependencies explicitly, install them into an isolated location, lock versions for reproducibility, and never allow one project's dependencies to contaminate…

> [!far-transfer] **Transfer Domain 3: AI-Assisted Work Beyond Coding** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> The Three Modes framework from Section 6 — Delegation, Scaffolding, and Dialogue — transfers directly to any domain where [[AI-Agents|AI assistants]] augment human work: writing, analysis, research, design, or decision-making. The Cargo Cult failure mode applies universally: accepting AI output without the ability to evaluate, modify, or defend it produces work that is formally competent but substantively unowned. The Copilot Collaboration Workflow translates: state your intent before seeing AI output, read and evaluate before using, test against known cases, modify to verify understanding,…

> [!far-transfer] **Transfer Domain 4: The PTAL Pattern as a Learning Framework** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> This guide used the Problem-Theory-Application-Limits structure throughout — and this structure is itself a transferable method for learning any complex skill domain. When approaching a new subject, begin with a concrete situation you face (Problem), seek the framework that explains it (Theory), translate the framework into action steps (Application), and identify where the framework fails (Limits). This sequence, applied to cooking, music, management, medicine, or any practical domain, produces the same benefit it produced here: knowledge that is immediately applicable because it was always…

## AI Insights

> [!claude-insight] **Claude's Perspective: The Two Kinds of Errors** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> There is a distinction that experienced developers internalize so deeply they forget it is not obvious — the distinction between errors that crash the program and errors that let it continue but produce wrong results. Tracebacks only appear for the first kind. The second kind — logical errors, off-by-one mistakes, incorrect conditional branches, variables that hold stale values — produce no error message at all. The code runs, produces output, and that output is quietly, invisibly wrong. This is why the debugger is not merely a tool for fixing crashes but a tool for understanding behavior,…

> [!claude-insight] **Claude's Perspective: The Understanding Verification Problem** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> The deepest challenge of AI-assisted coding is not that the AI produces bad code — it often produces excellent code — but that the practitioner has no reliable internal metric for whether they understand the code well enough to own it. "I read it and it makes sense" is not the same as understanding, because code can appear sensible without the reader grasping its boundary conditions, performance characteristics, or failure modes. The only reliable test of understanding is the ability to modify the code to handle a case the AI did not anticipate, or to explain — without looking at the code —…

> [!claude-insight] **Claude's Perspective: Python as Connective Tissue** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> The most underappreciated role of Python in a practitioner's toolkit is not as a destination language — a language in which one builds complete applications from scratch — but as **connective tissue** between other systems. A 20-line Python script can read data from a database, call a web API with that data, parse the response, write the result to a spreadsheet, and email a notification — connecting five systems that have no native ability to talk to each other. This connective role is why Python literacy is valuable even for practitioners whose primary domain is not software development: it…

## Section Summaries

> [!section-summary] **Practical Takeaways — Section 1** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> When setting up Python in VS Code, the critical understanding is that three independent systems must agree on where Python lives: the operating system's PATH, the VS Code Python extension's interpreter selection, and the terminal session's inherited environment. The setup protocol ensures all three point to the same installation. When they disagree, the "Multiple Pythons Problem" produces confusing behavior where packages install to one Python but code runs with another. The single most important checkbox in the entire setup process is "Add python.exe to PATH" during installation — missing it…

> [!section-summary] **Practical Takeaways — Section 2** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> VS Code provides four distinct execution paths for Python code — Run File, Run Selection, direct terminal execution, and debugger launch — each suited to different situations. The green Run button is the simplest and handles interpreter selection automatically. Run Selection is the best tool for learning and exploration. Direct terminal commands give maximum control but require attention to PATH and [[virtual-environment|virtual environment]] activation. The most common execution failure is the Working Directory Trap, where relative file paths resolve differently depending on which execution…

> [!section-summary] **Practical Takeaways — Section 3** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Python tracebacks are structured diagnostic documents: read the last line first for the error type, find your own code in the chain, and ask "why" to trace back to the root cause. The VS Code debugger extends this diagnostic capability from crash analysis to behavioral understanding — it lets you observe code in motion, inspect variable states at any point, and identify the exact moment where reality diverges from expectation. The two critical anti-patterns are reading tracebacks reactively (scanning for something that "looks wrong" rather than following the systematic protocol) and…

> [!section-summary] **Practical Takeaways — Section 4** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Virtual environments solve the fundamental problem of Python [[Package-Management|package management]] — that packages installed globally are shared across all projects and can conflict with each other. The protocol is simple and non-negotiable: create a `.venv` for every project, activate it before installing packages or running scripts, freeze dependencies to `requirements.txt` for reproducibility, and never commit the `.venv` directory to [[Git|version control]]. The most common failure is Activation Amnesia — forgetting that venv activation is session-specific and not persistent. The…

> [!section-summary] **Practical Takeaways — Section 5** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Python's module and import system transforms a collection of files into a navigable codebase by allowing one file to access code defined in another through the `import` statement. The standard project structure places all code in a root directory alongside the virtual environment and requirements file, with modules named in snake_case and separated by logical responsibility. The `if __name__ == "__main__":` guard makes the entry-point script importable without side effects. Start with a flat structure and add package directories only when the project demands it. The most common failure after…

> [!section-summary] **Practical Takeaways — Section 6** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> AI coding assistants are powerful tools whose value depends entirely on how they are used. The Three Modes framework — Delegation, Scaffolding, and Dialogue — provides a decision structure for matching the AI interaction to the task. The Copilot Collaboration Workflow ensures that generated code is understood before it is integrated: write the intent first, read before running, test with controlled inputs, modify to verify understanding, and add your own comments. The primary anti-pattern is the Cargo Cult — accumulating code you cannot explain or modify. The governing principle is: accept no…

> [!section-summary] **Practical Takeaways — Section 7** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Python's ecosystem is organized in concentric rings: the standard library (batteries included, no installation needed), PyPI (500,000+ packages via pip), and the broader tooling ecosystem. The practitioner's key skill is problem-library mapping — recognizing which ring and which library addresses the problem at hand. Python's greatest strength is as connective tissue — linking systems, transforming data between formats, and automating workflows that would otherwise require manual effort. The Problem-Library Map above is a starting reference; expand it as your experience grows. For any problem…

> [!section-summary] **Practical Takeaways — Section 8** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> Making a Python project shareable requires making its implicit context explicit through a reproducibility stack: `requirements.txt` for dependencies, a README for setup instructions, `.gitignore` for excluding machine-specific artifacts, and environment variables for secrets. The protocol's most powerful step is the test-from-scratch verification — cloning your own project into a fresh directory and attempting to set it up using only the documented instructions. Every step that fails is a gap you would otherwise inflict on every future user of your code. The Secrets Problem is the most…

## Protocols & Methods

> [!protocol] **Protocol: Complete Python + VS Code Setup from Scratch** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> **When to use:** First-time Python setup, or when a previous installation has become confused
> **Time required:** 10–20 minutes
> **Prerequisites:** VS Code installed, internet access, administrator privileges on the machine
> 
> 1. **Download Python from python.org:** Navigate to python.org/downloads and download the latest stable release (3.12 or later). Choose the Windows installer (64-bit) for most modern systems.
>    - Watch for: The download page may show multiple versions. Choose the one labeled "Latest Python 3" unless you have a specific version requirement.
> 
> 2. **Run the installer with PATH enabled:** When the installer opens, **check the box labeled "Add python.exe to PATH" before clicking anything else.** Then click "Install Now" for a standard installation, or "Customize…

> [!protocol] **Protocol: Systematic Traceback Reading** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> **When to use:** Any time a Python script produces an error with a traceback
> **Time required:** 1–5 minutes per error
> **Prerequisites:** The error output visible in the terminal or debug console
> 
> 1. **Read the LAST line first:** This is the error type and message. `TypeError: 'NoneType' object is not subscriptable` tells you that code tried to index into something (like `result[0]`) but that thing was `None` instead of a list or dictionary.
>    - Watch for: The error type is the word before the colon. Google `Python [ErrorType]` for general explanations of what causes this class of error.
> 
> 2. **Find YOUR code in the traceback:** Scan upward from the bottom for file paths that belong to your project (as opposed to paths inside Python's standard library or installed packages). The last entry…

> [!protocol] **Protocol: VS Code Debugger Setup and Basic Usage** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> **When to use:** When traceback reading gives an unclear diagnosis, when the error is logical rather than syntactic, or when you need to understand the flow of execution through complex code
> **Time required:** 2–10 minutes per debugging session
> **Prerequisites:** Python extension installed, a `.py` file open in the editor
> 
> 1. **Set a [[breakpoint|breakpoint]]:** Click in the gutter (the narrow column to the left of line numbers) at the line where you want execution to pause. A red dot appears. Place it at or before the line where you suspect the problem lies — if unsure, place it at the beginning of the function that eventually fails.
>    - Watch for: The red dot should be solid. If it is hollow or has a question mark, VS Code cannot set the breakpoint there (possibly due to a syntax error…

> [!protocol] **Protocol: Creating and Managing Virtual Environments in VS Code** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> **When to use:** At the start of every new Python project — no exceptions
> **Time required:** 2–5 minutes for initial setup
> **Prerequisites:** Python installed and working in VS Code (Section 1 complete)
> 
> 1. **Create the virtual environment:** Open the integrated terminal in your project's root directory. Run: `python -m venv .venv`
>    - This creates a `.venv` directory containing a private Python installation. The name `.venv` is conventional — the leading dot hides it in most file explorers, and VS Code recognizes it automatically.
>    - Watch for: If `python -m venv` fails, you may need `py -m venv .venv` on Windows, or you may need to install the `python3-venv` package on Linux.
> 
> 2. **Activate the environment:** On Windows: `.venv\Scripts\activate`. On Mac/Linux: `source…

> [!protocol] **Protocol: Standard Python Project Structure** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> **When to use:** When a project has grown beyond ~200 lines or involves more than one logical concern (data processing, output formatting, configuration, etc.)
> **Time required:** 15–30 minutes for initial restructuring
> **Prerequisites:** A working single-file script that you want to decompose
> 
> 1. **Establish the project root:** Create a dedicated directory for the project. This is the directory that contains your virtual environment, your `requirements.txt`, and all project code.
>    ```
>    my_project/
>    ├── .venv/
>    ├── requirements.txt
>    └── main.py
>    ```
>    - Watch for: The project root should be the directory you open in VS Code (File → Open Folder). This ensures VS Code's workspace features (search, go-to-definition, terminal working directory) all operate from the correct…

> [!protocol] **Protocol: The Copilot Collaboration Workflow** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> **When to use:** Whenever Copilot generates code that you intend to keep in your project
> **Time required:** 2–10 minutes per generated block (the verification is the investment)
> **Prerequisites:** Copilot or equivalent AI assistant active in VS Code; basic Python reading ability
> 
> 1. **Write the intent comment first:** Before letting Copilot generate code, write a clear comment describing what you want: `# Read CSV, filter rows where 'status' is 'active', return as list of dicts`. This forces you to articulate the requirement before seeing any implementation, which anchors your evaluation.
>    - Watch for: Vague comments produce vague code. "# Process the data" will generate something, but you will have no basis for evaluating whether it is correct. Be specific about inputs, outputs, and…

> [!protocol] **Protocol: Making a Python Project Shareable** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> **When to use:** Before sharing a project with anyone — a colleague, a client, or your future self across machines
> **Time required:** 15–30 minutes for a small project
> **Prerequisites:** A working project with a virtual environment (Section 4)
> 
> 1. **Verify and freeze dependencies:** Activate the project's virtual environment and run `pip freeze > requirements.txt`. Open the file and review it — does it contain only the packages your project actually uses, or does it include unrelated packages from earlier experimentation? If the latter, consider creating a clean venv, installing only the packages you need, and re-freezing.
>    - Watch for: `pip freeze` captures everything in the environment, including indirect dependencies. This is generally what you want — it ensures exact…

> [!protocol] **THE MASTER PROTOCOL: Python Project Lifecycle in VS Code** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> This integrates all section-level protocols into a single reference. Use as a checklist for new projects or as a diagnostic when something feels wrong in an existing project.
> 
> **PHASE 1: PROJECT INITIALIZATION**
> *(Sections 1, 4, 5)*
> 
> - [ ] Python installed and in PATH (`python --version` succeeds)
> - [ ] VS Code Python extension installed (ms-python.python)
> - [ ] Project directory created and opened as VS Code workspace
> - [ ] Virtual environment created: `python -m venv .venv`
> - [ ] Virtual environment activated (terminal shows `(.venv)` prefix)
> - [ ] VS Code interpreter set to `.venv` Python (status bar)
> - [ ] `.gitignore` created with `.venv/`, `__pycache__/`, `.env`
> - [ ] Git initialized: `git init`
> 
> **PHASE 2: DEVELOPMENT**
> *(Sections 2, 5, 6)*
> 
> - [ ] Entry point file created…

## Connections & Context

**Related concepts:**
[[python-interpreter|Python-Interpreter]] · [[integrated-development-environment|Integrated-Development-Environment]] · [[debugging|Debugging]] · [[virtual-environment|Virtual-Environment]] · [[github-copilot|GitHub-Copilot]] · [[mental-model]] · [[script-automation|Script-Automation]] · [[automation]] · [[api|API]] · [[python-interpreter|Python-Interpreter]] · [[command-line]] · [[linting|Linting]] · [[debugging|Debugging]] · [[type-hints|Type-Hints]] · [[pip]] · [[virtual-environment|Virtual-Environment]] · [[repl|REPL]] · [[virtual-environment|Virtual-Environment]] · [[repl|REPL]] · [[mental-model]] · [[virtual-environment|Virtual-Environment]] · [[breakpoint|Breakpoint]] · [[virtual-environment|Virtual-Environment]] · [[api|API]] · [[stack-trace|Stack-Trace]] · [[problem-solving|Problem-Solving]] · [[error-handling|Error-Handling]] · [[breakpoint|Breakpoint]] · [[deliberate-practice]] · [[debugging|Debugging]]

## Methodology Notes

> [!methodology-and-sources] **How to Use This Field Guide** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> This guide is designed for the VS Code power user who has little or no Python experience but finds themselves needing it with increasing frequency — for [[script-automation|scripting]], [[automation|automation]], data processing, or [[api]]-driven workflows. You know your editor well; what you lack is the mental model of how Python operates within it.
> 
> **Each section follows a consistent PTAL structure:**
> - **Scenario:** A recognizable situation to orient you — the kind of problem you have likely already encountered or will encounter soon
> - **Framework:** The conceptual architecture that…

> [!methodology-and-sources] **How This Guide Was Constructed** *(from [[python-development-in-vscode-practitioners-field-guide-2026-04-19]])*
> This report uses the **PTAL (Problem-Theory-Application-Limits) methodology** — a practice-first structure in which every section opens with a recognizable situation the practitioner might face, introduces theory only to explain that situation, translates theory into actionable protocols, and then addresses failure modes and boundary conditions.
> 
> **Why PTAL instead of theory-first?** Traditional instructional design presents concepts first and applications second — "here is the import system, now here is how to use it." This approach is logically clean but pedagogically inverted for…

---

## Source Attribution

**Extracted from:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
