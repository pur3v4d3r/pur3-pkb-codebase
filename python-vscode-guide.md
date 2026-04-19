# Running Python Scripts in VS Code — Complete Guide

## Foundation: Setting Up Your Environment

### Installing the Python Extension

Before you can run anything, install Microsoft's official **Python** extension (publisher: `ms-python`). Open the Extensions sidebar (`Ctrl+Shift+X` / `Cmd+Shift+X`), search "Python", and install it. This extension provides IntelliSense, linting, debugging, and — critically — interpreter selection. It also bundles **Pylance** for type checking and auto-completion.

Once installed, you'll see a Python version indicator in the bottom-left status bar. Click it to select which interpreter VS Code should use.

### Selecting and Managing Python Interpreters

VS Code can detect system Python, pyenv versions, conda environments, and virtual environments. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and type **"Python: Select Interpreter"** to see all available options.

**Creating a virtual environment from within VS Code:**

```bash
# In the integrated terminal
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate
```

After creating a `.venv` folder in your project root, VS Code will usually detect it automatically and prompt you to use it. If not, select it manually through the interpreter picker. The active interpreter is shown in the status bar and determines which Python runs your scripts.

**Why this matters:** If you run a script and get `ModuleNotFoundError` for a package you know you installed, you're almost certainly using the wrong interpreter. Always verify the status bar matches the environment where you installed your packages.

---

## The Basics: Four Ways to Run a Script

### Method 1: The Run Button (▶)

With a `.py` file open, click the **play button** in the top-right corner of the editor. This opens the integrated terminal and executes `python your_script.py` using the selected interpreter. It's the simplest method and works immediately.

**What actually happens:** VS Code runs something like:

```
/path/to/your/python /path/to/your/script.py
```

The full path to both the interpreter and your script file is used, which means it works regardless of your terminal's current directory or PATH configuration.

### Method 2: Running in the Integrated Terminal

Open the integrated terminal (`Ctrl+`` ` or `Ctrl+Shift+`` ` for a new one) and type:

```bash
python script.py
```

This gives you full control over arguments, environment variables, and working directory. It's what you'll use most often for real development work.

**Key shortcuts for the integrated terminal:**

| Action | Windows/Linux | macOS |
|---|---|---|
| Toggle terminal | `` Ctrl+` `` | `` Cmd+` `` |
| New terminal | `` Ctrl+Shift+` `` | `` Cmd+Shift+` `` |
| Split terminal | `Ctrl+Shift+5` | `Cmd+\` |
| Kill terminal | Trash icon or type `exit` | Same |
| Clear terminal | `clear` or `Ctrl+L` | `Cmd+K` |
| Scroll up | `Ctrl+Shift+↑` | `Cmd+↑` |
| Copy selection | `Ctrl+Shift+C` | `Cmd+C` |

### Method 3: Run Selection / Run Line

Select a block of code (or place your cursor on a single line) and press `Shift+Enter`. VS Code sends that code to the Python terminal (or a REPL) and executes it. This is extremely useful for iterative development — testing a function, checking a variable's value, or running a quick calculation without executing the entire file.

**Pro tip:** If no terminal is open, `Shift+Enter` opens one and starts a Python REPL. Subsequent `Shift+Enter` commands send code to that same REPL session, preserving state between executions.

### Method 4: The Debug Console

Press `F5` to start debugging (covered in detail below). The Debug Console at the bottom lets you evaluate expressions in the context of your running program — inspect variables, call functions, test conditions. It's a live REPL attached to your program's state at the current breakpoint.

---

## Command-Line Arguments and Environment Variables

### Passing Arguments to Scripts

When running from the terminal, arguments work exactly as they would in any shell:

```bash
python train_model.py --epochs 50 --learning-rate 0.001 --data ./dataset.csv
```

For the Run button or debugger, configure arguments in `.vscode/launch.json`:

```jsonc
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Train Model",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "args": ["--epochs", "50", "--learning-rate", "0.001", "--data", "./dataset.csv"],
      "console": "integratedTerminal"
    }
  ]
}
```

Now pressing `F5` runs your script with those arguments automatically.

### Setting Environment Variables

**Option A — In the terminal directly:**

```bash
# Linux/macOS
export API_KEY="sk-abc123"
python app.py

# Windows PowerShell
$env:API_KEY = "sk-abc123"
python app.py

# Windows CMD
set API_KEY=sk-abc123
python app.py
```

**Option B — Using a `.env` file (recommended):**

Create a `.env` file in your project root:

```env
API_KEY=sk-abc123
DATABASE_URL=postgresql://localhost:5432/mydb
DEBUG=true
```

Then in `launch.json`:

```jsonc
{
  "name": "Run with .env",
  "type": "debugpy",
  "request": "launch",
  "program": "${file}",
  "envFile": "${workspaceFolder}/.env",
  "console": "integratedTerminal"
}
```

The Python extension loads these variables before your script runs. Add `.env` to your `.gitignore` to keep secrets out of version control.

**Option C — Inline in launch.json:**

```jsonc
{
  "name": "Custom Env",
  "type": "debugpy",
  "request": "launch",
  "program": "${file}",
  "env": {
    "PYTHONPATH": "${workspaceFolder}/src",
    "LOG_LEVEL": "DEBUG"
  }
}
```

---

## Debugging: Beyond Print Statements

### Setting Up the Debugger

Press `F5` with a Python file open. If no `launch.json` exists, VS Code prompts you to create one. Choose "Python File" for the simplest configuration.

**Essential debugging shortcuts:**

| Action | Shortcut | What It Does |
|---|---|---|
| Start/Continue | `F5` | Begin debugging or resume after a breakpoint |
| Step Over | `F10` | Execute current line, skip into function calls |
| Step Into | `F11` | Step into the function call on current line |
| Step Out | `Shift+F11` | Finish current function, return to caller |
| Stop | `Shift+F5` | Kill the debug session |
| Restart | `Ctrl+Shift+F5` | Stop and re-run from the beginning |
| Toggle Breakpoint | `F9` | Add/remove breakpoint on current line |

### Breakpoints — Beyond the Basics

**Conditional breakpoints:** Right-click the gutter (left margin) → "Add Conditional Breakpoint." Enter a Python expression like `i > 100` or `user.name == "admin"`. The debugger only pauses when the condition is true. This is invaluable when debugging loops — instead of clicking Continue 500 times, break only when the interesting iteration occurs.

**Logpoints:** Right-click the gutter → "Add Logpoint." Enter a message like `Processing item {item_id}, count={len(results)}`. The debugger prints this to the console *without stopping execution*. It's `print()` debugging without modifying your code.

**Hit count breakpoints:** Right-click → "Add Conditional Breakpoint" → change dropdown to "Hit Count." Enter a number like `50`. The debugger stops only on the 50th hit. Useful for "it works for the first 49 records but breaks on the 50th" scenarios.

**Exception breakpoints:** In the BREAKPOINTS panel (bottom of the debug sidebar), check "Raised Exceptions" or "Uncaught Exceptions" to pause whenever an exception occurs, even if it's caught by a try/except block. This lets you inspect the state at the exact moment of failure.

### Advanced launch.json Configurations

```jsonc
{
  "version": "0.2.0",
  "configurations": [
    // Run the currently open file
    {
      "name": "Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },

    // Run a specific entry point with arguments
    {
      "name": "Run Server",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/src/server.py",
      "args": ["--port", "8080", "--debug"],
      "env": { "FLASK_ENV": "development" },
      "console": "integratedTerminal",
      "justMyCode": false  // Step into library code too
    },

    // Run as a module (python -m package.module)
    {
      "name": "Run Module",
      "type": "debugpy",
      "request": "launch",
      "module": "mypackage.cli",
      "args": ["process", "--input", "data.csv"],
      "cwd": "${workspaceFolder}",
      "console": "integratedTerminal"
    },

    // Debug pytest tests
    {
      "name": "Debug Tests",
      "type": "debugpy",
      "request": "launch",
      "module": "pytest",
      "args": ["-xvs", "tests/"],
      "console": "integratedTerminal",
      "justMyCode": false
    },

    // Attach to a running process
    {
      "name": "Attach to Process",
      "type": "debugpy",
      "request": "attach",
      "connect": { "host": "localhost", "port": 5678 }
    },

    // Django
    {
      "name": "Django Server",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver", "0.0.0.0:8000", "--noreload"],
      "django": true,
      "console": "integratedTerminal"
    },

    // FastAPI with uvicorn
    {
      "name": "FastAPI",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": ["app.main:app", "--reload", "--port", "8000"],
      "console": "integratedTerminal",
      "env": { "PYTHONPATH": "${workspaceFolder}" }
    }
  ]
}
```

**Variable substitution reference for launch.json:**

| Variable | Resolves To |
|---|---|
| `${file}` | Currently open file |
| `${workspaceFolder}` | Root of your VS Code workspace |
| `${fileDirname}` | Directory of the current file |
| `${fileBasenameNoExtension}` | Filename without extension |
| `${env:HOME}` | Value of the HOME environment variable |

---

## Testing Integration

### Configuring pytest

VS Code has built-in test discovery. Open Command Palette → **"Python: Configure Tests"** → select **pytest** → choose your test directory (usually `tests/`).

Once configured, the Testing sidebar (flask icon) shows all discovered tests. You can run individual tests, test files, or the entire suite with a single click. Green/red indicators show pass/fail status inline in the editor.

**settings.json for pytest:**

```jsonc
{
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [
    "tests",
    "-v",
    "--tb=short"
  ]
}
```

**Running tests from the terminal:**

```bash
# Run all tests
python -m pytest tests/ -v

# Run a specific file
python -m pytest tests/test_models.py -v

# Run a specific test function
python -m pytest tests/test_models.py::test_prediction_accuracy -v

# Run tests matching a keyword
python -m pytest -k "train" -v

# Stop on first failure
python -m pytest -x

# Show print output
python -m pytest -s

# Run with coverage
python -m pytest --cov=src --cov-report=html tests/
```

### Debugging a Failing Test

Click the debug icon next to any test in the Testing sidebar — VS Code launches the debugger attached to just that test. Set breakpoints in your test file or your source code, and the debugger stops at them. This is far more efficient than adding print statements and re-running.

---

## Terminal Productivity

### Multiple Terminals and Splits

VS Code supports multiple terminal instances. Use the `+` button in the terminal panel to create new ones, or split the current terminal with the split button. Each terminal can use a different shell (bash, PowerShell, zsh) or a different working directory.

**Renaming terminals:** Right-click a terminal tab → "Rename" to give it a descriptive name like "Server", "Tests", or "DB". When you have three or four terminals open, names prevent confusion.

**Terminal profiles in settings.json:**

```jsonc
{
  "terminal.integrated.profiles.linux": {
    "Python REPL": {
      "path": "python3",
      "args": ["-i"]
    },
    "Project Shell": {
      "path": "/bin/bash",
      "args": ["--login"],
      "env": { "VIRTUAL_ENV": "${workspaceFolder}/.venv" }
    }
  }
}
```

### Shell Integration and Command Navigation

VS Code's shell integration (enabled by default in recent versions) adds some powerful features. With it active, you can navigate between command outputs using `Ctrl+Shift+↑` / `Ctrl+Shift+↓` to jump between commands. Failed commands are marked with a red indicator in the gutter. You can also click on file paths in terminal output to open them directly in the editor.

### Auto-Activating Virtual Environments

Add this to your `settings.json`:

```jsonc
{
  "python.terminal.activateEnvironment": true,
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
}
```

Now every new terminal automatically activates your project's virtual environment. You'll see `(.venv)` in the prompt, confirming the right Python is active.

---

## Tasks: Automating Repetitive Commands

### Creating Custom Tasks

Tasks let you bind complex terminal commands to keyboard shortcuts or the Command Palette. Create `.vscode/tasks.json`:

```jsonc
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run current script",
      "type": "shell",
      "command": "python",
      "args": ["${file}"],
      "group": { "kind": "build", "isDefault": true },
      "presentation": { "reveal": "always", "panel": "shared" },
      "problemMatcher": []
    },
    {
      "label": "Run tests with coverage",
      "type": "shell",
      "command": "python",
      "args": ["-m", "pytest", "--cov=src", "--cov-report=term-missing", "tests/"],
      "group": "test",
      "presentation": { "reveal": "always", "panel": "dedicated" },
      "problemMatcher": []
    },
    {
      "label": "Lint with ruff",
      "type": "shell",
      "command": "ruff",
      "args": ["check", "${file}", "--fix"],
      "presentation": { "reveal": "silent" },
      "problemMatcher": {
        "owner": "ruff",
        "fileLocation": ["relative", "${workspaceFolder}"],
        "pattern": {
          "regexp": "^(.+):(\\d+):(\\d+): (\\w+) (.+)$",
          "file": 1, "line": 2, "column": 3, "code": 4, "message": 5
        }
      }
    },
    {
      "label": "Format with black",
      "type": "shell",
      "command": "black",
      "args": ["${file}"],
      "presentation": { "reveal": "silent" },
      "problemMatcher": []
    },
    {
      "label": "Type check with mypy",
      "type": "shell",
      "command": "mypy",
      "args": ["${file}", "--ignore-missing-imports"],
      "problemMatcher": []
    },
    {
      "label": "Install dependencies",
      "type": "shell",
      "command": "pip",
      "args": ["install", "-r", "requirements.txt"],
      "presentation": { "reveal": "always" },
      "problemMatcher": []
    }
  ]
}
```

**Running tasks:** `Ctrl+Shift+B` runs the default build task. `Ctrl+Shift+P` → "Tasks: Run Task" shows all available tasks.

### Compound Tasks (Run Multiple in Sequence)

```jsonc
{
  "label": "Lint + Test",
  "dependsOn": ["Lint with ruff", "Run tests with coverage"],
  "dependsOrder": "sequence",
  "problemMatcher": []
}
```

This runs ruff first, then tests — stopping if ruff fails.

---

## Keyboard-Driven Workflow: The Power User Setup

### Essential Keybindings for Python Development

Add these to your `keybindings.json` (`Ctrl+K Ctrl+S` → click the JSON icon):

```jsonc
[
  // Run current file in terminal
  {
    "key": "ctrl+shift+r",
    "command": "python.execInTerminal"
  },
  // Run selection in terminal
  {
    "key": "shift+enter",
    "command": "python.execSelectionInTerminal",
    "when": "editorTextFocus && editorLangId == 'python'"
  },
  // Toggle between editor and terminal
  {
    "key": "ctrl+`",
    "command": "workbench.action.terminal.toggleTerminal"
  },
  // Clear terminal
  {
    "key": "ctrl+k",
    "command": "workbench.action.terminal.clear",
    "when": "terminalFocus"
  },
  // Run default build task (e.g., your main script)
  {
    "key": "ctrl+shift+b",
    "command": "workbench.action.tasks.build"
  }
]
```

### Rapid Iteration Workflow

The fastest development loop in VS Code:

1. Edit code in the editor
2. Press `Ctrl+Shift+R` to run the file (or `Shift+Enter` for a selection)
3. Check output in the terminal
4. Press `` Ctrl+` `` to jump back to the editor
5. Repeat

For debugging iterations, `F5` starts, `F5` again continues to the next breakpoint, `Shift+F5` stops. No mouse required.

---

## Working Directory and Module Imports

### Understanding the Working Directory

When you run `python script.py` from the terminal, the working directory is wherever your terminal prompt currently points. When you use the Run button, it defaults to the workspace root.

This matters for relative file paths in your code:

```python
# This works if your terminal is in the project root
data = open("data/input.csv")

# This is safer — relative to the script's own location
from pathlib import Path
script_dir = Path(__file__).parent
data = open(script_dir / "data" / "input.csv")
```

You can control the working directory in `launch.json`:

```jsonc
{
  "name": "Run from src/",
  "type": "debugpy",
  "request": "launch",
  "program": "${file}",
  "cwd": "${workspaceFolder}/src"
}
```

### Fixing Import Errors with PYTHONPATH

If your project structure looks like this:

```
myproject/
├── src/
│   ├── models/
│   │   └── classifier.py
│   ├── utils/
│   │   └── helpers.py
│   └── main.py
├── tests/
│   └── test_classifier.py
└── .vscode/
    └── settings.json
```

And `test_classifier.py` does `from src.models.classifier import Model`, Python won't find it unless `myproject/` is on `PYTHONPATH`. Fix this in settings:

```jsonc
// .vscode/settings.json
{
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "${workspaceFolder}"
  },
  "terminal.integrated.env.osx": {
    "PYTHONPATH": "${workspaceFolder}"
  },
  "terminal.integrated.env.windows": {
    "PYTHONPATH": "${workspaceFolder}"
  }
}
```

Or in `launch.json`:

```jsonc
{
  "env": { "PYTHONPATH": "${workspaceFolder}" }
}
```

Or from the terminal:

```bash
# Linux/macOS
export PYTHONPATH=$(pwd)
python tests/test_classifier.py

# Running as a module (often cleaner)
python -m pytest tests/test_classifier.py
```

---

## Running Jupyter Notebooks in VS Code

### Native Notebook Support

VS Code handles `.ipynb` files natively with the Jupyter extension (usually auto-installed with the Python extension). Open any notebook file and you get a full notebook interface with cell execution, markdown rendering, and variable inspection.

**Key notebook shortcuts:**

| Action | Shortcut |
|---|---|
| Run cell | `Ctrl+Enter` |
| Run cell and move to next | `Shift+Enter` |
| Add cell above | `A` (in command mode) |
| Add cell below | `B` (in command mode) |
| Delete cell | `DD` (in command mode) |
| Toggle between edit/command mode | `Escape` / `Enter` |

### Interactive Window (Script + Notebook Hybrid)

Add `# %%` markers in a regular `.py` file to create "cells":

```python
# %%
import pandas as pd
import numpy as np

# %% Load data
df = pd.read_csv("data.csv")
print(df.shape)
print(df.head())

# %% Analysis
summary = df.describe()
print(summary)

# %% Visualization
import matplotlib.pyplot as plt
df['column'].hist()
plt.show()
```

Each `# %%` block gets a "Run Cell" button above it. Clicking it executes that cell in an Interactive Window — giving you notebook-style iterative execution inside a plain Python file. The advantage over `.ipynb` files is that `.py` files have cleaner diffs in version control.

---

## Linting, Formatting, and Code Quality

### Recommended Extension Setup

```jsonc
// settings.json
{
  // Ruff: fast linter + formatter (replaces flake8, isort, and partially black)
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },

  // Type checking with Pylance
  "python.analysis.typeCheckingMode": "basic",  // or "strict"

  // Pylance auto-imports
  "python.analysis.autoImportCompletions": true
}
```

This setup means every time you save a file, Ruff automatically fixes lint issues, organizes imports, and formats the code. Pylance flags type errors with red squiggles as you type.

### Running Quality Checks from Terminal

```bash
# Lint check (no changes)
ruff check .

# Lint and auto-fix
ruff check . --fix

# Format check (no changes)
ruff format --check .

# Format (apply changes)
ruff format .

# Type checking
mypy src/ --ignore-missing-imports

# All three in sequence
ruff check . --fix && ruff format . && mypy src/
```

---

## Remote and Container-Based Execution

### Remote SSH Development

Install the **Remote - SSH** extension. Press `F1` → "Remote-SSH: Connect to Host" → enter `user@hostname`. VS Code opens a new window connected to the remote machine. The integrated terminal runs commands on the remote server, and file editing happens remotely too. Your local machine just renders the UI.

This is particularly useful for running scripts on GPU servers or production-like environments.

### Dev Containers

Install the **Dev Containers** extension. Create `.devcontainer/devcontainer.json`:

```jsonc
{
  "name": "Python 3.12 Dev",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "charliermarsh.ruff"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python"
      }
    }
  }
}
```

Reopen the folder in the container (`F1` → "Dev Containers: Reopen in Container"), and you get a fully isolated, reproducible Python environment. Every team member gets the exact same setup.

---

## Performance and Profiling

### Profiling from the Terminal

```bash
# Basic profiling with cProfile
python -m cProfile -s cumulative script.py

# Save profile data for analysis
python -m cProfile -o profile.prof script.py

# Visualize with snakeviz (install: pip install snakeviz)
snakeviz profile.prof

# Line-level profiling (install: pip install line-profiler)
# Add @profile decorator to functions you want to profile
kernprof -l -v script.py

# Memory profiling (install: pip install memory-profiler)
python -m memory_profiler script.py
```

### Timing Quick Snippets

In the Interactive Window or terminal REPL:

```python
import timeit

# Time a single expression
timeit.timeit('sorted(range(1000, 0, -1))', number=10000)

# Time with setup
timeit.timeit(
    'df.groupby("category").sum()',
    setup='import pandas as pd; df = pd.DataFrame({"category": ["a","b"]*5000, "value": range(10000)})',
    number=100
)
```

---

## Configuration Checklist: The Complete settings.json

Here's a well-tuned `settings.json` for Python development:

```jsonc
{
  // ── Python Core ───────────────────────────────────────────────
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,

  // ── Editor Behavior ───────────────────────────────────────────
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.rulers": [88],
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },

  // ── Analysis ──────────────────────────────────────────────────
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "python.analysis.diagnosticMode": "workspace",

  // ── Testing ───────────────────────────────────────────────────
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests", "-v"],
  "python.testing.unittestEnabled": false,

  // ── Terminal ──────────────────────────────────────────────────
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "${workspaceFolder}"
  },
  "terminal.integrated.env.osx": {
    "PYTHONPATH": "${workspaceFolder}"
  },
  "terminal.integrated.scrollback": 10000,

  // ── Files ─────────────────────────────────────────────────────
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    ".mypy_cache": true,
    ".ruff_cache": true,
    ".pytest_cache": true,
    "*.egg-info": true
  }
}
```

---

## Troubleshooting Common Issues

**"Python was not found" or wrong version runs:**
Check the status bar interpreter. If it shows the wrong version, click it and select the correct one. For terminal commands, run `which python` (Linux/macOS) or `where python` (Windows) to see which binary the shell finds.

**"ModuleNotFoundError" for installed packages:**
Your terminal's active environment doesn't match where you installed the package. Run `pip list` to see what's installed in the current environment. If the package is missing, install it: `pip install package-name`.

**Script runs but can't find files (FileNotFoundError):**
Your working directory is wrong. Add `import os; print(os.getcwd())` at the top of your script to check. Use `pathlib.Path(__file__).parent` for paths relative to the script, or set `"cwd"` in `launch.json`.

**Debugger doesn't stop at breakpoints:**
Make sure `"justMyCode": true` (or `false` if debugging library code) is set in `launch.json`. If using `subprocess` or `multiprocessing`, the child process won't inherit breakpoints unless you attach a debugger to it separately.

**Terminal is using the wrong shell:**
VS Code defaults to your system shell. Change it in settings: `"terminal.integrated.defaultProfile.linux": "bash"` (or `"zsh"`, `"fish"`, etc.).

**Slow IntelliSense / Pylance:**
Large projects can overwhelm analysis. Add bulky directories to `"python.analysis.exclude"`:

```jsonc
{
  "python.analysis.exclude": [
    "**/node_modules",
    "**/data",
    "**/.venv"
  ]
}
```
