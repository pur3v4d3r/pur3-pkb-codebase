---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Metadata QRC, YAML Frontmatter Guide, Tag Generation Quick Ref]
---

# 📋 Quick Reference: Metadata Generation

## YAML Frontmatter Template
````yaml
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
````

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
````yaml
status: seedling   # Initial capture, rough notes, incomplete
status: budding    # Structure emerging, connections forming
status: evergreen  # Mature, well-developed, high-confidence
status: wilting    # Outdated, superseded, needs revision
````

## Certainty Field Values
````yaml
certainty: speculative  # Hypothesis, unverified, exploratory
certainty: probable     # Some supporting evidence
certainty: confident    # Well-supported, multiple sources
certainty: verified     # Empirically validated, authoritative
````

## Decision Tree: To Metadata or Not?
````
IS this a permanent note?
├─ Reference Note? → YES - Full metadata required
├─ Atomic Note? → YES - Full metadata required
├─ MOC? → YES - Full metadata required
├─ Synthesis Note? → YES - Full metadata required
├─ Simple query response? → NO - Skip metadata
├─ Conversational answer? → NO - Skip metadata
└─ Temporary/scratch note? → NO - Skip metadata
````

## Quick Examples

**For "Chain-of-Thought Prompting Techniques":**
````yaml
---
tags: #prompt-engineering #cognitive-frameworks #reference-note #llm-optimization
aliases: [CoT Prompting, Chain of Thought, Reasoning Chain Techniques]
status: evergreen
certainty: confident
type: reference
---
````

**For "Intrinsic Cognitive Load":**
````yaml
---
tags: #cognitive-science #cognitive-load-theory #atomic-note
aliases: [Intrinsic Load, Element Interactivity, Inherent Complexity]
status: evergreen
certainty: verified
type: atomic
---
````

**For "Obsidian Automation MOC":**
````yaml
---
tags: #obsidian #pkm #moc #automation
aliases: [Automation Hub, Workflow Index, Plugin Synergies Map]
status: budding
type: moc
---
````