---
title: File Naming Conventions Reference
id: "20251122124133"
type: reference
year: "[[2025]]"
tags:
  - pkb
  - pkm
  - year/2025
  - pkb/maintenance/refactoring
  - pkb/maintenance/cleanup
aliases:
  - "File Naming,Note Naming,Naming Systems"
link-up:
  - "[[project-pur3v4d3r-moc]]"
link-related:
  - "[[2025-11-22|Daily-Note]]"
---

---

> [!the-purpose]
> **Naming conventions are systematic approaches to assigning names to entities within your Personal Knowledge Base.** They serve as the foundational architecture that determines how easily you can find, link, and scale your knowledge system. In the context of PKM (Personal Knowledge Management), naming conventions are not merely organizational niceties—they are strategic decisions that profoundly impact the usability, maintainability, and long-term viability of your digital knowledge base.

---

## 📐 Core Principles of Effective Naming

The art and science of naming conventions rests upon several fundamental principles that transcend any specific system or methodology. These principles form the bedrock upon which all effective naming strategies are built, whether you're naming variables in code, files in a directory, or permanent notes in your [[Zettelkasten]].

> [!core-principle]
> **Consistency is the Prime Directive**
> 
> The single most important principle in naming conventions is *consistency*. A mediocre naming system applied consistently will always outperform a brilliant system applied haphazardly. Consistency enables pattern recognition, supports automation, and dramatically reduces cognitive load when navigating your PKB. When you establish a convention—whether it's using `YYYY-MM-DD` for dates or prefixing all MOCs with `🗺️`—you must commit to it across your entire system.

> [!core-principle]
> **Human Readability First, Machine Parsability Second**
> 
> While it's tempting to optimize for database queries or script automation, your naming conventions must prioritize human comprehension. You will spend far more time reading, scanning, and manually navigating your notes than you will writing scripts to process them. A filename like `20251111_quantum-entanglement_bell-theorem.md` is infinitely more useful than `qe_bt_1111.md`, even if the latter is slightly more efficient for certain automated processes. That said, modern PKB tools like [[04_library/00_obsidian-documentation/02_Official-Documentation/02_⚫🔌Plugins/Plugin_🤖Text-Generator/Obsidian]] offer robust tagging and metadata systems—use those for machine-readable categorization, and reserve filenames for human cognition.

> [!core-principle]
> **Scalability & Future-Proofing**
> 
> Your PKB will grow. What works for 50 notes may collapse under 5,000. Design your naming conventions with scale in mind from the beginning. This means avoiding brittle hierarchies (like deeply nested folder structures that depend on rigid categories), embracing unique identifiers that won't conflict as your vault expands, and choosing patterns that remain meaningful even when you've forgotten the context in which you created them. A timestamp-based ID like `202511112034` will remain unique and sortable decades from now; a sequential number like `Note_047` might eventually collide or become ambiguous.

> [!core-principle]
> **Clarity Over Cleverness**
> 
> Resist the urge to create overly clever or cryptic naming systems. Your future self—reviewing notes months or years later—will not remember your intricate prefix taxonomy or your elaborate emoji code. Names should be **self-documenting** wherever possible. Use full words instead of abbreviations unless the abbreviation is universally recognized in your domain (e.g., `AI` not `ArtInt`, `SQL` not `StrcQryLang`). The goal is immediate comprehension, not space savings on a filesystem where storage is essentially infinite.

> [!core-principle]
> **Separation of Concerns: Filenames vs. Metadata**
> 
> Modern PKB systems like [[04_library/00_obsidian-documentation/02_Official-Documentation/02_⚫🔌Plugins/Plugin_🤖Text-Generator/Obsidian]] support rich metadata through YAML frontmatter, inline tags, and properties. This means you don't need to cram every piece of information into the filename itself. Use filenames for **identification and basic human navigation**, and use metadata for **categorization, status tracking, and advanced queries**. For example, instead of `Project_Active_2025_ClientX_Strategy_v2_FINAL.md`, use `ClientX_Strategy.md` with frontmatter like `status: active`, `year: 2025`, `version: 2`, `project: ClientX`.

---

## 🗂️ Types of Naming Conventions

Naming conventions exist across multiple domains, from software engineering to library science to personal knowledge management. Understanding the broader landscape helps you make informed decisions about your own PKB strategy.

### ⚙️ General Technical Conventions

These conventions originated in computer science and software development but have influenced PKM practices, especially when integrating automation, scripting, and advanced queries.

| **Convention** | **Example** | **Use Case** | **PKB Relevance** |
|----------------|-------------|--------------|-------------------|
| **camelCase** | `myDailyNote`, `quantumMechanics` | Variables, functions in JavaScript/Java | Low; harder to read in file lists |
| **PascalCase** | `MyDailyNote`, `QuantumMechanics` | Class names, components | Moderate; can work for MOC titles |
| **snake_case** | `my_daily_note`, `quantum_mechanics` | Python variables, database fields | High; readable, URL-safe, cross-platform |
| **kebab-case** | `my-daily-note`, `quantum-mechanics` | URLs, CSS classes, Hugo/Jekyll | High; very readable, web-friendly |
| **SCREAMING_SNAKE_CASE** | `MAX_CONNECTIONS`, `API_KEY` | Constants, environment variables | Low; too aggressive for notes |

> [!helpful-tip]
> For PKB filenames, **`kebab-case`** and **`snake_case`** are your best friends. They're highly readable, work across all operating systems (unlike spaces, which can cause issues in scripts), and naturally separate conceptual units. If you're building a hybrid system that needs to be both human-friendly and automation-compatible, start with one of these.

### 🧠 PKB-Specific Conventions

Personal Knowledge Base naming conventions are specifically designed to support the unique needs of knowledge work: linking, emergence, time-tracking, and the evolution of ideas over time.

> [!definition]
> **Timestamp-Based IDs (Zettelkasten Style)**
> 
> The most common modern Zettelkasten convention is to use a unique timestamp as the primary identifier for each permanent note. The format is typically `YYYYMMDDHHmm` (year, month, day, hour, minute), creating IDs like `202511112034`. This guarantees uniqueness, provides automatic chronological ordering, and creates a permanent, immutable identifier that never needs to change even if you completely rewrite the note's content or title. The human-readable title becomes secondary, often appended after the ID: `202511112034_Naming-Conventions.md`.

> [!definition]
> **Semantic Naming (Title-First Approach)**
> 
> In contrast to timestamp IDs, semantic naming prioritizes the **conceptual identity** of the note in the filename itself. A note is simply called `Naming-Conventions.md` or `Quantum-Entanglement.md`. This approach maximizes human readability and makes file lists feel like a table of contents. However, it requires careful attention to avoid duplicates (what if you later want a note on "Naming Conventions in Biology"?) and can make linking more ambiguous in very large vaults.

> [!definition]
> **Hybrid Approaches (ID + Semantic Title)**
> 
> Many practitioners combine the best of both worlds: a unique ID followed by a descriptive title. This gives you the uniqueness and permanence of IDs with the scannability of semantic titles: `20251111_Naming-Conventions.md`, `🆔202511112034_Quantum-Entanglement.md`, or `NC_001_Naming-Conventions.md`. The ID serves as the technical anchor for links and automation, while the title serves human cognition.

---

## 🧭 PKB Naming Strategies & Methodologies

Different PKM methodologies prescribe (or imply) different naming conventions. Understanding these frameworks helps you choose or design a system that aligns with your workflow and philosophical approach to knowledge work.

### 🗃️ Zettelkasten Approaches

The [[zettelkasten method]] has perhaps the richest history of naming convention evolution, from Niklas Luhmann's original analog system to modern digital implementations.

> [!cosmos-concept]
> **Luhmann's Folgezettel: The Original Branching System**
> 
> Niklas Luhmann's original slip-box used an alphanumeric **folgezettel** (German: "following note") system that encoded both position and relationship. A note might be labeled `1`, with a continuation `1a`, a branch from that `1a1`, and an alternative to the original `1b`. This created a tree-like structure where the ID itself indicated conceptual proximity and branching. 
> 
> In digital PKBs, this system is generally considered **too rigid** for the fluid, multi-dimensional linking that tools like [[04_library/00_obsidian-documentation/02_Official-Documentation/02_⚫🔌Plugins/Plugin_🤖Text-Generator/Obsidian]] enable. However, the principle—that IDs can encode *some* structural information—remains influential.

**Modern Timestamp IDs** have largely replaced folgezettel in digital Zettelkasten implementations. The standard format is `YYYYMMDDHHmm` or `YYYYMMDDHHmmss`:

```
202511112034_Naming-Conventions.md
202511120815_Semantic-Web-Ontologies.md
202511130942_Information-Architecture.md
```

**Why timestamps work:**
- **Guaranteed uniqueness** (assuming you don't create multiple notes in the same minute)
- **Automatic chronological sorting** (useful for reviewing recent additions)
- **Immutability** (the ID never changes, even if the note evolves completely)
- **Low cognitive overhead** (you don't need to think about what to call the ID; it's automatic)

> [!helpful-tip]
> **Timestamp Format Best Practices**
> 
> - Use `YYYYMMDDHHmm` for most purposes (e.g., `202511112034`)
> - Add seconds (`YYYYMMDDHHmmss`) only if you're programmatically creating many notes per minute
> - Always use 24-hour time format to avoid AM/PM ambiguity
> - Consider using ISO 8601 format with hyphens (`2025-11-11T2034`) if your system needs to interoperate with other tools, though this is less compact

### 📦 PARA Method Naming

Tiago Forte's [[para method]] organizes all information into four top-level categories: **Projects**, **Areas**, **Resources**, and **Archives**. While PARA is more about *folder structure* than *filenames*, it does imply certain naming conventions.

**Typical PARA Naming Patterns:**

- **Projects:** `Project - Client Website Redesign`, `PROJ_Website-Redesign_2025Q4`
- **Areas:** `Area - Health & Fitness`, `AREA_Career-Development`
- **Resources:** `Resource - JavaScript Tutorials`, `RSRC_Stoic-Philosophy`
- **Archives:** `[ARCHIVE] Old Marketing Campaign`, `ARCH_2024_Client-Project`

> [!use-cases-and-examples]
> **PARA Prefix Strategy**
> 
> Some practitioners use explicit prefixes to make the PARA category visible in the filename:
> 
> - `P_` for Projects
> - `A_` for Areas
> - `R_` for Resources
> - `X_` for Archives (using `X` to alphabetically sort archives to the end)
> 
> Example: `P_Book-Writing_Chapter-3-Outline.md`, `R_Cognitive-Science_Mental-Models.md`
> 
> However, many PARA users prefer to rely on *folder location* to indicate category, keeping filenames cleaner and more semantic.

### 🔗 LYT (Linking Your Thinking) Framework

Nick Milo's [[linking your thinking]] framework emphasizes Maps of Content ([[MOCs]]) as navigational hubs. LYT doesn't prescribe rigid naming conventions, but common patterns have emerged:

**MOC Naming Patterns:**
- `000_Home.md` (the central index, using leading zeros for top sorting)
- `Philosophy_MOC.md` or `🗺️_Philosophy.md`
- `PKM_🗺️.md` (emoji as a visual indicator)
- `+++_Main-MOCs.md` (using symbols for top-level hubs)

**Hub Note Conventions:**
- **Numeric Prefixes** for sorting: `000_Home`, `100_Philosophy`, `200_Science`
- **Emoji Indicators**: `🗺️` for MOCs, `🏛️` for hubs, `📚` for resource lists
- **Suffix Identifiers**: `_MOC`, `_HUB`, `_INDEX`

> [!helpful-tip]
> If you use emoji prefixes for MOCs (e.g., `🗺️_Philosophy.md`), be consistent about where you place them. Leading emojis create visual grouping in file lists, while trailing emojis maintain alphabetical title sorting but are less visually prominent.

### 📅 Date-Based Systems

Date-based naming is essential for **Daily Notes**, **Journals**, **Meeting Notes**, and any time-sensitive content. The gold standard is **ISO 8601**: `YYYY-MM-DD`.

**Common Date Patterns:**

| **Pattern** | **Example** | **Use Case** |
|-------------|-------------|--------------|
| `YYYY-MM-DD` | `2025-11-11` | Daily notes (ISO 8601 standard) |
| `YYYYMMDD` | `20251111` | Compact timestamp IDs |
| `YYYY-Www` | `2025-W46` | Weekly notes (ISO week format) |
| `YYYY-MM` | `2025-11` | Monthly reviews |
| `YYYY-Qq` | `2025-Q4` | Quarterly notes |

> [!core-principle]
> **Always Use ISO 8601 for Dates**
> 
> The `YYYY-MM-DD` format is internationally recognized, unambiguous, and sorts correctly in both alphabetical and chronological order. Avoid regional formats like `MM/DD/YYYY` (US) or `DD/MM/YYYY` (European), which create confusion and sorting problems. When you need to include time, use `YYYY-MM-DDTHH-mm-ss` (the `T` is the ISO 8601 separator between date and time).

**Daily Notes Example:**
```
2025-11-11_Monday.md
2025-11-12_Tuesday.md
2025-11-13_Wednesday.md
```

**Meeting Notes Example:**
```
2025-11-11_Team-Standup_Project-Kickoff.md
2025-11-13_Client-Meeting_Website-Redesign-Review.md
```

### 🏷️ Prefix & Emoji Systems

Many PKB practitioners use **visual prefixes** (emojis or symbols) to create semantic categories that are instantly recognizable in file lists and graph views.

> [!use-cases-and-examples]
> **Emoji-Based Type Indicators**
> 
> **Status Indicators** (for evergreen note maturity):
> - `🌱` Seedling (new, underdeveloped idea)
> - `🌿` Budding (taking shape, needs work)
> - `🌳` Evergreen (mature, well-developed)
> 
> **Type Indicators**:
> - `📝` Permanent Note / Zettel
> - `📚` Literature Note (book/article summary)
> - `🗺️` Map of Content (MOC)
> - `🧩` Component / Template
> - `⚙️` Process / Workflow
> - `💡` Idea / Fleeting Note
> - `🎯` Goal / Project
> - `🔬` Research / Experiment
> - `📊` Data / Analysis
> 
> Example filenames:
> - `🌱202511112034_Naming-Conventions.md`
> - `🗺️_Philosophy.md`
> - `📚_How-to-Take-Smart-Notes_Ahrens.md`
> - `⚙️_Daily-Review-Process.md`

> [!warning]
> **The Emoji Over-Engineering Trap**
> 
> Emoji systems are seductive because they're visually appealing and easy to implement. However, they can quickly become over-engineered. If you find yourself with 20+ different emoji categories, you've defeated the purpose. Emojis should provide *glanceable, high-level categorization*, not replace your entire tagging and metadata system. Limit yourself to 5-10 core emojis, maximum.

**Symbol-Based Prefixes** (for sorting):
- `+` or `000` for top-level hubs (sorts to the top)
- `_` (underscore) for templates or meta-notes (sorts to bottom in many systems)
- `!` for urgent or priority items
- `@` for people-related notes
- `#` for project tags (though this can conflict with Markdown headers)

---

## 🖥️ Obsidian-Specific Considerations

[[04_library/00_obsidian-documentation/02_Official-Documentation/02_⚫🔌Plugins/Plugin_🤖Text-Generator/Obsidian]] is a powerful PKB tool, but it has specific constraints and features that impact your naming strategy. Understanding these nuances ensures your conventions work *with* the tool, not against it.

### 🚫 Reserved Characters & Limitations

**Characters to AVOID in Obsidian filenames:**
- `/` (forward slash) - Reserved for folder paths
- `\` (backslash) - Reserved for escape sequences
- `:` (colon) - Problematic on Windows (reserved for drive letters)
- `*` (asterisk) - Wildcard character in many systems
- `?` (question mark) - Wildcard character
- `"` (double quote) - String delimiter
- `<` `>` (angle brackets) - HTML/XML tags
- `|` (pipe) - Used in some Markdown table syntax

> [!warning]
> **Cross-Platform Compatibility**
> 
> If you sync your vault across Windows, macOS, and Linux, be especially careful with colons (`:`). While macOS and Linux allow colons in filenames, Windows does not. If you create a note on Mac called `Meeting: Client Review.md`, you'll get sync errors on Windows. Stick to hyphens (`-`) or underscores (`_`) as separators.

**Safe Characters:**
- `a-z`, `A-Z` (letters)
- `0-9` (numbers)
- `-` (hyphen/dash)
- `_` (underscore)
- `.` (period, for file extensions)
- Spaces (allowed but can complicate scripting; consider using `-` or `_` instead)

### 🔗 Wiki-Link Best Practices

Obsidian's `[[Wiki-Links]]` are case-sensitive and match on filename (excluding the `.md` extension). This has several implications:

1. **Unique Filenames Are Critical:** If you have both `Stoicism.md` and `Stoicism_Philosophy.md`, linking to `[[Stoicism]]` might create ambiguity. Obsidian will link to one, but which one depends on factors like folder depth and alphabetical order.

2. **Aliases Solve Ambiguity:** Use YAML frontmatter aliases to create multiple ways to link to the same note:
   ```yaml
   aliases:
     - Stoic Philosophy
     - Stoicism Overview
     - Ancient Stoicism
   ```
   Now `[[Stoic Philosophy]]`, `[[Stoicism Overview]]`, and `[[Ancient Stoicism]]` all resolve to the same note.

3. **Folder Paths in Links (Optional):** You can include the folder path in a link: `[[Philosophy/Stoicism]]`. This makes links unambiguous but reduces portability if you reorganize your vault.

> [!helpful-tip]
> **Avoid Folder Dependence**
> 
> Relying on folder paths in links (`[[Folder/Note]]`) creates fragility—if you move a note to a different folder, all those links break. Instead, use unique filenames or IDs, and rely on Obsidian's alias system for disambiguation. This makes your vault more resilient to restructuring.

### ⚡ Dataview Query Optimization

If you use the [[dataview]] plugin for advanced queries, your naming conventions can significantly impact query performance and flexibility.

**Leverage Metadata Over Filenames:**
Instead of encoding everything in the filename (`Project_Active_2025_ClientX_Strategy.md`), use frontmatter:

```yaml
---
title: ClientX Strategy
type: project
status: active
year: 2025
client: ClientX
---
```

Now you can query powerfully:
```
TABLE status, client, year
FROM "Projects"
WHERE type = "project" AND status = "active"
SORT year DESC
```

**Filename Patterns for Dataview:**
If you do encode information in filenames (like date-based notes), Dataview can parse them:

```
LIST
WHERE file.name >= "2025-11-01" AND file.name <= "2025-11-30"
```

This works because `YYYY-MM-DD` sorts both alphabetically and chronologically.

---

## 🛠️ Practical Implementation

Choosing and implementing a naming convention is not a one-time decision—it's an evolving practice. Here's how to approach it systematically.

### 🤔 Choosing Your System

> [!ask-yourself-this]
> **The Naming Convention Decision Tree**
> 
> 1. **What is your primary PKB philosophy?**
>    - If **Zettelkasten** → Use timestamp IDs (`YYYYMMDDHHmm`) with semantic titles
>    - If **PARA** → Use folder-based categorization with semantic filenames
>    - If **LYT** → Use emojis or prefixes for MOCs, semantic for content notes
>    - If **Mixed/Agnostic** → Hybrid approach (ID + title) with rich metadata
> 
> 2. **How large is your vault (or how large will it become)?**
>    - **<500 notes:** Semantic naming alone might suffice
>    - **500-2000 notes:** Consider hybrid (ID + title) or strict prefixing
>    - **>2000 notes:** Timestamp IDs or similarly unique identifiers become essential
> 
> 3. **Do you script or automate your vault?**
>    - **Yes:** Prioritize machine-parsable patterns (`snake_case`, `kebab-case`, consistent prefixes)
>    - **No:** Optimize for human readability; metadata handles the rest
> 
> 4. **How often do you refactor or restructure?**
>    - **Frequently:** Use unique IDs to preserve link integrity during moves
>    - **Rarely:** Semantic filenames are fine; just avoid duplicates
> 
> 5. **Do you want note maturity visible at a glance?**
>    - **Yes:** Use emoji status indicators (`🌱`, `🌿`, `🌳`)
>    - **No:** Track status in frontmatter (`status: seedling`)

### 🔄 Migrating Existing Notes

If you're adopting a new naming convention mid-vault, here's a strategic migration process:

**Phase 1: Audit & Document**
1. Catalog your current naming patterns (use a Dataview query or script)
2. Identify inconsistencies and problem areas
3. Document your *new* convention in a `Naming-Convention-Guide.md` note

**Phase 2: Create New Notes Correctly**
4. Immediately start using the new convention for all new notes
5. Update your templates (Templater, QuickAdd) to enforce the new system

**Phase 3: Gradual Refactoring**
6. **Do NOT attempt a mass rename** without backups and thorough testing
7. Rename notes incrementally as you work with them ("Boy Scout Rule": leave notes better than you found them)
8. Use Obsidian's "Update internal links" feature when renaming (it's automatic, but verify)

**Phase 4: Automated Batch Renaming (Advanced)**
9. For large-scale migrations, write a script (Python, PowerShell, Bash) that:
   - Backs up your vault
   - Renames files according to your new pattern
   - Updates all internal links using regex
10. Test on a small subset first; validate links afterward

> [!warning]
> **Backup Before Bulk Renaming**
> 
> Renaming files at scale—especially with scripts—is **dangerous**. Always create a complete backup of your vault before attempting automated migrations. Use version control (Git) if possible, so you can roll back if things go wrong.

### 📋 Templates & Automation

Once you've chosen a convention, embed it in your workflow through templates and automation.

**Templater Example (Timestamp ID + Title):**
```
---
title: <% tp.file.title %>
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
id: <% tp.date.now("YYYYMMDDHHmm") %>
type: permanent
status: 🌱
tags: []
---

# <% tp.file.title %>

> [!the-purpose]
> 

---

## 🧠 Core Concept



---

## 🔗 Related
- 
```

**QuickAdd Macro (Date-Based Meeting Note):**
Configure QuickAdd to prompt for meeting type and auto-generate:
```
2025-11-11_Team-Standup_[User Input].md
```

---

## 📚 Common Patterns by Note Type

Different types of notes serve different functions and thus benefit from tailored naming conventions.

> [!use-cases-and-examples]
> **Daily Notes**
> 
> **Convention:** `YYYY-MM-DD` (ISO 8601)
> 
> **Examples:**
> - `2025-11-11.md`
> - `2025-11-11_Monday.md` (with day name for extra context)
> 
> **Rationale:** Daily notes are fundamentally time-ordered. ISO 8601 ensures correct sorting and international compatibility. Obsidian's Daily Notes plugin expects this format by default.

> [!use-cases-and-examples]
> **Permanent Notes / Zettels**
> 
> **Convention:** `YYYYMMDDHHmm_Semantic-Title.md`
> 
> **Examples:**
> - `202511112034_Naming-Conventions.md`
> - `202511120815_Quantum-Entanglement-Bell-Theorem.md`
> 
> **Rationale:** The timestamp ID provides uniqueness and immutability; the semantic title provides human navigation and context. This is the dominant convention in modern digital Zettelkasten practice.

> [!use-cases-and-examples]
> **Literature Notes**
> 
> **Convention:** `Author_Year_Short-Title.md` or `📚_Author_Year_Short-Title.md`
> 
> **Examples:**
> - `Ahrens_2017_How-to-Take-Smart-Notes.md`
> - `📚_Kahneman_2011_Thinking-Fast-and-Slow.md`
> - `📄_Einstein_1905_Special-Relativity-Paper.md`
> 
> **Rationale:** Literature notes are *about* external sources. Including author and year in the filename makes it trivial to identify the source without opening the note. The emoji prefix (`📚` for books, `📄` for papers) visually groups literature notes in file lists.

> [!use-cases-and-examples]
> **Maps of Content (MOCs)**
> 
> **Convention:** `Topic_MOC.md` or `🗺️_Topic.md`
> 
> **Examples:**
> - `Philosophy_MOC.md`
> - `🗺️_Cognitive-Science.md`
> - `000_Home_MOC.md` (top-level index)
> 
> **Rationale:** MOCs are navigational hubs, not content nodes. Clearly distinguishing them with a suffix (`_MOC`) or emoji (`🗺️`) prevents confusion. Leading numbers (`000`, `100`) can establish a hierarchy of hub importance.

> [!use-cases-and-examples]
> **Project Notes**
> 
> **Convention:** `Project-Name_Phase_Topic.md` or `🎯_Project-Name_Topic.md`
> 
> **Examples:**
> - `Website-Redesign_Planning_Sitemap.md`
> - `🎯_Book-Writing_Chapter-3_Outline.md`
> - `ClientX_Q4_Marketing-Strategy.md`
> 
> **Rationale:** Project notes are transient and action-oriented. Including the project name and phase in the filename makes it easy to filter or archive all related notes when the project concludes. The `🎯` emoji signals "active project work."

> [!use-cases-and-examples]
> **Meeting Notes**
> 
> **Convention:** `YYYY-MM-DD_Meeting-Type_Topic.md`
> 
> **Examples:**
> - `2025-11-11_Team-Standup_Sprint-Review.md`
> - `2025-11-13_Client-Meeting_Website-Feedback.md`
> - `2025-11-15_1-on-1_Manager-Career-Goals.md`
> 
> **Rationale:** Meeting notes are time-bound and context-specific. Leading with the date ensures chronological grouping, while the meeting type and topic provide glanceable context when reviewing past meetings.

---

## 🚨 Anti-Patterns & Pitfalls

Even well-intentioned naming conventions can go awry. Here are the most common failure modes and how to avoid them.

> [!warning]
> **Anti-Pattern: Over-Complexity (The Metadata Overload Trap)**
> 
> **Example:** `P_A_2025-Q4_ClientX_WebsiteRedesign_Phase2_Strategy_v3_FINAL_REVIEWED.md`
> 
> **Why it fails:** This filename attempts to encode project type, status, date, client, project name, phase, topic, version, and review status. It's unreadable, unmaintainable, and will inevitably become inconsistent. If even *one* of these dimensions changes, the filename becomes misleading or requires renaming (and link updates).
> 
> **Fix:** Use metadata in frontmatter:
> ```yaml
> project: ClientX Website Redesign
> phase: 2
> status: reviewed
> version: 3
> quarter: 2025-Q4
> ```
> Filename: `ClientX-Website-Strategy.md`

> [!constraints-and-pitfalls]
> **Anti-Pattern: Premature Optimization**
> 
> You spend weeks designing the "perfect" naming system, complete with elaborate prefix taxonomies, emoji codes, and version control patterns… for a vault with 50 notes. This is **premature optimization**. The system becomes a burden before it provides value.
> 
> **Better approach:** Start simple (semantic filenames + basic date format for daily notes). Add complexity *only when you feel pain*. If you start getting duplicate names, add IDs. If you can't find project notes, add a prefix system. Let your system *evolve* with your vault, not precede it.

> [!constraints-and-pitfalls]
> **Anti-Pattern: Inconsistent Application**
> 
> You decide to use timestamp IDs for permanent notes… but only remember to do it 60% of the time. Now your vault is a mix of `202511112034_Topic.md` and `Topic-Name.md`, destroying the value of the convention.
> 
> **Fix:** Use templates and automation (Templater, QuickAdd) to *enforce* your convention. Make it harder to create notes the wrong way than the right way.

> [!warning]
> **Anti-Pattern: Ignoring Searchability**
> 
> You create a cryptic abbreviation system to save characters: `ProjX_Q4_Str_v2.md`. Six months later, you search for "strategy" and can't find it because you abbreviated it to `Str`.
> 
> **Fix:** Prioritize **discoverability**. Use full words in filenames. Modern filesystems don't care about filename length, and your search function can't find words you didn't write.

> [!constraints-and-pitfalls]
> **Anti-Pattern: Folder-Dependent Naming**
> 
> You have notes called `Overview.md` in multiple folders:
> ```
> /Philosophy/Overview.md
> /Science/Overview.md
> /Projects/Overview.md
> ```
> 
> When you link to `[[Overview]]`, which one does Obsidian choose? This creates ambiguity and fragility.
> 
> **Fix:** Make filenames unique, even across folders: `Philosophy-Overview.md`, `Science-Overview.md`, `Projects-Overview.md`. Then folder structure becomes a *convenience*, not a *requirement*.

> [!warning]
> **Anti-Pattern: The Emoji Explosion**
> 
> You start with `🗺️` for MOCs, `📝` for notes, and `📚` for books. Soon you have `🔬`, `🧪`, `🎯`, `💡`, `⚙️`, `🌱`, `🌿`, `🌳`, `🏛️`, `🧩`, `📊`, `🎨`, `🎬`, `🎵`… 20+ emojis, each with subtle semantic distinctions you can't remember.
> 
> **Fix:** Limit emojis to **5-7 truly distinct categories**. Use frontmatter metadata for fine-grained categorization.

---

## 🧭 Decision Framework

Still unsure which naming convention to adopt? Use this framework to align your choice with your needs.

> [!ask-yourself-this]
> **Guiding Questions for Your Naming Convention**
> 
> 1. **What is my primary goal with my PKB?**
>    - If **long-term knowledge building** (Zettelkasten) → Timestamp IDs + semantic titles
>    - If **project management** (GTD, PARA) → Project-based prefixes + PARA folders
>    - If **personal wiki / reference** → Pure semantic naming + rich metadata
> 
> 2. **How do I primarily navigate my vault?**
>    - If **search-driven** → Semantic filenames with full words
>    - If **graph/link-driven** → IDs to stabilize links; titles for display
>    - If **folder-driven** → Simple semantic names; folder structure provides context
> 
> 3. **Do I need to collaborate or share notes?**
>    - If **yes** → Avoid overly personal emojis or cryptic abbreviations; use standard formats (ISO dates, etc.)
>    - If **no** → You have more freedom for idiosyncratic systems
> 
> 4. **How important is note permanence vs. note evolution?**
>    - If notes are **immutable ideas** → Timestamp IDs (ID never changes, even if content evolves)
>    - If notes are **evolving documents** → Semantic names (reflect current understanding)
> 
> 5. **Am I a "gardener" or an "architect"?**
>    - If **gardener** (organic growth, emergence) → Minimal structure; let links and tags do the work
>    - If **architect** (planned structure, hierarchy) → Explicit prefixes, numbering systems, or PARA

**Trade-Off Analysis:**

| **Convention** | **Pros** | **Cons** |
|----------------|----------|----------|
| **Timestamp IDs** | Unique, immutable, sortable, low overhead | Less human-readable, requires discipline |
| **Semantic Naming** | Maximally readable, intuitive | Risk of duplicates, names can become outdated |
| **Hybrid (ID + Title)** | Best of both worlds | Longer filenames, slightly more visual clutter |
| **Emoji Prefixes** | Visually distinctive, glanceable categorization | Can't remember codes, OS compatibility issues |
| **Folder + Simple Names** | Intuitive, familiar from file systems | Fragile, hard to refactor, limits multi-categorization |
| **PARA System** | Excellent for action-oriented work | Less suited to pure knowledge work (Zettelkasten) |

---

## 🧪 Advanced Topics

### 🤖 Automation with Templater

**Auto-Generate Timestamp ID + Title on Note Creation:**

```
<%*
// Generate unique timestamp ID
const now = tp.date.now("YYYYMMDDHHmm");
const title = await tp.system.prompt("Note Title:");
const filename = `${now}_${title.replace(/\s+/g, '-')}`;

// Rename file
await tp.file.rename(filename);
-%>
---
id: <% now %>
title: <% title %>
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
type: permanent
status: 🌱
---

# <% title %>

> [!the-purpose]
> 

```

**Daily Note with Auto-Linking to Yesterday/Tomorrow:**

```
---
date: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
---

# <% tp.date.now("MMMM Do, YYYY") %>

← [[<% tp.date.now("YYYY-MM-DD", -1) %>]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>]] →

## 🌅 Morning

## 🌆 Evening
```

### 📊 Dataview Queries for Validation

**Find All Notes Without Timestamp IDs:**

```
TABLE file.name AS "Filename", file.ctime AS "Created"
WHERE !regexmatch("^\d{12}_", file.name)
  AND file.folder != "Templates"
SORT file.ctime DESC
```

**List Notes by Status Emoji:**

```
TABLE status, file.mtime AS "Modified"
WHERE startswith(file.name, "🌱") OR startswith(file.name, "🌿") OR startswith(file.name, "🌳")
GROUP BY status
```

### 🔄 Batch Renaming Strategies

**Python Script for Bulk Timestamp ID Addition:**

```python
import os
import re
from datetime import datetime

vault_path = "/path/to/your/vault"

for root, dirs, files in os.walk(vault_path):
    for filename in files:
        if filename.endswith(".md") and not re.match(r'^\d{12}_', filename):
            # Extract creation time
            filepath = os.path.join(root, filename)
            ctime = os.path.getctime(filepath)
            timestamp_id = datetime.fromtimestamp(ctime).strftime("%Y%m%d%H%M")
            
            # Construct new filename
            new_filename = f"{timestamp_id}_{filename}"
            new_filepath = os.path.join(root, new_filename)
            
            # Rename
            os.rename(filepath, new_filepath)
            print(f"Renamed: {filename} → {new_filename}")
```

> [!warning]
> Always test batch renaming scripts on a *copy* of your vault first. Update internal links afterward using Obsidian's built-in link updating or a tool like `ripgrep` + `sed`.

### 🧠 Thought Experiments

> [!thought-experiment]
> **The 10,000 Note Test**
> 
> Imagine your vault has grown to 10,000 notes. Can you still find what you need? Does your naming convention scale? If every note is called `Topic.md`, you'll be drowning in disambiguation. If every note has a timestamp ID, they'll sort chronologically—but is that meaningful for finding a specific concept? This mental exercise reveals whether your system is built for the long haul or just optimized for your current 100-note comfort zone.

> [!thought-experiment]
> **The 5-Year Time Capsule**
> 
> You close your vault today and don't open it for 5 years. When you return, will your filenames still make sense? Will `Proj_Q4_Str` be meaningful, or will it be cryptic gibberish? Will `202511112034_Naming-Conventions.md` still be unambiguous, or will you have forgotten your entire convention? The best naming systems are *self-documenting*—they don't rely on memory.

---

## 🧭 Further Exploration

> [!related-topics-to-consider]
> **Prerequisite Knowledge**
> - `[[Personal Knowledge Management]]` — The broader practice in which naming conventions exist
> - `[[Zettelkasten Method]]` — Understanding this methodology clarifies *why* certain naming conventions emerged
> - `[[Information Architecture]]` — The discipline of organizing information for findability and usability
> 
> **Directly Related Topics**
> - `[[Folder Structure Strategies]]` — How folder organization interacts with naming conventions
> - `[[Tagging Systems]]` — An alternative (or complement) to filename-based categorization
> - `[[Metadata and Frontmatter]]` — The modern solution to reducing filename complexity
> - `[[Linking Strategies]]` — How your naming convention impacts link creation and maintenance
> 
> **Advanced Sub-Topics**
> - `[[Templater Automation]]` — Enforcing naming conventions through templates
> - `[[Dataview for Vault Management]]` — Querying and validating your naming patterns
> - `[[Graph View Optimization]]` — How naming and structure affect graph readability
> - `[[Cross-Platform Sync Considerations]]` — Ensuring your conventions work on Windows, Mac, Linux, iOS, Android

> [!connections-and-links]
> **Related Methodologies & Frameworks**
> - `[[PARA Method]]` — Tiago Forte's project-oriented organization system
> - `[[Linking Your Thinking (LYT)]]` — Nick Milo's framework emphasizing MOCs
> - `[[Johnny Decimal System]]` — A decimal-based hierarchical organization method
> - `[[BASB (Building a Second Brain)]]` — The broader philosophy behind PARA
> 
> **Technical References**
> - `[[ISO 8601 Date Format]]` — The international standard for date representation
> - `[[Unicode and Emoji in Filenames]]` — Technical considerations for cross-platform emoji use
> - `[[Regular Expressions for Filename Parsing]]` — Advanced pattern matching for automation
> - `[[Git and Version Control for PKB]]` — How naming impacts version control workflows

> [!further-exploration]
> **For Deeper Study**
> - Read: *How to Take Smart Notes* by Sönke Ahrens (for Zettelkasten ID rationale)
> - Explore: The Obsidian Forum's "Showcase" category for real-world naming systems
> - Experiment: Set up a test vault and try 3-4 different conventions with the same set of notes
> - Analyze: Your own search patterns—how do you *actually* find notes? Design for that.

---

### 🔗 Related Topics for PKB Expansion

* `[[Personal Knowledge Management]]`
* `[[Zettelkasten Method]]`
* `[[Information Architecture]]`
* `[[PARA Method]]`
* `[[Linking Your Thinking]]`
* `[[Obsidian Workflow Optimization]]`
* `[[Metadata and Frontmatter Strategies]]`
* `[[Folder vs. Tag Organization]]`
* `[[Templater and QuickAdd Automation]]`
* `[[Dataview Query Language]]`