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
````markdown
> [!abstract] - Summaries & overviews
> [!definition] - Formal definitions
> [!principle-point] - Foundational principles
> [!structure] - Organizational frameworks
````

### COGNITIVE (Learning Aids)
````markdown
> [!example] - Concrete illustrations
> [!analogy] - Comparative understanding
> [!thought-experiment] - Exploratory reasoning
> [!mental-model] - Conceptual frameworks
> [!mnemonic] - Memory aids
````

### ANALYTICAL (Critical Thinking)
````markdown
> [!key-claim] - Central arguments
> [!evidence] - Supporting data
> [!counter-argument] - Alternative perspectives
> [!assumption] - Underlying premises
> [!limitation] - Boundary conditions
> [!implication] - Logical consequences
````

### PRAGMATIC (Application)
````markdown
> [!methodology-and-sources] - Process explanation
> [!what-this-does] - Functional description
> [!helpful-tip] - Practical guidance
> [!how-to] - Step-by-step instructions
> [!workflow] - Process sequences
> [!checklist] - Verification lists
````

### DIRECTIVE (Attention)
````markdown
> [!important] - Critical information
> [!warning] - Cautions & pitfalls
> [!attention] - Focus points
> [!danger] - Severe warnings
> [!caution] - Moderate warnings
````

### INFORMATIONAL (Reference)
````markdown
> [!note] - Supplementary information
> [!info] - Background information
> [!quote] - Direct citations
> [!cite] - Source attribution
````

### INTERACTIVE (Dynamic)
````markdown
> [!question] - Open questions
> [!faq] - Frequently asked questions
> [!todo] - Action items
> [!success] - Positive outcomes
> [!failure] - Failed approaches
````

## Callout Syntax Patterns

**Basic:**
````markdown
> [!type] Title
> Content line 1
> Content line 2
````

**Foldable (collapsed by default):**
````markdown
> [!type]Collapsed Title
> Hidden content
````

**Foldable (expanded by default):**
````markdown
> [!type]+ Expanded Title
> Visible content
````

**No Title:**
````markdown
> [!type]
> Content without title line
````

**Nested (max 3 levels):**
````markdown
> [!warning] Outer Warning
> Context
> > [!example] Nested Example
> > Details
> > > [!note] Deep Note
> > > Additional detail
````

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
````
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
````

## Common Patterns

**Definition + Example:**
````markdown
> [!definition] Cognitive Load
> The total mental effort being used in working memory.

> [!example] Real-World Application
> When learning to drive, managing steering + pedals + traffic rules
> simultaneously creates high cognitive load for beginners.
````

**Claim + Evidence:**
````markdown
> [!key-claim] Spaced Repetition Superiority
> Distributed practice produces better long-term retention than massing.

> [!evidence] Research Support
> Cepeda et al. (2006) meta-analysis of 317 experiments confirms
> consistent advantage of spacing (effect size d=0.40-0.60).
````

**Process + Warning:**
````markdown
> [!methodology-and-sources] Setup Process
> 1. Install Dataview plugin
> 2. Enable JavaScript queries
> 3. Create first DQL query

> [!warning] Common Pitfall
> Forgetting to enable JS queries causes DataviewJS code blocks
> to fail silently without error messages.
````

**Important + Supporting Tip:**
````markdown
> [!important] Critical Principle
> Link notes by meaning, not by topic hierarchy.

> [!helpful-tip] Implementation
> Ask "How does this connect?" not "Where does this belong?"
````

## Nesting Best Practices

✅ **Good Nesting:**
````markdown
> [!warning] Platform Compatibility
> This feature has platform-specific behaviors:
> > [!info] Windows
> > Full functionality supported
> > 
> > [!caution] Mobile
> > Limited - JavaScript execution unavailable
````

❌ **Excessive Nesting:**
````markdown
> [!note] Outer
> > [!info] Level 2
> > > [!example] Level 3
> > > > [!warning] Level 4 ← TOO DEEP
````

## Quick Self-Check
````
Does every callout serve a clear semantic purpose?
├─ YES → Good usage
└─ NO → Convert to prose or remove

Are callouts distributed evenly across sections?
├─ YES → Good balance
└─ NO → Redistribute or reduce

Can the note be read comfortably with callouts present?
├─ YES → Appropriate density
└─ NO → Reduce callout usage
````