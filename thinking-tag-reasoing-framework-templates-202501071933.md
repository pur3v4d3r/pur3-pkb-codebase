Based on the detailed analysis of the **Advanced Reasoning Brainstorming System (v2.0.0)**, I have designed a set of **Thinking Tag Templates**.

These templates are designed to be inserted into the system instructions or prompt of an AI model to force it to execute the specific cognitive architectures (Tree-of-Thoughts, Self-Refine, etc.) defined in your report *before* generating the final response.

Here are three distinct templates tailored for different depths of analysis.

### 1. The "Master Architect" Template (End-to-End Problem Solving)

**Best for:** Complex, ambiguous challenges requiring a full strategic and operational breakdown (e.g., "How do we fix the US healthcare system?" or "Design a Mars colony supply chain").

```xml
<thinking_process_guidelines>
You must execute the following structured cognitive process within your internal monologue before answering:

1.  **PHASE 1: PROBLEM ARCHITECTURE**
    * **Decomposition**: Define Core Challenge, Success Criteria (Hard/Soft constraints), and Stakeholder Map.
    * **Classification**: Is this Technical, Strategic, Creative, or Operational? Set your weighting accordingly.

2.  **PHASE 2: MULTI-PATH EXPLORATION (Tree of Thoughts)**
    * Generate ideas using *all four* approaches:
        * *Approach A (First Principles)*: Rebuild from ground truths.
        * *Approach B (Cross-Domain Analogy)*: Map solutions from Biology, Engineering, or History.
        * *Approach C (Contrarian Inversion)*: Invert the problem; optimize for the opposite to find insights.
        * *Approach D (Future-Backwards)*: Envision the ideal state 5 years out and work backward.

3.  **PHASE 3: DEEP EVALUATION & SYNTHESIS**
    * Select the top 5 ideas.
    * Score them on Feasibility (Technical/Resource) and Innovation (Novelty/Impact).
    * Synthesize: Combine complementary ideas into a robust portfolio (Quick Wins vs. Big Bets).

4.  **PHASE 4: CHAIN OF VERIFICATION**
    * Extract specific factual claims from your top ideas.
    * Perform "Independent Verification": Simulate a fact-check for each claim without bias.
    * Downgrade confidence for any idea relying on unverified claims.

5.  **PHASE 5: ADVERSARIAL CRITIQUE**
    * Play "Devil's Advocate." Attack your own top recommendations.
    * Refine the ideas to address these flaws or acknowledge the risks.

6.  **PHASE 6: SKELETON-OF-THOUGHTS**
    * Outline the final structure: Executive Summary -> Ranked Recommendations -> Implementation Path -> Risks.
</thinking_process_guidelines>

```

---

### 2. The "Innovation Engine" Template (Focus on Creativity)

**Best for:** Brainstorming, product design, or marketing challenges where novelty is prioritized over immediate operational feasibility. Focuses heavily on Phases 2 and 3.

```xml
<thinking_process_guidelines>
Focus your internal reasoning on Divergent Thinking and Synthesis:

1.  **Define the Box**: Briefly list the constraints so you know what you are breaking.

2.  **Run Cognitive Simulations (Approaches A-D)**:
    * *First Principles*: Strip away "industry standard" assumptions. What is the physics/logic of the problem?
    * *Analogy Transfer*: Force a metaphor. "How would a fungus/swarm/market/algorithm solve this?"
    * *Inversion*: "How could we guarantee failure?" -> Reverse that.
    * *Future-Back*: "It is 2030 and this problem is obsolete." What changed?

3.  **Synthesis & Mutation**:
    * Look for "Hybrid" solutions (e.g., Idea A3 + Idea C1).
    * Identify "Emergent Insights" that appear across multiple pathways.

4.  **Novelty Check**:
    * Discard any idea that is obvious or currently standard practice.
    * Prioritize ideas that score high on "Contrarian" and "Visionary" scales.
</thinking_process_guidelines>

```

---

### 3. The "Rigor & Risk" Template (Focus on Critique & Verification)

**Best for:** Reviewing an existing plan, strategic decision-making, or highly technical feasibility studies. Focuses heavily on Phases 4 and 5.

```xml
<thinking_process_guidelines>
Your primary goal is Risk Assessment and Truth-Seeking. Execute this verification loop:

1.  **Claim Extraction**: Isolate every factual claim, statistical assertion, or feasibility assumption in the proposed solution.

2.  **Verification Protocol**:
    * For each claim: Assign a confidence level (Verified/Partially Verified/Unknown).
    * *Constraint*: You must not assume the claim is true just because it sounds plausible.

3.  **Adversarial Attack (Red Teaming)**:
    * Adopt the persona of a hostile competitor or skeptical regulator.
    * Identify the "Fatal Flaw" in the logic.
    * Stress-test: "Under what specific conditions does this solution break?"

4.  **Confidence Calibration**:
    * Assign a final Confidence Score (Very Low to Very High).
    * If confidence is <70%, explicitly list the "Known Unknowns" that need research.
</thinking_process_guidelines>

```

### How to use these templates

1. **System Prompt Injection**: Paste the selected XML block into the system instructions of the LLM.
2. **User Prompt Injection**: If you don't have access to system instructions, paste the XML block at the very start of your prompt, followed by: *"Apply the framework above to the following challenge: [Your Challenge]."*
3. **Analyze the Output**: The model will (or should, depending on capabilities) produce a `<thinking>` block (or simply output the reasoning if thinking tags aren't supported) that follows this strict logic before giving you the final answer.


Based on the detailed system configuration provided, I have performed a deep analysis of the "Advanced Reasoning Brainstorming System" (ARBS).

Here is the breakdown of the system's cognitive architecture, followed by three specific **Thinking Tag Templates** designed to trigger this specific reasoning process in Large Language Models (LLMs) for analysis tasks.

### Part 1: System Analysis

The ARBS is a **meta-cognitive framework** designed to force an LLM out of linear, probable token generation and into a recursive, lateral, and critical thinking mode. It solves the common AI pitfalls of "hallucination" and "lazy convergence" (settling on the first likely answer).

**Core Mechanics:**

1. **Forced Divergence (Phase 2):** It explicitly forbids linear thinking by mandating four distinct "cognitive modes" (First Principles, Analogy, Contrarian, Future-Backwards). This mimics "Tree of Thoughts" prompting.
2. **Adaptive Weighting:** It recognizes that not all problems are equal. A technical engineering problem requires different cognitive weights (First Principles) than a marketing problem (Contrarian/Creative).
3. **Adversarial Filtering (Phase 3 & 5):** It integrates a "Devil's Advocate" step and a "Chain of Verification," effectively using the model to police its own output before the user sees it.
4. **Structured Synthesis:** It refuses to dump raw data. It forces the output into a specific "Skeleton of Thoughts" (Executive Summary → Ranked Recs → Actionable Steps).

---

### Part 2: Thinking Tag Templates

Below are three templates derived from this framework. You can paste these into your system instructions or prompt to force the specific type of reasoning described in the document.

#### Template 1: The "Omni-Solver" (Comprehensive Analysis)

*Use this for complex, undefined problems where you need the full power of the framework (Phases 1-6).*

```xml
<thinking_process>
  <step name="Decomposition">
    1. Define core problem and success criteria.
    2. Map stakeholders and their conflicting interests.
    3. Identify Hard vs. Soft constraints.
    4. Classify Problem Type: [TECHNICAL | STRATEGIC | CREATIVE | OPERATIONAL]
  </step>

  <step name="Ideation_Matrix">
    Generate 3-5 distinct ideas for EACH approach:
    
    [Approach A: First Principles]
    - Identify assumptions -> Challenge them -> Rebuild from ground truth.
    
    [Approach B: Cross-Domain Analogy]
    - Abstract the problem structure.
    - Map to [Biology, Engineering, History, Markets].
    - Transfer solution mechanics.
    
    [Approach C: Contrarian Inversion]
    - What is the orthodoxy? Invert it.
    - What would make this worse? (Reverse engineering).
    
    [Approach D: Future-Backwards]
    - Envision ideal state in 3 years.
    - Work backward to identifying necessary milestones today.
  </step>

  <step name="Deep_Critique">
    1. Select top 5 ideas.
    2. Extract verifiable claims (Stats, Market Data, Tech Limits).
    3. Perform Independent Verification (Simulated fact-checking).
    4. Rate Feasibility (Tech/Resource/Org) and Innovation (Novelty/Impact) on 1-10 scale.
  </step>

  <step name="Devils_Advocate">
    For the top 2 recommendations:
    - Attempt to destroy the idea. What is the fatal flaw?
    - If idea survives, list mitigations. If not, discard.
  </step>

  <step name="Final_Selection">
    Select:
    - 1 Quick Win
    - 1 Strategic Bet
    - 1 Moonshot
    Prepare "Skeleton of Thoughts" structure for final output.
  </step>
</thinking_process>

```

#### Template 2: The "Strategic Disruptor" (Creative/Strategic Focus)

*Use this for business strategy, marketing, or innovation tasks where "Approaches C and D" are most critical.*

```xml
<thinking_process>
  <phase name="Context_Setting">
    Classify: STRATEGIC / CREATIVE
    Primary Goal: Differentiation and Long-term Value.
  </phase>

  <phase name="Orthodoxy_Analysis">
    1. List the "Standard Model" of how this is currently done.
    2. Identify the "Invisible Constraints" everyone accepts.
  </phase>

  <phase name="Inversion_and_Future_Cast">
    <path_c>
      - If we optimized for the exact opposite metric, what happens?
      - How would a complete outsider solve this?
    </path_c>
    <path_d>
      - Describe the "Impossible Success" 5 years from now.
      - What "Magic" (technology/policy) is required to make it real?
      - How can we simulate that magic today?
    </path_d>
  </phase>

  <phase name="Feasibility_Anchoring">
    Take the wildest ideas from above and anchor them in reality:
    - What is the Minimum Viable Version?
    - What is the "Trojan Horse" entry point?
  </phase>

  <phase name="Risk_Assessment">
    Pre-Mortem: Imagine the strategy failed 2 years from now. Why did it fail?
  </phase>
</thinking_process>

```

#### Template 3: The "Rigorous Verifier" (Technical/Operational Focus)

*Use this when the solution is already known or proposed, and you need to stress-test it (Focus on Phases 3, 4, and 5).*

```xml
<thinking_process>
  <target_analysis>
    Input Idea: [Insert Idea/Plan]
  </target_analysis>

  <step name="Claim_Extraction_Protocol">
    Isolate distinct claims in the input:
    - Market Claims ("X people want this")
    - Technical Claims ("Y can handle Z load")
    - Resource Claims ("This will cost $A")
  </step>

  <step name="Chain_of_Verification">
    For each claim:
    1. Independent Check: Is this verified, plausible, or speculative?
    2. Confidence Score: Assign Low/Med/High confidence.
  </step>

  <step name="First_Principles_Audit">
    Deconstruct the solution to physics/code/process fundamentals:
    - Does it violate any hard constraints?
    - Is it built on a shaky assumption?
  </step>

  <step name="Adversarial_Stress_Test">
    Attack Vectors:
    - Scalability: What breaks at 10x scale?
    - Edge Cases: What happens in the worst-case scenario?
    - Adoption: Why will stakeholders hate this?
  </step>

  <step name="Refinement">
    Generate "Patch List": Specific modifications to fix identified flaws.
  </step>
</thinking_process>

```

### How to use these templates

To activate the **Advanced Reasoning Brainstorming System** effectively, append the relevant template to your prompt inside a specific tag.

**Example User Prompt:**

> "I need to design a new loyalty program for a coffee chain.
> Use the [Omni-Solver] thinking framework.
> [Paste Template 1 Here inside a system block or at the start of your prompt]"










Based on the **Advanced Reasoning Brainstorming System** architecture, here are four specialized Thinking Tag Templates. These isolate specific cognitive functions—Decomposition, Exploration, State Management, and Synthesis—allowing you to inject targeted reasoning behaviors into an LLM for specific phases of a task.

### 1. The "Fractal Decomposer" (Task Decomposition)

*Use this for complex, monolithic requests that need to be broken down into atomic, executable units before any work begins.*

```xml
<thinking_process_decomposition>
  <step name="Scope_Definition">
    1. Input Analysis: What is explicitly asked vs. implicitly needed?
    2. Constraints:
       - Hard (Binary pass/fail)
       - Soft (Trade-offs allowed)
    3. Output definition: What exactly does "Done" look like?
  </step>

  <step name="Atomic_Unit_Splitting">
    Apply recursive logic until tasks are "Atomic" (solvable in one step):
    
    Level 1 (Major Components):
    - [Component A]
    - [Component B]
    
    Level 2 (Sub-tasks for A):
    - [A.1] -> Dependencies?
    - [A.2] -> Dependencies?
    
    Level 3 (Atomic Actions for A.1):
    - [Action i]
    - [Action ii]
  </step>

  <step name="Logic_Flow">
    Map the critical path:
    - Blockers: What MUST happen first?
    - Parallelism: What can happen simultaneously?
    - Riskiest Assumption: Which sub-task is most likely to fail?
  </step>

  <step name="Staging">
    Group atomic actions into phases:
    - Phase 1: Foundation (The "Hello World" or MVP)
    - Phase 2: Core Logic
    - Phase 3: Polish & Edge Cases
  </step>
</thinking_process_decomposition>

```

### 2. The "Lateral Explorer" (Exploration & Divergence)

*Use this when you are stuck or need to widen the search space. It forces the model to abandon the "likely" path and explore the "possible" path.*

```xml
<thinking_process_exploration>
  <setting>
    Goal: Maximize variety of solution paths.
    Constraint: Do NOT critique ideas yet. Quantity > Quality.
  </setting>

  <step name="Perspective_Rotation">
    Redefine the problem from 3 radical perspectives:
    1. The Minimalist: "How to solve this with $0 or 0 lines of code?"
    2. The Maximalist: "If resources were infinite, what is the 'God Mode' solution?"
    3. The Alien: "How would a system with no knowledge of human context solve this?"
  </step>

  <step name="Domain_Transfer">
    Problem Pattern: [Abstract the pattern, e.g., "Resource Contention"]
    Map to:
    - Biological Systems (e.g., Ant colony foraging)
    - Historical Events (e.g., Industrial Revolution logistics)
    - Physical Laws (e.g., Path of least resistance)
    Extract the mechanism from the analogy and apply to current task.
  </step>

  <step name="Variable_Tweaking">
    Identify the 3 core variables of the problem.
    Randomly invert or exaggerate them:
    - Variable A (Speed) -> Make it instant vs. make it extremely slow/deliberate.
    - Variable B (Trust) -> Zero trust vs. total trust.
    - Variable C (Size) -> Micro vs. Macro.
  </step>
</thinking_process_exploration>

```

### 3. The "State Monitor" (State Management & Metacognition)

*Use this for long, multi-turn tasks (like coding a full app or writing a book) where the model needs to "remember" where it is in the broader plan.*

```xml
<thinking_process_state>
  <status_check>
    Current Goal: [What are we trying to achieve in THIS turn?]
    Global Progress: [Phase X of Y]
    Active Context:
    - Known Variables: [List confirmed facts/code snippets]
    - Unknowns: [List what we still need to figure out]
    - Technical Debt: [Hacks or shortcuts taken so far]
  </status_check>

  <validation>
    Compare Current State vs. Desired State:
    - Gap Analysis: What is missing?
    - Drift Warning: Are we diverging from the original requirements?
  </validation>

  <decision_logic>
    Based on status:
    IF (Unknowns > 0) -> Trigger [Research_Subroutine]
    IF (Error detected) -> Trigger [Debug_Subroutine]
    IF (On track) -> Trigger [Next_Atomic_Action]
  </decision_logic>

  <scratchpad_update>
    Write to persistent memory:
    - "Completed: [Task A]"
    - "Pending: [Task B]"
    - "Note to self: Watch out for [Edge Case X]"
  </scratchpad_update>
</thinking_process_state>

```

### 4. The "Convergence Engine" (Synthesis & Selection)

*Use this at the end of a brainstorming session to collapse multiple options into a single, high-confidence recommendation.*

```xml
<thinking_process_synthesis>
  <input_stream>
    Gather all generated options/paths from previous steps.
  </input_stream>

  <step name="Binary_Filter">
    Apply pass/fail criteria.
    - Discard any option that violates a Hard Constraint (Cost, Physics, Law).
    - Mark "Survivors".
  </step>

  <step name="Matrix_Evaluation">
    Score Survivors (1-5) on:
    - Complexity (Low is better)
    - Robustness (High is better)
    - Value/Impact (High is better)
    
    Calculate Weighted Score:
    Score = (Value * 1.5) + (Robustness * 1.0) - (Complexity * 1.0)
  </step>

  <step name="Hybridization">
    Look at the top 2-3 Survivors.
    - Can they be merged?
    - Does Option A solve Option B's main weakness?
    Create "Hybrid Candidate" if possible.
  </step>

  <step name="Recommendation_Lock">
    Select Winner.
    Draft "Why it won" rationale.
    Draft "Why others lost" rationale (pre-empting questions).
  </step>
</thinking_process_synthesis>

```



The "Advanced Reasoning Brainstorming System" (ARBS) is highly effective because it modularizes cognition. To help you apply this modularity to other specific cognitive tasks, here are three additional **Thinking Tag Templates**.

These focus on specific aspects of the reasoning pipeline: **Task Decomposition**, **Exploratory Research**, and **State/Progress Tracking**.

### Template 4: The "Fractal Decomposer" (Task Decomposition)

*Use this for breaking down massive, overwhelming projects into executable atoms. This template uses a recursive "zoom-in" strategy.*

```xml
<thinking_process>
  <step name="Prime_Directive">
    1. Define the Ultimate Goal (The "Definition of Done").
    2. Identify the "Critical Path" (The sequence of events that MUST happen).
  </step>

  <step name="Level_1_Major_Milestones">
    Split the project into 3-5 high-level phases (e.g., Research, Prototype, Scale).
    Format: [Phase Name] -> [Objective]
  </step>

  <step name="Level_2_Component_Splitting">
    For EACH Level 1 Phase:
    - Identify sub-components (Teams, Tech Stack, Logistics).
    - Flag dependencies: "Component B cannot start until Component A is finished."
  </step>

  <step name="Level_3_Atomic_Tasks">
    Zoom into the most critical Level 2 components.
    Break them into "Atomic Tasks" (tasks that can be done by one person in <4 hours).
    Tag each atom: [Hard/Easy], [High Priority/Low Priority].
  </step>

  <step name="Resequencing">
    Look at the pile of Atomic Tasks.
    - Which ones are "Blockers"? (Must be done first).
    - Which ones are "Quick Wins"? (Build momentum).
    - Which ones can be parallelized?
  </step>

  <output_prep>
    Generate a Gantt-style logic flow or a prioritized backlog.
  </output_prep>
</thinking_process>

```

### Template 5: The "Divergent Explorer" (Research & Learning)

*Use this when the goal isn't to solve a problem, but to map a new territory, learn a subject, or gather intelligence. It emphasizes breadth over depth initially, then targeted drilling.*

```xml
<thinking_process>
  <phase name="Cartography">
    1. Define the Knowledge Domain (e.g., "Generative AI Agents").
    2. Identify Key Landmarks:
       - Who are the key players/authors?
       - What are the seminal papers/events?
       - What is the jargon/vocabulary list?
    3. Identify "Terra Incognita" (What do we NOT know? What is controversial?).
  </phase>

  <phase name="Perspective_Rotation">
    View the topic through different lenses:
    - [The Historian]: How did we get here?
    - [The Engineer]: How does it actually work under the hood?
    - [The Economist]: Who makes money from this?
    - [The Critic]: What are the ethical/safety failures?
  </phase>

  <phase name="Synthesis_and_Gaps">
    1. Connect the dots: How does the History explain the Economics?
    2. Spot the contradictions: Where do experts disagree?
    3. Formulate "Research Questions": Specific queries to resolve contradictions.
  </phase>

  <phase name="Distillation">
    Compress findings into:
    - 5 Key Principles
    - 1 Core Mental Model
    - A "Learning Curriculum" for a beginner.
  </phase>
</thinking_process>

```

### Template 6: The "State Manager" (Long-Running Context)

*Use this for complex, multi-turn conversations or coding tasks where the model needs to "remember" where it is in a long process. This simulates a "Working Memory" buffer.*

```xml
<thinking_process>
  <step name="Context_Loading">
    1. Read previous turns.
    2. Identify the "Current State" of the project:
       - [ ] Planning
       - [ ] Execution
       - [ ] Debugging
       - [ ] Final Review
    3. Retrieve "Global Variables": (User constraints, file names, tech stack choices).
  </step>

  <step name="Delta_Analysis">
    - What was the last action taken?
    - Did it succeed? (Verify output vs intent).
    - What is the immediate "Next Logical Step"?
  </step>

  <step name="Lookahead">
    - If I take [Next Step], what is likely to break?
    - Do I have all necessary info, or do I need to ask the user?
    - *Decision:* Proceed or Pause for Input?
  </step>

  <step name="Commit_New_State">
    Define the "New State" after this turn is complete.
    (e.g., "Login function complete, moving to Database Schema").
  </step>
</thinking_process>

```

### User Guide: Mixing and Matching

You do not need to use the full ARBS system every time. You can mix these templates based on the user's request:

* **"Help me plan a wedding"**
* Use **Template 4 (Fractal Decomposer)** to break down the event into vendors, guests, timeline.
* Then use **Template 2 (Strategic Disruptor)** to brainstorm "Contrarian" ideas (e.g., "What if we didn't have a dinner?")


* **"Explain Quantum Computing to me"**
* Use **Template 5 (Divergent Explorer)**.
* Lens: [The Historian] (History of physics) -> [The Engineer] (Qubits vs Bits).


* **"Debug this 500-line Python script"**
* Use **Template 3 (Rigorous Verifier)** to extract "Claims" (This function returns X) and verify them.
* Use **Template 6 (State Manager)** to keep track of which bugs you've fixed as you iterate.