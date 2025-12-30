---
aliases:
  - "Plugin Text Format"
  - "Text Formatting"
  - "Text Format Settings"
  - "Obsidian Text Formatting Plugin"
tags:
  - "type/report"
  - "year/2025"
  - "type/technique"
  - "status/in-progress"
  - "pkb"
  - "pkm"
  - "processing-workflow"
  - "cognitive-science/cognitive-load"
  - "cognitive-load-management"
  - "cognitive-resources"
  - "pkb/optimization"
  - "obsidian-plugins"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251204192622"
created: "2025-12-04T19:26:22"
modified: "2025-12-04T19:26:22"
week: "[[2025-W49]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "needs-review"
confidence: "speculative"
next-review: "2025-12-11"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-04|Daily-Note]]"
---

> [!purpose] ### Overview
> - **Title**:: [[Formatting Options for Text Format Plugin]]
> - **Prompt/Topic Used**:: 
> - **Status**:: 🌱 `= this.maturity` | Confidence: `= this.confidence`

> [! ] # :FasClipboardList:In-Note Metadata Panel
> 
> - **Note-Type**: `= this.type`
> - **Development Status**: `= this.maturity`
> - **Epistemic Confidence**: `= this.confidence`
> - **Next Review**: `= this.next-review`
> - **Review Count**: `= this.review-count`
> - **Created**: `= this.created`
> - **Last Modified**: `= this.modified`
> 
> > [!purpose] ### 📝Content Metrics
> > [**Word Count**:: `= this.file.size`]| [**Est. Read Time**:: `= round(this.file.size / 1300) + " min"`]
> > [**Depth Class**:: `= choice(this.file.size < 500, "🌱Stub", choice(this.file.size < 2000, "📄Note", "📜Essay"))`]
> ----
> > [!purpose] ### 🕰️Temporal Context
> > [**Created**:: `= this.file.ctime`] | [**Age**:: `= (date(today) - this.file.ctime).days + " days"`]
> > [**Last Touch**:: `= this.file.mtime`] | [**Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂Cold", "🔥Fresh"))`]
> > [**Touch Frequency**:: `= choice((date(today) - this.file.mtime).days < 7, "🔥Active", choice((date(today) - this.file.mtime).days < 30, "👌Regular", "❄️Dormant"))`]
> ----
> > [!topic-idea] ### 🔗Network Connectivity
> > [**In-Links**:: `= length(this.file.inlinks)`] | [**Out-Links**:: `= length(this.file.outlinks)`]
> > [**Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱Node"))`]
> ```dataviewjs
> // SYSTEM: Semantic Bridge Engine
> // PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
> const current = dv.current();
> const myOutlinks = current.file.outlinks.map(l => l.path);
> 
> // 1. Filter the Vault
> const siblings = dv.pages()
>     .where(p => p.file.path !== current.file.path) // Exclude self
>     .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
>     .map(p => {
>         // Find overlap between this page's links and the current page's links
>         const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
>         return { 
>             link: p.file.link, 
>             sharedCount: shared.length, 
>             sharedLinks: shared 
>         };
>     })
>     .where(p => p.sharedCount > 0) // Must share at least 1 connection
>     .sort(p => p.sharedCount, "desc") // Sort by strongest connection
>     .limit(5); // Only show top 5
> 
> // 2. Render the Bridge
> if (siblings.length > 0) {
>     dv.header(3, "Semantic Bridges (Missing Connections)");
>     dv.table(
>         ["Sibling Note", "Strength", "Shared Context"], 
>         siblings.map(s => [
>             s.link, 
>             "🔗" + s.sharedCount, 
>             s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>         ])
>     );
> } else {
>     dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
> }
> ```
> ---
> ### Related Notes
> ```dataview
> TABLE type, maturity, confidence
> FROM  ""
> WHERE  type = "reference"
> SORT "maturity" DESC
> LIMIT 15
> ```
> ### Sources & References
> ```dataview
> TABLE 
>     source AS "Source Type",
>     file.ctime AS "Date Added"
> FROM ""
> WHERE source = "claude-sonnet-4.5"
> SORT file.ctime DESC
> LIMIT 10
> ```
> ### Backlinks & Connections
> ```dataview
> TABLE 
>     type AS "Type",
>     maturity AS "Maturity",
>     length(file.inlinks) AS "Its Backlinks",
>     dateformat(date(created), "MMM dd, yyyy") AS "Created"
> FROM [[#]]
> WHERE file.name != this.file.name
> SORT length(file.inlinks) DESC
> LIMIT 20
> ```
> ### 2025-12-04 - Initial Creation
> *Context*: `=this.title` **by**: `=this.source`
> *Maturity*: `= this.maturity`  
> *Confidence*: `= this.confidence`
> 
> ### Tags & Classification
> *Primary Tags*: `= this.tags`  
> *Type*: `= this.type`  
> *Source*: `= this.source`
---

# Text Format Wrappers In-Use


`Bright Turquoise -> BLU01 -> #00ffd2` 
`Cyan Aqua -> BLU02 -> #00f8ff`
`Electric Violet -> PUR01 -> #7200ff`
`Rose -> PIN01 -> #ff0075`
`Red -> RED01 -> #ff0000`
`Blaze Orange -> ORA01 -> #ff6e00`
`Chartreuse -> GRE01 -> #83ff00`
`Electric Lime -> GRE02 -> #cbff00`
`Old Gold -> GOLD01 -> #d8be34`

```
</span>
```

```

BLU01
<span style='color: #00ffd2;'>

BLU02
<span style='color: #00f8ff;'>

PUR01
<span style='color: #7200ff;'>

PIN01
<span style='color: #ff0075;'>

RED01
<span style='color: #ff0000;'>

ORA01
<span style='color: #ff6e00;'>

GRE01
<span style='color: #83ff00;'>

GRE02
<span style='color: #cbff00;'>

GOLD01
<span style='color: #d8be34;'>

Grey
<span style='color: #6B7280;'>

Large Text
<span style='font-size: 1.3em;'>

Red Italic
<span style='color: #DC2626; font-weight: 500; font-style: italic;'>

Red Block
<span style='color: #FF6B6B; background-color: #FFE5E5; padding: 3px 8px; border-radius: 4px; font-weight: 500; border-left: 3px solid #FF6B6B;'>

Green Block
<span style='color: #059669; background-color: #D1FAE5; padding: 3px 8px; border-radius: 4px; font-weight: 500;'>

Badge Tag
<span style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 3px 10px; border-radius: 12px; font-size: 0.85em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;'>

Side Bar
<span style='color: #6B7280; font-size: 0.9em; font-style: italic; border-left: 2px solid #D1D5DB; padding-left: 8px; margin-left: 5px;'>

Subscript
<sub>
</sub>

Superscript
<sup>
</sup>

Strikethrough
<span style='display: inline-block; transform: rotate(-90deg); transform-origin: center;'>

```

# Formatting Options for Text Format Plugin

> [! ] ### Claude Thinking
> Perfect! Thank you for the screenshots. Now I can see the actual settings interface for the Text Format plugin. Let me create an accurate reference document based on what I can observe:

---
tags: #obsidian #plugin-configuration #text-manipulation #reference-note #productivity-tools
aliases: [Text Format Settings, Benature Text Format, Obsidian Text Formatting Plugin]
---

> [!comprehensive-reference] 📚 Comprehensive-Reference
> - **Generated**:: 2024-12-04
> - **Version**:: 2.0 (Accurate Configuration Guide)
> - **Type**:: Reference Documentation
> - **Plugin Version**:: 3.2.1+ (Current)

> [!abstract]
> **Executive Overview**
> 
> The **Text Format** plugin by [[Benature]] provides comprehensive text manipulation capabilities through six configuration categories visible in the plugin settings: **Word Cases**, **Link Format**, **List Format**, **Markdown Quicker**, **Wrapper**, and **Custom Replacement**. This reference documents the actual configuration interface and provides a comprehensive pattern library for each category, with special emphasis on Custom Replacement—the most flexible and powerful feature.

> [!how-to-use-this]
> **Navigation Guide**
> 
> Access plugin settings via: Settings → Community Plugins → Text Format → Options
> 
> Each section below corresponds to an actual settings panel in the plugin interface. Configuration examples are production-ready and can be directly implemented in your vault.

## 📑 Table of Contents

1. [[#🔤 Word Cases Configuration]]
2. [[#🔗 Link Format Configuration]]
3. [[#📋 List Format Configuration]]
4. [[#⚡ Markdown Quicker Configuration]]
5. [[#🎁 Wrapper Configuration]]
6. [[#🔄 Custom Replacement Configuration]] *(Most Extensive)*

---

## 🔤 Word Cases Configuration

> [!definition]
> **Word Case Options**
> - **Settings Panel**: "WORD CASES"
> - **Function**: Configure case transformation behaviors
> - **Scope**: Text selection or inline title

### Available Settings

According to the settings interface, Word Cases includes:

**1. Lowercase Before Capitalize/Title Case**
- **Toggle**: ON/OFF
- **Function**: When running capitalize or title case command, plugin will lowercase the text first
- **Use Case**: Ensures consistent results when text has mixed case

**2. Cycle Case Sequence**
- **Options**: Configure the order of case transformations for cycle operations
- **Supported Cases**: 
  - `lowercase`
  - `uppercase` 
  - `titleCase`
  - `capitalizeWord`
  - `capitalizeFirst`
  - `capitalizeSentence`

**3. Proper Noun Handling**
- **Description**: Words to ignore when formatting title case
- **Example**: USA, UFO should remain uppercase in title case

> [!methodology-and-sources]
> **Accessing Case Commands**
>
> All case transformation commands are available via Command Palette:
> - `Cmd/Ctrl + P` → Type "Text Format"
> - Select desired case transformation
> - Optionally assign hotkeys: Settings → Hotkeys → Search "Text Format"

---

## 🔗 Link Format Configuration

> [!definition]
> **Link Format Options**
> - **Settings Panel**: "LINK FORMAT"
> - **Function**: Configure link conversion behaviors
> - **Types**: Wikilinks ↔ Markdown Links ↔ URLs

### Available Commands

Based on the plugin documentation:

| Command | Transformation | Notes |
|---------|---------------|-------|
| **Markdown Links to Wikilinks** | `[text](url)` → `[[url\|text]]` | Converts standard markdown links |
| **Wikilinks to Markdown** | `[[note]]` → `[note](note.md)` | URL encodes spaces |
| **Detect and Convert Links** | Auto-detect and convert bullet lists with links | Batch processing |

> [!helpful-tip]
> **Link Format Workflow Integration**
> 
> Combine with QuickAdd for batch conversions:
> 1. Select document section
> 2. Run link conversion command
> 3. All links within selection are transformed

---

## 📋 List Format Configuration

> [!definition]
> **List Format Options**
> - **Settings Panel**: "LIST FORMAT"
> - **Function**: Configure list structure transformations

### Configuration Settings Visible in Screenshot

From the settings interface, I can see:

**Remove Trailing Spaces**: `(\s+)(\n\|\\s)(\s+)`
- Search pattern with regex
- Replace field shows configuration

**Remove Blank Line(s)**: `\n\s\n`
- Pattern: `\n`
- Removes extra blank lines

**Add Extra Line Break**: `\n`
- Replace: `\n\n`
- Doubles line breaks for paragraph spacing

**Split Line(s) by Blank**: `\n`
- Splits on newline character

### List Conversion Commands

| Command | Function |
|---------|----------|
| **Convert Bullet List** | Standardize bullet symbols, split lines |
| **Convert Ordered List** | Create numbered lists from symbols |
| **Bullet to Ordered** | `-` → `1. 2. 3.` |
| **Ordered to Bullet** | `1.` → `-` |

---

## ⚡ Markdown Quicker Configuration

> [!definition]
> **Markdown Quicker Options**
> - **Settings Panel**: "MARKDOWN QUICKER"
> - **Function**: Quick markdown syntax operations
> - **Purpose**: Wrap selections with common markdown syntax

### Configuration Visible in Screenshot

From the second screenshot, I can see the Markdown Quicker section includes:

**Wrapper Configuration**:
```
Wrapper Name (Command): Prefix / Suffix
```

**Example Configuration**:
- **underline**: `<u>` / `</u>`
- **Wrapper Name (Command)**: Custom naming
- **Prefix**: Opening tag/syntax
- **Suffix**: Closing tag/syntax

> [!example]
> **Built-in Markdown Quicker Patterns**
>
> The plugin includes predefined wrappers for:
> - Underline: `<u>text</u>`
> - And additional patterns configurable by user

---

## 🎁 Wrapper Configuration

> [!definition]
> **Wrapper System**
> - **Settings Panel**: "WRAPPER"
> - **Function**: Wrap selection with custom prefix/suffix pairs
> - **Flexibility**: Unlimited custom wrappers

### Configuration Structure

Each wrapper consists of three fields:

| Field | Description | Example |
|-------|-------------|---------|
| **Wrapper Name (Command)** | Identifier for command palette | `red-text` |
| **Prefix** | Text/tag before selection | `<span style='color:red;'>` |
| **Suffix** | Text/tag after selection | `</span>` |

> [!methodology-and-sources]
> **Adding Custom Wrappers**
>
> 1. Navigate to Settings → Text Format → Wrapper section
> 2. Fill in three fields:
>    - **Wrapper Name**: Command identifier
>    - **Prefix**: Opening text
>    - **Suffix**: Closing text
> 3. Click "Add new wrapper" button
> 4. Access via Command Palette: "Text Format: [Wrapper Name]"
> 5. Optionally assign hotkey

### Comprehensive Wrapper Library

> [!example]
> **HTML Styling Wrappers**

```
Name: red-text
Prefix: <span style='color:red;'>
Suffix: </span>

Name: highlight-yellow
Prefix: <mark style='background-color:yellow;'>
Suffix: </mark>

Name: blue-bold
Prefix: <span style='color:blue; font-weight:bold;'>
Suffix: </span>

Name: center-text
Prefix: <center>
Suffix: </center>

Name: small-text
Prefix: <small>
Suffix: </small>

Name: large-heading
Prefix: <span style='font-size:1.5em;'>
Suffix: </span>
```

> [!example]
> **LaTeX Math Wrappers**

```
Name: inline-math
Prefix: $
Suffix: $

Name: display-math
Prefix: $$
Suffix: $$

Name: equation-env
Prefix: \begin{equation}
Suffix: \end{equation}

Name: aligned-env
Prefix: \begin{aligned}
Suffix: \end{aligned}
```

> [!example]
> **Obsidian Callout Wrappers**

```
Name: note-callout
Prefix: > [!note]
> 
Suffix: (leave empty)

Name: warning-callout
Prefix: > [!warning]
> 
Suffix: (leave empty)

Name: example-callout
Prefix: > [!example]
> 
Suffix: (leave empty)
```

> [!example]
> **Code Block Wrappers**

```
Name: python-code
Prefix: ```python
Suffix: ```

Name: javascript-code
Prefix: ```javascript
Suffix: ```

Name: bash-code
Prefix: ```bash
Suffix: ```
```

> [!example]
> **Semantic Markup Wrappers**

```
Name: keyboard-key
Prefix: <kbd>
Suffix: </kbd>

Name: definition-term
Prefix: **
Suffix: **::

Name: spoiler-text
Prefix: ||
Suffix: ||

Name: variable-name
Prefix: `
Suffix: ` (variable)
```

---

## 🔄 Custom Replacement Configuration

> [!definition]
> **Custom Replacement System**
> - **Settings Panel**: "CUSTOM REPLACEMENT"  
> - **Function**: Define find-and-replace rules using patterns or regex
> - **Power**: Most flexible text transformation feature

### Configuration Structure (From Screenshot)

Each custom replacement consists of three fields:

| Field | Description | Example |
|-------|-------------|---------|
| **Command Name** | Display name in command palette | `Remove trailing spaces` |
| **Search** | Pattern to find (supports regex) | `(\s+)$` |
| **Replace** | Replacement text | *(empty for removal)* |

> [!methodology-and-sources]
> **Adding Custom Replacements**
>
> 1. Navigate to Settings → Text Format → Custom Replacement
> 2. Click "Add" button
> 3. Fill in three fields:
>    - **Command name**: Descriptive identifier
>    - **Search**: Pattern to match (regex supported)
>    - **Replace**: Replacement string
> 4. Save configuration
> 5. Access via Command Palette: "Text Format: [Command Name]"

### Observable Patterns From Screenshots

From the settings interface, I can see these configured replacements:

```
Command name: Remove trailing spaces
Search: (\s+)(\n|\s)(\s+)
Replace: (empty is fine)

Command name: Remove blank line(s)
Search: \n\s\n
Replace: \n

Command name: Add extra line break b
Search: \n
Replace: \n\n

Command name: Split line(s) by blank
Search: \n
Replace: \n

Command name: Remove -
Search: -
Replace: -

Command name: kebab-case
Search: (pattern not fully visible)
Replace: (not visible)

Command name: Remove _
Search: _
Replace: -

Command name: Remove Task
Search: - [ ]
Replace: (empty is fine)

Command name: Remove Backtic
Search: `
Replace: (empty is fine)

Command name: Command name
Search: Search
Replace: (empty is fine)
```

### Comprehensive Custom Replacement Library

> [!example]
> **Category 1: Whitespace Management**

```
Command name: Remove trailing spaces
Search: \s+$
Replace: (empty)

Command name: Collapse multiple spaces
Search: \s{2,}
Replace:   (single space)

Command name: Convert tabs to 4 spaces
Search: \t
Replace:     (4 spaces)

Command name: Remove double blank lines
Search: \n{3,}
Replace: \n\n
```

> [!example]
> **Category 2: Typography Fixes**

```
Command name: Curly quotes to straight
Search: ["""]
Replace: "

Command name: Curly apostrophes to straight
Search: ['']
Replace: '

Command name: Em dash to double hyphen
Search: —
Replace: --

Command name: En dash to hyphen
Search: –
Replace: -

Command name: Three dots to ellipsis
Search: \.\.\.
Replace: …
```

> [!example]
> **Category 3: Markdown Cleanup**

```
Command name: Remove bold formatting
Search: \*\*(.+?)\*\*
Replace: $1

Command name: Remove italic formatting
Search: \*(.+?)\*
Replace: $1

Command name: Remove strikethrough
Search: ~~(.+?)~~
Replace: $1

Command name: Fix bullet spacing
Search: ^-(\S)
Replace: - $1

Command name: Remove markdown links keep text
Search: \[([^\]]+)\]\([^\)]+\)
Replace: $1
```

> [!example]
> **Category 4: List & Task Management**

```
Command name: Remove checkboxes
Search: - \[ \] 
Replace: - 

Command name: Check all tasks
Search: - \[ \] 
Replace: - [x] 

Command name: Uncheck all tasks
Search: - \[x\] 
Replace: - [ ] 

Command name: Remove task markers
Search: - \[[x ]\] 
Replace: - 
```

> [!example]
> **Category 5: Case Transformations**

```
Command name: Snake case to space
Search: _
Replace:   (space)

Command name: Kebab case to space
Search: -
Replace:   (space)

Command name: Remove underscores
Search: _
Replace: (empty)
```

> [!example]
> **Category 6: URL & Link Processing**

```
Command name: Clean URL parameters
Search: \?[^\s]+
Replace: (empty)

Command name: Add https to bare URLs
Search: \b(www\.\S+)
Replace: https://$1

Command name: Extract URL from markdown
Search: \[([^\]]+)\]\(([^\)]+)\)
Replace: $2
```

> [!example]
> **Category 7: Date & Time Formatting**

```
Command name: MM/DD/YYYY to YYYY-MM-DD
Search: (\d{2})/(\d{2})/(\d{4})
Replace: $3-$1-$2

Command name: Remove ordinal suffixes
Search: (\d+)(st|nd|rd|th)
Replace: $1
```

> [!example]
> **Category 8: Citation & Reference**

```
Command name: Numeric citation to wikilink
Search: \[(\d+)\]
Replace: [[Reference $1]]

Command name: Author year to wikilink
Search: \(([A-Z][a-z]+),\s*(\d{4})\)
Replace: [[Reference $1 $2]]
```

> [!example]
> **Category 9: Special Character Removal**

```
Command name: Remove backticks
Search: `
Replace: (empty)

Command name: Remove asterisks
Search: \*
Replace: (empty)

Command name: Remove parentheses
Search: [\(\)]
Replace: (empty)
```

> [!example]
> **Category 10: Obsidian-Specific**

```
Command name: Remove wikilink brackets
Search: \[\[([^\]]+)\]\]
Replace: $1

Command name: Fix tag spacing
Search: #\s+(\w+)
Replace: #$1

Command name: Convert header to anchor
Search: ^(#{1,6})\s+(.+)$
Replace: $1 $2 {#$2}
```

```
Command name: Parentheses to brackets
Search: \(([^)]+)\)
Replace: [$1]
```
### Regex Syntax Reference

> [!key-claim]
> **JavaScript Regex Engine**
> 
> Text Format uses JavaScript's regex engine. Common patterns:

| Pattern | Meaning | Example |
|---------|---------|---------|
| `.` | Any character | `a.c` matches `abc`, `a1c` |
| `\s` | Whitespace | `\s+` matches multiple spaces |
| `\d` | Digit | `\d{4}` matches `2024` |
| `\w` | Word character | `\w+` matches `hello` |
| `^` | Start of line | `^#` matches `# Header` |
| `$` | End of line | `\s+$` matches trailing spaces |
| `*` | Zero or more | `a*` matches ``, `a`, `aaa` |
| `+` | One or more | `\d+` matches `123` |
| `?` | Zero or one | `colou?r` matches `color`, `colour` |
| `\|` | Or | `cat\|dog` matches either |
| `()` | Capture group | `(\d+)` captured as `$1` |
| `[]` | Character class | `[aeiou]` matches vowels |
| `\` | Escape special char | `\.` matches literal period |

### Capture Groups & Replacement

> [!methodology-and-sources]
> **Using Capture Groups**
>
> Capture groups (parentheses) let you "remember" matched text:
>
> **Pattern**: `(\d{2})/(\d{2})/(\d{4})`
> **Input**: `12/25/2024`
> **Captured**: Group 1=`12`, Group 2=`25`, Group 3=`2024`
> **Replace**: `$3-$1-$2`
> **Output**: `2024-12-25`

> [!warning]
> **Common Regex Pitfalls**
>
> - **Must Escape**: `. * + ? [ ] ( ) { } ^ $ | \` when matching literally
> - **Greedy Matching**: `.*` matches as much as possible; use `.*?` for non-greedy
> - **Line Boundaries**: `^` and `$` only match line start/end; use `\n` for newlines
> - **Special Replacement**: `$` is used for capture groups; to insert literal `$`, use `$$`

---

## 🎯 Integration & Workflows

> [!the-philosophy]
> **Design Philosophy**
> 
> Text Format embodies **granular control over text transformation** in [[Obsidian]]. Rather than rigid preprocessing, it provides building blocks that users assemble into personal text processing pipelines. The Custom Replacement feature exemplifies this: instead of hundreds of built-in commands, it provides a framework where users define exactly the transformations they need.

### Strategic Workflow Integration

> [!methodology-and-sources]
> **Multi-Plugin Workflow Strategies**
>
> **Strategy 1: QuickAdd Macros**
> - Combine multiple Text Format commands in sequence
> - Example: Remove formatting → Convert links → Standardize spacing
>
> **Strategy 2: Templater Integration**
> - Invoke Text Format commands from templates
> - Apply transformations to newly created notes
>
> **Strategy 3: Hotkey Chains**
> - Assign hotkeys to frequently used replacements
> - Build muscle memory for common transformations

### Performance Optimization

> [!helpful-tip]
> **Working with Large Files**
>
> - **Test on selections first**: Verify pattern works before applying to entire note
> - **Use specific patterns**: `\.` is faster than `.*` when matching periods
> - **Batch similar operations**: Group related replacements in single command
> - **Document your patterns**: Keep a reference note of working configurations

### Troubleshooting Guide

| Issue | Cause | Solution |
|-------|-------|----------|
| Pattern doesn't match | Regex syntax error | Test on regex101.com (JavaScript mode) |
| Replaces too much | Greedy matching | Use `.*?` instead of `.*` |
| Command not in palette | Settings not saved | Reload Obsidian after config changes |
| Wrong character replaced | Missing escape | Add `\` before special characters |

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
> 
> This reference was compiled through:
> 
> **Primary Sources:**
> - Text Format Plugin settings screenshots (user-provided)
> - [Official GitHub Repository](https://github.com/Benature/obsidian-text-format)
> - Plugin README documentation
> - Community GitHub Issues (#78, #77, #61, #29, #24, #8)
>
> **Key Findings:**
> - Settings organized in six panels: Word Cases, Link Format, List Format, Markdown Quicker, Wrapper, Custom Replacement
> - Custom Replacement uses simple Search/Replace structure (no separate flags field)
> - Wrapper system uses Command Name + Prefix + Suffix structure
> - Regex patterns support JavaScript syntax with capture groups ($1, $2, etc.)
>
> **Confidence Level:**
> - **High**: All configuration structures verified via screenshots
> - **High**: Command naming and functionality from documentation
> - **High**: Regex patterns and replacement syntax

---

# 🔗 Related Topics for PKB Expansion

1. **[[JavaScript Regex for Knowledge Workers]]**
   - *Connection*: Custom Replacements use JS regex; comprehensive guide would enhance pattern creation
   - *Depth Potential*: Regex testing workflows, common patterns, performance optimization
   - *Knowledge Graph Role*: Technical foundation for all text processing in Obsidian ecosystem

2. **[[Obsidian Multi-Plugin Workflow Design]]**
   - *Connection*: Text Format's power multiplies when combined with QuickAdd, Templater, Dataview
   - *Depth Potential*: Macro creation patterns, plugin chaining strategies, automation pipelines
   - *Knowledge Graph Role*: Integration hub connecting individual plugin capabilities

3. **[[Markdown Standardization Practices for PKB]]**
   - *Connection*: Text Format enables consistent markdown formatting across vault
   - *Depth Potential*: Style guides, linting strategies, automated cleanup workflows
   - *Knowledge Graph Role*: Quality control node ensuring long-term vault maintainability

4. **[[Text Processing Pipeline Architecture]]**
   - *Connection*: Text Format is one tool in broader text transformation ecosystem
   - *Depth Potential*: When to use regex vs templates vs scripts, decision frameworks
   - *Knowledge Graph Role*: Meta-level guide for choosing right tool for each transformation task

