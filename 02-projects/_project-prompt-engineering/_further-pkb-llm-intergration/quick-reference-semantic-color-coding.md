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
````html
<span style='color: #HEXCODE;'>Colored text</span>
````

**Bold + color:**
````html
<span style='color: #FF00DC; font-weight: bold;'>Critical bold</span>
````

**Italic + color:**
````html
<span style='color: #72FFF1; font-style: italic;'>Technical italic</span>
````

**Strikethrough + color (deprecated):**
````html
<span style='text-decoration: line-through; color: #9E6CD3;'>Old approach</span>
````

**Background highlight:**
````html
<span style='background-color: #FFC70040;'>Highlighted text</span>
````

**Text + background:**
````html
<span style='background-color: #FFC70040; color: #FFC700;'>Maximum emphasis</span>
````

## When to Use Each Color

### 🟡 IMPERIAL GOLD (`#FFC700`)

**Apply to:**
- Core definitions introduced first time
- Central thesis or main argument
- Key terminology discussion depends upon
- "The answer is…" statements
- Terms referenced repeatedly later

**Example:**
````html
<span style='color: #FFC700;'>**Cognitive Load Theory**</span> explains how mental effort affects learning.
````

---

### 🟣 DEEP AMETHYST (`#9E6CD3`)

**Apply to:**
- Meta-commentary about structure
- Contextual framing ("Building upon…")
- Editorial notes or authorial asides
- Less critical details
- Deprecated/superseded information

**Example:**
````html
<span style='text-decoration: line-through; color: #9E6CD3;'>Old three-part framework</span> → New five-component model
````

---

### 🔵 CYBER CYAN (`#72FFF1`)

**Apply to:**
- Technical terms with precise meanings
- Code syntax, function names, APIs
- File paths, configuration parameters
- Data points, statistics, measurements
- Plugin/tool names

**Example:**
````html
Use <span style='color: #72FFF1;'>**Dataview**</span> plugin with <span style='color: #72FFF1;'>DQL</span> syntax.
````

---

### 🔴 NEON MAGENTA (`#FF00DC`)

**Apply to:**
- Warnings about common mistakes
- Critical issues needing attention
- Contradictions requiring resolution
- "Do NOT…" prohibitions
- Failure modes or edge cases

**Example:**
````html
<span style='color: #FF00DC;'>⚠️ Warning:</span> This will <span style='color: #FF00DC; font-weight: bold;'>delete all data</span>.
````

---

### 🟢 TERMINAL GREEN (`#27FF00`)

**Apply to:**
- Established principles accepted as true
- Successfully verified information
- Canonical definitions from authorities
- Completed tasks or resolved items
- Empirically validated findings

**Example:**
````html
<span style='color: #27FF00;'>✓ Verified:</span> This approach produces <span style='color: #27FF00;'>consistent results</span>.
````

---

### 🟠 REACTOR ORANGE (`#FF5700`)

**Apply to:**
- Citations and source attributions
- External resource references
- Questions requiring investigation
- Links to external documentation
- "According to [Source]…" statements

**Example:**
````html
<span style='color: #FF5700;'>According to Smith (2020)</span>, the effect is significant.
````

## Common Combination Patterns

**Definition with Source:**
````html
<span style='color: #FF5700;'>According to Sweller (1988)</span>, <span style='color: #FFC700;'>**cognitive load**</span> comprises <span style='color: #27FF00;'>intrinsic, extraneous, and germane components</span>.
````

**Technical Warning:**
````html
<span style='color: #FF00DC;'>⚠️ Critical:</span> Never use <span style='color: #72FFF1;'>`localStorage`</span> in artifacts—causes <span style='color: #FF00DC;'>silent failures</span>.
````

**Deprecated → Current:**
````html
<span style='text-decoration: line-through; color: #9E6CD3;'>Old approach</span> → <span style='color: #FFC700;'>Current best practice</span> → <span style='color: #27FF00;'>Verified solution</span>
````

**Process with Critical Step:**
````html
<span style='color: #72FFF1;'>Capture</span> → <span style='color: #72FFF1;'>Process</span> → <span style='color: #FF00DC; font-weight: bold;'>Link (CRITICAL)</span> → <span style='color: #72FFF1;'>Refine</span>
````

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
````
Squint test: Can you identify 3-5 key points by color alone?
├─ YES → Good balance
└─ NO → Adjust density

Does each color serve distinct semantic purpose?
├─ YES → Good differentiation
└─ NO → Review semantic mapping

Can section be read comfortably?
├─ YES → Acceptable density
└─ NO → Reduce color usage
````

## Accessibility Requirements

> [!important] Never Rely on Color Alone
> Always provide textual indicators:
> - Warnings: ^Warning: + **bold**
> - Verified: ^Verified: + color
> - Questions: ^Question: + color
> - Critical: ^CRITICAL: + **bold** + color

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