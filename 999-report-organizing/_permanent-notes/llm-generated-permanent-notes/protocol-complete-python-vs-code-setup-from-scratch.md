---
title: 'Protocol: Complete Python + VS Code Setup from Scratch'
aliases:
- Python + VS Code setup
- Python development environment setup
- 'Protocol: Complete Python + VS Code Setup from Scratch'
- protocol-complete-python-vs-code-setup-from-scratch
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
# Protocol: Complete Python + VS Code Setup from Scratch

> [!definition] Protocol: Complete Python + VS Code Setup from Scratch
> Protocol: Complete Python + VS Code Setup from Scratch is a step-by-step procedure for installing Python and configuring Visual Studio Code to support Python development, including setting up the PATH environment variable, installing necessary extensions, and verifying the setup.

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
> 4. **Install the Python extension in VS Code:** Open VS Code, go to Extensions (Ctrl+Shift+X), search for "Python" and install the extension published by Microsoft (ms-python.python). This will also install Pylance for [[type-hints|type checking]] and IntelliSense.
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

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
