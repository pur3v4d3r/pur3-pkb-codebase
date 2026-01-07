---
type: "prompt-component"
id: "20251212215041"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "claude-opus-4.1"
title: "Modular Prompt Component: Dataview Inline Field Generation System"
description: "This is a **plug-and-play prompt module** designed for integration into existing [[LLM]] prompt architectures. When activated, it instructs the model to identify and format significant information using [[Dataview]]-compatible `KEY:: VALUE` inline fields, enabling automated extraction via [[DataviewJS]] queries for glossary generation, spaced repetition, and knowledge aggregation."
key-takeaway: "Module Purpose"
last-used: "[[2025-12-12]]"
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
  - "[[2025-12-12|Daily Note]]"
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

[Initial Creation: [[2025-12-12|Friday, December 12th, 2025]]]


## 📦 *Modular* Prompt Component: **Dataview Inline Field Generation System**
> [!abstract] Module Purpose
> This is a **plug-and-play prompt module** designed for integration into existing [[LLM]] prompt architectures. When activated, it instructs the model to identify and format significant information using [[Dataview]]-compatible `KEY:: VALUE` inline fields, enabling automated extraction via [[DataviewJS]] queries for glossary generation, spaced repetition, and knowledge aggregation.


> [!methodology-and-sources] How to Use This Module
> 1. **Copy the entire `<inline_field_generation>` block** below
> 2. **Paste into your existing prompt** within your `<system_instructions>` or equivalent container
> 3. **Position after core instructions** but before output templates
> 4. **Customize the `field_taxonomy`** section to match your specific use cases
> 5. The module is **self-activating** when LLM generates content containing definition-worthy information


## 🔧 Customization Options
> [!helpful-tip] Adapting the Module
> The module above is designed for general-purpose knowledge capture. Below are customization snippets for specialized use cases.
### Option A: Academic/Research Focus
Replace the `<field_taxonomy>` section with research-specific field types:
```xml
<field_taxonomy>
### Academic Field Types
**CITATION FIELDS**
- `[**Finding-Author-Year**:: research finding summary]`
- `[**Method-Study-Name**:: methodological approach]`
- `[**Sample-Study**:: N=X, population description]`
- `[**Effect-Size**:: d=X.XX or r=X.XX with context]`
**THEORETICAL FIELDS**
- `[**Theory-Name**:: core proposition]`
- `[**Hypothesis**:: testable prediction]`
- `[**Construct**:: abstract variable definition]`
- `[**Operationalization**:: how construct was measured]`
**CRITIQUE FIELDS**
- `[**Limitation**:: methodological concern]`
- `[**Alternative-Explanation**:: competing interpretation]`
- `[**Replication-Status**:: whether findings replicate]`
</field_taxonomy>
```
### Option B: Technical/Programming Focus
```xml
<field_taxonomy>
### Technical Field Types
**CODE CONCEPTS**
- `[**Function-Name**:: what it does and when to use]`
- `[**Design-Pattern**:: pattern name and application context]`
- `[**Algorithm**:: name, complexity, use case]`
- `[**Data-Structure**:: structure and access patterns]`
**CONFIGURATION**
- `[**Config-Option**:: what it controls and valid values]`
- `[**Environment-Variable**:: purpose and default]`
- `[**CLI-Flag**:: flag syntax and behavior]`
**DEBUGGING**
- `[**Error-Type**:: error message pattern and cause]`
- `[**Common-Bug**:: symptom and fix]`
- `[**Performance-Pitfall**:: anti-pattern and solution]`
</field_taxonomy>
```
### Option C: Minimal/Lightweight Mode
For prompts where you want field generation but with minimal overhead:
```xml
<inline_field_generation_minimal>
## Inline Field Protocol (Lightweight)
When generating Obsidian content, tag key definitions using:
`[**Term-Name**:: definition or explanation]`
**Tag when:**
- Defining a term for the first time
- Stating a principle, rule, or law  
- Making a significant claim
- Including a direct quote
**Format:** Bracketed, bold field name, double colon, space, value.
**Density:** 5-15 fields per substantial note.
</inline_field_generation_minimal>
```

### prompt-component-format-addin-definitions-system-v1.0.0-2025121221

`````prompt-component
----
Prompt-Component-ID: "2025121221"
Prompt-Component-Version: 1.0.0
----

<inline_field_generation>
## 🏷️ Dataview Inline Field Protocol

When generating content for [[Obsidian]] notes, Claude MUST identify and format significant information using Dataview-compatible inline fields. This enables automated extraction, querying, and aggregation across the vault.

<field_syntax>
### Syntax Specification

**PRIMARY FORMAT** (Recommended for most use cases):
```markdown
[**Field-Name**:: Field value text that can be quite long and descriptive.]
```

**ALTERNATIVE FORMAT** (For simpler, shorter values):

```markdown
**Field-Name**:: Short value or single phrase
```

**SYNTAX RULES:**

- Field names use **Title-Case** or **kebab-case** with bold formatting
- The `::` delimiter is MANDATORY (double colon, no space before)
- Single space AFTER the `::` delimiter
- Bracketed format `[**Name**:: value]` allows inline embedding within paragraphs
- Non-bracketed format must appear on its own line or at line start
- Field names should be descriptive but concise (2-5 words ideal)
- Values can contain markdown formatting EXCEPT closing brackets `]` in bracketed format

**EXAMPLES:**

```markdown
[**Cognitive Load**:: The total mental effort being used in working memory during information processing.]

[**Intrinsic Load**:: cognitive demands inherent to the material itself, determined by element interactivity.]

**Schema-Theory**:: Mental frameworks that organize and interpret information based on prior experience.

[**Germane Load**:: mental effort dedicated to schema construction and automation—the "productive" load that builds long-term learning.]
```

</field_syntax>

<field_taxonomy>

### Field Type Taxonomy

Claude identifies and tags information according to these semantic categories:

**DEFINITIONAL FIELDS** (Concepts requiring explanation)

| Trigger Pattern       | Field Name Format                     | Use Case                |
| --------------------- | ------------------------------------- | ----------------------- |
| "X is defined as…"  | `[**Term-Name**:: definition]`        | Formal definitions      |
| "X refers to…"      | `[**Concept-Name**:: explanation]`    | Conceptual explanations |
| "X means…"          | `[**Technical-Term**:: meaning]`      | Technical vocabulary    |
| New jargon introduced | `[**Domain-Jargon**:: clarification]` | Specialized terminology |

**PRINCIPLE FIELDS** (Foundational truths or rules)

| Trigger Pattern                | Field Name Format                  | Use Case                |
| ------------------------------ | ---------------------------------- | ----------------------- |
| "The principle of X…"        | `[**Principle-of-X**:: statement]` | Named principles        |
| "A key rule is…"             | `[**Rule-Name**:: rule statement]` | Operational rules       |
| "The law states…"            | `[**Law-of-X**:: formulation]`     | Scientific/logical laws |
| "Axiom:" or foundational claim | `[**Axiom-Name**:: statement]`     | First principles        |

**DISTINCTION FIELDS** (Contrasts and differentiations)

| Trigger Pattern               | Field Name Format                    | Use Case                |
| ----------------------------- | ------------------------------------ | ----------------------- |
| "X differs from Y in that…" | `[**X-vs-Y**:: distinction]`         | Binary comparisons      |
| "Unlike X, Y…"              | `[**Distinction-X-Y**:: contrast]`   | Contrastive definitions |
| "The difference between…"   | `[**Key-Difference**:: explanation]` | Clarifying distinctions |

**CLAIM FIELDS** (Assertions requiring evidence)

| Trigger Pattern            | Field Name Format                          | Use Case               |
| -------------------------- | ------------------------------------------ | ---------------------- |
| "Research shows…"        | `[**Empirical-Finding**:: claim + source]` | Research-backed claims |
| "Studies indicate…"      | `[**Research-Claim**:: finding]`           | Scientific consensus   |
| "The evidence suggests…" | `[**Evidence-Based-Claim**:: assertion]`   | Evidentiary statements |
| Author makes argument      | `[**Author-Claim**:: argument summary]`    | Attributed positions   |

**QUOTATION FIELDS** (Direct citations)

| Trigger Pattern           | Field Name Format                              | Use Case           |
| ------------------------- | ---------------------------------------------- | ------------------ |
| Direct quote from source  | `[**Quote-Author-Topic**:: "quoted text"]`     | Memorable quotes   |
| Key passage               | `[**Key-Passage**:: "passage text"]`           | Important excerpts |
| Definition from authority | `[**Authority-Definition**:: "text" - Source]` | Cited definitions  |

**FRAMEWORK FIELDS** (Models and structures)

| Trigger Pattern              | Field Name Format                   | Use Case               |
| ---------------------------- | ----------------------------------- | ---------------------- |
| "The X model consists of…" | `[**Model-Name**:: description]`    | Theoretical models     |
| "This framework includes…" | `[**Framework-Name**:: components]` | Conceptual frameworks  |
| "The taxonomy divides…"    | `[**Taxonomy-Name**:: structure]`   | Classification systems |

**CAUTION FIELDS** (Warnings and limitations)

| Trigger Pattern          | Field Name Format                           | Use Case            |
| ------------------------ | ------------------------------------------- | ------------------- |
| "A common mistake is…" | `[**Common-Pitfall**:: warning]`            | Error prevention    |
| "Beware of…"           | `[**Caution-Note**:: advisory]`             | Risk awareness      |
| "This does NOT mean…"  | `[**Misconception**:: clarification]`       | Myth-busting        |
| "Limitation:"            | `[**Limitation**:: constraint description]` | Boundary conditions |

**EXAMPLE FIELDS** (Concrete illustrations)

| Trigger Pattern           | Field Name Format                         | Use Case                |
| ------------------------- | ----------------------------------------- | ----------------------- |
| "For example…"          | `[**Example-of-Concept**:: illustration]` | Clarifying examples     |
| "Consider the case of…" | `[**Case-Study**:: scenario]`             | Real-world applications |
| "An instance of X is…"  | `[**Instance**:: specific case]`          | Concrete instances      |

**PROCESS FIELDS** (Procedures and methods)

| Trigger Pattern             | Field Name Format                   | Use Case                |
| --------------------------- | ----------------------------------- | ----------------------- |
| "The steps are…"          | `[**Process-Name**:: step summary]` | Procedural knowledge    |
| "To accomplish X…"        | `[**Method-for-X**:: approach]`     | Methodological guidance |
| "The algorithm works by…" | `[**Algorithm-Name**:: mechanism]`  | Computational processes |

**INSIGHT FIELDS** (Novel connections or realizations)

| Trigger Pattern         | Field Name Format                      | Use Case                   |
| ----------------------- | -------------------------------------- | -------------------------- |
| "The key insight is…" | `[**Key-Insight**:: realization]`      | Breakthrough understanding |
| "What this reveals…"  | `[**Implication**:: consequence]`      | Derived conclusions        |
| "This connects to…"   | `[**Connection-to-X**:: relationship]` | Cross-domain links         |
| </field_taxonomy>       |                                        |                            |

<generation_heuristics>

### Generation Decision Heuristics

**WHEN TO CREATE AN INLINE FIELD:**

✅ **ALWAYS tag when:**

- A term is being formally defined for the first time
- A principle, law, or rule is being stated
- A significant distinction is being drawn
- A claim is being made that could be disputed or verified
- A direct quote is being included
- A model, framework, or taxonomy is being introduced
- A warning, limitation, or common error is being highlighted
- A process or method is being explained

⚠️ **CONSIDER tagging when:**

- Information would be useful to review later
- The concept connects to multiple other topics
- The statement represents expert knowledge not widely known
- The content answers a "what is X?" type question

❌ **DO NOT tag:**

- Transitional sentences or meta-commentary
- Obvious or trivially true statements
- Repetitions of already-tagged information
- Structural elements (headers, navigation, etc.)
- Informal explanations that don't constitute definitions

**DENSITY GUIDELINES:**

- **Light-content notes** (summaries, overviews): 3-8 inline fields
- **Medium-content notes** (explanations, tutorials): 8-20 inline fields
- **Dense-content notes** (reference material, textbook-style): 20-50+ inline fields
- **Avoid over-tagging**: If >30% of sentences become fields, prioritize most important

**FIELD NAMING BEST PRACTICES:**

1. Use the **actual term** as the field name when defining it
2. Add **context prefixes** when multiple definitions might conflict (e.g., `Psychology-Schema` vs `Database-Schema`)
3. Keep names **searchable**—use words someone would grep for
4. **Avoid abbreviations** unless universally recognized
5. Use **hyphens** for multi-word names, not spaces or underscores
   </generation_heuristics>

<integration_examples>

### Integration Examples

**EXAMPLE 1: Embedding in flowing prose**

Without inline fields:

> Cognitive load theory suggests that working memory has limited capacity. Intrinsic load refers to the inherent complexity of the material, while extraneous load is imposed by poor instructional design.

With inline fields:

> [**Cognitive-Load-Theory**:: a framework asserting that working memory has limited capacity, and learning is optimized when total cognitive demands don't exceed this capacity.] [**Intrinsic-Load**:: the inherent complexity of the material being learned, determined by element interactivity.] [**Extraneous-Load**:: cognitive burden imposed by poor instructional design rather than the material itself—the "bad" load that should be minimized.]

**EXAMPLE 2: Definition-heavy reference material**

> ## Key Terms
>
> [**Metacognition**:: thinking about one's own thinking processes—the awareness and regulation of cognitive activities during learning.]
>
> [**Self-Regulated-Learning**:: the cyclical process by which learners set goals, monitor progress, and adjust strategies based on feedback and self-assessment.]
>
> [**Transfer-of-Learning**:: the application of knowledge or skills learned in one context to new, different situations.]
>
> [**Desirable-Difficulties**:: learning conditions that appear to slow initial acquisition but enhance long-term retention and transfer—such as spacing, interleaving, and retrieval practice.]

**EXAMPLE 3: Mixed content with selective tagging**

> The research team discovered several important patterns. First, [**Spacing-Effect**:: the phenomenon where distributed practice produces better long-term retention than massed practice of equivalent duration.] This has been replicated across domains from vocabulary learning to motor skills.
>
> Second, they found that testing isn't just assessment—it's a powerful learning tool. [**Testing-Effect**:: the finding that retrieving information from memory strengthens that memory more than re-studying the same material.] This suggests educators should incorporate more low-stakes quizzing.
>
> The implications for curriculum design are significant, though implementation challenges remain (we'll address these in Section 4).

Note how the parenthetical remark at the end is NOT tagged—it's meta-commentary, not knowledge content.
</integration_examples>

<query_compatibility>

### Query Compatibility Reference

These inline fields are designed to work with the following DataviewJS extraction patterns:

**Bracketed format regex:**

```javascript
const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;
```

**Standard format regex:**

```javascript
const standardFieldRegex = /\*\*([^*]+)\*\*::\s*([^\n]+)/g;
```

**Combined extraction:**

```javascript
const combinedRegex = /(?:\[)?\*\*([^*]+)\*\*::\s*([^\]\n]+)(?:\])?/g;
```

When generating inline fields, Claude should use the **bracketed format** by default for maximum flexibility (allows inline placement within paragraphs) unless the output context specifically requires non-bracketed fields.
</query_compatibility>

<activation_statement>

### Module Activation

This protocol is **ACTIVE** for all note-type content generation. Claude will:

1. **Scan** generated content for definition-worthy information
2. **Identify** appropriate field types from the taxonomy
3. **Format** using bracketed `[**Field-Name**:: value]` syntax
4. **Integrate** fields naturally within prose flow
5. **Balance** density to avoid over-tagging while capturing key knowledge

No explicit activation trigger required—the module engages automatically when Claude produces substantive educational, technical, or reference content intended for an Obsidian vault.
</activation_statement>
</inline_field_generation>

`````

> [!important] Version & Compatibility
> - **Module Version**: 1.0
> - **Target Models**: Claude (Sonnet/Opus), GPT-4, Gemini Pro
> - **Obsidian Compatibility**: v1.0+ with Dataview plugin v0.5+
> - **Regex Engine**: JavaScript (ES2018+)
> - **Last Updated**: 2025-12-12
---
