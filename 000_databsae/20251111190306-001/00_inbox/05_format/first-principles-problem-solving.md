---
title: ⚙️The "First Principles" Problem-Solving Framework
id: 20251103211159
type: 🧩component
status: 🌱seedling
rating: ""
version: "1.0"
last-used: 2025-11-03
source: 🦖pur3v4d3r
url: https://gemini.google.com/app/d063ed97dc044da7
tags:
  - prompt-component-library
  - component
  - component/type/scaffold
  - component/type/scaffold
aliases:
  - prompting/component
  - component/⚙️first-principles-problem-Solving
  - component/type/🏗️scaffolding
link-up: "[[🧩prompting-materials-collection_🗺️moc]]"
link-related:
  - "[[gemini-prompt-components]]"
---
# ⚙️The "First Principles" Problem-Solving Framework

  * **[RATIONALE]:** This model combines [[Problem-Based Learning (PBL)]] with [[First Principles Thinking]]. Its purpose is to deconstruct a complex problem or system not by analogy, but by identifying its most fundamental, axiomatic truths. From this foundation, the LLM reasons *up* to build a novel solution or explanation. This model is invaluable for truly understanding *why* something works, rather than just *how* it works, making it ideal for mastering complex systems or scientific concepts.
## ⚙️ Scaffold: The "First Principles" Problem-Solving Framework

> **Note:**
>
>   * **Learning Model:** [[First Principles Thinking]] (Aristotelian) & [[Problem-Based Learning (PBL)]].
>   * **Pedagogical Purpose:** To achieve "generative" understanding by deconstructing a topic to its absolute, axiomatic truths (first principles) and reasoning *up* from them. This bypasses flawed analogies and conventional wisdom, forcing a true, foundational mastery.
>   * **Best Use Cases:**
>     1.  Understanding complex scientific concepts (e.g., [[General Relativity]], [[Quantum Mechanics]], [[Evolutionary Biology]]).
>     2.  Analyzing and re-designing complex systems (e.g., [[PKB Workflow Design]], [[Software Architecture]], [[Economic Models]]).
>     3.  Generating truly novel solutions to long-standing problems.

```component
---
id: prompt-block-🆔20251103211139
---

# ⚙️ First Principles Report: {{Problem or System Title}}

> [!the-goal]
> The goal of this report is to analyze {{Problem or System Title}} by rejecting reasoning-by-analogy and instead employing First Principles Thinking. We will deconstruct the topic to its fundamental, axiomatic truths and reason up from that foundation to build a robust, generative understanding.

> [!pre-read-questions]
> * What is the "common wisdom" or "analogous" way this topic is usually explained?
> * What are the core assumptions I hold about this topic before starting?

---

## 1. 🔍 Phase One: Deconstruct the Problem & Assumptions

This section identifies and dismantles the "conventional wisdom" and surface-level analogies.

> [!the-purpose]
> To identify the current, analogy-based understanding of the problem and the unexamined assumptions it relies upon.

### 1.1. Defining the Problem / System

> [!definition]
> **The Problem/System: {{Name of Problem/System}}**
> * Provide a clear, conventional definition of the topic.
> * How is this concept typically explained or understood? (e.g., "The economy is often described as a 'machine'…")

### 1.2. Identifying "Reasoning by Analogy"

> [!analogy]
> **Common Analogies & Heuristics**
> * What are the most common analogies used to explain this topic? (e.g., "The atom is like a 'solar system'," "The brain is like a 'computer'").
> * How do these analogies shape our understanding?

### 1.3. Challenging Conventional Assumptions

> [!question]
> **Challenging Core Assumptions**
> * This section rigorously questions the conventional wisdom.
> * **Assumption 1:** {{State a common assumption.}}
>     * > [!key-claim]
>     * Why is this assumed to be true? What if it is false?
> * **Assumption 2:** {{State another common assumption.}}
>     * > [!key-claim]
>     * What is the origin of this belief? What evidence *actually* supports it?
> * *(…Continue until all major assumptions are surfaced…)*

---

## 2. ⚛️ Phase Two: Identify First Principles

This is the core of the deconstruction, digging down to the "atomic" level of truth.

> [!the-purpose]
> To isolate the fundamental, irreducible truths of the system—the "first principles" from which all other complexity emerges. These are facts that cannot be debated or broken down further.

### 2.1. The Axiomatic Foundation

> [!atomic-concept]
> **Atomic Concept 1: {{Name of the First Principle}}**
> * Define this core, undeniable truth. (e.g., "For physics: Matter is composed of atoms," "For economics: Humans act to maximize perceived utility," "For biology: All life descends from a common ancestor via natural selection.").
> * > [!evidence]
> * Present the foundational evidence that establishes this as a first principle.

> [!atomic-concept]
> **Atomic Concept 2: {{Name of the First Principle}}**
> * Define this second core, undeniable truth.
> * > [!evidence]
> * Present the foundational evidence.

> [!equation]
> **(Optional) Foundational Equations/Laws**
> * If applicable, state the core mathematical or logical laws that govern this system. (e.g., $E=mc^2$, Laws of Thermodynamics, Law of Supply and Demand).

### 2.2. Distinguishing Principles from Derivatives

> [!analysis-logical]
> **Separating Truths from Dogma**
> * Analyze the assumptions from Phase 1 against the principles from Phase 2.1.
> * Which "common wisdom" elements are merely derivatives, traditions, or misinterpretations?
> * Which are in direct violation of the first principles?

---

## 3. 🧱 Phase Three: Re-Reasoning from the Ground Up

With a clean foundation, this section builds a new, more accurate model.

> [!the-purpose]
> To construct a new, generative model of the system by reasoning logically *upward* from the established first principles.

### 3.1. The First Causal Link

> [!casual-link]
> **Building the First Connection**
> * Take two or more `[!atomic-concept]` principles and explain the *necessary* logical consequence of their interaction.
> * > [!thought-experiment]
> * Use a thought experiment to illustrate this foundational link. (e.g., "If Principle A is true and Principle B is true, what *must* happen when…").

### 3.2. Emergent Complexity

> [!connection-ideas]
> **Layering Emergent Complexity**
> * How does the simple link from 3.1 lead to more complex phenomena?
> * Build the chain of logic, step-by-step, showing how the complex surface-level features (identified in Phase 1) are an *emergent property* of the simple underlying rules.
> * Use `[!phase-one]`, `[!phase-two]`, etc., if building a process.

### 3.3. A New Model

> [!core-principle]
> **The Re-Reasoned Model**
> * Describe the new model of understanding that has been built.
> * How is this model different, more accurate, and more powerful than the analogy-based model from Phase 1?

---

## 4. 💡 Phase Four: The Novel Solution & Its Implications

This section applies the new understanding to solve the original problem.

> [!the-purpose]
> To apply the newly constructed "First Principles" model to generate a novel solution or a more profound explanation.

### 4.1. A Novel Approach

> [!outcome]
> **A Novel Solution / Explanation**
> * Based on the model from Phase 3, what is the logical and optimal solution to the original problem?
> * How does this solution differ from conventional approaches?

### 4.2. Practical Application & Examples

> [!use-cases-and-examples]
> **Use Cases and Examples**
> * Provide 2-3 detailed examples of how this new understanding can be applied.
> * > [!example]
> * **Example 1:** {{Describe a practical application of the new model.}}
> * > [!example]
> * **Example 2:** {{Describe another practical application.}}

---

## 5. 🔬 Concluding Review & Validation

> [!review]
> **Review of the Re-Reasoned Model**
> * Summarize the journey from flawed analogy to first principles and finally to the new, generative model.
> * Reiterate the core insights gained.

> [!feynman-technique]
> **The Feynman Test**
> * Provide a final, simple explanation of the {{Topic}} as if teaching it to a novice, using *only* the new model derived from first principles. This confirms true understanding.

> [!further-exploration]
> **Future Applications**
> * What other problems or systems could this first-principles deconstruction be applied to?
> * What are the limitations of this new model?

```



