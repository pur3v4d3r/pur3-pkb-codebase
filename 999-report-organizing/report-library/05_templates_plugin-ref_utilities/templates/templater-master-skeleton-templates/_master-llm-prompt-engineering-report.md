<%*
/* ---------------------------------------------------------------
   LLM GENERATION REPORT SKELETON
   Use this for: Saving AI outputs, comparing models, testing prompts
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: AI MODELS ---
// Update this list as you swap models (e.g., new Local LLMs)
const aiModels = [
    "Gemini 1.5 Pro",
    "GPT-4o", 
    "Claude 3.5 Sonnet",
    "Local: Llama-3-8B", 
    "Local: Mistral-Large", 
    "Local: Qwen-2.5-Coder"
];
// --- CONFIGURATION: PROMPT STRATEGIES ---
// Tracks the specific architecture used
const promptStrategies = [
    "Zero-Shot / Direct", 
    "Chain-of-Thought (CoT)", 
    "Tree-of-Thoughts (ToT)", 
    "Role-Based / Persona", 
    "Few-Shot (Examples)", 
    "Iterative Refinement"
];
// --- CONFIGURATION: DOMAINS ---
const domains = [
    "Coding / Scripting", 
    "Prompt Engineering", 
    "Photography / Optics", 
    "Cosmology / Science", 
    "Philosophy / Stoicism", 
    "PKM / Obsidian"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Topic of Generation:");
const selectedModel = await tp.system.suggester(aiModels, aiModels, false, "Select Model Used:");
const selectedStrategy = await tp.system.suggester(promptStrategies, promptStrategies, false, "Prompt Strategy Used:");
const selectedDomain = await tp.system.suggester(domains, domains, false, "Knowledge Domain:");
// --- LOGIC: VERIFICATION STATUS ---
// Default to "Unverified" because LLMs hallucinate
const verificationStatus = "Unverified"; 
_%>
---
type: "ai-generation"
model: "<% selectedModel %>"
strategy: "<% selectedStrategy %>"
domain: "<% selectedDomain %>"
verified: "<% verificationStatus %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
tags:
  - "ai/output"
  - "ai/model/<% selectedModel.replace(/[: ]/g, "-").toLowerCase() %>"
  - "domain/<% selectedDomain.split(" / ")[0].toLowerCase() %>"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily-Note]]"
---

# 🤖 Gen-Report: <% title %>

> [!ai] Generation Metadata
> * **Model**:: [[<% selectedModel %>]]
> * **Strategy**:: <% selectedStrategy %>
> * **Date**:: <% tp.date.now("YYYY-MM-DD") %>
> * **Verdict**:: #status/unverified

---

## 🗣️ The Prompt
> [!note]Input Context
> **System / Persona:**
> (Paste your system instructions or "Gem" reference here)
> 
> **User Prompt:**
> ```text
> (Paste the exact prompt you used here)
> ```

---

## 📝 The Output
*Below is the raw output from the LLM.*

(Paste Output Here)

---

## 🕵️ Analysis & Critique
*Critique the performance. Did it hallucinate? Did it follow the formatting rules?*

* **Accuracy:** (1-10)
* **Adherence to Instructions:** (1-10)
* **Key Insights:**
    * * ## 🔗 Related Prompt Components
*Link to the reusable prompt modules in your Prompt Component Library used to build this:*
- [[Prompt-Component-A]]
- [[Prompt-Component-B]]