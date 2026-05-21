<%*
/* ---------------------------------------------------------------
   ATOMIC PROMPT COMPONENT
   Use this for: Building your "Prompt Component Library"
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: COMPONENT TYPES ---
const componentTypes = [
    "Role / Persona", 
    "Task / Instruction", 
    "Constraint / Guardrail", 
    "Output Format", 
    "Context / Knowledge Base", 
    "Tone / Style"
];
const variableRequirements = [
    "Static (No variables)",
    "Dynamic {{INPUT}}",
    "Dynamic {{CONTEXT}}",
    "Multi-Variable"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Component Name (e.g., CoT-Module-v1):");
const type = await tp.system.suggester(componentTypes, componentTypes, false, "Component Type:");
const vars = await tp.system.suggester(variableRequirements, variableRequirements, false, "Variable Requirement:");
_%>
---
type: "prompt-module"
module-type: "<% type %>"
variables: "<% vars %>"
version: "1.0"
status: "Active"
tags:
  - "prompt-engineering/component"
  - "prompt-engineering/type/<% type.split(" / ")[0].toLowerCase() %>"
created: "<% tp.date.now("YYYY-MM-DD") %>"
---

# 🧩 Component: <% title %>

> [!summary] usage
> **Purpose**:: [Briefly describe what this module achieves]
> **Best Used**:: [e.g., "When reasoning requires step-by-step logic"]

## 📋 The Syntax block
*Copy this block to insert into Master Prompts.*

[PASTE YOUR PROMPT INSTRUCTION HERE]

## ⚙️ Configuration

  * **Required Variables**:
      * `{{Variable_1}}`: Description…
  * **Token Cost Estimate**: \~ [Low/Med/High]

## 🧪 Version History

  * **v1.0** (\<% tp.date.now("YYYY-MM-DD") %\>): Initial commit. %>

## 🔗 Master Prompts Using This

  * [List the Master Instruction Sets that rely on this module]

<!-- end list -->