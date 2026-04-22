---
title: "Protocol: Standard Python Project Structure"
aliases: [Python project structure, PEP 405]
type: permanent-note
status: evergreen
confidence: medium
domain: programming
subdomains: []
tags: [permanent-note, programming]
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

# Protocol: Standard Python Project Structure

> [!definition] Protocol: Standard Python Project Structure
> *Definition pending — derived from 1 source report(s).*

## Additional Material

> [!protocol] Protocol: Standard Python Project Structure
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
>    - Watch for: The project root should be the directory you open in VS Code (File → Open Folder). This ensures VS Code's workspace features (search, go-to-definition, terminal working directory) all operate from the correct base.
>
> 2. **Identify logical modules:** Read through your monolithic script and identify distinct responsibilities: data loading, data transformation, output formatting, configuration, utility functions. Each of these becomes a separate `.py` file.
>    - Watch for: A module should have a clear, single purpose expressible in a short phrase. If you cannot describe what a module does in one sentence, it may be trying to do too much.
>
> 3. **Create the module files:** For a small-to-medium project, flat organization (all `.py` files in the project root) is sufficient:
>    ```
>    my_project/
>    ├── .venv/
>    ├── requirements.txt
>    ├── main.py          # Entry point — orchestrates the workflow
>    ├── data_loader.py   # Functions for reading input data
>    ├── processor.py     # Data transformation logic
>    ├── formatter.py     # Output formatting
>    └── config.py        # Configuration constants and settings
>    ```
>    - Watch for: Name files with lowercase and underscores (snake_case). Python module names become identifiers in your code (`import data_loader`), so they must follow Python naming rules — no spaces, no hyphens, no starting with numbers.
>
> 4. **Move functions and add imports:** Cut functions from the monolithic script and paste them into the appropriate module. In `main.py`, add import statements: `from data_loader import read_csv` or `import processor`. Move configuration values (file paths, constants, parameters) to `config.py` and import them where needed.
>    - Watch for: Circular imports — if `data_loader.py` imports from `processor.py` and `processor.py` imports from `data_loader.py`, Python will raise an `ImportError`. This usually indicates that the two modules are not properly separated. Resolve by creating a third module for the shared dependency, or by restructuring the code.
>
> 5. **Add the `if __name__ == "__main__":` guard to the entry point:** In `main.py`, wrap the execution logic:
>    ```python
>    def main():
>        # Your orchestration code here
>        data = read_csv("input.csv")
>        result = process(data)
>        write_output(result)
>
>    if __name__ == "__main__":
>        main()
>    ```
>    This guard ensures the script runs when executed directly (`python main.py`) but not when imported as a module by another script.
>    - Watch for: This is not boilerplate — it is a structural pattern that makes your code reusable. Without it, importing `main.py` from another script would execute the entire workflow as a side effect.
>
> 6. **Verify in VS Code:** Open the project folder in VS Code. Try Ctrl+Click on an imported function name — VS Code should navigate to its definition in the source module. Try F2 on a function name to rename it across all files. These features confirm that VS Code understands your project's module structure.
>    - Watch for: If go-to-definition does not work, ensure the Python extension has fully loaded (check the status bar) and that the correct interpreter is selected. Large projects may take a moment to index.
>
> **Expected outcome:** A project organized into focused modules with clear responsibilities, navigable through VS Code's code intelligence features.
> **If it's not working:** Import errors after restructuring usually mean the working directory assumption is wrong — see Section 2's Working Directory Trap.
> *— [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]*

## Connections

**Related:** [[python-interpreter]] · [[integrated-development-environment]] · [[debugging]] · [[virtual-environment]] · [[github-copilot]] · [[mental-model]] · [[script-automation]] · [[automation]] · [[api]] · [[python-interpreter]] · [[command-line]] · [[linting]] · [[debugging]] · [[type-hints]] · [[pip]] · [[virtual-environment]] · [[repl]] · [[virtual-environment]] · [[repl]] · [[mental-model]] · [[virtual-environment]] · [[breakpoint]] · [[virtual-environment]] · [[api]] · [[stack-trace]] · [[problem-solving]] · [[error-handling]] · [[breakpoint]] · [[deliberate-practice]] · [[debugging]] · [[Cognitive-Skill-Acquisition]] · [[api]] · [[pip]] · [[Dependency-Management]] · [[virtual-environment]] · [[Package-Management]] · [[Version-Control]] · [[Package-Management]] · [[Git]] · [[architecture-patterns]] · [[chunking]] · [[github-copilot]] · [[Cognitive-Skill-Acquisition]] · [[deliberate-practice]] · [[active-learning]] · [[cognitive-scaffolding]] · [[api]] · [[automation]] · [[Python-Standard-Library]] · [[pip]] · [[api]] · [[Regular-Expressions]] · [[Async-Programming]] · [[Programming-Concepts]] · [[Continuous-Integration-Continuous-Deployment]] · [[Git]] · [[Version-Control]] · [[metacognition]] · [[Abstraction]] · [[AI-Agents]] · [[self-regulated-learning]] · [[Cognitive-Skill-Acquisition]] · [[situated-learning]] · [[Contemplative-Mechanism]] · [[Test-Driven-Development]] · [[Quality-Assurance]] · [[metacognition]] · [[Empirical-Research-Methods]] · [[information-processing-theory]] · [[Data-Literacy]] · [[Visual-Representation]] · [[Information-Retrieval]] · [[Digital-Literacy]] · [[Ethical-Reasoning]] · [[cognitive-load-theory]] · [[distributed-cognition]] · [[expertise-development]] · [[Desirable-Difficulty]] · [[expertise-reversal-effect]] · [[generation-effect]] · [[scaffolding]] · [[cognitive-load-theory]] · [[self-regulated-learning]] · [[metacognition]] · [[expertise-development]] · [[AI-Agents]] · [[cognitive-load-theory]] · [[metacognition]] · [[self-regulated-learning]] · [[expertise-development]] · [[scaffolding]] · [[situated-learning]] · [[Desirable-Difficulty]] · [[generation-effect]] · [[transfer-of-learning]] · [[Python]] · [[vs-code]] · [[AI-Agents]] · [[Version-Control]] · [[personal-knowledge-management]] · [[automation]] · [[information-processing-theory]] · [[distributed-cognition]]

```dataview
LIST FROM [[Protocol Standard Python Project Structure]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[python-development-in-vscode-practitioners-field-guide-2026-04-19]]
