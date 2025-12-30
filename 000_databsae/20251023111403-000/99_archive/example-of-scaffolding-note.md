---
id: SS_Deep-Exposition
type: Structural-Scaffold
status:
  - ✅
version: 2
---

# 📖 Component Description
This is the "Foundational Report" scaffold, designed to generate a comprehensive, encyclopedic, and deeply researched report on a core topic. Its purpose is to build a thorough, foundational understanding from first principles.

It is explicitly designed to (1) provide extensive, high-quality prose, (2) identify new avenues for exploration, and (3) create explicit links to existing concepts in the PKB. It leverages a wide array of semantic callouts to structure this knowledge.

# ⚙️ Prompt Component
> [!prompt]
> **Structural Scaffold: Foundational Report (Deep Exposition)**
>
> **1. Define Core Parameters:**
>    * **[TOPIC]:** {{Specify the central topic, concept, or question}}
>    * **[DEPTH_LEVEL]:** {{e.g., "Encyclopedic overview," "In-depth technical analysis," "Historical context"}}
>    * **[EXISTING_CONCEPTS]:** {{(Optional) Provide a list of `[[wikilinks]]` from your vault that you want to connect this topic to, e.Example: `[[Concept A]]`, `[[Theory B]]`}}
>
> **2. Phase 1: Overture & Foundation (The "Why & What")**
>    * **Abstract:** Start with a `> [!abstract]` callout. Provide a high-level, 1-2 paragraph summary of the entire topic.
>    * **Definition:** Provide a clear, unambiguous `> [!definition]` of the `[TOPIC]`.
>    * **Core Principles:** Explain the "big picture." What is the fundamental idea?
>      * `> [!the-philosophy]` or `> [!core-principle]`
>      * `> What is the central problem this topic addresses or the core phenomenon it describes?`
>
> **3. Phase 2: Encyclopedic Exposition (The "Deep Dive")**
>    * **Deconstruction:** Break the `[TOPIC]` down into its logical, primary sub-headings (e.g., History, Mechanism, Key Figures, Sub-types, Implications).
>    * **Detailed Prose (Per Sub-Heading):** For *each* sub-heading, you must write extensive, detailed, and high-quality prose.
>    * **Semantic Enrichment:** As you write, you MUST actively use the following callouts to structure the information:
>        * `> [!atomic-concept]` (For breaking out a small, singular idea)
>        * `> [!key-claim]` (For stating a central assertion)
>        * `> [!evidence]` (To provide data, studies, or proof for a claim)
>        * `> [!argument]` / `> [!counter-argument]` (To explore debates within the field)
>        * `> [!analogy]` / `> [!example]` (To clarify complex points)
>        * `> [!equation]` (If the topic is technical/mathematical)
>        * `> [NOT-a-callout]` (Use `PC_Style-Quote_Integration` to embed `> [!quote]` and `> [!cite]` callouts where the author's voice is critical.)
>
> **4. Phase 3: PKB Integration & Exploration (The "New Avenues")**
>    * **Goal:** This phase fulfills the "discovery" and "connection" requirements.
>    * **Internal Connections:**
>      * `> [!connections-and-links]`
>      * `> Based on the `[EXISTING_CONCEPTS]` provided, explicitly state how this `[TOPIC]` connects to, expands upon, or challenges `[[Concept A]]` and `[[Theory B]]`."
>    * **External Exploration:**
>      * `> [!further-exploration]`
>      * `> Generate a list of 3-5 *new* topics, concepts, or questions that emerged from this report. These are "new avenues" for me to explore.`
>      * For each new avenue, format it as a `> [!topic-idea]` callout with a `[[New Wiki-Link]]`.
>
> **5. Phase 4: Synthesis & Reflection**
>    * **Summary:** Conclude with a `> [!summary]` callout, synthesizing the *most important* insights.
>    * **Prompt Reflection:**
>      * `> [!ask-yourself-this]`
>      * `> Generate 2-3 provocative questions for me (the user) to reflect on, based on this report.`
>
> **6. Phase 5: Metadata & Constraints**
>    * Apply `PC_Format-Enriched_YAML`, `PC_Format-PKB_Linking`, and `PC_Constraint-Demand_Depth_No_SummarIES`.

# 💡 Usage Guide
This is your primary scaffold for learning a new, complex subject from scratch. It is designed to be the "first-pass" foundational note, from which many other, more atomic notes (identified in `> [!further-exploration]`) will be created.

# 🔗 Relations
* **Pairs With:** `PC_Persona-Academic_Professor`, `PC_Persona-Conceptual_Explainer`, `PC_Format-Enriched_YAML`, `PC_Format-PKB_Linking`, `PC_Format-Semantic_Callouts`, `PC_Style-Quote_Integration`
* **Generates Work For:** `SS_Literature-Note-Creator` (by identifying new topics to research)