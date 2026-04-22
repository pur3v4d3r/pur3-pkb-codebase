---
title: "Protocol: VS Code Debugger Setup and Basic Usage"
aliases: [vs-code-debugger-configuration, vscode-debugging]
type: permanent-note
status: evergreen
confidence: medium
domain: uncategorized
subdomains: []
tags: [permanent-note, uncategorized]
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

# Protocol: VS Code Debugger Setup and Basic Usage

> [!definition] Protocol: VS Code Debugger Setup and Basic Usage
> *Definition pending — derived from 1 source report(s).*

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

**Related:** [[python-interpreter]] · [[integrated-development-environment]] · [[debugging]] · [[Virtual Environment]] · [[GitHub Copilot]] · [[mental-model]] · [[script-automation]] · [[automation]] · [[api]] · [[python-interpreter]] · [[command-line]] · [[linting]] · [[debugging]] · [[type-hints]] · [[pip]] · [[Virtual Environment]] · [[repl]] · [[Virtual Environment]] · [[repl]] · [[mental-model]] · [[Virtual Environment]] · [[breakpoint]] · [[Virtual Environment]] · [[api]] · [[stack-trace]] · [[problem-solving]] · [[error-handling]] · [[breakpoint]] · [[deliberate-practice]] · [[debugging]] · [[Cognitive-Skill-Acquisition]] · [[api]] · [[pip]] · [[Dependency-Management]] · [[Virtual Environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[architecture-patterns]] · [[Chunk (Miller, 1956; Chase & Simon, 1973)]] · [[GitHub Copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[active-learning]] · [[Cognitive Scaffolding]] · [[api]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[api]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[Cognitive Load Theory (CLT)]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[Expertise Reversal Effect (Kalyuga, Ayres, Chandler, Sweller, 2003)]] · [[generation-effect]] · [[Scaffolded Fading]] · [[Cognitive Load Theory (CLT)]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[Cognitive Load Theory (CLT)]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[Scaffolded Fading]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[Protocol VS Code Debugger Setup and Basic Usage]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
