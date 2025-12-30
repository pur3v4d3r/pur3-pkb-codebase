---
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
tags:
  - "#workflow"
llm-model: <% tp.system.suggester(["GPT-4o","Claude 3.5 Sonnet","Gemini 2.5 Pro","Llama 3","Gemini 2.5 Flash","Gemini 2.5 Pro API Key","GPT OSS 120B","Meta Llama 3 405B Instruct","Meta Llama 3 70B Instruct","Meta Llama 3.2 90B Instruct","Meta Llama 3.3 70B Instruct","Meta Llama 4 Scout Instruct","Qwen3 Coder 480B A35B Instruct","Qwen3 235B A22B Instruct","Qwen3 Next 80B A3B Thinking","Qwen3 Next 80B A3B Instruct","DeepSeek V3.1","DeepSeek R1 0528"], [  "GPT-4o",    "Claude 3.5 Sonnet",  "Gemini 2.5 Pro","Llama 3","Gemini 2.5 Flash","Gemini 2.5 Pro API Key","GPT OSS 120B","Meta Llama 3 405B Instruct","Meta Llama 3 70B Instruct","Meta Llama 3.2 90B Instruct","Meta Llama 3.3 70B Instruct","Meta Llama 4 Scout Instruct","Qwen3 Coder 480B A35B Instruct","Qwen3 235B A22B Instruct","Qwen3 Next 80B A3B Thinking","Qwen3 Next 80B A3B Instruct","DeepSeek V3.1","DeepSeek R1 0528"], false, "Select LLM Model:") %>
temperature: <% tp.system.prompt("Enter Model Temperature (e.g., 0.1 for factual, 0.7 for creative):") %>
---

# 📝 Execution Checklist: Deep Prompt Engineering and Curation

>[!note] **SOP Goal**
>To transform a raw generative AI output into a verified, structured, and linkable knowledge artifact ready for permanent assimilation into the PKB.
>
>**Current Artifact Title:** <% tp.file.title %>

## 🚧 1. Dynamic Progress Dashboard (Incomplete Steps)

This Dataview query displays the remaining actions from the SOP checklist below. When a task is checked off, it disappears from this list.

```dataview
TASK
FROM "<% tp.file.path(true) %>"
WHERE !completed
  AND contains(text, "#sop/")
SORT line ASC
LIMIT 100
````




-----

## ✅ 2. Master Task List (The Source of Truth)

### Phase I: Strategic Preparation (Discovery & Intent)

*(The prompt as a schematic blueprint for the desired knowledge artifact.)*

  - [ ] **P1/S1.0 Intent & Context**: Define the specific knowledge artifact being created (e.g., Atomic Note on X). `#sop/p-1-s-1`
  - [ ] **P1/S1.0 Contextualization**: Identify and select existing PKB notes to serve as **contextual grounding data** for the prompt (RAG). `#sop/p-1-s-2`
  - [ ] **P1/S1.1 Role Structuring**: Assign the prompt a detailed **Role** (e.g., specialized scientist) and Tone. `#sop/p-1-s-3`
  - [ ] **P1/S1.1 Constraint Setting**: Define explicit **Constraints** (e.g., word count, reading level, citation requirements). `#sop/p-1-s-4`
  - [ ] **P1/S1.1 Output Schema**: Demand the output in a precise, structured data format (e.g., JSON/YAML/specific Markdown). `#sop/p-1-s-5`

### Phase II: Generative Iteration (Capture & Refinement)

*(Eliciting the best possible response through iterative, strategic communication.)*

  - [ ] **P2/S2.0 CoT Prompting**: Embed mandatory **Chain-of-Thought (CoT)** instructions (e.g., "First, Define... Second, Analyze..."). `#sop/p-2-s-1`
  - [ ] **P2/S2.0 Temperature Check**: Select and register the appropriate **Temperature** setting in the YAML header (e.g., 0.1 for fact). `#sop/p-2-s-2`
  - [ ] **P2/S2.1 Initial Assessment**: Check the first generation for **Accuracy, Relevance, Format, and Completeness**. `#sop/p-2-s-3`
  - [ ] **P2/S2.1 Refinement Cycle**: If deficient, **Refine the *Prompt*** (not the output text) and re-test. `#sop/p-2-s-4`
  - [ ] **P2/S2.1 Complexity Check**: If refinement is excessive, implement **Sequential Prompts** (break into smaller queries). `#sop/p-2-s-5`

### Phase III: Curatorial Validation (Organize & Critique)

*(The non-negotiable human quality gate to ensure epistemic rigor.)*

  - [ ] **P3/S3.0 Factual Verification**: Manually validate all key factual assertions against **trusted external sources**. `#sop/p-3-s-1`
  - [ ] **P3/S3.0 Source Traceability**: Trace and verify the legitimacy and currency of any LLM-cited sources. `#sop/p-3-s-2`
  - [ ] **P3/S3.1 Adversarial Critique**: Generate a second prompt to challenge the output's integrity (e.g., check for bias or counter-arguments). `#sop/p-3-s-3`
  - [ ] **P3/S3.2 Quality Scoring**: Assign a definitive `critique_score` (0-5) in the YAML front matter. `#sop/p-3-s-4`
  - [ ] **P3/S3.2 Meta-Data Registration**: Ensure all tracking parameters (`llm_model`, `temperature`, etc.) are filled in the YAML. `#sop/p-3-s-5`

### Phase IV: Assimilation & Synthesis (Use & Optimize)

*(Structuring the validated output for long-term retention and application.)*

  - [ ] **P4/S4.0 Atomic Decomposition**: Break the validated output into concise, granular **Atomic Notes (Zettels)**. `#sop/p-4-s-1`
  - [ ] **P4/S4.0 Linking**: Link each new note (via bidirectional links) to at least **three** existing relevant concepts. `#sop/p-4-s-2`
  - [ ] **P4/S4.1 Structured Assimilation**: Integrate the new notes into an existing **Map of Content (MOC)**, or create a new MOC. `#sop/p-4-s-3`
  - [ ] **P4/S4.2 Deep Synthesis**: Perform deep synthesis (e.g., Feynman Technique) on the new knowledge. `#sop/p-4-s-4`
  - [ ] **P4/S4.2 Actionable Application**: Extract at least one **verb-first, actionable task** from the content. `#sop/p-4-s-5`
  - [ ] **P4/S4.2 Review Scheduling**: Set the `review_date` property in the YAML front matter for spaced repetition. `#sop/p-4-s-6`

<!-- end list -->