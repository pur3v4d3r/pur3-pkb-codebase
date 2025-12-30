---
aliases:
  - LLM PKB Integration Systems
  - Claude PKB Modules
tags:
  - type/report
  - year/2025
  - type/prompt-library
  - status/under-revision
  - pkb
  - prompt-engineering
  - concept-mapping
  - prompt-workflow/ideation
  - graph-analysis
  - prompting-technique/reflection/refinement
  - attention
  - reasoning
  - cognitive-pkm
source: claude-opus-4.1
id: "20251214114535"
created: 2025-12-14T11:45:35
modified: 2025-12-14T11:45:35
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
maturity: needs-review
confidence: provisional
next-review: 2025-12-21
review-count: 0
link-up:
  - "[[prompt-engineering-moc]]"
link-related:
  - "[[2025-12-14|Daily-Note]]"
---



# 🧠 Comprehensive LLM-PKB Integration Systems

## Executive Analysis

Your proposed integration enhancements represent a sophisticated evolution from **static knowledge capture** to **dynamic, queryable, self-documenting knowledge architecture**. The core insight driving all nine proposals is this: <span style='color: #FFC700;'>**metadata isn't overhead—it's infrastructure**</span>. Each marker, tag, and encoded relationship transforms flat text into a machine-traversable semantic graph while remaining human-readable.

Let me expand each existing proposal and introduce six additional systems I've identified as high-value gaps in the current architecture.

---

## 📊 Expanded Analysis of Existing Proposals

````
### Confidence Markers — Epistemic Status Encoding

> [!principle-point] Core Innovation
> [**Epistemic-Encoding**:: the practice of explicitly marking the certainty level of knowledge claims, enabling both human judgment calibration and machine-queryable evidence quality filtering.]

Your proposal correctly identifies that <span style='color: #FF00DC;'>undifferentiated claims create false equivalence</span>—a replicated meta-analysis finding and a single blog post opinion appear identically authoritative in standard notes.

**Expansion Opportunities:**

The five-tier system (`verified`, `established`, `provisional`, `speculative`, `contested`) could benefit from two additional dimensions:

1. <span style='color: #72FFF1;'>**Temporal Stability**</span>: Some claims are verified *but volatile* (e.g., current best practices in rapidly evolving fields). Add `^stable` vs `^volatile` modifiers.

2. <span style='color: #72FFF1;'>**Personal vs. Consensus**</span>: Distinguish between "the field believes X" and "I believe X based on my synthesis." Add `^consensus` vs `^personal-synthesis` markers.

**Enhanced Marker Taxonomy:**
```
[**Claim**:: value]^verified-stable          # Replicated, unlikely to change
[**Claim**:: value]^established-volatile     # Accepted now, field evolving
[**Claim**:: value]^provisional-consensus    # Tentative, but field agrees
[**Claim**:: value]^speculative-personal     # My hypothesis, not field's
[**Claim**:: value]^contested-active         # Ongoing debate
````






```
### Bidirectional Link Hints — Relationship Typing

> [!principle-point] Core Innovation
> [**Semantic-Link-Typing**:: encoding the *nature* of conceptual relationships rather than merely their *existence*, transforming wiki-links from navigational shortcuts into knowledge graph edges with queryable properties.]

Your relationship vocabulary is excellent. I'd expand it with additional relationship types critical for [[Cognitive Science]] and [[Learning Theory]] domains:

**Extended Relationship Vocabulary:**

| Type | Symbol | Use Case | Example |
|------|--------|----------|---------|
| `extends` | →(extends)→ | Theoretical elaboration | [[CLT]] →(extends)→ [[Information Processing]] |
| `operationalizes` | →(operationalizes)→ | Abstract → measurable | [[Intrinsic Load]] →(operationalizes)→ [[Element Interactivity]] |
| `analogous-to` | →(analogous-to)→ | Cross-domain parallel | [[Working Memory]] →(analogous-to)→ [[RAM]] |
| `precondition-for` | →(precondition-for)→ | Logical dependency | [[Schema Acquisition]] →(precondition-for)→ [[Automation]] |
| `falsifies` | →(falsifies)→ | Empirical refutation | [[Late Selection Evidence]] →(falsifies)→ [[Early Selection Theory]] |
| `synthesizes` | →(synthesizes)→ | Integration of multiple | [[Load Theory]] →(synthesizes)→ [[CLT]] + [[Perceptual Load]] |
```


````
### Atomic Extraction Markers — Note Spawning Signals

> [!principle-point] Core Innovation
> [**Extraction-Signaling**:: explicit markers within reference notes that flag embedded concepts as candidates for standalone atomic note creation, enabling systematic vault expansion workflows.]

Your `%%ATOMIC%%` syntax is clean. I'd enhance the metadata captured:

**Enhanced Atomic Candidate Schema:**
```markdown
> [!atomic-candidate] Filter Model (Broadbent 1958)
> **Slug**: `filter-model-broadbent-1958`
> **Note Type**: atomic-concept
> **Priority**: critical
> **Estimated Length**: 400-600 words
> **Key Relationships**: 
>   - →(superseded-by)→ [[Attenuation Model]]
>   - →(builds-on)→ [[Information Processing Theory]]
>   - →(tested-via)→ [[Dichotic Listening Paradigm]]
> **Source Coverage**: Needs primary source review
> **Extraction Trigger**: Referenced 3+ times in current vault
```

The addition of <span style='color: #72FFF1;'>**Extraction Trigger**</span> creates an auditable rationale for why this concept deserves atomization.
````

---

### 4-9. Remaining Proposals — Summary Enhancements

> [!abstract] Quick Enhancement Notes
> 
> **SR Integration**: Add `%%SR-INTERLEAVE%%` markers for concepts that should be mixed during review (combats [[Illusion of Competence]]).
> 
> **Source Provenance**: Add `^primary` vs `^secondary` source type markers; enable "trace to primary" queries.
> 
> **Prerequisite Mapping**: Add `soft-prerequisite` (helpful but not required) vs `hard-prerequisite` (must understand first).
> 
> **Semantic Versioning**: Add `breaking-change` flags when understanding fundamentally shifts (not just accumulates).
> 
> **Query Anchors**: Namespace anchors by domain: `%%QA:attention:all-theories%%` vs `%%QA:memory:encoding-types%%`.
> 
> **Contradiction Markers**: Add `resolution-attempted` field tracking your synthesis efforts.

---

## 🆕 Novel Integration Systems

Based on gaps in the current architecture, I propose six additional high-value systems:

---

### 10. **Cognitive Load Indicators** — Study Session Optimization

<span style='color: #FFC700;'>**Problem**</span>: Notes vary dramatically in cognitive demand, but nothing signals this to future-you planning a study session.

<span style='color: #27FF00;'>**Solution**</span>: Embed complexity indicators enabling intelligent study session construction.

```markdown
---
cognitive-load:
  intrinsic: high          # Inherent complexity of material
  element-interactivity: 8 # Scale 1-10
  prerequisite-count: 5    # Number of concepts assumed known
  estimated-passes: 3      # Times needed for mastery
  optimal-state: "alert, caffeinated, 45min+ available"
---

<!-- Or inline -->
%%LOAD: intrinsic=high | interactivity=8 | passes=3%%
```

**PKB Value**: Filter notes by available cognitive bandwidth; build progressive difficulty queues; avoid overwhelm.

---

### 11. **Application Context Markers** — Transfer Facilitation

<span style='color: #FFC700;'>**Problem**</span>: Knowledge captured but no encoding of *where/when* to apply it.

<span style='color: #27FF00;'>**Solution**</span>: Explicit application domain and trigger condition markers.

```markdown
> [!application-context] Cognitive Load Theory
> **Domains**: 
>   - [[Instructional Design]] — curriculum sequencing
>   - [[UX Design]] — interface complexity management
>   - [[Prompt Engineering]] — chunk complexity calibration
> **Trigger Conditions**:
>   - "Learner seems overwhelmed" → reduce extraneous load
>   - "Material isn't sticking" → check element interactivity
>   - "Expert blind spot detected" → scaffold missing schemas
> **Anti-Patterns**:
>   - Applying to entertainment content (not learning context)
>   - Ignoring individual differences in prior knowledge

[**Application-Domain**:: [[Prompt Engineering]] | trigger:"complex instructions failing" | action:"decompose into sequential steps"]
```

**PKB Value**: Query "what knowledge applies to X situation"; build domain-specific toolkits; reduce [[Inert Knowledge]] problem.

---

### 12. **Evidence Weight Indicators** — Epistemological Rigor

<span style='color: #FFC700;'>**Problem**</span>: "Research shows…" conflates single underpowered study with robust meta-analysis.

<span style='color: #27FF00;'>**Solution**</span>: Hierarchical evidence typing following [[Evidence-Based Practice]] standards.

```markdown
<!-- Evidence hierarchy markers -->
[**Finding**:: claim here]^evidence:meta-analysis
[**Finding**:: claim here]^evidence:rct
[**Finding**:: claim here]^evidence:observational
[**Finding**:: claim here]^evidence:case-study
[**Finding**:: claim here]^evidence:expert-opinion
[**Finding**:: claim here]^evidence:anecdote

<!-- Enhanced with sample size and effect -->
[**Spacing-Effect**:: distributed practice improves retention]^evidence:meta-analysis|n=29000|d=0.42
```

**PKB Value**: Filter claims by evidence quality; identify knowledge areas needing stronger foundations; calibrate confidence appropriately.

---

### 13. **Synthesis Potential Markers** — Cross-Domain Opportunity Flags

<span style='color: #FFC700;'>**Problem**</span>: Valuable cross-domain connections remain latent because no mechanism flags synthesis opportunities.

<span style='color: #27FF00;'>**Solution**</span>: Explicit markers identifying concepts ripe for interdisciplinary integration.

```markdown
> [!synthesis-opportunity] Attention as Resource Allocation
> **Source Domain**: [[Cognitive Psychology]] — [[Kahneman Capacity Model]]
> **Target Domains**: 
>   - [[Economics]] — scarcity/allocation parallels
>   - [[Computer Science]] — CPU scheduling algorithms
>   - [[Organizational Behavior]] — team cognitive bandwidth
> **Synthesis Type**: analogical-transfer
> **Exploration Status**: unexplored
> **Potential Value**: high (novel framework possible)

%%SYNTHESIS: source=kahneman-capacity | targets=economics,cs-scheduling | status=unexplored%%
```

**PKB Value**: Systematic innovation cultivation; directed cross-domain reading; novel framework generation.

---

### 14. **Temporal Decay Indicators** — Knowledge Freshness Tracking

<span style='color: #FFC700;'>**Problem**</span>: Fields evolve; notes become stale; no mechanism signals when review/update is needed.

<span style='color: #27FF00;'>**Solution**</span>: Domain-specific decay rates and review triggers.

```markdown
---
freshness:
  domain-volatility: high    # How fast does this field move?
  last-verified: 2025-01-15  # When did you confirm currency?
  decay-rate: 6-months       # Review interval
  staleness-risk: medium     # Current status
  update-triggers:
    - "New major publication in field"
    - "Paradigm shift indicators"
    - "Personal confusion when applying"
---

%%FRESHNESS: volatility=high | verified=2025-01 | decay=6mo | status=current%%
```

**PKB Value**: Automated review queues; field-appropriate update scheduling; prevent outdated knowledge application.

---

### 15. **Mental Model Anchors** — Framework Integration Points

<span style='color: #FFC700;'>**Problem**</span>: Individual concepts exist but aren't explicitly connected to overarching mental models that organize understanding.

<span style='color: #27FF00;'>**Solution**</span>: Explicit anchoring of concepts to foundational thinking frameworks.

```markdown
> [!mental-model-anchor] 
> **Concept**: [[Cognitive Load Theory]]
> **Anchors To**:
>   - [[Systems Thinking]] — feedback loops between load types
>   - [[Constraint Theory]] — bottleneck identification
>   - [[First Principles Thinking]] — decomposition to element level
>   - [[Inversion]] — what would INCREASE load? (avoid that)
> **Integration Notes**: CLT is fundamentally a constraint/bottleneck model applied to cognition

[**Model-Anchor**:: [[Cognitive Load Theory]] ←anchors-to→ [[Constraint Theory]] | insight:"learning bottlenecks = cognitive constraints"]
```

**PKB Value**: Rapid sense-making through framework activation; transferable reasoning patterns; metacognitive scaffolding.

---

### 16. **Counterexample Collection** — Edge Case Tracking

<span style='color: #FFC700;'>**Problem**</span>: Principles captured without boundary conditions; overgeneralization risk.

<span style='color: #27FF00;'>**Solution**</span>: Systematic counterexample and exception documentation.

```markdown
> [!counterexample] Testing Effect Limitations
> **Principle**: [[Testing Effect]] — retrieval practice enhances retention
> **Counterexample**: Very low-knowledge learners may benefit more from restudy initially
> **Boundary Condition**: Requires sufficient initial encoding to retrieve
> **Source**: Karpicke & Blunt, 2011
> **Implication**: Scaffold before testing for novices

[**Boundary-Condition**:: [[Testing Effect]] fails-when: "initial encoding insufficient" | population:"absolute novices" | alternative:"restudy then test"]
```

**PKB Value**: Nuanced principle application; prevent overgeneralization; track edge cases systematically.

---

## 🔧 Complete Modular Prompt Components

Below are production-ready prompt components for all 16 systems. Each is designed for independent insertion into your agent architecture.

---

### Module 1: Epistemic Confidence Encoding

`````xml
<epistemic_confidence_encoding>
## 🎯 Epistemic Status Encoding Protocol

When generating knowledge claims, explicitly encode confidence levels using inline markers.

<confidence_taxonomy>
### Primary Confidence Levels

| Marker | Definition | Typical Source | Visual |
|--------|------------|----------------|--------|
| `^verified` | Multiple independent replications; scientific consensus | Meta-analyses, systematic reviews | 🟢 |
| `^established` | Widely accepted in field; standard textbook content | Authoritative texts, review papers | 🔵 |
| `^provisional` | Single study, recent finding, limited replication | Primary research, recent publications | 🟡 |
| `^speculative` | Theoretical inference, hypothesized relationship | Personal synthesis, theoretical papers | 🟠 |
| `^contested` | Active scholarly debate; conflicting evidence | Debate literature, response papers | 🔴 |

### Secondary Modifiers (Optional)

| Modifier | Meaning | Use Case |
|----------|---------|----------|
| `-stable` | Unlikely to change significantly | Well-established principles |
| `-volatile` | Field actively evolving; may shift | Cutting-edge domains |
| `-consensus` | Represents field agreement | Distinguishing from personal view |
| `-personal` | Personal synthesis, not field consensus | Original analysis |
</confidence_taxonomy>

<syntax_specification>
### Syntax Patterns

**Basic Format:**
```markdown
[**Field-Name**:: claim content]^confidence-level
```

**With Secondary Modifier:**
```markdown
[**Field-Name**:: claim content]^confidence-level-modifier
```

**Examples:**
```markdown
[**Spacing-Effect**:: distributed practice produces superior retention to massed practice]^verified-stable

[**Desirable-Difficulties**:: conditions that slow initial learning but enhance long-term retention]^established-consensus

[**AI-Consciousness**:: large language models may develop emergent self-models]^speculative-personal

[**Retrieval-Practice-Mechanisms**:: testing effect operates via elaborative retrieval processes]^provisional-volatile

[**Learning-Styles-Validity**:: matching instruction to preferences improves outcomes]^contested-active
```
</syntax_specification>

<generation_heuristics>
### When to Apply Each Level

**^verified**: Apply when:
- Multiple meta-analyses converge
- Effect replicated across labs, populations, contexts
- No serious methodological challenges remain
- Would be surprising if overturned

**^established**: Apply when:
- Appears in authoritative textbooks
- Cited without hedging in review papers
- Taught as standard curriculum content
- Limited ongoing debate

**^provisional**: Apply when:
- Based on single study or limited samples
- Published within last 2-3 years without replication
- Methodology sound but awaiting confirmation
- From reputable source but not yet consensus

**^speculative**: Apply when:
- Personal theoretical inference
- Extrapolating from adjacent domains
- "If X is true, then Y should follow" reasoning
- No direct empirical test yet

**^contested**: Apply when:
- Prominent researchers disagree
- Response/rebuttal papers exist
- Replication attempts show mixed results
- Active debate in journals
</generation_heuristics>

<integration_notes>
### Dataview Query Compatibility

These markers enable queries like:

```dataview
TABLE file.name as "Note", confidence
FROM "permanent-notes"
WHERE contains(file.content, "^speculative")
SORT file.mtime DESC
```

### Output Requirements
- Every substantive claim in reference notes SHOULD have confidence encoding
- Definitions from authoritative sources: `^established` minimum
- Personal syntheses: `^speculative-personal` or `^provisional-personal`
- Density: 40-60% of inline fields should carry confidence markers
</integration_notes>
</epistemic_confidence_encoding>
`````

---

### Module 2: Semantic Relationship Typing

`````xml
<semantic_relationship_typing>
## 🔗 Link Relationship Encoding Protocol

When establishing connections between concepts, encode the semantic relationship type.

<relationship_vocabulary>
### Core Relationship Types

| Relationship | Symbol | Definition | Use Case |
|--------------|--------|------------|----------|
| `builds-on` | →(builds-on)→ | Theoretical foundation | B extends/requires A |
| `supersedes` | →(supersedes)→ | Historical replacement | B replaces A |
| `contradicts` | →(contradicts)→ | Logical/empirical conflict | A and B incompatible |
| `supports` | →(supports)→ | Evidential backing | A provides evidence for B |
| `modulates` | →(modulates)→ | Causal influence | A affects magnitude of B |
| `instantiates` | →(instantiates)→ | Example of category | A is instance of B |
| `developed-by` | →(developed-by)→ | Attribution | B created A |
| `applied-in` | →(applied-in)→ | Practical domain | A is applied in context B |
| `extends` | →(extends)→ | Elaboration | B expands scope of A |
| `operationalizes` | →(operationalizes)→ | Abstract to measurable | B makes A testable |
| `analogous-to` | →(analogous-to)→ | Cross-domain parallel | A structurally similar to B |
| `precondition-for` | →(precondition-for)→ | Logical dependency | A must exist for B |
| `falsifies` | →(falsifies)→ | Empirical refutation | A disproves B |
| `synthesizes` | →(synthesizes)→ | Integration | C combines A + B |
| `component-of` | →(component-of)→ | Part-whole | A is part of B |
| `contrasts-with` | →(contrasts-with)→ | Distinguished from | A differs meaningfully from B |
</relationship_vocabulary>

<syntax_specification>
### Syntax Patterns

**Inline Field Format (Recommended):**
```markdown
[**Relationship-Type**:: [[Source]] →(relation)→ [[Target]]]
```

**Narrative Integration:**
```markdown
[[Cognitive Load Theory]] →(builds-on)→ [[Working Memory Model]] and →(extends)→ [[Information Processing Theory]].
```

**Complex Multi-Relation:**
```markdown
[**Theoretical-Lineage**:: [[Filter Model]] →(superseded-by)→ [[Attenuation Model]] →(integrated-into)→ [[Capacity Model]]]
```

**With Annotations:**
```markdown
[**Relationship**:: [[CLT]] →(applied-in)→ [[Instructional Design]] | annotation:"primary application domain since 1980s"]
```
</syntax_specification>

<generation_heuristics>
### Relationship Selection Guide

**Temporal/Historical Relations:**
- `supersedes`: Theory A historically replaced by Theory B
- `builds-on`: Theory B emerged from foundation of Theory A
- `developed-by`: Attribution to researcher/theorist

**Logical/Structural Relations:**
- `component-of`: Part-whole relationships
- `precondition-for`: Necessary conditions
- `instantiates`: Example-category relationships
- `operationalizes`: Abstract-concrete mappings

**Evidential Relations:**
- `supports`: Evidence favoring a claim
- `falsifies`: Evidence against a claim
- `contradicts`: Incompatible claims

**Functional Relations:**
- `modulates`: Causal/influence relationships
- `applied-in`: Domain of application
- `extends`: Scope expansion

**Comparative Relations:**
- `analogous-to`: Cross-domain structural similarity
- `contrasts-with`: Meaningful distinction
- `synthesizes`: Integration of multiple sources
</generation_heuristics>

<output_requirements>
### Density Guidelines

- Reference notes: 8-15 explicit relationship encodings
- MOCs: Heavy relationship typing (primary purpose)
- Atomic notes: 2-5 key relationships minimum
- Always encode when introducing how concepts relate
</output_requirements>
</semantic_relationship_typing>
`````

---

### Module 3: Atomic Extraction Signaling

`````xml
<atomic_extraction_signaling>
## 🧬 Note Spawning Protocol

When generating reference notes, identify concepts warranting atomic note extraction.

<extraction_criteria>
### Atomic Candidate Identification

**ALWAYS flag when:**
- Named theory, model, or framework with distinct identity
- Named researcher with significant contribution to topic
- Technical term with >50 words of explanation needed
- Principle or law with broad applicability
- Phenomenon with dedicated research literature
- Method or technique with procedural steps

**CONSIDER flagging when:**
- Concept referenced 3+ times across vault
- Term likely to appear in multiple domains
- Definition contested or evolved over time
- Practical applications warrant separate treatment

**DO NOT flag:**
- Generic terms with dictionary definitions
- Passing mentions without substantive explanation
- Concepts already atomized elsewhere in vault
</extraction_criteria>

<callout_specification>
### Atomic Candidate Callout Structure

```markdown
> [!atomic-candidate] Concept Name (Attribution Year)
> **Slug**: `kebab-case-identifier`
> **Note Type**: [atomic-concept | principle | framework | theorist | method | phenomenon]
> **Priority**: [critical | high | medium | low]
> **Estimated Scope**: [word count range]
> **Key Relationships**:
>   - →(relation)→ [[Related Concept 1]]
>   - →(relation)→ [[Related Concept 2]]
> **Source Status**: [needs-primary-review | has-primary | secondary-only]
> **Extraction Trigger**: [rationale for flagging]
```
</callout_specification>

<inline_alternative>
### Lightweight Inline Syntax

For rapid marking without full callout:

```markdown
%%ATOMIC: slug-name | note-type | priority | trigger-reason%%
```

**Examples:**
```markdown
%%ATOMIC: filter-model-broadbent | framework | high | foundational-attention-theory%%
%%ATOMIC: allocation-policy | atomic-concept | critical | central-to-capacity-model%%
%%ATOMIC: yerkes-dodson-law | principle | medium | frequently-referenced%%
```
</inline_alternative>

<note_type_definitions>
### Note Type Classifications

| Type | Definition | Typical Length | Example |
|------|------------|----------------|---------|
| `atomic-concept` | Single well-defined idea | 300-600 words | Intrinsic Load |
| `principle` | Generalizable rule/law | 400-800 words | Spacing Effect |
| `framework` | Multi-component model | 800-1500 words | Cognitive Load Theory |
| `theorist` | Researcher biography + contributions | 600-1000 words | Daniel Kahneman |
| `method` | Procedural technique | 500-1000 words | Retrieval Practice |
| `phenomenon` | Observed effect/pattern | 400-800 words | Testing Effect |
</note_type_definitions>

<priority_definitions>
### Priority Level Guidelines

| Priority | Definition | Action Timeline |
|----------|------------|-----------------|
| `critical` | Core concept for current project | Extract immediately |
| `high` | Important for domain understanding | Extract this week |
| `medium` | Valuable but not urgent | Add to extraction queue |
| `low` | Nice-to-have, low frequency | Extract when relevant |
</priority_definitions>

<output_requirements>
### Generation Guidelines

- Place atomic markers immediately after relevant content
- Reference notes should yield 3-8 atomic candidates typically
- Use callout format for high/critical priority items
- Use inline format for medium/low priority items
- Always include extraction trigger rationale
</output_requirements>
</atomic_extraction_signaling>
`````

---

### Module 4: Spaced Repetition Integration

````xml
<spaced_repetition_integration>
## 🔄 SR Hook Generation Protocol

Generate spaced repetition compatible markers for key knowledge elements.

<card_types>
### SR Card Type Specifications

**Type 1: Basic Q&A**
```markdown
%%SR-CARD%%
Q: [Clear, specific question targeting single concept]
A: [Concise, complete answer]
%%END-SR%%
```

**Type 2: Cloze Deletion**
```markdown
%%SR-CLOZE%%
[Sentence with {{c1::key term}} for deletion and {{c2::another term}} if needed]
%%END-SR%%
```

**Type 3: Inline Quick-Review**
```markdown
%%SR: [prompt/question] → [response/answer]%%
```

**Type 4: Comparison Card**
```markdown
%%SR-COMPARE%%
Concept A: [Name]
Concept B: [Name]
Key Difference: [Distinguishing feature]
%%END-SR%%
```

**Type 5: Interleaving Marker** (for related cards to mix)
```markdown
%%SR-INTERLEAVE: topic-group-name%%
[Card content]
%%END-SR%%
```
</card_types>

<generation_triggers>
### When to Generate SR Hooks

**ALWAYS generate for:**
- Every formal definition (`[**Definition-Field**:: value]`)
- Every named principle or law
- Every key distinction/contrast
- Core framework components
- Critical procedural steps

**CONSIDER generating for:**
- Supporting examples that illuminate concepts
- Common misconceptions (what it's NOT)
- Application trigger conditions
- Historical context (who/when/why)

**Avoid generating for:**
- Meta-commentary and transitions
- Self-evident statements
- Content better learned through application than memorization
</generation_triggers>

<card_quality_standards>
### High-Quality Card Characteristics

**Questions should:**
- Target exactly ONE piece of knowledge
- Be unambiguous (only one correct answer)
- Use consistent terminology with source material
- Test understanding, not just recognition

**Answers should:**
- Be complete without being verbose
- Match the specificity of the question
- Use the same phrasing as the source when precision matters

**Cloze deletions should:**
- Delete meaningful terms, not filler words
- Maintain sentence comprehensibility with deletion
- Number deletions for multi-card generation (c1, c2, c3)
</card_quality_standards>


### Generation Examples

**From Definition:**
```markdown
[**Cognitive-Load**:: the total mental effort being used in working memory during information processing]

%%SR-CARD%%
Q: What is cognitive load?
A: The total mental effort being used in working memory during information processing.
%%END-SR%%

%%SR-CLOZE%%
{{c1::Cognitive load}} refers to the total {{c2::mental effort}} being used in {{c3::working memory}} during information processing.
%%END-SR%%
```

**From Distinction:**
```markdown
[**Intrinsic-vs-Extraneous**:: intrinsic load stems from material complexity; extraneous load stems from poor instructional design]

%%SR-COMPARE%%
Concept A: Intrinsic Load
Concept B: Extraneous Load
Key Difference: Intrinsic stems from material complexity (unavoidable); extraneous stems from poor design (reducible).
%%END-SR%%
```

**From Principle:**
```markdown
[**Spacing-Effect**:: distributed practice produces better retention than massed practice]

%%SR-CARD%%
Q: What does the spacing effect predict about practice distribution?
A: Distributed practice produces better long-term retention than massed practice of equivalent duration.
%%END-SR%%

%%SR-CLOZE%%
The {{c1::spacing effect}} demonstrates that {{c2::distributed}} practice produces better retention than {{c3::massed}} practice.
%%END-SR%%
```
</examples>

<density_guidelines>
### Output Requirements

- **Reference notes**: 5-12 SR hooks per major section
- **Atomic notes**: 2-4 SR hooks (focused coverage)
- **Prioritize**: Definitions, principles, distinctions, procedures
- **Interleaving**: Group related cards with `%%SR-INTERLEAVE%%` tags
</density_guidelines>
</spaced_repetition_integration>
`````

---

### Module 5: Source Provenance Chains

`````xml
<source_provenance_chains>
## 📚 Citation Traceability Protocol

Encode source attribution enabling claim-to-evidence traceability.

<provenance_syntax>
### Inline Provenance Markers

**Basic Source Attribution:**
```markdown
[**Claim-Name**:: claim content]
^source:: [[ref-author-year-title]] p.XX
^evidence-type:: [type]
^status:: [replication-status]
```

**Compact Inline Format:**
```markdown
[**Claim**:: value | src:author-year:pXX | evidence:type | status:level]
```

**Narrative Integration:**
```markdown
<span style='color: #FF5700;'>According to Kahneman (1973, p.47)</span>, [**Arousal-Capacity-Claim**:: arousal modulates total available capacity along an inverted-U function]^verified.
```
</provenance_syntax>

<evidence_type_taxonomy>
### Evidence Classification

| Type | Definition | Weight |
|------|------------|--------|
| `meta-analysis` | Systematic synthesis of multiple studies | Highest |
| `systematic-review` | Comprehensive literature review | Very High |
| `rct` | Randomized controlled trial | High |
| `quasi-experimental` | Non-randomized comparison | Moderate-High |
| `observational` | Correlational, cohort, case-control | Moderate |
| `case-study` | Single case or small n | Low-Moderate |
| `theoretical-claim` | Logical/theoretical argument | Variable |
| `expert-opinion` | Authority without data | Low |
| `anecdote` | Personal experience | Very Low |
</evidence_type_taxonomy>

<source_type_markers>
### Source Classification

| Marker | Meaning |
|--------|---------|
| `^primary` | Original research/data source |
| `^secondary` | Review, textbook, summary |
| `^tertiary` | Encyclopedia, handbook |
| `^personal` | Personal observation/synthesis |
</source_type_markers>

<reference_note_format>
### Structured Reference Entry

```markdown
> [!reference] author-year-short-title
> **Full Citation**: [Complete citation in preferred format]
> **Type**: [book | article | chapter | report | thesis]
> **Access**: [DOI/URL/Library]
> **Key Claims Sourced**:
>   - [[Claim-Name-1]]^pXX
>   - [[Claim-Name-2]]^pYY
> **Quality Assessment**: [Methodological notes]
> **Personal Notes**: [Your evaluation]
```
</reference_note_format>

<generation_guidelines>
### When to Include Provenance

**ALWAYS include for:**
- Empirical claims with specific findings
- Statistics, percentages, effect sizes
- Direct quotations or close paraphrases
- Controversial or contested claims
- Claims that might be challenged

**CONSIDER including for:**
- Historical attributions (who said/did what when)
- Technical definitions from specific sources
- Methodological recommendations

**MAY omit for:**
- Common knowledge in the field
- Your own syntheses (mark as `^personal` instead)
- Logical deductions from established principles
</generation_guidelines>

<query_compatibility>
### Dataview Integration

Enable queries like:
```dataview
LIST FROM "permanent-notes"
WHERE contains(file.content, "evidence:anecdote")
```

```dataview
TABLE claim, source
FROM "cognitive-science"
WHERE contains(file.content, "^status::unverified")
```
</query_compatibility>
</source_provenance_chains>
`````

---

### Module 6: Prerequisite Dependency Mapping

`````xml
<prerequisite_dependency_mapping>
## 🗺️ Learning Path Encoding Protocol

Explicitly declare knowledge dependencies enabling automated learning path generation.

<frontmatter_specification>
### YAML Frontmatter Format

```yaml
---
prerequisites:
  hard:
    - "[[concept-slug-1]]"  # Must understand first
    - "[[concept-slug-2]]"
  soft:
    - "[[concept-slug-3]]"  # Helpful but not required
    - "[[concept-slug-4]]"
enables:
  direct:
    - "[[concept-slug-5]]"  # Directly unlocks
    - "[[concept-slug-6]]"
  related:
    - "[[concept-slug-7]]"  # Benefits from this knowledge
difficulty: [foundational | intermediate | advanced | expert]
estimated-study-time: [Xmin]
optimal-sequence-position: [early | middle | late | capstone]
---
```
</frontmatter_specification>

<callout_format>
### Inline Callout Alternative

```markdown
> [!prerequisite] Required Background
> **Hard Prerequisites** (must understand first):
> - [[Information Processing Theory]] — foundational framework
> - [[Working Memory Basics]] — capacity constraints
> 
> **Soft Prerequisites** (helpful context):
> - [[History of Cognitive Psychology]] — theoretical lineage
> - [[Research Methods in Cogsci]] — study interpretation

> [!enables] This Unlocks
> **Direct Applications**:
> - [[Cognitive Load Theory]] — primary extension
> - [[Instructional Design Principles]] — practical application
> 
> **Related Topics**:
> - [[Expertise Development]] — schema automation
> - [[Multimedia Learning]] — CLT application
```
</callout_format>

<dependency_types>
### Prerequisite Classification

| Type | Symbol | Definition |
|------|--------|------------|
| `hard` | ⚠️ | Cannot understand B without A |
| `soft` | 💡 | A enriches understanding of B |
| `parallel` | ↔️ | A and B mutually inform |
| `optional` | ➕ | A deepens but isn't needed |

| Type | Symbol | Definition |
|------|--------|------------|
| `direct` | → | This note directly enables |
| `related` | ~ | Benefits from this knowledge |
| `advanced` | ↑ | Expert-level extension |
</dependency_types>

<difficulty_calibration>
### Difficulty Level Definitions

| Level | Definition | Typical Prerequisites |
|-------|------------|----------------------|
| `foundational` | Entry-level; minimal background | 0-2 concepts |
| `intermediate` | Builds on basics | 3-5 concepts |
| `advanced` | Requires substantial foundation | 6-10 concepts |
| `expert` | Assumes comprehensive knowledge | 10+ concepts |
</difficulty_calibration>

<generation_guidelines>
### When to Include Dependencies

**ALWAYS specify:**
- Hard prerequisites for advanced content
- Direct enables for foundational content
- Difficulty level for all substantive notes
- Study time estimates for reference notes

**Derive from:**
- Concepts assumed but not explained in the note
- Explicit "building on X" statements
- Theoretical lineages
- Practical applications mentioned
</generation_guidelines>

<query_compatibility>
### Learning Path Queries

```dataview
LIST FROM "cognitive-science"
WHERE difficulty = "foundational"
SORT file.name ASC
```

```dataview
TABLE enables.direct as "Unlocks"
FROM "permanent-notes"
WHERE contains(prerequisites.hard, "[[working-memory]]")
```
</query_compatibility>
</prerequisite_dependency_mapping>
`````

---

### Module 7: Semantic Versioning for Concepts

`````xml
<semantic_concept_versioning>
## 📊 Knowledge Evolution Tracking Protocol

Track how understanding of concepts evolves over time.

<frontmatter_specification>
### YAML Frontmatter Format

```yaml
---
concept-version: "X.Y.Z"
# X = Major (paradigm shift), Y = Minor (significant addition), Z = Patch (clarification)

version-history:
  - version: "1.0.0"
    date: "YYYY-MM-DD"
    change: "Initial understanding from [source]"
    trigger: "First encounter with concept"
  - version: "2.0.0"
    date: "YYYY-MM-DD"
    change: "Major revision incorporating [new framework]"
    trigger: "Read [source] that contradicted previous understanding"
    breaking: true
  - version: "2.1.0"
    date: "YYYY-MM-DD"
    change: "Added application domain [X]"
    trigger: "Applied concept in new context"

last-review: "YYYY-MM-DD"
next-review: "YYYY-MM-DD"
stability: [stable | evolving | volatile]
---
```
</frontmatter_specification>

<version_semantics>
### Version Number Meanings

| Component | Increment When | Example |
|-----------|----------------|---------|
| **Major (X)** | Fundamental understanding changes; old version now seems wrong | 1.0 → 2.0: "Realized CLT applies to expertise differently than I thought" |
| **Minor (Y)** | Significant addition that extends without contradicting | 2.0 → 2.1: "Added connection to multimedia learning principles" |
| **Patch (Z)** | Clarification, typo fix, minor refinement | 2.1 → 2.1.1: "Clarified definition wording" |
</version_semantics>

<breaking_change_flag>
### Breaking Change Documentation

When `breaking: true`:

```yaml
- version: "3.0.0"
  date: "2025-05-15"
  change: "Complete reconceptualization of attention as predictive process"
  trigger: "Deep dive into predictive processing framework"
  breaking: true
  deprecated-understanding: "Previous view of attention as filter/resource"
  migration-notes: "Review all notes linking to old attention model"
```
</breaking_change_flag>

<stability_indicators>
### Stability Classifications

| Status | Definition | Action |
|--------|------------|--------|
| `stable` | Well-established understanding, unlikely to change | Standard review cycle |
| `evolving` | Actively developing understanding | More frequent review |
| `volatile` | Field or understanding in flux | Flag for close monitoring |
</stability_indicators>

<inline_alternative>
### Lightweight Inline Syntax

```markdown
%%VERSION: 2.1.0 | last-updated:2025-05 | stability:evolving%%
```
</inline_alternative>
</semantic_concept_versioning>
`````

---

### Module 8: Query Anchors

`````xml
<query_anchor_system>
## 🎯 Dataview Optimization Points Protocol

Create explicit query targets for efficient vault-wide searches.

<anchor_syntax>
### Query Anchor Format

**Basic Syntax:**
```markdown
%%QUERY-ANCHOR: namespace:identifier%%
```

**Namespaced Examples:**
```markdown
%%QUERY-ANCHOR: attention:all-theories%%
%%QUERY-ANCHOR: attention:capacity-models%%
%%QUERY-ANCHOR: attention:filter-models%%
%%QUERY-ANCHOR: memory:encoding-strategies%%
%%QUERY-ANCHOR: learning:retrieval-practice-evidence%%
%%QUERY-ANCHOR: methodology:experimental-paradigms%%
```

**Multi-Tag Anchors:**
```markdown
%%QUERY-ANCHOR: attention:capacity + historical + foundational%%
```
</anchor_syntax>

<namespace_taxonomy>
### Standard Namespaces

| Namespace | Use For |
|-----------|---------|
| `attention` | Attention and concentration topics |
| `memory` | Memory systems and processes |
| `learning` | Learning theories and techniques |
| `cognition` | General cognitive processes |
| `methodology` | Research methods and paradigms |
| `application` | Practical applications |
| `theorist` | Researcher-specific content |
| `debate` | Contested or debated topics |
</namespace_taxonomy>

<identifier_patterns>
### Common Identifier Patterns

| Pattern | Example | Use |
|---------|---------|-----|
| `all-[category]` | `all-theories` | Collect all items of type |
| `[model]-components` | `clm-components` | Parts of a specific model |
| `evidence-for-[claim]` | `evidence-for-spacing` | Supporting evidence |
| `against-[claim]` | `against-learning-styles` | Counter-evidence |
| `applications-of-[concept]` | `applications-of-clt` | Practical uses |
| `history-of-[topic]` | `history-of-attention` | Historical development |
</identifier_patterns>

<query_examples>
### Dataview Query Patterns

**Find all items with anchor:**
```dataview
LIST FROM "permanent-notes"
WHERE contains(file.content, "%%QUERY-ANCHOR: attention:all-theories%%")
```

**Count anchored items:**
```dataview
TABLE length(rows) as "Count"
FROM "permanent-notes"
WHERE contains(file.content, "QUERY-ANCHOR: learning:")
GROUP BY true
```
</query_examples>

<placement_guidelines>
### Where to Place Anchors

- **At section start**: For content that spans multiple paragraphs
- **After key definitions**: For concepts you'll want to collect
- **In MOCs**: For navigation hub creation
- **Before evidence blocks**: For evidence collection queries
</placement_guidelines>
</query_anchor_system>
`````

---

### Module 9: Contradiction and Tension Markers

`````xml
<contradiction_tension_markers>
## ⚖️ Intellectual Honesty Encoding Protocol

Explicitly mark unresolved tensions, contradictions, and debates.

<tension_callout_specification>
### Tension Callout Structure

```markdown
> [!tension] Descriptive Tension Name
> **Position A**: [Claim/Theory A]
> - **Proponents**: [Researchers/Schools]
> - **Key Evidence**: [Supporting findings]
> 
> **Position B**: [Claim/Theory B]
> - **Proponents**: [Researchers/Schools]
> - **Key Evidence**: [Supporting findings]
> 
> **Current Status**: [active-debate | partially-resolved | synthesis-emerging]
> **Resolution Attempts**: [Notable reconciliation efforts]
> **Personal Stance**: [Your current position with rationale]
> **Needed for Resolution**: [What evidence/argument would settle this]
```
</tension_callout_specification>

<inline_syntax>
### Inline Tension Markers

```markdown
[**Unresolved-Tension**:: tension-name | positions:A-vs-B | status:active | priority:high]

[**Contradiction**:: [[Claim A]] ↔conflicts↔ [[Claim B]] | status:unresolved | personal-lean:A]
```
</inline_syntax>

<status_taxonomy>
### Tension Status Classifications

| Status | Definition | Action |
|--------|------------|--------|
| `active-debate` | Ongoing scholarly disagreement | Monitor literature |
| `partially-resolved` | Some consensus emerging | Document synthesis |
| `synthesis-emerging` | Integration being developed | Track development |
| `historical` | Past debate, now resolved | Document for context |
| `personal-confusion` | You're confused, not necessarily the field | Study more |
</status_taxonomy>

<contradiction_types>
### Contradiction Classifications

| Type | Definition | Example |
|------|------------|---------|
| `empirical` | Conflicting data/findings | Replication failures |
| `theoretical` | Incompatible frameworks | Single vs multiple resource pools |
| `methodological` | Disputes about how to measure | Implicit vs explicit measures |
| `definitional` | Different concept meanings | What counts as "attention" |
| `scope` | Different boundary conditions | Lab vs real-world findings |
</contradiction_types>

<resolution_tracking>
### Resolution Attempt Documentation

```markdown
> [!resolution-attempt] Synthesis of Position A and B
> **Date**: YYYY-MM-DD
> **Approach**: [How you tried to reconcile]
> **Outcome**: [success | partial | failed]
> **Remaining Issues**: [What's still unresolved]
> **Next Steps**: [Further investigation needed]
```
</resolution_tracking>

<generation_guidelines>
### When to Create Tension Markers

**ALWAYS mark when:**
- Two cited sources explicitly disagree
- "However, critics argue…" type statements
- Multiple competing models exist for same phenomenon
- Your own analysis reveals inconsistency

**Include in:**
- Reference notes covering debated topics
- Synthesis notes attempting integration
- MOCs organizing contested domains
</generation_guidelines>
</contradiction_tension_markers>
`````

---

### Module 10: Cognitive Load Indicators

`````xml
<cognitive_load_indicators>
## 🧠 Study Session Optimization Protocol

Embed complexity indicators enabling intelligent study planning.

<frontmatter_specification>
### YAML Frontmatter Format

```yaml
---
cognitive-load:
  intrinsic: [low | moderate | high | very-high]
  element-interactivity: [1-10]
  prerequisite-density: [count of assumed concepts]
  abstraction-level: [concrete | mixed | abstract | highly-abstract]
  
study-parameters:
  estimated-time: [Xmin]
  optimal-passes: [count for mastery]
  spacing-interval: [suggested review gap]
  optimal-state: "[description of ideal study conditions]"
  
chunking-guide:
  recommended-chunks: [count]
  natural-break-points: 
    - "[section/heading 1]"
    - "[section/heading 2]"
---
```
</frontmatter_specification>

<intrinsic_load_rubric>
### Intrinsic Load Assessment

| Level | Element Interactivity | Description |
|-------|----------------------|-------------|
| `low` | 1-3 | Can understand elements independently |
| `moderate` | 4-5 | Some elements must be held simultaneously |
| `high` | 6-8 | Many interdependent elements |
| `very-high` | 9-10 | All elements must be processed together |
</intrinsic_load_rubric>

<inline_syntax>
### Lightweight Inline Format

```markdown
%%LOAD: intrinsic=high | interactivity=7 | time=45min | passes=3 | state="focused, rested"%%
```
</inline_syntax>

<callout_format>
### Study Guide Callout

```markdown
> [!study-guide] Optimal Approach for This Note
> **Cognitive Demand**: High (element interactivity: 7/10)
> **Time Required**: 45-60 minutes for deep processing
> **Passes Needed**: 3 (initial → review → integrate)
> **Optimal Conditions**: Quiet environment, alert state, 50+ min available
> **Chunking Strategy**: 
>   1. Theoretical foundation (15 min)
>   2. Model components (20 min)
>   3. Applications (15 min)
> **Warning**: Don't attempt when fatigued—concepts compound
```
</callout_format>

<state_recommendations>
### Optimal State Descriptors

| Note Type | Recommended State |
|-----------|------------------|
| Foundational concepts | Any receptive state |
| Complex theory | Alert, focused, uninterrupted |
| Technical procedures | Ready to practice actively |
| Synthesis/integration | Creative, connective mindset |
| Review notes | Spaced, testing-oriented |
</state_recommendations>

<generation_guidelines>
### When to Include Load Indicators

**ALWAYS include for:**
- Reference notes (primary study materials)
- Complex theoretical frameworks
- Technical procedures with multiple steps

**Assessment Heuristics:**
- Count concepts that must be held in mind simultaneously
- Note abstraction level (concrete examples lower load)
- Consider prerequisite knowledge assumed
- Estimate based on your own experience processing the material
</generation_guidelines>
</cognitive_load_indicators>
`````

---

### Module 11: Application Context Markers

`````xml
<application_context_markers>
## 🎯 Transfer Facilitation Protocol

Encode where/when/how to apply captured knowledge.

<callout_specification>
### Application Context Callout

```markdown
> [!application-context] Concept Name
> **Primary Domains**:
>   - [[Domain 1]] — [specific use case]
>   - [[Domain 2]] — [specific use case]
>   - [[Domain 3]] — [specific use case]
> 
> **Trigger Conditions** (when to apply):
>   - "[Observable situation 1]" → [recommended action]
>   - "[Observable situation 2]" → [recommended action]
>   - "[Observable situation 3]" → [recommended action]
> 
> **Anti-Patterns** (when NOT to apply):
>   - [Situation where this doesn't work]
>   - [Common misapplication]
> 
> **Implementation Notes**:
>   - [Practical consideration 1]
>   - [Practical consideration 2]
```
</callout_specification>

<inline_syntax>
### Inline Application Markers

```markdown
[**Application-Domain**:: [[Domain]] | trigger:"situation description" | action:"recommended response" | confidence:high]

[**Anti-Pattern**:: [[Concept]] | context:"where it fails" | reason:"why it doesn't work" | alternative:"what to do instead"]
```
</inline_syntax>

<trigger_condition_patterns>
### Trigger Condition Formats

| Pattern | Example |
|---------|---------|
| Problem-based | "When learner shows overwhelm" → reduce extraneous load |
| Context-based | "In technical documentation" → apply chunking principles |
| Symptom-based | "Information not sticking" → check element interactivity |
| Goal-based | "Seeking long-term retention" → implement spaced practice |
| Resource-based | "Limited study time available" → prioritize high-yield |
</trigger_condition_patterns>

<domain_taxonomy>
### Common Application Domains

| Domain Category | Examples |
|-----------------|----------|
| **Education** | Curriculum design, tutoring, self-study |
| **Design** | UX, instructional materials, presentations |
| **Communication** | Technical writing, teaching, explaining |
| **Professional** | Meeting facilitation, training, onboarding |
| **Personal** | Self-improvement, habit formation, learning |
| **Technical** | Prompt engineering, documentation, code review |
</domain_taxonomy>

<generation_guidelines>
### When to Include Application Context

**ALWAYS include for:**
- Principles with clear practical applications
- Methods and techniques
- Frameworks designed for application

**Include triggers for:**
- Every principle worth remembering
- Concepts with non-obvious application points
- Knowledge at risk of becoming inert
</generation_guidelines>
</application_context_markers>
`````

---

### Module 12: Evidence Weight Indicators

`````xml
<evidence_weight_indicators>
## ⚖️ Epistemological Rigor Protocol

Classify evidence quality following evidence-based practice hierarchies.

<evidence_hierarchy>
### Evidence Strength Taxonomy

| Level | Type | Definition | Weight |
|-------|------|------------|--------|
| 1 | `meta-analysis` | Systematic quantitative synthesis | Highest |
| 2 | `systematic-review` | Comprehensive qualitative synthesis | Very High |
| 3 | `rct` | Randomized controlled trial | High |
| 4 | `quasi-experimental` | Non-randomized controlled study | Moderate-High |
| 5 | `cohort` | Prospective observational | Moderate |
| 6 | `case-control` | Retrospective comparison | Moderate-Low |
| 7 | `case-series` | Multiple cases without control | Low |
| 8 | `case-study` | Single case detailed examination | Low |
| 9 | `expert-opinion` | Authority assertion | Very Low |
| 10 | `anecdote` | Personal/informal observation | Lowest |
</evidence_hierarchy>

<inline_syntax>
### Evidence Marker Syntax

**Basic:**
```markdown
[**Finding-Name**:: claim content]^evidence:evidence-type
```

**Enhanced with Metadata:**
```markdown
[**Finding-Name**:: claim content]^evidence:meta-analysis|k=45|n=12000|d=0.65|p<.001
```

| Metadata | Meaning |
|----------|---------|
| `k` | Number of studies in meta-analysis |
| `n` | Total sample size |
| `d` | Cohen's d effect size |
| `r` | Correlation coefficient |
| `OR` | Odds ratio |
| `p` | P-value significance |
</inline_syntax>

<quality_markers>
### Study Quality Modifiers

| Modifier | Meaning |
|----------|---------|
| `-strong` | High methodological rigor |
| `-moderate` | Acceptable methodology |
| `-weak` | Notable limitations |
| `-flawed` | Serious problems identified |

**Example:**
```markdown
[**Claim**:: finding]^evidence:rct-strong|n=500|d=0.45
```
</quality_markers>

<replication_status>
### Replication Markers

| Status | Meaning |
|--------|---------|
| `replicated` | Successfully reproduced |
| `partially-replicated` | Mixed reproduction results |
| `failed-replication` | Key replication attempt failed |
| `not-yet-replicated` | Awaiting replication |
| `pre-registered` | Study was pre-registered |
</replication_status>

<generation_guidelines>
### When to Include Evidence Markers

**ALWAYS include for:**
- Empirical claims with specific findings
- Statistical claims (percentages, effect sizes)
- Claims that could be contested

**Quality Assessment Questions:**
- Was it randomized?
- Was there a control group?
- What was the sample size?
- Has it been replicated?
- Was it pre-registered?
</generation_guidelines>
</evidence_weight_indicators>
`````

---

### Module 13: Synthesis Potential Markers

`````xml
<synthesis_potential_markers>
## 🔮 Cross-Domain Opportunity Protocol

Flag concepts with high potential for interdisciplinary synthesis.

<callout_specification>
### Synthesis Opportunity Callout

```markdown
> [!synthesis-opportunity] Opportunity Title
> **Source Domain**: [[Primary Domain]] — [[Specific Concept]]
> **Target Domains**:
>   - [[Target Domain 1]] — [potential connection]
>   - [[Target Domain 2]] — [potential connection]
>   - [[Target Domain 3]] — [potential connection]
> 
> **Synthesis Type**: [analogical | structural | functional | mechanistic]
> **Exploration Status**: [unexplored | initial-notes | developing | mature]
> **Potential Value**: [high | medium | low]
> **Generativity**: [How many new insights might emerge?]
> 
> **Seed Questions**:
>   - [Question that might drive synthesis 1]
>   - [Question that might drive synthesis 2]
> 
> **Next Action**: [Specific step to explore this]
```
</callout_specification>

<inline_syntax>
### Inline Synthesis Markers

```markdown
%%SYNTHESIS: source=concept-name | targets=domain1,domain2,domain3 | type=analogical | status=unexplored | value=high%%

[**Synthesis-Potential**:: [[Source Concept]] ←bridges→ [[Target Domain]] | type:analogical | status:unexplored]
```
</inline_syntax>

<synthesis_types>
### Synthesis Type Definitions

| Type | Definition | Example |
|------|------------|---------|
| `analogical` | Structural similarity across domains | Attention allocation ↔ Economic resource allocation |
| `structural` | Same formal structure, different content | Graph theory ↔ Social networks ↔ Neural networks |
| `functional` | Same function, different mechanism | Working memory ↔ RAM ↔ Short-term buffers |
| `mechanistic` | Shared underlying causal mechanism | All learning as prediction error minimization |
| `metaphorical` | Illuminating but not rigorous parallel | Mind as computer (useful but imperfect) |
</synthesis_types>

<exploration_status>
### Status Definitions

| Status | Definition | Next Action |
|--------|------------|-------------|
| `unexplored` | Noticed but not investigated | Create exploration note |
| `initial-notes` | Some preliminary thinking | Develop structured comparison |
| `developing` | Active synthesis work | Refine and test framework |
| `mature` | Well-developed integration | Document and apply |
</exploration_status>

<generation_triggers>
### When to Flag Synthesis Potential

**High-Value Signals:**
- Concept has abstract structure applicable elsewhere
- You notice yourself thinking "this is like X"
- Framework seems domain-general despite specific origin
- Multiple fields use similar concepts with different names
- Explanatory mechanism seems fundamental
</generation_triggers>
</synthesis_potential_markers>
`````

---

### Module 14: Temporal Decay Indicators

`````xml
<temporal_decay_indicators>
## ⏰ Knowledge Freshness Protocol

Track information currency and trigger systematic review.

<frontmatter_specification>
### YAML Frontmatter Format

```yaml
---
freshness:
  domain-volatility: [stable | moderate | high | volatile]
  last-verified: YYYY-MM-DD
  decay-rate: [Xdays | Xweeks | Xmonths | Xyears]
  staleness-risk: [low | medium | high | critical]
  
update-triggers:
  - "[Event that should trigger review]"
  - "[Publication type that should trigger update]"
  
review-history:
  - date: YYYY-MM-DD
    action: "[What you checked/updated]"
    outcome: "[Still current | Updated X | Major revision]"
---
```
</frontmatter_specification>

<volatility_calibration>
### Domain Volatility Guide

| Level | Decay Rate | Examples |
|-------|------------|----------|
| `stable` | Years | Historical facts, foundational principles, well-established theories |
| `moderate` | 6-12 months | Established best practices, consensus positions |
| `high` | 1-6 months | Emerging research areas, technology practices |
| `volatile` | Days-weeks | Current events, rapidly evolving fields, AI/ML techniques |
</volatility_calibration>

<inline_syntax>
### Lightweight Inline Format

```markdown
%%FRESHNESS: volatility=high | verified=2025-05 | decay=3mo | risk=medium%%
```
</inline_syntax>

<staleness_indicators>
### Staleness Risk Assessment

| Risk Level | Definition | Action |
|------------|------------|--------|
| `low` | Well within freshness window | Normal review cycle |
| `medium` | Approaching review due date | Schedule review |
| `high` | Past typical decay period | Review soon |
| `critical` | Significantly outdated | Review immediately |
</staleness_indicators>

<update_trigger_patterns>
### Common Update Triggers

| Trigger Type | Example |
|--------------|---------|
| Publication | "New meta-analysis in this area" |
| Event | "Major conference with relevant findings" |
| Personal | "Applied this and found issues" |
| External | "Someone questioned this claim" |
| Systematic | "6 months since last verification" |
</update_trigger_patterns>

<generation_guidelines>
### When to Include Freshness Markers

**ALWAYS include for:**
- Topics in rapidly evolving fields
- Best practice recommendations
- Statistical claims that might be updated
- Technology-specific information

**Volatility Assessment Questions:**
- How often does this field publish updates?
- How recent is the source material?
- Are there ongoing debates that might resolve?
- Is this affected by changing technology/society?
</generation_guidelines>
</temporal_decay_indicators>
`````

---

### Module 15: Mental Model Anchors




`````xml
<mental_model_anchors>
## 🧭 Framework Integration Protocol

Explicitly connect concepts to foundational mental models.

<callout_specification>
### Mental Model Anchor Callout

```markdown
> [!mental-model-anchor] Concept Name
> **Primary Model Anchors**:
>   - [[Mental Model 1]] — [how this concept instantiates/applies the model]
>   - [[Mental Model 2]] — [connection explanation]
>   - [[Mental Model 3]] — [connection explanation]
> 
> **Model Application Notes**:
>   - [How thinking through Model 1 illuminates this concept]
>   - [What Model 2 lens reveals about this]
> 
> **Inverse Application** (this concept AS a mental model):
>   - Can be applied to: [Other domains where this concept works as a lens]
```
</callout_specification>

<inline_syntax>
### Inline Model Anchors

```markdown
[**Model-Anchor**:: [[Concept]] ←anchors-to→ [[Mental Model]] | insight:"what the connection reveals"]

[**Model-Application**:: [[Concept]] ←as-lens-for→ [[Target Domain]] | insight:"how concept illuminates domain"]
```
</inline_syntax>

<foundational_model_library>
### Core Mental Model Reference

| Model | Core Insight | Application Trigger |
|-------|--------------|---------------------|
| [[First Principles]] | Decompose to fundamentals | "What are the basic building blocks?" |
| [[Inversion]] | Solve by negation | "What would make this fail?" |
| [[Second-Order Effects]] | Consequences of consequences | "And then what?" |
| [[Systems Thinking]] | Interconnected wholes | "What are the feedback loops?" |
| [[Opportunity Cost]] | Value of alternatives foregone | "What am I giving up?" |
| [[Constraint Theory]] | Bottleneck identification | "What's the limiting factor?" |
| [[Circle of Competence]] | Know your limits | "Am I qualified to judge this?" |
| [[Map vs Territory]] | Models ≠ reality | "How accurate is this representation?" |
| [[Occam's Razor]] | Prefer simplicity | "Is there a simpler explanation?" |
| [[Falsification]] | Seeking disconfirmation | "How could this be wrong?" |
</foundational_model_library>

<bidirectional_application>
### Two-Way Model Use

**Concept → Model** (Anchoring):
"How does [[First Principles Thinking]] illuminate [[Cognitive Load Theory]]?"
→ CLT decomposes to: capacity limits + element interactivity + load types

**Concept → Lens** (Projection):
"How can [[Cognitive Load Theory]] serve as a lens for [[Software Architecture]]?"
→ Code complexity creates cognitive load; modular design reduces it
</bidirectional_application>

<generation_guidelines>
### When to Include Model Anchors

**ALWAYS anchor when:**
- Concept has clear structural parallel to known model
- Understanding deepens through model lens
- Concept itself functions as a mental model for other domains

**Model Selection Heuristic:**
- Which 2-3 models most illuminate this concept?
- Which models would an expert naturally invoke here?
- What model would help a novice understand faster?
</generation_guidelines>
</mental_model_anchors>
`````

---

### Module 16: Counterexample Collection

`````xml
<counterexample_collection>
## 🚧 Boundary Condition Protocol

Systematically document exceptions, edge cases, and limitations.

<callout_specification>
### Counterexample Callout

```markdown
> [!counterexample] Principle/Claim Name
> **Principle Statement**: [What the principle claims]
> 
> **Counterexample**: [Situation where principle fails]
> **Boundary Condition**: [What factor makes it fail]
> **Population/Context**: [Who/where it doesn't apply]
> **Source**: [Citation if empirical]
> 
> **Implication for Application**:
>   - [How to adjust when this boundary is hit]
>   - [What to do instead]
> 
> **Principle Revision** (if needed):
>   - Original: "[Broad claim]"
>   - Revised: "[More accurate, bounded claim]"
```
</callout_specification>

<inline_syntax>
### Inline Boundary Markers

```markdown
[**Boundary-Condition**:: [[Principle]] fails-when:"condition description" | population:"affected group" | alternative:"what to do instead"]

[**Counterexample**:: [[Claim]] negated-by:"specific case" | implication:"how this changes understanding"]

[**Exception**:: [[Rule]] except-when:"exception condition" | frequency:"how often this occurs"]
```
</inline_syntax>

<boundary_types>
### Boundary Condition Taxonomy

| Type | Definition | Example |
|------|------------|---------|
| `population` | Doesn't apply to certain groups | "Testing effect weaker for very low-knowledge learners" |
| `context` | Doesn't apply in certain settings | "Spacing effect reduced in high-pressure testing contexts" |
| `magnitude` | Only applies within certain ranges | "Desirable difficulty only when difficulty is moderate" |
| `temporal` | Doesn't apply at certain times | "Interleaving less effective in initial skill acquisition" |
| `interaction` | Moderated by other variables | "Expertise reversal effect—what helps novices hurts experts" |
| `methodological` | Only appears with certain methods | "Effect may be artifact of lab conditions" |
</boundary_types>

<exception_frequency>
### Exception Frequency Markers

| Marker | Meaning | Action |
|--------|---------|--------|
| `rare` | Unusual edge case | Note but apply principle normally |
| `occasional` | Happens sometimes | Check conditions before applying |
| `common` | Frequent exception | Always verify applicability |
| `systematic` | Predictable from theory | Build into standard application |
</exception_frequency>

<generation_guidelines>
### When to Document Counterexamples

**ALWAYS document when:**
- Source explicitly notes limitations
- You've encountered failure cases
- Population or context restrictions are known
- Moderating variables are documented

**Questions to Surface Counterexamples:**
- When does this NOT work?
- Who does this NOT help?
- Under what conditions does this reverse?
- What's the smallest viable context for this principle?
</generation_guidelines>
</counterexample_collection>
`````

---

## 🔧 Unified Integration Module

This master module combines the highest-priority systems into a single deployable component:

````xml
<enhanced_pkb_integration>
## 🧬 Enhanced PKB Integration Protocol v1.0

This unified module integrates: epistemic encoding, relationship typing, atomic extraction, and application context marking.

<activation_statement>
This protocol activates automatically for all substantive knowledge content. Claude will:
1. **Encode epistemic confidence** on all factual claims
2. **Type relationships** when establishing conceptual connections
3. **Signal atomic candidates** within reference notes
4. **Mark application contexts** for actionable knowledge
</activation_statement>

<integrated_output_example>
### Example: Integrated Output Demonstration

```markdown
---
tags: #cognitive-psychology #attention #reference-note
aliases: [Kahneman Capacity Model, Resource Theory of Attention]
cognitive-load:
  intrinsic: high
  element-interactivity: 7
prerequisites:
  hard: ["[[information-processing-theory]]", "[[arousal-theory]]"]
freshness:
  domain-volatility: stable
  last-verified: 2025-05
---
```
# Capacity Model of Attention (Kahneman 1973)

[**Capacity-Model-Definition**:: a framework proposing that attention operates through a limited pool of undifferentiated processing resources, allocated dynamically based on task demands, arousal level, and strategic priorities]^established-stable

%%ATOMIC: capacity-model-kahneman | framework | critical | foundational-attention-theory%%

## Core Components

The model comprises several interacting elements:

[**Arousal-Capacity-Relationship**:: arousal modulates total available resources along an inverted-U function]^verified-stable
^source:: [[ref-kahneman-1973]] p.47
^evidence-type:: theoretical-claim

[**Theoretical-Foundation**:: [[Capacity Model]] →(builds-on)→ [[Yerkes-Dodson Law]] + [[Information Processing Theory]]]

%%QUERY-ANCHOR: attention:capacity-model-components%%

> [!application-context] Capacity Model Application
> **Domains**: 
>   - [[Instructional Design]] — predict when learners will be overwhelmed
>   - [[UX Design]] — interface complexity management
> **Trigger Conditions**:
>   - "Learner performance degrades under stress" → check arousal level
>   - "Dual-task interference observed" → resources exhausted
> **Anti-Patterns**:
>   - Assuming capacity is fixed (it fluctuates with arousal)

> [!counterexample] Capacity Model Limitations
> **Principle**: Single undifferentiated resource pool
> **Counterexample**: Modality-specific interference patterns suggest multiple pools
> **Boundary Condition**: Model may oversimplify for cross-modal tasks
> **Alternative**: Consider [[Multiple Resource Theory]] for complex interfaces

</integrated_output_example>

<priority_integration_matrix>
### Integration Priority by Note Type

| Note Type | Epistemic | Relations | Atomic | Application | Load | Evidence |
|-----------|:---------:|:---------:|:------:|:-----------:|:----:|:--------:|
| Reference Note | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓ | ✓✓ | ✓✓✓ |
| Atomic Note | ✓✓ | ✓✓ | — | ✓✓✓ | ✓ | ✓✓ |
| MOC | ✓ | ✓✓✓ | — | ✓ | — | — |
| Synthesis Note | ✓✓✓ | ✓✓✓ | ✓ | ✓✓ | ✓✓ | ✓✓ |

Legend: ✓✓✓ = Always include | ✓✓ = Usually include | ✓ = Sometimes include | — = Rarely needed
</priority_integration_matrix>

<density_guidelines>
### Overall Density Targets

Per major section of a reference note:
- Epistemic markers: 3-6 claims marked
- Relationship encodings: 2-4 typed links
- Atomic candidates: 1-3 flagged
- Application contexts: 1-2 per applicable concept
- Evidence markers: On all empirical claims
- SR hooks: 3-5 for key content
</density_guidelines>

<validation_checklist>
### Pre-Output Validation

Before finalizing enhanced PKB content, verify:

**Epistemic Layer:**
- [ ] All substantive claims have confidence markers
- [ ] Markers match actual evidence strength
- [ ] Personal synthesis distinguished from consensus

**Relationship Layer:**
- [ ] Key conceptual relationships are typed
- [ ] Relationship types are semantically accurate
- [ ] Bidirectional link opportunities identified

**Extraction Layer:**
- [ ] Atomizable concepts flagged
- [ ] Priority levels assigned appropriately
- [ ] Extraction triggers documented

**Application Layer:**
- [ ] Actionable concepts have application contexts
- [ ] Trigger conditions are specific and observable
- [ ] Anti-patterns noted where relevant

**Meta Layer:**
- [ ] Cognitive load indicators present (for complex notes)
- [ ] Freshness parameters set (for volatile topics)
- [ ] Mental model anchors identified (for frameworks)
</validation_checklist>
</enhanced_pkb_integration>
`````

---

# 🔗 Related Topics for PKB Expansion

1. **[[Dataview Query Library for PKB Integration]]**
   - *Connection*: All these markers become powerful with systematic queries
   - *Depth Potential*: Complete query cookbook for each marker type
   - *Knowledge Graph Role*: Operational bridge between encoding and retrieval

2. **[[Obsidian Automation Workflows for Marker Processing]]**
   - *Connection*: Transform markers into automated vault maintenance
   - *Depth Potential*: Templater scripts, QuickAdd macros, periodic note reviews
   - *Knowledge Graph Role*: Technical implementation layer

3. **[[Epistemology for Knowledge Workers]]**
   - *Connection*: Theoretical foundation for confidence calibration
   - *Depth Potential*: When to trust claims, evidence evaluation frameworks
   - *Knowledge Graph Role*: Conceptual grounding for epistemic markers

4. **[[Zettelkasten Atomicity Principles]]**
   - *Connection*: Theory behind atomic extraction decisions
   - *Depth Potential*: What makes a good atomic note, granularity decisions
   - *Knowledge Graph Role*: Methodological foundation for extraction signals

---

---

### 📖 Extracted Definitions
```dataviewjs
const currentFile = dv.current().file;
const content = await dv.io.load(currentFile.path);
const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;

let definitions = [];
let match;

while ((match = bracketedFieldRegex.exec(content)) !== null) {
    definitions.push({
        key: match[1].trim(),
        value: match[2].trim()
    });
}

// Group by first letter
const grouped = {};
definitions.forEach(d => {
    const firstLetter = d.key[0].toUpperCase();
    if (!grouped[firstLetter]) grouped[firstLetter] = [];
    grouped[firstLetter].push(d);
});

// Display grouped results
const sortedLetters = Object.keys(grouped).sort();

for (let letter of sortedLetters) {
    dv.header(4, `${letter}`);
    dv.table(
        ["Term", "Definition"],
        grouped[letter].map(d => [`**${d.key}**`, d.value])
    );
}
`````





I'll analyze this brilliant foundation and significantly expand it with additional integration systems, then provide complete modular prompt components for everything.

---
tags: #prompt-engineering #pkb-architecture #obsidian #dataview-integration #reference-note #llm-integration
aliases: [LLM PKB Integration Systems, Claude PKB Modules, Agentic Knowledge Encoding]
---

# 🧠 Comprehensive LLM-PKB Integration Systems

## Executive Analysis

Your proposed integration enhancements represent a sophisticated evolution from **static knowledge capture** to **dynamic, queryable, self-documenting knowledge architecture**. The core insight driving all nine proposals is this: <span style='color: #FFC700;'>**metadata isn't overhead—it's infrastructure**</span>. Each marker, tag, and encoded relationship transforms flat text into a machine-traversable semantic graph while remaining human-readable.

Let me expand each existing proposal and introduce six additional systems I've identified as high-value gaps in the current architecture.

---

## 📊 Expanded Analysis of Existing Proposals

### 1. Confidence Markers — Epistemic Status Encoding

> [!principle-point] Core Innovation
> [**Epistemic-Encoding**:: the practice of explicitly marking the certainty level of knowledge claims, enabling both human judgment calibration and machine-queryable evidence quality filtering.]

Your proposal correctly identifies that <span style='color: #FF00DC;'>undifferentiated claims create false equivalence</span>—a replicated meta-analysis finding and a single blog post opinion appear identically authoritative in standard notes.

**Expansion Opportunities:**

The five-tier system (`verified`, `established`, `provisional`, `speculative`, `contested`) could benefit from two additional dimensions:

1. <span style='color: #72FFF1;'>**Temporal Stability**</span>: Some claims are verified *but volatile* (e.g., current best practices in rapidly evolving fields). Add `^stable` vs `^volatile` modifiers.

2. <span style='color: #72FFF1;'>**Personal vs. Consensus**</span>: Distinguish between "the field believes X" and "I believe X based on my synthesis." Add `^consensus` vs `^personal-synthesis` markers.

**Enhanced Marker Taxonomy:**
```
[**Claim**:: value]^verified-stable          # Replicated, unlikely to change
[**Claim**:: value]^established-volatile     # Accepted now, field evolving
[**Claim**:: value]^provisional-consensus    # Tentative, but field agrees
[**Claim**:: value]^speculative-personal     # My hypothesis, not field's
[**Claim**:: value]^contested-active         # Ongoing debate
```

---

### 2. Bidirectional Link Hints — Relationship Typing

> [!principle-point] Core Innovation
> [**Semantic-Link-Typing**:: encoding the *nature* of conceptual relationships rather than merely their *existence*, transforming wiki-links from navigational shortcuts into knowledge graph edges with queryable properties.]

Your relationship vocabulary is excellent. I'd expand it with additional relationship types critical for [[Cognitive Science]] and [[Learning Theory]] domains:

**Extended Relationship Vocabulary:**

| Type | Symbol | Use Case | Example |
|------|--------|----------|---------|
| `extends` | →(extends)→ | Theoretical elaboration | [[CLT]] →(extends)→ [[Information Processing]] |
| `operationalizes` | →(operationalizes)→ | Abstract → measurable | [[Intrinsic Load]] →(operationalizes)→ [[Element Interactivity]] |
| `analogous-to` | →(analogous-to)→ | Cross-domain parallel | [[Working Memory]] →(analogous-to)→ [[RAM]] |
| `precondition-for` | →(precondition-for)→ | Logical dependency | [[Schema Acquisition]] →(precondition-for)→ [[Automation]] |
| `falsifies` | →(falsifies)→ | Empirical refutation | [[Late Selection Evidence]] →(falsifies)→ [[Early Selection Theory]] |
| `synthesizes` | →(synthesizes)→ | Integration of multiple | [[Load Theory]] →(synthesizes)→ [[CLT]] + [[Perceptual Load]] |

---

### 3. Atomic Extraction Markers — Note Spawning Signals

> [!principle-point] Core Innovation
> [**Extraction-Signaling**:: explicit markers within reference notes that flag embedded concepts as candidates for standalone atomic note creation, enabling systematic vault expansion workflows.]

Your `%%ATOMIC%%` syntax is clean. I'd enhance the metadata captured:

**Enhanced Atomic Candidate Schema:**
```markdown
> [!atomic-candidate] Filter Model (Broadbent 1958)
> **Slug**: `filter-model-broadbent-1958`
> **Note Type**: atomic-concept
> **Priority**: critical
> **Estimated Length**: 400-600 words
> **Key Relationships**: 
>   - →(superseded-by)→ [[Attenuation Model]]
>   - →(builds-on)→ [[Information Processing Theory]]
>   - →(tested-via)→ [[Dichotic Listening Paradigm]]
> **Source Coverage**: Needs primary source review
> **Extraction Trigger**: Referenced 3+ times in current vault
```

The addition of <span style='color: #72FFF1;'>**Extraction Trigger**</span> creates an auditable rationale for why this concept deserves atomization.

---

### 4-9. Remaining Proposals — Summary Enhancements

> [!abstract] Quick Enhancement Notes
> 
> **SR Integration**: Add `%%SR-INTERLEAVE%%` markers for concepts that should be mixed during review (combats [[Illusion of Competence]]).
> 
> **Source Provenance**: Add `^primary` vs `^secondary` source type markers; enable "trace to primary" queries.
> 
> **Prerequisite Mapping**: Add `soft-prerequisite` (helpful but not required) vs `hard-prerequisite` (must understand first).
> 
> **Semantic Versioning**: Add `breaking-change` flags when understanding fundamentally shifts (not just accumulates).
> 
> **Query Anchors**: Namespace anchors by domain: `%%QA:attention:all-theories%%` vs `%%QA:memory:encoding-types%%`.
> 
> **Contradiction Markers**: Add `resolution-attempted` field tracking your synthesis efforts.

---

## 🆕 Novel Integration Systems

Based on gaps in the current architecture, I propose six additional high-value systems:

---

### 10. **Cognitive Load Indicators** — Study Session Optimization

<span style='color: #FFC700;'>**Problem**</span>: Notes vary dramatically in cognitive demand, but nothing signals this to future-you planning a study session.

<span style='color: #27FF00;'>**Solution**</span>: Embed complexity indicators enabling intelligent study session construction.

```markdown
---
cognitive-load:
  intrinsic: high          # Inherent complexity of material
  element-interactivity: 8 # Scale 1-10
  prerequisite-count: 5    # Number of concepts assumed known
  estimated-passes: 3      # Times needed for mastery
  optimal-state: "alert, caffeinated, 45min+ available"
---

<!-- Or inline -->
%%LOAD: intrinsic=high | interactivity=8 | passes=3%%
```

**PKB Value**: Filter notes by available cognitive bandwidth; build progressive difficulty queues; avoid overwhelm.

---

### 11. **Application Context Markers** — Transfer Facilitation

<span style='color: #FFC700;'>**Problem**</span>: Knowledge captured but no encoding of *where/when* to apply it.

<span style='color: #27FF00;'>**Solution**</span>: Explicit application domain and trigger condition markers.

```markdown
> [!application-context] Cognitive Load Theory
> **Domains**: 
>   - [[Instructional Design]] — curriculum sequencing
>   - [[UX Design]] — interface complexity management
>   - [[Prompt Engineering]] — chunk complexity calibration
> **Trigger Conditions**:
>   - "Learner seems overwhelmed" → reduce extraneous load
>   - "Material isn't sticking" → check element interactivity
>   - "Expert blind spot detected" → scaffold missing schemas
> **Anti-Patterns**:
>   - Applying to entertainment content (not learning context)
>   - Ignoring individual differences in prior knowledge

[**Application-Domain**:: [[Prompt Engineering]] | trigger:"complex instructions failing" | action:"decompose into sequential steps"]
```

**PKB Value**: Query "what knowledge applies to X situation"; build domain-specific toolkits; reduce [[Inert Knowledge]] problem.

---

### 12. **Evidence Weight Indicators** — Epistemological Rigor

<span style='color: #FFC700;'>**Problem**</span>: "Research shows…" conflates single underpowered study with robust meta-analysis.

<span style='color: #27FF00;'>**Solution**</span>: Hierarchical evidence typing following [[Evidence-Based Practice]] standards.

```markdown
<!-- Evidence hierarchy markers -->
[**Finding**:: claim here]^evidence:meta-analysis
[**Finding**:: claim here]^evidence:rct
[**Finding**:: claim here]^evidence:observational
[**Finding**:: claim here]^evidence:case-study
[**Finding**:: claim here]^evidence:expert-opinion
[**Finding**:: claim here]^evidence:anecdote

<!-- Enhanced with sample size and effect -->
[**Spacing-Effect**:: distributed practice improves retention]^evidence:meta-analysis|n=29000|d=0.42
```

**PKB Value**: Filter claims by evidence quality; identify knowledge areas needing stronger foundations; calibrate confidence appropriately.

---

### 13. **Synthesis Potential Markers** — Cross-Domain Opportunity Flags

<span style='color: #FFC700;'>**Problem**</span>: Valuable cross-domain connections remain latent because no mechanism flags synthesis opportunities.

<span style='color: #27FF00;'>**Solution**</span>: Explicit markers identifying concepts ripe for interdisciplinary integration.

```markdown
> [!synthesis-opportunity] Attention as Resource Allocation
> **Source Domain**: [[Cognitive Psychology]] — [[Kahneman Capacity Model]]
> **Target Domains**: 
>   - [[Economics]] — scarcity/allocation parallels
>   - [[Computer Science]] — CPU scheduling algorithms
>   - [[Organizational Behavior]] — team cognitive bandwidth
> **Synthesis Type**: analogical-transfer
> **Exploration Status**: unexplored
> **Potential Value**: high (novel framework possible)

%%SYNTHESIS: source=kahneman-capacity | targets=economics,cs-scheduling | status=unexplored%%
```

**PKB Value**: Systematic innovation cultivation; directed cross-domain reading; novel framework generation.

---

### 14. **Temporal Decay Indicators** — Knowledge Freshness Tracking

<span style='color: #FFC700;'>**Problem**</span>: Fields evolve; notes become stale; no mechanism signals when review/update is needed.

<span style='color: #27FF00;'>**Solution**</span>: Domain-specific decay rates and review triggers.

```markdown
---
freshness:
  domain-volatility: high    # How fast does this field move?
  last-verified: 2025-01-15  # When did you confirm currency?
  decay-rate: 6-months       # Review interval
  staleness-risk: medium     # Current status
  update-triggers:
    - "New major publication in field"
    - "Paradigm shift indicators"
    - "Personal confusion when applying"
---

%%FRESHNESS: volatility=high | verified=2025-01 | decay=6mo | status=current%%
```

**PKB Value**: Automated review queues; field-appropriate update scheduling; prevent outdated knowledge application.

---

### 15. **Mental Model Anchors** — Framework Integration Points

<span style='color: #FFC700;'>**Problem**</span>: Individual concepts exist but aren't explicitly connected to overarching mental models that organize understanding.

<span style='color: #27FF00;'>**Solution**</span>: Explicit anchoring of concepts to foundational thinking frameworks.

```markdown
> [!mental-model-anchor] 
> **Concept**: [[Cognitive Load Theory]]
> **Anchors To**:
>   - [[Systems Thinking]] — feedback loops between load types
>   - [[Constraint Theory]] — bottleneck identification
>   - [[First Principles Thinking]] — decomposition to element level
>   - [[Inversion]] — what would INCREASE load? (avoid that)
> **Integration Notes**: CLT is fundamentally a constraint/bottleneck model applied to cognition

[**Model-Anchor**:: [[Cognitive Load Theory]] ←anchors-to→ [[Constraint Theory]] | insight:"learning bottlenecks = cognitive constraints"]
```

**PKB Value**: Rapid sense-making through framework activation; transferable reasoning patterns; metacognitive scaffolding.

---

### 16. **Counterexample Collection** — Edge Case Tracking

<span style='color: #FFC700;'>**Problem**</span>: Principles captured without boundary conditions; overgeneralization risk.

<span style='color: #27FF00;'>**Solution**</span>: Systematic counterexample and exception documentation.

```markdown
> [!counterexample] Testing Effect Limitations
> **Principle**: [[Testing Effect]] — retrieval practice enhances retention
> **Counterexample**: Very low-knowledge learners may benefit more from restudy initially
> **Boundary Condition**: Requires sufficient initial encoding to retrieve
> **Source**: Karpicke & Blunt, 2011
> **Implication**: Scaffold before testing for novices

[**Boundary-Condition**:: [[Testing Effect]] fails-when: "initial encoding insufficient" | population:"absolute novices" | alternative:"restudy then test"]
```

**PKB Value**: Nuanced principle application; prevent overgeneralization; track edge cases systematically.

---

## 🔧 Complete Modular Prompt Components

Below are production-ready prompt components for all 16 systems. Each is designed for independent insertion into your agent architecture.

---

### Module 1: Epistemic Confidence Encoding

```xml
<epistemic_confidence_encoding>
## 🎯 Epistemic Status Encoding Protocol

When generating knowledge claims, explicitly encode confidence levels using inline markers.

<confidence_taxonomy>
### Primary Confidence Levels

| Marker | Definition | Typical Source | Visual |
|--------|------------|----------------|--------|
| `^verified` | Multiple independent replications; scientific consensus | Meta-analyses, systematic reviews | 🟢 |
| `^established` | Widely accepted in field; standard textbook content | Authoritative texts, review papers | 🔵 |
| `^provisional` | Single study, recent finding, limited replication | Primary research, recent publications | 🟡 |
| `^speculative` | Theoretical inference, hypothesized relationship | Personal synthesis, theoretical papers | 🟠 |
| `^contested` | Active scholarly debate; conflicting evidence | Debate literature, response papers | 🔴 |

### Secondary Modifiers (Optional)

| Modifier | Meaning | Use Case |
|----------|---------|----------|
| `-stable` | Unlikely to change significantly | Well-established principles |
| `-volatile` | Field actively evolving; may shift | Cutting-edge domains |
| `-consensus` | Represents field agreement | Distinguishing from personal view |
| `-personal` | Personal synthesis, not field consensus | Original analysis |
</confidence_taxonomy>

<syntax_specification>
### Syntax Patterns

**Basic Format:**
```markdown
[**Field-Name**:: claim content]^confidence-level
```

**With Secondary Modifier:**
```markdown
[**Field-Name**:: claim content]^confidence-level-modifier
```

**Examples:**
```markdown
[**Spacing-Effect**:: distributed practice produces superior retention to massed practice]^verified-stable

[**Desirable-Difficulties**:: conditions that slow initial learning but enhance long-term retention]^established-consensus

[**AI-Consciousness**:: large language models may develop emergent self-models]^speculative-personal

[**Retrieval-Practice-Mechanisms**:: testing effect operates via elaborative retrieval processes]^provisional-volatile

[**Learning-Styles-Validity**:: matching instruction to preferences improves outcomes]^contested-active
```
</syntax_specification>

<generation_heuristics>
### When to Apply Each Level

**^verified**: Apply when:
- Multiple meta-analyses converge
- Effect replicated across labs, populations, contexts
- No serious methodological challenges remain
- Would be surprising if overturned

**^established**: Apply when:
- Appears in authoritative textbooks
- Cited without hedging in review papers
- Taught as standard curriculum content
- Limited ongoing debate

**^provisional**: Apply when:
- Based on single study or limited samples
- Published within last 2-3 years without replication
- Methodology sound but awaiting confirmation
- From reputable source but not yet consensus

**^speculative**: Apply when:
- Personal theoretical inference
- Extrapolating from adjacent domains
- "If X is true, then Y should follow" reasoning
- No direct empirical test yet

**^contested**: Apply when:
- Prominent researchers disagree
- Response/rebuttal papers exist
- Replication attempts show mixed results
- Active debate in journals
</generation_heuristics>

<integration_notes>
### Dataview Query Compatibility

These markers enable queries like:

```dataview
TABLE file.name as "Note", confidence
FROM "permanent-notes"
WHERE contains(file.content, "^speculative")
SORT file.mtime DESC
```

### Output Requirements
- Every substantive claim in reference notes SHOULD have confidence encoding
- Definitions from authoritative sources: `^established` minimum
- Personal syntheses: `^speculative-personal` or `^provisional-personal`
- Density: 40-60% of inline fields should carry confidence markers
</integration_notes>
</epistemic_confidence_encoding>
```

---

### Module 2: Semantic Relationship Typing

```xml
<semantic_relationship_typing>
## 🔗 Link Relationship Encoding Protocol

When establishing connections between concepts, encode the semantic relationship type.

<relationship_vocabulary>
### Core Relationship Types

| Relationship | Symbol | Definition | Use Case |
|--------------|--------|------------|----------|
| `builds-on` | →(builds-on)→ | Theoretical foundation | B extends/requires A |
| `supersedes` | →(supersedes)→ | Historical replacement | B replaces A |
| `contradicts` | →(contradicts)→ | Logical/empirical conflict | A and B incompatible |
| `supports` | →(supports)→ | Evidential backing | A provides evidence for B |
| `modulates` | →(modulates)→ | Causal influence | A affects magnitude of B |
| `instantiates` | →(instantiates)→ | Example of category | A is instance of B |
| `developed-by` | →(developed-by)→ | Attribution | B created A |
| `applied-in` | →(applied-in)→ | Practical domain | A is applied in context B |
| `extends` | →(extends)→ | Elaboration | B expands scope of A |
| `operationalizes` | →(operationalizes)→ | Abstract to measurable | B makes A testable |
| `analogous-to` | →(analogous-to)→ | Cross-domain parallel | A structurally similar to B |
| `precondition-for` | →(precondition-for)→ | Logical dependency | A must exist for B |
| `falsifies` | →(falsifies)→ | Empirical refutation | A disproves B |
| `synthesizes` | →(synthesizes)→ | Integration | C combines A + B |
| `component-of` | →(component-of)→ | Part-whole | A is part of B |
| `contrasts-with` | →(contrasts-with)→ | Distinguished from | A differs meaningfully from B |
</relationship_vocabulary>

<syntax_specification>
### Syntax Patterns

**Inline Field Format (Recommended):**
```markdown
[**Relationship-Type**:: [[Source]] →(relation)→ [[Target]]]
```

**Narrative Integration:**
```markdown
[[Cognitive Load Theory]] →(builds-on)→ [[Working Memory Model]] and →(extends)→ [[Information Processing Theory]].
```

**Complex Multi-Relation:**
```markdown
[**Theoretical-Lineage**:: [[Filter Model]] →(superseded-by)→ [[Attenuation Model]] →(integrated-into)→ [[Capacity Model]]]
```

**With Annotations:**
```markdown
[**Relationship**:: [[CLT]] →(applied-in)→ [[Instructional Design]] | annotation:"primary application domain since 1980s"]
```
</syntax_specification>

<generation_heuristics>
### Relationship Selection Guide

**Temporal/Historical Relations:**
- `supersedes`: Theory A historically replaced by Theory B
- `builds-on`: Theory B emerged from foundation of Theory A
- `developed-by`: Attribution to researcher/theorist

**Logical/Structural Relations:**
- `component-of`: Part-whole relationships
- `precondition-for`: Necessary conditions
- `instantiates`: Example-category relationships
- `operationalizes`: Abstract-concrete mappings

**Evidential Relations:**
- `supports`: Evidence favoring a claim
- `falsifies`: Evidence against a claim
- `contradicts`: Incompatible claims

**Functional Relations:**
- `modulates`: Causal/influence relationships
- `applied-in`: Domain of application
- `extends`: Scope expansion

**Comparative Relations:**
- `analogous-to`: Cross-domain structural similarity
- `contrasts-with`: Meaningful distinction
- `synthesizes`: Integration of multiple sources
</generation_heuristics>

<output_requirements>
### Density Guidelines

- Reference notes: 8-15 explicit relationship encodings
- MOCs: Heavy relationship typing (primary purpose)
- Atomic notes: 2-5 key relationships minimum
- Always encode when introducing how concepts relate
</output_requirements>
</semantic_relationship_typing>
```

---

### Module 3: Atomic Extraction Signaling

```xml
<atomic_extraction_signaling>
## 🧬 Note Spawning Protocol

When generating reference notes, identify concepts warranting atomic note extraction.

<extraction_criteria>
### Atomic Candidate Identification

**ALWAYS flag when:**
- Named theory, model, or framework with distinct identity
- Named researcher with significant contribution to topic
- Technical term with >50 words of explanation needed
- Principle or law with broad applicability
- Phenomenon with dedicated research literature
- Method or technique with procedural steps

**CONSIDER flagging when:**
- Concept referenced 3+ times across vault
- Term likely to appear in multiple domains
- Definition contested or evolved over time
- Practical applications warrant separate treatment

**DO NOT flag:**
- Generic terms with dictionary definitions
- Passing mentions without substantive explanation
- Concepts already atomized elsewhere in vault
</extraction_criteria>

<callout_specification>
### Atomic Candidate Callout Structure

```markdown
> [!atomic-candidate] Concept Name (Attribution Year)
> **Slug**: `kebab-case-identifier`
> **Note Type**: [atomic-concept | principle | framework | theorist | method | phenomenon]
> **Priority**: [critical | high | medium | low]
> **Estimated Scope**: [word count range]
> **Key Relationships**:
>   - →(relation)→ [[Related Concept 1]]
>   - →(relation)→ [[Related Concept 2]]
> **Source Status**: [needs-primary-review | has-primary | secondary-only]
> **Extraction Trigger**: [rationale for flagging]
```
</callout_specification>

<inline_alternative>
### Lightweight Inline Syntax

For rapid marking without full callout:

```markdown
%%ATOMIC: slug-name | note-type | priority | trigger-reason%%
```

**Examples:**
```markdown
%%ATOMIC: filter-model-broadbent | framework | high | foundational-attention-theory%%
%%ATOMIC: allocation-policy | atomic-concept | critical | central-to-capacity-model%%
%%ATOMIC: yerkes-dodson-law | principle | medium | frequently-referenced%%
```
</inline_alternative>

<note_type_definitions>
### Note Type Classifications

| Type | Definition | Typical Length | Example |
|------|------------|----------------|---------|
| `atomic-concept` | Single well-defined idea | 300-600 words | Intrinsic Load |
| `principle` | Generalizable rule/law | 400-800 words | Spacing Effect |
| `framework` | Multi-component model | 800-1500 words | Cognitive Load Theory |
| `theorist` | Researcher biography + contributions | 600-1000 words | Daniel Kahneman |
| `method` | Procedural technique | 500-1000 words | Retrieval Practice |
| `phenomenon` | Observed effect/pattern | 400-800 words | Testing Effect |
</note_type_definitions>

<priority_definitions>
### Priority Level Guidelines

| Priority | Definition | Action Timeline |
|----------|------------|-----------------|
| `critical` | Core concept for current project | Extract immediately |
| `high` | Important for domain understanding | Extract this week |
| `medium` | Valuable but not urgent | Add to extraction queue |
| `low` | Nice-to-have, low frequency | Extract when relevant |
</priority_definitions>

<output_requirements>
### Generation Guidelines

- Place atomic markers immediately after relevant content
- Reference notes should yield 3-8 atomic candidates typically
- Use callout format for high/critical priority items
- Use inline format for medium/low priority items
- Always include extraction trigger rationale
</output_requirements>
</atomic_extraction_signaling>
```

---

### Module 4: Spaced Repetition Integration

```xml
<spaced_repetition_integration>
## 🔄 SR Hook Generation Protocol

Generate spaced repetition compatible markers for key knowledge elements.

<card_types>
### SR Card Type Specifications

**Type 1: Basic Q&A**
```markdown
%%SR-CARD%%
Q: [Clear, specific question targeting single concept]
A: [Concise, complete answer]
%%END-SR%%
```

**Type 2: Cloze Deletion**
```markdown
%%SR-CLOZE%%
[Sentence with {{c1::key term}} for deletion and {{c2::another term}} if needed]
%%END-SR%%
```

**Type 3: Inline Quick-Review**
```markdown
%%SR: [prompt/question] → [response/answer]%%
```

**Type 4: Comparison Card**
```markdown
%%SR-COMPARE%%
Concept A: [Name]
Concept B: [Name]
Key Difference: [Distinguishing feature]
%%END-SR%%
```

**Type 5: Interleaving Marker** (for related cards to mix)
```markdown
%%SR-INTERLEAVE: topic-group-name%%
[Card content]
%%END-SR%%
```
</card_types>

<generation_triggers>
### When to Generate SR Hooks

**ALWAYS generate for:**
- Every formal definition (`[**Definition-Field**:: value]`)
- Every named principle or law
- Every key distinction/contrast
- Core framework components
- Critical procedural steps

**CONSIDER generating for:**
- Supporting examples that illuminate concepts
- Common misconceptions (what it's NOT)
- Application trigger conditions
- Historical context (who/when/why)

**Avoid generating for:**
- Meta-commentary and transitions
- Self-evident statements
- Content better learned through application than memorization
</generation_triggers>

<card_quality_standards>
### High-Quality Card Characteristics

**Questions should:**
- Target exactly ONE piece of knowledge
- Be unambiguous (only one correct answer)
- Use consistent terminology with source material
- Test understanding, not just recognition

**Answers should:**
- Be complete without being verbose
- Match the specificity of the question
- Use the same phrasing as the source when precision matters

**Cloze deletions should:**
- Delete meaningful terms, not filler words
- Maintain sentence comprehensibility with deletion
- Number deletions for multi-card generation (c1, c2, c3)
</card_quality_standards>

<examples>
### Generation Examples

**From Definition:**
```markdown
[**Cognitive-Load**:: the total mental effort being used in working memory during information processing]

%%SR-CARD%%
Q: What is cognitive load?
A: The total mental effort being used in working memory during information processing.
%%END-SR%%

%%SR-CLOZE%%
{{c1::Cognitive load}} refers to the total {{c2::mental effort}} being used in {{c3::working memory}} during information processing.
%%END-SR%%
```

**From Distinction:**
```markdown
[**Intrinsic-vs-Extraneous**:: intrinsic load stems from material complexity; extraneous load stems from poor instructional design]

%%SR-COMPARE%%
Concept A: Intrinsic Load
Concept B: Extraneous Load
Key Difference: Intrinsic stems from material complexity (unavoidable); extraneous stems from poor design (reducible).
%%END-SR%%
```

**From Principle:**
```markdown
[**Spacing-Effect**:: distributed practice produces better retention than massed practice]

%%SR-CARD%%
Q: What does the spacing effect predict about practice distribution?
A: Distributed practice produces better long-term retention than massed practice of equivalent duration.
%%END-SR%%

%%SR-CLOZE%%
The {{c1::spacing effect}} demonstrates that {{c2::distributed}} practice produces better retention than {{c3::massed}} practice.
%%END-SR%%
```
</examples>

<density_guidelines>
### Output Requirements

- **Reference notes**: 5-12 SR hooks per major section
- **Atomic notes**: 2-4 SR hooks (focused coverage)
- **Prioritize**: Definitions, principles, distinctions, procedures
- **Interleaving**: Group related cards with `%%SR-INTERLEAVE%%` tags
</density_guidelines>
</spaced_repetition_integration>
```

---

### Module 5: Source Provenance Chains

```xml
<source_provenance_chains>
## 📚 Citation Traceability Protocol

Encode source attribution enabling claim-to-evidence traceability.

<provenance_syntax>
### Inline Provenance Markers

**Basic Source Attribution:**
```markdown
[**Claim-Name**:: claim content]
^source:: [[ref-author-year-title]] p.XX
^evidence-type:: [type]
^status:: [replication-status]
```

**Compact Inline Format:**
```markdown
[**Claim**:: value | src:author-year:pXX | evidence:type | status:level]
```

**Narrative Integration:**
```markdown
<span style='color: #FF5700;'>According to Kahneman (1973, p.47)</span>, [**Arousal-Capacity-Claim**:: arousal modulates total available capacity along an inverted-U function]^verified.
```
</provenance_syntax>

<evidence_type_taxonomy>
### Evidence Classification

| Type | Definition | Weight |
|------|------------|--------|
| `meta-analysis` | Systematic synthesis of multiple studies | Highest |
| `systematic-review` | Comprehensive literature review | Very High |
| `rct` | Randomized controlled trial | High |
| `quasi-experimental` | Non-randomized comparison | Moderate-High |
| `observational` | Correlational, cohort, case-control | Moderate |
| `case-study` | Single case or small n | Low-Moderate |
| `theoretical-claim` | Logical/theoretical argument | Variable |
| `expert-opinion` | Authority without data | Low |
| `anecdote` | Personal experience | Very Low |
</evidence_type_taxonomy>

<source_type_markers>
### Source Classification

| Marker | Meaning |
|--------|---------|
| `^primary` | Original research/data source |
| `^secondary` | Review, textbook, summary |
| `^tertiary` | Encyclopedia, handbook |
| `^personal` | Personal observation/synthesis |
</source_type_markers>

<reference_note_format>
### Structured Reference Entry

```markdown
> [!reference] author-year-short-title
> **Full Citation**: [Complete citation in preferred format]
> **Type**: [book | article | chapter | report | thesis]
> **Access**: [DOI/URL/Library]
> **Key Claims Sourced**:
>   - [[Claim-Name-1]]^pXX
>   - [[Claim-Name-2]]^pYY
> **Quality Assessment**: [Methodological notes]
> **Personal Notes**: [Your evaluation]
```
</reference_note_format>

<generation_guidelines>
### When to Include Provenance

**ALWAYS include for:**
- Empirical claims with specific findings
- Statistics, percentages, effect sizes
- Direct quotations or close paraphrases
- Controversial or contested claims
- Claims that might be challenged

**CONSIDER including for:**
- Historical attributions (who said/did what when)
- Technical definitions from specific sources
- Methodological recommendations

**MAY omit for:**
- Common knowledge in the field
- Your own syntheses (mark as `^personal` instead)
- Logical deductions from established principles
</generation_guidelines>

<query_compatibility>
### Dataview Integration

Enable queries like:
```dataview
LIST FROM "permanent-notes"
WHERE contains(file.content, "evidence:anecdote")
```

```dataview
TABLE claim, source
FROM "cognitive-science"
WHERE contains(file.content, "^status::unverified")
```
</query_compatibility>
</source_provenance_chains>
```

---

### Module 6: Prerequisite Dependency Mapping

```xml
<prerequisite_dependency_mapping>
## 🗺️ Learning Path Encoding Protocol

Explicitly declare knowledge dependencies enabling automated learning path generation.

<frontmatter_specification>
### YAML Frontmatter Format

```yaml
---
prerequisites:
  hard:
    - "[[concept-slug-1]]"  # Must understand first
    - "[[concept-slug-2]]"
  soft:
    - "[[concept-slug-3]]"  # Helpful but not required
    - "[[concept-slug-4]]"
enables:
  direct:
    - "[[concept-slug-5]]"  # Directly unlocks
    - "[[concept-slug-6]]"
  related:
    - "[[concept-slug-7]]"  # Benefits from this knowledge
difficulty: [foundational | intermediate | advanced | expert]
estimated-study-time: [Xmin]
optimal-sequence-position: [early | middle | late | capstone]
---
```
</frontmatter_specification>

<callout_format>
### Inline Callout Alternative

```markdown
> [!prerequisite] Required Background
> **Hard Prerequisites** (must understand first):
> - [[Information Processing Theory]] — foundational framework
> - [[Working Memory Basics]] — capacity constraints
> 
> **Soft Prerequisites** (helpful context):
> - [[History of Cognitive Psychology]] — theoretical lineage
> - [[Research Methods in Cogsci]] — study interpretation

> [!enables] This Unlocks
> **Direct Applications**:
> - [[Cognitive Load Theory]] — primary extension
> - [[Instructional Design Principles]] — practical application
> 
> **Related Topics**:
> - [[Expertise Development]] — schema automation
> - [[Multimedia Learning]] — CLT application
```
</callout_format>

<dependency_types>
### Prerequisite Classification

| Type | Symbol | Definition |
|------|--------|------------|
| `hard` | ⚠️ | Cannot understand B without A |
| `soft` | 💡 | A enriches understanding of B |
| `parallel` | ↔️ | A and B mutually inform |
| `optional` | ➕ | A deepens but isn't needed |

| Type | Symbol | Definition |
|------|--------|------------|
| `direct` | → | This note directly enables |
| `related` | ~ | Benefits from this knowledge |
| `advanced` | ↑ | Expert-level extension |
</dependency_types>

<difficulty_calibration>
### Difficulty Level Definitions

| Level | Definition | Typical Prerequisites |
|-------|------------|----------------------|
| `foundational` | Entry-level; minimal background | 0-2 concepts |
| `intermediate` | Builds on basics | 3-5 concepts |
| `advanced` | Requires substantial foundation | 6-10 concepts |
| `expert` | Assumes comprehensive knowledge | 10+ concepts |
</difficulty_calibration>

<generation_guidelines>
### When to Include Dependencies

**ALWAYS specify:**
- Hard prerequisites for advanced content
- Direct enables for foundational content
- Difficulty level for all substantive notes
- Study time estimates for reference notes

**Derive from:**
- Concepts assumed but not explained in the note
- Explicit "building on X" statements
- Theoretical lineages
- Practical applications mentioned
</generation_guidelines>

<query_compatibility>
### Learning Path Queries

```dataview
LIST FROM "cognitive-science"
WHERE difficulty = "foundational"
SORT file.name ASC
```

```dataview
TABLE enables.direct as "Unlocks"
FROM "permanent-notes"
WHERE contains(prerequisites.hard, "[[working-memory]]")
```
</query_compatibility>
</prerequisite_dependency_mapping>
```

---

### Module 7: Semantic Versioning for Concepts

```xml
<semantic_concept_versioning>
## 📊 Knowledge Evolution Tracking Protocol

Track how understanding of concepts evolves over time.

<frontmatter_specification>
### YAML Frontmatter Format

```yaml
---
concept-version: "X.Y.Z"
# X = Major (paradigm shift), Y = Minor (significant addition), Z = Patch (clarification)

version-history:
  - version: "1.0.0"
    date: "YYYY-MM-DD"
    change: "Initial understanding from [source]"
    trigger: "First encounter with concept"
  - version: "2.0.0"
    date: "YYYY-MM-DD"
    change: "Major revision incorporating [new framework]"
    trigger: "Read [source] that contradicted previous understanding"
    breaking: true
  - version: "2.1.0"
    date: "YYYY-MM-DD"
    change: "Added application domain [X]"
    trigger: "Applied concept in new context"

last-review: "YYYY-MM-DD"
next-review: "YYYY-MM-DD"
stability: [stable | evolving | volatile]
---
```
</frontmatter_specification>

<version_semantics>
### Version Number Meanings

| Component | Increment When | Example |
|-----------|----------------|---------|
| **Major (X)** | Fundamental understanding changes; old version now seems wrong | 1.0 → 2.0: "Realized CLT applies to expertise differently than I thought" |
| **Minor (Y)** | Significant addition that extends without contradicting | 2.0 → 2.1: "Added connection to multimedia learning principles" |
| **Patch (Z)** | Clarification, typo fix, minor refinement | 2.1 → 2.1.1: "Clarified definition wording" |
</version_semantics>

<breaking_change_flag>
### Breaking Change Documentation

When `breaking: true`:

```yaml
- version: "3.0.0"
  date: "2025-05-15"
  change: "Complete reconceptualization of attention as predictive process"
  trigger: "Deep dive into predictive processing framework"
  breaking: true
  deprecated-understanding: "Previous view of attention as filter/resource"
  migration-notes: "Review all notes linking to old attention model"
```
</breaking_change_flag>

<stability_indicators>
### Stability Classifications

| Status | Definition | Action |
|--------|------------|--------|
| `stable` | Well-established understanding, unlikely to change | Standard review cycle |
| `evolving` | Actively developing understanding | More frequent review |
| `volatile` | Field or understanding in flux | Flag for close monitoring |
</stability_indicators>

<inline_alternative>
### Lightweight Inline Syntax

```markdown
%%VERSION: 2.1.0 | last-updated:2025-05 | stability:evolving%%
```
</inline_alternative>
</semantic_concept_versioning>
```

---

### Module 8: Query Anchors

```xml
<query_anchor_system>
## 🎯 Dataview Optimization Points Protocol

Create explicit query targets for efficient vault-wide searches.

<anchor_syntax>
### Query Anchor Format

**Basic Syntax:**
```markdown
%%QUERY-ANCHOR: namespace:identifier%%
```

**Namespaced Examples:**
```markdown
%%QUERY-ANCHOR: attention:all-theories%%
%%QUERY-ANCHOR: attention:capacity-models%%
%%QUERY-ANCHOR: attention:filter-models%%
%%QUERY-ANCHOR: memory:encoding-strategies%%
%%QUERY-ANCHOR: learning:retrieval-practice-evidence%%
%%QUERY-ANCHOR: methodology:experimental-paradigms%%
```

**Multi-Tag Anchors:**
```markdown
%%QUERY-ANCHOR: attention:capacity + historical + foundational%%
```
</anchor_syntax>

<namespace_taxonomy>
### Standard Namespaces

| Namespace | Use For |
|-----------|---------|
| `attention` | Attention and concentration topics |
| `memory` | Memory systems and processes |
| `learning` | Learning theories and techniques |
| `cognition` | General cognitive processes |
| `methodology` | Research methods and paradigms |
| `application` | Practical applications |
| `theorist` | Researcher-specific content |
| `debate` | Contested or debated topics |
</namespace_taxonomy>

<identifier_patterns>
### Common Identifier Patterns

| Pattern | Example | Use |
|---------|---------|-----|
| `all-[category]` | `all-theories` | Collect all items of type |
| `[model]-components` | `clm-components` | Parts of a specific model |
| `evidence-for-[claim]` | `evidence-for-spacing` | Supporting evidence |
| `against-[claim]` | `against-learning-styles` | Counter-evidence |
| `applications-of-[concept]` | `applications-of-clt` | Practical uses |
| `history-of-[topic]` | `history-of-attention` | Historical development |
</identifier_patterns>

<query_examples>
### Dataview Query Patterns

**Find all items with anchor:**
```dataview
LIST FROM "permanent-notes"
WHERE contains(file.content, "%%QUERY-ANCHOR: attention:all-theories%%")
```

**Count anchored items:**
```dataview
TABLE length(rows) as "Count"
FROM "permanent-notes"
WHERE contains(file.content, "QUERY-ANCHOR: learning:")
GROUP BY true
```
</query_examples>

<placement_guidelines>
### Where to Place Anchors

- **At section start**: For content that spans multiple paragraphs
- **After key definitions**: For concepts you'll want to collect
- **In MOCs**: For navigation hub creation
- **Before evidence blocks**: For evidence collection queries
</placement_guidelines>
</query_anchor_system>
```

---

### Module 9: Contradiction and Tension Markers

```xml
<contradiction_tension_markers>
## ⚖️ Intellectual Honesty Encoding Protocol

Explicitly mark unresolved tensions, contradictions, and debates.

<tension_callout_specification>
### Tension Callout Structure

```markdown
> [!tension] Descriptive Tension Name
> **Position A**: [Claim/Theory A]
> - **Proponents**: [Researchers/Schools]
> - **Key Evidence**: [Supporting findings]
> 
> **Position B**: [Claim/Theory B]
> - **Proponents**: [Researchers/Schools]
> - **Key Evidence**: [Supporting findings]
> 
> **Current Status**: [active-debate | partially-resolved | synthesis-emerging]
> **Resolution Attempts**: [Notable reconciliation efforts]
> **Personal Stance**: [Your current position with rationale]
> **Needed for Resolution**: [What evidence/argument would settle this]
```
</tension_callout_specification>

<inline_syntax>
### Inline Tension Markers

```markdown
[**Unresolved-Tension**:: tension-name | positions:A-vs-B | status:active | priority:high]

[**Contradiction**:: [[Claim A]] ↔conflicts↔ [[Claim B]] | status:unresolved | personal-lean:A]
```
</inline_syntax>

<status_taxonomy>
### Tension Status Classifications

| Status | Definition | Action |
|--------|------------|--------|
| `active-debate` | Ongoing scholarly disagreement | Monitor literature |
| `partially-resolved` | Some consensus emerging | Document synthesis |
| `synthesis-emerging` | Integration being developed | Track development |
| `historical` | Past debate, now resolved | Document for context |
| `personal-confusion` | You're confused, not necessarily the field | Study more |
</status_taxonomy>

<contradiction_types>
### Contradiction Classifications

| Type | Definition | Example |
|------|------------|---------|
| `empirical` | Conflicting data/findings | Replication failures |
| `theoretical` | Incompatible frameworks | Single vs multiple resource pools |
| `methodological` | Disputes about how to measure | Implicit vs explicit measures |
| `definitional` | Different concept meanings | What counts as "attention" |
| `scope` | Different boundary conditions | Lab vs real-world findings |
</contradiction_types>

<resolution_tracking>
### Resolution Attempt Documentation

```markdown
> [!resolution-attempt] Synthesis of Position A and B
> **Date**: YYYY-MM-DD
> **Approach**: [How you tried to reconcile]
> **Outcome**: [success | partial | failed]
> **Remaining Issues**: [What's still unresolved]
> **Next Steps**: [Further investigation needed]
```
</resolution_tracking>

<generation_guidelines>
### When to Create Tension Markers

**ALWAYS mark when:**
- Two cited sources explicitly disagree
- "However, critics argue…" type statements
- Multiple competing models exist for same phenomenon
- Your own analysis reveals inconsistency

**Include in:**
- Reference notes covering debated topics
- Synthesis notes attempting integration
- MOCs organizing contested domains
</generation_guidelines>
</contradiction_tension_markers>
```

---

### Module 10: Cognitive Load Indicators

```xml
<cognitive_load_indicators>
## 🧠 Study Session Optimization Protocol

Embed complexity indicators enabling intelligent study planning.

<frontmatter_specification>
### YAML Frontmatter Format

```yaml
---
cognitive-load:
  intrinsic: [low | moderate | high | very-high]
  element-interactivity: [1-10]
  prerequisite-density: [count of assumed concepts]
  abstraction-level: [concrete | mixed | abstract | highly-abstract]
  
study-parameters:
  estimated-time: [Xmin]
  optimal-passes: [count for mastery]
  spacing-interval: [suggested review gap]
  optimal-state: "[description of ideal study conditions]"
  
chunking-guide:
  recommended-chunks: [count]
  natural-break-points: 
    - "[section/heading 1]"
    - "[section/heading 2]"
---
```
</frontmatter_specification>

<intrinsic_load_rubric>
### Intrinsic Load Assessment

| Level | Element Interactivity | Description |
|-------|----------------------|-------------|
| `low` | 1-3 | Can understand elements independently |
| `moderate` | 4-5 | Some elements must be held simultaneously |
| `high` | 6-8 | Many interdependent elements |
| `very-high` | 9-10 | All elements must be processed together |
</intrinsic_load_rubric>

<inline_syntax>
### Lightweight Inline Format

```markdown
%%LOAD: intrinsic=high | interactivity=7 | time=45min | passes=3 | state="focused, rested"%%
```
</inline_syntax>

<callout_format>
### Study Guide Callout

```markdown
> [!study-guide] Optimal Approach for This Note
> **Cognitive Demand**: High (element interactivity: 7/10)
> **Time Required**: 45-60 minutes for deep processing
> **Passes Needed**: 3 (initial → review → integrate)
> **Optimal Conditions**: Quiet environment, alert state, 50+ min available
> **Chunking Strategy**: 
>   1. Theoretical foundation (15 min)
>   2. Model components (20 min)
>   3. Applications (15 min)
> **Warning**: Don't attempt when fatigued—concepts compound
```
</callout_format>

<state_recommendations>
### Optimal State Descriptors

| Note Type | Recommended State |
|-----------|------------------|
| Foundational concepts | Any receptive state |
| Complex theory | Alert, focused, uninterrupted |
| Technical procedures | Ready to practice actively |
| Synthesis/integration | Creative, connective mindset |
| Review notes | Spaced, testing-oriented |
</state_recommendations>

<generation_guidelines>
### When to Include Load Indicators

**ALWAYS include for:**
- Reference notes (primary study materials)
- Complex theoretical frameworks
- Technical procedures with multiple steps

**Assessment Heuristics:**
- Count concepts that must be held in mind simultaneously
- Note abstraction level (concrete examples lower load)
- Consider prerequisite knowledge assumed
- Estimate based on your own experience processing the material
</generation_guidelines>
</cognitive_load_indicators>
```

---

### Module 11: Application Context Markers

```xml
<application_context_markers>
## 🎯 Transfer Facilitation Protocol

Encode where/when/how to apply captured knowledge.

<callout_specification>
### Application Context Callout

```markdown
> [!application-context] Concept Name
> **Primary Domains**:
>   - [[Domain 1]] — [specific use case]
>   - [[Domain 2]] — [specific use case]
>   - [[Domain 3]] — [specific use case]
> 
> **Trigger Conditions** (when to apply):
>   - "[Observable situation 1]" → [recommended action]
>   - "[Observable situation 2]" → [recommended action]
>   - "[Observable situation 3]" → [recommended action]
> 
> **Anti-Patterns** (when NOT to apply):
>   - [Situation where this doesn't work]
>   - [Common misapplication]
> 
> **Implementation Notes**:
>   - [Practical consideration 1]
>   - [Practical consideration 2]
```
</callout_specification>

<inline_syntax>
### Inline Application Markers

```markdown
[**Application-Domain**:: [[Domain]] | trigger:"situation description" | action:"recommended response" | confidence:high]

[**Anti-Pattern**:: [[Concept]] | context:"where it fails" | reason:"why it doesn't work" | alternative:"what to do instead"]
```
</inline_syntax>

<trigger_condition_patterns>
### Trigger Condition Formats

| Pattern | Example |
|---------|---------|
| Problem-based | "When learner shows overwhelm" → reduce extraneous load |
| Context-based | "In technical documentation" → apply chunking principles |
| Symptom-based | "Information not sticking" → check element interactivity |
| Goal-based | "Seeking long-term retention" → implement spaced practice |
| Resource-based | "Limited study time available" → prioritize high-yield |
</trigger_condition_patterns>

<domain_taxonomy>
### Common Application Domains

| Domain Category | Examples |
|-----------------|----------|
| **Education** | Curriculum design, tutoring, self-study |
| **Design** | UX, instructional materials, presentations |
| **Communication** | Technical writing, teaching, explaining |
| **Professional** | Meeting facilitation, training, onboarding |
| **Personal** | Self-improvement, habit formation, learning |
| **Technical** | Prompt engineering, documentation, code review |
</domain_taxonomy>

<generation_guidelines>
### When to Include Application Context

**ALWAYS include for:**
- Principles with clear practical applications
- Methods and techniques
- Frameworks designed for application

**Include triggers for:**
- Every principle worth remembering
- Concepts with non-obvious application points
- Knowledge at risk of becoming inert
</generation_guidelines>
</application_context_markers>
```

---

### Module 12: Evidence Weight Indicators

```xml
<evidence_weight_indicators>
## ⚖️ Epistemological Rigor Protocol

Classify evidence quality following evidence-based practice hierarchies.

<evidence_hierarchy>
### Evidence Strength Taxonomy

| Level | Type | Definition | Weight |
|-------|------|------------|--------|
| 1 | `meta-analysis` | Systematic quantitative synthesis | Highest |
| 2 | `systematic-review` | Comprehensive qualitative synthesis | Very High |
| 3 | `rct` | Randomized controlled trial | High |
| 4 | `quasi-experimental` | Non-randomized controlled study | Moderate-High |
| 5 | `cohort` | Prospective observational | Moderate |
| 6 | `case-control` | Retrospective comparison | Moderate-Low |
| 7 | `case-series` | Multiple cases without control | Low |
| 8 | `case-study` | Single case detailed examination | Low |
| 9 | `expert-opinion` | Authority assertion | Very Low |
| 10 | `anecdote` | Personal/informal observation | Lowest |
</evidence_hierarchy>

<inline_syntax>
### Evidence Marker Syntax

**Basic:**
```markdown
[**Finding-Name**:: claim content]^evidence:evidence-type
```

**Enhanced with Metadata:**
```markdown
[**Finding-Name**:: claim content]^evidence:meta-analysis|k=45|n=12000|d=0.65|p<.001
```

| Metadata | Meaning |
|----------|---------|
| `k` | Number of studies in meta-analysis |
| `n` | Total sample size |
| `d` | Cohen's d effect size |
| `r` | Correlation coefficient |
| `OR` | Odds ratio |
| `p` | P-value significance |
</inline_syntax>

<quality_markers>
### Study Quality Modifiers

| Modifier | Meaning |
|----------|---------|
| `-strong` | High methodological rigor |
| `-moderate` | Acceptable methodology |
| `-weak` | Notable limitations |
| `-flawed` | Serious problems identified |

**Example:**
```markdown
[**Claim**:: finding]^evidence:rct-strong|n=500|d=0.45
```
</quality_markers>

<replication_status>
### Replication Markers

| Status | Meaning |
|--------|---------|
| `replicated` | Successfully reproduced |
| `partially-replicated` | Mixed reproduction results |
| `failed-replication` | Key replication attempt failed |
| `not-yet-replicated` | Awaiting replication |
| `pre-registered` | Study was pre-registered |
</replication_status>

<generation_guidelines>
### When to Include Evidence Markers

**ALWAYS include for:**
- Empirical claims with specific findings
- Statistical claims (percentages, effect sizes)
- Claims that could be contested

**Quality Assessment Questions:**
- Was it randomized?
- Was there a control group?
- What was the sample size?
- Has it been replicated?
- Was it pre-registered?
</generation_guidelines>
</evidence_weight_indicators>
```

---

### Module 13: Synthesis Potential Markers

```xml
<synthesis_potential_markers>
## 🔮 Cross-Domain Opportunity Protocol

Flag concepts with high potential for interdisciplinary synthesis.

<callout_specification>
### Synthesis Opportunity Callout

```markdown
> [!synthesis-opportunity] Opportunity Title
> **Source Domain**: [[Primary Domain]] — [[Specific Concept]]
> **Target Domains**:
>   - [[Target Domain 1]] — [potential connection]
>   - [[Target Domain 2]] — [potential connection]
>   - [[Target Domain 3]] — [potential connection]
> 
> **Synthesis Type**: [analogical | structural | functional | mechanistic]
> **Exploration Status**: [unexplored | initial-notes | developing | mature]
> **Potential Value**: [high | medium | low]
> **Generativity**: [How many new insights might emerge?]
> 
> **Seed Questions**:
>   - [Question that might drive synthesis 1]
>   - [Question that might drive synthesis 2]
> 
> **Next Action**: [Specific step to explore this]
```
</callout_specification>

<inline_syntax>
### Inline Synthesis Markers

```markdown
%%SYNTHESIS: source=concept-name | targets=domain1,domain2,domain3 | type=analogical | status=unexplored | value=high%%

[**Synthesis-Potential**:: [[Source Concept]] ←bridges→ [[Target Domain]] | type:analogical | status:unexplored]
```
</inline_syntax>

<synthesis_types>
### Synthesis Type Definitions

| Type | Definition | Example |
|------|------------|---------|
| `analogical` | Structural similarity across domains | Attention allocation ↔ Economic resource allocation |
| `structural` | Same formal structure, different content | Graph theory ↔ Social networks ↔ Neural networks |
| `functional` | Same function, different mechanism | Working memory ↔ RAM ↔ Short-term buffers |
| `mechanistic` | Shared underlying causal mechanism | All learning as prediction error minimization |
| `metaphorical` | Illuminating but not rigorous parallel | Mind as computer (useful but imperfect) |
</synthesis_types>

<exploration_status>
### Status Definitions

| Status | Definition | Next Action |
|--------|------------|-------------|
| `unexplored` | Noticed but not investigated | Create exploration note |
| `initial-notes` | Some preliminary thinking | Develop structured comparison |
| `developing` | Active synthesis work | Refine and test framework |
| `mature` | Well-developed integration | Document and apply |
</exploration_status>

<generation_triggers>
### When to Flag Synthesis Potential

**High-Value Signals:**
- Concept has abstract structure applicable elsewhere
- You notice yourself thinking "this is like X"
- Framework seems domain-general despite specific origin
- Multiple fields use similar concepts with different names
- Explanatory mechanism seems fundamental
</generation_triggers>
</synthesis_potential_markers>
```

---

### Module 14: Temporal Decay Indicators

```xml
<temporal_decay_indicators>
## ⏰ Knowledge Freshness Protocol

Track information currency and trigger systematic review.

<frontmatter_specification>
### YAML Frontmatter Format

```yaml
---
freshness:
  domain-volatility: [stable | moderate | high | volatile]
  last-verified: YYYY-MM-DD
  decay-rate: [Xdays | Xweeks | Xmonths | Xyears]
  staleness-risk: [low | medium | high | critical]
  
update-triggers:
  - "[Event that should trigger review]"
  - "[Publication type that should trigger update]"
  
review-history:
  - date: YYYY-MM-DD
    action: "[What you checked/updated]"
    outcome: "[Still current | Updated X | Major revision]"
---
```
</frontmatter_specification>

<volatility_calibration>
### Domain Volatility Guide

| Level | Decay Rate | Examples |
|-------|------------|----------|
| `stable` | Years | Historical facts, foundational principles, well-established theories |
| `moderate` | 6-12 months | Established best practices, consensus positions |
| `high` | 1-6 months | Emerging research areas, technology practices |
| `volatile` | Days-weeks | Current events, rapidly evolving fields, AI/ML techniques |
</volatility_calibration>

<inline_syntax>
### Lightweight Inline Format

```markdown
%%FRESHNESS: volatility=high | verified=2025-05 | decay=3mo | risk=medium%%
```
</inline_syntax>

<staleness_indicators>
### Staleness Risk Assessment

| Risk Level | Definition | Action |
|------------|------------|--------|
| `low` | Well within freshness window | Normal review cycle |
| `medium` | Approaching review due date | Schedule review |
| `high` | Past typical decay period | Review soon |
| `critical` | Significantly outdated | Review immediately |
</staleness_indicators>

<update_trigger_patterns>
### Common Update Triggers

| Trigger Type | Example |
|--------------|---------|
| Publication | "New meta-analysis in this area" |
| Event | "Major conference with relevant findings" |
| Personal | "Applied this and found issues" |
| External | "Someone questioned this claim" |
| Systematic | "6 months since last verification" |
</update_trigger_patterns>

<generation_guidelines>
### When to Include Freshness Markers

**ALWAYS include for:**
- Topics in rapidly evolving fields
- Best practice recommendations
- Statistical claims that might be updated
- Technology-specific information

**Volatility Assessment Questions:**
- How often does this field publish updates?
- How recent is the source material?
- Are there ongoing debates that might resolve?
- Is this affected by changing technology/society?
</generation_guidelines>
</temporal_decay_indicators>
```

---

### Module 15: Mental Model Anchors

```xml
<mental_model_anchors>
## 🧭 Framework Integration Protocol

Explicitly connect concepts to foundational mental models.

<callout_specification>
### Mental Model Anchor Callout

```markdown
> [!mental-model-anchor] Concept Name
> **Primary Model Anchors**:
>   - [[Mental Model 1]] — [how this concept instantiates/applies the model]
>   - [[Mental Model 2]] — [connection explanation]
>   - [[Mental Model 3]] — [connection explanation]
> 
> **Model Application Notes**:
>   - [How thinking through Model 1 illuminates this concept]
>   - [What Model 2 lens reveals about this]
> 
> **Inverse Application** (this concept AS a mental model):
>   - Can be applied to: [Other domains where this concept works as a lens]
```
</callout_specification>

<inline_syntax>
### Inline Model Anchors

```markdown
[**Model-Anchor**:: [[Concept]] ←anchors-to→ [[Mental Model]] | insight:"what the connection reveals"]

[**Model-Application**:: [[Concept]] ←as-lens-for→ [[Target Domain]] | insight:"how concept illuminates domain"]
```
</inline_syntax>

<foundational_model_library>
### Core Mental Model Reference

| Model | Core Insight | Application Trigger |
|-------|--------------|---------------------|
| [[First Principles]] | Decompose to fundamentals | "What are the basic building blocks?" |
| [[Inversion]] | Solve by negation | "What would make this fail?" |
| [[Second-Order Effects]] | Consequences of consequences | "And then what?" |
| [[Systems Thinking]] | Interconnected wholes | "What are the feedback loops?" |
| [[Opportunity Cost]] | Value of alternatives foregone | "What am I giving up?" |
| [[Constraint Theory]] | Bottleneck identification | "What's the limiting factor?" |
| [[Circle of Competence]] | Know your limits | "Am I qualified to judge this?" |
| [[Map vs Territory]] | Models ≠ reality | "How accurate is this representation?" |
| [[Occam's Razor]] | Prefer simplicity | "Is there a simpler explanation?" |
| [[Falsification]] | Seeking disconfirmation | "How could this be wrong?" |
</foundational_model_library>

<bidirectional_application>
### Two-Way Model Use

**Concept → Model** (Anchoring):
"How does [[First Principles Thinking]] illuminate [[Cognitive Load Theory]]?"
→ CLT decomposes to: capacity limits + element interactivity + load types

**Concept → Lens** (Projection):
"How can [[Cognitive Load Theory]] serve as a lens for [[Software Architecture]]?"
→ Code complexity creates cognitive load; modular design reduces it
</bidirectional_application>

<generation_guidelines>
### When to Include Model Anchors

**ALWAYS anchor when:**
- Concept has clear structural parallel to known model
- Understanding deepens through model lens
- Concept itself functions as a mental model for other domains

**Model Selection Heuristic:**
- Which 2-3 models most illuminate this concept?
- Which models would an expert naturally invoke here?
- What model would help a novice understand faster?
</generation_guidelines>
</mental_model_anchors>
```

---

### Module 16: Counterexample Collection

```xml
<counterexample_collection>
## 🚧 Boundary Condition Protocol

Systematically document exceptions, edge cases, and limitations.

<callout_specification>
### Counterexample Callout

```markdown
> [!counterexample] Principle/Claim Name
> **Principle Statement**: [What the principle claims]
> 
> **Counterexample**: [Situation where principle fails]
> **Boundary Condition**: [What factor makes it fail]
> **Population/Context**: [Who/where it doesn't apply]
> **Source**: [Citation if empirical]
> 
> **Implication for Application**:
>   - [How to adjust when this boundary is hit]
>   - [What to do instead]
> 
> **Principle Revision** (if needed):
>   - Original: "[Broad claim]"
>   - Revised: "[More accurate, bounded claim]"
```
</callout_specification>

<inline_syntax>
### Inline Boundary Markers

```markdown
[**Boundary-Condition**:: [[Principle]] fails-when:"condition description" | population:"affected group" | alternative:"what to do instead"]

[**Counterexample**:: [[Claim]] negated-by:"specific case" | implication:"how this changes understanding"]

[**Exception**:: [[Rule]] except-when:"exception condition" | frequency:"how often this occurs"]
```
</inline_syntax>

<boundary_types>
### Boundary Condition Taxonomy

| Type | Definition | Example |
|------|------------|---------|
| `population` | Doesn't apply to certain groups | "Testing effect weaker for very low-knowledge learners" |
| `context` | Doesn't apply in certain settings | "Spacing effect reduced in high-pressure testing contexts" |
| `magnitude` | Only applies within certain ranges | "Desirable difficulty only when difficulty is moderate" |
| `temporal` | Doesn't apply at certain times | "Interleaving less effective in initial skill acquisition" |
| `interaction` | Moderated by other variables | "Expertise reversal effect—what helps novices hurts experts" |
| `methodological` | Only appears with certain methods | "Effect may be artifact of lab conditions" |
</boundary_types>

<exception_frequency>
### Exception Frequency Markers

| Marker | Meaning | Action |
|--------|---------|--------|
| `rare` | Unusual edge case | Note but apply principle normally |
| `occasional` | Happens sometimes | Check conditions before applying |
| `common` | Frequent exception | Always verify applicability |
| `systematic` | Predictable from theory | Build into standard application |
</exception_frequency>

<generation_guidelines>
### When to Document Counterexamples

**ALWAYS document when:**
- Source explicitly notes limitations
- You've encountered failure cases
- Population or context restrictions are known
- Moderating variables are documented

**Questions to Surface Counterexamples:**
- When does this NOT work?
- Who does this NOT help?
- Under what conditions does this reverse?
- What's the smallest viable context for this principle?
</generation_guidelines>
</counterexample_collection>
```

---

## 🔧 Unified Integration Module

This master module combines the highest-priority systems into a single deployable component:

```xml
<enhanced_pkb_integration>
## 🧬 Enhanced PKB Integration Protocol v1.0

This unified module integrates: epistemic encoding, relationship typing, atomic extraction, and application context marking.

<activation_statement>
This protocol activates automatically for all substantive knowledge content. Claude will:
1. **Encode epistemic confidence** on all factual claims
2. **Type relationships** when establishing conceptual connections
3. **Signal atomic candidates** within reference notes
4. **Mark application contexts** for actionable knowledge
</activation_statement>

<integrated_output_example>
### Example: Integrated Output Demonstration

```markdown
---
tags: #cognitive-psychology #attention #reference-note
aliases: [Kahneman Capacity Model, Resource Theory of Attention]
cognitive-load:
  intrinsic: high
  element-interactivity: 7
prerequisites:
  hard: ["[[information-processing-theory]]", "[[arousal-theory]]"]
freshness:
  domain-volatility: stable
  last-verified: 2025-05
---

# Capacity Model of Attention (Kahneman 1973)

[**Capacity-Model-Definition**:: a framework proposing that attention operates through a limited pool of undifferentiated processing resources, allocated dynamically based on task demands, arousal level, and strategic priorities]^established-stable

%%ATOMIC: capacity-model-kahneman | framework | critical | foundational-attention-theory%%

## Core Components

The model comprises several interacting elements:

[**Arousal-Capacity-Relationship**:: arousal modulates total available resources along an inverted-U function]^verified-stable
^source:: [[ref-kahneman-1973]] p.47
^evidence-type:: theoretical-claim

[**Theoretical-Foundation**:: [[Capacity Model]] →(builds-on)→ [[Yerkes-Dodson Law]] + [[Information Processing Theory]]]

%%QUERY-ANCHOR: attention:capacity-model-components%%

> [!application-context] Capacity Model Application
> **Domains**: 
>   - [[Instructional Design]] — predict when learners will be overwhelmed
>   - [[UX Design]] — interface complexity management
> **Trigger Conditions**:
>   - "Learner performance degrades under stress" → check arousal level
>   - "Dual-task interference observed" → resources exhausted
> **Anti-Patterns**:
>   - Assuming capacity is fixed (it fluctuates with arousal)

> [!counterexample] Capacity Model Limitations
> **Principle**: Single undifferentiated resource pool
> **Counterexample**: Modality-specific interference patterns suggest multiple pools
> **Boundary Condition**: Model may oversimplify for cross-modal tasks
> **Alternative**: Consider [[Multiple Resource Theory]] for complex interfaces
```
</integrated_output_example>

<priority_integration_matrix>
### Integration Priority by Note Type

| Note Type | Epistemic | Relations | Atomic | Application | Load | Evidence |
|-----------|:---------:|:---------:|:------:|:-----------:|:----:|:--------:|
| Reference Note | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓ | ✓✓ | ✓✓✓ |
| Atomic Note | ✓✓ | ✓✓ | — | ✓✓✓ | ✓ | ✓✓ |
| MOC | ✓ | ✓✓✓ | — | ✓ | — | — |
| Synthesis Note | ✓✓✓ | ✓✓✓ | ✓ | ✓✓ | ✓✓ | ✓✓ |

Legend: ✓✓✓ = Always include | ✓✓ = Usually include | ✓ = Sometimes include | — = Rarely needed
</priority_integration_matrix>

<density_guidelines>
### Overall Density Targets

Per major section of a reference note:
- Epistemic markers: 3-6 claims marked
- Relationship encodings: 2-4 typed links
- Atomic candidates: 1-3 flagged
- Application contexts: 1-2 per applicable concept
- Evidence markers: On all empirical claims
- SR hooks: 3-5 for key content
</density_guidelines>

<validation_checklist>
### Pre-Output Validation

Before finalizing enhanced PKB content, verify:

**Epistemic Layer:**
- [ ] All substantive claims have confidence markers
- [ ] Markers match actual evidence strength
- [ ] Personal synthesis distinguished from consensus

**Relationship Layer:**
- [ ] Key conceptual relationships are typed
- [ ] Relationship types are semantically accurate
- [ ] Bidirectional link opportunities identified

**Extraction Layer:**
- [ ] Atomizable concepts flagged
- [ ] Priority levels assigned appropriately
- [ ] Extraction triggers documented

**Application Layer:**
- [ ] Actionable concepts have application contexts
- [ ] Trigger conditions are specific and observable
- [ ] Anti-patterns noted where relevant

**Meta Layer:**
- [ ] Cognitive load indicators present (for complex notes)
- [ ] Freshness parameters set (for volatile topics)
- [ ] Mental model anchors identified (for frameworks)
</validation_checklist>
</enhanced_pkb_integration>
```

---

# 🔗 Related Topics for PKB Expansion

1. **[[Dataview Query Library for PKB Integration]]**
   - *Connection*: All these markers become powerful with systematic queries
   - *Depth Potential*: Complete query cookbook for each marker type
   - *Knowledge Graph Role*: Operational bridge between encoding and retrieval

2. **[[Obsidian Automation Workflows for Marker Processing]]**
   - *Connection*: Transform markers into automated vault maintenance
   - *Depth Potential*: Templater scripts, QuickAdd macros, periodic note reviews
   - *Knowledge Graph Role*: Technical implementation layer

3. **[[Epistemology for Knowledge Workers]]**
   - *Connection*: Theoretical foundation for confidence calibration
   - *Depth Potential*: When to trust claims, evidence evaluation frameworks
   - *Knowledge Graph Role*: Conceptual grounding for epistemic markers

4. **[[Zettelkasten Atomicity Principles]]**
   - *Connection*: Theory behind atomic extraction decisions
   - *Depth Potential*: What makes a good atomic note, granularity decisions
   - *Knowledge Graph Role*: Methodological foundation for extraction signals

---