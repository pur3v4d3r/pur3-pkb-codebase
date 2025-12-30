---
type: component
component-type: format
atomic-composite: atomic
domain: pkb
id: 20251221020500
status: active
version: 1.0.0
rating: 0.0
performance-score: 0.0
source: original
created: 2025-12-21
modified: 2025-12-21
usage-count: 0
last-used: 
confidence: established
maturity: evergreen
tags:
  - year/2025
  - prompt-engineering/component
  - component-type/format
  - domain/pkb
aliases:
  - note-spawner
  - atomic-candidate-generator
  - extraction-protocol
conflicts-with:
  - [[seamless-narrative-generator]]
  - [[simplified-summary-format]]
synergies-with:
  - [[semantic-relationship-typing]]
  - [[academic-literature-synthesizer]]
  - [[smart-curator-persona]]
used-in-prompts: []
link-up: [[prompt-engineering-moc]]
---
# Format: Atomic Extraction Signaling

> [!definition] Component Definition
> A structural protocol that instructs the LLM to identify, classify, and format specific concepts within a text that warrant extraction into independent atomic notes, using distinct visual callouts or inline markers.

## 🎯 When to Use
- **Literature Processing**: When summarizing books or papers and needing to identify key concepts for a permanent Zettelkasten/PKM vault.
- **Refactoring**: When breaking down long, "messy" thoughts into structured atomic units.
- **Curriculum Mapping**: When analyzing a subject to determine the necessary learning nodes.
- **Knowledge Graph Expansion**: When explicitly looking to grow the density of a knowledge base.

## 🚫 When NOT to Use
- **Casual Reading**: When the goal is a quick gist, not deep study.
- **Final Polish**: When generating text intended for publication or external communication.
- **Simple Lists**: When a basic bulleted list of keywords would suffice.
- **Low-Density Content**: Content lacking technical depth where "atomic" concepts don't really exist.

## 📝 COMPONENT TEXT
```prompt
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
>  - →(relation)→ [[Related Concept 1]]
>  - →(relation)→ [[Related Concept 2]]
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

## 🔀 VARIATIONS

### Variation 1: Actionable Todo List
Use this when you want a consolidated checklist at the end of a note, rather than interrupting the text flow with callouts.

```prompt
<atomic_checklist_protocol>
Instead of inline callouts, compile a "Refactoring Queue" at the bottom of the response.

Format:
## 📥 Extraction Queue
- [ ] [[Concept Name]] (Priority: High) - *Trigger*: {Reason}
- [ ] [[Concept Name]] (Priority: Low) - *Trigger*: {Reason}
</atomic_checklist_protocol>
```

### Variation 2: JSON Data Payload
Use this for automated workflows where a script parses the LLM output to create files automatically.

```prompt
<atomic_json_protocol>
Output extraction candidates in a strict JSON block at the end of the response.

```json
{
  "candidates": [
    {
      "name": "Concept Name",
      "slug": "concept-name",
      "type": "principle",
      "priority": "high",
      "relationships": ["concept-a", "concept-b"]
    }
  ]
}
```
</atomic_json_protocol>
```

## 🤝 RELATIONSHIPS

### Works Well With
- [[semantic-relationship-typing]] - The "Key Relationships" field in the callout specifically relies on the arrow syntax (e.g., `→(builds-on)→`) defined in that component.
- [[academic-literature-synthesizer]] - Provides the complex source material that necessitates this extraction protocol.
- [[curator-persona]] - A persona that naturally looks for connections and distinct concepts aligns well with this task.

### Conflicts With
- [[seamless-narrative-generator]] - The visual callouts break the reading experience.
- [[simple-wikilink-format]] - This component demands metadata (slugs, types) that simple linking ignores.

## 📊 PERFORMANCE DATA

### Usage Statistics
- **Total Uses**: `VIEW[0]`
- **Last Used**: `VIEW[]`
- **Performance Score**: `VIEW[0.0]`/10

### Test Results
#### Test 1: Cognitive Psychology Text
**Date**: 2025-12-21
**Prompt Used In**: [[pkm-ingestion-workflow]]
**Quality Score**: N/A
**Notes**: Initial formalization. Key observation: LLMs sometimes struggle to determine "Estimated Scope" (word count) accurately. This field might be speculative.

## 💡 USAGE EXAMPLES

### Example 1: Processing a Textbook Chapter
**Context**: Summarizing a chapter on Memory Models.
**Full Prompt**:
```markdown
Summarize the section on "Baddeley's Working Memory" and apply the <atomic_extraction_signaling> to identify the core components.
```
**Outcome**:
```markdown
Baddeley and Hitch proposed a multi-component system replacing the unitary short-term store.

> [!atomic-candidate] Working Memory Model (1974)
> **Slug**: `working-memory-model`
> **Note Type**: framework
> **Priority**: critical
> **Estimated Scope**: 800-1200 words
> **Key Relationships**:
>   - →(supersedes)→ [[Short-Term Memory Store]]
>   - →(component-of)→ [[Human Memory Architecture]]
> **Source Status**: has-primary
> **Extraction Trigger**: Foundational framework in cognitive psychology.

The model consists of the Central Executive, Phonological Loop, and Visuo-Spatial Sketchpad.

%%ATOMIC: phonological-loop | component | high | distinct-subsystem-with-own-capacity%%
```
**Effectiveness**: ⭐⭐⭐⭐⭐

### Example 2: Meeting Notes Refactoring
**Context**: Converting rough meeting notes into actionable concepts.
**Full Prompt**:
```markdown
Review these notes on the "Project Phoenix" architecture. Identify distinct modules that need their own documentation using the atomic signaling.
```
**Outcome**:
```markdown
We agreed to use the Strangler Fig pattern to migrate the legacy monolith.

> [!atomic-candidate] Strangler Fig Pattern (2004)
> **Slug**: `strangler-fig-pattern`
> **Note Type**: method
> **Priority**: high
> **Estimated Scope**: 400-600 words
> **Key Relationships**:
>   - →(applied-in)→ [[Legacy Migration]]
> **Source Status**: needs-primary-review
> **Extraction Trigger**: Selected architectural strategy for Q1.
```
**Effectiveness**: ⭐⭐⭐⭐⭐

## 🔧 OPTIMIZATION HISTORY

### Version 1.0.0 - 2025-12-21
**Changes**: Initial formalization of the user's XML module.
**Impact**: Standardized the callout structure and priority definitions.

## 🎓 LESSONS LEARNED

- **Callout Formatting**: The `>` blockquote syntax is robust in Markdown, but if the LLM misses a newline, the callout breaks. The prompt must emphasize structure.
- **Over-Extraction**: Without the "DO NOT flag" criteria, LLMs tend to flag every single proper noun. The exclusion criteria are just as important as the inclusion criteria.
- **Slug Generation**: LLMs are good at generating `kebab-case` slugs, which saves significant time during manual file creation later.

## 📚 REFERENCES

- **Source**: User submitted XML (Module 3).
- **Concept**: Zettelkasten Method (Atomic Notes).
- **Tool**: Obsidian Callouts (Visual styling).
```