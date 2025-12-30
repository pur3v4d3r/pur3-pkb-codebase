---
title:
aliases:
  - Meta Bind
  - Metabind
  - Meta Bind Plugin
  - Input Fields Plugin
  - Dynamic Forms in Obsidian
  - Interactive Metadata System
tags:
  - year/2025
  - pkb
  - pkm
  - obsidian/plugins/meta-bind
  - pkb/metadata/frontmatter
  - pkb/metadata/yaml
  - type/reference
  - knowledge-workflow
id: "20251119204930"
created: 2025-11-19T20:49:30
week: "[[2025-W47]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
link-up:
  - 
link-related:
  - "[[2025-11-19|Daily-Note]]"
  - "[[permeant-note_moc]]"
status: completed
completed-date: 2025-11-20
completed: false
---

---

aliases: [Meta Bind Plugin, Input Fields Plugin, Dynamic Forms in Obsidian, Interactive Metadata System]
---

# 📝 Meta Bind Plugin — Interactive Metadata Management for Obsidian

> [!the-purpose]
> **Meta Bind transforms your static [[obsidian]] notes into dynamic, interactive documents** by allowing you to create input fields, view fields, and action buttons that bind directly to [[YAML Frontmatter]] properties. This creates a **bidirectional synchronization system** where changes to input fields instantly update metadata, and metadata changes instantly reflect in your note content—enabling powerful [[Dashboard Design]], [[Task Management]], [[habit tracking]], and [[Project Management]] workflows within your [[Personal Knowledge Base]].

---

## 🎯 Core Concept & Value Proposition

> [!core-principle]
> **The Meta Bind Philosophy: "Edit Metadata from Anywhere"**
> 
> Traditional [[obsidian]] workflows require you to edit frontmatter properties at the top of notes or through the properties panel. Meta Bind breaks this limitation by allowing you to create interactive input fields anywhere within your note body that remain synchronized with frontmatter properties in real-time. This enables you to build custom interfaces, interactive dashboards, and dynamic forms that feel more like applications than static documents.

Meta Bind is fundamentally about making your notes interactive—it enables you to create input fields for editing metadata, view fields for displaying metadata, and buttons for triggering actions, all bound to frontmatter properties that stay synchronized. The plugin operates on a **reactive programming model** where changes propagate instantly across all bound elements, creating a seamless user experience similar to modern web applications.

### Why This Matters for PKM

In a sophisticated [[Personal Knowledge Base]], metadata isn't just descriptive—it's functional. You use it to:
- Track project status, completion percentages, and priorities
- Manage reading lists, research progress, and review schedules
- Build interconnected dashboards using [[dataview]] queries
- Implement [[GTD]] (Getting Things Done) workflows
- Create [[03-notes/01_permanent-notes/01_cognitive-development/Spaced Repetition]] systems and [[habit tracking]] mechanisms

Meta Bind elevates metadata from a **passive annotation system** to an **active control system**, allowing you to manipulate your knowledge graph through intuitive interfaces rather than raw YAML editing.

---

## ⚙️ Architecture: The Three Pillars of Meta Bind

### 1. Input Fields — Write Operations

> [!definition]
> **Input Fields** are interactive UI elements (toggles, text boxes, sliders, date pickers, etc.) that allow you to edit frontmatter properties directly from within your note content. When you interact with an input field, it writes the new value to the bound frontmatter property, and when that property changes elsewhere, the input field updates to reflect the new value.

**Syntax Foundation:**
```markdown
`INPUT[fieldType:bindTarget]`
```

**Core Input Types:**
- `toggle` — Boolean true/false switch
- `text` — Single-line text input
- `textArea` — Multi-line text input
- `number` — Numeric input with optional min/max
- `slider` — Numeric slider with range
- `date` — Date picker
- `time` — Time picker
- `datetime` — Combined date and time picker
- `select` — Dropdown menu
- `multiSelect` — Multi-option selection
- `inlineSelect` — Compact dropdown
- `suggester` — Autocomplete text field
- `toggle` — Boolean switch
- `progressBar` — Visual progress indicator (read-only display, typically paired with slider)
- `list` — List management interface
- `listSuggester` — List with autocomplete

### 2. View Fields — Read Operations

> [!definition]
> **View Fields** are reactive display elements that show the current value of one or more frontmatter properties. Unlike Dataview inline queries which refresh periodically, view fields update instantly when bound properties change, and they can perform computations on multiple properties simultaneously.

**Syntax Foundation:**
```markdown
`VIEW[{bindTarget}]`
`VIEW[viewType]{expression}`
```

**Key Features:**
- **Mathematical operations**: View fields support mathematical expressions like `{distanceKm} * 0.621371` to convert kilometers to miles
- **Multi-property binding**: Reference multiple frontmatter properties in a single view field
- **Computed persistence**: Option to save computed values back to frontmatter
- **Markdown rendering**: Can render frontmatter text as formatted Markdown
- **JavaScript views**: Advanced users can enable JavaScript-powered view fields for complex computations and conditional logic

### 3. Buttons — Action Triggers

> [!definition]
> **Buttons** are clickable elements that execute actions when pressed. Buttons can trigger Obsidian commands, run Templater scripts, create new notes, update metadata values, and perform complex multi-step workflows.

**Syntax Options:**
`````markdown
<!-- Inline button referencing a code block -->
`BUTTON[buttonId]`

<!-- Code block button with full configuration -->
```meta-bind-button
id: my-button
style: primary
label: Click Me
action:
  type: command
  command: 'templater-obsidian:create-new-note-from-template'
```
`````

**Available Button Actions:**
- `command` — Execute any Obsidian command
- `js` — Run JavaScript code
- `open` — Open URLs or notes
- `sleep` — Add delays in multi-action sequences
- `updateMetadata` — Modify frontmatter properties
- `templaterCreateNote` — Create notes using [[Templater]] templates
- `replaceInNote` — Find and replace text operations
- `regexpReplaceInNote` — Regex-based replacements
- `insertIntoNote` — Insert content at specific positions

---

## 🔗 Bind Targets: The Connection Mechanism

> [!core-principle]
> **Bind Targets are the addressing system** that tells Meta Bind *where* to read from or write to. They consist of three parts: storage type (frontmatter, memory, etc.), storage path (which note), and property name (which field).

### Bind Target Anatomy

```markdown
`storageType^storagePath#property`
```

**Components:**
1. **Storage Type** (optional, defaults to `frontmatter`)
   - `frontmatter^` — YAML frontmatter (default)
   - `memory^` — Temporary in-memory storage (not persisted)
   
2. **Storage Path** (optional, defaults to current note)
   - Omit for current note
   - `filename#` for note by name
   - `folder/subfolder/filename#` for full path
   
3. **Property** (required)
   - Simple: `propertyName`
   - With spaces: Use JavaScript bracket syntax like `['property name']` for properties with special characters
   - Nested: `parent.child` or `parent['child name']`

### Practical Examples
`INPUT[toggle:completed]`
```markdown
<!-- Bind to 'completed' in current note's frontmatter -->
`INPUT[toggle:completed]`

<!-- Bind to 'status' in a different note -->
`INPUT[inlineSelect:Projects/ProjectA#status]`

<!-- Bind to nested property -->
`INPUT[number:project.budget.total]`

<!-- Temporary binding (not saved to frontmatter) -->
`INPUT[text:memory^temporaryNote]`

<!-- Property with spaces -->
`INPUT[date:['Due Date']]`



```

---

## 💡 Practical Implementation Patterns

### Pattern 1: Task Completion Toggle

**Use Case:** Track task completion status without editing frontmatter directly.

```markdown
---
completed: false
---

# My Task

**Status:** `INPUT[toggle:completed] Mark as complete`
```

### Pattern 2: Priority & Status Dashboard

**Use Case:** Visual project management interface.

```markdown
---
status: in-progress
priority: high
progress: 45
---

# Project Dashboard

**Status:** `INPUT[inlineSelect(option(planning, 📋 Planning),option(in-progress, 🚧 In Progress),option(review, 👀 Review),option(completed, ✅ Completed)):status]`

**Priority:** `INPUT[inlineSelect(option(1, 🔴 Critical),option(2, 🟠 High),option(3, 🟡 Medium),option(4, 🟢 Low)):priority]`

**Progress:** `INPUT[slider(minValue(0), maxValue(100)):progress]%`

`VIEW[progressBar]{progress}`
```

### Pattern 3: Reading List Tracker

**Use Case:** Manage reading progress with dates and ratings.

```markdown
---
read-status: reading
started-date: ""
completed-date: ""
rating: 0
---

# Book Review: [[Book Title]]

**Status:** `INPUT[inlineSelect(option(to-read, 📚 To Read),option(reading, 📖 Reading),option(completed, ✅ Completed)):read-status]`

**Started:** `INPUT[date:started-date]`
**Finished:** `INPUT[date:completed-date]`

**Rating:** `INPUT[slider(minValue(0), maxValue(5)):rating] ⭐`

> [!summary]
> Current rating: `VIEW[{rating}]/5 stars`
```

### Pattern 4: Habit Tracking Grid

**Use Case:** Daily habit completion tracking.

```markdown
---
habits:
  exercise: false
  meditation: false
  reading: false
  journaling: false
---

# Daily Habits — [[2025-11-19]]

- **Exercise (30 min):** `INPUT[toggle:habits.exercise]`
- **Meditation (10 min):** `INPUT[toggle:habits.meditation]`
- **Reading (25 min):** `INPUT[toggle:habits.reading]`
- **Journaling:** `INPUT[toggle:habits.journaling]`


```

### Pattern 5: Meeting Notes Template with Templater

**Use Case:** Create meeting notes with dynamic metadata capture using Meta Bind buttons to trigger Templater template instantiation.

```markdown
<!-- On your Meetings MOC page -->

```meta-bind-button
id: create-meeting
style: primary
label: 📝 New Meeting Note
action:
  type: templaterCreateNote
  templateFile: Templates/Meeting Template
  folderPath: Meetings
  fileName: TKTK
  openNote: true
```
```

**Meeting Template:**
```markdown
---
attendees: []
meeting-date: 2025-11-20
summary: ""
action-items: []
---

# Meeting: templater-pkb-cheat-sheat

**Date:** `INPUT[date:meeting-date]`
**Attendees:** `INPUT[list:attendees]`
**Summary:** `INPUT[textArea(class(meta-bind-full-width)):summary]`

## Discussion Notes

## Action Items
`INPUT[list(addLabel(Add Action Item)):action-items]`


```

---

## 🔌 Plugin Integration Ecosystem

> [!connection-ideas]
> **Meta Bind's true power emerges through integrations** with other [[obsidian]] plugins, creating compound workflows that leverage each tool's strengths.

### Integration with Dataview

Meta Bind input fields can be embedded within DataviewJS queries to create interactive tables where each row has controls for modifying that specific note's metadata.

**Example: Interactive Task Table**

```dataviewjs
const pages = dv.pages('#task')
  .where(p => p.status != "completed")
  .sort(p => p.priority);

dv.table(
  ["Task", "Status", "Priority", "Complete"],
  pages.map(p => [
    p.file.link,
    `\`INPUT[inlineSelect(option(todo, To Do), option(in-progress, In Progress), option(blocked, Blocked)):${p.file.path}#status]\``,
    `\`INPUT[slider(minValue(1), maxValue(4)):${p.file.path}#priority]\``,
    `\`INPUT[toggle:${p.file.path}#completed]\``
  ])
);
```



> [!helpful-tip]
> **Syntax Note:** The trick to embedding Meta Bind in DataviewJS is using template literals with `${p.file.path}` to dynamically inject the correct bind target path for each note.

### Integration with Templater

Meta Bind buttons can trigger [[Templater]] template creation workflows, combining:
- **Meta Bind**: User-friendly button interfaces
- **Templater**: Dynamic content generation and file manipulation

**Example: Goal Creation Workflow**

You can create a Meta Bind button that executes a Templater command to create a new goal note from a template, automatically filling in metadata and moving the note to the correct folder.

```meta-bind-button
id: create-goal
style: primary
label: 🎯 New Goal
action:
  type: command
  command: 'templater-obsidian:create-new-note-from-template'
```

### Integration with Tasks Plugin

The Meta Bind plugin can work alongside the Tasks plugin to create hybrid task management systems where:
- **Tasks** handles due dates, recurrence, and markdown task syntax
- **Meta Bind** provides visual status indicators, priority sliders, and completion toggles

### Integration with QuickAdd

Combine [[component-exemplar-quickadd-plugin-documentation-v1.0.0-20251119225738]] capture workflows with Meta Bind buttons:
1. Meta Bind button triggers QuickAdd macro
2. QuickAdd presents capture interface
3. New note created with Meta Bind input fields pre-configured
4. Return to dashboard with updated [[dataview]] query

### Integration with Day Planner / Full Calendar

Use Meta Bind to:
- Set event dates that sync with calendar plugins
- Toggle event completion status
- Adjust time blocks and duration through sliders
- Maintain bidirectional sync between calendar view and note metadata

---

## 🚀 Advanced Techniques

### Computed Values with View Fields

> [!insight]
> **View fields can perform calculations and save results** back to frontmatter, enabling derived metadata that updates automatically.

**Example: Budget Tracker**

```markdown
---
budget-total: 10000
spent-marketing: 3500
spent-development: 4200
spent-operations: 1100
remaining: 0
---

**Total Budget:** $VIEW[{budget-total}]

**Expenditures:**
- Marketing: INPUT[number:spent-marketing]
- Development: INPUT[number:spent-development]
- Operations: INPUT[number:spent-operations]

**Remaining Budget:** VIEW[math(saveAsBindTarget(remaining))]{
  budget-total - spent-marketing - spent-development - spent-operations
}
```

The `saveAsBindTarget(remaining)` argument tells Meta Bind to persist the computed value to the `remaining` frontmatter property.

### JavaScript-Powered View Fields

For advanced users, Meta Bind supports JavaScript view fields that can access the same APIs as JS Engine, enabling complex conditional logic and dynamic content generation.

**Example: Conditional Status Display**

````markdown
```meta-bind-js-view
---
x: status
y: deadline
---
const status = context.bound.x;
const deadline = new Date(context.bound.y);
const today = new Date();
const daysUntil = Math.ceil((deadline - today) / (1000 * 60 * 60 * 24));

if (status === "completed") {
  return "✅ **Completed**";
} else if (daysUntil < 0) {
  return `🚨 **Overdue by ${Math.abs(daysUntil)} days**`;
} else if (daysUntil <= 3) {
  return `⚠️ **Due in ${daysUntil} days**`;
} else {
  return `📅 Due in ${daysUntil} days`;
}
```
````

> [!warning]
> **JavaScript view fields require manual enablement** in Meta Bind settings due to potential security risks. Only enable if you understand the code you're executing.

### Multi-Action Button Workflows

Buttons can execute sequential actions, enabling complex workflows:

```meta-bind-button
id: finalize-project
style: primary
label: ✅ Finalize Project
actions:
  - type: updateMetadata
    bindTarget: status
    evaluate: false
    value: completed
  - type: updateMetadata
    bindTarget: completed-date
    evaluate: false
    value: 2025-11-20
  - type: command
    command: 'obsidian-kanban:archive-completed-cards'
  - type: open
    link: "[[Projects MOC]]"
```

### Input Field Templates

Meta Bind supports reusable input field templates defined globally in plugin settings, allowing you to create consistent input patterns across your vault.

**Define Template in Settings:**
```markdown
id: ratingSlider
template: slider(minValue(1), maxValue(5), class(rating-slider))
```

**Use Template in Notes:**
```markdown
INPUT[#ratingSlider:book-rating]
```

This applies the pre-configured slider settings to any binding target.

---

## 🎨 Daily PKB Workflow Integration

> [!use-cases-and-examples]
> **How Meta Bind Enhances Daily Knowledge Work:**

### Morning Routine Dashboard

Create a **Daily Note template** with Meta Bind controls for:
- Mood tracking (slider 1-10)
- Energy level (select dropdown)
- Today's focus areas (multi-select checklist)
- Habit completion toggles
- Quick capture input fields

### Project Status Review

Build a **Projects MOC** that uses:
- Dataview to query all project notes
- Meta Bind input fields embedded in table for quick status updates
- Buttons to create new project notes from templates
- Progress bars showing completion percentages
- Priority sliders visible across all active projects

### Reading & Research Management

Maintain a **Reading List MOC** with:
- Status indicators (to-read, reading, completed)
- Started/finished date pickers
- Rating sliders for completed books
- Notes field for key takeaways
- Dataview queries filtered by Meta Bind metadata

### Zettelkasten Note Development

In your **Literature Notes** and **Permanent Notes**:
- Development status dropdown (seedling → budding → evergreen)
- Confidence rating for claims
- Source citation count tracking
- Last reviewed date with toggle for "needs review"
- Connection density indicator

---

## ⚠️ Limitations & Considerations

> [!constraints-and-pitfalls]
> **Important Caveats for Meta Bind Usage:**

### Performance Considerations

- Dynamically creating many input or view fields with JavaScript can impact performance, especially across numerous notes.
- Complex JavaScript view fields recalculate on every bound property change
- Large Dataview tables with embedded Meta Bind fields may render slowly

### Architectural Constraints

- **Single-note loading requirement**: View fields only work when the note containing them is open—if Note A has a view field computing values for Note B, and Note A is closed, the computation won't update.
- **No circular dependencies**: Meta Bind detects and prevents infinite loops between view fields
- **Input fields don't auto-create properties**: An input field only writes to its bound property when interacted with, meaning it won't automatically create missing frontmatter properties on note load.
- **Mobile limitations**: Some complex JavaScript features may not work on mobile devices

### Sync & Compatibility

- All Meta Bind state is stored in frontmatter, so **sync is native**—no special configuration needed
- Plugin must be installed on all devices where you want interactive functionality
- If viewing notes without Meta Bind installed, you'll see raw syntax (e.g., `INPUT[toggle:done]`)

### Learning Curve

- Bind target syntax requires understanding of path notation
- JavaScript view fields require programming knowledge
- Button actions have specific configuration requirements
- Integration with other plugins needs experimentation

---

## 🎓 Best Practices for PKB Integration

> [!methodology-and-sources]
> **Patterns from the Meta Bind Community:**

### 1. Progressive Enhancement Strategy

Start with **simple toggles and selects**, then gradually add:
1. Basic input fields (toggles, dates, text)
2. View fields for computed values
3. Buttons for common actions
4. Dataview + Meta Bind hybrid tables
5. JavaScript-powered advanced features

### 2. Template-First Design

Build Meta Bind functionality into **[[Templater]] templates** rather than manually adding fields to individual notes. This ensures:
- Consistency across note types
- Reduced cognitive load (template handles structure)
- Easier maintenance (update template, not 100 notes)
- Faster note creation

### 3. Metadata Schema Planning

Before implementing Meta Bind extensively, **design your frontmatter schema**:
- What properties do each note type need?
- Which properties should be editable via input fields?
- Which should be computed via view fields?
- What naming conventions will you use?

Document this in a **[[PKB Style Guide]]** or **[[Metadata Schema MOC]]**.

### 4. Dashboard-Centric Architecture

Use Meta Bind to create **navigational hubs** (MOCs) that provide:
- At-a-glance status of all notes in a category
- Quick-edit capabilities via embedded input fields
- One-click note creation buttons
- Visual progress indicators

This transforms MOCs from passive indexes into **active command centers**.

### 5. Separation of Concerns

Keep **data** (frontmatter) separate from **interface** (Meta Bind fields):
- Don't duplicate information in both frontmatter and note body
- Let input fields be the *only* way to edit specific properties
- Use view fields to display computed values rather than manually updating text

---

## 🔧 Technical Configuration

### Essential Settings

**Enable JavaScript Evaluation** (optional, for advanced users):
- Settings → Meta Bind → Enable JavaScript View Fields
- Enables JS-powered view fields and computed bindings
- ⚠️ Only enable if you understand security implications

**Configure Button Templates**:
- Settings → Meta Bind → Button Templates
- Define global button configurations for reuse
- Useful for frequently-used actions like template creation

**Set Default Bind Target Storage**:
- Usually `frontmatter` (default) is optimal
- Consider `memory` for temporary UI state that shouldn't persist

### Recommended Plugin Stack

For maximum Meta Bind effectiveness, also install:
- **[[dataview]]** — Query and display metadata dynamically
- **[[Templater]]** — Create templates with Meta Bind fields
- **[[component-exemplar-quickadd-plugin-documentation-v1.0.0-20251119225738]]** — Capture workflows that leverage Meta Bind
- **[[Tasks]]** — Complementary task management
- **[[Buttons]]** (legacy alternative, but Meta Bind buttons are superior)
- **[[Callout Manager]]** — Style input field containers
- **[[CSS Snippets]]** — Custom styling for Meta Bind elements

---

## 📚 Learning Resources

> [!important-links]
> **Official Documentation & Community Resources:**
> 
> - [Meta Bind Official Documentation](https://www.moritzjung.dev/obsidian-meta-bind-plugin-docs/) — Comprehensive guides and API reference
> - [GitHub Repository](https://github.com/mProjectsCode/obsidian-meta-bind-plugin) — Source code, issues, feature requests
> - [Meta Bind Playground Command] — Run `Open Meta Bind Playground` in Obsidian to see all input types in action
> - [Example Vault](https://github.com/mProjectsCode/obsidian-meta-bind-plugin-docs) — Test vault with working examples
> - [Obsidian Forum Meta Bind Discussions](https://forum.obsidian.md/search?q=meta%20bind) — Community use cases and troubleshooting

---

# 🧭 Related Topics for PKB Expansion

1. **[[Dataview Plugin]]**
   - *Connection*: Meta Bind and Dataview form a powerful combination—Dataview queries data, Meta Bind modifies it interactively
   - *Depth Potential*: Understanding DataviewJS patterns for embedding Meta Bind fields in dynamic tables
   - *Knowledge Graph Role*: Core automation plugin that works synergistically with Meta Bind

2. **[[Reactive Programming in PKM]]**
   - *Connection*: Meta Bind's instant synchronization model is based on reactive programming principles
   - *Depth Potential*: Exploring how reactive data flows enable real-time knowledge base interactions
   - *Knowledge Graph Role*: Conceptual foundation for understanding modern PKM plugin architectures

3. **[[Dashboard Design Principles]]**
   - *Connection*: Meta Bind enables dashboard creation—but effective dashboards require design thinking
   - *Depth Potential*: Information architecture, visual hierarchy, and cognitive load management for PKB dashboards
   - *Knowledge Graph Role*: Bridge between technical capability (Meta Bind) and user experience (design)

4. **[[Metadata Schema Design for PKB]]**
   - *Connection*: Meta Bind exposes the importance of well-structured metadata—poor schema = poor interface
   - *Depth Potential*: Designing frontmatter taxonomies, property naming conventions, and data types
   - *Knowledge Graph Role*: Foundational PKB architecture topic that determines scalability and maintainability

---

```
<thinking>
**REQUEST CLASSIFICATION:**
- Type: comprehensive_note (reference note)
- Scope: reference (exhaustive coverage of Meta Bind plugin)
- Research Required: YES - Need current information about Meta Bind plugin features, capabilities, integration possibilities, and best practices since this is a community plugin that may have evolved

**RESEARCH PLAN:**
I need to search for:
1. Meta Bind plugin core functionality and features
2. Meta Bind use cases and practical applications
3. Meta Bind integration with other Obsidian plugins (Dataview, Templater, Tasks, etc.)
4. Meta Bind syntax and implementation examples
5. Best practices for Meta Bind in PKM workflows

**STRUCTURAL PLANNING:**
Metadata:
- Tags: #obsidian #plugin #meta-bind #pkm #automation #reference-note
- Aliases: [Meta Bind Plugin, Input Fields Plugin, Dynamic Forms in Obsidian]

Outline:
1. Overview & Core Concept (what Meta Bind is, why it matters)
2. Core Features & Capabilities (input fields, view fields, buttons, embed buttons)
3. Syntax & Implementation (how to create bindings, field types)
4. Plugin Integration Ecosystem (Dataview, Templater, Tasks, QuickAdd, etc.)
5. Practical Use Cases (task management, habit tracking, project dashboards, etc.)
6. Advanced Techniques (computed values, conditional display, complex bindings)
7. Workflow Integration (how it fits into daily PKB activities)
8. Limitations & Considerations
9. Expansion topics (related plugins, advanced automation, etc.)

**WIKI-LINK OPPORTUNITIES:**
[[Obsidian]], [[YAML Frontmatter]], [[Dataview]], [[Templater]], [[Tasks Plugin]], [[QuickAdd]], [[Metadata]], [[PKM Automation]], [[Dynamic Content]], [[Input Fields]], [[View Fields]], [[Button Actions]], [[Dashboard Design]], [[Project Management]], [[Habit Tracking]], [[Progressive Summarization]], [[MOC]], [[Template System]], [[Reactive Programming]], [[Data Binding]]

**CALLOUT STRATEGY:**
- [!definition] for core concepts
- [!core-principle] for fundamental mechanics
- [!what-this-does] for feature explanations
- [!example] for syntax demonstrations
- [!methodology-and-sources] for implementation patterns
- [!connection-ideas] for plugin integrations
- [!use-cases-and-examples] for practical applications
- [!helpful-tip] for best practices
- [!warning] for limitations
- [!insight] for advanced techniques

Let me search for current Meta Bind information.
</thinking>Now I have comprehensive information about Meta Bind. Let me create the reference note.
```
