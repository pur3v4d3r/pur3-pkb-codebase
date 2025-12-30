



```yaml
---
tags: [#vscode #prompt-engineering #llmops #obsidian #productivity #microsoft]
aliases: [Prompty Extension, .prompty file, VS Code Prompty]
status: evergreen
certainty: high
type: reference
freshness:
  domain-volatility: moderate
  last-verified: 2024-05-25
prerequisites:
  hard: [VS Code, basic-yaml, basic-markdown]
  soft: [prompt-engineering-basics, jinja2-templating]
enables:
  direct: [prompt-testing, prompt-versioning, rapid-prototyping]
  related: [llm-evaluation, cognitive-architecture-design]
---
```

> [!comprehensive-reference] 📚 Comprehensive Reference
> - **Generated**:: [[2025-12-24]]
> - **Version**:: 1.0
> - **Exploration Depth**:: 4 (Architectural & Workflow Integration)
> - **Search Count**:: 5
> - **Focus**:: Adaptation for Obsidian/Cognitive Science PKB Workflow

> [!abstract]
> **Executive Overview**
> **Prompty** is a Microsoft-developed asset class and VS Code extension that treats prompts as primary code artifacts. It unifies the **prompt template** (Markdown), **model configuration** (YAML frontmatter), and **logic** (Jinja2) into a single executable file (`.prompty`). For your use case, it effectively turns your Obsidian vault into an executable prompt testing ground, bridging the gap between static knowledge management and dynamic AI application development.

> [!how-to-use-this]
> **Navigation Guide**
> 1. **Anatomy**: Understand the file structure (crucial for your library).
> 2. **Workflow**: How to execute and test within VS Code.
> 3. **The Paradigm Shift**: How this integrates with your specific Obsidian/Claude/Gemini setup.
> 4. **PKB Integration**: How to organize these assets in your vault.

## 📑 Table of Contents
1. [Core Architecture: The .prompty Standard](#core-architecture-the-prompty-standard)
2. [The VS Code Extension Capability](#the-vs-code-extension-capability)
3. [Paradigm Integration: Obsidian + Prompty](#paradigm-integration-obsidian--prompty)
4. [Application to Cognitive Science Project](#application-to-cognitive-science-project)
5. [PKB Integration Strategy](#pkb-integration-strategy)

---

## 🏛️ Core Architecture: The .prompty Standard

Prompty is not just an extension; it is a **file standard** designed to be language-agnostic. It adheres to the "Prompt-as-Code" philosophy.

### The Anatomy of a .prompty File
A `.prompty` file is essentially a Markdown file with extended capabilities. It consists of two distinct parts:

1.  **YAML Frontmatter**: Defines metadata, model parameters, and inputs.
2.  **Markdown Body**: Contains the system/user message templates using Jinja2 syntax.

> [!definition]
> **The .prompty Artifact**
> A single file that encapsulates the *entire* definition of an LLM call, making it versionable, shareable, and executable.

#### Example Schema

```markdown
---
name: CognitiveLoadAnalyzer
description: Analyzes text for cognitive load factors based on Sweller's theory.
authors: [User]
tags: [cognitive-science, analysis]
version: 1.0
model:
  api: chat
  configuration:
    type: azure_openai
    azure_deployment: gpt-4
    api_version: 2023-12-01-preview
  parameters:
    temperature: 0.2
    max_tokens: 1000
inputs:
  text_to_analyze:
    type: string
  audience_level:
    type: string
    default: "novice"
sample:
  text_to_analyze: "The mitochondria is the powerhouse of the cell."
  audience_level: "expert"
---
system:
You are a cognitive scientist specializing in Instructional Design.
Analyze the input for Intrinsic, Extraneous, and Germane load.

user:
Analyze this text for a {{audience_level}} audience:
{{text_to_analyze}}

```

### Key Components

* **[**Model Configuration**:: Defines which model runs the prompt (OpenAI, Azure, generic HTTP endpoints)].^configurable
* **[**Inputs**:: Defines the variables expected by the template (like function arguments)].^schema-enforced
* **[**Sample Data**:: Embedded JSON values that allow you to "Run" the prompt immediately without external code].^rapid-testing
* **[**Template Body**:: Uses standard Markdown + [[Jinja2]] for logic (loops, conditionals)].^flexible

---

## 🛠️ The VS Code Extension Capability

The Prompty extension (bundled with Azure AI tooling or standalone) transforms VS Code into a prompt IDE.

### 1. In-Editor Execution

You do not need to run a Python script to test a prompt.

* **Action**: Click the "Run" button (Play icon) appearing in the `.prompty` file.
* **Result**: The extension interpolates the `sample` data into the Jinja2 template, calls the configured API, and displays the output in a split pane.

### 2. Code Generation

This is critical for your workflow with **Claude Code** and **Gemini Code Assist**.

* **Feature**: Right-click a `.prompty` file -> "Generate Code".
* **Output**: Creates a Python or C# wrapper function that loads the prompt and executes it.
* **Benefit**: You "develop" in Markdown/Prompty, then "compile" to Python code for your application.

### 3. Tracing and Evaluation

* It integrates with **Prompt Flow** to show trace execution (input -> template -> model -> output).
* Allows you to verify variable substitution visually.

> [!warning]
> **Provider Dependency**
> While the format is open, the extension is heavily optimized for Azure OpenAI and standard OpenAI endpoints. Using it with local models (Ollama/LM Studio) usually requires pointing the `api` configuration to a local endpoint (e.g., `base_url: http://localhost:11434/v1`).

---

## 🔄 Paradigm Integration: Obsidian + Prompty

This is where your specific setup becomes powerful. Since you run your Obsidian PKB *through* VS Code, you have a unique advantage.

### The "Unified Vault" Concept

> [!mental-model-anchor]
> **Prompt-Base as Knowledge-Base**
> Treat your Prompty files as "Executable Atomic Notes". They live in your Obsidian vault but are acted upon by VS Code.

#### Implementation Strategy

1. **Storage**: Create a folder in your Obsidian vault called `90-Prompts` or `Library/Prompts`.
2. **File Format**: Save your prompts as `.prompty` files.
* *Obsidian View*: Obsidian will see these as plain text (or Markdown if you associate the extension). You can edit the text, link to them using `[[WikiLinks]]`, and tag them.
* *VS Code View*: When opened in VS Code, they render with the Prompty UI (Run buttons, syntax highlighting).


3. **Cross-Linking**:
* In a concept note (e.g., `[[Cognitive Load Theory]]`), you can link to the implementation: "Implemented in [[CognitiveLoadAnalyzer.prompty]]".
* *Note*: Obsidian might not natively support the `.prompty` extension for clickable links without a plugin, but the file system link works. Alternatively, use `.md` extension but keep the Prompty structure (VS Code might need configuration to treat `.md` with specific frontmatter as Prompty, or you stick to `.prompty` and accept Obsidian treats it as a raw file).
* *Recommendation*: Stick to `.prompty` extension. In Obsidian, use the "File Explorer" to find them, or use a "Text File" plugin to view them.



### Role of Your AI Partners

* **Gemini Code Assist**: Use it to write the *Jinja2 logic* inside the Prompty file. "Gemini, create a loop here that iterates over the history list."
* **Claude Code**: Use it to orchestrate the *integration*. "Claude, write a Python script that loads all `.prompty` files from my `Library/Prompts` folder and runs an evaluation on them."

---

## 🧠 Application to Cognitive Science Project

You are building a "cognitive science backed prompt engineering library". Prompty is the ideal container for this.

### 1. Theory-Driven Templates

You can enforce cognitive patterns in the template structure.

**Example: Chain of Thought (CoT) Template**

```markdown
---
name: CoT_Reasoner
...
---
system:
You are an expert reasoner.
structure:
1. Break down the problem.
2. Verify assumptions.
3. Solve step-by-step.

```

### 2. The "Laboratory" Approach

* **Hypothesis**: "Does adding an emotional stimulus improve reasoning on this task?"
* **Experiment**:
1. Create `Task_Control.prompty`.
2. Create `Task_Emotion.prompty` (identical but with emotional system prompt).
3. Run both in VS Code side-by-side using the same `sample` input.
4. Compare outputs immediately.



### 3. Library Publication

Because `.prompty` files are just text, your "Library" is simply a Git repository of these files. Users of your library can import them and run them immediately if they have the extension.

---

## 📊 PKB Integration & Metadata

How to structure the `.prompty` files to serve as reference notes themselves.

> [!application-context]
> **Metadata Strategy**
> Use the `meta` or `tags` field in the Prompty frontmatter to align with your Obsidian taxonomy.

**Recommended Frontmatter Fields:**

```yaml
---
name: "SocraticTutor"
tags: [education, socratic-method, cognitive-scaffolding]
meta:
  theory_basis: "[[Constructivism]]"
  created_date: "2024-12-24"
  complexity: "Intermediate"
...

```

### Atomic Candidate Extraction

| Concept | Action |
| --- | --- |
| **Prompt Pattern** | Extract the *logic* (Jinja2) into a reusable snippet or base Prompty file. |
| **System Persona** | Create a dedicated `.txt` or `.md` file for the Persona (e.g., `Personas/Socrates.md`) and load it into the Prompty file (Prompty supports file referencing). |
| **Test Case** | Extract complex `sample` data into a separate JSON file (`test_data.json`) and reference it in the Prompty file. |

---

## 🔗 Related Topics for PKB Expansion

* [[Prompt Engineering]]: The discipline defined by these tools.
* [[Jinja2]]: The templating language used for logic within Prompty.
* [[LLMOps]]: The operational lifecycle (Dev -> Test -> Deploy) that Prompty facilitates.
* [[Semantic Kernel]]: Microsoft's SDK that natively consumes Prompty files.
* [[Azure AI Studio]]: The cloud backend that pairs with Prompty for large-scale evals.

```

**Would you like me to generate a template `.prompty` file specifically designed for your "Cognitive Science PKB" that implements a specific technique (like Tree of Thoughts or Self-Consistency) to test in your VS Code setup right now?**

```