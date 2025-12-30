---
tags: #pkm #obsidian #reference-note #quick-reference #dataview
aliases: [Inline Field QRC, Dataview Fields Guide, Field Syntax Reference]
---

# 🏷️ Quick Reference: Inline Field Generation

## Syntax Formats

**Bracketed (inline embedding):**
````markdown
[**Field-Name**:: Value that can be long and descriptive.]
````

**Non-bracketed (line-start or own line):**
````markdown
**Field-Name**:: Short value or phrase
````

**With wiki-links:**
````markdown
**Related-Concepts**:: [[Concept 1]], [[Concept 2]]
````

## Field Type Quick Matrix

| Field Type | Trigger | Format Example |
|------------|---------|----------------|
| **Definition** | "X is defined as…" | `[**Term-Name**:: definition text]` |
| **Principle** | "The principle of X…" | `[**Principle-of-X**:: statement]` |
| **Distinction** | "X differs from Y…" | `[**X-vs-Y**:: difference]` |
| **Claim** | "Research shows…" | `[**Empirical-Finding**:: claim + source]` |
| **Framework** | "Model consists of…" | `[**Model-Name**:: components]` |
| **Caution** | "Common mistake…" | `[**Common-Pitfall**:: warning]` |
| **Example** | "For example…" | `[**Example-of-X**:: illustration]` |
| **Process** | "Steps are…" | `[**Process-Name**:: procedure]` |
| **Insight** | "Key insight is…" | `[**Key-Insight**:: realization]` |

## When to Create Inline Fields

✅ **CREATE field when content:**
- Provides formal/technical definition
- States foundational principle or rule
- Makes empirical claim with evidence
- Describes model/framework/taxonomy
- Documents step-by-step process
- Draws critical distinction
- Captures significant insight
- Contains queryable metadata

❌ **DON'T create field when:**
- Restating obvious information
- Transitional/meta-commentary
- Already tagged in same section
- Generic example without unique value
- Casual observation (not principle-level)

## Density Guidelines

| Note Type | Light | Standard | Dense |
|-----------|-------|----------|-------|
| **Atomic** | 3-5 | 5-8 | 8-12 |
| **Reference** | 8-15 | 15-25 | 25-50 |
| **Technical** | 15-20 | 20-35 | 35-60 |
| **Synthesis** | 10-15 | 15-25 | 25-40 |

> [!warning] Over-Tagging Threshold
> Never exceed 30% of sentences as inline fields. If every sentence becomes a field, you're over-tagging.

## Complete Field Type Taxonomy

### DEFINITIONAL FIELDS
````markdown
[**Cognitive-Load**:: The total mental effort used in working memory.]
[**Zettelkasten**:: A personal knowledge management system using atomic notes…]
[**DQL**:: Dataview Query Language—SQL-like syntax for Obsidian queries.]
````

### PRINCIPLE FIELDS
````markdown
[**Principle-of-Atomic-Notes**:: Each note contains exactly one idea, fully developed.]
[**Millers-Law**:: Average person can hold 7±2 chunks in working memory simultaneously.]
````

### DISTINCTION FIELDS
````markdown
[**Atomic-vs-Reference**:: Atomic notes contain single concepts (300-800 words), reference notes provide comprehensive coverage (1500-4000+ words).]
[**Intrinsic-vs-Extraneous-Load**:: Intrinsic stems from material complexity (unavoidable), extraneous from poor design (should minimize).]
````

### CLAIM FIELDS
````markdown
[**Spacing-Effect-Research**:: Distributed practice produces superior retention compared to massed practice (Cepeda et al., 2006), with optimal intervals expanding logarithmically.]
[**Testing-Effect-Finding**:: Retrieval practice enhances retention more than re-studying (Roediger & Karpicke, 2006).]
````

### QUOTATION FIELDS
````markdown
[**Quote-Luhmann-Zettelkasten**:: "The Zettelkasten is not mere collection; it is a tool to think with." (Luhmann, 1992)]
````

### FRAMEWORK FIELDS
````markdown
[**Cognitive-Load-Model**:: Three components: intrinsic (inherent complexity), extraneous (instructional burden), germane (schema construction effort).]
[**PARA-Model**:: Projects, Areas, Resources, Archives—organizational framework dividing information into four categories.]
````

### CAUTION FIELDS
````markdown
[**Pitfall-Over-Organization**:: Spending excessive time on organizational systems instead of actual knowledge work.]
[**Limitation-Spaced-Repetition**:: Optimizes retention of discrete facts but less effective for conceptual understanding.]
````

### PROCESS FIELDS
````markdown
[**Process-Progressive-Summarization**:: Layer 1: Capture. Layer 2: Bold passages. Layer 3: Highlight bolded. Layer 4: Executive summary.]
[**SuperMemo-Algorithm**:: Spaced repetition scheduling: new_interval = previous_interval × ease_factor.]
````

### INSIGHT FIELDS
````markdown
[**Key-Insight-Emergence**:: Zettelkasten value grows non-linearly—once connection density reaches critical mass, serendipitous discovery accelerates dramatically.]
````

## Example Integration in Context
````markdown
## Cognitive Load Theory

[**Cognitive-Load-Theory**:: Framework asserting working memory has limited capacity, and learning is optimized when total cognitive demands don't exceed this capacity.]

The theory identifies three types of load:

[**Intrinsic-Load**:: Inherent complexity of material, determined by element interactivity.]

[**Extraneous-Load**:: Cognitive burden imposed by poor instructional design rather than material itself.]

[**Germane-Load**:: Mental effort dedicated to schema construction—the "productive" load.]

[**Key-Implication-CLT**:: Since intrinsic load cannot be reduced, optimizing learning requires minimizing extraneous load while maximizing germane load.]

## Research Support

[**Sweller-Finding-1988**:: Cognitive load theory provides guidelines for presenting information in manner that encourages learner activities optimizing intellectual performance.]

[**Common-Pitfall-CLT-Application**:: Designers often reduce all load rather than distinguishing between extraneous (bad) and germane (good) load types.]
````

## Dataview Query Examples

**Extract all definitions:**
````dataviewj
const pages = dv.pages('#reference-note');
for (let page of pages) {
    const content = await dv.io.load(page.file.path);
    const defRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;
    let match;
    while (match = defRegex.exec(content)) {
        dv.paragraph(`**${match[1]}**: ${match[2]}`);
    }
}
````

**Query principles:**
````datavie
TABLE filter(file.lists, (item) => contains(item, "**Principle-"))
FROM #cognitive-science
SORT file.name
````

## Syntax Rules (Critical)

✅ **Correct:**
````markdown
[**Field-Name**:: Value text.]
**Field-Name**:: Value
**Related**:: [[Note 1]], [[Note 2]]
````

❌ **Incorrect:**
````markdown
**Field-Name: Value  (missing second colon)
** Field-Name**:: Value  (space before name)
**Field-Name** :: Value  (space before colons)
[**Field-Name**:: Value with ] bracket]  (closing bracket in value)
````

## Quick Self-Check
````
Are you tagging genuinely significant information?
├─ YES → Proceed
└─ NO → Skip field

Would this be useful in a Dataview query?
├─ YES → Strong candidate
└─ NO → Reconsider

Is this already captured in headers or structure?
├─ YES → Skip (redundant)
└─ NO → Proceed

Are you under 30% field density?
├─ YES → Safe to continue
└─ NO → Increase selectivity
````