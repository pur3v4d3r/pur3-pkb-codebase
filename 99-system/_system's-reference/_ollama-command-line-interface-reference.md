---
title: ⌨️ Ollama Command Line Interface (CLI) Reference
aliases:
  - Ollama CLI
  - ⌨️ OLLAMA COMMAND LINE Interface (CLI) REFERENCE
  - Ollama Commands
  - Ollama Reference
tags:
  - prompt-engineering
  - advanced-prompting/rag
  - advanced-prompting/rag/context-injection
  - advanced-prompting/rag/hybrid-search
  - advanced-prompting/function-calling
  - advanced-prompting/function-calling/tool-definition
  - advanced-prompting/function-calling/orchestration
  - advanced-prompting/programming
  - prompt-workflow
  - prompt-workflow/ideation/use-case
  - prompt-workflow/deployment/production
  - prompt-workflow/deployment/monitoring
  - prompt-workflow/deployment/maintenance
created: 2025-10-06T10:00:17.874Z
updated: 2025-10-06T10:00:41.675Z
date created: 2025-10-06T06:00:17.000-04:00
date modified: 2025-10-09T21:45:47.282-04:00
---
The default server name/address for Ollama is:

### `http://localhost:11434`



# ⌨️ OLLAMA COMMAND LINE Interface (CLI) REFERENCE

> [!the-purpose]
> Here is a comprehensive table of all the essential Ollama Command Line Interface (CLI) commands, categorized by their function. This covers everything from managing your models to controlling the server itself.

---

## **OLLAMA COMMAND LINE Interface (CLI) REFERENCE**

### **CATEGORY 1: CORE MODEL OPERATIONS (GET, RUN, AND INTERACT)**

These are the commands you will use most often to download, launch, and talk to your models.

| Command                   | Purpose                                                                                                                | Example                                                                                | The WHY                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **`ollama run <model>`**  | **The Main Command.** Downloads the specified model (if not local) and starts an interactive chat session immediately. | `ollama run llama3.1:8b`                                                               | The quickest way to start using an LLM. It combines the pull and the execution into one step.   |
| **`ollama pull <model>`** | Downloads a model and saves it to your local machine, **without** starting a chat session.                             | `ollama pull mixtral`                                                                  | Used for pre-loading large models in the background or for scripting.                           |
| **`ollama stop <model>`** | Gracefully shuts down a model that is currently running in the background (using memory/GPU).                          | `ollama stop llama3.1:8b`                                                              | Essential for freeing up your valuable VRAM and system memory when the model is not in use.     |
| **`ollama rm <model>`**   | Permanently deletes a downloaded model from your storage.                                                              | `ollama rm phi3:mini`                                                                  | Used to reclaim hard drive space once you are done experimenting with a model.                  |
| **`ollama list`**         | **or `ollama ls`**                                                                                                     | Lists all models currently stored on your local machine, along with their size and ID. | Helps you keep track of your local model library and identify models to remove.                 |
| **`ollama ps`**           | Lists models that are currently **running** (active and consuming CPU/GPU resources).                                  | `ollama ps`                                                                            | Vital for monitoring resource usage and seeing which models need to be stopped (`ollama stop`). |

### **CATEGORY 2: SERVER AND SYSTEM MANAGEMENT**

These commands control the overarching Ollama server and its configuration.

| Command                | Purpose                                                                                                                               | Example            | The WHY                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------ |
| **`ollama serve`**     | Starts the main Ollama API server (on `http://localhost:11434`), making it accessible to external applications like your web clipper. | `ollama serve`     | This process must be running in the background for your browser tools to work. |
| **`ollama --version`** | Displays the current version of your Ollama installation.                                                                             | `ollama --version` | Useful for troubleshooting and ensuring you have the latest features.          |
| **`ollama --help`**    | Displays a list of all available CLI commands and brief descriptions.                                                                 | `ollama --help`    | The authoritative, real-time reference directly from the executable.           |

### **CATEGORY 3: CUSTOMIZATION AND INSPECTION (ADVANCED)**

These commands are used to create personalized models and inspect model details for deeper understanding.

|Command|Purpose|Example|The WHY|
|---|---|---|---|
|**`ollama show <model>`**|Displays detailed metadata about a model, including the license, parameters (like temperature and context length), and the system prompt.|`ollama show mixtral`|Allows you to inspect the model's "DNA" to understand exactly how it is configured to behave.|
|**`ollama create -f <Modelfile>`**|Creates a new, custom model version based on instructions defined in a text file (the Modelfile).|`ollama create my-assistant -f Modelfile.txt`|This is how you set a permanent system prompt or change parameters like temperature for a personalized LLM.|
|**`ollama cp <src> <dest>`**|Copies an existing local model and gives it a new name.|`ollama cp llama3.1:8b speedy-chat`|Great for creating a backup or a custom working copy before you modify its settings.|
|**`ollama push <model>`**|Uploads a custom-created model to the Ollama registry (requires an account).|`ollama push myusername/new-model`|Used to share your custom-tuned LLMs with the community or other systems.|

### **IN-SESSION COMMANDS (WHEN RUNNING `ollama run`)**

Once you are in the interactive chat session (where you see `>>>`), you can use these special slash commands:

|Command|Purpose|Example|
|---|---|---|
|**`/bye`**|Exits the current interactive chat session (but the model may remain running in the background for a few minutes).|`>>> /bye`|
|**`/?`**|Displays a list of all in-session commands.|`>>> /?`|
|**`/set parameter <name> <value>`**|Temporarily changes a parameter for the model _only in that session_.|`>>> /set parameter temperature 0.9`|
|**`/show info`**|Displays detailed information about the model you are currently using in that session.|`>>> /show info`|

By having this comprehensive list, you are now empowered to perform complex model management and ensure your powerful RTX 4090 system is always running with peak efficiency and customized depth!
