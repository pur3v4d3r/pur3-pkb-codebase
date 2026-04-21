---
title: "Protocol: Complete Python + VS Code Setup from Scratch"
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

# Protocol: Complete Python + VS Code Setup from Scratch

> [!definition] Protocol: Complete Python + VS Code Setup from Scratch
> *Definition pending — derived from 1 source report(s).*

## Additional Material

> [!protocol] Protocol: Complete Python + VS Code Setup from Scratch
> **When to use:** First-time Python setup, or when a previous installation has become confused
> **Time required:** 10–20 minutes
> **Prerequisites:** VS Code installed, internet access, administrator privileges on the machine
>
> 1. **Download Python from python.org:** Navigate to python.org/downloads and download the latest stable release (3.12 or later). Choose the Windows installer (64-bit) for most modern systems.
>    - Watch for: The download page may show multiple versions. Choose the one labeled "Latest Python 3" unless you have a specific version requirement.
>
> 2. **Run the installer with PATH enabled:** When the installer opens, **check the box labeled "Add python.exe to PATH" before clicking anything else.** Then click "Install Now" for a standard installation, or "Customize installation" if you need to change the install directory.
>    - Watch for: If you miss the PATH checkbox, you will need to add the Python directory to PATH manually through System Properties → Environment Variables → Path, adding both `C:\Users\[YourName]\AppData\Local\Programs\Python\Python3XX\` and its `Scripts\` subdirectory.
>
> 3. **Verify the installation in a terminal:** Open a fresh terminal (not one that was open before the install — it will not have the updated PATH). Type `python --version` and press Enter. You should see output like `Python 3.12.x`.
>    - Watch for: On some Windows configurations, `python` may not work but `py` will. If `py --version` succeeds, Python is installed but the PATH entry is missing or points to the wrong location.
>
> 4. **Install the Python extension in VS Code:** Open VS Code, go to Extensions (Ctrl+Shift+X), search for "Python" and install the extension published by Microsoft (ms-python.python). This will also install Pylance for [[Type-Hints|type checking]] and IntelliSense.
>    - Watch for: There are multiple Python-related extensions. The official Microsoft one has millions of installs and a blue verified checkmark.
>
> 5. **Select the Python interpreter:** Open a `.py` file, then look at the bottom-right of the VS Code status bar. Click where it says "Select Interpreter" (or shows a Python version). From the dropdown, select the Python installation you just verified in Step 3. If it does not appear, click "Enter interpreter path..." and browse to the Python executable.
>    - Watch for: If you see multiple interpreters listed (e.g., from Anaconda, WSL, or previous installations), select the one matching the version you just installed. The path should contain `Python3XX` in a `Programs` directory.
>
> 6. **Test the complete chain:** Create a file called `test_setup.py` containing `print("Setup complete!")`. Press F5 or click the Run button (triangle icon in the top-right). The integrated terminal should open, execute the script, and display "Setup complete!".
>    - Watch for: If VS Code asks you to create a launch configuration, select "Python File" from the dropdown. If the terminal shows a PATH error despite the status bar showing a valid interpreter, restart VS Code completely — the terminal session may have cached the old PATH.
>
> **Expected outcome:** A working Python installation recognized by both the system terminal and VS Code, with the Python extension providing IntelliSense, linting, and run/debug capabilities.
> **If it's not working:** See the failure mode below, then try the verification checklist in the Appendix.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Python-Interpreter]] · [[Integrated-Development-Environment]] · [[Debugging]] · [[Virtual-Environment]] · [[GitHub-Copilot]] · [[mental-model]] · [[Script-Automation]] · [[automation]] · [[API]] · [[Python-Interpreter]] · [[command-line]] · [[Linting]] · [[Debugging]] · [[Type-Hints]] · [[pip]] · [[Virtual-Environment]] · [[REPL]] · [[Virtual-Environment]] · [[REPL]] · [[mental-model]] · [[Virtual-Environment]] · [[Breakpoint]] · [[Virtual-Environment]] · [[API]] · [[Stack-Trace]] · [[Problem-Solving]] · [[Error-Handling]] · [[Breakpoint]] · [[deliberate-practice]] · [[Debugging]] · [[Cognitive-Skill-Acquisition]] · [[API]] · [[pip]] · [[Dependency-Management]] · [[Virtual-Environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[Architecture-Patterns]] · [[chunking]] · [[GitHub-Copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[Active-Learning]] · [[cognitive-scaffolding]] · [[API]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[API]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[cognitive-load-theory]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[expertise-reversal-effect]] · [[generation-effect]] · [[scaffolding]] · [[cognitive-load-theory]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[cognitive-load-theory]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[scaffolding]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[Protocol Complete Python + VS Code Setup from Scratch]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
