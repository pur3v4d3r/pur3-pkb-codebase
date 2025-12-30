


> [!wave] ### Claude Thinking
> The user wants Quick Reference Cards (QRCs) for the comprehensive PKB Obsidian Specialist Module. These should be condensed, scannable, practical guides that extract the essential decision trees, syntax patterns, and heuristics from the massive 35k token module.
> I should create multiple QRCs covering different aspects:
> 1. Metadata Generation QRC
> 2. Wiki-Link Protocol QRC
> 3. Callout Taxonomy QRC
> 4. Inline Field Generation QRC
> 5. Semantic Color Coding QRC
> 6. Note Type Specifications QRC
> 7. Quality Gates Checklist QRC
> 8. Expansion Section QRC
> Each should be:
> - Highly scannable (tables, decision trees, visual hierarchy)
> - Concise but complete (no fluff, just actionable info)
> - Production-ready (can be used as actual reference during note creation)
> - Formatted for Obsidian (uses callouts, tables, formatting appropriately)
> - Self-contained (doesn't require referring back to main document)
> Format as actual markdown files that could be saved as reference notes in an Obsidian vault.
> I'll create a comprehensive set of Quick Reference Cards that distill the module into scannable, actionable guides. These are formatted as Obsidian notes you can paste directly into your vault.
> 
---



Table of Contents

[[#Wiki-Link Protocol]]
[[#Semantic Callouts Reference]]
[[#Field Syntax Reference]]
[[#Semantic Colors Reference]]
[[#Note Classification Guide]]
[[#Quality Gates Checklist]]






`````markdown
---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Metadata QRC, YAML Frontmatter Guide, Tag Generation Quick Ref]
---

# 📋 Quick Reference: Metadata Generation

## YAML Frontmatter Template

```yaml
---
tags: #primary-domain #methodology #content-type [#technical] [#status]
aliases: [Alternative 1, Abbrev, Search Term, Related]
created: {{date:YYYY-MM-DD}}
modified: {{date:YYYY-MM-DD}}
status: [seedling|budding|evergreen|wilting]
certainty: [speculative|probable|confident|verified]
type: [atomic|reference|moc|synthesis|index|dashboard]
related: [[Note 1]], [[Note 2]], [[Note 3]]
---
```

## Tag Generation: 5-Position System

| Position | Type | Example | Decision Logic |
|----------|------|---------|----------------|
| **1** | **Primary Domain** | `#cognitive-science` | Broad category - singular, lowercase, hyphenated |
| **2** | **Methodology** | `#zettelkasten` | Framework/approach being discussed |
| **3** | **Content Type** | `#reference-note` | Structural classification (atomic/reference/moc/synthesis) |
| **4** | **Technical** | `#dataview-query` | Optional - Tool/language/plugin specific |
| **5** | **Status/Meta** | `#in-progress` | Optional - Workflow/priority indicator |

> [!important] Tag Requirements
> - **Total:** 3-5 tags (3 mandatory, 2 optional)
> - **Format:** `#lowercase-hyphenated` (no spaces, no camelCase)
> - **Avoid:** Generic tags like `#notes` or `#information`

## Alias Generation: 4 Types

| Type | Purpose | Example |
|------|---------|---------|
| **Abbreviations** | Common shortenings | `PKM` for "Personal Knowledge Management" |
| **Alternative Phrasings** | Semantic equivalents | `Knowledge Base` for "PKB Architecture" |
| **Search Terms** | How users might search | `Note Card System` for "Zettelkasten" |
| **Related Concepts** | Adjacent terminology | `Atomic Notes` for "Evergreen Notes" |

> [!helpful-tip] Alias Quantity
> - **Minimum:** 2 aliases
> - **Target:** 3-4 aliases
> - **Maximum:** 5 aliases (avoid clutter)

## Status Field Values

```yaml
status: seedling   # Initial capture, rough notes, incomplete
status: budding    # Structure emerging, connections forming
status: evergreen  # Mature, well-developed, high-confidence
status: wilting    # Outdated, superseded, needs revision
```

## Certainty Field Values

```yaml
certainty: speculative  # Hypothesis, unverified, exploratory
certainty: probable     # Some supporting evidence
certainty: confident    # Well-supported, multiple sources
certainty: verified     # Empirically validated, authoritative
```

## Decision Tree: To Metadata or Not?

```
IS this a permanent note?
├─ Reference Note? → YES - Full metadata required
├─ Atomic Note? → YES - Full metadata required
├─ MOC? → YES - Full metadata required
├─ Synthesis Note? → YES - Full metadata required
├─ Simple query response? → NO - Skip metadata
├─ Conversational answer? → NO - Skip metadata
└─ Temporary/scratch note? → NO - Skip metadata
```

## Quick Examples

**For "Chain-of-Thought Prompting Techniques":**
```yaml
---
tags: #prompt-engineering #cognitive-frameworks #reference-note #llm-optimization
aliases: [CoT Prompting, Chain of Thought, Reasoning Chain Techniques]
status: evergreen
certainty: confident
type: reference
---
```

**For "Intrinsic Cognitive Load":**
```yaml
---
tags: #cognitive-science #cognitive-load-theory #atomic-note
aliases: [Intrinsic Load, Element Interactivity, Inherent Complexity]
status: evergreen
certainty: verified
type: atomic
---
```



----
----
----



## Obsidian Automation MOC

**For "Obsidian Automation MOC":**
```yaml
---
tags: #obsidian #pkm #moc #automation
aliases: [Automation Hub, Workflow Index, Plugin Synergies Map]
status: budding
type: moc
---
```
`````











---
----
----








## Wiki-Link Protocol


`````markdown
---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Wiki-Link QRC, Linking Guide, Knowledge Graph Reference]
---

# 🔗 Quick Reference: Wiki-Link Protocol

## Discovery Heuristic: When to Create Links

**CREATE `[[Wiki-Link]]` if ANY of these are true:**

✅ Core concept central to response  
✅ Technical term requiring definition  
✅ Topic with potential for separate note  
✅ Cross-reference opportunity to existing knowledge  
✅ Subject area with exploratory depth  
✅ Framework or methodology with theoretical foundation  
✅ Person/author significant to the field  
✅ Tool or plugin in ecosystem  
✅ Process or technique with procedural knowledge  

**DO NOT link:**

❌ Generic terms not specific to domain ("things", "ideas")  
❌ Every mention of same term (link first occurrence only per section)  
❌ Common words just because notes might exist  
❌ Trivial concepts not warranting dedicated notes  

## Target Density by Note Type

| Note Type | Target Wiki-Links | Links per Section |
|-----------|-------------------|-------------------|
| **Simple Query** | 3-6 | 2-3 |
| **Atomic Note** | 5-8 | 3-5 |
| **Reference Note** | 20-40 | 5-15 |
| **MOC** | 30-100+ | N/A (primary feature) |
| **Synthesis Note** | 15-30 | 5-10 |
| **Technical Guide** | 15-40 | 5-12 |

## Link Format Patterns

**Standard Link:**
```markdown
[[Note Title]]
```

**Display Text Link:**
```markdown
[[Note Title|Display Text]]
```
Use when: Grammatical integration, shortened reference, alternative phrasing

**Section Link:**
```markdown
[[Note Title#Section Heading]]
[[Note Title#Section|Display Text]]
```

**Block Link:**
```markdown
[[Note Title#^block-id]]
```

## Quality Decision Tree

```
FOR each potential link candidate:

Does term represent discrete, learnable concept?
├─ NO → Don't link
└─ YES → Continue

Would reader benefit from dedicated note?
├─ NO → Keep as plain text
└─ YES → Continue

Does link create meaningful graph connection?
├─ NO → Reconsider
└─ YES → Continue

Has term been linked in this section already?
├─ YES → Don't link again
└─ NO → CREATE LINK [[Term]]
```

## Link Pattern Examples

> [!example] Good Linking
> [[Cognitive Load Theory]] explains how cognitive load affects learning. When load exceeds capacity, it overwhelms [[Working Memory]].
> 
> *Links key concepts once per section*

> [!warning] Over-Linking (Avoid)
> [[Cognitive Load]] theory explains how [[cognitive load]] affects learning. When [[cognitive load]] is too high, [[cognitive load]] overwhelms [[working memory]].
> 
> *Same term linked repeatedly = visual clutter*

> [!warning] Under-Linking (Avoid)
> Cognitive Load Theory explains how cognitive load affects learning through working memory constraints and schema construction.
> 
> *Missing obvious opportunities for key concepts*

## Category-Specific Linking

**Theoretical Frameworks:**
```markdown
[[Cognitive Load Theory]], [[Self-Determination Theory]], [[Dual Coding Theory]]
```

**Technical Terms:**
```markdown
[[Dataview]], [[DQL]], [[DataviewJS]], [[Meta Bind]]
```

**Methodologies:**
```markdown
[[Zettelkasten]], [[Progressive Summarization]], [[Spaced Repetition]]
```

**Processes:**
```markdown
[[Atomic Note Creation]], [[MOC Development]], [[Knowledge Graph Building]]
```

## Bi-Directional Linking Strategy

When creating links, consider:

**Forward Links** (this note → others):
- Primary connections outward

**Potential Backlinks** (others → this note):
- What existing notes should link here?
- Mention in "Related Topics" section

**Example:**
```markdown
In [[Cognitive Load Theory]]:

Forward links to:
- [[Working Memory]]
- [[Schema Theory]]
- [[Instructional Design]]

Should be linked from:
- [[Learning Theory Overview]]
- [[Educational Psychology]]
- [[Multimedia Learning]]
```

## Link Density Self-Check

```
Squint test: Can you identify 5-8 key concepts by scanning for wiki-links?
├─ YES → Good density
└─ NO → Adjust (too sparse or too dense)

Every paragraph has links?
├─ YES → Good knowledge graph building
└─ NO → Scan for missed opportunities

Every sentence has links?
├─ YES → Probably over-linking (reduce)
└─ NO → Check if key concepts are linked
```

## Integration with Display Text

**Use display text for:**

1. **Grammatical flow:**
   ```markdown
   theories of [[Cognitive Load Theory|cognitive load]]
   ```

2. **Abbreviation expansion:**
   ```markdown
   [[Self-Determination Theory|SDT]]
   ```

3. **Section-specific reference:**
   ```markdown
   [[Cognitive Load Theory#Intrinsic Load|intrinsic cognitive load]]
   `````









----
----
----








## Semantic Callouts Reference


`````

---

```markdown
---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Callout QRC, Callout Guide, Semantic Callouts Reference]
---

# 📢 Quick Reference: Callout Taxonomy

## Most Common Callout Types (Top 10)

| Callout | Icon | Primary Use | Example |
|---------|------|-------------|---------|
| `[!definition]` | 📖 | Formal definitions | Technical term explanations |
| `[!example]` | 💡 | Concrete illustrations | Practical demonstrations |
| `[!warning]` | ⚠️ | Cautions & pitfalls | Common mistakes to avoid |
| `[!important]` | ❗ | Critical information | Must-know points |
| `[!key-claim]` | 🎯 | Central arguments | Main thesis statements |
| `[!evidence]` | 📊 | Supporting data | Research findings |
| `[!helpful-tip]` | 💡 | Practical guidance | Best practices |
| `[!methodology-and-sources]` | ⚙️ | Process explanation | How things work |
| `[!note]` | 📝 | Supplementary info | Additional context |
| `[!abstract]` | 📋 | Summary/overview | Executive summaries |

## Complete Taxonomy (30+ Types)

### STRUCTURAL (Organization)
```markdown
> [!abstract] - Summaries & overviews
> [!definition] - Formal definitions
> [!principle-point] - Foundational principles
> [!structure] - Organizational frameworks
```

### COGNITIVE (Learning Aids)
```markdown
> [!example] - Concrete illustrations
> [!analogy] - Comparative understanding
> [!thought-experiment] - Exploratory reasoning
> [!mental-model] - Conceptual frameworks
> [!mnemonic] - Memory aids
```

### ANALYTICAL (Critical Thinking)
```markdown
> [!key-claim] - Central arguments
> [!evidence] - Supporting data
> [!counter-argument] - Alternative perspectives
> [!assumption] - Underlying premises
> [!limitation] - Boundary conditions
> [!implication] - Logical consequences
```

### PRAGMATIC (Application)
```markdown
> [!methodology-and-sources] - Process explanation
> [!what-this-does] - Functional description
> [!helpful-tip] - Practical guidance
> [!how-to] - Step-by-step instructions
> [!workflow] - Process sequences
> [!checklist] - Verification lists
```

### DIRECTIVE (Attention)
```markdown
> [!important] - Critical information
> [!warning] - Cautions & pitfalls
> [!attention] - Focus points
> [!danger] - Severe warnings
> [!caution] - Moderate warnings
```

### INFORMATIONAL (Reference)
```markdown
> [!note] - Supplementary information
> [!info] - Background information
> [!quote] - Direct citations
> [!cite] - Source attribution
```

### INTERACTIVE (Dynamic)
```markdown
> [!question] - Open questions
> [!faq] - Frequently asked questions
> [!todo] - Action items
> [!success] - Positive outcomes
> [!failure] - Failed approaches
```

## Callout Syntax Patterns

**Basic:**
```markdown
> [!type] Title
> Content line 1
> Content line 2
```

**Foldable (collapsed by default):**
```markdown
> [!type]Collapsed Title
> Hidden content
```

**Foldable (expanded by default):**
```markdown
> [!type]+ Expanded Title
> Visible content
```

**No Title:**
```markdown
> [!type]
> Content without title line
```

**Nested (max 3 levels):**
```markdown
> [!warning] Outer Warning
> Context
> > [!example] Nested Example
> > Details
> > > [!note] Deep Note
> > > Additional detail
```

## Density Guidelines

| Note Type | Target Callouts | Callouts per 500 words |
|-----------|-----------------|------------------------|
| **Atomic Note** | 2-4 | 2-3 |
| **Reference Note** | 12-15 | 3-4 |
| **MOC** | 5-8 | 2-3 |
| **Synthesis Note** | 10-12 | 4-5 |
| **Technical Guide** | 15-20 | 5-6 |

> [!warning] Over-Use Warning
> If >30% of your note is inside callouts, you're over-using them. Callouts should accent prose, not replace it.

## Selection Decision Tree

```
What is the primary purpose of this content block?

Definitional → [!definition] or [!principle-point]
Example/Analogy → [!example] or [!analogy]
Warning/Caution → [!danger] / [!warning] / [!caution] (by severity)
Process/How-To → [!how-to] or [!methodology-and-sources]
Argument/Claim → [!key-claim] with [!evidence] support
Alternative View → [!counter-argument]
Supplementary → [!note] or [!info]
Critical Point → [!important] or [!attention]
Question → [!question]
Meta/Structural → [!abstract] or [!structure]
```

## Common Patterns

**Definition + Example:**
```markdown
> [!definition] Cognitive Load
> The total mental effort being used in working memory.

> [!example] Real-World Application
> When learning to drive, managing steering + pedals + traffic rules
> simultaneously creates high cognitive load for beginners.
```

**Claim + Evidence:**
```markdown
> [!key-claim] Spaced Repetition Superiority
> Distributed practice produces better long-term retention than massing.

> [!evidence] Research Support
> Cepeda et al. (2006) meta-analysis of 317 experiments confirms
> consistent advantage of spacing (effect size d=0.40-0.60).
```

**Process + Warning:**
```markdown
> [!methodology-and-sources] Setup Process
> 1. Install Dataview plugin
> 2. Enable JavaScript queries
> 3. Create first DQL query

> [!warning] Common Pitfall
> Forgetting to enable JS queries causes DataviewJS code blocks
> to fail silently without error messages.
```

**Important + Supporting Tip:**
```markdown
> [!important] Critical Principle
> Link notes by meaning, not by topic hierarchy.

> [!helpful-tip] Implementation
> Ask "How does this connect?" not "Where does this belong?"
```

## Nesting Best Practices

✅ **Good Nesting:**
```markdown
> [!warning] Platform Compatibility
> This feature has platform-specific behaviors:
> > [!info] Windows
> > Full functionality supported
> > 
> > [!caution] Mobile
> > Limited - JavaScript execution unavailable
```

❌ **Excessive Nesting:**
```markdown
> [!note] Outer
> > [!info] Level 2
> > > [!example] Level 3
> > > > [!warning] Level 4 ← TOO DEEP
```

## Quick Self-Check

```
Does every callout serve a clear semantic purpose?
├─ YES → Good usage
└─ NO → Convert to prose or remove

Are callouts distributed evenly across sections?
├─ YES → Good balance
└─ NO → Redistribute or reduce

Can the note be read comfortably with callouts present?
├─ YES → Appropriate density
└─ NO → Reduce callout usage
`````









----
----
----









## Field Syntax Reference

`````

---

```markdown
---
tags: #pkm #obsidian #reference-note #quick-reference #dataview
aliases: [Inline Field QRC, Dataview Fields Guide, Field Syntax Reference]
---

# 🏷️ Quick Reference: Inline Field Generation

## Syntax Formats

**Bracketed (inline embedding):**
```markdown
[**Field-Name**:: Value that can be long and descriptive.]
```

**Non-bracketed (line-start or own line):**
```markdown
**Field-Name**:: Short value or phrase
```

**With wiki-links:**
```markdown
**Related-Concepts**:: [[Concept 1]], [[Concept 2]]
```

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
```markdown
[**Cognitive-Load**:: The total mental effort used in working memory.]
[**Zettelkasten**:: A personal knowledge management system using atomic notes…]
[**DQL**:: Dataview Query Language—SQL-like syntax for Obsidian queries.]
```

### PRINCIPLE FIELDS
```markdown
[**Principle-of-Atomic-Notes**:: Each note contains exactly one idea, fully developed.]
[**Millers-Law**:: Average person can hold 7±2 chunks in working memory simultaneously.]
```

### DISTINCTION FIELDS
```markdown
[**Atomic-vs-Reference**:: Atomic notes contain single concepts (300-800 words), reference notes provide comprehensive coverage (1500-4000+ words).]
[**Intrinsic-vs-Extraneous-Load**:: Intrinsic stems from material complexity (unavoidable), extraneous from poor design (should minimize).]
```

### CLAIM FIELDS
```markdown
[**Spacing-Effect-Research**:: Distributed practice produces superior retention compared to massed practice (Cepeda et al., 2006), with optimal intervals expanding logarithmically.]
[**Testing-Effect-Finding**:: Retrieval practice enhances retention more than re-studying (Roediger & Karpicke, 2006).]
```

### QUOTATION FIELDS
```markdown
[**Quote-Luhmann-Zettelkasten**:: "The Zettelkasten is not mere collection; it is a tool to think with." (Luhmann, 1992)]
```

### FRAMEWORK FIELDS
```markdown
[**Cognitive-Load-Model**:: Three components: intrinsic (inherent complexity), extraneous (instructional burden), germane (schema construction effort).]
[**PARA-Model**:: Projects, Areas, Resources, Archives—organizational framework dividing information into four categories.]
```

### CAUTION FIELDS
```markdown
[**Pitfall-Over-Organization**:: Spending excessive time on organizational systems instead of actual knowledge work.]
[**Limitation-Spaced-Repetition**:: Optimizes retention of discrete facts but less effective for conceptual understanding.]
```

### PROCESS FIELDS
```markdown
[**Process-Progressive-Summarization**:: Layer 1: Capture. Layer 2: Bold passages. Layer 3: Highlight bolded. Layer 4: Executive summary.]
[**SuperMemo-Algorithm**:: Spaced repetition scheduling: new_interval = previous_interval × ease_factor.]
```

### INSIGHT FIELDS
```markdown
[**Key-Insight-Emergence**:: Zettelkasten value grows non-linearly—once connection density reaches critical mass, serendipitous discovery accelerates dramatically.]
```

## Example Integration in Context

```markdown
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
```

## Dataview Query Examples

**Extract all definitions:**
```dataviewj
const pages = dv.pages('#reference-note');
for (let page of pages) {
    const content = await dv.io.load(page.file.path);
    const defRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;
    let match;
    while (match = defRegex.exec(content)) {
        dv.paragraph(`**${match[1]}**: ${match[2]}`);
    }
}
```

**Query principles:**
```datavie
TABLE filter(file.lists, (item) => contains(item, "**Principle-"))
FROM #cognitive-science
SORT file.name
```

## Syntax Rules (Critical)

✅ **Correct:**
```markdown
[**Field-Name**:: Value text.]
**Field-Name**:: Value
**Related**:: [[Note 1]], [[Note 2]]
```

❌ **Incorrect:**
```markdown
**Field-Name: Value  (missing second colon)
** Field-Name**:: Value  (space before name)
**Field-Name** :: Value  (space before colons)
[**Field-Name**:: Value with ] bracket]  (closing bracket in value)
```

## Quick Self-Check

```
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
`````






----
----
----






## Semantic Colors Reference

`````

---

```markdown
---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Color Coding QRC, HTML Color Guide, Semantic Colors Reference]
---

# 🎨 Quick Reference: Semantic Color Coding

## Color Palette & Semantic Roles

| Role | Color | Hex | Use When |
|------|-------|-----|----------|
| **🟡 Primary/Key** | <span style='color: #FFC700;'>Imperial Gold</span> | `#FFC700` | Core definitions, main arguments, key terms |
| **🟣 Secondary** | <span style='color: #9E6CD3;'>Deep Amethyst</span> | `#9E6CD3` | Meta-notes, context, deprecated content |
| **🔵 Technical** | <span style='color: #72FFF1;'>Cyber Cyan</span> | `#72FFF1` | Technical terms, code, data, specs |
| **🔴 Critical** | <span style='color: #FF00DC;'>Neon Magenta</span> | `#FF00DC` | Warnings, errors, conflicts |
| **🟢 Verified** | <span style='color: #27FF00;'>Terminal Green</span> | `#27FF00` | Established truths, verified facts |
| **🟠 Reference** | <span style='color: #FF5700;'>Reactor Orange</span> | `#FF5700` | Citations, questions, sources |

## Syntax Patterns

**Basic color:**
```html
<span style='color: #HEXCODE;'>Colored text</span>
```

**Bold + color:**
```html
<span style='color: #FF00DC; font-weight: bold;'>Critical bold</span>
```

**Italic + color:**
```html
<span style='color: #72FFF1; font-style: italic;'>Technical italic</span>
```

**Strikethrough + color (deprecated):**
```html
<span style='text-decoration: line-through; color: #9E6CD3;'>Old approach</span>
```

**Background highlight:**
```html
<span style='background-color: #FFC70040;'>Highlighted text</span>
```

**Text + background:**
```html
<span style='background-color: #FFC70040; color: #FFC700;'>Maximum emphasis</span>
```

## When to Use Each Color

### 🟡 IMPERIAL GOLD (`#FFC700`)

**Apply to:**
- Core definitions introduced first time
- Central thesis or main argument
- Key terminology discussion depends upon
- "The answer is…" statements
- Terms referenced repeatedly later

**Example:**
```html
<span style='color: #FFC700;'>**Cognitive Load Theory**</span> explains how mental effort affects learning.
```

---

### 🟣 DEEP AMETHYST (`#9E6CD3`)

**Apply to:**
- Meta-commentary about structure
- Contextual framing ("Building upon…")
- Editorial notes or authorial asides
- Less critical details
- Deprecated/superseded information

**Example:**
```html
<span style='text-decoration: line-through; color: #9E6CD3;'>Old three-part framework</span> → New five-component model
```

---

### 🔵 CYBER CYAN (`#72FFF1`)

**Apply to:**
- Technical terms with precise meanings
- Code syntax, function names, APIs
- File paths, configuration parameters
- Data points, statistics, measurements
- Plugin/tool names

**Example:**
```html
Use <span style='color: #72FFF1;'>**Dataview**</span> plugin with <span style='color: #72FFF1;'>DQL</span> syntax.
```

---

### 🔴 NEON MAGENTA (`#FF00DC`)

**Apply to:**
- Warnings about common mistakes
- Critical issues needing attention
- Contradictions requiring resolution
- "Do NOT…" prohibitions
- Failure modes or edge cases

**Example:**
```html
<span style='color: #FF00DC;'>⚠️ Warning:</span> This will <span style='color: #FF00DC; font-weight: bold;'>delete all data</span>.
```

---

### 🟢 TERMINAL GREEN (`#27FF00`)

**Apply to:**
- Established principles accepted as true
- Successfully verified information
- Canonical definitions from authorities
- Completed tasks or resolved items
- Empirically validated findings

**Example:**
```html
<span style='color: #27FF00;'>✓ Verified:</span> This approach produces <span style='color: #27FF00;'>consistent results</span>.
```

---

### 🟠 REACTOR ORANGE (`#FF5700`)

**Apply to:**
- Citations and source attributions
- External resource references
- Questions requiring investigation
- Links to external documentation
- "According to [Source]…" statements

**Example:**
```html
<span style='color: #FF5700;'>According to Smith (2020)</span>, the effect is significant.
```

## Common Combination Patterns

**Definition with Source:**
```html
<span style='color: #FF5700;'>According to Sweller (1988)</span>, <span style='color: #FFC700;'>**cognitive load**</span> comprises <span style='color: #27FF00;'>intrinsic, extraneous, and germane components</span>.
```

**Technical Warning:**
```html
<span style='color: #FF00DC;'>⚠️ Critical:</span> Never use <span style='color: #72FFF1;'>`localStorage`</span> in artifacts—causes <span style='color: #FF00DC;'>silent failures</span>.
```

**Deprecated → Current:**
```html
<span style='text-decoration: line-through; color: #9E6CD3;'>Old approach</span> → <span style='color: #FFC700;'>Current best practice</span> → <span style='color: #27FF00;'>Verified solution</span>
```

**Process with Critical Step:**
```html
<span style='color: #72FFF1;'>Capture</span> → <span style='color: #72FFF1;'>Process</span> → <span style='color: #FF00DC; font-weight: bold;'>Link (CRITICAL)</span> → <span style='color: #72FFF1;'>Refine</span>
```

## Density Guidelines

**Target Ranges:**
- Minimum: 5-10% of text colored
- Target: 15-25% of text colored
- Maximum: 30-35% of text colored
- Never exceed: 40% (readability breaks down)

**Per 500-word section:**
- Minimum: 2-3 colored spans
- Target: 5-8 colored spans
- Maximum: 12-15 colored spans

> [!warning] Over-Saturation Alert
> If every sentence is colored, the system loses meaning. Color should draw the eye to what matters most.

## Quick Self-Check

```
Squint test: Can you identify 3-5 key points by color alone?
├─ YES → Good balance
└─ NO → Adjust density

Does each color serve distinct semantic purpose?
├─ YES → Good differentiation
└─ NO → Review semantic mapping

Can section be read comfortably?
├─ YES → Acceptable density
└─ NO → Reduce color usage
```

## Accessibility Requirements

> [!important] Never Rely on Color Alone
> Always provide textual indicators:
> - Warnings: ⚠️ + "Warning:" + **bold**
> - Verified: ✓ + "Verified:" + color
> - Questions: ❓ + "Question:" + color
> - Critical: ⚠️ + "CRITICAL:" + **bold** + color

## Activation Logic

**Auto-activate when:**
- Content has multiple semantic categories
- User requests "color coding" or "visual hierarchy"
- Technical documentation with warnings + code
- Content benefits from scannable anchors

**Suppress when:**
- User requests "plain text"
- Output for non-HTML platforms
- Simple Q&A without complexity
- Accessibility requirements prohibit color
`````








----
-----
----







## Note Classification Guide

`````

---

```markdown
---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Note Types QRC, Note Classification Guide]
---

# 📝 Quick Reference: Note Type Specifications

## Note Type Comparison Matrix

| Type | Length | Wiki-Links | Callouts | Metadata? | Purpose |
|------|--------|------------|----------|-----------|---------|
| **Simple Query** | 300-600 | 3-6 | 2-3 | ❌ NO | Quick answer |
| **Atomic** | 300-800 | 5-8 | 2-4 | ✅ YES | Single concept |
| **Reference** | 1500-4000+ | 20-40 | 12-15 | ✅ YES | Comprehensive resource |
| **MOC** | Variable | 30-100+ | 5-8 | ✅ YES | Navigation hub |
| **Synthesis** | 800-1500 | 15-30 | 10-12 | ✅ YES | Cross-domain integration |
| **Technical** | Variable | 15-40 | 15-20 | ✅ YES | Implementation guide |

## ATOMIC NOTES

**Purpose:** Thoroughly explain ONE concept

**Structure:**
```markdown
---
tags: #domain #concept #atomic-note
aliases: [Alt Name, Abbrev]
status: budding
type: atomic
---

# [Concept Name]

> [!definition] [Concept]
> Clear, precise definition

## Core Explanation
[What it is, why it matters, how it works]

## Key Distinctions
[What it's NOT, boundary clarification]

> [!example] Concrete Illustration
> [Specific example]

## Connections
[Relationships to related concepts]

## Applications
[Where/how this applies in practice]

## 🔗 Related Topics for PKB Expansion
[4 extension topics]
```

**Target Specs:**
- Length: 300-800 words
- Wiki-Links: 5-8 highly relevant
- Callouts: 2-4 semantic
- Focus: Clarity, precision, foundation

---

## REFERENCE NOTES

**Purpose:** Exhaustive coverage as permanent knowledge artifact

**Structure:**
```markdown
---
tags: #domain #framework #reference-note #subdomain
aliases: [Full Name, Abbrev, Search Terms]
status: evergreen
type: reference
---

# [Topic Name]

> [!abstract] Overview
> Executive summary

## Theoretical Foundations
[Academic frameworks, principles, history]

> [!definition] Key Term
> [Definition]

## Core Concepts
[Detailed explanation]

> [!key-claim] Central Proposition
> [Claim with support]

> [!evidence] Supporting Research
> [Empirical evidence]

## Practical Applications
[Real-world use cases]

> [!example] Application Scenario
> [Concrete demonstration]

## Advanced Topics
[Sophisticated extensions]

## Critical Analysis
[Limitations, competing views]

## References
[Citations]

## 🔗 Related Topics for PKB Expansion
[4-6 extension topics]
```

**Target Specs:**
- Length: 1500-4000+ words (no upper limit)
- Wiki-Links: 20-40 for knowledge graph
- Callouts: 12-15 for organization
- Focus: Depth, comprehensiveness, scholarly rigor

---

## MAPS OF CONTENT (MOCs)

**Purpose:** Curated navigation hub for knowledge domain

**Structure:**
```markdown
---
tags: #domain #moc
aliases: [Domain Map, Domain Index]
status: evergreen
type: moc
---

# [Domain] Map of Content

> [!abstract] Domain Overview
> Scope and organization

## Dashboard Metrics
**Total Notes:** [Dataview count]
**Maturity:** [Distribution]

## Core Concepts (🌳 Evergreen)
- [[Concept 1]] - Brief description
- [[Concept 2]] - Brief description

## Developing Notes (🌿 Budding)
- [[Topic 1]] - Status and needs

## Emerging Ideas (🌱 Seedling)
- [[New Concept]] - Initial thoughts

## Requires Attention (🍂 Wilting)
- [[Outdated Note]] - Why needs review

## Semantic Bridges
**To [[Other Domain MOC]]:**
- [[Bridge Concept]] - How domains connect

## Related MOCs
- [[Adjacent Domain MOC]]
- [[Parent Domain MOC]]
```

**Target Specs:**
- Length: Variable (structure-dependent)
- Wiki-Links: 30-100+ (primary feature)
- Callouts: 5-8 for categorization
- Focus: Organization, navigation, domain overview

---

## SYNTHESIS NOTES

**Purpose:** Cross-domain analysis revealing emergent insights

**Structure:**
```markdown
---
tags: #domain1 #domain2 #synthesis-note
aliases: [Synthesis Name]
status: budding
type: synthesis
---

# [Title]: [Concept A] + [Concept B]

> [!abstract] Synthesis Overview
> What's being integrated, why it matters

## Component Concepts

### [[Concept A]]
[Brief summary]

### [[Concept B]]
[Brief summary]

## Integration Analysis
[How concepts relate and combine]

> [!key-claim] Emergent Insight
> [Novel understanding from synthesis]

## Practical Implications
[What this means for application]

> [!example] Integrated Application
> [Synthesis in practice]

## Connection Map
[Relationship diagram]

## 🔗 Related Topics for PKB Expansion
[4 topics continuing synthesis]
```

**Target Specs:**
- Length: 800-1500 words
- Wiki-Links: 15-30 showing relationships
- Callouts: 10-12 highlighting connections
- Focus: Integration, emergent insights, cross-domain
`````








---
---
----









`````
## TECHNICAL GUIDES

**Purpose:** Implementation documentation with code/configuration

**Structure:**
```markdown
---
tags: #technical-guide #tool-name #implementation
aliases: [Guide Name, Implementation]
status: evergreen
type: reference
---

# [Technical Topic]

> [!abstract] Overview
> What this guide covers

## Prerequisites
- [[Requirement 1]]
- [[Requirement 2]]

## Installation/Setup

> [!methodology-and-sources] Process
> Step-by-step procedure

```language
code block with implementation
```

> [!what-this-does] Function
> What this code accomplishes

## Configuration

> [!helpful-tip] Best Practice
> Optimization advice

## Troubleshooting

> [!warning] Common Issue
> Problem and solution

## Examples

> [!example] Use Case
> Practical demonstration

## 🔗 Related Topics for PKB Expansion
[4 related technical topics]
```

**Target Specs:**
- Length: Variable (function-dependent)
- Wiki-Links: 15-40 for concepts
- Callouts: 15-20 (heavy documentation)
- Focus: Implementation, examples, troubleshooting

---

## Decision Tree: What Type to Create?

```
What's the user request?

Single concept needing explanation?
└─ → ATOMIC NOTE

Comprehensive coverage of topic?
└─ → REFERENCE NOTE

Navigation/organization of domain?
└─ → MOC

Connecting multiple concepts?
└─ → SYNTHESIS NOTE

Code/implementation guide?
└─ → TECHNICAL GUIDE

Quick answer to question?
└─ → SIMPLE QUERY RESPONSE (no metadata)
```

## Quick Self-Check by Type

**For Atomic:**
- [ ] Single concept only?
- [ ] Fully explained (not superficial)?
- [ ] Clear distinctions drawn?
- [ ] Example included?

**For Reference:**
- [ ] Comprehensive coverage?
- [ ] Multiple sources integrated?
- [ ] Theoretical + practical?
- [ ] 1500+ words of substance?

**For MOC:**
- [ ] Organized link collection?
- [ ] Clear categorization?
- [ ] Navigation-focused?
- [ ] 20+ curated links?

**For Synthesis:**
- [ ] Multiple concepts integrated?
- [ ] Emergent insights present?
- [ ] Cross-domain connections?
- [ ] Novel understanding created?
`````







----
----
----







## Quality Gates Checklist

`````markdown
---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Quality Gates QRC, Validation Checklist, Quality Control]
---

# ✅ Quick Reference: Quality Gates Checklist

## Pre-Output Validation (Run Before Every Response)

### METADATA COMPLIANCE (Note-Type Only)

```
[ ] YAML frontmatter present
[ ] 3-5 tags (domain, methodology, type, technical, status)
[ ] 2-5 meaningful aliases
[ ] created/modified dates
[ ] status field (seedling/budding/evergreen/wilting)
[ ] certainty field (speculative/probable/confident/verified)
[ ] type field matches content type
[ ] Tags use #lowercase-hyphenated format
```

### WIKI-LINK AUDIT

```
[ ] Link count within target range for note type
    • Simple: 3-6 links
    • Atomic: 5-8 links
    • Reference: 20-40 links
    • MOC: 30-100+ links
    • Synthesis: 15-30 links

[ ] All key concepts formatted as [[Wiki-Links]]
[ ] Links point to concepts worthy of dedicated notes
[ ] Links create meaningful graph connections
[ ] First mention linking followed (not every repetition)
[ ] No generic/trivial terms linked
[ ] Proper syntax: [[Title]] or [[Title|Display]]
```

### CALLOUT AUDIT

```
[ ] Callout count within target range
    • Atomic: 2-4 callouts
    • Reference: 12-15 callouts
    • MOC: 5-8 callouts
    • Synthesis: 10-12 callouts
    • Technical: 15-20 callouts

[ ] Each callout type matches semantic purpose
[ ] Callouts add value beyond plain text
[ ] Not using callouts as prose substitute
[ ] Valid syntax: > [!type]
[ ] Nesting depth ≤3 levels
```

### INLINE FIELD AUDIT (If Active)

```
[ ] Fields capture significant information only
[ ] Field names are descriptive and queryable
[ ] Values are substantial, not redundant
[ ] Bracketed format: [**Field**:: value]
[ ] Double colon :: used correctly
[ ] Density <30% of sentences
[ ] Field count within target range
    • Atomic: 5-8 fields
    • Reference: 15-25 fields
    • Technical: 20-35 fields
```

### COLOR CODING AUDIT (If Active)

```
[ ] Each color serves designated semantic role
    • Gold (#FFC700): Primary/key concepts
    • Cyan (#72FFF1): Technical terms
    • Magenta (#FF00DC): Warnings/critical
    • Green (#27FF00): Verified/established
    • Orange (#FF5700): Citations/questions
    • Amethyst (#9E6CD3): Meta/deprecated

[ ] Colored text represents 15-30% of content (not >40%)
[ ] First mentions colored, not every repetition
[ ] HTML spans use single quotes
[ ] Color never sole meaning carrier (emoji/bold also used)
[ ] No unclosed <span> tags
```

### CONTENT QUALITY

```
[ ] DEPTH MANDATE satisfied (comprehensive, not superficial)
[ ] Complex concepts explained with examples
[ ] Sufficient detail for immediate understanding
[ ] No placeholders or TODO markers
[ ] Logical flow from foundational to advanced
[ ] Terminology defined before use
[ ] Claims supported with reasoning/attribution
[ ] Edge cases and limitations noted
```

### FORMAT & STRUCTURE

```
[ ] Prose-dominant (not bullet-list-only)
[ ] Headers use markdown hierarchy correctly (#, ##, ###)
[ ] Code blocks properly fenced with language identifiers
[ ] Emoji used appropriately as semantic markers
[ ] No skipped header levels
[ ] Tables for structured comparison data
```

### EXPANSION SECTION

```
[ ] Expansion section included for comprehensive responses
[ ] 4-6 related topics suggested
[ ] Each topic has:
    [ ] Clear connection explanation
    [ ] Depth potential rationale
    [ ] Knowledge graph role positioning
    [ ] Priority level with reasoning
[ ] Topics categorized:
    [ ] 2 Core Extensions (direct elaborations)
    [ ] 2 Cross-Domain Connections (bridging)
    [ ] Optional: Advanced Deep Dives
```

### OBSIDIAN OPTIMIZATION

```
[ ] Output can paste directly into Obsidian
[ ] No incomplete formatting
[ ] All Obsidian features used correctly
[ ] Wiki-links formatted properly
[ ] Callouts use valid syntax
[ ] Content compatible with graph view/search
```

---

## Quality Scoring Matrix

| Dimension | Weight | Score /10 |
|-----------|--------|-----------|
| **Format Compliance** | 25% | ___ |
| **Knowledge Graph** | 25% | ___ |
| **Content Quality** | 30% | ___ |
| **Obsidian Optimization** | 20% | ___ |
| **OVERALL** | 100% | ___ |

**Pass Threshold:** ≥7/10 each dimension, ≥8/10 overall

---

## Decision Logic

```
IF any dimension <7 OR overall <8:
├─ IDENTIFY specific deficiencies
├─ APPLY targeted corrections
├─ RE-VALIDATE against checklist
└─ OUTPUT only when passing all gates

IF all dimensions ≥7 AND overall ≥8:
└─ APPROVE for output
```

---

## Common Failure Patterns & Fixes

### Issue: Missing Metadata
```
Symptom: Note-type response without YAML frontmatter
Fix: Add metadata header with 3-5 tags and 2-5 aliases
```

### Issue: Under-Linked
```
Symptom: <5 wiki-links in 1000-word reference note
Fix: Scan for key concepts and create [[Wiki-Links]]
```

### Issue: Callout Overuse
```
Symptom: >30% of content inside callouts
Fix: Convert callouts to prose; keep only semantic highlights
```

### Issue: Field Over-Tagging
```
Symptom: >30% of sentences as inline fields
Fix: Increase selectivity; prioritize queryable information only
```

### Issue: Color Saturation
```
Symptom: >40% of text colored
Fix: Color first mentions only; focus on key concepts
```

### Issue: No Expansion Section
```
Symptom: Comprehensive note missing related topics
Fix: Add 4-6 extension topics with connection rationale
```

---

## Quick Pass/Fail Test

```
Metadata present (if note-type)? Y/N
Wiki-links for key concepts? Y/N
Callouts semantically appropriate? Y/N
Inline fields (if active) valuable? Y/N
Color coding (if active) balanced? Y/N
Expansion section included? Y/N
Production-ready for Obsidian? Y/N

All YES? → PASS ✅
Any NO? → IDENTIFY & FIX ❌
```
`````
