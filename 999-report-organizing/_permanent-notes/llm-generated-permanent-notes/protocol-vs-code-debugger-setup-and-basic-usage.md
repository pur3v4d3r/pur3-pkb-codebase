---
title: 'Protocol: VS Code Debugger Setup and Basic Usage'
aliases:
- vs-code-debugger-configuration
- vscode-debugging
- 'Protocol: VS Code Debugger Setup and Basic Usage'
- protocol-vs-code-debugger-setup-and-basic-usage
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
# Protocol: VS Code Debugger Setup and Basic Usage

> [!definition] Protocol: VS Code Debugger Setup and Basic Usage
> Protocol: VS Code Debugger Setup and Basic Usage refers to a set of steps for configuring and using the built-in debugger in Visual Studio Code (VS Code) to identify and resolve logical errors in Python code by setting breakpoints, inspecting variables, and stepping through code.

## Additional Material

> [!protocol] Protocol: VS Code Debugger Setup and Basic Usage
> **When to use:** When traceback reading gives an unclear diagnosis, when the error is logical rather than syntactic, or when you need to understand the flow of execution through complex code
> **Time required:** 2–10 minutes per debugging session
> **Prerequisites:** Python extension installed, a `.py` file open in the editor
>
> 1. **Set a [[breakpoint|breakpoint]]:** Click in the gutter (the narrow column to the left of line numbers) at the line where you want execution to pause. A red dot appears. Place it at or before the line where you suspect the problem lies — if unsure, place it at the beginning of the function that eventually fails.
>    - Watch for: The red dot should be solid. If it is hollow or has a question mark, VS Code cannot set the breakpoint there (possibly due to a syntax error in the file preventing parsing).
>
> 2. **Start the debugger:** Press F5 or click "Run and Debug" from the sidebar. If prompted, select "Python File" as the debug configuration. The script will run normally until it reaches your breakpoint, then pause.
>    - Watch for: The first time you debug, VS Code may create a `.vscode/launch.json` file. Accept the defaults unless you need to pass arguments (add them in the `"args"` field of the configuration).
>
> 3. **Inspect variables:** When paused at a breakpoint, the Variables pane in the left sidebar shows all variables in the current scope and their values. Hover over any variable in the code editor to see its value as a tooltip. Use the Debug Console at the bottom to type expressions and see their results (e.g., type `len(my_list)` to check a list's length).
>    - Watch for: Variables will show as "not available" if they have not been assigned yet at the current point of execution.
>
> 4. **Step through code:** Use the debug toolbar buttons: Step Over (F10) executes the current line and moves to the next; Step Into (F11) enters a function call to debug inside it; Step Out (Shift+F11) finishes the current function and returns to the caller; Continue (F5) resumes execution until the next breakpoint.
>    - Watch for: Step Over versus Step Into is the key decision. Use Step Over to move through your own logic sequentially. Use Step Into only when you need to see what happens inside a specific function call.
>
> 5. **Identify the divergence point:** Watch the variables as you step. The moment a variable holds a value you did not expect — `None` instead of a list, an empty dictionary instead of one with data, a count of 0 instead of 10 — you have found the divergence point. The bug is either at that line or in whatever produced the unexpected value.
>    - Watch for: The divergence point is often several lines before the crash point. The traceback tells you where the program died; the debugger tells you where it went wrong.
>
> **Expected outcome:** Identification of the exact point where program state diverges from expectations, enabling a targeted fix.
> **If it's not working:** If the debugger does not pause at breakpoints, verify the debug configuration is set to "Python File" and not a different debug type. If the debugger launches but immediately terminates, check for syntax errors that prevent the script from loading.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[Virtual Environment]] · [[api]] · [[metacognition]] · [[debugging]] · [[automation]] · [[pip]] · [[Cognitive-Skill-Acquisition]] · [[Version-Control]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive Load Theory (CLT)]] · [[expertise-development]] · [[python-interpreter]] · [[GitHub Copilot]] · [[mental-model]] · [[repl]] · [[breakpoint]] · [[deliberate-practice]] · [[Package-Management]] · [[Git]] · [[situated-learning]] · [[information-processing-theory]] · [[distributed-cognition]] · [[Desirable-Difficulty]] · [[generation-effect]]
---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
