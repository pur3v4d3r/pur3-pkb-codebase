# Meta Bind Plugin - Complete Reference Guide

> **Plugin Version:** 1.4.6
> **Official Documentation:** https://www.moritzjung.dev/obsidian-meta-bind-plugin-docs/
> **Purpose:** Make notes interactive with inline input fields, metadata displays, and buttons

---
🎯 Key Features
- Exact syntax verified from your plugin files
	- Real examples from your vault
- All arguments documented for each field type
- Button styles and properties table
- Bind target syntax with cross-note examples
- JavaScript view fields with context API
- Plugin configuration reference
- Best practices section
- Quick reference card at the end
The guide is structured for easy navigation with a table of contents and is formatted to be used directly in your vault for reference when building templates

## Table of Contents

1. [Quick Start Syntax](#quick-start-syntax)
2. [Input Fields](#input-fields)
3. [View Fields](#view-fields)
4. [Buttons](#buttons)
5. [Bind Target Syntax](#bind-target-syntax)
6. [JavaScript View Fields](#javascript-view-fields)
7. [Template Examples](#template-examples)
8. [Plugin Configuration](#plugin-configuration)

---

## Quick Start Syntax

### Basic Input Field
```markdown
INPUT[fieldType:bindTarget]
INPUT[fieldType(argument1, argument2):bindTarget]
```

### Basic View Field
```markdown
VIEW[{propertyName}]
VIEW[{propertyName}][viewType]
VIEW[expression][viewType:saveTarget]
```

### Basic Button (Inline)
```markdown
BUTTON[buttonId]
```

### Basic Button (Code Block)
````markdown
```meta-bind-button
label: Button Text
style: primary
action:
  type: command
  command: 'command-id'
```
````

---

## Input Fields

### 1. Toggle (Boolean)

**Basic Syntax:**
```markdown
INPUT[toggle:completed]
INPUT[toggle:published]
```

**With Arguments:**
```markdown
INPUT[toggle(showcase):reviewed]
INPUT[toggle(onValue(1), offValue(0)):binary]
INPUT[toggle(defaultValue(true)):enabled]
```

**Arguments:**
- `showcase` - Display the field prominently
- `onValue(value)` - Custom value when toggled on (default: true)
- `offValue(value)` - Custom value when toggled off (default: false)
- `defaultValue(value)` - Initial value if property doesn't exist

**Example in Frontmatter:**
```markdown
---
completed: false
published: true
---

**Completed:** INPUT[toggle:completed]
**Published:** INPUT[toggle:published]
```

---

### 2. Text Input

**Basic Syntax:**
```markdown
INPUT[text:title]
INPUT[text:author]
```

**With Arguments:**
```markdown
INPUT[text(showcase):name]
INPUT[text(limit(50)):short-description]
INPUT[text(placeholder(Enter title here)):title]
INPUT[text(defaultValue(Untitled)):title]
```

**Arguments:**
- `showcase` - Display prominently
- `limit(n)` - Maximum character count
- `placeholder(text)` - Placeholder text
- `defaultValue(text)` - Default value

---

### 3. Text Area (Multi-line)

**Basic Syntax:**
```markdown
INPUT[textArea:notes]
INPUT[textArea:description]
```

**With Arguments:**
```markdown
INPUT[textArea(showcase):summary]
INPUT[textArea(class(meta-bind-full-width)):content]
INPUT[textArea(placeholder(Write notes here...)):notes]
INPUT[textArea(limit(500)):short-notes]
```

**Arguments:**
- `showcase` - Display prominently
- `class(className)` - Custom CSS class
- `placeholder(text)` - Placeholder text
- `limit(n)` - Maximum character count
- `multiLine(true/false)` - Enable/disable multi-line

**Common CSS Classes:**
- `meta-bind-full-width` - Full width text area

---

### 4. Number

**Basic Syntax:**
```markdown
INPUT[number:age]
INPUT[number:price]
```

**With Arguments:**
```markdown
INPUT[number(minValue(0)):quantity]
INPUT[number(maxValue(100)):percentage]
INPUT[number(minValue(0), maxValue(10)):rating]
INPUT[number(placeholder(0)):count]
```

**Arguments:**
- `minValue(n)` - Minimum allowed value
- `maxValue(n)` - Maximum allowed value
- `placeholder(n)` - Placeholder number
- `defaultValue(n)` - Default value

---

### 5. Slider

**Basic Syntax:**
```markdown
INPUT[slider:volume]
INPUT[slider:rating]
```

**With Arguments:**
```markdown
INPUT[slider(showcase):priority]
INPUT[slider(addLabels):importance]
INPUT[slider(minValue(0), maxValue(5)):rating]
INPUT[slider(minValue(0), maxValue(100), stepSize(5)):progress]
INPUT[slider(addLabels, minValue(1), maxValue(10), stepSize(1)):difficulty]
```

**Arguments:**
- `showcase` - Display prominently
- `addLabels` - Show min/max labels
- `minValue(n)` - Minimum value (default: 0)
- `maxValue(n)` - Maximum value (default: 100)
- `stepSize(n)` - Increment size (default: 1)
- `class(className)` - Custom CSS class

**Example:**
```markdown
---
progress: 45
rating: 3
---

**Progress:** INPUT[slider(addLabels, minValue(0), maxValue(100)):progress]%
**Rating:** INPUT[slider(minValue(1), maxValue(5), stepSize(0.5)):rating] / 5
```

---

### 6. Select (Single Choice)

**Basic Syntax:**
```markdown
INPUT[select(option(value1), option(value2)):propertyName]
INPUT[select(option(val, Display Name)):propertyName]
```

**With Arguments:**
```markdown
INPUT[select(showcase, option(1), option(2), option(3)):choice]
INPUT[select(option(pending), option(active), option(done)):status]
INPUT[select(option(low, Low Priority), option(high, High Priority)):priority]
```

**Arguments:**
- `showcase` - Display prominently
- `option(value)` - Simple option (value used as label)
- `option(value, displayName)` - Option with custom display name

**Example:**
```markdown
---
status: pending
---

INPUT[select(
  option(pending, 📋 Pending),
  option(in-progress, 🚧 In Progress),
  option(completed, ✅ Completed)
):status]
```

---

### 7. Inline Select (Compact Dropdown)

**Basic Syntax:**
```markdown
INPUT[inlineSelect(option(val1), option(val2)):property]
```

**With Arguments:**
```markdown
INPUT[inlineSelect(showcase, option(1, One), option(2, Two)):choice]
INPUT[inlineSelect(
  option(planning, 📋 Planning),
  option(in-progress, 🚧 In Progress),
  option(review, 👀 Review),
  option(done, ✅ Done)
):status]
```

**Arguments:**
- Same as Select field
- More compact display (inline dropdown vs. block)

---

### 8. Multi-Select (Multiple Choices)

**Basic Syntax:**
```markdown
INPUT[multiSelect(option(tag1), option(tag2), option(tag3)):tags]
```

**With Arguments:**
```markdown
INPUT[multiSelect(showcase, option(a, Label A), option(b, Label B)):items]
INPUT[multiSelect(
  option(javascript, JavaScript),
  option(python, Python),
  option(rust, Rust)
):languages]
```

**Arguments:**
- `showcase` - Display prominently
- `option(value)` or `option(value, displayName)` - Multiple allowed

**Example:**
```markdown
---
tags: []
---

**Tags:** INPUT[multiSelect(
  option(project),
  option(research),
  option(urgent),
  option(review)
):tags]
```

---

### 9. Date Picker

**Basic Syntax:**
```markdown
INPUT[date:startDate]
INPUT[datePicker:deadline]
```

**Example:**
```markdown
---
start-date: 2025-01-15
due-date: 2025-02-28
---

**Start Date:** INPUT[date:start-date]
**Due Date:** INPUT[datePicker:due-date]
```

**Note:** Both `date` and `datePicker` work identically. Uses format from plugin settings (default: YYYY-MM-DD).

---

### 10. Date-Time

**Basic Syntax:**
```markdown
INPUT[dateTime:createdAt]
INPUT[dateTime(showcase):timestamp]
```

**Example:**
```markdown
---
created-at: 2025-01-15T14:30:00
---

**Created:** INPUT[dateTime:created-at]
```

---

### 11. Time

**Basic Syntax:**
```markdown
INPUT[time:meetingTime]
INPUT[time:alarm]
```

**Example:**
```markdown
---
meeting-time: "14:30"
---

**Meeting Time:** INPUT[time:meeting-time]
```

---

### 12. Suggester (Autocomplete)

**Basic Syntax:**
```markdown
INPUT[suggester(optionQuery(#tag)):reference]
INPUT[suggester(useLinks(true)):note-reference]
```

**With Arguments:**
```markdown
INPUT[suggester(optionQuery(#project), useLinks(true)):linked-project]
INPUT[suggester(useLinks(false), allowOther(true)):custom-value]
INPUT[suggester(optionQuery("folder/path"), useLinks(partial)):partial-link]
```

**Arguments:**
- `optionQuery(#tag)` - Query by tag
- `optionQuery("folder/path")` - Query folder contents
- `useLinks(true/partial/false)` - How to format selected value
  - `true` - Full wikilink: `[[Note Name]]`
  - `partial` - Partial link: `Note Name`
  - `false` - Plain text: `Note Name`
- `allowOther(true/false)` - Allow custom values not in suggestions

**Example:**
```markdown
---
project-reference: ""
---

**Related Project:** INPUT[suggester(
  optionQuery(#project),
  useLinks(true)
):project-reference]
```

---

### 13. List

**Basic Syntax:**
```markdown
INPUT[list:items]
INPUT[list:tasks]
```

**With Arguments:**
```markdown
INPUT[list(addLabel(Add Item)):shopping-list]
INPUT[list(placeholder(Enter item)):items]
INPUT[list(multiLine(true)):notes]
INPUT[list(limit(10)):top-ten]
```

**Arguments:**
- `addLabel(text)` - Custom label for "Add" button
- `placeholder(text)` - Placeholder for new items
- `multiLine(true/false)` - Multi-line text entries
- `limit(n)` - Maximum number of items

**Example:**
```markdown
---
action-items: []
---

## Action Items
INPUT[list(addLabel(Add Action Item)):action-items]
```

---

### 14. List Suggester

**Basic Syntax:**
```markdown
INPUT[listSuggester(optionQuery(#tag)):items]
INPUT[listSuggester(useLinks(true)):references]
```

**With Arguments:**
```markdown
INPUT[listSuggester(
  optionQuery(#reference),
  useLinks(true)
):related-notes]
```

**Arguments:**
- Same as Suggester, but creates a list of selected items

---

### 15. Image Suggester

**Basic Syntax:**
```markdown
INPUT[imageSuggester(optionQuery("Attachments")):coverImage]
INPUT[imageSuggester(optionQuery("Images")):banner]
```

**Arguments:**
- `optionQuery("folder/path")` - Path to image folder

**Example:**
```markdown
---
cover-image: ""
---

**Cover Image:** INPUT[imageSuggester(
  optionQuery("Attachments/Images")
):cover-image]
```

---

### 16. Progress Bar (Display Only)

**Basic Syntax:**
```markdown
INPUT[progressBar:completion]
VIEW[progressBar]{progress}
```

**Note:** Progress bar is primarily for viewing. Use with slider for input.

**Example:**
```markdown
---
progress: 65
---

**Progress:** INPUT[slider(minValue(0), maxValue(100)):progress]%

VIEW[progressBar]{progress}
```

---

## View Fields

### 1. Math View (Default)

**Basic Syntax:**
```markdown
VIEW[{propertyName}]
VIEW[{property1} + {property2}]
```

**With Expressions:**
```markdown
VIEW[{budget} - {spent}]
VIEW[{price} * {quantity}]
VIEW[round({value}, 2)]
VIEW[{total} / {count}]
```

**Save Computed Values:**
```markdown
VIEW[{budget} - {spent}][math:remaining]
VIEW[math(saveAsBindTarget(total))]{price * quantity}
```

**With Arguments:**
```markdown
VIEW[{value}][math(class(warning))]
VIEW[{result}][math(hidden)]
```

**Built-in Functions:**
- `round(value, decimals)` - Round to decimal places
- `number(value)` - Convert to number
- `length(value)` - Get length of string/array

**Example:**
```markdown
---
budget-total: 10000
spent-marketing: 3500
spent-development: 4200
spent-operations: 1100
---

**Total Budget:** $VIEW[{budget-total}]
**Total Spent:** $VIEW[{spent-marketing} + {spent-development} + {spent-operations}]
**Remaining:** $VIEW[{budget-total} - {spent-marketing} - {spent-development} - {spent-operations}]
```

---

### 2. Text View

**Basic Syntax:**
```markdown
VIEW[{propertyName}][text]
VIEW[{description}][text]
```

**With Markdown Rendering:**
```markdown
VIEW[**Bold {text}**][text(renderMarkdown)]
VIEW[{title} - {subtitle}][text(renderMarkdown)]
VIEW[# {heading}][text(renderMarkdown)]
```

**With Arguments:**
```markdown
VIEW[{content}][text(class(custom-class))]
VIEW[{hidden-value}][text(hidden)]
```

**Arguments:**
- `renderMarkdown` - Render markdown syntax
- `class(className)` - Custom CSS class
- `hidden` - Hide the view field

---

### 3. Link View

**Basic Syntax:**
```markdown
`VIEW[{noteName}][link]`
`VIEW[{noteName}|Display Text][link]`
```

**Example:**
```markdown
---
project-name: "Project Alpha"
project-note: "Projects/Alpha"
---

**Project:** VIEW[{project-note}|{project-name}][link]
```

---

### 4. Image View

**Basic Syntax:**
```markdown
VIEW[{imagePath}][image]
VIEW[{coverImage}][image]
```

**Example:**
```markdown
---
cover-image: "Attachments/cover.png"
---

VIEW[{cover-image}][image]
```

---

## Buttons

### Inline Button Reference

**Basic Syntax:**
```markdown
BUTTON[buttonId]
BUTTON[buttonId, buttonId2, buttonId3]
```

**Example:**
```markdown
```meta-bind-button
id: archive-note
label: Archive
style: primary
action:
  type: command
  command: 'obsidian-kanban:archive-completed-cards'
```

Click to archive: BUTTON[archive-note]
```

---

### Code Block Button Definition

**Basic Structure:**
````markdown
```meta-bind-button
id: unique-button-id
label: Button Text
style: primary
icon: "icon-name"
tooltip: "Hover text description"
hidden: false
class: "custom-css-class"
cssStyle: "color: blue;"
action:
  type: actionType
  [action-specific properties]
```
````

---

### Button Styles

**Available Styles:**
- `default` - Grey button (standard appearance)
- `primary` - Accent color button (prominent)
- `destructive` - Red button (for destructive actions)
- `plain` - No background styling (minimal)

**Example:**
````markdown
```meta-bind-button
label: Delete Note
style: destructive
action:
  type: command
  command: 'app:delete-file'
```
````

---

### Button Properties

| Property | Type | Required | Description | Example |
|----------|------|----------|-------------|---------|
| `id` | string | No | Unique identifier for inline reference | `"my-button"` |
| `label` | string | Yes | Button text | `"Click Me"` |
| `style` | enum | Yes | Visual style | `primary`, `default`, `destructive`, `plain` |
| `icon` | string | No | Lucide icon name | `"file-code"`, `"save"`, `"trash"` |
| `tooltip` | string | No | Hover text | `"Click to save"` |
| `hidden` | boolean | No | Hide button | `true` or `false` |
| `class` | string | No | Custom CSS class | `"custom-button"` |
| `cssStyle` | string | No | Inline CSS | `"color: red; font-weight: bold;"` |
| `action` | object | No* | Single action | See action types below |
| `actions` | array | No* | Multiple actions | See multi-action buttons |

*Note: Either `action` or `actions` is required, but not both.

---

### Button Action Types

#### 1. Command Action

Execute Obsidian commands.

**Syntax:**
````markdown
```meta-bind-button
label: Open Palette
style: primary
action:
  type: command
  command: 'command-palette:open'
```
````

**Properties:**
- `type: command`
- `command: 'command-id'` - Obsidian command ID

**Common Commands:**
- `'command-palette:open'` - Open command palette
- `'obsidian-kanban:archive-completed-cards'` - Archive Kanban cards
- `'app:delete-file'` - Delete current file
- `'editor:toggle-bold'` - Toggle bold formatting

**Find Command IDs:**
Open Developer Console (Ctrl+Shift+I) and run:
```javascript
app.commands.listCommands()
```

---

#### 2. JavaScript Action

Execute JavaScript from a file.

**Syntax:**
````markdown
```meta-bind-button
label: Run Script
style: primary
action:
  type: js
  file: "scripts/myScript.js"
  args:
    arg1: "value1"
    arg2: 123
```
````

**Properties:**
- `type: js`
- `file: "path/to/script.js"` - Path to JavaScript file
- `args: {}` - Optional arguments object

**JavaScript File Example:**
```javascript
// scripts/myScript.js
module.exports = async (args, app) => {
  const { arg1, arg2 } = args;
  new Notice(`${arg1}: ${arg2}`);
};
```

---

#### 3. Inline JavaScript Action

Execute inline JavaScript code.

**Syntax:**
````markdown
```meta-bind-button
label: Run Code
style: primary
action:
  type: inlineJS
  code: |
    console.log('Button clicked!');
    new Notice('Hello from inline JS!');
```
````

**Properties:**
- `type: inlineJS`
- `code: "javascript code"` - Inline JavaScript

**Available Context:**
- `app` - Obsidian app object
- `Notice` - Obsidian Notice constructor
- Current note context

---

#### 4. Open Action

Open URLs or notes.

**Syntax:**
````markdown
```meta-bind-button
label: Open Note
style: primary
action:
  type: open
  link: "[[Note Name]]"
```

```meta-bind-button
label: Open Website
style: default
action:
  type: open
  link: "https://example.com"
```
````

**Properties:**
- `type: open`
- `link: "url or [[wikilink]]"` - URL or note link

---

#### 5. Input Action

Input text to command palette.

**Syntax:**
````markdown
```meta-bind-button
label: Search
style: primary
action:
  type: input
  str: "search term"
```
````

**Properties:**
- `type: input`
- `str: "text"` - Text to input to command palette

---

#### 6. Sleep Action

Add delays in action sequences.

**Syntax:**
````markdown
```meta-bind-button
label: Delayed Action
style: primary
actions:
  - type: updateMetadata
    bindTarget: status
    value: "processing"
  - type: sleep
    ms: 2000
  - type: updateMetadata
    bindTarget: status
    value: "completed"
```
````

**Properties:**
- `type: sleep`
- `ms: number` - Milliseconds to wait

---

#### 7. Update Metadata Action

Modify frontmatter properties.

**Syntax:**
````markdown
```meta-bind-button
label: Mark Complete
style: primary
action:
  type: updateMetadata
  bindTarget: completed
  evaluate: false
  value: true
```

```meta-bind-button
label: Increment Counter
style: default
action:
  type: updateMetadata
  bindTarget: count
  evaluate: true
  value: "x + 1"
```
````

**Properties:**
- `type: updateMetadata`
- `bindTarget: "propertyName"` - Property to update
- `evaluate: boolean` - Whether to evaluate value as expression
- `value: any` - New value or expression

**Evaluate Examples:**
- `evaluate: false`, `value: "completed"` → Set to literal string "completed"
- `evaluate: true`, `value: "x + 1"` → Increment current value by 1
- `evaluate: true`, `value: "!x"` → Toggle boolean value

---

#### 8. Templater Create Note Action

Create notes from Templater templates.

**Syntax:**
````markdown
```meta-bind-button
label: New Project
style: primary
action:
  type: templaterCreateNote
  templateFile: "Templates/Project Template.md"
  folderPath: "Projects"
  fileName: "New Project {{date}}"
  openNote: true
```
````

**Properties:**
- `type: templaterCreateNote`
- `templateFile: "path"` - Path to template file
- `folderPath: "path"` - Destination folder
- `fileName: "name"` - New file name (supports Templater syntax)
- `openNote: boolean` - Open after creation (optional)

---

#### 9. Run Templater File Action

Execute Templater template in current note.

**Syntax:**
````markdown
```meta-bind-button
label: Run Template
style: primary
action:
  type: runTemplaterFile
  templateFile: "Templates/Scripts/update-metadata.md"
```
````

**Properties:**
- `type: runTemplaterFile`
- `templateFile: "path"` - Path to Templater template

---

#### 10. Create Note Action

Simple note creation without Templater.

**Syntax:**
````markdown
```meta-bind-button
label: New Note
style: primary
action:
  type: createNote
  folderPath: "Notes"
  fileName: "Untitled Note"
  openNote: true
```
````

**Properties:**
- `type: createNote`
- `folderPath: "path"` - Destination folder
- `fileName: "name"` - New file name
- `openNote: boolean` - Open after creation (optional)

---

#### 11. Replace In Note Action

Find and replace text by line number.

**Syntax:**
````markdown
```meta-bind-button
label: Update Section
style: default
action:
  type: replaceInNote
  fromLine: 10
  toLine: 15
  replacement: "New content here"
```
````

**Properties:**
- `type: replaceInNote`
- `fromLine: number` - Start line number (0-indexed)
- `toLine: number` - End line number (0-indexed, inclusive)
- `replacement: "text"` - Replacement text

---

#### 12. Regexp Replace In Note Action

Find and replace using regular expressions.

**Syntax:**
````markdown
```meta-bind-button
label: Clean Formatting
style: default
action:
  type: regexpReplaceInNote
  regexp: "\\[\\[(.+?)\\]\\]"
  regexpFlags: "g"
  replacement: "$1"
```
````

**Properties:**
- `type: regexpReplaceInNote`
- `regexp: "pattern"` - Regular expression pattern
- `regexpFlags: "flags"` - Regex flags (g, i, m, etc.)
- `replacement: "text"` - Replacement text ($1, $2 for captures)

---

#### 13. Insert Into Note Action

Insert text at specific line number.

**Syntax:**
````markdown
```meta-bind-button
label: Add Entry
style: primary
action:
  type: insertIntoNote
  line: 20
  value: "## New Section\n\nContent here"
```
````

**Properties:**
- `type: insertIntoNote`
- `line: number` - Line number to insert at (0-indexed)
- `value: "text"` - Content to insert

---

#### 14. Replace Self Action

Replace the button code block itself.

**Syntax:**
````markdown
```meta-bind-button
label: Archive This Section
style: destructive
action:
  type: replaceSelf
  replacement: "> [!info] Archived\n> This section was archived."
```
````

**Properties:**
- `type: replaceSelf`
- `replacement: "text"` - Content to replace button with

**Use Case:** One-time actions that remove themselves after execution.

---

### Multi-Action Buttons

Execute multiple actions in sequence.

**Syntax:**
````markdown
```meta-bind-button
label: Complete Workflow
style: primary
actions:
  - type: updateMetadata
    bindTarget: status
    evaluate: false
    value: "completed"
  - type: updateMetadata
    bindTarget: completed-date
    evaluate: false
    value: "2025-12-14"
  - type: command
    command: 'obsidian-kanban:archive-completed-cards'
  - type: open
    link: "[[Projects MOC]]"
```
````

**Properties:**
- `actions: []` - Array of action objects
- Each action follows the same syntax as single actions

**Execution Order:**
- Actions execute sequentially (top to bottom)
- Use `sleep` action to add delays between steps

**Example: Complex Project Completion**
````markdown
```meta-bind-button
label: Complete Project
style: primary
actions:
  - type: updateMetadata
    bindTarget: status
    evaluate: false
    value: "completed"
  - type: updateMetadata
    bindTarget: completion-date
    evaluate: false
    value: "{{date:YYYY-MM-DD}}"
  - type: updateMetadata
    bindTarget: progress
    evaluate: false
    value: 100
  - type: sleep
    ms: 500
  - type: command
    command: 'obsidian-kanban:archive-completed-cards'
  - type: open
    link: "[[Projects Dashboard]]"
```
````

---

## Bind Target Syntax

### Structure

**Format:**
```
[storageType^]storagePath#propertyName
```

### Components

1. **Storage Type** (optional): `storageType^`
   - `memory^` - Temporary storage (not saved)
   - Omit for frontmatter (default)

2. **Storage Path** (optional): `storagePath`
   - Omit for current note
   - `NoteName` - Specific note
   - `Folder/NoteName` - Note in folder

3. **Property Name** (required): `#propertyName`
   - `propertyName` - Simple property
   - `property.nested.path` - Nested property
   - `['Property With Spaces']` - Property with spaces

### Examples

**Current Note Frontmatter:**
```markdown
INPUT[toggle:completed]
INPUT[text:title]
VIEW[{status}]
```

**Specific Note:**
```markdown
INPUT[select:Projects/ProjectA#status]
VIEW[{OtherNote#propertyName}]
```

**Nested Property:**
```markdown
INPUT[number:project.budget.total]
INPUT[text:author.name]
```

**Property with Spaces:**
```markdown
INPUT[date:['Due Date']]
INPUT[text:['Project Name']]
```

**Memory Storage (Temporary):**
```markdown
INPUT[text:memory^tempVar]
VIEW[{memory^calculation}]
```

**Cross-Note Binding:**
```markdown
---
project-status: ""
---

**Status from Project A:** VIEW[{Projects/Project A#status}]
**Update Status:** INPUT[inlineSelect(
  option(planning),
  option(active),
  option(done)
):Projects/Project A#status]
```

---

## JavaScript View Fields

Execute JavaScript to compute and display values.

### Basic Syntax

````markdown
```meta-bind-js-view
{property1} as var1
{property2} as var2
save to {outputProperty}
---
// JavaScript code here
return result;
```
````

### Structure

**Three Parts:**
1. **Binding Section** (above `---`): Bind frontmatter properties to variables
2. **Code Section** (below `---`): JavaScript code
3. **Return Value**: What to display/save

### Context API

**Available Objects:**
- `context.bound.variableName` - Access bound variables
- `context.metadata.frontmatter` - Direct frontmatter access
- `engine.markdown.create()` - Create markdown content
- `engine.markdown.createEl()` - Create HTML elements

### Examples

#### Example 1: Simple Calculation

````markdown
---
number1: 10
number2: 5
result: 0
---

```meta-bind-js-view
{number1} as n1
{number2} as n2
save to {result}
---
return context.bound.n1 * context.bound.n2;
```
````

#### Example 2: Formatted Output

````markdown
---
distance: 42
time: 3.5
---

```meta-bind-js-view
{distance} as dist
{time} as t
---
const speed = context.bound.dist / context.bound.t;
return engine.markdown.create(`**Average Speed:** ${speed.toFixed(2)} km/h`);
```
````

#### Example 3: Conditional Display

````markdown
---
score: 85
---

```meta-bind-js-view
{score} as score
---
const s = context.bound.score;
let grade;
if (s >= 90) grade = "A";
else if (s >= 80) grade = "B";
else if (s >= 70) grade = "C";
else grade = "F";

return engine.markdown.create(`**Grade:** ${grade} (${s}%)`);
```
````

#### Example 4: List Processing

````markdown
---
tasks:
  - "Task 1"
  - "Task 2"
  - "Task 3"
---

```meta-bind-js-view
{tasks} as taskList
---
const tasks = context.bound.taskList || [];
const total = tasks.length;
return engine.markdown.create(`**Total Tasks:** ${total}`);
```
````

#### Example 5: Date Calculations

````markdown
---
start-date: "2025-01-01"
end-date: "2025-12-31"
---

```meta-bind-js-view
{start-date} as start
{end-date} as end
---
const s = new Date(context.bound.start);
const e = new Date(context.bound.end);
const days = Math.ceil((e - s) / (1000 * 60 * 60 * 24));
return engine.markdown.create(`**Duration:** ${days} days`);
```
````

---

## Template Examples

### Template 1: Project Note

````markdown
---
title: <%= tp.file.title %>
status: planning
priority: medium
progress: 0
start-date: ""
due-date: ""
completed: false
tags:
  - project
---

# <%= tp.file.title %>

## Metadata

**Status:** INPUT[inlineSelect(
  option(planning, 📋 Planning),
  option(in-progress, 🚧 In Progress),
  option(review, 👀 Review),
  option(completed, ✅ Completed)
):status]

**Priority:** INPUT[inlineSelect(
  option(low, 🟢 Low),
  option(medium, 🟡 Medium),
  option(high, 🟠 High),
  option(critical, 🔴 Critical)
):priority]

**Progress:** INPUT[slider(addLabels, minValue(0), maxValue(100)):progress]%
VIEW[progressBar]{progress}

**Start Date:** INPUT[date:start-date]
**Due Date:** INPUT[date:due-date]
**Completed:** INPUT[toggle:completed]

## Description

INPUT[textArea(class(meta-bind-full-width), placeholder(Project description...)):description]

## Action Items

INPUT[list(addLabel(Add Action Item)):action-items]

## Notes

INPUT[textArea(class(meta-bind-full-width)):notes]

---

```meta-bind-button
label: Mark Complete
style: primary
actions:
  - type: updateMetadata
    bindTarget: status
    evaluate: false
    value: "completed"
  - type: updateMetadata
    bindTarget: completed
    evaluate: false
    value: true
  - type: updateMetadata
    bindTarget: progress
    evaluate: false
    value: 100
```

```meta-bind-button
label: Archive Project
style: destructive
action:
  type: command
  command: 'app:delete-file'
```
````

---

### Template 2: Meeting Notes

````markdown
---
meeting-title: <%= tp.file.title %>
meeting-date: <%= tp.date.now("YYYY-MM-DD") %>
meeting-time: <%= tp.date.now("HH:mm") %>
attendees: []
topics: []
action-items: []
follow-up-date: ""
completed: false
tags:
  - meeting
---

# <%= tp.file.title %>

## Meeting Details

**Date:** INPUT[date:meeting-date]
**Time:** INPUT[time:meeting-time]
**Completed:** INPUT[toggle:completed]
**Follow-up Date:** INPUT[date:follow-up-date]

## Attendees

INPUT[list(addLabel(Add Attendee)):attendees]

## Topics Discussed

INPUT[list(addLabel(Add Topic), multiLine(true)):topics]

## Notes

INPUT[textArea(class(meta-bind-full-width), placeholder(Meeting notes...)):notes]

## Action Items

INPUT[list(addLabel(Add Action Item)):action-items]

## Decisions Made

INPUT[textArea(class(meta-bind-full-width)):decisions]

---

```meta-bind-button
label: Create Follow-up Meeting
style: primary
action:
  type: templaterCreateNote
  templateFile: "Templates/Meeting Template.md"
  folderPath: "Meetings"
  fileName: "Follow-up - {{date:YYYY-MM-DD}}"
  openNote: true
```

```meta-bind-button
label: Mark Complete
style: primary
action:
  type: updateMetadata
  bindTarget: completed
  evaluate: false
  value: true
```
````

---

### Template 3: Task/Report Note

````markdown
---
title: <%= tp.file.title %>
status: pending
priority: medium
progress: 0
estimated-hours: 0
actual-hours: 0
start-date: ""
due-date: ""
completed: false
reviewed: false
tags:
  - task
---

# <%= tp.file.title %>

## Task Details

**Status:** INPUT[inlineSelect(
  option(pending, ⏳ Pending),
  option(active, 🚧 Active),
  option(blocked, 🚫 Blocked),
  option(done, ✅ Done)
):status]

**Priority:** INPUT[slider(addLabels, minValue(1), maxValue(5)):priority]

**Progress:** INPUT[slider(addLabels, minValue(0), maxValue(100)):progress]%
VIEW[progressBar]{progress}

## Dates

**Start:** INPUT[date:start-date]
**Due:** INPUT[date:due-date]
**Completed:** INPUT[toggle:completed]
**Reviewed:** INPUT[toggle:reviewed]

## Time Tracking

**Estimated Hours:** INPUT[number(minValue(0)):estimated-hours]
**Actual Hours:** INPUT[number(minValue(0)):actual-hours]
**Difference:** VIEW[{actual-hours} - {estimated-hours}] hours

## Description

INPUT[textArea(class(meta-bind-full-width), placeholder(Task description...)):description]

## Checklist

INPUT[list(addLabel(Add Step)):checklist]

## Notes

INPUT[textArea(class(meta-bind-full-width)):notes]

---

```meta-bind-button
label: Mark Complete
style: primary
actions:
  - type: updateMetadata
    bindTarget: status
    evaluate: false
    value: "done"
  - type: updateMetadata
    bindTarget: completed
    evaluate: false
    value: true
  - type: updateMetadata
    bindTarget: progress
    evaluate: false
    value: 100
```
````

---

### Template 4: Reading/Learning Note

````markdown
---
title: <%= tp.file.title %>
type: book
status: to-read
progress: 0
rating: 0
start-date: ""
finish-date: ""
completed: false
author: ""
source: ""
tags:
  - reading
---

# <%= tp.file.title %>

## Metadata

**Type:** INPUT[inlineSelect(
  option(book, 📚 Book),
  option(article, 📄 Article),
  option(video, 🎥 Video),
  option(course, 🎓 Course)
):type]

**Status:** INPUT[inlineSelect(
  option(to-read, 📋 To Read),
  option(reading, 📖 Reading),
  option(completed, ✅ Completed)
):status]

**Progress:** INPUT[slider(addLabels, minValue(0), maxValue(100)):progress]%
VIEW[progressBar]{progress}

**Rating:** INPUT[slider(addLabels, minValue(0), maxValue(5), stepSize(0.5)):rating] / 5

**Author:** INPUT[text:author]
**Source:** INPUT[text:source]

## Dates

**Started:** INPUT[date:start-date]
**Finished:** INPUT[date:finish-date]
**Completed:** INPUT[toggle:completed]

## Summary

INPUT[textArea(class(meta-bind-full-width), placeholder(Brief summary...)):summary]

## Key Takeaways

INPUT[list(addLabel(Add Takeaway), multiLine(true)):takeaways]

## Notes

INPUT[textArea(class(meta-bind-full-width)):notes]

## Related

INPUT[listSuggester(optionQuery(#reading), useLinks(true)):related-notes]

---

```meta-bind-button
label: Mark Completed
style: primary
actions:
  - type: updateMetadata
    bindTarget: status
    evaluate: false
    value: "completed"
  - type: updateMetadata
    bindTarget: completed
    evaluate: false
    value: true
  - type: updateMetadata
    bindTarget: progress
    evaluate: false
    value: 100
  - type: updateMetadata
    bindTarget: finish-date
    evaluate: false
    value: "{{date:YYYY-MM-DD}}"
```
````

---

### Template 5: Budget Tracker

````markdown
---
title: <%= tp.file.title %>
budget-total: 0
spent-operations: 0
spent-marketing: 0
spent-development: 0
spent-other: 0
remaining: 0
tags:
  - budget
  - finance
---

# <%= tp.file.title %>

## Budget Overview

**Total Budget:** $INPUT[number(minValue(0)):budget-total]

## Expenditures

**Operations:** $INPUT[number(minValue(0)):spent-operations]
**Marketing:** $INPUT[number(minValue(0)):spent-marketing]
**Development:** $INPUT[number(minValue(0)):spent-development]
**Other:** $INPUT[number(minValue(0)):spent-other]

## Calculations

**Total Spent:** $VIEW[{spent-operations} + {spent-marketing} + {spent-development} + {spent-other}]

**Remaining Budget:** $VIEW[{budget-total} - {spent-operations} - {spent-marketing} - {spent-development} - {spent-other}][math:remaining]

**Percentage Used:** VIEW[round(({spent-operations} + {spent-marketing} + {spent-development} + {spent-other}) / {budget-total} * 100, 1)]%

```meta-bind-js-view
{budget-total} as total
{spent-operations} as ops
{spent-marketing} as mkt
{spent-development} as dev
{spent-other} as other
---
const spent = context.bound.ops + context.bound.mkt + context.bound.dev + context.bound.other;
const remaining = context.bound.total - spent;
const percentage = (spent / context.bound.total * 100).toFixed(1);

let status = "✅ On Track";
if (percentage > 90) status = "🔴 Over Budget Risk";
else if (percentage > 75) status = "🟡 High Usage";

return engine.markdown.create(`**Status:** ${status} (${percentage}% used)`);
```

## Notes

INPUT[textArea(class(meta-bind-full-width)):notes]
````

---

## Plugin Configuration

### Location
```
.obsidian/plugins/obsidian-meta-bind-plugin/data.json
```

### Configuration Options

```json
{
  "devMode": false,
  "ignoreCodeBlockRestrictions": false,
  "preferredDateFormat": "YYYY-MM-DD",
  "firstWeekday": {
    "index": 1,
    "name": "Monday",
    "shortName": "Mo"
  },
  "syncInterval": 200,
  "enableJs": true,
  "viewFieldDisplayNullAsEmpty": false,
  "enableSyntaxHighlighting": true,
  "enableEditorRightClickMenu": true,
  "inputFieldTemplates": [],
  "buttonTemplates": [],
  "excludedFolders": ["templates"]
}
```

### Key Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `devMode` | boolean | false | Enable developer features |
| `ignoreCodeBlockRestrictions` | boolean | false | Allow Meta Bind in all code blocks |
| `preferredDateFormat` | string | "YYYY-MM-DD" | Date format for date pickers |
| `firstWeekday` | object | Monday | First day of week in calendars |
| `syncInterval` | number | 200 | Metadata sync interval (ms) |
| `enableJs` | boolean | true | Enable JavaScript view fields |
| `viewFieldDisplayNullAsEmpty` | boolean | false | Display null as empty string |
| `enableSyntaxHighlighting` | boolean | true | Syntax highlighting in code blocks |
| `enableEditorRightClickMenu` | boolean | true | Right-click menu in editor |
| `inputFieldTemplates` | array | [] | Custom input field templates |
| `buttonTemplates` | array | [] | Custom button templates |
| `excludedFolders` | array | ["templates"] | Folders to exclude from Meta Bind |

---

## Best Practices

### 1. Organize with Templates
- Create reusable templates with Meta Bind fields
- Use consistent naming for properties across templates
- Keep templates in excluded folders to avoid performance issues

### 2. Performance Considerations
- Limit JavaScript view fields in large notes
- Use `excludedFolders` to exclude template folders
- Avoid excessive nested bindings
- Use `syncInterval` to balance responsiveness and performance

### 3. Property Naming
- Use kebab-case for multi-word properties: `start-date`, `action-items`
- Avoid spaces in property names (use bracket notation if needed)
- Be consistent across notes for easier querying

### 4. Button Organization
- Define complex buttons once, reference with `BUTTON[id]`
- Use descriptive button labels
- Group related actions in multi-action buttons
- Use appropriate styles (`destructive` for dangerous actions)

### 5. Input Field Selection
- Use `inlineSelect` for compact status fields
- Use `slider` with `addLabels` for numeric ranges
- Use `textArea` with `class(meta-bind-full-width)` for large text
- Use `suggester` for note/tag references

### 6. View Field Usage
- Default to `math` view for calculations
- Use `text(renderMarkdown)` for formatted display
- Save computed values with `[math:propertyName]` syntax
- Use JavaScript views for complex logic only

---

## Quick Reference Card

### Input Field Syntax
```markdown
INPUT[type:property]
INPUT[type(args):property]
```

### View Field Syntax
```markdown
VIEW[{property}]
VIEW[{property}][type]
VIEW[expression][type:saveTarget]
```

### Button Syntax
```markdown
BUTTON[id]
```

````markdown
```meta-bind-button
label: Text
style: primary|default|destructive|plain
action:
  type: command|js|open|updateMetadata|...
  [action properties]
```
````

### Bind Target Syntax
```markdown
property                    # Current note
NoteName#property          # Other note
folder/note#property       # Note in folder
property.nested            # Nested property
['Property Name']          # Property with spaces
memory^tempVar             # Temporary storage
```

### Common Patterns
```markdown
# Toggle
INPUT[toggle:completed]

# Status Dropdown
INPUT[inlineSelect(option(todo), option(doing), option(done)):status]

# Progress Bar
INPUT[slider(addLabels, minValue(0), maxValue(100)):progress]%
VIEW[progressBar]{progress}

# Date Range
**Start:** INPUT[date:start-date]
**End:** INPUT[date:end-date]

# List Input
INPUT[list(addLabel(Add Item)):items]

# Math View
VIEW[{total} - {spent}][math:remaining]

# Complete Button
```meta-bind-button
label: Mark Complete
style: primary
action:
  type: updateMetadata
  bindTarget: completed
  evaluate: false
  value: true
```
```

---

## Resources

- **Official Documentation:** https://www.moritzjung.dev/obsidian-meta-bind-plugin-docs/
- **Plugin Version:** 1.4.6
- **Author:** Moritz Jung
- **Local Documentation:** `04-library/02-pkb-and-pkm-learning/-reference/-official-documentation/-plugin-meta-bind/`

---

**Last Updated:** 2025-12-14
**Version:** 1.0
**For:** Meta Bind Plugin v1.4.6
