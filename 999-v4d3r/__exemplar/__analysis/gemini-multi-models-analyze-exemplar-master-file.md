

MAIN-GOAL:: New Exemplar Material for Prompt Engineering.

PLAN:: 
- Use Gemini's context window to analyze the massive repomix file for the exemplars, and the Prompt Patterns PDF.
- Use Gemini2.5 [vertex-ai-platform] to do the same process to see how much the answer differs.





# Gemini 3.0 Chat 

### Gemini Thinking

**Defining the Analysis Focus**
I'm now fully immersed in understanding the user's core intent. I've pinpointed that the analysis revolves around a specific system prompt and two accompanying files. My immediate focus is to grasp the user's desired outcome from the analysis. I'm carefully examining the prompt and files, searching for clues about the expected depth and scope of the assessment.

**Unveiling the Underlying Strategy**
I'm now zeroing in on the ultimate goal: a complete, production-ready exemplar that elevates an LLM's inference capabilities. The central strategy involves constructing a pattern catalog and synthesizing a high-level overview from the input materials. This will provide a significant boost to LLM reasoning. Specifically, I'm examining a complex system prompt and a relevant research paper to achieve this outcome. The aim is for the output to be a comprehensive demonstration of advanced techniques.

**Analyzing Exemplar Structure**
I'm now diving into the exemplar-prompt-engineering-master.md file, focusing on the described prompt engineering templates. My goal is to extract structural and formatting patterns, especially regarding "Input/Output Examples (Few-Shot)" and "Final Output Formatting." I've updated my execution plan to include fetching this file's full content with File Fetcher alongside the PDF for a comprehensive pattern assessment.

**Identifying Core Prompting Strategies**
I am now thoroughly analyzing the prompt-patterns.pdf to uncover the underlying prompt engineering techniques. I'm focusing on the "Prompt Pattern Catalog" and expect to find techniques like Meta-Language Creation, Output Automater, Persona, and more. This detailed examination aims to identify strategies suitable for an advanced prompt engineering exemplar. I'm aiming to synthesize this into a clear, concise catalog.

**Extracting Key Prompting Elements**
I'm now focusing on specific patterns I expect to find in the exemplar-prompt-engineering-master.md file. I'm looking for Few-Shot input/output pairs, Chain of Thought structures, XML/HTML tagging, role definitions, and task decomposition within the file. Simultaneously, I'm analyzing the user's system prompt, highlighting its hybrid ToT + Reflexion, XML thinking tags, quality gates, composite scoring, role-playing, and constraint-checking components. This is all to build a comprehensive overview.

**Defining Comprehensive Structure**
I've now structured the planned output into three sections. Section 1 will detail a pattern catalog, categorized into architectural, interaction, output, and verification patterns. Section 2 will explain how these patterns synergize, emphasizing the shift towards prompt-as-code principles. The final Section 3 will offer practical implementation guidance. I'm focusing on the multi-phase state machine pattern and hidden thought injection.

**Defining Implementation Strategies**
I am now identifying key patterns within the provided materials, focusing on techniques that enhance LLM reasoning. The "Risk-First Analysis" is a clear example, and I'm developing detailed explanations of how an LLM can utilize patterns like "Persona," using relevant lexicon, and the "REPARATIVE" mnemonic framework from the system prompt. I'm focusing on "ToT" implementation via XML branches as a structural pattern.

**Cataloging the Concepts**
I'm currently working on building a robust catalog of prompt engineering patterns derived from the provided resources, starting with the prompt-patterns.pdf paper and exemplar-prompt-engineering-master. I'm focusing on creating something production-ready, analyzing the files and system prompt to build a comprehensive pattern library. My aim is to make it easily accessible and useful for expert users.

**Developing a Comprehensive Catalog**
I'm now integrating the markdown file's advanced prompt techniques and code examples, alongside the academic patterns from the PDF and the complex system prompt. This gives me a clearer perspective on composite prompt patterns. I'm focusing on structuring the catalog categorically for easy navigation, including high-level overviews for each pattern type to give context. The goal is to produce a readily usable resource.

**Organizing the Patterns**
I've refined my approach to categorize the patterns, creating separate sections for Foundational, Reasoning Architectures, Agentic Frameworks, Meta-Optimization, Quality Assurance/Safety, and Structure/Formatting. I'm excited about the "Academic Report Enhancement Agent" as a demonstration of a Composite Pattern. I am now proceeding to generate the final response, starting with a high-level overview.

**Deep Diving into Patterns**
I'm expanding my analysis to include detailed "how-to" guides for each key pattern, with definitions, use cases, and "prompt-as-code" examples for practical application. I'm excited about deconstructing the "Academic Report Enhancement Agent" as a case study, highlighting the interplay of patterns like the XML state management. Finally, I'm integrating best practices for production implementation, like temperature settings. I want to emphasize the analogy between software design patterns and prompt engineering, to provide a structured, usable, expert-level resource.




### Output

This document analyzes the provided "Academic Report Enhancement Agent v1.0" system prompt alongside the uploaded reference materials (`prompt-patterns.pdf` and `exemplar-prompt-engineering-master.md`). It synthesizes these inputs into a production-ready catalog of reasoning patterns and prompt engineering techniques designed to elevate LLM inference quality.

# 🧠 Production Pattern Catalog & Reasoning Architectures

**Version 1.0 | Status: Production Exemplar**

## 1. High-Level Overview: Prompt Engineering as Software Architecture

The core philosophy extracted from these materials is that high-performance LLM interactions are not "questions" but **software architectures**. The uploaded papers and the "Enhancement Agent" demonstrate a shift from simple instruction to **Prompt-as-Code**, characterized by:

* **Modular Design:** Prompts are broken into functional components (Context, Instruction, Constraint, Output Specification).
* **State Management:** Complex tasks use XML tags or phase definitions to track progress (e.g., `<phase_1>`).
* **Cognitive Architectures:** Reasoning is not linear; it uses tree structures (ToT), graphs (GoT), or loops (Reflexion).
* **Quality Gates:** Explicit validation steps must be passed before generating final output.

## 2. The Master Pattern Catalog

### Category A: Cognitive Architectures (Reasoning)

*Techniques that structure *how* the model thinks, moving beyond linear prediction.*

| Pattern Name | Definition | Best Use Case | Implementation Constraint |
| --- | --- | --- | --- |
| **Tree of Thoughts (ToT)** | Explores multiple reasoning branches, evaluating trade-offs before backtracking or committing. | Complex planning, strategic analysis, or tasks with multiple valid paths. | Requires a "State Evaluator" component to score branches (e.g., "Score: 7.0/10"). |
| **Self-Consistency** | Generates multiple reasoning paths (ensemble) and selects the most frequent/consistent answer. | Math, logic puzzles, or high-stakes fact retrieval. | set `temperature=0.7` for diversity, then vote on the final answer. |
| **Program of Thoughts (PoT)** | Offloads calculation to executable code (Python) rather than natural language prediction. | Mathematical operations, data aggregation, or precise logic. | Model must output code blocks; requires an interpreter sandbox. |
| **Graph of Thoughts (GoT)** | Non-linear reasoning where thoughts can merge, loop, or aggregate (many-to-one). | Comparative analysis, synthesis of conflicting data sources. | High token cost; best for "offline" heavy-duty processing. |
| **Chain of Thought (CoT)** | Forces the model to generate intermediate reasoning steps before the final answer. | Standard logic tasks, word problems. | Use "Let's think step by step" or specific `Reasoning:` headers. |

### Category B: Agentic & Iterative Frameworks

*Patterns that enable the model to act, learn, and improve over time.*

| Pattern Name | Definition | Best Use Case | Implementation Constraint |
| --- | --- | --- | --- |
| **Reflexion** | A loop where the agent critiques its own past failures and stores "reflections" in memory to improve future attempts. | Coding, complex writing, or tasks requiring adaptation. | Requires a "Memory" block to inject past reflections into the context. |
| **ReAct (Reason + Act)** | Interleaves reasoning traces with action execution (Reason -> Act -> Observe -> Reason). | Tasks requiring external tools (Search, Calculator, APIs). | Strict format enforcement: `THOUGHT:`, `ACTION:`, `OBSERVATION:`. |
| **Self-Refine** | Iterative improvement loop: Generate -> Critique -> Refine -> Finalize. | Drafting high-quality content (essays, reports) to remove hallucinations. | Define explicit "Pass Thresholds" (e.g., "Must score > 8/10"). |
| **Chain of Verification (CoVe)** | Generates a baseline response, drafts verification questions to fact-check it, then revises. | Reducing hallucinations in factual queries. | Split into distinct steps: 1. Draft, 2. Verify, 3. Rewrite. |

### Category C: Structural & Format Patterns

*Software design patterns adapted for text generation (from White et al. paper).*

| Pattern Name | Definition | Example Trigger |
| --- | --- | --- |
| **Persona Pattern** | Adopts a specific role to constrain search space and adopt domain lexicon. | "Act as a [Role]..." / "You are [System Identity]..." |
| **Meta-Language Creation** | Defines a custom notation or shorthand for the interaction. | "When I say 'X', it means [Complex State]..." |
| **Output Automater** | Enforces a machine-readable format for downstream code execution. | "Output ONLY valid JSON..." / "Wrap code in <script> tags." |
| **Template Pattern** | Provides a rigid skeleton the model must fill in. | "Use this format: Section 1: [Content]..." |
| **Cognitive Verifier** | Forces the model to ask clarifying questions before answering. | "When you need more info, ask me questions until you can answer." |
| **Flipped Interaction** | The model asks the user questions to drive the goal. | "I will ask you questions to deploy X. You answer." |

---

## 3. Case Study: The "Enhancement Agent" Architecture

*Deconstructing the User's System Prompt to reveal production-grade implementation.*

The provided "Academic Report Enhancement Agent" is a **Composite Pattern** utilizing a Hybrid ToT + Reflexion architecture. Here are the specific mechanisms it uses that an LLM can replicate:

### 3.1. XML State Management

Instead of vague instructions, the prompt uses XML tags to enforce a **State Machine**.

* **Pattern:** ` <phase_1> ... </phase_1>`
* **Reasoning:** This creates "sandboxed" environments for the model. It cannot "leak" into Phase 2 until Phase 1 is validated.

### 3.2. Hidden "Extended Thinking"

The prompt explicitly separates internal processing from user delivery.

* **Pattern:** `(Execute in Extended Thinking)` or `OUTPUT OF PHASE 1 (in extended thinking only)`
* **Reasoning:** Prevents the user from seeing the "messy" brainstorming (ToT branches) while ensuring the final output is polished.

### 3.3. Algorithm-in-Prompt

The prompt includes pseudo-code logic for decision making.

* **Pattern:**
```text
IF composite >= 7.0 → EXPLORE
IF composite < 5.0 → PRUNE

```


* **Reasoning:** Forces the model to simulate a logic engine, reducing the "fuzzy" decision-making typical of LLMs.

### 3.4. The Mnemonic Framework (REPARATIVE)

It defines a specific acronym for quality control.

* **Pattern:** **R**igor, **E**vidence, **P**recision, **A**rchitecture...
* **Reasoning:** Anchoring complex evaluation criteria to a mnemonic helps the model recall and apply *all* constraints without dropping context.

---

## 4. Production Implementation Guide

To implement these patterns effectively during inference:

### Step 1: Define the Cognitive Architecture

Do not just ask for an answer. Define *how* the model should reach it.

* *Bad:* "Improve this report."
* *Good:* "Execute a Tree of Thoughts exploration to identify weak arguments, then use Self-Consistency to validate improvements."

### Step 2: Enforce XML Structuring

Use XML tags to separate specific types of reasoning. This helps parsers (and the model itself) distinguish between "meta-reasoning" and "content."

```xml
<thinking>
   <branch_1>...</branch_1>
   <evaluation>Score: 4/10</evaluation>
</thinking>
<response>
   ...
</response>

```

### Step 3: Implement Quality Gates

Never allow the model to stream the final answer immediately. Force a stop-sequence or an internal evaluation step.

* **Technique:** **Refusal Breaker / Constraint Check**.
* *Prompt:* "You CANNOT proceed to Phase 6 until ALL dimensions pass their thresholds."

### Step 4: Use Few-Shot Formatting (Input/Output Examples)

As seen in `exemplar-prompt-engineering-master.md`, providing concrete examples of the *structure* (not just content) dramatically improves adherence.

```markdown
Input: [Example Input]
Ideal Output:
<analysis>
  ...
</analysis>

```

## 5. Summary of Extracted "Prompt-as-Code" Techniques

1. **Tie-Breaker Heuristics:** Explicitly tell the model how to resolve conflicts (e.g., "Weight Impact 0.4, Risk 0.3").
2. **Visualization Generator:** Ask the model to generate text-based visualizations (Mermaid.js, ASCII) to verify its structural understanding.
3. **Risk-First Analysis:** A specific reasoning path that asks "What could go wrong?" to counterbalance optimism bias.
4. **Meta-Commentary:** Instruct the model to provide a summary of *what* it changed and *why*, distinct from the content itself.




















































































# Gemini 2.5 Pro on Vertex AI
[Prompt:: Exemplar Generator Agent]
[Model:: Gemini-2.5-Pro]
[Google Search Grounding:: TRUE]
[Temperature:: 0.8]
[Output Token Limit:: 65535]
[Seed:: FALSE]
[Top-P:: 0.95]














### Gemini Thinking


**Constructing a Master Exemplar**
My initial focus is on deconstructing the request. I've broken down the core task, which involves extracting information on prompt engineering from the document dump. The primary goal is to produce a "Chain of Thought Master Exemplar," which will guide the analysis. This work will continue to involve synthesis.

**Refining Extraction Protocols**
I'm now prioritizing the extraction of critical elements. Specifically, I'm focusing on "How It Works," "When to Use," and "Implementation Templates" for Chain of Thought. My analysis of the 01-reasoning-techniques-guide.md file reveals promising details. I'm building a concise framework that'll be easily adaptable.

**Formulating the Analytical Framework**
Now I'm delving deeper, mapping out my approach to generate the Chain of Thought Exemplar. My plan involves a two-pronged attack: first, a high-level overview from 00-advanced-prompt-engineering -index.md, and second, a detailed dissection of CoT from 01-reasoning-techniques-guide.md. I am also examining the files that provide specific techniques.

**Planning the Synthesis Strategy**
I'm now devising the method for crafting the "Chain of Thought Master Exemplar." First, I'll dissect the request, understanding the goal and the implicit constraints. Then, I'll perform a detailed file categorization, creating a mental model to understand how everything relates. This involves careful examination of various documents and their roles.

**Structuring the Master Guide**
I'm now prioritizing the structure of my exemplar. I'll include a "Definition" section, drawing information from multiple sources, and followed by a "When to Use" section, informed by decision trees and performance data. The core will be a "Core Implementation Patterns" section with zero and few shot examples and a contrastive CoT example.

**Categorizing and Planning Output**
I'm now deep in the file categorization phase, and building a conceptual model of how the documents relate. The index file will be the skeleton, the techniques guide the meat, and the exemplar files will show the ideal structure. I have planned a structure for my output to include templates.

**Prioritizing the Synthesis Plan**
My immediate plan involves refining my structure for the exemplar. I will use Markdown, and divide it into clear sections. I will concentrate on the "Definition", "When to Use", and "Implementation Patterns" sections as high priorities for now.

**Planning Extraction & Synthesis**
I'm now diving deep into the file categorization phase. I'm focusing on the index file as the structural guide, the reasoning techniques guide for CoT specifics, and exemplar files to model the output. I'm prioritizing the integration of all templates into the exemplar's structure.

**Refining Extraction Protocols**
I'm now prioritizing the extraction of crucial elements for the 'Definition' section, drawing heavily from the '01-reasoning-techniques-guide.md' file. After that I'll move on to 'When to Use' and create the 'Implementation Templates' as soon as I can to keep a strong, consistent structure.










### Output

### Summary of Chain of Thought (CoT) Prompting

Based on a comprehensive review of the provided documents, Chain of Thought (CoT) prompting is a powerful and essential technique for enhancing the reasoning capabilities of Large Language Models (LLMs). Instead of generating an answer directly, CoT guides the model to produce a series of intermediate, logical steps that lead to the final conclusion, similar to how a human would work through a complex problem. This method significantly improves performance on tasks requiring arithmetic, commonsense, and symbolic reasoning. The transparency of the reasoning process also aids in debugging and building trust in the model's outputs.

The technique is considered an emergent ability of LLMs, becoming more effective as model size and complexity increase. However, instruction tuning has enabled even smaller models to leverage CoT.

### Core CoT Implementation Patterns

Several distinct patterns for implementing CoT have been identified, each with specific use cases and templates.

#### 1. Zero-Shot CoT
This is the simplest form of CoT, where the model is prompted to reason step-by-step without being given explicit examples. It is highly effective for general reasoning tasks where the model needs to be encouraged to "think aloud."

*   **Trigger Phrase**: The technique is activated by adding a simple instruction like "Let's think step by step." to the prompt. Other effective phrases include "Let's work this out in a step-by-step way to be sure we have the right answer" and "First, let's think about this logically."
*   **When to Use**: It is best used for multi-step or logical problems where the model might otherwise jump to a conclusion. It should be the first approach before moving to more complex methods.
*   **Template**:
    ```
    Question: {question}

    Answer: Let's think step by step.
    ```

#### 2. Few-Shot CoT
This pattern provides the model with one or more complete examples of a question, a step-by-step reasoning chain, and the final answer. The model then uses this demonstrated pattern to solve a new problem. Few-Shot CoT generally outperforms Zero-Shot CoT, especially for complex tasks, as it gives the model a clear template to follow.

*   **When to Use**: This is ideal for complex or novel tasks where the desired reasoning structure is specific and needs to be demonstrated.
*   **Template**:
    ```
    Question: {Example Question 1}
    Answer: {Step-by-step reasoning for Example 1} The final answer is {Answer 1}.

    Question: {Example Question 2}
    Answer: {Step-by-step reasoning for Example 2} The final answer is {Answer 2}.

    Question: {New Question}
    Answer:
    ```

#### 3. Plan-and-Solve (PS) Prompting
This is a two-stage technique where the model is first instructed to devise a plan to solve the problem and then execute that plan. This explicit separation of planning and execution leads to more robust reasoning.

*   **Structure**:
    1.  **Plan**: Understand the problem, extract variables, and outline the solution steps.
    2.  **Solve**: Carry out the plan, calculating intermediate variables and showing the work.
*   **Template**:
    ```
    Let’s first understand the problem, extract relevant variables..., and make a complete plan. Then, let’s carry out the plan...

    Question: {question}
    Answer:
    Plan:
    1. [Step 1]
    2. [Step 2]
    ...
    Execution:
    1. [Execution of Step 1]
    2. [Execution of Step 2]
    ...
    Final Answer: {answer}
    ```

#### 4. Tabular CoT
This technique structures the model's reasoning process into a table, forcing a highly organized, step-by-step analysis. It is particularly effective for problems that can be broken down into discrete sub-questions.

*   **Structure**: The reasoning is organized into columns like `|step|subquestion|process|result|`.
*   **Template**:
    ```
    You are a reasoning assistant that uses Tabular Chain-of-Thought (Tab-CoT). You must generate your reasoning in a table format...

    Question: {question}
    Answer:
    |step|subquestion|process|result|
    |---|---|---|---|
    |1|...|...|...|
    |2|...|...|...|
    ```

### Advanced CoT Variations and Integrations

The provided documents detail several advanced techniques that either build upon or integrate with CoT to further enhance performance.

*   **Self-Consistency**: This is a powerful ensemble method where multiple CoT reasoning paths are generated (using a higher `temperature` setting), and the final answer is determined by a majority vote. This significantly improves reliability, especially for mathematical tasks.
*   **Chain of Verification (CoVe)**: A technique to reduce hallucinations. The model first generates a CoT response, then creates verification questions to check its own claims, answers those questions independently, and finally produces a corrected answer.
*   **Tree of Thoughts (ToT)**: Extends CoT by exploring multiple reasoning paths simultaneously in a tree structure. It evaluates the promise of each intermediate "thought" and can backtrack, allowing for more deliberate problem-solving.
*   **ReAct (Reason and Act)**: This framework integrates CoT with tool use. The "Thought" part of the `Thought-Action-Observation` loop is a chain of thought that informs which action (tool) to take next.
*   **Thread of Thought (ThoT)**: This is particularly useful for tasks with long or cluttered contexts, such as Retrieval-Augmented Generation (RAG). The model is prompted to "walk through the context in manageable parts step by step, summarizing and analyzing as we go."

### Best Practices and Pitfalls

*   **When to Use CoT**: Use for complex problems requiring multi-step logic. Avoid it for simple factual recall where it adds unnecessary overhead.
*   **Clarity is Key**: Prompts should be clear and concise. Complex problems benefit from breaking them down into smaller, logical steps.
*   **Experimentation**: The effectiveness of different CoT variations can depend on the model and the specific task. It is crucial to experiment and iterate on prompts.
*   **Common Issues**:
    *   **Skipping Steps**: The model may give a short answer without detailed reasoning. This can be mitigated by explicitly instructing it to explain each step or by breaking the prompt into sub-questions.
    *   **Error Propagation**: An error in an early step can lead to an incorrect final answer. Self-Consistency and CoVe are effective mitigation strategies.
*   









































































































# Gemini 3.0 Pro Preview on Vertex AI
[Prompt:: Exemplar Generator Agent]
[Model:: Gemini-3.0-Pro]
[Google Search Grounding:: TRUE]
[Temperature:: 0.8]
[Output Token Limit:: 65535]
[Seed:: FALSE]
[Top-P:: 0.95]



### Starter Prompt Used

````prompt
Review this exemplar document VERY CLOSELY and extract information we can use to build a Chain of Thought Master Exemplar for use during inference time.
MAIN GOAL: Production ready exempla(s) to be implemented as soon as possible to increase reasoning ability and overall quality of output produced during sessions.
````

### Gemini Thinking

**Examining the Core Goal**
I'm now zeroing in on the ultimate objective: crafting a Chain of Thought Master Exemplar. My focus is entirely on the desired output, the very thing I'm building, and the ways I will ultimately use it. I'm taking the prompt as the blueprint, and the templates as the tools to realize this goal.

**Dissecting Source Material**
I'm now carefully reviewing the source document, pinpointing the critical elements of each prompt engineering technique. I'm taking notes on what's effective, and mapping out the best way to extract the crucial components from each guide. It appears 'integration patterns' are key; identifying the optimal combinations will be essential.

**Constructing the Meta-Cognitive Prompt**
The current focus is on building the "Meta-Cognitive" system prompt. I've broken it into roles, protocols, technique selectors, and execution phases. The technique selector will be the key, dynamically choosing the optimal reasoning strategy based on task complexity. I am carefully writing the instructions for assessing the user query and selecting the appropriate chain-of-thought technique.

**Constructing the "Menu"**
I'm now focusing on the "Technique Selector," crafting the "menu" of reasoning approaches. This involves precisely defining CoT, ToT, CoVe, Reflexion, and Analogical prompting, ensuring the model can accurately distinguish between them. I'm taking the source docs and distilling the essential triggers and output formats for each technique to optimize the master exemplar.

**Formulating the XML Structure**
Now I'm designing the XML-based prompt structure, using HTML-like tags for clarity and compatibility with modern LLM optimizations. Key sections will be included for the model's role, the meta-cognitive protocol, the technique selector, and the execution protocol. The thinking section is particularly important, as is the use of different tags to clearly differentiate parts of the prompt.

**Formulating the XML Blueprint**
I'm now in the process of formulating a structured XML blueprint, inspired by the YAML schema and HTML-like templates. I am going to use an HTML-like XML structure to define the prompt, using tags for the model's role, meta-cognitive protocol, and execution sections. The goal is clarity and compatibility with current LLM optimizations.







### Output

Based on a close review of the provided codebase—specifically the `00-advanced-prompt-engineering-index.md`, `master-yaml-techniques-exemplar.md`, and the various technique guides (ToT, CoT, CoVe)—I have constructed a **Master Chain of Thought Exemplar**.

This is designed to be a **System Prompt** or **Meta-Prompt** that you can inject into your inference pipeline. It dynamically selects the best reasoning framework (Tree of Thoughts, Chain of Verification, etc.) based on the complexity of the user's request.

### 🧠 The Reasoning Engine Master Exemplar

**Usage:** Paste this into your System Instruction or prepended to the user message.

```xml
<system_identity>
  You are an Advanced Reasoning Engine designed to solve complex problems by dynamically selecting and applying state-of-the-art prompt engineering frameworks. You do not just answer; you architect a solution path using the most appropriate cognitive strategy.
</system_identity>

<cognitive_protocol>
  Upon receiving a user query, you must execute the following "Meta-Cognition" phase before generating the final response. This phase happens inside <thinking> tags.

  PHASE 1: CLASSIFICATION & STRATEGY SELECTION
  1. Analyze the user's request complexity and type.
  2. Select the optimal reasoning framework from the "Reasoning Library" below.
  3. Justify the selection.

  PHASE 2: EXECUTION (Internal Monologue)
  Execute the selected framework step-by-step.
  - If "Chain of Thought": Break down into linear steps.
  - If "Tree of Thoughts": Generate 3 branches, evaluate, prune, and backtrack if needed.
  - If "Chain of Verification": Draft -> Generate Verification Questions -> Answer Independently -> Revise.
  - If "Program of Thoughts": Write pseudo-code/Python to solve logic/math.
  - If "Reflexion": Draft -> Critique -> Refine.

  PHASE 3: SYNTHESIS
  Present the final output clearly, stripping away the internal scaffolding unless the user asked to see the reasoning.
</cognitive_protocol>

<reasoning_library>
  <strategy name="Tree of Thoughts (ToT)">
    <trigger>Complex planning, creative writing, strategic decision making, or problems with multiple valid paths.</trigger>
    <method>
      1. Decompose problem into intermediate steps (thoughts).
      2. Generate multiple candidate thoughts for the next step.
      3. Evaluate each candidate (Sure/Likely/Impossible).
      4. Select best path (BFS/DFS) and backtrack if a dead end is hit.
    </method>
  </strategy>

  <strategy name="Chain of Verification (CoVe)">
    <trigger>Factual queries, biographies, list generation, or high-stakes information retrieval where hallucination is a risk.</trigger>
    <method>
      1. Generate Baseline Response.
      2. Plan Verification Questions (to check facts in baseline).
      3. Execute Verifications (answer questions independently of baseline).
      4. Generate Final Verified Response (correcting errors).
    </method>
  </strategy>

  <strategy name="Program of Thoughts (PoT)">
    <trigger>Mathematical word problems, logic puzzles, date calculations, or algorithmic tasks.</trigger>
    <method>
      1. Define variables.
      2. Express reasoning as executable logic/code steps.
      3. Calculate deterministic result.
    </method>
  </strategy>

  <strategy name="Rephrase and Respond (RaR)">
    <trigger>Ambiguous, vague, or short user queries.</trigger>
    <method>
      1. Rephrase the user's question to be more specific and explicit.
      2. Expand intent and constraints.
      3. Answer the rephrased question.
    </method>
  </strategy>

  <strategy name="Standard Chain of Thought (CoT)">
    <trigger>General reasoning, linear problem solving, explanations.</trigger>
    <method>
      1. Break problem into logical sub-steps.
      2. Solve sequentially.
    </method>
  </strategy>
</reasoning_library>

<output_format>
  1. Begin with <thinking> tags to show your Meta-Cognition and Strategy Selection.
  2. Inside <thinking>, show the execution of the selected framework (e.g., the Tree of Thoughts branches or Verification Questions).
  3. Close </thinking>.
  4. Provide the final, polished response to the user.
</output_format>
```

---

### 📝 Implementation Guide (How to use this)

Based on the `integration-patterns-guide.md` found in your codebase, here is how you should implement this for maximum effect:

#### 1. The "Meta-Cognitive" Handshake
When the session starts, the LLM will now pause to classify the problem.
*   **User Input:** "Create a marketing plan for a new coffee brand."
*   **Model Response (Internal):** *Recognizes this requires exploration and planning. Activates **Tree of Thoughts**.*
*   **User Input:** "Who was the president when the first iPhone released?"
*   **Model Response (Internal):** *Recognizes this is a factual claim prone to hallucination. Activates **Chain of Verification**.*

#### 2. Optimization for Specific Agents
If you are building specific agents (as referenced in `exemplar-multiple-research-agents.md`), you can hardcode the strategy in the `<cognitive_protocol>` section:

*   **For a Math Agent:** Force `Program of Thoughts`.
*   **For a Research Agent:** Force `Chain of Verification`.
*   **For a Creative Writing Agent:** Force `Tree of Thoughts`.

#### 3. Key Components Extracted from Your Codebase
*   **Axiom of Explicitness:** (From `master-yaml-techniques-exemplar.md`) The prompt explicitly tells the model *how* to think, rather than just asking it to be smart.
*   **Reasoning Library:** Aggregated from `01-reasoning-techniques-guide.md` and `Advanced_Prompt_Engineering_Techniques` folder.
*   **XML Structure:** Adopted from the `claude` specific optimization strategies found in `master-yaml-techniques-exemplar.md` (Section 9.1).

### Example Output using this Exemplar

**User:** "Solve this: 24 game using inputs 4, 9, 10, 13."

**Model Output:**
```xml
<thinking>
PHASE 1: SELECTION
Strategy: Tree of Thoughts (ToT)
Reason: The Game of 24 is a combinatorial search problem with dead ends. Standard CoT often fails here.

PHASE 2: EXECUTION
Input: [4, 9, 10, 13]
Goal: 24

Branch 1:
13 - 10 = 3
Left: [4, 9, 3]
9 - 3 = 6
Left: [4, 6]
4 * 6 = 24
Evaluation: Solved.

Branch 2:
10 - 4 = 6
Left: [9, 13, 6]
13 + 9 = 22
Left: [22, 6] -> Impossible.

Selected Path: Branch 1.
</thinking>

The solution is: (9 - (13 - 10)) * 4 = 24
```

----


### Prompt Used

```prompt
Now generate examples for each of the different reasoning paths the model can take from the "Reasoning Engine Master Exemplar". Be sure to include working code the models can use, in addition to the natural language examples.
```

### Gemini Thinking

**Seeking Exemplification Paths**
I'm now generating examples for each reasoning path. I've begun with the Tree of Thoughts and Chain of Verification, focusing on diverse problem types to illustrate their strengths. My aim is to clearly demonstrate how each path can be applied to varied scenarios, from abstract problem-solving to practical application, like the Program of Thoughts reasoning path.

**Defining Example Structures**
I'm structuring the examples now, considering the best format to represent the internal monologues. I'm focusing on the "Tree of Thoughts," "Chain of Verification," "Program of Thoughts," "Rephrase and Respond," and "Standard Chain of Thought" reasoning paths, as they were defined earlier. The goal is to provide clear, natural language demonstrations for each.


### Output

Here are detailed examples for each reasoning path defined in the Master Exemplar. These demonstrate how the model should behave internally (inside `<thinking>` tags) and what code it might generate or execute.

---

### 1. Tree of Thoughts (ToT) Example
**Trigger:** Complex planning, creative writing, or strategic decision-making.
**Scenario:** A user asks for a 3-course dinner menu for a mixed group (Vegans and Keto dieters) that feels cohesive.

```xml
<thinking>
PHASE 1: SELECTION
Strategy: Tree of Thoughts (ToT)
Reason: The request has conflicting constraints (Vegan vs. Keto) and requires thematic cohesion. A single linear path might get stuck on a dish that satisfies one group but not the other.

PHASE 2: EXECUTION

**Root Node:** 3-Course Menu (Vegan + Keto friendly)

**Branch 1 (Theme: Mediterranean)**
- Starter: Hummus with veggie sticks (Vegan/Keto ok).
- Main: Grilled Eggplant for Vegans / Grilled Fish for Keto. *Critique: Two different mains breaks cohesion.*
- Dessert: Fruit salad. *Critique: Fruit often too high carb for strict Keto.*
- Evaluation: ❌ Weak cohesion.

**Branch 2 (Theme: Asian Fusion)**
- Starter: Miso Soup with Tofu. *Critique: Soy often avoided in strict Keto, but manageable.*
- Main: Zucchini Noodle Stir-fry.
  - Topping A: Edamame (Vegan).
  - Topping B: Chicken (Keto).
  - Base Sauce: Sesame oil/Soy (works for both).
- Dessert: Coconut Milk Chia Pudding with almond slivers.
  - Vegan: Yes (Coconut milk).
  - Keto: Yes (High fat, low carb, use stevia).
- Evaluation: ✅ Strong cohesion, shared base components.

**Branch 3 (Theme: Mexican)**
- Starter: Guacamole with cucumber slices. (Works).
- Main: Taco Bar.
  - Shells: Lettuce wraps (Keto/Vegan).
  - Fillings: Spiced Walnuts (Vegan) vs Beef (Keto).
- Dessert: Avocado Chocolate Mousse.
  - Vegan: Yes.
  - Keto: Yes (Avocado is fat source).
- Evaluation: ✅ Very strong, but maybe "Taco Bar" feels less formal than a 3-course request.

**Selection:** Branch 2 (Asian Fusion) offers the most "plated dinner" feel while satisfying constraints.

</thinking>

Here is a cohesive Asian Fusion menu designed to satisfy both Vegan and Keto guests seamlessly:

**1. Starter:** Miso & Tofu Broth with Scallions
**2. Main:** Sesame Zucchini Noodle Stir-fry (Served with Edamame for Vegans, Grilled Chicken for Keto)
**3. Dessert:** Coconut Chia Seed Pudding with Toasted Almonds
```

---

### 2. Chain of Verification (CoVe) Example
**Trigger:** High-stakes factual queries or list generation.
**Scenario:** A user asks, "List 3 movies where Tom Hanks and Meg Ryan starred together."

```xml
<thinking>
PHASE 1: SELECTION
Strategy: Chain of Verification (CoVe)
Reason: Specific factual association query. Hallucination risk is moderate (mixing up rom-com actors).

PHASE 2: EXECUTION

**Step 1: Baseline Generation**
1. Sleepless in Seattle
2. You've Got Mail
3. Catch Me If You Can

**Step 2: Verification Questions**
- Q1: Did Tom Hanks and Meg Ryan start in "Sleepless in Seattle"?
- Q2: Did Tom Hanks and Meg Ryan start in "You've Got Mail"?
- Q3: Did Tom Hanks and Meg Ryan start in "Catch Me If You Can"?
- Q4: Are there other movies they starred in together?

**Step 3: Execution of Verification**
- A1: Yes, they are the leads.
- A2: Yes, they are the leads.
- A3: Checking cast... Tom Hanks is in it. Leonardo DiCaprio is in it. Meg Ryan is NOT in it. -> *Error Detected.*
- A4: Checking collaboration list... "Joe Versus the Volcano" (1990) and "Ithaca" (2015).

**Step 4: Final Correction**
Replace "Catch Me If You Can" with "Joe Versus the Volcano".

</thinking>

Tom Hanks and Meg Ryan have starred together in the following movies:
1. **Joe Versus the Volcano** (1990)
2. **Sleepless in Seattle** (1993)
3. **You've Got Mail** (1998)
*(They also reunited for "Ithaca" in 2015).*
```

---

### 3. Program of Thoughts (PoT) Example
**Trigger:** Math word problems or logic puzzles.
**Scenario:** "I have a $500 budget. I need to buy 5 widgets at $45 each and 3 gadgets at $80 each. Sales tax is 8%. Do I have enough?"

```xml
<thinking>
PHASE 1: SELECTION
Strategy: Program of Thoughts (PoT)
Reason: Arithmetic calculation with tax logic. LLMs often make small math errors in plain text. Python code is safer.

PHASE 2: EXECUTION
Writing Python code to solve...

```python
def check_budget():
    budget = 500
    
    # Item costs
    widget_price = 45
    widget_count = 5
    gadget_price = 80
    gadget_count = 3
    
    # Subtotal
    subtotal = (widget_price * widget_count) + (gadget_price * gadget_count)
    
    # Tax
    tax_rate = 0.08
    tax_amount = subtotal * tax_rate
    
    # Total
    total_cost = subtotal + tax_amount
    
    remaining = budget - total_cost
    is_enough = remaining >= 0
    
    return {
        "subtotal": subtotal,
        "tax": tax_amount,
        "total": total_cost,
        "remaining": remaining,
        "enough": is_enough
    }

result = check_budget()
print(result)
```

**Output Simulation:**
{'subtotal': 465, 'tax': 37.2, 'total': 502.2, 'remaining': -2.2, 'enough': False}

</thinking>

No, you do not have enough money.

**Breakdown:**
*   **Subtotal:** $465.00
*   **Tax (8%):** $37.20
*   **Total Cost:** $502.20

You are over budget by **$2.20**.
```

---

### 4. Rephrase and Respond (RaR) Example
**Trigger:** Vague or ambiguous prompts.
**Scenario:** User types just: "How do I fix the internet?"

```xml
<thinking>
PHASE 1: SELECTION
Strategy: Rephrase and Respond (RaR)
Reason: The user input is extremely vague. It could mean fixing a local WiFi connection, or fixing systemic issues with the World Wide Web (privacy, centralization).

PHASE 2: EXECUTION

**Original Query:** "How do I fix the internet?"

**Interpretation A (Technical/Local):** "How do I troubleshoot my internet connection when it is slow or down?"
**Interpretation B (Societal/Global):** "How can we solve the systemic problems of the modern internet like misinformation or privacy loss?"

**Selected Rephrasing:** Since the user likely faces a connection issue (most common intent), I will answer Interpretation A primary, but acknowledge B.

**Rephrased Question:** "What are the steps to troubleshoot a non-working home internet connection?"

</thinking>

It sounds like you might be having trouble with your connection. Here is how to **troubleshoot your home internet** (Interpretation A):

1.  **Restart your Modem/Router:** Unplug it for 30 seconds and plug it back in.
2.  **Check your Device:** Toggle WiFi off and on again.
3.  **Check for Outages:** Look at your ISP's status page on your phone.

*(If you meant "fixing the internet" in a societal sense—like privacy or centralization—please let me know, and we can discuss protocols like decentralized web or privacy legislation!)*
```

---

### 5. Standard Chain of Thought (CoT) Example
**Trigger:** General explanations or linear reasoning.
**Scenario:** "Why does the sky turn red at sunset?"

```xml
<thinking>
PHASE 1: SELECTION
Strategy: Standard Chain of Thought (CoT)
Reason: This is a scientific explanation that follows a linear causal chain (physics of light -> atmosphere -> visual result).

PHASE 2: EXECUTION

1.  **Concept:** Rayleigh Scattering. Sunlight contains all colors. Blue light scatters the most because of short waves.
2.  **Midday:** Sun is overhead. Path through atmosphere is short. We see the scattered blue light.
3.  **Sunset:** Sun is at the horizon. The path sunlight travels through the atmosphere is much longer.
4.  **Filtering:** Because the path is long, most of the blue light is scattered completely away before reaching our eyes.
5.  **Result:** The remaining wavelengths are the longer ones (Reds, Oranges, Yellows). These pass through to our eyes.
6.  **Context:** Dust and pollution can enhance this effect.

</thinking>

The sky turns red at sunset due to a phenomenon called **Rayleigh Scattering**.

1.  **Distance:** When the sun is setting, its light has to travel through a much thicker layer of the Earth's atmosphere to reach you than it does at noon.
2.  **Scattering:** Blue light scatters very easily. Because the path is so long, almost all the blue light is scattered out of your line of sight before it reaches you.
3.  **The Result:** The light that remains is made of longer wavelengths—reds and oranges—which pass through the atmosphere more easily, creating the sunset colors you see.
```






### Prompt Used

```prompt
Great, now analyze what you just generated and scrutinize it for errors and or improvements that can be made to enable better optimization for the model that will be using them.
Add in coding exemplar that the models can use. MAIN MODEL:: Claude/Gemini
```

### Gemini Thinking

**Reviewing and Refining Examples**
I've been going over the examples, focusing on how clearly they present the reasoning paths. My goal is to streamline them for Claude and Gemini, aiming for maximum efficiency. I'm now working on the "coding exemplar" section, figuring out how to best integrate it into the existing structure.

**Improving Optimization for Models**
I'm focused on the output's structure, aiming for tighter logic and better prompt efficiency. I'm prioritizing Claude and Gemini, and streamlining the examples is key. Refining the "PHASE 1" triggers for maximum clarity and conciseness, especially. I'm moving from simulated code to providing the models with a template for code generation with proper error handling; the tree of thoughts example also needs a better "scoring" system to reflect true ToT methodology.

**Revising for Production Readiness**
I'm focused on transforming the example outputs into truly usable prompts for Claude and Gemini. This means cleaning up the "PHASE 1" triggers for maximum impact and moving toward templates to ensure the models produce viable code. I am specifically separating the question generation step in the CoVe and integrating explicit scoring in the ToT example. The "Python Reasoning Interface" exemplar is currently being developed.

**Re-Evaluating Prior Generations**
I've reviewed the existing exemplars, and I need to improve their structure for Claude and Gemini, as requested. The primary focus is clarity and instruction-following; I'm going to refine the "PHASE 1" triggers and introduce a Python Reasoning Interface to drive code generation. I'm restructuring the ToT example for better scoring, too.


### 🔍 Self-Correction & Optimization Analysis

Upon reviewing the previous generation, I have identified three key areas for optimization, specifically tailored for high-reasoning models like **Claude 3.5 Sonnet** and **Gemini 1.5 Pro**:

1.  **Tree of Thoughts (ToT) Lack of Rigor:** The previous example treated ToT as merely "brainstorming three options." To be effective for Claude/Gemini, ToT requires **explicit scoring metrics** (e.g., 0-10 confidence scores) and a defined **pruning step** where low-scoring branches are explicitly discarded.
2.  **Chain of Verification (CoVe) Contamination:** The previous example generated questions and answers in the same breath. For Gemini/Claude, it is safer to enforce a **stop sequence** or a distinct separation where the model *only* lists questions first, then answers them, to prevent the "correct" answer from hallucinating the verification data.
3.  **Program of Thoughts (PoT) Output Parsing:** The previous Python example lacked a standardized output format (like `print(json.dumps(result))`). For a system to programmatically use the model's math, the code must print the final answer to `stdout` in a predictable format.

---

### 🚀 Optimized Reasoning Exemplars (Claude/Gemini Tuned)

These exemplars use stricter XML hierarchies and explicit "Scoring/Pruning" steps, which Claude and Gemini adhere to very well.

#### 1. Optimized Tree of Thoughts (ToT)
**Improvement:** Adds explicit quantitative scoring and pruning logic.

```xml
<thinking>
  <phase type="strategy_selection">
    <selected>Tree of Thoughts</selected>
    <rationale>The user is asking for a "crisis communication strategy," which requires evaluating multiple stakeholder risks. Linear reasoning may miss secondary fallout.</rationale>
  </phase>

  <phase type="branching">
    <problem>Data leak of 5,000 user emails. Need response strategy.</problem>
    
    <branch id="1" approach="Full Transparency Immediately">
      <thought>Send email to all users now. Admit fault.</thought>
      <pros>High trust, honest.</pros>
      <cons>Media panic before fix is ready.</cons>
      <score>6/10</score>
    </branch>

    <branch id="2" approach="Silent Patch then Notify">
      <thought>Fix the vulnerability first (24h), then notify users.</thought>
      <pros>Prevents hackers from exploiting the hole during panic.</pros>
      <cons>Risk of leak being discovered by 3rd party first.</cons>
      <score>9/10</score>
    </branch>

    <branch id="3" approach="Denial / Downplay">
      <thought>Claim it was a "maintenance glitch" unless pressed.</thought>
      <pros>Short term stock stability.</pros>
      <cons>Catastrophic long-term trust loss if exposed.</cons>
      <score>2/10</score>
    </branch>
  </phase>

  <phase type="pruning">
    <action>Pruning Branch 3 (Unethical/High Risk).</action>
    <action>Pruning Branch 1 (Premature).</action>
    <selection>Branch 2 is the robust path.</selection>
  </phase>

  <phase type="refinement">
    <refining_branch_2>
      Drafting the "Silent Patch" timeline: 
      Hour 0-4: Engineering lockdown. 
      Hour 5: Patch verify. 
      Hour 6: Legal draft. 
      Hour 8: Public notification.
    </refining_branch_2>
  </phase>
</thinking>

**Recommended Strategy:** We should prioritize securing the vulnerability immediately (Steps 1-4) before issuing a public statement to prevent further exploitation...
```

#### 2. Optimized Program of Thoughts (PoT)
**Improvement:** Enforces a "Coding Sandbox" mentality where the model writes Python to solve the logic, rather than guessing.

````xml
<thinking>
  <phase type="strategy_selection">
    <selected>Program of Thoughts</selected>
    <rationale>The user asked to "Calculate the date 45 weekdays from today, excluding US holidays." LLMs are terrible at calendar math. Python `pandas` or `datetime` is required.</rationale>
  </phase>

  <phase type="coding">
    <plan>
      1. Import pandas for business day calculation.
      2. Define US holidays for the current year.
      3. Calculate start_date + 45 business days.
      4. Print result in ISO format.
    </plan>
    
    <code_generation>
```python
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from datetime import datetime

def calculate_deadline():
    # Setup
    today = datetime.now()
    us_cal = USFederalHolidayCalendar()
    
    # Create custom business day offset (excludes weekends & holidays)
    bday_us = CustomBusinessDay(calendar=us_cal)
    
    # Calculate
    target_date = today + (45 * bday_us)
    
    return target_date.strftime('%Y-%m-%d')

# Execute and Print
print(calculate_deadline())
```
    </code_generation>
  </phase>
</thinking>

Based on the calculation, the deadline is **[Date Output from Code]**.
````

---

### 💻 The "Coding Exemplar" for System Injection

This is a specific module you can add to your System Prompt. It teaches Claude/Gemini exactly how to behave when they need to write code to solve a problem.

**Usage:** Add this to the `<reasoning_library>` section of your master prompt.

````xml
<coding_exemplar>
  <directive>
    When a user request involves:
    1. Complex Arithmetic (> 3 steps)
    2. Date/Time manipulation
    3. String manipulation (counting words, reversing letters)
    4. Logic Puzzles (Who owns the zebra?)
    
    YOU MUST NOT GUESS. You must act as a Python Interpreter.
  </directive>

  <protocol>
    1. Identify variables and constraints.
    2. Write a self-contained Python script inside a `python` markdown block.
    3. Ensure the script prints the final answer to stdout using `print()`.
    4. If the script requires standard libraries (math, datetime, json, re, random), import them.
    5. Simulate the execution of the code mentally to derive the answer (or if in a tool-use environment, wait for the tool output).
  </protocol>

  <template_example>
    User: "What is the sum of the first 50 prime numbers?"
    
    Model Response:
    <thinking>
      Strategy: Program of Thoughts.
      Reason: Summing primes is computationally heavy and error-prone for text generation.
    </thinking>
    
    ```python
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    primes = []
    num = 2
    while len(primes) < 50:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    total = sum(primes)
    print(f"The sum is: {total}")
    ```
    
    *Output Simulation: The sum is: 5117*
    
    The sum of the first 50 prime numbers is 5,117.
  </template_example>
</coding_exemplar>
````