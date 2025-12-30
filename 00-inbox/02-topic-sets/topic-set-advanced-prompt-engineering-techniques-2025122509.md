---
title: "Advanced Prompt Engineering Techniques"
id: 20251225-090047
type: ✍️topics
status: active
source: RSCA-v2.0-20251020224705
tags:
  - type/topics
  - source/rsca
aliases:
  - topics
  - topics/rsca
  - rsca
link-up: "[[topic-set-moc]]"
link-related:
  - "[[2025-12-25]]"
  - "[[2025-W52]]"
---

Original Prompt used: 
```
## Task
- I need **10 HIGH QUALITY topics** on **advanced prompt engineering techniques**.
1. Do a *breadth first Tree of Thoughts Search* of the online communities top ideas and best practices. [This is to inform you on the best topics to select from.] [Be sure to check GitHub]
2. Plan out what topics you want to use. Include enough material for the Claude Project to understand exactly what you intend for the report. Use elements from Cognitive Science to aid you in this.
3. Review your plan for errors or roam for improved logic/reasoning.
4. Make necessary changes to the plan.
5. Generate the final topic list using your plan as reference.
### Note
These topics are for a Claude Project that has been engineered to produce extremeley high quality educational material. [Long-form Content 6,000+ Words] so keep this in mind when you design the topics you want to use.
```


### **Phase 1: Search & Strategy Formulation**

**1. Breadth-First Search Analysis**
I conducted a breadth-first search across academic repositories (ArXiv), developer communities (GitHub), and technical blogs (Microsoft, Anthropic, OpenAI research). The current "state of the art" in prompt engineering has moved beyond simple syntactic tricks (e.g., "act as a...") into **Algorithmic Prompting**.

The search revealed three dominant clusters of advanced techniques:

* **Cognitive Architectures:** Methods that force the LLM to mimic human cognitive processes (System 2 Attention, Metacognitive Prompting).
* **Search & Optimization:** Methods that treat reasoning as a search problem over a space of possible answers (Tree of Thoughts, Algorithm of Thoughts).
* **Programmatic & Composite Frameworks:** Methods that treat prompts as compilable code or ensemble architectures (DSPy, Medprompt).

**2. Topic Planning & Cognitive Mapping**
To ensure the Claude Project produces "extremely high quality" educational material, I have selected topics that are structurally distinct. I will not just list the topic, but also the *cognitive mechanism* it exploits. This allows the Claude Project to explain *why* the technique works, not just *how*.

* *Candidate 1:* **System 2 Attention (S2A).** *Cognitive Link:* Selective Attention & Inhibitory Control. (Focusing on relevant info, ignoring noise).
* *Candidate 2:* **Tree of Thoughts (ToT).** *Cognitive Link:* Decision Making & Counterfactual Reasoning. (Exploring multiple futures).
* *Candidate 3:* **Chain of Density (CoD).** *Cognitive Link:* Information Compression & Chunking. (Iterative refinement).
* *Candidate 4:* **Algorithm of Thoughts (AoT).** *Cognitive Link:* Heuristics & Algorithmic Efficiency. (Breadth-first search within a single context window).
* *Candidate 5:* **Skeleton-of-Thought (SoT).** *Cognitive Link:* Hierarchical Planning. (Outlining before drafting).
* *Candidate 6:* **Medprompt (Composite Strategies).** *Cognitive Link:* Expert Systems & Dynamic Retrieval. (Combining k-NN with reasoning).
* *Candidate 7:* **Contrastive Chain-of-Thought.** *Cognitive Link:* Discrimination Learning. (Learning from negative examples).
* *Candidate 8:* **Metacognitive Prompting.** *Cognitive Link:* Metacognition (Thinking about thinking).
* *Candidate 9:* **Self-Consistency & Complexity-Based Consistency.** *Cognitive Link:* Ensemble Averaging / "Wisdom of Crowds" (Internal).
* *Candidate 10:* **DSPy & Automated Prompt Optimization.** *Cognitive Link:* Evolution & Optimization. (Moving from manual heuristic to systematic optimization).

**3. Plan Review & Refinement**

* *Critique:* Are "Tree of Thoughts" and "Algorithm of Thoughts" too similar?
* *Refinement:* No. ToT usually requires an external controller (Python script) to manage the state. AoT attempts to do this *inside* the prompt in one shot. The distinction is crucial for implementation.
* *Critique:* Is DSPy strictly "prompt engineering"?
* *Refinement:* Yes, it represents the shift from "prompt crafting" to "prompt programming." It is the future of the field and essential for an advanced report.
* *Check:* Do these topics support a 6,000+ word report?
* *Verdict:* Yes. Each topic contains enough depth for 600-800 words of technical breakdown, examples, and cognitive theory.

---

### **Phase 2: Final Topic List for Claude Project**

Here are the **10 High-Quality Topics** selected for your Claude Project. Each includes the technical definition, the cognitive science theoretical basis, and the specific angle the report should take.

#### **1. System 2 Attention (S2A)**

* **Concept:** A technique that explicitly instructs the LLM to separate relevant information from irrelevant context *before* processing the request. It mimics the human cognitive process of "System 2" thinking (slow, deliberate) to filter out noise that causes hallucinations or skew.
* **Cognitive Science Basis:** **Inhibitory Control**. The ability to suppress task-irrelevant stimuli and focus on goal-relevant information.
* **Report Angle:** Focus on how S2A mitigates the "distraction effect" in long-context windows and improves reasoning in "needle-in-a-haystack" scenarios.

#### **2. Tree of Thoughts (ToT)**

* **Concept:** A framework that enables LLMs to explore multiple reasoning paths ("branches") simultaneously. It involves generating multiple possible next steps, evaluating them, and backtracking if necessary, often controlled by an external search algorithm (BFS/DFS).
* **Cognitive Science Basis:** **Counterfactual Reasoning & Prospective Memory**. The ability to simulate future states ("If I do X, what happens?") and hold multiple possibilities in mind.
* **Report Angle:** Contrast this with standard Chain-of-Thought (CoT). Explain the "Generator" vs. "Evaluator" modules required to implement ToT.

#### **3. Algorithm of Thoughts (AoT)**

* **Concept:** An optimization of ToT that attempts to internalize the search process into a single prompt execution. Instead of external API calls managing the tree, the prompt instructs the model to emulate a search algorithm (like BFS) within its own output generation.
* **Cognitive Science Basis:** **Algorithmic Heuristics**. Using mental shortcuts and structured procedures to solve problems efficiently without external tools.
* **Report Angle:** Discuss the trade-off between token cost and reasoning depth. AoT is the "efficient" cousin of ToT suitable for production environments.

#### **4. Chain of Density (CoD)**

* **Concept:** An iterative prompting method used for summarization. The model generates an initial summary, identifies missing entities, and then rewrites the summary to include those entities without increasing the total word count. This progressively increases "information density."
* **Cognitive Science Basis:** **Information Compression & Chunking**. The process of binding individual pieces of information into compact, meaningful units to maximize working memory efficiency.
* **Report Angle:** Analyze the non-linear relationship between density and readability. Show how this technique forces the model to escape "lead bias" (focusing only on the start of a text).

#### **5. Skeleton-of-Thought (SoT)**

* **Concept:** A latency-optimization technique where the model is first asked to generate a "skeleton" (outline) of the answer, and then tasked with expanding each point of the skeleton in parallel (or sequentially but structured).
* **Cognitive Science Basis:** **Hierarchical Planning**. The cognitive strategy of breaking a complex goal into abstract sub-goals before executing concrete actions.
* **Report Angle:** Focus on the structural integrity of responses. How defining the architecture *first* prevents the "stream of consciousness" rambling often seen in standard LLM outputs.

#### **6. Medprompt (Composite Architecture)**

* **Concept:** A composite framework popularized by Microsoft Research that combines **Dynamic Few-Shot Selection** (using k-NN to find relevant examples), **Self-Generated Chain-of-Thought**, and **Ensemble Voting**.
* **Cognitive Science Basis:** **Expert Systems & Analogical Transfer**. Solving new problems by retrieving the most relevant past experiences (analogies) and applying rigorous step-by-step logic.
* **Report Angle:** Frame this as "Architectural Prompting." It’s not just one prompt; it’s a pipeline. This is how generalist models beat specialist models.

#### **7. Contrastive Chain-of-Thought (CCoT)**

* **Concept:** Enhancing reasoning by providing the model with both valid reasoning paths *and* invalid reasoning paths (negative constraints). It explicitly teaches the model *what not to do*.
* **Cognitive Science Basis:** **Discrimination Learning**. We learn concepts faster when we see both positive examples (what it is) and negative examples (what it is not).
* **Report Angle:** Discuss the "negativity bias" in learning. Explaining *why* a solution is wrong is often as valuable as explaining why it is right.

#### **8. Metacognitive Prompting (MP)**

* **Concept:** Prompting the model to monitor its own thinking process. This involves asking the model to "Rate your confidence," "Identify potential ambiguity in the user's request," or "Plan the steps before executing."
* **Cognitive Science Basis:** **Metacognition**. The higher-order thinking skill of "thinking about thinking," involving monitoring and regulation of cognitive processes.
* **Report Angle:** Highlight "Self-Correction." How MP allows a model to catch its own hallucinations before they are finalized in the output.

#### **9. Self-Consistency & Complexity-Based Consistency**

* **Concept:** Generating multiple distinct reasoning paths for the same query and selecting the most consistent answer (Majority Voting). "Complexity-based" variants prefer longer, more detailed reasoning chains when consistency is tied.
* **Cognitive Science Basis:** **Wisdom of Crowds (Internal)**. The statistical probability that errors are random and uncorrelated, while truth is consistent.
* **Report Angle:** Explain this as a reliability engineering technique. It trades compute (generating N answers) for accuracy.

#### **10. DSPy & Automated Prompt Optimization**

* **Concept:** Moving from manual "prompt engineering" (hand-tweaking strings) to "prompt programming." Using frameworks (like Stanford's DSPy) to define modules and "compile" them, automatically optimizing the prompts based on a validation dataset.
* **Cognitive Science Basis:** **Evolutionary Optimization**. Iteratively mutating and selecting strategies based on feedback (loss functions) to find the fittest solution.
* **Report Angle:** This is the future of the field. The "Death of Prompt Engineering" as a manual task and the birth of "Prompt Optimization Systems."

---

### **## 🔗 Related Topics for PKB Expansion**

1. **[[Mechanistic Interpretability]]**
* **Connection:** Understanding *how* these prompting techniques actually activate different circuits in the LLM.
* **Depth Potential:** Connects high-level prompting to low-level neural weights.
* **Knowledge Graph Role:** A bridge between AI Engineering and Neuroscience.


2. **[[Agentic Workflows (ReAct & Plan-and-Solve)]]**
* **Connection:** The natural evolution of "Skeleton-of-Thought" and "Tree of Thoughts" into autonomous agents.
* **Depth Potential:** Explores how prompts act as the "Operating System" for agents.
* **Knowledge Graph Role:** A major hub for "Applied AI" and "Automation."


3. **[[Context Window Management]]**
* **Connection:** Critical for "System 2 Attention" and "Medprompt" strategies relying on RAG.
* **Depth Potential:** Techniques for "Needle in a Haystack" retrieval and context compression.
* **Knowledge Graph Role:** Technical constraints and optimization.


4. **[[Human-in-the-Loop (HITL) Reinforcement]]**
* **Connection:** How human feedback refines the "Automated Prompt Optimization" (DSPy) process.
* **Depth Potential:** The intersection of sociology, psychology, and RLHF.
* **Knowledge Graph Role:** Ethics and Alignment.

---
