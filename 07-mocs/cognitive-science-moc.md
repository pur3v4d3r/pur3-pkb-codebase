---
aliases:
  - Cognitive Science MOC
  - CogSci Knowledge Hub
  - Mind and Brain Studies Map
  - Cognitive Science Index
tags:
  - type/moc
  - year/2025
  - cognitive-science
  - cognitive-psychology
  - neuroscience
  - learning-theory
  - memory-systems
  - executive-function
  - metacognition
  - status/developing
  - context/research
  - context/theoretical
  - nature/conceptual
source: original-synthesis
id: 20251213-cognitive-science-moc
created: 2025-12-13T14:30:00
modified: 2025-12-13T14:30:00
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: moc
maturity: developing
confidence: high
next-review: 2025-12-20
review-count: 0
link-count: 85
backlink-count: 0
cssclass: cognitive-science-moc
link-up:
  - "[[04-library/02-pkb-and-pkm-learning/-reference/-official-documentation/-pkb-frameworks/-imf-advanced-starter-kit/philosophy-moc]]"
  - "[[neuroscience-moc]]"
  - "[[learning-theory-moc]]"
  - "[[psychology-moc]]"
  - "[[educational-psychology-moc]]"
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[cognitive-architecture]]"
  - "[[working-memory]]"
  - "[[cognitive-load-theory]]"
  - "[[executive-function]]"
  - "[[self-regulated-learning]]"
  - "[[dual-process-theory]]"
  - "[[distributed-cognition]]"
  - "[[extended-mind]]"
pillars:
  - Foundational Architecture
  - Memory Systems & Information Processing
  - Attention & Executive Control
  - Development & Learning Processes
  - Metacognition & Self-Regulation
  - Applied Domains & Clinical Integration
total-permanent-notes: 85
domain-keywords:
  - cognition
  - memory
  - attention
  - learning
  - metacognition
  - executive-function
  - neuroplasticity
  - cognitive-development
research-priorities:
  - Sensory Processing & Perception
  - Language & Communication
  - Social Cognition
  - Computational Models
  - Applied Cognitive Ergonomics
---

# Cognitive Science MOC

---
tags: #cognitive-science #moc #knowledge-hub #reference-note
aliases: [Cognitive Science Hub, CogSci MOC, Mind and Brain Studies]
---

> [!abstract] Overview
> This Map of Content serves as the primary navigation hub for **Cognitive Science**—an interdisciplinary field investigating the nature of the mind, brain, and intelligent behavior. [**Cognitive-Science**:: the interdisciplinary study of mind and intelligence, encompassing psychology, neuroscience, philosophy, linguistics, artificial intelligence, and anthropology to understand mental processes like perception, memory, reasoning, and decision-making.]
> 
> The MOC is organized into six core pillars representing major research domains, followed by applied frameworks and cross-cutting themes that integrate cognitive principles with real-world applications.

---

## 🎯 Purpose & Scope

This MOC provides:
- **Conceptual Navigation**: Hierarchical pathways through cognitive science subdomains
- **Integration Points**: Links between theoretical frameworks and practical applications
- **Research Context**: Connections to neuroscience, psychology, philosophy, and learning sciences
- **Applied Knowledge**: Bridges to educational design, clinical interventions, and self-improvement methodologies

> [!important] Navigation Philosophy
> This MOC follows a **hub-and-spoke architecture**: core theoretical concepts anchor the center, with applied frameworks and methodologies radiating outward. Use the semantic bridges section to discover unexpected connections across domains.

---

## 📊 Maturity Dashboard

```dataviewjs
// Aggregate maturity statistics across cognitive science notes
const cogSciPages = dv.pages('#cognitive-science')
    .where(p => p.type !== 'moc');

const maturityCounts = {
    'seedling': 0,
    'budding': 0,
    'developing': 0,
    'evergreen': 0
};

cogSciPages.forEach(p => {
    if (p.maturity && maturityCounts.hasOwnProperty(p.maturity)) {
        maturityCounts[p.maturity]++;
    }
});

const total = Object.values(maturityCounts).reduce((a, b) => a + b, 0);

dv.header(3, "📈 Knowledge Base Maturity");
dv.table(
    ["Maturity Level", "Count", "Percentage"],
    [
        ["🌱 Seedling", maturityCounts.seedling, `${((maturityCounts.seedling/total)*100).toFixed(1)}%`],
        ["🌿 Budding", maturityCounts.budding, `${((maturityCounts.budding/total)*100).toFixed(1)}%`],
        ["🌳 Developing", maturityCounts.developing, `${((maturityCounts.developing/total)*100).toFixed(1)}%`],
        ["🌲 Evergreen", maturityCounts.evergreen, `${((maturityCounts.evergreen/total)*100).toFixed(1)}%`]
    ]
);

dv.paragraph(`**Total Cognitive Science Notes**: ${total}`);
```

---

## 🏛️ Pillar I: Foundational Architecture

> [!principle-point] Core Principle
> [**Cognitive-Architecture**:: the theoretical framework describing the fundamental structures and processes underlying human cognition, including memory systems, attention mechanisms, and computational models of mind.]

### Core Concepts
- [[Cognitive Science]] - Master overview of the field
- [[Cognitive Architecture]] - Structural frameworks of mind
- [[Cognitive Psychology]] - Experimental study of mental processes
- [[Distributed Cognition]] - Cognition as system-level phenomenon
- [[Extended Mind]] - Mind beyond brain boundaries

### Theoretical Models
- [[Dual Process Theory]] - System 1 (automatic) vs System 2 (deliberate)
- [[Signal Detection Theory]] - Decision-making under uncertainty
- [[Information Theory]] - Quantifying information and communication

### Related Systems
- [[Philosophy of Mind]] - Metaphysical foundations
- [[Epistemology]] - Theory of knowledge
- [[Evolutionary Epistemology]] - Evolution of cognitive systems

```dataview
TABLE maturity, confidence, file.ctime as Created
WHERE type = "permanent-note"
SORT maturity DESC, confidence DESC
LIMIT 10
```

---

## 🧠 Pillar II: Memory Systems & Information Processing

> [!definition] Central Framework
> [**Memory-Systems**:: the cognitive architecture dividing memory into multiple interacting subsystems—working memory, long-term memory, episodic memory, semantic memory, and procedural memory—each with distinct properties, capacities, and neural substrates.]

### Primary Memory Systems
- [[Working Memory]] - Active information maintenance
  - [[Long-Term Working Memory]] - Expertise-driven capacity
  - [[Cognitive Load Theory]] - Capacity limitations and optimization
    - [[Intrinsic Load]] - Task complexity
    - [[Extraneous Load]] - Design-imposed burden
    - [[Germane Load]] - Schema construction effort

### Long-Term Storage
- [[Long-Term Memory]] - Permanent knowledge storage
- [[Retrospective Memory]] - Past event recall
- [[Curve Of Forgetting]] - Forgetting dynamics

### Applied Memory Techniques
- [[Spaced Repetition]] - Optimal review scheduling
- [[Progressive Summarization]] - Layered compression
- [[Deliberate Practice]] - Skill acquisition through focused rehearsal

```dataview
TABLE maturity, confidence, next-review
FROM #memory OR #cognitive-load-theory OR #working-memory
WHERE type = "permanent-note" AND maturity != "evergreen"
SORT next-review ASC
LIMIT 8
```

> [!helpful-tip] Study Integration
> Memory systems research directly informs [[Instructional Design]] and [[Learning Theory]]. See Pillar V for pedagogical applications.

---

## 🎯 Pillar III: Attention & Executive Control

> [!key-claim] Executive Primacy
> [**Executive-Function**:: higher-order cognitive processes that regulate goal-directed behavior, including working memory updating, inhibitory control, cognitive flexibility, planning, and error monitoring—primarily associated with prefrontal cortex activity.]

### Attention Mechanisms
- [[Attention]] - Selective information processing
- [[Focus Of Attention]] - Attentional control strategies
- [[Higher-Order Cognition]] - Complex reasoning processes

### Executive Functions
- [[Executive Function]] - Cognitive control overview
- [[Cognitive Flexibility]] - Mental set-shifting
- [[Inhibitory Control]] - Response suppression
- [[Automation]] - Proceduralization of skills

### Monitoring & Regulation
- [[Cognitive Restructuring]] - Thought pattern modification
- [[Cognitive Reappraisal]] - Emotion regulation via reinterpretation
- [[Emotional Regulation]] - Affect management strategies

### Neural Substrates
- [[Default Mode Network]] - Task-negative baseline activity
- [[Neural Networks]] - Interconnected brain systems
- [[Neuroplasticity]] - Experience-dependent brain change
  - [[Neuroplastic]] - Adaptive reorganization capacity

```dataview
TABLE maturity, confidence, file.outlinks as "Related Concepts"
FROM #attention OR #executive-function OR #inhibitory-control
WHERE "03-notes/01_permanent-notes/01_cognitive-development"
SORT maturity DESC
LIMIT 4
```


> [!example] Clinical Application
> Executive dysfunction features prominently in [[Cognitive-Behavioral Therapy]] for [[Anxiety disorders]] and [[Major Depressive Disorder]], where [[Cognitive Distortions]] and [[Automatic Thoughts]] reflect impaired cognitive control.

---

## 🌱 Pillar IV: Development & Learning Processes

> [!methodology-and-sources] Developmental Framework
> [**Cognitive-Development**:: the progressive transformation of mental structures and processes across the lifespan, encompassing perceptual, attentional, memory, reasoning, and problem-solving capabilities—investigated through cross-sectional, longitudinal, and microgenetic research designs.]

### Developmental Foundations
- [[Cognitive Development]] - Lifespan cognitive change
- [[Educational Psychology]] - Learning in formal contexts
- [[Learning Theory]] - Principles of knowledge acquisition

### Self-Directed Learning
- [[Self Directed Learning]] - Autonomous learning processes
- [[Self-Regulated Learning]] - Metacognitive learning control
- [[Self-Regulation-Theory]] - Theoretical foundations
- [[Self Behavioral Management]] - Behavioral self-control

### Instructional Applications
- [[Instructional Design]] - Systematic learning design
- [[Library Science]] - Information organization and access

### Psychological Foundations
- [[Motivation Science]] - Drive and goal pursuit
  - [[Motivational Psychology]] - Applied motivation research
  - [[Self Determination Theory]] - Intrinsic motivation framework
    - [[Intrinsic Motivation]] - Internal drive
    - [[Competence]] - Mastery perception
    - [[Relatedness]] - Social connection need
  - [[Cognitive Theory]] - Mental representations of goals

```dataview
TABLE maturity, confidence, source
FROM #learning-theory OR #cognitive-development OR #self-regulated-learning
WHERE type = "permanent-note"
SORT confidence DESC, maturity DESC
LIMIT 10
```

> [!analogy] Scaffolding Metaphor
> Just as [[Deliberate Practice]] requires structured challenge incrementally above current skill level, cognitive development proceeds through [[Neuroplastic]] reorganization driven by optimally difficult tasks—neither too easy (no adaptation stimulus) nor too hard (cognitive overload).

---

## 🧘 Pillar V: Metacognition & Self-Regulation

> [!definition] Metacognitive Core
> [**Metacognition**:: cognition about cognition—the awareness, monitoring, and regulation of one's own cognitive processes, including knowledge about strategies, task demands, and personal capabilities, coupled with executive control over learning and problem-solving.]

### Metacognitive Components
- [[Epistemic Cognition]] - Thinking about knowledge itself
- [[Epistemic Accountability]] - Justification standards
- [[Self-Compassion]] - Self-kindness during failure
- [[Self-control strategies]] - Impulse regulation techniques

### Monitoring & Control
- [[Consider The Opposite]] - Debiasing through perspective-taking
- [[Pre Mortem Analysis]] - Prospective failure analysis
- [[Prospective Hindsight]] - Imagined retrospection
- [[Planning]] - Goal-directed action sequencing
  - [[Habit Formation]] - Automaticity development
  - [[Pomodoro Technique]] - Time-boxed focus method

### Psychological Resilience
- [[Psychological Resilience]] - Adversity adaptation
- [[Mindfulness Meditation]] - Present-moment awareness
- [[Flow Theory]] - Optimal experience states

### Cognitive Distortions & Corrections
- [[Cognitive Distortions]] - Systematic thinking errors
  - [[Automatic Thoughts]] - Rapid, uncritical cognitions
  - [[Rumination]] - Perseverative negative thought
- [[Cognitive Biases]] - Systematic judgment deviations
  - [[Confirmation Bias]] - Belief-confirming evidence preference
  - [[Anchoring Effect]] - Initial value over-influence
  - [[Availability Heuristic]] - Ease-of-recall bias
  - [[Representativeness Heuristic]] - Stereotype-based judgment
  - [[Illusions Of Comprehension]] - Metacognitive illusions

```dataview
TABLE maturity, confidence, tags
FROM #metacognition OR #self-regulation OR #cognitive-biases
WHERE type = "permanent-note"
SORT file.mtime DESC
LIMIT 12
```

> [!warning] Metacognitive Trap
> [**Illusions-Of-Comprehension**:: the metacognitive failure where learners overestimate their understanding due to fluency cues (ease of processing) that correlate weakly with actual comprehension—a core challenge in [[Self-Regulated Learning]].]

---

## 🎭 Pillar VI: Applied Domains & Clinical Integration

> [!methodology-and-sources] Translational Research
> This pillar bridges basic cognitive science with real-world applications in clinical psychology, education, philosophy, and performance optimization.

### Clinical Applications
- [[Cognitive-Behavioral Therapy]] - Thought-behavior intervention
  - [[Anxiety disorders]] - Pathological worry and fear
  - [[Major Depressive Disorder]] - Depressive cognition patterns

### Philosophical Foundations
- [[Stoicism]] - Ancient cognitive therapy
  - [[Stoic Philosophy]] - Rational emotion management
  - [[Dichotomy of Control]] - Internal/external locus distinction
- [[Locus Of Control]] - Agency attribution
- [[Socratic Method]] - Question-based inquiry
- [[Socratic Thinking]] - Critical reasoning approach
- [[Pragmatism]] - Action-oriented epistemology

### Performance & Motivation
- [[System 1]] - Fast, automatic processing
- [[System 2]] - Slow, deliberate reasoning

```dataview
TABLE maturity, confidence, link-up
FROM #clinical OR #philosophy-of-mind OR #stoicism
WHERE type = "permanent-note"
SORT maturity DESC
LIMIT 8
```

---

## 🌉 Semantic Bridges: Cross-Domain Connections

> [!helpful-tip] Discovering Hidden Links
> The following DataviewJS query identifies "sibling notes"—permanent notes that share multiple outgoing links with cognitive science concepts, suggesting thematic overlap and potential integration opportunities.

```dataviewjs
// Semantic Bridge Engine: Find notes with shared contexts
const cogSciPages = dv.pages('#cognitive-science')
    .where(p => p.type === "permanent-note");

const cogSciPaths = cogSciPages.map(p => p.file.path);
const otherPages = dv.pages()
    .where(p => p.type === "permanent-note" && !cogSciPaths.includes(p.file.path));

const bridges = [];

otherPages.forEach(page => {
    const sharedLinks = page.file.outlinks.filter(link => 
        cogSciPaths.includes(link.path)
    );
    
    if (sharedLinks.length >= 2) {
        bridges.push({
            note: page.file.link,
            connections: sharedLinks.length,
            domains: page.tags.slice(0, 3).join(", ")
        });
    }
});

bridges.sort((a, b) => b.connections - a.connections);

if (bridges.length > 0) {
    dv.header(3, "🔗 High-Connectivity External Notes");
    dv.table(
        ["Note", "Shared Links", "Primary Domains"],
        bridges.slice(0, 10).map(b => [
            b.note,
            `🔗 ${b.connections}`,
            b.domains
        ])
    );
} else {
    dv.paragraph("*No high-connectivity external notes found. Expand your knowledge graph!*");
}
```

### Known Integration Points

**Cognitive Science ↔ Philosophy**
- [[Epistemology]] ↔ [[Cognitive Development]] (developmental epistemology)
- [[Stoicism]] ↔ [[Cognitive Restructuring]] (ancient CBT parallels)
- [[Philosophy of Mind]] ↔ [[Extended Mind]] (consciousness theories)

**Cognitive Science ↔ Neuroscience**
- [[Working Memory]] ↔ [[Default Mode Network]] (neural correlates)
- [[Neuroplasticity]] ↔ [[Habit Formation]] (synaptic change)
- [[Executive Function]] ↔ [[Neural Networks]] (prefrontal systems)

**Cognitive Science ↔ Education**
- [[Cognitive Load Theory]] ↔ [[Instructional Design]] (design implications)
- [[Spaced Repetition]] ↔ [[Curve Of Forgetting]] (optimal scheduling)
- [[Self-Regulated Learning]] ↔ [[Deliberate Practice]] (skill mastery)

**Cognitive Science ↔ Clinical Psychology**
- [[Cognitive Biases]] ↔ [[Cognitive Distortions]] (systematic errors)
- [[Cognitive Reappraisal]] ↔ [[Emotional Regulation]] (affect management)
- [[Anxiety disorders]] ↔ [[Automatic Thoughts]] (pathological cognition)

---

## 📚 Specialized Submaps & Related MOCs

> [!abstract] Navigational Aids
> For deeper exploration of specific domains, consult these specialized maps:

### Internal Submaps
- **Memory Systems Deep Dive** → See Pillar II
- **Executive Function Hub** → See Pillar III
- **Learning Sciences Integration** → See Pillar IV
- **Metacognition & Bias** → See Pillar V

### External MOCs (Cross-References)
- [[Learning Theory MOC]] - Pedagogical frameworks
- [[Neuroscience MOC]] - Brain structure and function
- [[Philosophy MOC]] - Epistemology and mind
- [[Psychology MOC]] - Applied psychology domains
- [[PKB & PKM MOC]] - Knowledge management applications

---

## 🔬 Research & Review Queue

```dataview
TABLE maturity, confidence, next-review, review-count
FROM #cognitive-science
WHERE type = "permanent-note" AND maturity != "evergreen"
SORT next-review ASC
LIMIT 15
```

> [!important] Review Protocol
> **Priority Review Targets:**
> - Notes with `maturity: seedling` or `budding` → Require expansion
> - Notes with `next-review` overdue → Need validation
> - Notes with `review-count: 0` → Never systematically reviewed
> 
> **Review Checklist:**
> - [ ] Are all key concepts wiki-linked?
> - [ ] Does the note integrate with related concepts?
> - [ ] Are empirical claims properly sourced?
> - [ ] Is the maturity level accurate?
> - [ ] Are there new connections to add?

---

## 📊 MOC Analytics

```dataviewjs
// Aggregate statistics across cognitive science domain
const pages = dv.pages('#cognitive-science')
    .where(p => p.type === "permanent-note");

const totalNotes = pages.length;
const avgConfidence = pages.array()
    .map(p => {
        const confMap = {'speculative': 1, 'provisional': 2, 'moderate': 3, 'established': 4, 'high': 5};
        return confMap[p.confidence] || 0;
    })
    .reduce((a, b) => a + b, 0) / totalNotes;

const avgLinks = pages.array()
    .map(p => p.file.outlinks.length)
    .reduce((a, b) => a + b, 0) / totalNotes;

const avgBacklinks = pages.array()
    .map(p => p.file.inlinks.length)
    .reduce((a, b) => a + b, 0) / totalNotes;

const topSources = pages.array()
    .map(p => p.source)
    .filter(s => s)
    .reduce((acc, s) => {
        acc[s] = (acc[s] || 0) + 1;
        return acc;
    }, {});

dv.header(3, "📈 Domain Statistics");
dv.paragraph(`
**Total Permanent Notes**: ${totalNotes}  
**Average Confidence**: ${avgConfidence.toFixed(2)}/5  
**Average Outlinks**: ${avgLinks.toFixed(1)}  
**Average Backlinks**: ${avgBacklinks.toFixed(1)}  
**Knowledge Graph Density**: ${(avgLinks * avgBacklinks / totalNotes).toFixed(2)}
`);

dv.header(4, "🔝 Top Sources");
const sortedSources = Object.entries(topSources)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5);
dv.list(sortedSources.map(([source, count]) => `**${source}**: ${count} notes`));
```

---

## 🎯 Next Steps & Expansion Opportunities

### Priority Development Areas
1. **Sensory Processing** - Add notes on perception, pattern recognition, vision/audition
2. **Language & Communication** - Expand linguistic cognition, pragmatics, semiotics
3. **Social Cognition** - Theory of mind, empathy, cultural cognition
4. **Computational Models** - Bayesian cognition, connectionism, symbolic AI
5. **Applied Ergonomics** - Human factors, interface design, cognitive engineering

### Cross-Domain Integration Projects
- **Cognitive Science ↔ AI/ML** - Neural networks, cognitive architectures, AGI
- **Cognitive Science ↔ Economics** - Behavioral economics, decision theory, nudges
- **Cognitive Science ↔ Anthropology** - Cultural cognition, distributed systems
- **Cognitive Science ↔ Linguistics** - Psycholinguistics, language acquisition

### Maintenance Tasks
- [ ] Audit all `seedling` notes for promotion to `budding`
- [ ] Create bi-directional links between pillars (currently under-connected)
- [ ] Add inline Dataview fields for key definitions
- [ ] Create visual concept maps using Excalidraw or Mermaid
- [ ] Tag papers with year and author for citation tracking

---

## 🔗 Related Topics for PKB Expansion

1. **[[Embodied Cognition]]**
   - *Connection*: Extends [[Extended Mind]] by emphasizing bodily basis of thought
   - *Depth Potential*: Bridges cognitive science with phenomenology, motor control, AI robotics
   - *Knowledge Graph Role*: Links Pillar I (architecture) with sensorimotor foundations

2. **[[Situated Cognition]]**
   - *Connection*: Complements [[Distributed Cognition]] and [[Extended Mind]]
   - *Depth Potential*: Environmental context effects on reasoning, learning, memory
   - *Knowledge Graph Role*: Cross-domain hub connecting cognition, ecology, education

3. **[[Predictive Processing]]**
   - *Connection*: Unifying framework for perception, action, learning, and consciousness
   - *Depth Potential*: Bayesian brain hypothesis, active inference, free energy principle
   - *Knowledge Graph Role*: Meta-theoretical framework potentially reorganizing entire MOC

4. **[[Cognitive Phenomenology]]**
   - *Connection*: Integrates [[Philosophy of Mind]] with empirical cognitive science
   - *Depth Potential*: Subjective experience of thinking, consciousness, qualia
   - *Knowledge Graph Role*: Bridges Pillar I with [[Mindfulness Meditation]] and phenomenology

---

> [!quote] Closing Reflection
> "The mind is not a vessel to be filled, but a fire to be kindled." — Plutarch
> 
> This MOC represents not a static map but a dynamic knowledge graph—a living system that grows through exploration, critique, and integration. As your understanding deepens, so too should the connections between these concepts, revealing new patterns and possibilities for both theoretical insight and practical application.

---

**MOC Metadata:**
- **Created**: 2025-12-13
- **Last Major Update**: 2025-12-13
- **Total Permanent Notes Catalogued**: 85+ concepts
- **MOC Maturity**: Developing (comprehensive structure established, ongoing refinement needed)
- **Maintenance Frequency**: Quarterly review recommended