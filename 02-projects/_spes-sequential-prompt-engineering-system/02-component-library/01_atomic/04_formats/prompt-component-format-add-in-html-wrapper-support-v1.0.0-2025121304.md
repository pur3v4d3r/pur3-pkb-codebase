---
type: "prompt-component"
id: "20251213044814"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "claude-opus-4.1"
title: "Modular Prompt Component: Semantic HTML Color Coding System"
description: "This is a **plug-and-play prompt module** designed for integration into existing [[LLM]] prompt architectures. When activated, it instructs the model to apply semantic color coding using inline HTML `<span>` wrappers, creating visual hierarchy and categorical encoding that persists in [[Obsidian]]'s Reading Mode and exports."
key-takeaway: "Custimization Options"
last-used: "[[2025-12-13]]"
tags:
  - "year/2025"
  - "llm-capability/generation"
  - "prompt-workflow/deployment"
  - "prompt-pattern"
  - "prompt-engineering/anatomy"
aliases:
  - "Prompt-Engineering"
  - "Prompt Component"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-13|Daily Note]]"
  - "[[2025-W50|Weekly Review]]"
---

> [!in-note-metadata]
> ### Prompt Component Metadata
> 
> *Prompt-Component-ID*:: `=this.id`
> *Prompt-Component-Version*:: `=this.version`
> *Prompt-Component-Description*:: `=this.description`
> 
> > [!review] 🕰️Temporal Context
> > **Created**:: `= this.file.ctime` | **Age**:: `= (date(today) - this.file.ctime).days + " days"`
> > **Last Touch**:: `= this.file.mtime` | **Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`
> 
> > [!review] 📝Content Metrics
> > **Word Count**:: `= this.file.size` B | **Est. Read Time**:: `= round(this.file.size / 1300) + " min"`
> > **Depth Class**:: `= choice(this.file.size < 500, "🌱 Stub", choice(this.file.size < 2000, "📄 Note", "📜 Essay"))`
>
> >[!review] 🛠️ Metadata Health Check
> > **Missing Fields**:: `$= const fields = ["status", "type", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`

> [!purpose] 🔗Network Connectivity
> **In-Links**:: `= length(this.file.inlinks)` | **Out-Links**:: `= length(this.file.outlinks)`
> **Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`
> 
> > [!review] 📂Folder Context
> > **Location**:: `= this.file.folder`
> > **Neighbors**:: `$= dv.pages('"' + dv.current().file.folder + '"').length - 1` other notes here.
>```dataviewjs
>// 🧠 SYSTEM: Semantic Bridge Engine
>// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
>const current = dv.current();
>const myOutlinks = current.file.outlinks.map(l => l.path);
>
>// 1. Filter the Vault
>const siblings = dv.pages()
>    .where(p => p.file.path !== current.file.path) // Exclude self
>    .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
>    .map(p => {
>        // Find overlap between this page's links and the current page's links
>        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
>        return { 
>            link: p.file.link, 
>            sharedCount: shared.length, 
>            sharedLinks: shared 
>        };
>    })
>    .where(p => p.sharedCount > 0) // Must share at least 1 connection
>    .sort(p => p.sharedCount, "desc") // Sort by strongest connection
>    .limit(5); // Only show top 5
>
>// 2. Render the Bridge
>if (siblings.length > 0) {
>    dv.header(4, "🌉 Semantic Bridges (Missing Connections)");
>    dv.table(
>        ["Sibling Note", "Strength", "Shared Context"], 
>        siblings.map(s => [
>            s.link, 
>            "🔗 " + s.sharedCount, 
>            s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>        ])
>    );
>} else {
>    dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
>}
>```
>
>#### Related Notes
>```dataview
>TABLE rating, title, status, version, source
>FROM  ""
>WHERE  type = "prompt-component"
>SORT "maturity" DESC
>LIMIT 15
>```

[Initial Creation: [[2025-12-13|Saturday, December 13th, 2025]]]

---
> [!abstract] Module Purpose
> This is a **plug-and-play prompt module** designed for integration into existing [[LLM]] prompt architectures. When activated, it instructs the model to apply semantic color coding using inline HTML `<span>` wrappers, creating visual hierarchy and categorical encoding that persists in [[Obsidian]]'s Reading Mode and exports.

---

## 🔌 Integration Instructions

> [!methodology-and-sources] How to Use This Module
> 1. **Copy the entire `<semantic_color_system>` block** below
> 2. **Paste into your existing prompt** within your `<system_instructions>` or equivalent container
> 3. **Position after core instructions** but before output templates
> 4. **Customize color assignments** in the `<color_palette>` section if your theme differs
> 5. The module **activates contextually** when generating content with categorical or hierarchical information

---


## 🎨 Quick Reference Card

> [!helpful-tip] Copy-Paste Snippets
> Keep these templates handy for manual application:

### Text Colors (Full Saturation)
```html
<span style='color: #FFC700;'>Primary/Gold</span>
<span style='color: #9E6CD3;'>Secondary/Amethyst</span>
<span style='color: #72FFF1;'>Technical/Cyan</span>
<span style='color: #FF00DC;'>Critical/Magenta</span>
<span style='color: #27FF00;'>Definition/Green</span>
<span style='color: #FF5700;'>Reference/Orange</span>
```

### Background Highlights (40% Opacity)
```html
<span style='background-color: #FFC70040;'>Gold Highlight</span>
<span style='background-color: #9E6CD340;'>Amethyst Highlight</span>
<span style='background-color: #72FFF140;'>Cyan Highlight</span>
<span style='background-color: #FF00DC40;'>Magenta Highlight</span>
<span style='background-color: #27FF0040;'>Green Highlight</span>
<span style='background-color: #FF570040;'>Orange Highlight</span>
```

### Special Formatting
```html
<span style='text-decoration: line-through; color: #9E6CD3;'>Strikethrough</span>
<span style='color: #FF00DC; font-weight: bold;'>Bold Critical</span>
<span style='background-color: #FFC70040; color: #FFC700;'>Emphasized Key</span>
```

---

## 🔧 Customization Options

### Option A: Reduced Palette (4 Colors)

For simpler visual systems, reduce to essential categories:

```xml
<color_palette_minimal>
| Role | Color | Hex | Use |
|------|-------|-----|-----|
| Primary | Gold | `#FFC700` | Key concepts, definitions |
| Technical | Cyan | `#72FFF1` | Code, data, specifications |
| Warning | Magenta | `#FF00DC` | Errors, conflicts, warnings |
| Reference | Orange | `#FF5700` | Citations, questions, sources |
</color_palette_minimal>
```

### Option B: Theme-Matched Palette

If your Obsidian theme uses different accent colors, replace the hex codes in `<color_palette>` to match. Use a color picker on your theme's CSS variables to extract exact values.

### Option C: Accessibility Mode

For better contrast/accessibility, use these adjusted values:

```xml
<color_palette_accessible>
| Role | Adjusted Hex | Notes |
|------|--------------|-------|
| Primary | `#FFD700` | Brighter gold for dark themes |
| Secondary | `#B794F4` | Lighter purple for visibility |
| Technical | `#81E6D9` | Softer cyan, easier on eyes |
| Critical | `#FC8181` | Warmer red, less harsh |
| Definition | `#68D391` | Softer green, AA compliant |
| Reference | `#F6AD55` | Warmer orange, better contrast |
</color_palette_accessible>
```

---

## 📊 Validation Checklist

```
When reviewing LLM output for proper color coding:

- [ ] Correct HTML syntax (single quotes, proper hex format)
- [ ] Semantic appropriateness (colors match their assigned meanings)
- [ ] Density balance (not overwhelming, ~20-30% max)
- [ ] First-mention coloring (not every repetition)
- [ ] No colored headers (use markdown headers instead)
- [ ] No broken spans (all tags properly closed)
- [ ] Strikethrough used correctly (for deprecated content only)
- [ ] Highlights use muted variants (`40` suffix)

```
---

## ⚠️ Known Limitations

> [!warning] Platform Compatibility
> - **Obsidian Reading Mode**: ✅ Full support
> - **Obsidian Live Preview**: ✅ Renders correctly
> - **Obsidian Source Mode**: ⚠️ Shows raw HTML
> - **GitHub Markdown**: ❌ Strips inline styles
> - **Notion Import**: ❌ Does not preserve
> - **PDF Export**: ⚠️ Depends on export method

> [!important] Wiki-Link Coloring
> Coloring wiki-link display text (`[[Note|<span>Display</span>]]`) may not work in all Obsidian versions. Test in your vault before relying on this pattern.
# prompt-component-format-add-in-html-wrapper-support-v1.0.0-2025121304

`````prompt-component
----
Prompt-Component-ID: "2025121304"
Prompt-Component-Version: 1.0.0
----

<semantic_color_system>
## 🎨 Semantic HTML Color Coding Protocol

When generating content for [[Obsidian]] notes, Claude applies semantic color coding using inline HTML `<span>` elements to create visual hierarchy, categorical encoding, and information prioritization. This system transforms flat text into a **visually scannable knowledge artifact**.

<color_palette>
### Color Palette Specification

Claude uses this six-color semantic system, each with a **full saturation** variant for text and a **muted (40% opacity)** variant for highlights/backgrounds:

| Semantic Role | Color Name | Hex Code | Muted Hex | Visual Logic |
|---------------|------------|----------|-----------|--------------|
| **Primary** | Imperial Gold | `#FFC700` | `#FFC70040` | Key concepts, definitions, core arguments, H1-level importance |
| **Secondary** | Deep Amethyst | `#9E6CD3` | `#9E6CD340` | Structural elements, meta-notes, context, organizational markers |
| **Technical** | Cyber Cyan | `#72FFF1` | `#72FFF140` | Technical terms, syntax, data points, code references, specifications |
| **Critical** | Neon Magenta | `#FF00DC` | `#FF00DC40` | Warnings, conflicts, errors, items requiring attention, contradictions |
| **Definition** | Terminal Green | `#27FF00` | `#27FF0040` | Verified truths, established principles, completed items, axioms |
| **Reference** | Reactor Orange | `#FF5700` | `#FF570040` | External citations, bibliography, questions, sources, attributions |

</color_palette>

<syntax_specification>
### HTML Syntax Patterns

**BASIC TEXT COLORING:**
```html
<span style='color: #HEXCODE;'>Colored text content</span>
```

**STRIKETHROUGH WITH COLOR** (for deprecated/superseded content):
```html
<span style='text-decoration: line-through; color: #9E6CD3;'>Deprecated content</span>
```

**HIGHLIGHTED/BACKGROUND** (using muted colors):
```html
<span style='background-color: #FFC70040;'>Highlighted text</span>
```

**COMBINED STYLES:**
```html
<span style='color: #FF00DC; font-weight: bold;'>Critical bold text</span>
<span style='color: #72FFF1; font-style: italic;'>Technical italic term</span>
<span style='background-color: #27FF0040; color: #27FF00;'>Emphasized definition</span>
```

**SYNTAX RULES:**
- Always use **single quotes** for the style attribute value
- Hex codes must include the `#` prefix
- Multiple CSS properties separated by semicolons
- No line breaks within span tags
- Spans can wrap around markdown formatting (bold, italic) but NOT headers or block elements
- Nesting spans is permitted but should be avoided for readability

</syntax_specification>

<semantic_mapping>
### Semantic Role Assignments

Claude applies colors according to these categorical mappings:

**🟡 IMPERIAL GOLD (`#FFC700`) — Primary/Key Concepts**
Apply to:
- Core definitions being introduced for the first time
- Central thesis statements or main arguments
- Key terms that are the focus of the current section
- "The takeaway is…" type statements
- Answers to the primary question being addressed

**🟣 DEEP AMETHYST (`#9E6CD3`) — Secondary/Structural**
Apply to:
- Meta-commentary about the note structure
- Cross-references to other notes or sections
- Contextual framing ("In the context of…", "Building on…")
- Deprecated or superseded information (with strikethrough)
- Organizational markers and transitions
- "Note to self" or editorial comments

**🔵 CYBER CYAN (`#72FFF1`) — Technical/Specification**
Apply to:
- Technical terminology with precise meanings
- Code syntax, function names, variable references
- Data points, statistics, measurements
- Specifications, parameters, configurations
- File paths, commands, API references
- Mathematical notation or formulas

**🔴 NEON MAGENTA (`#FF00DC`) — Critical/Warning**
Apply to:
- Warnings about common mistakes or pitfalls
- Contradictions or conflicts requiring resolution
- Items flagged for review or verification
- Error states, failure modes, edge cases
- "Do NOT…" prohibitions
- Unresolved questions or gaps in knowledge

**🟢 TERMINAL GREEN (`#27FF00`) — Definition/Verified**
Apply to:
- Established principles accepted as true
- Axioms or foundational assumptions
- Successfully verified information
- Completed tasks or resolved items
- "This is confirmed…" type statements
- Canonical definitions from authoritative sources

**🟠 REACTOR ORANGE (`#FF5700`) — Reference/External**
Apply to:
- Citations and attributions
- External sources being quoted or paraphrased
- Questions posed for further investigation
- Links to external resources
- "According to [Source]…" statements
- Bibliography and reference list items

</semantic_mapping>

<application_heuristics>
### Application Decision Heuristics

**WHEN TO APPLY COLOR:**

✅ **ALWAYS color when:**
- Introducing a key term for the first time in a section
- Making a warning or critical note
- Citing an external source
- Marking something as deprecated/superseded
- Highlighting a verified principle or definition
- Referencing technical syntax or code

⚠️ **CONSIDER coloring when:**
- Emphasizing contrast between two concepts
- Drawing attention to a particularly important point
- Creating visual anchors for later scanning
- Distinguishing between different types of information in a list

❌ **DO NOT color:**
- Every instance of a repeated term (color first mention only)
- Entire paragraphs (color specific phrases, not blocks)
- Headers (use markdown headers, not colored spans)
- More than 20-30% of total text (preserve readability)
- Generic transitions or filler phrases
- When the meaning is already clear from context

**DENSITY GUIDELINES:**
- **Light usage** (conversational notes): 2-5 colored spans per section
- **Medium usage** (reference notes): 5-15 colored spans per section
- **Dense usage** (technical documentation): 15-30 colored spans per section
- **Maximum**: Never exceed ~30% of text being colored

**BALANCE PRINCIPLE:**
The colors should create a **rhythm** when scanning—not overwhelm. If every sentence has color, the system loses meaning. Color should draw the eye to **what matters most**.

</application_heuristics>

<combination_patterns>
### Common Combination Patterns

**Pattern 1: Definition Introduction**
```markdown
<span style='color: #FFC700;'>**Cognitive Load**</span> refers to <span style='color: #27FF00;'>the total mental effort being used in working memory during information processing</span>.
```
*Gold for the term being defined, Green for the verified definition itself.*

**Pattern 2: Deprecated → Replaced**
```markdown
<span style='text-decoration: line-through; color: #9E6CD3;'>Classical Conditioning Model</span> → <span style='color: #FFC700;'>Constructivist Learning Framework</span>
```
*Amethyst strikethrough for old, Gold for the replacement.*

**Pattern 3: Technical Warning**
```markdown
<span style='color: #FF00DC;'>⚠️ Warning:</span> The <span style='color: #72FFF1;'>`async/await`</span> pattern will fail silently if not wrapped in a try-catch block.
```
*Magenta for the warning label, Cyan for the technical term.*

**Pattern 4: Cited Principle**
```markdown
<span style='color: #FF5700;'>According to Sweller (1988)</span>, <span style='color: #27FF00;'>intrinsic load cannot be reduced—only managed through schema acquisition</span>.
```
*Orange for the citation, Green for the established principle.*

**Pattern 5: Question for Investigation**
```markdown
<span style='color: #FF5700;'>❓ Open Question:</span> Does <span style='color: #72FFF1;'>spaced repetition</span> effectiveness vary by domain complexity?
```
*Orange for the question marker, Cyan for the technical term within.*

**Pattern 6: Contrast/Distinction**
```markdown
<span style='color: #FFC700;'>Intrinsic motivation</span> emerges from within, while <span style='color: #9E6CD3;'>extrinsic motivation</span> depends on external rewards.
```
*Gold for primary concept, Amethyst for the contrasting secondary concept.*

**Pattern 7: Error State**
```markdown
<span style='color: #FF00DC;'>**FAILED:**</span> <span style='color: #72FFF1;'>npm install</span> returned exit code 1 due to peer dependency conflict.
```
*Magenta for error status, Cyan for the technical command.*

**Pattern 8: Highlighted Background Emphasis**
```markdown
The key insight is: <span style='background-color: #FFC70040; color: #FFC700;'>learning is not about storing information but about building retrieval pathways</span>.
```
*Gold text on muted gold background for maximum emphasis.*

</combination_patterns>

<integration_with_other_modules>
### Integration with Other Prompt Modules

**WITH INLINE FIELD MODULE:**
Color coding can be combined with `[**KEY**:: VALUE]` inline fields:
```markdown
[<span style='color: #FFC700;'>**Cognitive-Load**</span>:: <span style='color: #27FF00;'>the total mental effort being used in working memory</span>]
```

**WITH WIKI-LINKS:**
Apply color to the display text of wiki-links where appropriate:
```markdown
See [[Cognitive Load Theory|<span style='color: #72FFF1;'>Cognitive Load Theory</span>]] for technical details.
```
*Note: Some Obsidian versions may not render this correctly—test in your vault.*

**WITH CALLOUTS:**
Use inside callouts for additional emphasis:
```markdown
> [!warning] Critical Implementation Note
> <span style='color: #FF00DC;'>Do NOT</span> use <span style='color: #72FFF1;'>`eval()`</span> for parsing user input—this creates injection vulnerabilities.
```

</integration_with_other_modules>

<output_examples>
### Complete Output Examples

**EXAMPLE 1: Conceptual Explanation**

> <span style='color: #FFC700;'>**Self-Determination Theory**</span> posits that human motivation is driven by three innate psychological needs: <span style='color: #27FF00;'>autonomy</span> (the need to feel in control), <span style='color: #27FF00;'>competence</span> (the need to master challenges), and <span style='color: #27FF00;'>relatedness</span> (the need for social connection).
>
> <span style='color: #FF5700;'>According to Deci & Ryan (1985)</span>, when these needs are satisfied, individuals experience <span style='color: #FFC700;'>intrinsic motivation</span>—engagement driven by inherent interest rather than external rewards.
>
> <span style='color: #FF00DC;'>⚠️ Common Misconception:</span> SDT does not claim extrinsic motivation is inherently bad. Rather, it describes a <span style='color: #9E6CD3;'>continuum of internalization</span> from external regulation to integrated regulation.

**EXAMPLE 2: Technical Documentation**

> ## Configuration
>
> Set the <span style='color: #72FFF1;'>`PYTHONPATH`</span> environment variable before running the script:
>
> ```bash
> export PYTHONPATH="/path/to/ooxml:$PYTHONPATH"
> ```
>
> <span style='color: #FF00DC;'>**Critical:**</span> The <span style='color: #72FFF1;'>`--break-system-packages`</span> flag is required for pip installations in this environment.
>
> <span style='color: #27FF00;'>✓ Verified:</span> This configuration works with Python 3.10+ and Obsidian v1.4+.

**EXAMPLE 3: Comparative Analysis**

> | Approach | Status |
> |----------|--------|
> | <span style='text-decoration: line-through; color: #9E6CD3;'>Behaviorist Model</span> | Superseded |
> | <span style='color: #FFC700;'>Constructivist Model</span> | Current Standard |
> | <span style='color: #FF5700;'>Connectivist Model</span> | Under Investigation |
>
> The shift from <span style='text-decoration: line-through; color: #9E6CD3;'>behaviorism</span> to <span style='color: #FFC700;'>constructivism</span> represents a fundamental change in how we understand learning—from <span style='color: #9E6CD3;'>passive reception</span> to <span style='color: #27FF00;'>active construction of knowledge</span>.

</output_examples>

<activation_statement>
### Module Activation

This protocol is **CONTEXTUALLY ACTIVE** for note-type content generation. Claude will:

1. **Identify** categorical information that benefits from visual encoding
2. **Select** appropriate semantic colors from the palette
3. **Apply** HTML span wrappers with correct syntax
4. **Balance** density to maintain readability (~20-30% max colored)
5. **Combine** with other formatting (bold, italic, wiki-links) where appropriate

**Activation Triggers:**
- Content contains definitions, warnings, or technical terms
- User requests "color coding," "visual hierarchy," or "semantic markup"
- Output is explicitly intended for Obsidian PKB integration
- Multiple categories of information appear in same section

**Suppression Triggers:**
- User requests plain text or minimal formatting
- Output is intended for platforms that don't render HTML
- Content is conversational/informal without categorical structure

</activation_statement>
</semantic_color_system>

`````

> [!important] Version & Compatibility
> - **Module Version**: 1.0
> - **Target Models**: Claude (Sonnet/Opus), GPT-4, Gemini Pro
> - **Obsidian Compatibility**: v1.0+ (Reading Mode)
> - **HTML Rendering**: Inline styles only (no external CSS)
> - **Last Updated**: 2025-12-13