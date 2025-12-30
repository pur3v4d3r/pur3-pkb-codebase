---
type: "component"
component-type: "instruction"
atomic-composite: "composite"
domain: "educational"
id: "20251220143000"
status: "active"
version: "1.0.0"
rating: "0.0"
performance-score: "0.0"
source: "original"
created: "2025-12-20"
modified: "2025-12-20"
usage-count: 0
last-used: ""
confidence: "established"
maturity: "evergreen"
tags:
  - "year/2025"
  - "prompt-engineering/component"
  - "component-type/instruction"
  - "domain/educational"
  - "pkb-operations"
  - "foundational-learning"
  - "comprehensive-exposition"
aliases:
  - "Foundational Report Scaffold"
  - "Deep Exposition Framework"
  - "Encyclopedic Learning Template"
  - "First-Pass Research Structure"
link-up: "[[prompt-engineering-moc]]"
conflicts-with: []
synergies-with:
  - "[[PC_Persona-Academic_Professor]]"
  - "[[PC_Persona-Conceptual_Explainer]]"
  - "[[PC_Format-Enriched_YAML]]"
  - "[[PC_Format-PKB_Linking]]"
  - "[[PC_Format-Semantic_Callouts]]"
  - "[[PC_Style-Quote_Integration]]"
used-in-prompts: []
---

> [!usage] Component Template Usage
> **Purpose**: Generate comprehensive, foundational research notes that serve as entry points for learning new complex subjects.
>
> **This is your primary scaffold for learning a new, complex subject from scratch.**

[Component Created: [[2025-12-20|Friday, December 20th, 2025]]]

---

# Instruction: Foundational Report Scaffold (Deep Exposition)

> [!definition] Component Definition
> A multi-phase instructional framework that guides LLMs to produce encyclopedic, foundational research notes with deep exposition, semantic enrichment, PKB integration, and discovery pathways for complex topics.

## 🎯 When to Use

- Learning a completely new subject area from scratch (first-pass research)
- Creating comprehensive foundational notes that spawn multiple atomic notes
- Building "hub" notes that connect to existing PKB knowledge
- Requiring encyclopedic depth with semantic structure (not just summaries)
- Establishing conceptual foundations before specialized deep-dives
- Mapping out "what I don't know" about a broad topic systematically
- Generating discovery pathways (identifying new avenues for exploration)

## 🚫 When NOT to Use

- Quick factual lookups or definitions (use atomic note templates instead)
- Technical how-to guides or procedural documentation (use process templates)
- Synthesis of already-understood concepts (use synthesis note templates)
- Literature note creation from specific sources (use literature note scaffolds)
- Project-specific documentation (use project hub templates)
- When you need concise summaries rather than deep exposition
- For topics where you already have substantial existing notes (use synthesis instead)

---

## 📝 COMPONENT TEXT
```prompt
**Structural Scaffold: Foundational Report (Deep Exposition)**

**1. Define Core Parameters:**
   * **[TOPIC]:** {{Specify the central topic, concept, or question}}
   * **[DEPTH_LEVEL]:** {{e.g., "Encyclopedic overview," "In-depth technical analysis," "Historical context"}}
   * **[EXISTING_CONCEPTS]:** {{(Optional) Provide a list of `[[wikilinks]]` from your vault that you want to connect this topic to. Example: `[[Concept A]]`, `[[Theory B]]`}}

**2. Phase 1: Overture & Foundation (The "Why & What")**
   * **Abstract:** Start with a `> [!abstract]` callout. Provide a high-level, 1-2 paragraph summary of the entire topic.
   * **Definition:** Provide a clear, unambiguous `> [!definition]` of the `[TOPIC]`.
   * **Core Principles:** Explain the "big picture." What is the fundamental idea?
     * Use `> [!the-philosophy]` or `> [!core-principle]` callouts
     * Address: What is the central problem this topic addresses or the core phenomenon it describes?

**3. Phase 2: Encyclopedic Exposition (The "Deep Dive")**
   * **Deconstruction:** Break the `[TOPIC]` down into its logical, primary sub-headings (e.g., History, Mechanism, Key Figures, Sub-types, Implications).
   * **Detailed Prose (Per Sub-Heading):** For *each* sub-heading, write extensive, detailed, and high-quality prose.
   * **Semantic Enrichment:** As you write, actively use the following callouts to structure the information:
       * `> [!atomic-concept]` (For breaking out a small, singular idea)
       * `> [!key-claim]` (For stating a central assertion)
       * `> [!evidence]` (To provide data, studies, or proof for a claim)
       * `> [!argument]` / `> [!counter-argument]` (To explore debates within the field)
       * `> [!analogy]` / `> [!example]` (To clarify complex points)
       * `> [!equation]` (If the topic is technical/mathematical)
       * Embed `> [!quote]` and `> [!cite]` callouts where the author's voice is critical

**4. Phase 3: PKB Integration & Exploration (The "New Avenues")**
   * **Goal:** This phase fulfills the "discovery" and "connection" requirements.
   * **Internal Connections:**
     * Use `> [!connections-and-links]` callout
     * Based on the `[EXISTING_CONCEPTS]` provided, explicitly state how this `[TOPIC]` connects to, expands upon, or challenges the existing concepts
   * **External Exploration:**
     * Use `> [!further-exploration]` callout
     * Generate a list of 3-5 *new* topics, concepts, or questions that emerged from this report
     * These are "new avenues" for future exploration
     * For each new avenue, format it as a `> [!topic-idea]` callout with a `[[New Wiki-Link]]`

**5. Phase 4: Synthesis & Reflection**
   * **Summary:** Conclude with a `> [!summary]` callout, synthesizing the *most important* insights
   * **Prompt Reflection:**
     * Use `> [!ask-yourself-this]` callout
     * Generate 2-3 provocative questions for reflection, based on this report

**6. Phase 5: Metadata & Constraints**
   * Generate appropriate YAML frontmatter with tags and aliases
   * Ensure all key concepts are formatted as `[[Wiki-Links]]`
   * Apply semantic callouts throughout
   * CRITICAL: Demand depth - no summaries, only comprehensive exposition
```

---

## 🔀 VARIATIONS

### Variation 1: Technical/Mathematical Focus
```prompt
**Structural Scaffold: Foundational Report (Technical Deep Dive)**

**1. Define Core Parameters:**
   * **[TECHNICAL_TOPIC]:** {{Specify the technical/mathematical subject}}
   * **[FORMALISM_LEVEL]:** {{e.g., "Rigorous mathematical," "Conceptual with equations," "Applied focus"}}
   * **[PREREQUISITES]:** {{List required background: `[[Linear Algebra]]`, `[[Calculus]]`}}

**2. Phase 1: Foundation**
   * **Abstract:** Provide technical overview in `> [!abstract]`
   * **Formal Definition:** Use `> [!definition]` with mathematical notation
   * **Prerequisites Map:** `> [!prerequisite]` callout listing required concepts

**3. Phase 2: Technical Exposition**
   * **Mathematical Framework:** Present core equations with `> [!equation]` callouts
   * **Proofs & Derivations:** Use `> [!proof]` callouts for formal arguments
   * **Worked Examples:** Extensive `> [!example]` with step-by-step solutions
   * **Edge Cases:** Document with `> [!warning]` or `> [!counter-example]`

**4. Phase 3: Applications & Implementation**
   * **Algorithmic Details:** `> [!methodology-and-sources]` for procedures
   * **Code Examples:** Properly fenced code blocks with explanations
   * **Computational Complexity:** Analysis with `> [!technical-note]`

**5. Phase 4: PKB Integration**
   * **Theory Connections:** Link to `[[Theoretical Foundations]]`
   * **Applied Pathways:** `> [!further-exploration]` for implementation topics
   * **Advanced Extensions:** `> [!topic-idea]` for graduate-level topics

**6. Metadata:**
   * Tags: #technical-reference #mathematical-foundations
   * Inline fields for theorem names, complexity bounds
```

### Variation 2: Historical/Contextual Focus
```prompt
**Structural Scaffold: Foundational Report (Historical Context)**

**1. Define Core Parameters:**
   * **[HISTORICAL_TOPIC]:** {{Specify the subject with temporal scope}}
   * **[TIME_PERIOD]:** {{e.g., "Ancient to modern," "20th century," "Last decade"}}
   * **[NARRATIVE_STYLE]:** {{e.g., "Chronological," "Thematic," "Biographical"}}

**2. Phase 1: Historical Foundation**
   * **Abstract:** Historical overview in `> [!abstract]`
   * **Timeline:** Major periods and turning points
   * **Context:** `> [!context]` for social/political/technological environment

**3. Phase 2: Historical Exposition**
   * **Chronological Development:** Organize by eras/periods
   * **Key Figures:** `> [!biographical-note]` for important contributors
   * **Primary Sources:** `> [!quote]` with `> [!cite]` from original texts
   * **Debates & Interpretations:** `> [!argument]` vs `> [!counter-argument]`

**4. Phase 3: Legacy & Impact**
   * **Modern Relevance:** How history informs present
   * **Historiographical Debates:** `> [!scholarly-debate]`
   * **Connections:** Link to `[[Modern Developments]]`

**5. Phase 4: Exploration Pathways**
   * **Further Reading:** `> [!references]` with primary/secondary sources
   * **Related Topics:** `> [!topic-idea]` for adjacent historical questions

**6. Metadata:**
   * Tags: #historical-context #intellectual-history
   * Inline fields for dates, figures, sources
```

### Variation 3: Comparative Analysis Focus
```prompt
**Structural Scaffold: Foundational Report (Comparative Analysis)**

**1. Define Core Parameters:**
   * **[COMPARATIVE_TOPIC]:** {{e.g., "Behaviorism vs Constructivism"}}
   * **[COMPARISON_DIMENSIONS]:** {{e.g., "Theory, Application, Evidence, Limitations"}}
   * **[SYNTHESIS_GOAL]:** {{e.g., "Integration," "Selection criteria," "Complementary usage"}}

**2. Phase 1: Framework Setup**
   * **Abstract:** Overview of comparison in `> [!abstract]`
   * **Definitions:** Separate `> [!definition]` for each approach
   * **Comparison Matrix:** Table outlining key dimensions

**3. Phase 2: Deep Comparison**
   * **Dimension-by-Dimension Analysis:**
     * For each dimension, use `> [!comparison]` callout
     * Present both approaches fairly
     * Include `> [!evidence]` supporting each
   * **Strengths & Limitations:**
     * `> [!success]` for validated applications
     * `> [!failure]` for documented shortcomings

**4. Phase 3: Integration & Selection**
   * **When to Use What:** `> [!decision-criteria]`
   * **Synthesis Opportunities:** `> [!synthesis-potential]`
   * **Complementary Usage:** How approaches can combine

**5. Phase 4: Exploration**
   * **Alternative Approaches:** `> [!topic-idea]` for third options
   * **Hybrid Frameworks:** `> [!further-exploration]` for integrative work

**6. Metadata:**
   * Tags: #comparative-analysis #framework-evaluation
   * Inline fields for decision criteria
```

---

## 🧩 COMPOSITION

**Atomic Components:**
- [[PC_Format-Enriched_YAML]] - Metadata generation
- [[PC_Format-PKB_Linking]] - Wiki-link integration
- [[PC_Format-Semantic_Callouts]] - Callout taxonomy application
- [[PC_Style-Quote_Integration]] - Source attribution
- [[PC_Constraint-Demand_Depth_No_SummarIES]] - Depth enforcement
- [[PC_Instruction-Phase_Based_Workflow]] - Multi-phase structure
- [[PC_Instruction-Discovery_Pathway_Generation]] - Exploration topics

**Composition Pattern:**
1. **Sequential Phases:** 5 distinct phases executed in order (Foundation → Exposition → Integration → Synthesis → Metadata)
2. **Parallel Enrichment:** Within Phase 2, multiple semantic callouts applied simultaneously
3. **Conditional Application:** Phase 3 connections conditional on `[EXISTING_CONCEPTS]` provided
4. **Feedback Loop:** Phase 4 reflection informs Phase 3 discovery pathways
5. **Meta-Layer:** Phase 5 metadata wraps entire output

---

## 🤝 RELATIONSHIPS

### Works Well With

- **[[PC_Persona-Academic_Professor]]** - Elevates tone to scholarly rigor, enhances credibility of encyclopedic exposition
- **[[PC_Persona-Conceptual_Explainer]]** - Ensures clarity in complex sections, prevents jargon overload
- **[[PC_Format-Enriched_YAML]]** - Provides metadata structure for Phase 5, enables vault-wide queries
- **[[PC_Format-PKB_Linking]]** - Operationalizes Phase 3 integration, strengthens knowledge graph
- **[[PC_Format-Semantic_Callouts]]** - Powers Phase 2 semantic enrichment, creates scannable structure
- **[[PC_Style-Quote_Integration]]** - Essential for evidence-based claims in academic/historical variations
- **[[PC_Constraint-Demand_Depth_No_SummarIES]]** - Enforces core principle of comprehensive exposition

### Conflicts With

- **[[PC_Format-Concise_Summary]]** - Directly contradicts depth mandate, produces superficial output
- **[[PC_Constraint-Maximum_500_Words]]** - Length restriction incompatible with encyclopedic scope
- **[[PC_Style-Bullet_Point_Only]]** - Undermines prose-based exposition requirement
- **[[PC_Persona-Casual_Friend]]** - Tone mismatch with scholarly foundational research
- **[[PC_Instruction-Quick_Reference]]** - Purpose mismatch (reference vs foundational learning)

---

## 📊 PERFORMANCE DATA

### Usage Statistics
- **Total Uses**: `VIEW[{usage-count}]`
- **Last Used**: `VIEW[{last-used}]`
- **Performance Score**: `VIEW[{performance-score}]`/10
- **Average Rating in Prompts**: [Calculate from used-in-prompts]

### Test Results

#### Test 1: Cognitive Load Theory (Educational Psychology)
**Date**: Pending first use
**Prompt Used In**: [[prompt-link]]
**Quality Score**: /10
**Notes**: Initial test should evaluate:
- Depth of encyclopedic coverage
- Quality of discovery pathways generated
- Effectiveness of PKB integration
- Callout density and semantic appropriateness

---

## 💡 USAGE EXAMPLES

### Example 1: Learning Quantum Computing Fundamentals

**Context**: User with computer science background wants to learn quantum computing from scratch. Has existing notes on [[Linear Algebra]], [[Probability Theory]], and [[Classical Computing]].

**Full Prompt**:
```
You are an academic professor specializing in quantum computing education.

Use the Foundational Report Scaffold to create a comprehensive introduction to quantum computing.

[TOPIC]: Quantum Computing Fundamentals
[DEPTH_LEVEL]: Encyclopedic overview with mathematical foundations
[EXISTING_CONCEPTS]: [[Linear Algebra]], [[Probability Theory]], [[Classical Computing]], [[Information Theory]]

Follow all 5 phases meticulously. In Phase 2, ensure you cover:
- Historical development
- Quantum mechanics foundations (qubits, superposition, entanglement)
- Quantum gates and circuits
- Quantum algorithms (conceptual)
- Hardware implementations (overview)
- Current limitations

In Phase 3, explicitly connect to my existing notes on linear algebra (vector spaces for quantum states) and classical computing (comparison of computational models).

Generate at least 5 discovery pathways in Phase 4 for topics like specific quantum algorithms, quantum error correction, quantum cryptography, etc.
```

**Outcome**: 
- 8,000+ word foundational report
- 25+ wiki-links to existing and new concepts
- 15+ semantic callouts organizing content
- 5 discovery pathways identified:
  - [[Shor's Algorithm]] (factorization)
  - [[Grover's Algorithm]] (search)
  - [[Quantum Error Correction Codes]]
  - [[Quantum Cryptography and BB84]]
  - [[Topological Quantum Computing]]
- Explicit connections showing how linear algebra concepts map to quantum state representations

**Effectiveness**: ⭐⭐⭐⭐⭐

---

### Example 2: Comparative Analysis of Learning Theories

**Context**: Educator building PKB on pedagogical approaches. Wants comprehensive comparison to inform teaching practice.

**Full Prompt**:
```
You are a conceptual explainer with expertise in educational theory.

Use the Foundational Report Scaffold (Comparative Analysis Variation) to analyze major learning theories.

[COMPARATIVE_TOPIC]: Behaviorism vs Cognitivism vs Constructivism
[COMPARISON_DIMENSIONS]: Theoretical foundations, View of learner, Instructional methods, Evidence base, Limitations, Modern applications
[SYNTHESIS_GOAL]: Develop selection criteria for when to apply each approach

[EXISTING_CONCEPTS]: [[Cognitive Load Theory]], [[Metacognition]], [[Self-Determination Theory]]

Ensure Phase 2 includes:
- Fair representation of each theory's strengths
- Evidence from empirical research (use quote integration)
- Documented limitations and criticisms

In Phase 4, generate provocative questions about integrative frameworks and hybrid approaches.
```

**Outcome**:
- Comprehensive comparison matrix across 6 dimensions
- Evidence-based analysis with 12+ cited sources
- Decision criteria for instructional design contexts
- 4 synthesis pathways identified:
  - [[Cognitive-Behavioral Integration in Education]]
  - [[Situated Cognition Theory]]
  - [[Communities of Practice]]
  - [[Technology-Enhanced Constructivism]]

**Effectiveness**: ⭐⭐⭐⭐⭐

---

## 📗 USED IN PROMPTS
```dataview
TABLE status, rating, usage-count, last-used
FROM ""
WHERE type = "prompt" AND contains(components-used, this.file.link)
SORT rating DESC
LIMIT 10
```

### Manual Links
- [[Prompt: Quantum Computing Foundations]] (hypothetical)
- [[Prompt: Learning Theory Comparison]] (hypothetical)

---

## 🔧 OPTIMIZATION HISTORY

### Version 1.0.0 - 2025-12-20
**Changes**: Initial creation from existing scaffold documentation
**Impact**: Baseline established. Formalized structure enables systematic testing and iteration.

---

## 🎓 LESSONS LEARNED

- **Phase sequencing matters**: Foundation → Exposition → Integration → Synthesis creates natural knowledge building progression
- **Discovery pathways are critical**: Phase 3's `[!further-exploration]` prevents "dead-end" learning - always generates next steps
- **Semantic callout density**: Target 12-20 callouts for comprehensive reports to maintain scannability without overwhelming
- **Variation adaptation**: Technical/Historical/Comparative variations show scaffold is flexible framework, not rigid template
- **Depth enforcement essential**: Without explicit "no summaries" constraint, LLMs default to shallow coverage even with detailed scaffold
- **PKB integration needs explicit prompting**: Phase 3's `[EXISTING_CONCEPTS]` parameter crucial - without it, notes become isolated islands
- **Reflection questions underutilized**: Phase 4's `[!ask-yourself-this]` often generates generic questions - needs refinement for provocation
- **Metadata generation timing**: Phase 5 placement ensures tags/aliases reflect actual content generated, not assumed content

---

## 📚 REFERENCES

- [[Zettelkasten Methodology]] - Atomic note spawning principle informs Phase 3 discovery pathways
- [[Progressive Summarization]] - Anti-pattern reference (this scaffold explicitly rejects summarization approach)
- [[Evergreen Note Principles]] - Foundational reports serve as "hub" evergreen notes
- [[Chain-of-Density Prompting]] - Layered exposition approach in Phase 2
- Anthropic's Constitutional AI - Multi-phase structure inspired by constitutional prompting patterns
- Cognitive Load Theory - Semantic callout organization reduces extraneous load during review

---

*Component Template Version: 1.0.0 | Created: 2025-12-20*