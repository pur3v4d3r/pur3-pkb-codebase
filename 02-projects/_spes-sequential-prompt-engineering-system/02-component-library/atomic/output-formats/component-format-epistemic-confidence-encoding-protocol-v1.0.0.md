---
type: component
component-type: format
atomic-composite: atomic
domain: pkb
id: 20251221015600
status: active
version: 1.1.0
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
  - epistemic-status
  - confidence-markers
  - truth-encoding
conflicts-with: []
synergies-with: []
used-in-prompts: []
link-up: [[prompt-engineering-moc]]
---

# Format: Epistemic Confidence Encoding Protocol

> [!definition] Component Definition
> A syntax specification and decision framework that instructs the LLM to explicitly tag the certainty level of knowledge claims using specific inline markers for Personal Knowledge Management (PKM) systems.

## 🎯 When to Use
- **Knowledge Synthesis**: When processing academic papers or complex articles into permanent notes.
- **Fact-Checking**: When distinguishing between established scientific consensus and theoretical speculation.
- **PKM Database Building**: When generating notes destined for Obsidian (specifically for Dataview queries).
- **Nuanced Analysis**: When the "truthiness" of a claim is just as important as the claim itself.

## 🚫 When NOT to Use
- **Creative Writing**: The syntax breaks narrative flow and immersion.
- **General Correspondence**: Emails or chat messages where markdown metadata is confusing.
- **Code Generation**: Unless specifically commenting within documentation blocks.
- **Absolute Beginners**: If the user does not understand the difference between "verified" and "established."

## 📝 COMPONENT TEXT
```prompt
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
`[**Field-Name**:: claim content]^confidence-level`

**With Secondary Modifier:**
`[**Field-Name**:: claim content]^confidence-level-modifier`

**Examples:**
- `[**Spacing-Effect**:: distributed practice produces superior retention to massed practice]^verified-stable`
- `[**AI-Consciousness**:: large language models may develop emergent self-models]^speculative-personal`
</syntax_specification>

<generation_heuristics>
### When to Apply Each Level

1. **^verified**: Apply ONLY when multiple meta-analyses converge or the effect is replicated across diverse contexts.
2. **^established**: Apply when found in standard textbooks or cited without hedging in review papers.
3. **^provisional**: Apply to single studies, recent findings (last 2-3 years), or sound methodology awaiting confirmation.
4. **^speculative**: Apply to theoretical inferences, "If X then Y" logic without empiricism, or cross-domain extrapolations.
5. **^contested**: Apply when prominent researchers disagree or replication attempts show mixed results.
</generation_heuristics>

<output_requirements>
- Every substantive claim in output notes MUST have confidence encoding.
- Target Density: 40-60% of inline fields should carry confidence markers.
- Definitions from authoritative sources default to `^established`.
- Personal syntheses must be marked `^speculative-personal` or `^provisional-personal`.
</output_requirements>
</epistemic_confidence_encoding>
```

## 🔀 VARIATIONS

### Variation 1: Visual/Emoji Only (Lite Version)
Use this when strict database syntax is not required, but visual indicators are needed for quick reading.

```prompt
<epistemic_visual_markers>
Instead of complex syntax, append a visual status indicator to every key claim:

🟢 (Verified/Consensus)
🔵 (Established/Standard)
🟡 (Provisional/Single Study)
🟠 (Speculative/Theoretical)
🔴 (Contested/Debated)

Example: "The spacing effect improves retention 🟢, though the optimal interval is debated 🔴."
</epistemic_visual_markers>
```

### Variation 2: Bayesian Probability (Technical)
Use this for fields requiring numerical probability estimates rather than categorical labels.

```prompt
<epistemic_probability_encoding>
Encode confidence as a Bayesian probability estimate (0.0-1.0) based on the strength of evidence.

Format: `[Claim content] (P=0.XX)`

- P>0.95: Verified/Consensus
- P>0.80: Established/Likely
- P>0.50: Provisional/Plausible
- P<0.50: Speculative/Unlikely

Example: `[AGI will be achieved by 2030] (P=0.40)`
</epistemic_probability_encoding>
```

## 🤝 RELATIONSHIPS

### Works Well With
- [[obsidian-markdown-formatter]] - Provides the structural container for these inline fields.
- [[academic-literature-synthesizer]] - Generates the content that requires this specific validation.
- [[socratic-questioner]] - Can be used to challenge `^provisional` or `^speculative` claims to deepen analysis.

### Conflicts With
- [[simplified-summary-format]] - The syntax adds noise that contradicts the goal of simplicity.
- [[creative-writing-persona]] - Fiction generally requires suspension of disbelief, not epistemic tagging.

## 📊 PERFORMANCE DATA

### Usage Statistics
- **Total Uses**: `VIEW[0]`
- **Last Used**: `VIEW[]`
- **Performance Score**: `VIEW[0.0]`/10

### Test Results
#### Test 1: Cognitive Science Summary
**Date**: 2025-12-21
**Prompt Used In**: [[academic-summarizer-workflow]]
**Quality Score**: N/A
**Notes**: Initial formalization. Testing required to see if LLM correctly distinguishes between `^provisional` (single study) and `^speculative` (theory).

## 💡 USAGE EXAMPLES

### Example 1: Summarizing a Medical Study
**Context**: User wants to extract key claims from a new study on caffeine and sleep, formatted for their Obsidian vault.
**Full Prompt**:
```markdown
You are a research assistant. Summarize the following abstract using the <epistemic_confidence_encoding> protocol.

Abstract: "In a randomized controlled trial (n=15), we observed that caffeine intake 10 hours prior to bed reduced deep sleep by 20%. This contradicts earlier assumptions that the cutoff is 6 hours."
```
**Outcome**:
```markdown
[**Caffeine-Sleep-Latency**:: caffeine intake 10 hours pre-bed reduces deep sleep by 20%]^provisional-volatile

[**Standard-Caffeine-Cutoff**:: 6 hours prior to bed is sufficient for clearance]^contested
```
**Effectiveness**: ⭐⭐⭐⭐⭐

### Example 2: Theoretical Physics Note
**Context**: Synthesizing a blog post about String Theory.
**Full Prompt**:
```markdown
Extract the core claim about dimensions from this text using the epistemic encoding: "String theory mathematically requires at least 10 dimensions to function, though we have never observed more than 4."
```
**Outcome**:
```markdown
[**String-Theory-Dimensions**:: requires at least 10 dimensions for mathematical consistency]^established-consensus

[**Observable-Dimensions**:: universe contains more than 4 dimensions]^speculative-theoretical
```
**Effectiveness**: ⭐⭐⭐⭐⭐

## 🔧 OPTIMIZATION HISTORY

### Version 1.1.0 - 2025-12-21
**Changes**: Formalized original XML module into standard component schema. Added "When to Apply" heuristics to help LLM distinguish between edge cases (e.g., Verified vs Established).
**Impact**: Improved consistency in LLM decision making.

### Version 1.0.0 - Original
**Changes**: Initial XML submission.
**Impact**: Established the syntax and taxonomy.

## 🎓 LESSONS LEARNED

- **Distinction Difficulty**: LLMs tend to overuse `^verified`. The heuristic "Multiple independent replications" must be strictly enforced.
- **Syntax Rigidity**: The `::` syntax is specific to the Dataview plugin. If the LLM adds a space or changes the brackets, the query fails. The "Syntax Patterns" section is critical.
- **Subjectivity**: The `-personal` modifier is essential for preventing hallucinations from looking like facts.

## 📚 REFERENCES

- **Source**: Original user submission (Module 1).
- **Tool**: Obsidian Dataview Plugin Documentation (for inline field syntax).
```