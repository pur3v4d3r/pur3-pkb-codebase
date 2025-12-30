---
title: "Templater: 📚Comprehensive-Reference"
id: 20251113-202519
type: reference
status: seedling
rating: ""
source: claude-4.5-sonnet
url: https://claude.ai/chat/7db8f382-92f6-493a-999e-439a96aa681b
tags:
  - year/2025
  - status/seedling
  - pkb/infrastructure
  - type/reference
  - source/llm/claude
  - pkb
  - pkb/plugin/templater
  - pkm
  - pkb/infrastructure/automation
aliases:
  - Templater Plugin
  - Templater Reference
  - Obsidian Templater Guide
  - Templater Syntax Reference
link-up: []
link-related: []
---
`LAST KNOWN READING POSITION:    `

---

aliases: [Templater Plugin, Templater Reference, Obsidian Templater Guide, Templater Syntax Reference]
---




> [!comprehensive-reference] 📚 Comprehensive-Reference
> - **Generated**:: 2025-11-13
> - **Version**:: 1.0
> - **Type**:: Reference Documentation

> [!abstract]
> **Executive Overview**
> [[Templater]] is the most powerful community plugin for [[obsidian]], enabling dynamic template creation through a custom [[Templating Language]], [[JavaScript]] execution, and [[System Command]] integration. This plugin transforms static [[Markdown]] files into intelligent, context-aware document generators that can manipulate [[Frontmatter]], create files programmatically, interact with the [[Obsidian API]], and automate complex [[workflow]] patterns within your [[Personal Knowledge Base]].

> [!how-to-use-this]
> **Navigation Guide**
> This reference note is organized into 10 major sections covering every aspect of Templater from novice installation through expert-level [[JavaScript]] scripting. Use the table of contents below for quick navigation, or search for specific functions using [[Wiki-Links]]. Each section includes detailed syntax specifications, practical examples with accurate code, and progressive skill-building from basic to advanced usage.

## 📑 Table of Contents

1. [[#🎯 1. Introduction & Core Concepts|Introduction & Core Concepts]]
2. [[#⚙️ 2. Installation & Configuration|Installation & Configuration]]
3. [[#📐 3. Syntax Fundamentals|Syntax Fundamentals]]
4. [[#📦 4. Internal Functions - Complete Reference|Internal Functions - Complete Reference]]
5. [[#🎨 5. Command Types & Execution Modes|Command Types & Execution Modes]]
6. [[#🔧 6. User Functions & Custom Scripts|User Functions & Custom Scripts]]
7. [[#🚀 7. Advanced Patterns & Workflows|Advanced Patterns & Workflows]]
8. [[#🔗 8. Integration with Obsidian Ecosystem|Integration with Obsidian Ecosystem]]
9. [[#⚠️ 9. Troubleshooting & Best Practices|Troubleshooting & Best Practices]]
10. [[#🎓 10. Mastery Patterns & Philosophy|Mastery Patterns & Philosophy]]

---

## 🎯 1. Introduction & Core Concepts

### What is Templater?

[[Templater]] is a community plugin for [[obsidian]] that extends the native [[04_library/02_pkb-and-pkm-learning/_reference/_official-documentation/_obsidian/_obsidian-web-clipper 1/templates]] functionality by introducing a powerful [[Templating Engine]] based on a custom implementation called [[rusty_engine]]. Unlike Obsidian's core templates plugin (which simply inserts static text), Templater provides dynamic content generation through:

- **Variable Interpolation**: Insert computed values based on file metadata, dates, or custom logic
- **JavaScript Execution**: Run arbitrary [[JavaScript]] code within templates
- **Function Library**: Access 70+ built-in functions organized into logical modules
- **User Extensions**: Create custom functions via [[JavaScript]] scripts or [[System Commands]]
- **API Access**: Full access to the [[Obsidian API]] for vault manipulation

> [!definition]
> - **Template**:: A [[Markdown]] file containing both static content and dynamic [[Templater Commands]] enclosed in `<% %>` tags
> - **Command**:: A text snippet between `<%` and `%>` that executes code or inserts values
> - **tp Object**:: The root namespace containing all Templater functions and modules

### Fundamental Architecture

Templater operates on a hierarchical object model where all functionality is accessed through the `tp` object:

```
tp (root object)
├── tp.config     → Plugin configuration access
├── tp.date       → Date manipulation functions
├── tp.file       → File operations and metadata
├── tp.frontmatter → YAML frontmatter access
├── tp.hooks      → Lifecycle event handlers
├── tp.obsidian   → Direct Obsidian API access
├── tp.system     → User interaction prompts
├── tp.user       → Custom user-defined functions
├── tp.web        → Web API integration
└── tp.app        → Full Obsidian app instance
```

> [!core-principle]
> **Single Responsibility Hierarchy**
> Every Templater function follows the [[Dot Notation]] pattern `tp.<module>.<function>()`, creating a self-documenting, discoverable API. This architectural decision enables [[Intellisense]] support and prevents namespace collisions.

### How Templates Execute

When Templater processes a template, it follows this execution sequence:

1. **Template Selection**: User triggers template insertion via command palette, hotkey, or automatic folder rule
2. **Content Loading**: Templater reads the template file's [[Markdown]] content
3. **Command Discovery**: Parser identifies all `<% %>` command blocks
4. **Sequential Execution**: Commands execute **bottom-to-top** (this is critical for [[Frontmatter]] manipulation)
5. **String Replacement**: Executed commands' output replaces the command blocks
6. **Final Insertion**: Processed content inserts at cursor position or replaces entire file

> [!warning]
> **Execution Order Gotcha**
> Templater executes functions **bottom-to-top**, not top-to-bottom. This means frontmatter values set at the top of your template won't be available to `tp.frontmatter` calls later in the same template execution. Use [[#tp.hooks|tp.hooks.on_all_templates_executed()]] for post-processing that requires frontmatter access.

---

## ⚙️ 2. Installation & Configuration

### Installation Process

> [!methodology-and-sources]
> **Step-by-Step Installation**
> 
> 1. Open Obsidian Settings (⚙️ icon or `Cmd/Ctrl + ,`)
> 2. Navigate to **Community Plugins**
> 3. If prompted, disable [[Safe Mode]] (required for community plugins)
> 4. Click **Browse** to open the community plugin browser
> 5. Search for "**Templater**" by **SilentVoid13**
> 6. Click **Install**, then **Enable**
> 7. **IMPORTANT**: Disable the core "Templates" plugin to avoid conflicts
>    - Go to Settings → Core Plugins
>    - Toggle OFF the "Templates" plugin

### Essential Configuration Settings

Once installed, configure Templater through Settings → Templater:

#### Template Folder Location

> [!what-this-does]
> **Template Folder Location**
> Specifies which folder contains your template files. Templater only recognizes [[Markdown]] files in this folder (and subfolders) as valid templates.

**Best Practice**: Create a dedicated folder structure:
```
📁 Your Vault
└── 📁 Templates/
    ├── 📁 Daily/
    ├── 📁 Projects/
    ├── 📁 Snippets/
    └── 📁 Meta/
```

**Configuration**: Set "Template folder location" to `Templates` (or your chosen folder name)

#### Trigger Templater on New File Creation

> [!helpful-tip]
> **Automatic Template Application**
> Enable this to automatically apply templates when creating new files. This works with:
> - [[Daily Notes]] core plugin
> - [[Calendar]] plugin
> - [[Periodic Notes]] plugin
> - Any plugin that creates files programmatically

**Critical Requirement**: You **must** configure either [[#Folder Templates]] or [[#File Regex Templates]] for this to work.

#### Folder Templates

Maps specific folders to specific templates. When a file is created in a designated folder, Templater automatically applies the associated template.

**Example Configuration**:
| Folder Path | Template Path |
|-------------|---------------|
| `Daily/` | `Templates/Daily/daily-note.md` |
| `Projects/` | `Templates/Projects/project-template.md` |
| `People/` | `Templates/Meta/person-template.md` |

#### Syntax Highlighting

- **Syntax Highlighting on Desktop**: Adds [[Syntax Highlighting]] for Templater commands in edit mode
- **Syntax Highlighting on Mobile**: Same feature for mobile (use cautiously as it may affect [[Live Preview]] performance)

#### Automatic Jump to Cursor

When enabled, automatically triggers [[#tp.file.cursor|tp.file.cursor()]] after template insertion, moving your cursor to the first defined cursor position.

**Manual Alternative**: Set a hotkey for "Templater: Jump to next cursor position" to control cursor jumping manually.

#### Script Files Folder Location

> [!important]
> **User Scripts Configuration**
> Specify a folder for [[JavaScript]] files that define [[User Functions]]. These scripts extend Templater's functionality with custom logic.

**Recommended Structure**:
```
📁 Scripts/
├── 📄 myCustomFunction.js
├── 📄 advancedFormatter.js
└── 📁 modules/
    └── 📄 helpers.js
```

**Requirements**:
- Scripts must be `.js` files (not `.md`)
- Must follow [[CommonJS]] module format (`module.exports = ...`)
- Must be created outside Obsidian (use text editor or IDE)

#### Startup Templates

Templates that execute automatically when Obsidian launches. Useful for:
- Initializing daily [[Dashboard]] notes
- Updating [[MOC]] indices
- Triggering background [[Automation]] tasks

> [!warning]
> **Startup Performance**
> Startup templates execute synchronously and can delay Obsidian's launch. Use sparingly and optimize for performance.

---

## 📐 3. Syntax Fundamentals

### Command Syntax Structure

> [!definition]
> - **Opening Tag**:: `<%` — Marks the beginning of a Templater command
> - **Closing Tag**:: `%>` — Marks the end of a Templater command  
> - **Complete Command**:: `<% expression or code %>`

Every Templater command must have both opening and closing tags. The content between tags determines command behavior.

### Two Core Command Types

#### Interpolation Commands (`<%`)

**Purpose**: Output the result of an expression

**Syntax**: `<% expression %>`

**Behavior**: Evaluates the expression and inserts the returned value into your document

**Examples**:
```markdown
<% tp.date.now() %>
<!-- Outputs: 2025-11-13 -->

<% tp.file.title %>
<!-- Outputs: The current file's title -->

<% 2 + 2 %>
<!-- Outputs: 4 -->

<% "Hello " + tp.file.title %>
<!-- Outputs: Hello YourFileName -->
```

> [!helpful-tip]
> **When to Use Interpolation**
> Use interpolation commands when you want to insert a single value. These are ideal for simple, one-line insertions like dates, filenames, or basic calculations.

#### Execution Commands (`<%*`)

**Purpose**: Execute [[JavaScript]] code without default output

**Syntax**: `<%* code %>`

**Behavior**: Runs JavaScript code silently. To produce output, you must explicitly append to the `tR` variable (Template Result).

**Examples**:
`````
`````javascript
<%*
// This executes but produces no output
const myVar = "test";
%>

<%*
// This DOES produce output
tR += "This text will appear";
%>

<%*
// Complex logic with conditional output
if (tp.file.title.startsWith("Project")) {
    tR += "This is a project note!";
} else {
    tR += "This is a regular note.";
}
%>

<%*
// Variable declaration for later use
let todayDate = tp.date.now("YYYY-MM-DD");
%>
Date: <% todayDate %>
````
`````

> [!core-principle]
> **The tR Variable**
> `tR` (Template Result) is a special string variable that accumulates the final template output. In execution commands, you control what gets inserted by manipulating `tR` using `+=` to append or `=` to overwrite.

### Function Invocation Syntax

All Templater functions follow this pattern:

```javascript
tp.<module>.<function>(argument1, argument2, ...)
````

**Breakdown**:
- `tp` → Root object (always required)
- `.` → [[Dot Notation]] for accessing child objects/functions
- `<module>` → Functional grouping (date, file, system, etc.)
- `.<function>` → Specific function name
- `()` → Parentheses required for function invocation
- Arguments inside parentheses (if function accepts them)

**Valid Examples**:
```javascript
<% tp.date.now() %>
<% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
<% tp.system.prompt("Enter title") %>
```

**Invalid Examples (Will Error)**:
```javascript
<% tp.date.now %>          // Missing parentheses
<% date.now() %>           // Missing tp prefix
<% tp.date.now(format: "YYYY-MM-DD") %>  // Named arguments (not JS syntax)
```

### Argument Types & Syntax

#### String Arguments

Enclosed in single or double quotes:
```javascript
<% tp.file.rename("New Title") %>
<% tp.date.now('YYYY-MM-DD') %>
```

#### Number Arguments

Raw integers (no quotes):
```javascript
<% tp.date.now("YYYY-MM-DD", 7) %>     // 7 days offset
<% tp.file.cursor(1) %>                // Cursor position 1
```

#### Boolean Arguments

Lowercase `true` or `false` only:
```javascript
<% await tp.file.create_new("Content", "Filename", true) %>  // true = open file
<% await tp.system.prompt("Title", null, false) %>           // false = don't throw on cancel
```

#### Optional Arguments

Indicated in documentation with `?` suffix:
```javascript
tp.date.now(format?: string, offset?: number, reference?: string)
```

**Usage Rules**:
1. Optional arguments can be omitted: `tp.date.now()` is valid
2. Optional arguments must follow order if partially used
3. Use `null` or `undefined` to skip an optional argument:
   ```javascript
   <% tp.date.now("YYYY-MM-DD", null, "2025-01-01") %>  // Skip offset, provide reference
   ```

#### Default Values

Some arguments have defaults (shown with `=` in docs):
```javascript
tp.file.creation_date(format: string = "YYYY-MM-DD HH:mm")
```

If omitted, the default value applies:
```javascript
<% tp.file.creation_date() %>  // Uses default: "YYYY-MM-DD HH:mm"
```

### Async/Await Syntax

> [!important]
> **Asynchronous Functions**
> Many Templater functions are [[Asynchronous]] and require the `await` keyword. These functions return [[Promises]] that must be resolved.

**Functions Requiring await**:
- `tp.file.create_new()`
- `tp.file.move()`
- `tp.file.rename()`
- `tp.file.include()`
- `tp.system.prompt()`
- `tp.system.suggester()`
- `tp.web` functions

**Correct Async Usage**:
```javascript
<%* 
const userInput = await tp.system.prompt("Enter name");
await tp.file.rename(userInput);
%>
```

**Incorrect (Will Error)**:
```javascript
<%* 
const userInput = tp.system.prompt("Enter name");  // Missing await!
tp.file.rename(userInput);  // Missing await!
%>
```

> [!warning]
> **Async in Interpolation vs Execution**
> Interpolation commands: `<% await tp.system.prompt("Name") %>`  
> Execution commands: `<%* const name = await tp.system.prompt("Name"); %>`
> 
> Both contexts support `await`, but execution commands require variable assignment to store the result.

---

## 📦 4. Internal Functions - Complete Reference

### tp.config Module

> [!definition]
> **tp.config**: Provides access to Templater's running configuration and plugin settings

#### Available Properties

```javascript
<% tp.config.template_file %>        // TFile object of current template
<% tp.config.target_file %>          // TFile object of file being modified
<% tp.config.run_mode %>             // Execution context (CREATE_NEW, APPEND, etc.)
<% tp.config.active_file %>          // Currently active file in editor
```

**Use Cases**:
- Detect whether template is creating new file vs appending to existing
- Access template metadata within the template itself
- Conditional logic based on execution context

---

### tp.date Module

> [!definition]
> **tp.date**: Complete date manipulation toolkit using [[Moment.js]] formatting

All date functions use [[Moment.js]] format strings. Reference: [Moment.js Format Documentation](https://momentjs.com/docs/#/displaying/format/)

#### tp.date.now()

**Signature**:
```javascript
tp.date.now(format?: string = "YYYY-MM-DD", offset?: number|string, reference?: string, reference_format?: string)
```

**Purpose**: Get current date with optional offset and custom reference point

**Arguments**:
- `format`: Output format (default: `"YYYY-MM-DD"`)
- `offset`: Days to add/subtract (number) or [[ISO 8601]] duration string
- `reference`: Use this date instead of today (string)
- `reference_format`: Format of the reference date

**Examples**:
```javascript
// Basic usage
<% tp.date.now() %>
// Output: 2025-11-13

// Custom format
<% tp.date.now("dddd, MMMM Do YYYY") %>
// Output: Thursday, November 13th 2025

// With numeric offset
<% tp.date.now("YYYY-MM-DD", -7) %>   // Last week
<% tp.date.now("YYYY-MM-DD", 14) %>   // Two weeks from now

// With ISO 8601 duration offset
<% tp.date.now("YYYY-MM-DD", "P-1M") %>   // Last month
<% tp.date.now("YYYY-MM-DD", "P1Y") %>    // Next year
<% tp.date.now("YYYY-MM-DD", "P-2W") %>   // Two weeks ago

// Using file title as reference (for Daily Notes)
<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>
// Tomorrow relative to filename date
```

> [!helpful-tip]
> **ISO 8601 Duration Format**
> Format: `P[n]Y[n]M[n]D` where P = Period, Y = Years, M = Months, D = Days
> - Negative durations: prefix with `-` (e.g., `P-1M`)
> - Examples: `P1Y2M3D` = 1 year, 2 months, 3 days

#### tp.date.tomorrow()

**Signature**:
```javascript
tp.date.tomorrow(format?: string = "YYYY-MM-DD")
```

**Purpose**: Get tomorrow's date

**Examples**:
```javascript
<% tp.date.tomorrow() %>
// Output: 2025-11-14

<% tp.date.tomorrow("dddd, MMMM Do") %>
// Output: Friday, November 14th
```

#### tp.date.yesterday()

**Signature**:
```javascript
tp.date.yesterday(format?: string = "YYYY-MM-DD")
```

**Purpose**: Get yesterday's date

**Examples**:
```javascript
<% tp.date.yesterday() %>
// Output: 2025-11-12

<% tp.date.yesterday("MMM DD, YYYY") %>
// Output: Nov 12, 2025
```

#### tp.date.weekday()

**Signature**:
```javascript
tp.date.weekday(format: string = "YYYY-MM-DD", weekday: number, reference?: string, reference_format?: string)
```

**Purpose**: Get specific weekday date relative to reference point

**Arguments**:
- `format`: Output format
- `weekday`: Day number (0 = Monday in most locales, adjust based on locale)
- `reference`: Reference date string
- `reference_format`: Format of reference date

**Examples**:
```javascript
// This week's Monday
<% tp.date.weekday("YYYY-MM-DD", 0) %>

// Next Monday
<% tp.date.weekday("YYYY-MM-DD", 7) %>

// Previous Monday from file title date
<% tp.date.weekday("YYYY-MM-DD", -7, tp.file.title, "YYYY-MM-DD") %>

// This Friday (if locale starts week on Monday, Friday = 4)
<% tp.date.weekday("dddd, MMM DD", 4) %>
```

#### Common Date Format Patterns

| Format String | Output Example | Description |
|---------------|----------------|-------------|
| `YYYY-MM-DD` | 2025-11-13 | ISO standard date |
| `DD/MM/YYYY` | 13/11/2025 | European format |
| `MM/DD/YYYY` | 11/13/2025 | US format |
| `MMMM Do, YYYY` | November 13th, 2025 | Long format with ordinal |
| `dddd` | Thursday | Full weekday name |
| `ddd` | Thu | Abbreviated weekday |
| `YYYY-MM-DD HH:mm` | 2025-11-13 14:30 | Date with time |
| `HH:mm:ss` | 14:30:45 | Time only |
| `YYYY-[W]WW` | 2025-W46 | ISO week number |

---

### tp.file Module

> [!definition]
> **tp.file**: Comprehensive file manipulation and metadata access

#### tp.file.content

**Type**: String property (not a function)

**Purpose**: Access the raw content of the current file at template execution time

**Examples**:
```javascript
// Display entire file content
<% tp.file.content %>

// Use in execution command for manipulation
<%*
const content = tp.file.content;
const wordCount = content.split(/\s+/).length;
tR += `Word count: ${wordCount}`;
%>
```

> [!warning]
> **Read-Only Property**
> Modifying `tp.file.content` does NOT update the file. Use `tp.app.vault.modify()` for actual file editing.

#### tp.file.create_new()

**Signature**:
```javascript
tp.file.create_new(template: TFile|string, filename?: string, open_new: boolean = false, folder?: TFolder|string)
```

**Purpose**: Programmatically create new files with template or content

**Arguments**:
- `template`: Either a TFile template object or raw content string
- `filename`: New filename (without `.md` extension)
- `open_new`: Whether to open the created file
- `folder`: Destination folder (TFolder object or path string)

**Examples**:
```javascript
// Create file with raw content
<%* await tp.file.create_new("# New Note\n\nContent here", "MyNewNote") %>

// Create file using another template
<%*
const template = tp.file.find_tfile("Templates/Project");
await tp.file.create_new(template, "Project Alpha");
%>

// Create and open immediately
<%* await tp.file.create_new("Content", "OpenMe", true) %>

// Create in specific folder (current file's folder)
<%* await tp.file.create_new("Content", "SameFolder", false, tp.file.folder(true)) %>

// Create in specific folder by path
<%* await tp.file.create_new("Content", "OrgNote", false, "Projects/Active") %>

// Create and link to new file
[[<% (await tp.file.create_new("Content", "LinkedNote")).basename %>]]
```

> [!warning]
> **Async Execution Order**
> If `open_new: true`, the file opens immediately while template continues executing. Subsequent commands may write to the NEW file, not the original! Use caution with this parameter.

#### tp.file.creation_date()

**Signature**:
```javascript
tp.file.creation_date(format: string = "YYYY-MM-DD HH:mm")
```

**Purpose**: Get file's filesystem creation date

**Examples**:
```javascript
<% tp.file.creation_date() %>
// Output: 2025-11-13 09:30

<% tp.file.creation_date("dddd Do MMMM YYYY HH:mm:ss") %>
// Output: Thursday 13th November 2025 09:30:45
```

#### tp.file.cursor()

**Signature**:
```javascript
tp.file.cursor(order?: number)
```

**Purpose**: Set cursor position after template insertion

**Arguments**:
- `order`: Jump sequence number (cursors activate in numerical order)

**Examples**:
```javascript
// Single cursor point
Title: <% tp.file.cursor() %>

// Multiple cursor points (jump order)
Name: <% tp.file.cursor(1) %>
Email: <% tp.file.cursor(2) %>
Phone: <% tp.file.cursor(3) %>

// Multi-cursor mode (same order number)
<% tp.file.cursor(1) %>Content between cursors<% tp.file.cursor(1) %>
```

**Navigation**: After insertion, use the configured hotkey (set in Obsidian Settings → Hotkeys → "Templater: Jump to next cursor position") to cycle through cursor positions.

#### tp.file.cursor_append()

**Signature**:
```javascript
tp.file.cursor_append(content: string)
```

**Purpose**: Append content at the current active cursor position

**Example**:
```javascript
<%* tp.file.cursor_append("Text inserted at cursor") %>
```

#### tp.file.exists()

**Signature**:
```javascript
tp.file.exists(filepath: string)
```

**Purpose**: Check if file exists at given path

**Arguments**:
- `filepath`: Vault-relative path including `.md` extension

**Examples**:
```javascript
<%* 
if (await tp.file.exists("Projects/Alpha.md")) {
    tR += "Project Alpha already exists!";
} else {
    await tp.file.create_new("# Alpha", "Projects/Alpha");
}
%>

// Check current file exists
<% await tp.file.exists(tp.file.folder(true) + "/" + tp.file.title + ".md") %>
```

#### tp.file.find_tfile()

**Signature**:
```javascript
tp.file.find_tfile(filename: string)
```

**Purpose**: Search vault for file and return [[TFile]] object

**Arguments**:
- `filename`: File basename (with or without `.md`)

**Examples**:
```javascript
// Get TFile object
<%* const myFile = tp.file.find_tfile("MyNote"); %>

// Access TFile properties
<% tp.file.find_tfile("MyTemplate").basename %>
<% tp.file.find_tfile("MyTemplate").extension %>
<% tp.file.find_tfile("MyTemplate").path %>

// Use with other functions
<%* await tp.file.include(tp.file.find_tfile("SharedContent")) %>
```

#### tp.file.folder()

**Signature**:
```javascript
tp.file.folder(absolute: boolean = false)
```

**Purpose**: Get current file's folder name

**Arguments**:
- `absolute`: If true, returns full vault path; if false, returns folder basename

**Examples**:
```javascript
// Just folder name
<% tp.file.folder() %>
// Output: Projects

// Full path
<% tp.file.folder(true) %>
// Output: Work/Active/Projects
```

#### tp.file.include()

**Signature**:
```javascript
tp.file.include(include_link: string|TFile)
```

**Purpose**: Include another file's content (templates process recursively)

**Arguments**:
- `include_link`: Wikilink string or TFile object; supports section/block references

**Examples**:
```javascript
// Include entire file
<% await tp.file.include("[[SharedHeader]]") %>

// Include with TFile object
<% await tp.file.include(tp.file.find_tfile("Footer")) %>

// Include specific section
<% await tp.file.include("[[LongDoc#Section Title]]") %>

// Include specific block
<% await tp.file.include("[[Research#^keyfindings]]") %>
```

> [!helpful-tip]
> **Recursive Template Processing**
> When you include a file that contains Templater commands, those commands execute as well. This enables modular, reusable template components.

#### tp.file.last_modified_date()

**Signature**:
```javascript
tp.file.last_modified_date(format: string = "YYYY-MM-DD HH:mm")
```

**Purpose**: Get file's last modification timestamp

**Examples**:
```javascript
<% tp.file.last_modified_date() %>
// Output: 2025-11-13 14:45

<% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
// Output: Thursday 13th November 2025 14:45:30
```

#### tp.file.move()

**Signature**:
```javascript
tp.file.move(new_path: string, file_to_move?: TFile)
```

**Purpose**: Move/rename file to new vault location

**Arguments**:
- `new_path`: New vault-relative path (WITHOUT `.md` extension)
- `file_to_move`: File to move (defaults to current file)

**Examples**:
```javascript
// Move current file to different folder
<%* await tp.file.move("/Archive/" + tp.file.title) %>

// Move AND rename
<%* await tp.file.move("/Projects/Active/ProjectAlpha") %>

// Conditional file organization
<%*
if (tp.file.title.startsWith("Daily-")) {
    await tp.file.move("/Journal/Daily/" + tp.file.title);
} else {
    await tp.file.move("/Notes/" + tp.file.title);
}
%>
```

#### tp.file.path()

**Signature**:
```javascript
tp.file.path(relative: boolean = false)
```

**Purpose**: Get file's path

**Arguments**:
- `relative`: If true, returns vault-relative path; if false, returns absolute system path

**Examples**:
```javascript
// Vault-relative path
<% tp.file.path(true) %>
// Output: Work/Projects/Alpha.md

// Absolute system path
<% tp.file.path() %>
// Output: /Users/name/Documents/Vault/Work/Projects/Alpha.md
```

#### tp.file.rename()

**Signature**:
```javascript
tp.file.rename(new_title: string)
```

**Purpose**: Rename current file (preserves extension and location)

**Examples**:
```javascript
// Simple rename
<%* await tp.file.rename("NewFileName") %>

// Programmatic rename
<%*
const timestamp = tp.date.now("YYYYMMDDHHmm");
await tp.file.rename(tp.file.title + "-" + timestamp);
%>

// Interactive rename
<%*
const newName = await tp.system.prompt("Enter new filename");
if (newName) {
    await tp.file.rename(newName);
}
%>
```

#### tp.file.selection()

**Signature**:
```javascript
tp.file.selection()
```

**Purpose**: Get currently selected text in editor

**Examples**:
```javascript
// Wrap selection in bold
**<% tp.file.selection() %>**

// Transform selection
<%*
const selected = tp.file.selection();
tR += selected.toUpperCase();
%>
```

**Use Case**: Create templates that manipulate highlighted text (e.g., formatting, transformation, analysis)

#### tp.file.tags

**Type**: Array property (not a function)

**Purpose**: Access file's tags as array of strings

**Examples**:
```javascript
// Display all tags
<% tp.file.tags %>
// Output: #project,#active,#review

// Check for specific tag
<%*
if (tp.file.tags.includes("#project")) {
    tR += "This is a project file!";
}
%>

// Tag-based conditional content
<%*
if (tp.file.tags.some(tag => tag.startsWith("#urgent"))) {
    tR += "⚠️ URGENT: ";
}
%>
```

#### tp.file.title

**Type**: String property (not a function)

**Purpose**: Get file's title (basename without extension)

**Examples**:
```javascript
// Display title
<% tp.file.title %>

// Parse title components
<% tp.file.title.split(" ")[0] %>  // First word
<% tp.file.title.substring(11) %>  // Remove YYYY-MM-DD prefix

// Use in logic
<%*
if (tp.file.title.startsWith("Draft")) {
    tR += "🚧 Work in Progress";
}
%>
```

---

### tp.frontmatter Module

> [!definition]
> **tp.frontmatter**: Access [[YAML]] frontmatter values from current file

#### Accessing Frontmatter Values

**Syntax**: `tp.frontmatter.<key>` where `<key>` is the frontmatter property name

**Examples**:
```yaml
---
title: My Document
author: John Doe
tags: [work, project]
priority: high
created: 2025-11-13
---
```

```javascript
// Access simple properties
<% tp.frontmatter.title %>       // My Document
<% tp.frontmatter.author %>      // John Doe
<% tp.frontmatter.priority %>    // high

// Access array properties
<% tp.frontmatter.tags %>              // work,project
<% tp.frontmatter.tags[0] %>           // work
<% tp.frontmatter.tags.join(", ") %>   // work, project

// Properties with spaces (use bracket notation)
<% tp.frontmatter["created date"] %>
```

> [!warning]
> **Execution Order Limitation**
> Due to bottom-to-top execution, `tp.frontmatter` cannot access frontmatter values SET by Templater commands in the same template execution. Frontmatter must exist BEFORE template runs, or use [[#tp.hooks.on_all_templates_executed()]] for post-processing.

**Advanced Array Manipulation**:
```javascript
<%*
// Get all tags as formatted list
const tagList = tp.frontmatter.tags
    .map(tag => `- ${tag}`)
    .join("\n");
tR += tagList;
%>

// Filter frontmatter arrays
<%*
const urgentItems = tp.frontmatter.tasks
    .filter(task => task.priority === "urgent");
tR += urgentItems.length + " urgent tasks";
%>
```

---

### tp.system Module

> [!definition]
> **tp.system**: User interaction and system integration functions

#### tp.system.clipboard()

**Signature**:
```javascript
tp.system.clipboard()
```

**Purpose**: Get current clipboard contents

**Examples**:
```javascript
// Insert clipboard content
Pasted: <% tp.system.clipboard() %>

// Transform clipboard data
<%*
const clipContent = tp.system.clipboard();
tR += `> ${clipContent}`;  // Convert to blockquote
%>
```

#### tp.system.prompt()

**Signature**:
```javascript
tp.system.prompt(prompt_text?: string, default_value?: string, throw_on_cancel: boolean = false, multiline?: boolean = false)
```

**Purpose**: Display text input modal to user

**Arguments**:
- `prompt_text`: Question/label shown to user
- `default_value`: Pre-filled value in input field
- `throw_on_cancel`: If true, throws error when user cancels (stops execution)
- `multiline`: If true, shows textarea instead of single-line input

**Examples**:
```javascript
// Basic prompt
<% await tp.system.prompt("Enter title") %>

// With default value
<% await tp.system.prompt("Your name?", "John Doe") %>

// Multiline input
<%* 
const description = await tp.system.prompt(
    "Enter description", 
    null, 
    false, 
    true
);
%>

// Reuse value multiple times
<%*
let projectName = await tp.system.prompt("Project name");
await tp.file.rename(projectName);
%>
# <% projectName %>
Project: **<% projectName %>**
```

> [!helpful-tip]
> **Cancel Behavior**
> By default, canceling a prompt returns `null`. Set `throw_on_cancel: true` to halt template execution on cancel—useful for required inputs.

#### tp.system.suggester()

**Signature**:
```javascript
tp.system.suggester(text_items: string[]|((item: T) => string), items: T[], throw_on_cancel: boolean = false, placeholder: string = "", limit?: number)
```

**Purpose**: Display searchable dropdown menu; return selected item

**Arguments**:
- `text_items`: Array of display strings OR mapping function
- `items`: Array of actual values (same length as text_items)
- `throw_on_cancel`: Throw error on cancel
- `placeholder`: Placeholder text in search box
- `limit`: Max items rendered simultaneously (performance optimization)

**Examples**:
```javascript
// Simple suggester (text and values identical)
<% await tp.system.suggester(
    ["Option A", "Option B", "Option C"],
    ["Option A", "Option B", "Option C"]
) %>

// With mapping function (cleaner syntax when identical)
<% await tp.system.suggester(
    item => item,
    ["Happy", "Sad", "Excited"]
) %>

// Different display vs return values
<%*
const priorities = await tp.system.suggester(
    ["🔥 Urgent", "⚡ High", "📋 Normal", "📦 Low"],
    ["urgent", "high", "normal", "low"]
);
%>
Priority: <% priorities %>

// File suggester
<%*
const selectedFile = await tp.system.suggester(
    item => item.basename,
    tp.app.vault.getMarkdownFiles()
);
%>
[[<% selectedFile.basename %>]]

// Tag suggester
<%*
const allTags = Object.keys(tp.app.metadataCache.getTags())
    .map(tag => tag.replace("#", ""));
const selectedTag = await tp.system.suggester(
    item => item,
    allTags
);
%>
#<% selectedTag %>

// With placeholder and limit
<%*
const choice = await tp.system.suggester(
    item => item.name,
    largeDataArray,
    false,
    "Type to search...",
    50  // Only render 50 items at once
);
%>
```

> [!use-cases-and-examples]
> **Real-World Use Cases**
> 1. **Project Template Selector**: Let user choose project type from predefined list
> 2. **Link Existing File**: Select from all vault files to create link
> 3. **Tag Assignment**: Choose from existing tags for consistency
> 4. **Template Variants**: Pick specific template variation before proceeding

#### tp.system.multi_suggester()

**Signature**:
```javascript
tp.system.multi_suggester(text_items: string[]|((item: T) => string), items: T[], throw_on_cancel: boolean = false, title: string = "", limit?: number)
```

**Purpose**: Like suggester but allows multiple selections

**Returns**: Array of selected items

**Examples**:
```javascript
// Select multiple moods
<%*
const moods = await tp.system.multi_suggester(
    ["😊 Happy", "😢 Sad", "😕 Confused", "😠 Angry"],
    ["happy", "sad", "confused", "angry"]
);
%>
Moods: <% moods.join(", ") %>

// Select multiple files
<%*
const selectedFiles = await tp.system.multi_suggester(
    item => item.basename,
    tp.app.vault.getMarkdownFiles(),
    false,
    "Select related files"
);

const links = selectedFiles
    .map(f => `- [[${f.basename}]]`)
    .join("\n");
%>
## Related Files
<% links %>

// Tag multi-select
<%*
const allTags = Object.keys(tp.app.metadataCache.getTags())
    .map(x => x.replace("#", ""));
const selectedTags = await tp.system.multi_suggester(
    item => item,
    allTags
);
%>
tags: [<% selectedTags.join(", ") %>]
```

---

### tp.web Module

> [!definition]
> **tp.web**: Web API integration for external data fetching

#### tp.web.daily_quote()

**Signature**:
```javascript
tp.web.daily_quote()
```

**Purpose**: Fetch random inspirational quote from quotes.rest API

**Example**:
```javascript
<% tp.web.daily_quote() %>
// Output: 
// > Do the best you can until you know better. Then when you know better, do better.
// > — Maya Angelou
```

> [!helpful-tip]
> **Quote Formatting**
> The quote returns as formatted [[Markdown]] blockquote with attribution. Perfect for [[Daily Notes]] motivation sections.

#### tp.web.random_picture()

**Signature**:
```javascript
tp.web.random_picture(size?: string, query?: string, include_size?: boolean)
```

**Purpose**: Fetch random image from Unsplash API

**Arguments**:
- `size`: Dimensions (e.g., "1920x1080")
- `query`: Search term for specific images
- `include_size`: Include size parameter in URL

**Example**:
```javascript
<% tp.web.random_picture("800x600", "nature") %>
```

---

### tp.obsidian Module

> [!definition]
> **tp.obsidian**: Direct access to [[Obsidian API]] classes and utilities

This module exposes Obsidian's native API for advanced manipulation beyond Templater's built-in functions.

#### Common API Access Patterns

```javascript
// Normalize file path
<% tp.obsidian.normalizePath("Path//to///file.md") %>
// Output: Path/to/file.md

// Convert HTML to Markdown
<% tp.obsidian.htmlToMarkdown("<h1>Title</h1><p>Content</p>") %>
// Output: # Title\n\nContent

// Get all folders
<%*
const folders = tp.app.vault.getAllLoadedFiles()
    .filter(x => x instanceof tp.obsidian.TFolder)
    .map(x => x.name);
tR += folders.join("\n");
%>

// HTTP request
<%*
const response = await tp.obsidian.requestUrl("https://api.example.com/data");
const data = response.json;
tR += data.title;
%>
```

> [!warning]
> **Advanced API Usage**
> tp.obsidian provides low-level API access. Always consult [Obsidian API Type Definitions](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts) for detailed documentation.

---

### tp.app Module

> [!definition]
> **tp.app**: Full [[Obsidian API]] app instance for complete vault control

`tp.app` provides access to the entire Obsidian application object, enabling deep integration with vault internals.

#### Key Sub-Objects

**tp.app.vault**: File system operations
```javascript
// Get all Markdown files
<%* 
const allFiles = tp.app.vault.getMarkdownFiles();
%>

// Read file content
<%*
const file = tp.file.find_tfile("MyNote");
const content = await tp.app.vault.read(file);
%>

// Modify file content
<%*
const file = tp.file.find_tfile("Target");
const newContent = "Updated content";
await tp.app.vault.modify(file, newContent);
%>

// Delete file
<%*
const file = tp.file.find_tfile("ToDelete");
await tp.app.vault.delete(file);
%>
```

**tp.app.workspace**: Editor and UI interaction
```javascript
// Get active file
<%*
const activeFile = tp.app.workspace.getActiveFile();
%>

// Get last active file (useful for "back" links)
<%*
const lastFile = tp.app.workspace.lastActiveFile;
%>

// Get recently opened files
<%*
const recentFiles = tp.app.workspace.getLastOpenFiles();
%>
```

**tp.app.fileManager**: Advanced file operations
```javascript
// Update frontmatter programmatically
<%*
const file = tp.file.find_tfile("MyNote");
await tp.app.fileManager.processFrontMatter(file, (frontmatter) => {
    frontmatter["status"] = "complete";
    frontmatter["updated"] = tp.date.now();
});
%>

// Generate Markdown link
<%*
const targetFile = tp.file.find_tfile("Target");
const link = tp.app.fileManager.generateMarkdownLink(
    targetFile,
    tp.file.folder(true)
);
tR += link;
%>
```

**tp.app.metadataCache**: Query vault metadata
```javascript
// Get file cache (frontmatter, links, tags)
<%*
const file = tp.file.find_tfile("MyNote");
const cache = tp.app.metadataCache.getFileCache(file);
const frontmatter = cache?.frontmatter;
%>

// Get all tags in vault
<%*
const allTags = tp.app.metadataCache.getTags();
const tagList = Object.keys(allTags).join(", ");
%>
```

---

### tp.hooks Module

> [!definition]
> **tp.hooks**: Lifecycle event handlers for post-execution tasks

#### tp.hooks.on_all_templates_executed()

**Signature**:
```javascript
tp.hooks.on_all_templates_executed(callback_function)
```

**Purpose**: Execute callback AFTER all templates finish processing

**Use Cases**:
- Update frontmatter after template content is generated
- Run commands from other plugins (e.g., [[Linter]])
- Perform cleanup or validation tasks

**Examples**:
```javascript
// Update frontmatter after template completes
<%*
tp.hooks.on_all_templates_executed(async () => {
    const file = tp.file.find_tfile(tp.file.path(true));
    await tp.app.fileManager.processFrontMatter(file, (fm) => {
        fm["last_templated"] = tp.date.now();
        fm["template_version"] = "2.0";
    });
});
%>

// Run Linter plugin after template
<%*
tp.hooks.on_all_templates_executed(() => {
    tp.app.commands.executeCommandById("obsidian-linter:lint-file");
});
%>

// Complex post-processing
<%*
tp.hooks.on_all_templates_executed(async () => {
    // Update related files
    const relatedFiles = tp.frontmatter.related || [];
    for (const filename of relatedFiles) {
        const file = tp.file.find_tfile(filename);
        if (file) {
            await tp.app.fileManager.processFrontMatter(file, (fm) => {
                if (!fm.backlinks) fm.backlinks = [];
                fm.backlinks.push(tp.file.title);
            });
        }
    }
});
%>
```

> [!warning]
> **Execution Context**
> Hooks execute AFTER template insertion completes. They cannot modify the template output itself, only perform side effects like file manipulation or API calls.

---

## 🎨 5. Command Types & Execution Modes

### Whitespace Control

> [!definition]
> **Whitespace Control**: Syntax utilities to manage newlines and spacing around commands

Execution commands (`<%*`) produce blank lines by default since they don't output content. Whitespace control removes these unwanted spaces.

#### Trim Newline After Command (`-%>`)

**Syntax**: Add `-` before closing `%>`

**Effect**: Removes ONE newline immediately after the command

**Example Without Whitespace Control**:
```markdown
<%* if (tp.file.title == "Test") { %>
This is a test file!
<%* } else { %>
This is NOT a test file!
<%* } %>
Some content below.
```

**Output** (notice blank lines):
```markdown

This is NOT a test file!

Some content below.
```

**Example With Whitespace Control**:
```markdown
<%* if (tp.file.title == "Test") { -%>
This is a test file!
<%* } else { -%>
This is NOT a test file!
<%* } -%>
Some content below.
```

**Output** (clean):
```markdown
This is NOT a test file!
Some content below.
```

#### Trim All Whitespace Before Command (`<%_`)

**Syntax**: Add `_` after opening `<%`

**Effect**: Removes all whitespace (spaces, tabs, newlines) before the command

**Example**:
```markdown
Title:    <%_ tp.file.title %>
```

**Output**:
```markdown
Title:MyFileName
```

#### Trim All Whitespace After Command (`_%>`)

**Syntax**: Add `_` before closing `%>`

**Effect**: Removes all whitespace after the command

**Example**:
```markdown
<% tp.date.now() _%>    Extra spaces removed
```

**Output**:
```markdown
2025-11-13Extra spaces removed
```

#### Combined Whitespace Control

```markdown
<%_ tp.file.title _%>
```
Removes all whitespace before AND after the command.

> [!helpful-tip]
> **Best Practice for Conditional Blocks**
> Always use `-%>` on execution command closing tags within if/else blocks to prevent blank line accumulation:
> ```javascript
> <%* if (condition) { -%>
> Content
> <%* } else { -%>
> Other content
> <%* } -%>
> ```

---

### Dynamic Commands (DEPRECATED)

> [!warning]
> **Dynamic Commands Are Deprecated**
> As of Templater v2.0+, dynamic commands (`<%+`) are no longer actively maintained. Use [[dataview]] plugin for live-updating content instead.

**Original Purpose**: Commands that re-execute in preview mode

**Syntax**: `<%+ expression %>`

**Example** (no longer recommended):
```markdown
Last modified: <%+ tp.file.last_modified_date() %>
```

**Why Deprecated**:
- Caching issues prevent reliable updates
- Performance problems with large vaults
- Better alternatives exist ([[dataview]], [[Tracker]])

**Modern Alternative**:
Use Dataview inline queries for live-updating metadata:
```markdown
Last modified: `= this.file.mtime`
```

---

### Execution Command Output Control

#### The tR Variable

> [!core-principle]
> **Template Result (tR)**
> All Templater output accumulates in the `tR` string variable. In interpolation commands, `tR` is managed automatically. In execution commands, YOU control `tR` explicitly.

**Append to Output**:
```javascript
<%*
tR += "This text will appear in the note.";
tR += "\n\nAnother paragraph.";
%>
```

**Overwrite Output (Clear Previous Content)**:
```javascript
<%*
// This clears everything Templater generated up to this point
tR = "";
// Now only THIS content will appear
tR += "Fresh start!";
%>
```

> [!use-cases-and-examples]
> **Use Case: Template Frontmatter Exclusion**
> Templates often contain frontmatter you don't want in the final note:
> 
> ```yaml
> ---
> type: template
> category: daily-note
> ---
> This is my template description.
> 
> <%* tR = "" -%>
> ---
> type: daily-note
> date: <% tp.date.now() %>
> ---
> 
> # Daily Note
> ```
> 
> The `tR = ""` clears the template's own frontmatter/description, so only content AFTER that line appears in the created note.

---

## 🔧 6. User Functions & Custom Scripts

### User Functions Overview

> [!definition]
> **User Functions**: Custom functions you define to extend Templater's capabilities beyond built-in functions

Two types of user functions:
1. **Script User Functions**: [[JavaScript]] files that export functions
2. **System User Functions**: Shell commands that return output

### Script User Functions

#### Setup Process

> [!methodology-and-sources]
> **Creating Your First Script User Function**
> 
> 1. Create a folder for scripts in your vault (e.g., `Scripts/`)
> 2. Configure Templater: Settings → Templater → Script files folder location → Select your `Scripts` folder
> 3. Create `.js` files in the scripts folder (must be created outside Obsidian using text editor)
> 4. Write functions following [[CommonJS]] module syntax
> 5. Reload Obsidian or restart to load scripts
> 6. Invoke in templates via `tp.user.<script_filename>()`

#### Basic Script Structure

**File**: `Scripts/myFunction.js`
```javascript
function myFunction(message) {
    return `Message from script: ${message}`;
}

module.exports = myFunction;
```

**Usage in Template**:
```markdown
<% tp.user.myFunction("Hello World") %>
```

**Output**:
```markdown
Message from script: Hello World
```

#### Accessing Templater Functions in Scripts

Scripts don't have automatic access to `tp` or `tR`. You must pass them as arguments.

**Script with tp Access**: `Scripts/advancedScript.js`
```javascript
function advancedScript(tp) {
    const title = tp.file.title;
    const date = tp.date.now("YYYY-MM-DD");
    return `# ${title}\nCreated: ${date}`;
}

module.exports = advancedScript;
```

**Template Usage**:
```markdown
<% tp.user.advancedScript(tp) %>
```

#### Async User Functions

For functions requiring `await` (API calls, file operations):

**Script**: `Scripts/fetchData.js`
```javascript
async function fetchData(tp, apiUrl) {
    const response = await tp.obsidian.requestUrl(apiUrl);
    const data = response.json;
    return `Fetched: ${data.title}`;
}

module.exports = fetchData;
```

**Template Usage**:
```markdown
<% await tp.user.fetchData(tp, "https://api.example.com/data") %>
```

#### Complex Script Example

**Script**: `Scripts/processDaily.js`
```javascript
async function processDaily(tp) {
    // Get today's date
    const today = tp.date.now("YYYY-MM-DD");
    
    // Find all files created today
    const todayFiles = tp.app.vault.getMarkdownFiles().filter(file => {
        const cache = tp.app.metadataCache.getFileCache(file);
        return cache?.frontmatter?.created === today;
    });
    
    // Generate links
    const links = todayFiles
        .map(f => `- [[${f.basename}]]`)
        .join("\n");
    
    return `## Files Created Today\n${links}`;
}

module.exports = processDaily;
```

**Template Usage**:
```markdown
<% await tp.user.processDaily(tp) %>
```

#### TSDoc Documentation for Intellisense

Add [[TSDoc]] comments for better IDE support:

**Script**: `Scripts/documentedFunction.js`
```javascript
/**
 * Creates a formatted project header
 * @param {Object} tp - The Templater object
 * @param {string} projectName - Name of the project
 * @param {string} status - Project status (active|archived|planning)
 * @returns {string} Formatted project header
 */
function createProjectHeader(tp, projectName, status) {
    const icon = status === 'active' ? '🚀' : 
                 status === 'archived' ? '📦' : '📋';
    
    return `${icon} **${projectName}** | Status: ${status}`;
}

module.exports = createProjectHeader;
```

> [!helpful-tip]
> **Script Troubleshooting**
> If scripts don't load:
> 1. Verify `.js` extension (not `.js.md`)
> 2. Check file was created outside Obsidian
> 3. Ensure proper `module.exports` syntax
> 4. Reload Obsidian after creating/editing scripts
> 5. Check console (Ctrl+Shift+I) for JavaScript errors

---

### System User Functions

> [!definition]
> **System User Functions**: Execute shell commands and capture their output

**Security Warning**: System commands can execute arbitrary code. Only run trusted commands.

#### Configuration

Settings → Templater → System User Functions → Add New User Function
- **Function Name**: What you'll type in templates
- **System Command**: Shell command to execute
- **Operating System**: Platform this command works on

#### Basic Example

**Configuration**:
- Name: `getCurrentUser`
- Command: `whoami` (Linux/Mac) or `echo %USERNAME%` (Windows)

**Template Usage**:
```markdown
Current user: <% tp.user.getCurrentUser() %>
```

#### Passing Arguments to System Commands

Arguments passed as [[Environment Variables]].

**Configuration**:
- Name: `echo`
- Command: `echo $MY_VARIABLE` (Linux/Mac) or `echo %MY_VARIABLE%` (Windows)

**Template Usage**:
```javascript
<% tp.user.echo({MY_VARIABLE: "Hello from template"}) %>
```

**Arguments Syntax**: Single JavaScript object with property names matching environment variable names.

#### Advanced System Command Example

**Configuration**:
- Name: `gitStatus`
- Command: `cd "$VAULT_PATH" && git status --short`

**Template Usage**:
```javascript
<%*
const vaultPath = tp.app.vault.adapter.basePath;
const status = tp.user.gitStatus({VAULT_PATH: vaultPath});
%>
```git-status
<% status %>
```
```

---

## 🚀 7. Advanced Patterns & Workflows

### Conditional Content Generation

#### Single Condition

```javascript
<%* if (tp.file.title.startsWith("Daily")) { -%>
## Daily Log
- Morning routine
- Work tasks
- Evening reflection
<%* } -%>
```

#### If-Else

```javascript
<%* if (tp.frontmatter.status === "complete") { -%>
✅ **Status**: Complete
<%* } else { -%>
⏳ **Status**: In Progress
<%* } -%>
```

#### Multiple Conditions

```javascript
<%* 
const priority = tp.frontmatter.priority;
if (priority === "urgent") {
    tR += "🔥 **URGENT**\n";
} else if (priority === "high") {
    tR += "⚡ **High Priority**\n";
} else if (priority === "normal") {
    tR += "📋 **Normal**\n";
} else {
    tR += "📦 **Low Priority**\n";
}
-%>
```

#### Switch Statement

```javascript
<%*
switch(tp.frontmatter.type) {
    case "project":
        tR += "## Project Tasks\n- [ ] Task 1\n";
        break;
    case "meeting":
        tR += "## Meeting Notes\n**Attendees**:\n";
        break;
    case "research":
        tR += "## Research Findings\n**Sources**:\n";
        break;
    default:
        tR += "## General Notes\n";
}
-%>
```

### Loops and Iteration

#### For Loop

```javascript
<%*
for (let i = 1; i <= 5; i++) {
    tR += `${i}. Item ${i}\n`;
}
-%>
```

#### Array Iteration

```javascript
<%*
const tags = ["project", "active", "review"];
for (const tag of tags) {
    tR += `- #${tag}\n`;
}
-%>
```

#### Map Transformation

```javascript
<%*
const files = tp.app.vault.getMarkdownFiles()
    .filter(f => f.basename.startsWith("Project"))
    .map(f => `- [[${f.basename}]]`)
    .join("\n");
tR += files;
-%>
```

### File Creation Workflows

#### Create Multiple Related Files

```javascript
<%*
const projectName = await tp.system.prompt("Project name");
const phases = ["Planning", "Execution", "Review"];

for (const phase of phases) {
    const filename = `${projectName} - ${phase}`;
    const content = `# ${filename}\n\nStatus: Not Started`;
    await tp.file.create_new(content, filename, false, "Projects");
}

tR += `Created ${phases.length} project files for ${projectName}`;
-%>
```

#### Conditional File Creation

```javascript
<%*
const dailyPath = `Journal/Daily/${tp.date.now("YYYY-MM-DD")}`;

if (!await tp.file.exists(dailyPath + ".md")) {
    const template = tp.file.find_tfile("Templates/Daily");
    await tp.file.create_new(template, tp.date.now("YYYY-MM-DD"), false, "Journal/Daily");
    tR += "✅ Created today's daily note";
} else {
    tR += "ℹ️ Daily note already exists";
}
-%>
```

### Interactive Template Builder

```javascript
<%*
// Gather user input
const noteType = await tp.system.suggester(
    ["📝 Meeting", "🚀 Project", "📚 Research", "💡 Idea"],
    ["meeting", "project", "research", "idea"]
);
const title = await tp.system.prompt("Note title");
const priority = await tp.system.suggester(
    ["🔥 Urgent", "⚡ High", "📋 Normal", "📦 Low"],
    ["urgent", "high", "normal", "low"]
);
// Build frontmatter
tR = `---
title: ${title}
type: ${noteType}
priority: ${priority}
created: ${tp.date.now()}
---
`;
// Type-specific content
if (noteType === "meeting") {
    tR += `## Meeting Details
**Date**: ${tp.date.now("YYYY-MM-DD")}
**Attendees**: 
**Agenda**: 
## Notes
## Action Items
- [ ] `;
} else if (noteType === "project") {
    tR += `## Project Overview
## Goals
## Tasks
- [ ] 
## Timeline`;
} else if (noteType === "research") {
    tR += `## Research Question
## Sources
## Findings
## Conclusions`;
} else {
    tR += `## Idea
## Context
## Next Steps`;
}
-%>
```

### Automated File Organization

```javascript
<%*
// Auto-organize based on tags and date
const tags = tp.file.tags;
const date = tp.date.now("YYYY-MM");
let targetFolder = "Notes/Unsorted";
if (tags.includes("#project")) {
    targetFolder = `Projects/${date}`;
} else if (tags.includes("#meeting")) {
    targetFolder = `Meetings/${date}`;
} else if (tags.includes("#daily")) {
    targetFolder = `Journal/Daily/${tp.date.now("YYYY")}`;
}
// Move file to organized location
await tp.file.move(`${targetFolder}/${tp.file.title}`);
tR += `📁 Organized to: ${targetFolder}`;
-%>
```

### Advanced Frontmatter Management

```javascript
<%*
// Template with dynamic frontmatter generation
const title = await tp.system.prompt("Title");
const tags = await tp.system.multi_suggester(
    item => item,
    ["work", "personal", "urgent", "review", "reference"]
);
// Calculate derived values
const fileId = tp.date.now("YYYYMMDDHHmmss");
const weekNumber = tp.date.now("YYYY-[W]WW");
tR = `---
id: ${fileId}
title: ${title}
tags: [${tags.join(", ")}]
created: ${tp.date.now()}
week: ${weekNumber}
status: draft
---
# ${title}
`;
-%>
```

---

## 🔗 8. Integration with Obsidian Ecosystem

### Templater + Dataview

Combine Templater's creation power with [[dataview]]'s querying capability.

**Template Creates Structure, Dataview Fills Content**:
```markdown
---
type: project-dashboard
---

# Project Dashboard

<%* tR += `Last updated: ${tp.date.now("YYYY-MM-DD HH:mm")}\n\n` -%>

## Active Projects
​```dataview
TABLE status, priority, due
FROM "Projects"
WHERE status = "active"
SORT priority ASC, due ASC
​```

## Completed This Week
​```dataview
LIST
FROM "Projects"
WHERE status = "complete" 
AND file.mtime >= date(this.week)
​```
```

### Templater + Calendar Plugin

Auto-create [[Daily Notes]] with rich templates when clicking calendar dates.

**Configuration**:
1. Install Calendar plugin
2. Set Calendar's "New file location" to match Templater's folder template for `Journal/Daily/`
3. Create template: `Templates/Daily/daily-note.md`

**Template**:
```markdown
---
date: <% tp.date.now("YYYY-MM-DD") %>
weekday: <% tp.date.now("dddd") %>
week: <% tp.date.now("[W]WW") %>
---

# <% tp.date.now("dddd, MMMM Do YYYY") %>

## 🌅 Morning
- [ ] Morning routine

## 💼 Work Focus

## 📝 Notes

## 🌙 Evening
- [ ] Evening reflection

---
[[<% tp.date.yesterday("YYYY-MM-DD") %>|← Yesterday]] | [[<% tp.date.tomorrow("YYYY-MM-DD") %>|Tomorrow →]]
```

### Templater + QuickAdd

[[component-exemplar-quickadd-plugin-documentation-v1.0.0-20251119225738]] provides macro automation that can trigger Templater templates with pre-filled data.

**Use Case**: Create meeting notes via single command with participant auto-fill.

**QuickAdd Macro**:
```javascript
module.exports = async (params) => {
    const {quickAddApi: qa} = params;
    
    const participants = await qa.suggester(
        ["Team A", "Team B", "Team C"],
        [
            ["Alice", "Bob"],
            ["Carol", "Dave"],
            ["Eve", "Frank"]
        ]
    );
    
    qa.variables = {
        participants: participants.join(", "),
        date: window.moment().format("YYYY-MM-DD")
    };
    
    // Trigger Templater template with these variables
};
```

### Templater + Natural Language Dates

Use [[Natural Language Dates]] for more flexible date input.

**Example**:
```javascript
<%*
// User enters "next monday" or "in 2 weeks"
const dateInput = await tp.system.prompt("Enter date (natural language)");

// Process with NLP plugin (if installed)
const processedDate = window.moment(dateInput, "YYYY-MM-DD").format("YYYY-MM-DD");

tR += `Due date: ${processedDate}`;
-%>
```

### Templater + Tasks Plugin

Auto-generate task lists with dates and recurrence.

```markdown
<%*
const taskName = await tp.system.prompt("Task name");
const due = tp.date.now("YYYY-MM-DD", 7); // Due in 7 days
%>

## Tasks
- [ ] <% taskName %> 📅 <% due %>
```

---

## ⚠️ 9. Troubleshooting & Best Practices

### Common Errors & Solutions

#### Error: "Template couldn't be found"

**Cause**: Template file not in configured template folder

**Solution**:
1. Verify Settings → Templater → Template folder location is correct
2. Ensure template file is in that folder or subfolder
3. Check spelling of template name

#### Error: "Cannot read property X of undefined"

**Cause**: Accessing property that doesn't exist (often frontmatter)

**Solution**:
```javascript
// Bad
<% tp.frontmatter.nonexistent_property %>

// Good (check existence first)
<%* 
if (tp.frontmatter.property) {
    tR += tp.frontmatter.property;
} else {
    tR += "Property not set";
}
-%>
```

#### Error: "await is only valid in async function"

**Cause**: Using `await` without `async` context

**Solution**: Use execution commands for async operations:
```javascript
// Bad
<% await tp.system.prompt("Name") %>

// Good
<%* const name = await tp.system.prompt("Name"); %>
<% name %>
```

#### Error: "SyntaxError: Unexpected token"

**Cause**: JavaScript syntax error in execution command

**Solution**:
- Check for missing brackets, quotes, parentheses
- Validate JavaScript syntax in external editor first
- Use browser console (Ctrl+Shift+I) to see full error details

#### Frontmatter Values Not Available

**Cause**: Bottom-to-top execution order

**Solution**: Use hooks for frontmatter manipulation:
```javascript
<%*
tp.hooks.on_all_templates_executed(async () => {
    const file = tp.file.find_tfile(tp.file.path(true));
    await tp.app.fileManager.processFrontMatter(file, (fm) => {
        fm["processed"] = true;
    });
});
%>
```

### Performance Optimization

> [!helpful-tip]
> **Optimize Large Template Execution**
> 
> 1. **Minimize file searches**: Cache `tp.file.find_tfile()` results
> 2. **Batch operations**: Process arrays once rather than in separate loops
> 3. **Use suggester limits**: `limit` parameter prevents rendering thousands of items
> 4. **Avoid redundant API calls**: Store values in variables
> 5. **Defer non-critical tasks**: Use hooks for background processing

**Example - Before Optimization**:
```javascript
<%*
for (let i = 0; i < 100; i++) {
    const file = tp.file.find_tfile("Template"); // SLOW: 100 file searches
    tR += file.basename;
}
%>
```

**Example - After Optimization**:
```javascript
<%*
const file = tp.file.find_tfile("Template"); // FAST: 1 file search
for (let i = 0; i < 100; i++) {
    tR += file.basename;
}
%>
```

### Security Best Practices

> [!warning]
> **Security Considerations**
> 
> 1. **Never run untrusted templates**: Templater executes arbitrary JavaScript
> 2. **Audit system commands**: System user functions can access your entire system
> 3. **Validate user input**: Sanitize prompts before file operations
> 4. **Review community templates**: Check code before using shared templates
> 5. **Backup regularly**: Complex templates can modify many files

### Template Organization

**Recommended Structure**:
```
📁 Templates/
├── 📁 Daily/
│   ├── daily-note.md
│   └── weekly-review.md
├── 📁 Projects/
│   ├── project-template.md
│   └── sprint-planning.md
├── 📁 Meta/
│   ├── person.md
│   └── meeting.md
├── 📁 Snippets/
│   ├── header-block.md
│   └── task-section.md
└── 📁 Components/
    ├── shared-header.md
    └── common-footer.md
```

**Naming Conventions**:
- Prefix templates by use context: `ff-filename` (full file), `ss-snippet` (snippet)
- Use descriptive names: `project-kickoff` not `template1`
- Group related templates in subfolders

### Testing Templates

> [!methodology-and-sources]
> **Template Testing Workflow**
> 
> 1. **Create test vault**: Separate vault for template development
> 2. **Test incrementally**: Add complexity gradually
> 3. **Use console logging**: `console.log()` in execution commands (view in Dev Tools)
> 4. **Test edge cases**: Empty inputs, missing frontmatter, non-existent files
> 5. **Document assumptions**: Comment what data your template expects

**Console Logging Example**:
```javascript
<%*
console.log("File title:", tp.file.title);
console.log("Frontmatter:", tp.frontmatter);

const userInput = await tp.system.prompt("Name");
console.log("User entered:", userInput);
%>
```

---

## 🎓 10. Mastery Patterns & Philosophy

### The Templater Mindset

> [!the-philosophy]
> **From Static to Dynamic Knowledge Management**
> 
> Traditional note-taking treats documents as fixed artifacts. Templater transforms this paradigm by making notes **living, responsive entities** that adapt to context, query data sources, and maintain consistency across your vault. Mastering Templater means thinking in terms of:
> 
> - **Generative Patterns** not static boilerplate
> - **Context-Aware Creation** not blind insertion
> - **Systematic Consistency** not manual updates
> - **Computational Augmentation** not just automation

### Progressive Skill Development

#### Novice Level (0-1 month)
- Use interpolation commands for dates and file metadata
- Apply basic conditional formatting
- Create simple folder templates
- Master the built-in function reference

#### Intermediate Level (1-3 months)
- Write execution commands with complex logic
- Build interactive templates with prompts and suggesters
- Create custom user scripts for repetitive tasks
- Integrate with other plugins (Dataview, Calendar)

#### Advanced Level (3-6 months)
- Architect multi-file creation workflows
- Manipulate vault structure programmatically
- Use Obsidian API directly for deep integration
- Build reusable template component libraries

#### Expert Level (6+ months)
- Design template ecosystems that maintain vault consistency
- Create domain-specific templating languages via user functions
- Optimize template performance at scale
- Contribute to Templater development or documentation

### Composable Template Architecture

> [!core-principle]
> **Modularity Through Inclusion**
> 
> Instead of monolithic templates, build a library of composable components using [[#tp.file.include()]].

**Component Structure**:
```
📁 Templates/
├── 📁 Components/
│   ├── frontmatter-standard.md
│   ├── daily-header.md
│   ├── task-section.md
│   └── footer-links.md
└── 📁 Assemblies/
    ├── daily-note.md      (composes multiple components)
    ├── project-note.md    (composes multiple components)
    └── meeting-note.md    (composes multiple components)
```

**Component Example** (`Components/frontmatter-standard.md`):
```markdown
---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
created: <% tp.date.now() %>
modified: <% tp.file.last_modified_date() %>
---
```

**Assembly Example** (`Assemblies/daily-note.md`):
```markdown
<% await tp.file.include("[[Components/frontmatter-standard]]") %>
<% await tp.file.include("[[Components/daily-header]]") %>

## Today's Focus

<% await tp.file.include("[[Components/task-section]]") %>

<% await tp.file.include("[[Components/footer-links]]") %>
```

### Template Versioning Strategy

Track template evolution to maintain vault consistency:

```yaml
---
template_version: 2.1.0
template_last_updated: 2025-11-13
template_changelog: |
  2.1.0 - Added automated task rollover
  2.0.0 - Migrated to modular component structure
  1.0.0 - Initial template
---
```

### Anti-Patterns to Avoid

> [!warning]
> **Common Template Anti-Patterns**
> 
> 1. **Monolithic Templates**: 500+ line templates → Use components
> 2. **Duplicate Logic**: Same code in multiple templates → Extract to user function
> 3. **Hardcoded Values**: File paths, dates, names → Use variables and prompts
> 4. **No Error Handling**: Assumes perfect input → Validate and provide fallbacks
> 5. **Synchronous Operations**: Forgetting `await` on async functions → Always await
> 6. **Template Sprawl**: 50+ similar templates → Parameterize and consolidate

### The Future-Proof Template

> [!principle-point]
> **Design Principles for Longevity**
> 
> 1. **Document Assumptions**: Comment what data your template expects
> 2. **Graceful Degradation**: Provide defaults when data is missing
> 3. **Version Awareness**: Include version metadata
> 4. **Modular Components**: Small, focused, reusable pieces
> 5. **Error Messages**: Helpful feedback when things fail
> 6. **Performance Conscious**: Optimize for scale

**Example Future-Proof Template**:
```javascript
<%*
/**
 * Project Note Template
 * Version: 2.0.0
 * Requires: Templater v2.0+
 * Dependencies: Components/project-header, Components/task-block
 * 
 * Assumptions:
 * - File will be created in Projects/ folder
 * - User will provide project name and status
 */

// Graceful input handling
let projectName = await tp.system.prompt("Project name");
if (!projectName || projectName.trim() === "") {
    projectName = "Untitled Project";
}

let status = await tp.system.suggester(
    ["Active", "Planning", "Archived"],
    ["active", "planning", "archived"]
);
if (!status) {
    status = "planning"; // Default if cancelled
}

// Error-handled file operations
try {
    await tp.file.rename(projectName);
} catch (error) {
    console.error("Failed to rename file:", error);
    tR += "⚠️ Could not rename file. Please rename manually.\n\n";
}

// Version-tracked output
tR += `---
template: project-note
template_version: 2.0.0
project_name: ${projectName}
status: ${status}
created: ${tp.date.now()}
---

`;

// Modular component inclusion with fallback
try {
    tR += await tp.file.include("[[Components/project-header]]");
} catch (error) {
    tR += "# " + projectName + "\n\n"; // Fallback if component missing
}

tR += `## Overview

## Goals

## Timeline

`;

try {
    tR += await tp.file.include("[[Components/task-block]]");
} catch (error) {
    tR += "## Tasks\n- [ ] \n"; // Fallback
}
-%>
```

---

## 🎯 Synthesis & Mastery

> [!analogy]
> **The Template as a Living Document Constructor**
> 
> Think of Templater not as a "fancy clipboard" but as a **document factory with a sophisticated API**. Each template is a production line specification that can query inventory (your vault), gather requirements (user prompts), apply business logic (conditionals), and assemble the final product (your note) with precision and consistency.
> 
> Just as a modern factory doesn't build every product identically but adjusts to specifications while maintaining quality standards, your templates should be *parameterized*, *context-aware*, and *adaptable* while ensuring *structural consistency*.

### Comparative Analysis: Templater vs Alternatives

| Approach | Flexibility | Learning Curve | Performance | Use Case |
|----------|-------------|----------------|-------------|----------|
| **Core Templates** | Low | Minimal | Excellent | Simple static insertion |
| **Templater** | Very High | Moderate-High | Good | Dynamic, interactive, programmatic |
| **Dataview** | Medium | Moderate | Excellent | Query and display, not creation |
| **QuickAdd** | High | High | Good | Macro automation, complex workflows |
| **Manual JS** | Maximum | Very High | Varies | Custom plugin development |

**When to Use Each**:
- **Core Templates**: Simple, truly static content (email signatures, code snippets)
- **Templater**: Dynamic file creation, interactive workflows, vault automation
- **Dataview**: Live-updating views, aggregation, reporting (complements Templater)
- **QuickAdd**: Multi-step macros, external integrations, Templater orchestration
- **Manual JS**: Plugin-level features, performance-critical operations

### Cognitive Models for Template Design

**Decision Tree Approach**:
```
Template Design Decision
├─ Is content purely static?
│  ├─ YES → Use Core Templates
│  └─ NO → Continue
├─ Does it require user input?
│  ├─ YES → Use tp.system prompts/suggesters
│  └─ NO → Continue
├─ Does it create multiple files?
│  ├─ YES → Use tp.file.create_new() loops
│  └─ NO → Continue
├─ Does it need complex logic?
│  ├─ YES → Use execution commands with conditionals
│  └─ NO → Use interpolation commands
└─ Does it need external data?
   ├─ YES → Create user function or use tp.web
   └─ NO → Use built-in functions
```

### Template Patterns Library

> [!quick-reference]
> **Essential Template Patterns**
> 
> - **Date Navigation**: `[[<% tp.date.yesterday() %>|← Previous]] | [[<% tp.date.tomorrow() %>|Next →]]`
> - **File Creation Date**: `Created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>`
> - **Conditional Section**: `<%* if (condition) { -%> Content <%* } -%>`
> - **User Input**: `<%* const input = await tp.system.prompt("Label"); %>`
> - **File Selection**: `<%* const file = await tp.system.suggester(item => item.basename, tp.app.vault.getMarkdownFiles()); %>`
> - **Array to List**: `<%* tp.frontmatter.items.map(x => `- ${x}`).join("\n") %>`
> - **Create Related File**: `<%* await tp.file.create_new(content, filename, false, folder); %>`
> - **Frontmatter Update**: `<%* tp.hooks.on_all_templates_executed(async () => { /* update frontmatter */ }); %>`

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
> - **Primary Source**: Official Templater Documentation (silentvoid13.github.io/Templater/)
> - **GitHub Repository**: SilentVoid13/Templater (issues, discussions, examples)
> - **Community Resources**: Obsidian Forum, Reddit, user showcases
> - **Code Examples**: Tested in Templater v2.x (current as of 2025-11-13)
> - **Synthesis Approach**: Comprehensive aggregation of syntax, functions, patterns, and best practices
> - **Confidence Level**: High for documented features; Medium for edge cases and advanced patterns

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-13 | Initial comprehensive reference compilation |

---

# 🔗 Related Topics for PKB Expansion

1. **[[Advanced JavaScript for Templater]]**
   - *Connection*: Deep dive into JavaScript patterns specifically optimized for Templater execution
   - *Depth Potential*: Covers async/await mastery, error handling, API integration, and performance optimization
   - *Knowledge Graph Role*: Technical skills node connecting Templater to broader programming knowledge

2. **[[Obsidian Automation Workflows]]**
   - *Connection*: How Templater integrates with QuickAdd, Dataview, Calendar, and other automation plugins
   - *Depth Potential*: Multi-plugin orchestration patterns, macro programming, vault-wide automation strategies
   - *Knowledge Graph Role*: Workflow hub connecting individual plugin capabilities into cohesive systems

3. **[[Personal Knowledge Management System Design]]**
   - *Connection*: How dynamic templates support systematic knowledge capture and organization
   - *Depth Potential*: Information architecture, note taxonomy, retrieval optimization, and template-driven consistency
   - *Knowledge Graph Role*: Meta-level design principles governing all PKM tool usage

4. **[[Obsidian API Deep Reference]]**
   - *Connection*: Full exploration of tp.app and tp.obsidian for advanced vault manipulation
   - *Depth Potential*: Complete API coverage, plugin integration patterns, custom tool development
   - *Knowledge Graph Role*: Technical foundation for extending Obsidian beyond plugin capabilities

```
<thinking>
This is a comprehensive reference note request for the Templater plugin in Obsidian. Let me analyze the requirements:

**REQUEST CLASSIFICATION:**
- Type: comprehensive_note (reference documentation)
- Scope: reference (exhaustive coverage of Templater plugin)
- Research Required: YES - I need to gather current, authoritative information about Templater's complete feature set, syntax, and best practices
- User Expertise: Novice seeking expert-level precision
- Critical Requirement: Code accuracy is paramount

**RESEARCH STRATEGY:**
I need to conduct systematic web research to ensure:
1. Complete syntax coverage (all template commands)
2. Current best practices and documentation
3. Real-world examples and use cases
4. Common pitfalls and solutions
5. Integration with other Obsidian features

Let me execute targeted searches:

**SEARCH 1: Core Templater Documentation**
- Query Rationale: Need official documentation for accurate syntax and features
- Expected Insight: Complete command reference, installation, basic usage

**SEARCH 2: Advanced Templater Techniques**
- Query Rationale: Need advanced patterns, user functions, system commands
- Expected Insight: Complex examples, automation workflows, scripting capabilities

**SEARCH 3: Templater Best Practices**
- Query Rationale: Need community wisdom, common patterns, expert tips
- Expected Insight: Professional workflows, optimization strategies, troubleshooting

**SEARCH 4: Templater with Dataview and Other Plugins**
- Query Rationale: Need integration patterns with other common plugins
- Expected Insight: Cross-plugin workflows, compatibility considerations

**SEARCH 5: Templater User Functions and JavaScript**
- Query Rationale: Need detailed coverage of custom scripting capabilities
- Expected Insight: JavaScript integration, complex automation examples

**STRUCTURAL PLANNING:**

STRUCTURAL REASONING:
├── Core Concept Architecture
│   ├── Why this structure? Start with fundamentals (installation, basic syntax) → Progress to advanced features (scripting, automation) → Conclude with mastery patterns
│   └── Information flow logic: Pedagogical progression from novice to expert, with immediate practical application at each level
│
├── Hierarchy Decisions
│   ├── Primary sections: 
│   │   1. Introduction & Setup (foundational)
│   │   2. Core Syntax & Commands (reference lookup)
│   │   3. Template Types & Patterns (practical application)
│   │   4. Advanced Features (power user techniques)
│   │   5. User Functions & Scripting (expert customization)
│   │   6. Integration & Workflows (real-world usage)
│   │   7. Troubleshooting & Best Practices (problem-solving)
│   │   8. Mastery Patterns (synthesis)
│   └── Subsection depth: 3-4 levels to allow both scanning and deep reference
│
└── Cross-referencing Strategy
    ├── Internal links to related sections (e.g., "See [[#User Functions]] for custom scripting")
    ├── Wiki-links for Obsidian concepts ([[Dataview]], [[Daily Notes]], [[Frontmatter]])
    ├── Wiki-links for programming concepts ([[JavaScript]], [[Template Literals]], [[Asynchronous Programming]])
    └── Expansion topics toward adjacent plugin ecosystem and advanced PKM patterns

**METADATA PLANNING:**
Tags: #obsidian #templater #automation #reference-note #plugin-documentation
Aliases: [Templater Plugin, Templater Reference, Obsidian Templater Guide, Templater Syntax Reference]

**CALLOUT STRATEGY:**
- [!definition] for syntax definitions
- [!example] extensively for code demonstrations
- [!warning] for common pitfalls
- [!helpful-tip] for expert techniques
- [!methodology-and-sources] for complex workflows
- [!quick-reference] for syntax lookup tables
- [!what-this-does] for feature explanations
- [!use-cases-and-examples] for practical applications

**WIKI-LINK OPPORTUNITIES:**
- Obsidian core concepts: [[Frontmatter]], [[Templates]], [[Folders]], [[Daily Notes]], [[Metadata]]
- Related plugins: [[Dataview]], [[QuickAdd]], [[Custom JS]], [[Natural Language Dates]]
- Programming concepts: [[JavaScript]], [[Regular Expressions]], [[Async/Await]], [[Promises]], [[Date Objects]]
- PKM concepts: [[Zettelkasten]], [[MOC]], [[Atomic Notes]], [[Template Systems]], [[Automation Workflows]]
- File system concepts: [[File Paths]], [[Working Directory]], [[Relative Paths]], [[Absolute Paths]]

Now I'll execute the web searches to gather comprehensive, accurate information.
</thinking>Let me continue gathering more information about advanced features.Now I have comprehensive research. Let me create the exhaustive reference documentation for Templater.
```