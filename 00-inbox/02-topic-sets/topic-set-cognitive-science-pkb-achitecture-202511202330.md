---
title: "Cognitive Science × PKB Architecture: Integration Topics"
id: 20251120-233059
type: ✍️topics
status: ⚡active
rating: ""
source: RSAC-v2.0🆔20251020224705
url: ""
tags:
  - cognitive-science
  - pkm
  - learning-theory
  - knowledge-work
  - information-architecture
  - knowledge-workflow
  - pkb/design/information-architecture
  - pkb/architecture
  - pkm/theory
  - pkm/workflow
aliases:
  - Cognitive PKM Design
  - Science-Based Knowledge Management
  - Cognitive Architecture for PKB
link-up: "[[✍️Topics_🗺️MOC]]"
link-related:
  -
---


---
aliases: [Cognitive PKM Design, Science-Based Knowledge Management, Cognitive Architecture for PKB]
---

# Cognitive Science × PKB Architecture: Integration Topics

The intersection of [[Cognitive Science]] and [[03-notes/01_permanent-notes/02_personal-knowledge-base/Personal Knowledge Management]] represents one of the most fertile grounds for systematic PKB improvement. Your refactoring goal—to embed cognitive principles into the foundational architecture—moves beyond superficial organization toward designing a system that genuinely extends and complements human cognition rather than fighting against it.

> [!principle-point] Core Insight: Cognitive Alignment Principle
> An effective PKB should reduce [[Cognitive Load]], support [[Schema Formation]], enable [[Metacognition]], and scaffold [[Self-Regulated Learning]]. The architecture itself becomes an external cognitive artifact that compensates for working memory limitations while amplifying long-term memory consolidation.

## 🧠 Essential Integration Topics

### 1. **[[Working Memory Architecture in Note Design]]**

> [!key-claim] Design Constraint from Cognitive Science
> [[Working Memory]] has a capacity limit of approximately 4±1 chunks for novel information (Cowan, 2001), with traditional estimates of 7±2 now considered inflated. This isn't a flaw—it's a design specification for your PKB.

**The Cognitive Principle**: Working memory acts as the cognitive bottleneck between perception and long-term storage. Information must be processed through this limited-capacity system before meaningful encoding occurs. [[Chunking]] allows us to compress multiple elements into single meaningful units, effectively expanding functional capacity.

**PKB Application Architecture**:
- **Atomic Note Sizing**: Each note should contain one conceptual "chunk" that can be held entirely in working memory during processing
- **Progressive Disclosure Systems**: Use folded sections, transclusion, or linked elaboration rather than massive monolithic notes
- **Cognitive Load Indicators**: Develop a tagging system that signals processing complexity (#high-cognitive-load, #requires-prerequisites, #multi-step-reasoning)
- **Interleaving Structure**: Design MOCs and index notes that present 3-5 items at once, preventing working memory overflow during navigation

> [!methodology-and-sources] Implementation Pattern: The 4-Chunk Rule
> When creating reference notes or MOCs, structure information into 4 major sections/themes. This aligns with working memory capacity and makes the entire note's architecture graspable in a single cognitive load. Sub-sections can elaborate, but the top-level structure should be immediately comprehensible.

> [!example] Practical Application
> Instead of a massive "Machine Learning" note with 20 subsections, create:
> - [[Machine Learning - Core Paradigms]] (4 main approaches)
> - [[Machine Learning - Mathematical Foundations]] (4 key concepts)
> - [[Machine Learning - Practical Implementation]] (4 workflow stages)
> Each becomes a manageable cognitive chunk, with an MOC linking them.

### 2. **[[Desirable Difficulties and Retrieval Practice Design]]**

> [!principle-point] The Retrieval Paradox
> Making information *harder* to retrieve (within limits) actually strengthens long-term retention. This insight from [[Cognitive Psychology]] fundamentally challenges typical PKB design that prioritizes frictionless access.

**The Cognitive Principle**: [[Retrieval Practice]] (testing effect) and [[Desirable Difficulties]] create stronger memory traces than passive review. The cognitive effort required during retrieval strengthens neural pathways. [[Bjork's Desirable Difficulties Framework]] suggests optimal learning involves appropriate challenges during encoding and retrieval.

**PKB Application Architecture**:
- **Spaced Retrieval Systems**: Implement spaced repetition not just for flashcards, but for note review cycles (perhaps using Dataview queries with date calculations)
- **Generative Note Prompts**: Create "question notes" that require you to synthesize answers from multiple sources before checking your linked answer note
- **Interleaved Topic Organization**: Mix related but distinct concepts in MOCs rather than blocking identical types together (challenges discrimination abilities)
- **Reduced Visual Scaffolding**: Occasional use of links without preview text forces active recall of destination content
- **Elaborative Interrogation Templates**: Design note templates that require you to answer "why" and "how" questions, not just record facts

> [!methodology-and-sources] Implementation Pattern: Active Reconstruction Protocol
> When reviewing important notes, close them and attempt to recreate the core structure from memory in a temporary note. Compare afterward. The reconstruction effort—even with errors—produces stronger encoding than passive re-reading.

> [!counter-argument] Balance Required
> While desirable difficulties enhance learning, excessive friction creates frustration without benefit. The goal is *appropriate* challenge during retrieval, not arbitrary obstacles. Monitor your cognitive response: productive struggle feels effortful but engaging; unproductive struggle feels blocked and frustrating.

### 3. **[[Schema Theory and MOC Architecture]]**

> [!definition] Schema
> In cognitive science, a [[Schema]] is an organized pattern of thought or behavior that organizes information and relationships among information. Schemas act as mental frameworks that help us interpret new information in relation to existing knowledge structures.

**The Cognitive Principle**: [[Schema Theory]] (Bartlett, Piaget, later Anderson) proposes that learning involves integrating new information into existing cognitive structures. Well-developed schemas enable: (1) faster information processing, (2) better inference-making, (3) enhanced memory through meaningful organization, and (4) transfer of knowledge to novel situations.

**PKB Application Architecture**:
- **MOCs as External Schemas**: Design your [[Maps of Content]] to mirror the hierarchical, interconnected nature of cognitive schemas rather than arbitrary categorical filing
- **Schema Elaboration Patterns**: Create "schema development notes" that explicitly track how your understanding structure evolved over time
- **Progressive Formalization**: Start with loosely connected notes (schema formation), gradually develop stronger organizational principles (schema refinement), eventually create formal MOCs (mature schemas)
- **Cross-Schema Linking**: Actively create connections between different MOCs to represent how schemas interact in cognition
- **Schema Violation Tracking**: Maintain notes about when new information contradicted your existing mental models (these are learning opportunities)

> [!analogy] The Building Metaphor
> Schemas are like architectural frameworks. Individual notes are bricks. MOCs are blueprints showing how bricks relate. Without the blueprint (MOC/schema), you have a pile of bricks. Without the bricks (atomic notes), you have an empty framework. Both must co-evolve.

> [!example] Multi-Level Schema Implementation
> For your cognitive science study:
> - **Level 1 Schema**: [[Cognitive Science MOC]] - Broad domains (perception, memory, learning, reasoning)
> - **Level 2 Schemas**: [[Memory Systems MOC]], [[Learning Theories MOC]] - Specialized areas
> - **Level 3 Schemas**: [[Working Memory Models MOC]], [[Long-Term Memory Consolidation MOC]] - Specific phenomena
> - **Atomic Notes**: Individual concepts, studies, principles
> Each level represents increasing specialization, mirroring how expert schemas develop.

### 4. **[[Dual Coding Theory and Multimodal Note Design]]**

**The Cognitive Principle**: [[Dual Coding Theory]] (Paivio) demonstrates that information encoded both verbally and visually produces stronger, more accessible memories than either alone. The brain processes linguistic and visual information through partially independent channels, allowing parallel encoding without channel interference.

**PKB Application Architecture**:
- **Systematic Diagram Integration**: Develop protocols for adding visual representations (Mermaid diagrams, concept maps, flow charts) to verbal explanations
- **Visual-Verbal Templates**: Create note templates requiring both text explanation and visual model
- **Icon and Emoji Semantics**: Use consistent visual markers as secondary encoding (⚙️ for processes, 🔗 for connections, 💡 for insights)
- **Sketch-to-Digital Workflow**: Maintain a system for capturing hand-drawn concept sketches and integrating them into formal notes
- **Metaphor and Analogy Banks**: Systematically collect visual metaphors for abstract concepts (stored as reusable blocks)

> [!helpful-tip] Implementation Strategy
> When learning complex abstract concepts (like theoretical frameworks in cognitive science), create companion visual notes using Mermaid or Excalidraw. The act of translating verbal to visual representation forces deeper processing and creates dual retrieval pathways.

### 5. **[[Metacognitive Monitoring Systems]]**

> [!key-claim] Self-Knowledge as Knowledge Management
> Effective [[Self-Regulated Learning]] requires accurate [[Metacognition]]—awareness of what you know, what you don't know, and how well you're learning. Your PKB should function as an external metacognitive tool.

**The Cognitive Principle**: [[Metacognition]] involves monitoring and controlling cognitive processes. Research on [[Judgments of Learning]], [[Metacomprehension]], and [[Self-Regulated Learning]] (Zimmerman, Winne & Hadwin) shows that effective learners actively monitor their understanding and adjust strategies accordingly.

**PKB Application Architecture**:
- **Confidence Tagging**: Add metadata indicating certainty levels (#confident-understanding, #partial-grasp, #confused-needs-review)
- **Comprehension Check Notes**: Create dedicated notes asking "What don't I understand yet about [[Topic]]?" Updated as understanding evolves
- **Learning Strategy Logs**: Maintain meta-notes tracking which note-taking approaches worked well for different content types
- **Error Documentation**: Systematically record misconceptions and corrected understandings (invaluable for identifying knowledge gaps)
- **Progress Visualization**: Use Dataview queries to track notes by confidence level, review frequency, or connection density
- **Pre-Study Predictions**: Before deep-diving into a topic, create a note predicting what you'll learn; compare afterward to calibrate metacognitive accuracy

> [!methodology-and-sources] Implementation Pattern: The Three-Phase Review Protocol
> **Phase 1 - Self-Test**: Before opening a note, write down everything you remember about the topic
> **Phase 2 - Comparison**: Open the note and identify gaps, errors, and surprises
> **Phase 3 - Metacognitive Update**: Add tags/comments about what you overestimated knowing vs. what you actually retained

### 6. **[[Cognitive Load Management in Hierarchy Design]]**

**The Cognitive Principle**: [[Cognitive Load Theory]] (Sweller) distinguishes between three types of load: [[Intrinsic Load]] (inherent complexity), [[Extraneous Load]] (poorly designed presentation), and [[Germane Load]] (productive processing). Effective instructional design minimizes extraneous load while optimizing germane load appropriate to learner expertise.

**PKB Application Architecture**:
- **Expertise-Adaptive Structure**: Organize notes differently for learning vs. expert reference (learners need more scaffolding, experts need dense interconnection)
- **Worked Example Progressions**: In technical notes, provide fully worked examples before problem sets (reduces intrinsic load during skill acquisition)
- **Coherent Visual Design**: Maintain consistent formatting to reduce extraneous load from unpredictable presentation
- **Segmentation Principle**: Break complex explanations into separately navigable segments rather than continuous scrolling
- **Pre-Training Notes**: Create prerequisite concept notes that reduce intrinsic load of advanced topics by building foundational schemas first
- **Eliminate Redundancy**: Remove duplicate information across notes (split-attention effect) unless serving spaced repetition purposes

> [!warning] The Expertise Reversal Effect
> Note structures that help novices can actually hinder experts. Your PKB design should evolve as your expertise develops. Early-stage notes need more scaffolding; advanced notes benefit from density and assumption of prior knowledge.

### 7. **[[Transfer-Oriented Knowledge Structuring]]**

**The Cognitive Principle**: [[Transfer of Learning]]—applying knowledge to novel contexts—is the ultimate goal of education but notoriously difficult. Research on [[Near Transfer vs. Far Transfer]] shows that abstract principles and varied contextual exposure enhance transferability.

**PKB Application Architecture**:
- **Principle Extraction Notes**: For every concrete example or case study, create a separate note extracting the abstract principle
- **Multiple Context Linking**: Connect the same principle to 3+ different application domains
- **Analogical Reasoning Templates**: Systematically map similarities and differences between domains to strengthen abstract understanding
- **Problem-Solution Pattern Libraries**: Maintain notes organizing recurring solution patterns across different problems
- **Cross-Domain MOCs**: Create synthetic MOCs that deliberately juxtapose concepts from different fields to highlight transferable patterns

> [!example] Transfer Architecture in Practice
> Learning about [[Feedback Loops]] in systems thinking? Create:
> - [[Feedback Loops - Abstract Principle]] (domain-independent definition)
> - [[Feedback Loops in Biological Systems]] (homeostasis, hormone regulation)
> - [[Feedback Loops in Software Architecture]] (circuit breakers, rate limiting)
> - [[Feedback Loops in Personal Habits]] (identity reinforcement, environment design)
> - [[Feedback Loops - Cross-Domain MOC]] (links all above, highlights transferable patterns)

### 8. **[[Constructivist Note Evolution Protocols]]**

> [!principle-point] Knowledge as Construction
> [[Constructivist Learning Theory]] (Piaget, Vygotsky, von Glasersfeld) posits that learners actively construct understanding rather than passively receiving information. This has profound implications for how notes should evolve.

**The Cognitive Principle**: Constructivism emphasizes that learning is an active process of building mental models through interaction with information, reflection, and social discourse. [[Zone Of Proximal Development]] (Vygotsky) suggests optimal learning occurs just beyond current independent capability with appropriate scaffolding.

**PKB Application Architecture**:
- **Version-Tracked Evolution**: Use git or date-stamped sections to preserve how your understanding changed over time
- **Dialogue Notes**: Record arguments between different theoretical perspectives you're working to reconcile
- **Socratic Question Chains**: Embed progressive questioning in notes to guide future review sessions
- **Scaffolding Removal Protocol**: Periodically remove explanatory scaffolding from mature notes to test independent understanding
- **Uncertainty Markers**: Flag areas of active knowledge construction with tags like #developing-understanding or #synthesis-in-progress
- **Collaborative Construction**: If engaging in social learning, maintain shared notes showing how group understanding evolved

> [!methodology-and-sources] Implementation Pattern: The Iterative Deepening Cycle
> **First Pass** (Initial Encounter): Create simple definition note with basic understanding
> **Second Pass** (Elaboration): Add examples, connections, questions
> **Third Pass** (Integration): Link to related concepts, identify patterns
> **Fourth Pass** (Transformation): Restructure note based on deeper understanding, potentially split into atomic concepts
> **Fifth Pass** (Teaching): Rewrite note as if explaining to others—this reveals gaps

### 9. **[[Self-Determination Theory and Intrinsic Motivation Design]]**

**The Cognitive Principle**: [[Self-Determination Theory]] (Deci & Ryan) identifies three psychological needs crucial for intrinsic motivation: [[Autonomy]] (sense of control), [[Competence]] (feeling effective), and [[Relatedness]] (connection to others/purposes). When these needs are satisfied, engagement and learning quality increase dramatically.

**PKB Application Architecture**:
- **Autonomy Support**: Design flexible organizational systems allowing multiple valid structures (tags, folders, links) rather than rigid hierarchies
- **Competence Indicators**: Implement progress tracking that shows growing mastery (connection counts, concept depth metrics, review success rates)
- **Personal Relevance Linking**: Explicitly connect abstract concepts to personal goals, projects, or curiosities
- **Curiosity-Driven Navigation**: Create "mystery notes" or "question collections" that intrigue you, pulling you into exploration rather than pushing obligation
- **Achievement Systems**: Consider implementing personal "learning quests" or challenges within your PKB
- **Relatedness Through Synthesis**: Frame learning as conversation with thinkers you admire (dialogue with authors via annotations)

> [!helpful-tip] Motivation Architecture
> Structure your PKB workflow to answer intrinsically motivating questions like:
> - "What surprising connections can I discover today?"
> - "How does this make me more capable?"
> - "What does this help me create/understand/achieve?"
> Rather than extrinsically motivated tasks like "Review 20 flashcards."

### 10. **[[Interleaving and Spacing in Review Workflows]]**

**The Cognitive Principle**: Research on [[Spacing Effect]] (Ebbinghaus, continued by Cepeda et al.) and [[Interleaving Practice]] demonstrates that distributed practice across time and mixed practice across topics produces better long-term retention than massed or blocked practice, despite feeling less fluent during learning.

**PKB Application Architecture**:
- **Algorithmic Review Scheduling**: Implement Dataview queries that surface notes for review based on expanding intervals (1 day, 3 days, 1 week, 2 weeks, 1 month, 3 months)
- **Cross-Topic Daily Digests**: Create daily review notes that randomly sample 3-5 notes from different domains rather than reviewing topics in blocks
- **Interleaved MOC Organization**: In learning-focused MOCs, order topics by interleaving related concepts rather than grouping all similar items together
- **Temporal Context Variation**: Review the same note in different contexts (morning vs. evening, different physical locations, different surrounding topics)
- **Anti-Cramming Protocols**: Use calendar blocking or task systems to prevent reviewing the same topic too frequently

> [!methodology-and-sources] Implementation Pattern: The 1-3-7-21-90 Review Cadence
> For newly created notes that represent significant learning:
> - **Day 1**: Initial creation + processing
> - **Day 3**: First review (catch immediate misconceptions)
> - **Day 7**: Second review (consolidate into long-term memory)
> - **Day 21**: Third review (strengthen retrieval pathways)
> - **Day 90**: Quarterly review (maintain accessibility)
> 
> Use Dataview to automatically calculate these dates and generate review queues.

### 11. **[[Embodied Cognition and Spatial Note Organization]]**

**The Cognitive Principle**: [[Embodied Cognition]] research demonstrates that physical and spatial reasoning scaffolds abstract thought. [[Method of Loci]], [[Spatial Memory]] advantages, and gesture-enhanced learning all show that leveraging spatial cognition improves information organization and retrieval.

**PKB Application Architecture**:
- **Canvas-Based Knowledge Maps**: Use Obsidian Canvas to create spatial arrangements of notes where physical proximity reflects conceptual relatedness
- **Consistent Spatial Metaphors**: Position certain types of content consistently (foundational concepts at bottom/center, applications at periphery, etc.)
- **Journey-Based MOCs**: Structure MOCs as conceptual "walks" through territory with explicit spatial language ("moving from X to Y," "at the intersection of A and B")
- **Gestural Annotations**: If using tablet input, incorporate handwritten spatial annotations that leverage embodied reasoning
- **3D Knowledge Structures**: Experiment with hierarchical spatial layouts where depth represents abstraction levels

> [!analogy] The Mental Palace Architecture
> Like the ancient [[Method of Loci]] technique, your PKB can function as a "memory palace" where ideas have spatial locations. When you need to retrieve information about [[Cognitive Load Theory]], you don't just search—you navigate to the "Learning Theories wing" of your knowledge palace, "walk" to the "Instructional Design section," and "see" cognitive load theory in its spatial context among related concepts.

### 12. **[[Incremental Reading and Progressive Summarization]]**

**The Cognitive Principle**: [[Incremental Learning]] (Wozniak) involves processing information in small chunks over extended time, allowing each encounter to build on previous understanding. Combined with [[Levels of Processing Theory]] (Craik & Lockhart), which shows deeper processing creates stronger memories, this suggests iterative refinement as optimal.

**PKB Application Architecture**:
- **Five-Layer Processing System**:
  1. **Layer 1 - Capture**: Raw highlights and clippings
  2. **Layer 2 - Bold**: Mark most important passages (first filter)
  3. **Layer 3 - Highlight**: Further refinement to core insights
  4. **Layer 4 - Summary**: Rewrite in your own words
  5. **Layer 5 - Remix**: Integrate into permanent notes, create new connections
- **Incremental Note Queues**: Maintain lists of partially processed notes to revisit systematically
- **Time-Boxing Protocols**: Process each note for only 10-15 minutes per session, returning later with fresh perspective
- **Comprehension Evolution Tracking**: Date-stamp different summary layers to observe how understanding deepened
- **Progressive Linking**: Add connections incrementally—first obvious links, later subtle cross-domain relationships

> [!methodology-and-sources] Implementation Pattern: The Three-Pass Processing Protocol
> **Pass 1 (Extraction)**: Copy important passages from source, minimal editing
> **Pass 2 (Translation)**: Rewrite key points in your own words, identify concepts needing wiki-links
> **Pass 3 (Integration)**: Break apart into atomic notes, create MOC structures, establish cross-references
> Each pass occurs days or weeks apart, allowing unconscious processing and consolidation between sessions.

---

## 🔧 Architectural Implementation Considerations

> [!important] Integration Sequence Strategy
> Don't attempt to implement all principles simultaneously. This creates cognitive overload and architectural paralysis. Instead, use a phased approach:
> 
> **Phase 1 (Foundation)**: Working Memory Architecture + Schema Theory MOCs
> **Phase 2 (Practice)**: Retrieval Practice Design + Spacing Protocols  
> **Phase 3 (Enrichment)**: Dual Coding + Metacognitive Monitoring
> **Phase 4 (Optimization)**: Transfer Structuring + Constructivist Evolution
> **Phase 5 (Motivation)**: Self-Determination elements + Embodied organization

Your refactoring process should itself embody [[Incremental Learning]] principles—systematically improve one architectural element at a time while maintaining a functional system throughout.

> [!example] Concrete Starting Point
> Begin with working memory-informed note sizing. Audit your current reference notes:
> - How many distinct concepts does each contain?
> - Can you hold the entire note structure in working memory while reading?
> - Would splitting into atomic notes improve processing?
> 
> This single change will cascade into improved schema organization, better linking, and reduced cognitive load—foundational for all subsequent improvements.

---

# 🔗 Related Topics for PKB Expansion

1. **[[Cognitive Apprenticeship Models in Self-Directed Learning]]**
   - *Connection*: Bridges the gap between formal cognitive science principles and practical PKB workflow development, addressing how to internalize expert-level knowledge organization practices
   - *Depth Potential*: Exploration of scaffolding, fading, and modeling techniques adapted for solo learning contexts where you function as both apprentice and master
   - *Knowledge Graph Role*: Connects cognitive science learning theories to practical PKB skill development, serving as implementation methodology for theoretical principles

2. **[[Expertise Development Stages and PKB Architecture Evolution]]**
   - *Connection*: As you progress from novice to expert in cognitive science (and in PKM itself), your PKB needs different structures—this topic examines how system design should adapt across expertise levels
   - *Depth Potential*: Integration of [[Dreyfus Model of Skill Acquisition]], [[Adaptive Expertise]] theory, and [[Expertise Reversal Effect]] with concrete PKB transformation strategies
   - *Knowledge Graph Role*: Meta-level topic that informs how all other cognitive science principles should be applied differently based on current knowledge state

3. **[[Cognitive Offloading vs. Cognitive Partnership in External Systems]]**
   - *Connection*: Addresses fundamental question: should your PKB simply store information (offloading) or actively enhance thinking processes (partnership)? Different cognitive science principles support different answers
   - *Depth Potential*: Synthesis of [[Extended Mind Thesis]] (Clark & Chalmers), [[Distributed Cognition]], and [[Cognitive Artifacts]] research with PKB design philosophy
   - *Knowledge Graph Role*: Theoretical foundation that shapes every architectural decision—determines whether you design for retrieval or for thinking augmentation

4. **[[Affective Factors in Long-Term PKB Engagement]]**
   - *Connection*: Cognitive science of learning cannot ignore emotion and motivation; this topic examines [[Affective Neuroscience]] principles for sustaining multi-year PKB practice
   - *Depth Potential*: Integration of [[Emotional Memory Enhancement]], [[Interest Development Theory]], [[Flow State Design]], and [[Self-Determination Theory]] specifically for knowledge work contexts
   - *Knowledge Graph Role*: Addresses the critical sustainability dimension often missing from purely cognitive analyses—bridges to practical long-term system viability

```
<thinking>
Let me analyze this request using the ReAct protocol:

**PHASE 1: ANALYZE**

Request Classification:
- Type: comprehensive_note (the user wants topic recommendations with depth)
- Scope: synthesis (connecting two domains - Cognitive Science and PKB/PKM)
- Research Required: NO - This is within my training knowledge and the user is asking for conceptual connections, not recent developments

Structural Planning:
- Information Architecture: 
  - Introduction contextualizing the intersection
  - Main topics organized by cognitive science domains
  - Each topic should explain the cognitive principle + PKB application
  - Practical implementation considerations
  - Expansion section with 4 related topics

- Wiki-Link Opportunities: 
  - All cognitive science theories mentioned
  - PKM methodologies
  - Specific PKB design patterns
  - Cognitive concepts like working memory, schemas, etc.

- Callout Strategy:
  - [!principle-point] for core cognitive science principles
  - [!methodology-and-sources] for practical PKB applications
  - [!key-claim] for important insights
  - [!example] for concrete illustrations
  - [!analogy] for bridging understanding

- Metadata Planning:
  - Tags: #cognitive-science #pkm #pkb-architecture #synthesis-note #learning-theory
  - Aliases: [Cognitive PKM Design, Science-Based Knowledge Management, Cognitive Architecture for PKB]

The user explicitly mentions they're refactoring their PKB and want to integrate cognitive science principles systematically. They mention specific theories: Self-Determination Theory, Cognitive Load Theory, Constructivist Learning Theory, Self-Regulated Learning, Incremental Learning.

This is definitely a comprehensive request requiring a full synthesis note with metadata header.

**PHASE 2: COMPOSE**

I'll create a comprehensive synthesis note that:
1. Provides meaningful topics at the intersection
2. Explains the cognitive principle
3. Shows practical PKB applications
4. Uses rich wiki-links for knowledge graph building
5. Employs semantic callouts strategically
6. Includes concrete examples
7. Ends with 4 expansion topics

**PHASE 3: VALIDATE**
Pre-output checklist:
- [ ] Metadata header with tags + aliases
- [ ] Key concepts as wiki-links (target: 20-40)
- [ ] Multiple callouts (target: 8-15)
- [ ] Clear header hierarchy
- [ ] Prose-dominant (not just lists)
- [ ] Expansion section with 4 topics
</thinking>
```