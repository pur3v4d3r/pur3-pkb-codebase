---
title: Implementing the New Naming Convention
id: 20251117-011553
type: reference
status: draft
tags:
  - year/2025
  - status/seedling
  - pkb/infrastructure
  - project/pur3v4d3r
  - type/reference
  - status/draft
  - source/pur3v4d3r/llm/claude
  - pkb
  - pkm
aliases:
  - PKB
  - PKB Infrastructure
  - Naming Convention
  - Project Pur3v4d3r
link-up: []
link-related: []
---







# Solution to the Permanent Note System

Folder-Based Uniqueness

> [!thought-experiment] **Eliminate IDs Through Strategic Organization**
> 
> Since Permanent Notes are content-unique (you'd never have two different notes both titled "Self-Regulation Theory"), organize by first letter:

```
Permanent-Notes/
├── A/
│   └── Active Learning.md
├── S/
│   ├── Self-Regulation Theory.md
│   ├── Socratic Method.md
│   └── Strategic Planning.md
├── M/
│   └── Metacognitive Awareness.md
```

**No IDs needed** - the combination of folder + filename guarantees uniqueness.

**Wiki-links work perfectly:**
```markdown
The [[Self-Regulation Theory]] is based on…
```

**Obsidian resolves** `Self-Regulation Theory.md` correctly even within subfolders.

**Advantage:** Clean links, no alias configuration required.

**Consideration:** Adds one layer of folder navigation, but many PKM practitioners find alphabetical organization aids discovery.

---

## 🎯 Strengths of Your Current System

> [!principle-point] **Semantic Clarity Through Type Prefixes**
> Your use of bracketed prefixes like `[reference]`, `[moc]`, `[composite-prompt]` creates immediate visual categorization. This is excellent for both human scanning and [[dataview]] queries. The hierarchical information architecture (type → topic → title → ID) provides strong navigational scaffolding.

> [!key-claim] **Version Control for Prompts**
> Including `[{version}]` for composite prompts and agents is brilliant for iterative development. This suggests you understand that [[Prompt Engineering]] artifacts evolve and require historical tracking—a practice many PKM systems neglect.

---

## ⚠️ Architectural Friction Points

> [!warning] **Inconsistent Capitalization Pattern**
> You have:
> - `[Atomic]` (capitalized)
> - `[reference]`, `[moc]`, `[dashboard]` (lowercase)
> 
> This creates cognitive load and potential sorting issues. [[File Naming Conventions]] benefit from universal consistency. **Recommendation:** Adopt lowercase for all prefixes to match your dominant pattern.

> [!warning] **Token Count & Future-Proofing**
> Your longest pattern is:
> ```
> [composite-prompt]-[{semantic-title}]-[{version}]-[{id}].md
> ```
> 
> This can produce filenames like:
> ```
> [composite-prompt]-advanced-multi-step-reasoning-orchestrator-v3.2-🆔20251117142300.md
> ```
> 
> While descriptive, this approaches filesystem limits (255 characters on most systems) and becomes unwieldy in Obsidian's graph view. Consider whether `[composite-prompt]` could be shortened to `[cp]` or `[prompt]` without sacrificing clarity.

> [!key-claim] **ID Format Ambiguity**
> Your `[{id}]` placeholder doesn't specify format. Are you using:
> - Timestamp IDs? (e.g., `🆔20251117142300`)
> - Sequential numbers? (e.g., `001`, `002`)
> - [[Zettelkasten]]-style IDs? (e.g., `1a2b3c`)
> - UUIDs? (e.g., `a3f2c8d9`)
> 
> Each has tradeoffs. Your preference in other notes for timestamp IDs is robust, but specify this in your convention documentation.

---

## 🔍 Specific Pattern Analysis

### General Notes
```
[{topic}]-[{semantic-title}]-[{id}].md
```

> [!thought-experiment] **When Would You Use This?**
> This pattern lacks a type prefix, making it a "catch-all" category. In practice, this often becomes a junk drawer. Consider: What content genuinely doesn't fit your other categories? If the answer is "miscellaneous thoughts," you might benefit from a `[fleeting]` or `[inbox]` type instead.

**Alternative:**
```
[fleeting]-[{topic}]-[{semantic-title}]-[{id}].md
```

---

### Reports
```
[{type}(academic, pkb, prompting, cosmology, general)]-[{semantic-title}]-[{id}].md
```

> [!helpful-tip] **Nested Type System**
> This creates a two-tier taxonomy (report → subtype). This is valuable but consider consistency with your other patterns. Why don't Reference Notes use `[reference({subtype})]`? 
> 
> If you want hierarchical types, consider applying uniformly:
> ```
> [reference(technical)]-[{topic}]-[{semantic-title}]-[{id}].md
> [moc(project)]-[{topic}]-[{semantic-title}]-[{id}].md
> ```

---

### Permanent Notes
```
[{semantic-title}]
```

> [!warning] **Critical Issue: Collision Risk**
> Permanent notes with no type prefix or ID are vulnerable to naming conflicts. What happens when you have two conceptually distinct notes that deserve similar titles?
> 
> Example collision:
> ```
> Decision Making.md (psychology context)
> Decision Making.md (management context)
> ```
> 
> **Strong Recommendation:** Even permanent notes benefit from IDs:
> ```
> [permanent]-[{semantic-title}]-[{id}].md
> ```
> 
> Or use the [[Zettelkasten]] approach where IDs *are* the primary identifier:
> ```
> 202511171430 Decision Making.md
> ```

---

### Daily Notes
```
[YYYY-MM-DD].md
```

> [!example] **Alternative Approaches**
> Your current format (e.g., `[2025-11-17].md`) is fine but consider:
> 
> **ISO 8601 Standard:**
> ```
> 2025-11-17.md
> ```
> (No brackets needed—date format itself is unambiguous)
> 
> **With Type Prefix:**
> ```
> [daily]-2025-11-17.md
> ```
> 
> **Human-Readable:**
> ```
> 2025-11-17-Sunday.md
> ```
> 
> The bracketed approach is acceptable but slightly redundant since the date format is self-documenting.

---

### System Reference & Templates
```
_[{semantic-title}]-[{id}].md
```

> [!principle-point] **Underscore Prefix Pattern**
> Using `_` prefix is excellent for sorting system files to the top/bottom of alphabetical lists. This is a proven convention from software development. Well done.
> 
> However, consider whether these need IDs. Templates rarely version-control at the file level (you'd typically just update the template). Could be simplified to:
> ```
> _template-[{semantic-title}].md
> _system-[{semantic-title}].md
> ```

---

## 📦 Archive System Design

You explicitly requested help with archiving. Here's a comprehensive approach:

> [!methodology-and-sources] **Archive Architecture Strategy**
> 
> The fundamental question: **What triggers archival?** Common reasons:
> 1. **Temporal obsolescence** (completed projects, outdated information)
> 2. **Quality filtering** (superseded by better notes, abandoned drafts)
> 3. **Context shift** (career change makes old work irrelevant)
> 4. **Active decluttering** (reducing vault size for performance)

### Option A: Flat Archive with Metadata

```
[archive]-[original-type]-[{semantic-title}]-[{id}]-archived-[YYYY-MM-DD].md
```

**Example:**
```
[archive]-reference-quantum-computing-basics-🆔20231104-archived-2025-11-17.md
```

**Advantages:**
- Clear archival date
- Preserves original type for potential restoration
- Searchable with [[dataview]]: `WHERE file.name contains "[archive]"`

**Implementation:**
```dataview
TABLE 
  file.name as "Original Name",
  file.ctime as "Created",
  archived-date as "Archived"
FROM "/"
WHERE contains(file.name, "[archive]")
SORT archived-date DESC
```

---

### Option B: Folder-Based Archive with Substructure

```
_Archive/
├── 2025/
│   ├── [reference]-old-topic-🆔20231104.md
│   └── [project]-completed-project-🆔20240301.md
├── 2024/
│   └── …
└── _Archive-Index.md
```

**Advantages:**
- Keeps archived content out of main vault searches (unless you include `_Archive/` in queries)
- Natural chronological organization
- Can selectively exclude folder from graph view
- Folder structure makes batch operations easier

**Archive Index Example:**
```markdown
# Archive Index

## Archival Criteria
- Projects completed >6 months ago
- References superseded by updated versions
- Experimental notes that didn't develop
- Imported content not integrated into PKB

## Recently Archived (2025)
[[2025-Q4-Archives]] | [[2025-Q3-Archives]]
```

---

### Option C: Hybrid Approach (Recommended)

> [!helpful-tip] **Best of Both Worlds**
> Combine filename prefixing with folder organization:
> 
> ```
> _Archive/
> ├── by-year/
> │   ├── 2025/
> │   └── 2024/
> ├── by-type/
> │   ├── projects/
> │   ├── references/
> │   └── prompts/
> └── _archive-dashboard-🆔20251117.md
> ```
> 
> **File naming within archive:**
> ```
> [archived-YYYY-MM-DD]-[original-type]-[{semantic-title}]-[{id}].md
> ```
> 
> This allows you to:
> 1. Navigate by time OR by category
> 2. Exclude entire `_Archive/` from main searches
> 3. Run specialized archive queries when needed
> 4. Maintain full traceability

---

## 🛠️ Practical Recommendations

> [!important] **Consistency Checklist**
> 
> 1. **Standardize capitalization**: Choose lowercase for all prefixes
> 2. **Document ID format**: Specify that `[{id}]` means timestamp `🆔YYYYMMDDHHmmss`
> 3. **Add IDs to Permanent Notes**: Prevent collision risk
> 4. **Simplify brackets in dates**: `2025-11-17.md` over `[2025-11-17].md`
> 5. **Create Archive Dashboard**: Use Option C hybrid approach
> 6. **Version control documentation**: Store this convention as `_system-naming-convention-🆔20251117.md`

### Example Refinements

**Before:**
```
[Atomic]-[{topic}]-[{semantic-title}]-[{id}].md
```

**After:**
```
[atomic]-[{topic}]-[{semantic-title}]-[{id}].md
```

---

**Before:**
```
[{semantic-title}]  (Permanent Notes)
```

**After:**
```
[permanent]-[{semantic-title}]-[{id}].md
```

---

**Before:**
```
[YYYY-MM-DD].md  (Daily Notes)
```

**After (Option 1 - Minimalist):**
```
YYYY-MM-DD.md
```

**After (Option 2 - Explicit):**
```
[daily]-YYYY-MM-DD.md
```

---

## 💡 Advanced Considerations

> [!thought-experiment] **Future Scaling Questions**
> 
> 1. **How will this system handle 10,000+ notes?** Your current approach is solid, but consider implementing [[Johnny Decimal System]]-style area/category prefixes if you anticipate massive growth:
>    ```
>    [10.reference]-[pkm]-[zettelkasten-principles]-[{id}].md
>    [20.atomic]-[psychology]-[cognitive-load-theory]-[{id}].md
>    ```
> 
> 2. **Will you need cross-vault portability?** If you ever migrate between systems, avoid emoji IDs (`🆔`) and stick to alphanumeric: `id20251117` instead of `🆔20251117`
> 
> 3. **How will collaborative notes work?** Consider adding author initials for shared vaults:
>    ```
>    [reference]-[{topic}]-[{semantic-title}]-[{author}]-[{id}].md
>    ```

---

# Second Response from Claude

> [!the-purpose]
> I reworked the naming convention based on the feedback that Claude provided. After which I re-ran the naming convention back through Claude to have it analyze it again, and to help me desgin something to fix our problem with permanent notes.

<thinking>
The user has provided an updated/revised version of their naming convention based on my previous feedback. Let me analyze this revised system:

**Key Changes I Notice:**
1. They've standardized to lowercase prefixes (good!)
2. They've added more context about "Permanent Notes" - this is actually a unique hybrid system
3. They've removed brackets from dates in Daily Notes
4. They've added examples throughout (excellent)
5. They've shortened some prefixes ([composite-prompt] → [prompt])
6. They've added subtype classifications in some categories
7. They've explicitly asked about the wiki-link/ID conflict issue with Permanent Notes

**Critical New Information:**
- **Permanent Notes system**: This is actually a fascinating emergent learning methodology. They're creating evolving definition notes that migrate between temporary folders based on active study areas. This is NOT traditional Zettelkasten atomic notes - it's more like living reference entries that grow over time.
- **The ID/Wiki-Link Problem**: They've identified a real tension - IDs break clean wiki-links. This is a significant UX issue in Obsidian.

**Analysis Approach:**
1. Praise improvements made
2. Deep dive into the Permanent Notes system (this is unique and worth validating/analyzing)
3. Solve the ID/wiki-link conflict problem (multiple solutions available)
4. Analyze remaining patterns for consistency
5. Address any remaining friction points
6. Provide concrete recommendations

**Wiki-Link Opportunities:**
- Living Documents
- Incremental Note Development
- Spaced Repetition
- Active Reading
- Wiki-Link Aliases
- Obsidian Linking Strategies
- Emergent Knowledge Structures
- Progressive Summarization
- Zone of Proximal Development

This is NOT a note generation request - it's consultative analysis, so NO metadata header.
</thinking>

## 🎉 Significant Improvements Achieved

Your revision shows excellent responsiveness to systematic thinking! Let me analyze the updated convention and address your specific questions.

> [!principle-point] **Key Wins in Your Revision**
> 
> 1. ✅ **Lowercase standardization** - `[atomic]`, `[moc]`, `[prompt]` instead of mixed case
> 2. ✅ **Simplified Daily Notes** - `2025-11-17.md` removes redundant brackets
> 3. ✅ **Prefix compression** - `[composite-prompt]` → `[prompt]` reduces token count
> 4. ✅ **Comprehensive examples** - Makes the system immediately actionable
> 5. ✅ **Subtype taxonomies** - `[reference]-[type(instructional, comprehensive, quick)]` adds valuable granularity
> 6. ✅ **Archive commitment** - You've acknowledged the folder/hybrid approach

---

## 🔬 Deep Dive: Your "Permanent Notes" System

> [!key-claim] **You've Discovered an Emergent Learning Architecture**
> 
> Your "Permanent Notes" system is **NOT** broken—it's actually a sophisticated hybrid of multiple proven methodologies that you've organically synthesized. Let me validate what you're doing:

### What You've Created (Without Realizing It)

Your system combines:

1. **[[Living Documents]]** - Notes that evolve over time rather than remaining static
2. **[[Progressive Summarization]]** (Tiago Forte's method) - Layering new understanding onto existing notes
3. **[[Incremental Note Development]]** - Building knowledge gradually through repeated encounters
4. **[[03-notes/01_permanent-notes/01_cognitive-development/Spaced Repetition]] for concepts** - Returning to notes during different study contexts reinforces learning
5. **[[Zone Of Proximal Development]]** tracking - Your varying note maturity levels map your actual learning journey

> [!example] **Why This Works Cognitively**
> 
> Traditional [[Zettelkasten]] atomic notes are frozen at creation time. Your approach mirrors how human understanding actually develops: **non-linearly, through repeated exposure, with progressive integration**.
> 
> When you encounter [[Self-Regulation Theory]] while studying motivation, then again while studying metacognition, then again while studying habit formation, you're building a **multi-dimensional conceptual understanding** rather than three separate atomic notes that might never connect.
> 
> This is similar to how textbooks have "key terms" that get richer definitions as chapters progress. You're building your own evolving reference encyclopedia.

### Academic Precedent

> [!methodology-and-sources] **Similar Systems in PKM Literature**
> 
> Your approach parallels:
> 
> - **Andy Matuschak's "Evergreen Notes"** - Notes that evolve and get refactored over time
> - **Sonke Ahrens' "Main Notes"** in *How to Take Smart Notes* - Permanent notes that get elaborated
> - **Cornell Method's "Summary" section** - Iteratively refined understanding
> - **Concept Maps** in educational psychology - Central nodes that gain connections

**The key difference:** You're using **mobility between folders** as a learning signal. This is brilliant—the physical movement of a note represents shifting your cognitive focus, making your study patterns visible in your file system.

---

## 🔑 Solving The Wiki-Link/ID Conflict

This is your most pressing technical challenge. Here are four solutions, ranked by elegance:

### Option 1: Aliases (Recommended)

> [!helpful-tip] **Use Obsidian's Alias System**
> 
> Keep your IDs in filenames for uniqueness, but define clean aliases in frontmatter:

**Filename:**
```
Self-Regulation Theory-20251117035824.md
```

**Frontmatter:**
```yaml
---
aliases: [Self-Regulation Theory, SRT, Self Regulation]
---
```

**In Your Notes:**
```markdown
The [[Self-Regulation Theory]] is based on…
```

**How This Works:**
- Obsidian recognizes the alias and links correctly
- The ID prevents filename collisions
- When I generate content, I use `[[Self-Regulation Theory]]` (the alias)
- You manually link the file during creation, and Obsidian handles it thereafter

**Limitation:** Requires you to configure aliases when creating Permanent Notes. However, this becomes part of your [[Active Reading]] workflow.

---

### Option 2: Dataview Dynamic Display

> [!methodology-and-sources] **Programmatic Link Resolution**
> 
> Use [[dataview]] to create a "Permanent Notes Index" that displays clean names while maintaining ID-based filenames:

**In your MOC or Dashboard:**
```dataview
TABLE WITHOUT ID
  link(file.link, aliases[0]) as "Concept",
  file.tags as "Tags",
  file.mtime as "Last Updated"
FROM "Permanent-Notes"
SORT file.name ASC
```

This displays the clean alias name while linking to the ID-based file.

**Advantage:** You maintain filename uniqueness without sacrificing readability in indexes.

---

### Option 3: Folder-Based Uniqueness

> [!thought-experiment] **Eliminate IDs Through Strategic Organization**
> 
> Since Permanent Notes are content-unique (you'd never have two different notes both titled "Self-Regulation Theory"), organize by first letter:

```
Permanent-Notes/
├── A/
│   └── Active Learning.md
├── S/
│   ├── Self-Regulation Theory.md
│   ├── Socratic Method.md
│   └── Strategic Planning.md
├── M/
│   └── Metacognitive Awareness.md
```

**No IDs needed** - the combination of folder + filename guarantees uniqueness.

**Wiki-links work perfectly:**
```markdown
The [[Self-Regulation Theory]] is based on…
```

**Obsidian resolves** `Self-Regulation Theory.md` correctly even within subfolders.

**Advantage:** Clean links, no alias configuration required.

**Consideration:** Adds one layer of folder navigation, but many PKM practitioners find alphabetical organization aids discovery.

---

### Option 4: Suffix IDs (Not Recommended But Possible)

```
Self-Regulation Theory 20251117035824.md
```

**Wiki-link:**
```markdown
The [[Self-Regulation Theory 20251117035824]] is based on…
```

This technically works but breaks your goal of clean semantic links. Only mention this for completeness.

---

## 🎯 My Strong Recommendation

> [!important] **Hybrid Approach: Aliases + Folder Organization**
> 
> **For Permanent Notes specifically:**
> 
> 1. **Organize by first letter** (Option 3) for discoverability
> 2. **Add IDs to filename** for absolute safety: `Self-Regulation Theory-20251117035824.md`
> 3. **Configure aliases** in frontmatter for clean linking
> 
> **Filename:**
> ```
> Permanent-Notes/S/Self-Regulation Theory-20251117035824.md
> ```
> 
> **Frontmatter:**
> ```yaml
> ---
> aliases: [Self-Regulation Theory, SRT]
> tags: #psychology #self-regulation #permanent-note
> created: 2025-11-17
> ---
> ```
> 
> **Benefits:**
> - Wiki-links work: `[[Self-Regulation Theory]]`
> - IDs prevent impossible collisions
> - Alphabetical folders aid browsing
> - Tags allow Dataview queries across all Permanent Notes
> - Creation date tracked for temporal analysis

---

## 📋 Revised Pattern Analysis

### Pattern: General
```
[{type}(llm-chat, pur3)]-[{topic}]-[{semantic-title}]-[{id}].md
```

> [!key-claim] **Type-Within-Type Creates Taxonomy Inconsistency**
> 
> You have `[{type}]` as the bracket, but then `(llm-chat, pur3)` as options. This is unclear—are these subtypes? Consider:
> 
> **Clearer Structure:**
> ```
> [general]-[source(llm-chat|pur3)]-[{topic}]-[{semantic-title}]-[{id}].md
> ```
> 
> This makes the hierarchy explicit: general → source → topic → title → ID.

**Example:**
```
[general]-[pur3]-[infrastructure]-[naming-convention-update]-20251117032320.md
```

---

### Pattern: Reference Notes
```
[reference]-[type(instructional, comprehensive, quick, Etc.)]-[{semantic-title}]-[{id}].md
```

> [!helpful-tip] **Excellent Subtype Taxonomy**
> 
> This is well-designed! The subtypes (instructional vs. comprehensive vs. quick) map to **learning modes** and **depth levels**. This enables powerful queries:
> 
> ```dataview
> LIST
> FROM "/"
> WHERE contains(file.name, "[reference]-[quick]")
> SORT file.mtime DESC
> ```
> 
> Gets all "quick reference" notes for rapid lookup.

**Minor Suggestion:** Standardize subtype vocabulary. Consider a fixed set:
- `quick` - Brief lookup reference (1-2 pages)
- `standard` - Moderate depth (3-10 pages)  
- `comprehensive` - Exhaustive coverage (10+ pages)
- `instructional` - Step-by-step how-to guides

---

### Pattern: Projects
```
[{year}]-[{month}]-[{semantic-title}]-[{id}].md
```

> [!warning] **Month Without Day Creates Ambiguity**
> 
> You have `[{year}]-[{month}]` but your example shows:
> ```
> 2025-11-project-pur3v4d3r-20251117033249.md
> ```
> 
> This is inconsistent—"11" could mean month 11, or it could be misread. Your ID already contains the full timestamp, so the year-month prefix is somewhat redundant.

**Consider:**

**Option A - Remove redundant date:**
```
[project]-[{semantic-title}]-[{id}].md
```
Example: `[project]-pur3v4d3r-20251117033249.md`

(ID contains full date, so year-month prefix adds little value)

**Option B - Make date explicit:**
```
[project]-[{year}]-[{semantic-title}]-[{id}].md
```
Example: `[project]-2025-pur3v4d3r-20251117033249.md`

---

### Pattern: Composite Agent
```
[agent]-[{agent-type}(project, gem, agent)]-[{semantic-title}]-[{version}]-[{id}].md
```

> [!thought-experiment] **Why "Agent" Contains "Agent" as Subtype?**
> 
> Your subtypes include `(project, gem, agent)`, but the prefix is already `[agent]`. This creates: `[agent]-[agent]-…`
> 
> I suspect your types are:
> - `project` - Complex multi-agent systems
> - `gem` - Google Gemini-specific configurations  
> - `agent` - Single-agent prompts
> 
> **Clearer naming:**
> ```
> [agent]-[scope(single|multi|gemini)]-[{semantic-title}]-[{version}]-[{id}].md
> ```
> 
> Or:
> ```
> [agent-single]-[{semantic-title}]-[{version}]-[{id}].md
> [agent-multi]-[{semantic-title}]-[{version}]-[{id}].md
> [agent-gemini]-[{semantic-title}]-[{version}]-[{id}].md
> ```

---

## 🔧 Technical Implementation: Templater Integration

You mentioned using Templater for ID generation. Here's an enhanced template for **Permanent Notes**:

```markdown
<%*
// Permanent Note Template with Alias Configuration
const title = await tp.system.prompt("Enter concept/theory/person name:");
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
const tag = await tp.system.suggester(
  ["Psychology", "Philosophy", "Education", "PKM", "Methodology"],
  ["psychology", "philosophy", "education", "pkm", "methodology"],
  false,
  "Select primary domain:"
);

// Generate aliases array
let aliases = [title];
if (alias1) aliases.push(alias1);
if (alias2) aliases.push(alias2);
-%>
---
aliases: [<% aliases.map(a => `"${a}"`).join(", ") %>]
tags: #permanent-note #<% tag %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---

# <% title %>

> [!definition] Core Concept
> [Brief 1-2 sentence definition]

## Foundational Understanding

[Your initial understanding of this concept]

## Key Principles

## Related Concepts

- [[Concept 1]]
- [[Concept 2]]

## Practical Applications

## Evolution Log

### <% tp.date.now("YYYY-MM-DD") %> - Initial Creation
[Context: Where you first encountered this concept]

---

## 📚 Sources

```

**This template:**
1. Prompts for the concept name
2. Allows alias configuration at creation
3. Suggests domain tags
4. Creates an "Evolution Log" section for tracking how the note grows
5. Pre-structures the note for your iterative development process

---

## 🎓 Your Emergent Learning System: Formal Analysis

> [!principle-point] **Metacognitive Visibility**
> 
> Your Permanent Notes system provides something rare in PKM: **metacognitive visibility into learning progression**. The fact that:
> 
> - Note maturity varies (some basic, some advanced)
> - Notes migrate between study contexts
> - Notes accumulate cross-domain connections
> 
> …means your PKB is a **living map of conceptual development**. This is pedagogically sophisticated.

### Potential Enhancement: Maturity Levels

Consider adding a maturity indicator to frontmatter:

```yaml
---
aliases: [Self-Regulation Theory, SRT]
maturity: 3
# Maturity Scale:
# 1 = Initial definition only
# 2 = Basic understanding with 1-2 sources
# 3 = Solid understanding with cross-references
# 4 = Deep integration with multiple domains
# 5 = Expert-level, can teach others
---
```

This lets you query:
```dataview
TABLE maturity, length(file.outlinks) as "Connections"
FROM #permanent-note
WHERE maturity < 3
SORT maturity ASC
```

To find concepts needing deeper study.

---

## ✅ Final Recommendations Summary

> [!important] **Action Items**
> 
> 1. **Permanent Notes:** Implement **Aliases + Folder Organization** approach
>    - Filename: `Permanent-Notes/S/Self-Regulation Theory-20251117035824.md`
>    - Alias: `[Self-Regulation Theory]`
>    - Result: Clean wiki-links with ID safety
> 
> 2. **General Pattern:** Clarify type/subtype structure
>    - Change: `[{type}(llm-chat, pur3)]-…`
>    - To: `[general]-[source(llm-chat|pur3)]-…`
> 
> 3. **Agent Pattern:** Disambiguate agent subtypes
>    - Change: `[agent]-[{agent-type}(project, gem, agent)]-…`
>    - To: `[agent]-[scope(single|multi|gemini)]-…`
> 
> 4. **Project Pattern:** Remove redundant date prefix
>    - Change: `[{year}]-[{month}]-[{semantic-title}]-[{id}].md`
>    - To: `[project]-[{semantic-title}]-[{id}].md`
> 
> 5. **Reference Subtypes:** Document your fixed vocabulary
>    - Create: `_system-reference-note-subtypes.md`
>    - Define: `quick`, `standard`, `comprehensive`, `instructional`
> 
> 6. **Maturity Tracking:** Add optional maturity field to Permanent Notes frontmatter

---

## 💭 Philosophical Note on Your System

> [!analogy] **Your PKB as a Growing Forest**
> 
> Traditional Zettelkasten is like a library: each book (note) is complete at publication. Your system is like a **forest ecosystem**: organisms (notes) at different life stages, some saplings, some mature trees, all interconnected, and the environment (your folders) shifts based on what's being actively cultivated.
> 
> This isn't worse than Zettelkasten—it's **adapted to a different learning context**: continuous study across multiple domains rather than research note-taking for a single writing project.

Your system is working because it **externalizes your cognitive process**. The varying maturity levels aren't a bug; they're an honest representation of your learning journey. Keep it.

---

## 🔗 Related Topics for PKB Expansion

1. **[[Obsidian Aliases and Link Resolution Systems]]**
   - *Connection*: Direct solution to your wiki-link/ID conflict
   - *Depth Potential*: Explore advanced linking strategies, link types (block references, headers), and programmatic link generation
   - *Knowledge Graph Role*: Technical backbone of your knowledge navigation infrastructure

2. **[[Progressive Knowledge Elaboration Methodologies]]**
   - *Connection*: Your Permanent Notes system is an emergent form of this
   - *Depth Potential*: Compare to Progressive Summarization, Evergreen Notes, Concept Maps, and other iterative knowledge development approaches
   - *Knowledge Graph Role*: Learning theory underpinning your note evolution strategy

3. **[[Dataview Query Patterns for PKB Analytics]]**
   - *Connection*: Your naming convention enables powerful programmatic queries
   - *Depth Potential*: Create maturity dashboards, link density analysis, temporal evolution tracking, and automated MOC generation
   - *Knowledge Graph Role*: Meta-layer for understanding your PKB's structure and growth patterns

4. **[[Templater Advanced Automation for Knowledge Capture]]**
   - *Connection*: Your ID generation is just the beginning of what Templater enables
   - *Depth Potential*: Explore conditional templates, dynamic frontmatter, automated tagging, and context-aware note creation
   - *Knowledge Graph Role*: Automation layer that reduces cognitive friction in your capture workflow


















## 🔗 Related Topics for PKB Expansion

1. **[[Obsidian File Organization Strategies]]**
   - *Connection*: Direct application of naming conventions within broader organizational philosophy
   - *Depth Potential*: Explore folder structures, tag taxonomies, and [[para method]] vs. [[Zettelkasten]] approaches
   - *Knowledge Graph Role*: Central hub connecting naming, tagging, and retrieval systems

2. **[[Dataview Query Patterns for File Classification]]**
   - *Connection*: Your naming convention enables powerful programmatic queries
   - *Depth Potential*: Create dynamic MOCs, dashboards, and automated reports based on filename patterns
   - *Knowledge Graph Role*: Technical implementation layer for leveraging your organizational system

3. **[[Version Control for Knowledge Work]]**
   - *Connection*: Your `[{version}]` parameter for prompts hints at sophisticated change tracking
   - *Depth Potential*: Explore Git integration, diff visualization, and temporal note evolution
   - *Knowledge Graph Role*: Intersection of PKM and software development practices

4. **[[Digital Archive Management Best Practices]]**
   - *Connection*: Your explicit need for Archive system design
   - *Depth Potential*: Archival triggers, retention policies, search optimization for historical content
   - *Knowledge Graph Role*: Lifecycle management for knowledge assets, connects to [[Information Governance]]