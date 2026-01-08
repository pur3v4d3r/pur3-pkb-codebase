---
type: "reference"
id: "20260108000006"
status: "active"
maturity: "evergreen"
confidence: "established"
link-up: "[[architecture-overview]]"
tags:
  - "year/2026"
  - "spes-system"
  - "reference"
  - "obsidian"
  - "plugins"
  - "syntax"
aliases:
  - "Obsidian Plugin Syntax Reference"
  - "Templater Meta-Bind Dataview QuickAdd Guide"
created: "2026-01-08"
modified: "2026-01-08"
---

# Obsidian Plugin Syntax Reference

> [!abstract] Purpose
> Comprehensive syntax reference for Templater, Meta-Bind, Dataview/DataviewJS, and QuickAdd. Includes examples with error handling and best practices.

---

## 🎯 Templater

### User Selection from Options

```javascript
<%*
// User selection from options
const choice = await tp.system.suggester(
  ["Option A", "Option B", "Option C"],  // Display names
  ["value_a", "value_b", "value_c"],      // Return values
  false,                                   // throwOnCancel (false = don't error on cancel)
  "Select an option:"                      // Placeholder text
);

// Handle cancellation
if (!choice) {
  new Notice("Selection cancelled.");
  return;  // Exit template
}

tR += `You selected: ${choice}`;
_%>
```

### Multi-Select with Array Handling

```javascript
<%*
// Multi-select (returns array)
const selected = await tp.system.suggester(
  ["Item 1", "Item 2", "Item 3", "Item 4"],
  ["item1", "item2", "item3", "item4"],
  true,  // Allow multiple selections
  "Select one or more items:"
);

// Handle array or single value
const selectedArray = Array.isArray(selected) ? selected : [selected];

// Handle cancellation
if (!selectedArray || selectedArray.length === 0) {
  new Notice("No selections made. Template cancelled.");
  return;
}

// Format as YAML list
const yamlList = selectedArray.map(item => `  - ${item}`).join('\n');
tR += yamlList;
_%>
```

### Text Input with Validation

```javascript
<%*
// Text input with validation
const title = await tp.system.prompt("Enter title:", "Default Value");

// Validate input
if (!title || title.trim() === "") {
  new Notice("❌ Title required. Template cancelled.");
  return;
}

// Sanitize for filename (remove special characters)
const sanitized = title.replace(/[\\/:*?"<>|]/g, "-");

tR += `Title: ${title}`;
_%>
```

### File Operations

```javascript
<%*
// Get current file properties
const fileName = tp.file.title;
const folder = tp.file.folder(true);  // true = include full path
const filePath = tp.file.path(true);

// Move/rename file
const newFileName = `prefix-${fileName}-suffix.md`;
await tp.file.move(`${folder}/${newFileName}`);

// Create new file
const content = "# New File\n\nContent here";
await tp.file.create_new(content, "New File Name", false, folder);
_%>
```

### Cursor Placement

```markdown
## Section 1
<% tp.file.cursor(1) %>

## Section 2
<% tp.file.cursor(2) %>

## Section 3
<% tp.file.cursor(3) %>
```

### Date Formatting

```javascript
<%*
// Various date formats
const today = tp.date.now("YYYY-MM-DD");
const timestamp = tp.date.now("YYYYMMDDHHmmss");
const readable = tp.date.now("dddd, MMMM Do, YYYY");
const weekNumber = tp.date.now("gggg-[W]WW");

// Date offset (7 days from now)
const nextWeek = tp.date.now("YYYY-MM-DD", 7);
const lastWeek = tp.date.now("YYYY-MM-DD", -7);
_%>
```

### Error Handling

```javascript
<%*
try {
  // Risky operation
  const result = await tp.system.prompt("Enter value:");

  // Validation
  if (!result) {
    throw new Error("No value provided");
  }

  tR += `Result: ${result}`;

} catch (error) {
  new Notice(`❌ Error: ${error.message}`);
  console.error("Template error:", error);
  return;  // Exit gracefully
}
_%>
```

---

## 🎨 Meta-Bind

### View Fields (Read-Only)

```markdown
<!-- Display frontmatter values -->
**Created**: `VIEW[{created}]`
**Status**: `VIEW[{status}]`
**Rating**: `VIEW[{rating}]` / 10
```

### Input Fields

```markdown
<!-- Text input -->
`INPUT[text:title]`

<!-- Suggester (dropdown) -->
`INPUT[suggester(option(Low), option(Medium), option(High)):priority]`

<!-- Slider -->
`INPUT[slider(min(1), max(10)):confidence]`

<!-- Toggle (checkbox) -->
`INPUT[toggle:is_tested]`

<!-- Text area (multi-line) -->
`INPUT[text_area:notes]`

<!-- Number input -->
`INPUT[number:usage-count]`
```

### Buttons

```markdown
<!-- Button with command -->
`BUTTON[insert-component]`
```

**Button Definition** (in Meta-Bind settings):
```json
{
  "label": "Insert Component",
  "action": "command",
  "command": "quickadd:runMacro",
  "args": { "macro": "Insert Prompt Component" },
  "class": "mod-cta"
}
```

---

## 📊 Dataview

### Table Queries

```dataview
TABLE
  status AS "Status",
  priority AS "Priority",
  file.mtime AS "Modified"
FROM "prompts"
WHERE type = "prompt"
SORT priority DESC, file.mtime DESC
LIMIT 10
```

### List Queries

```dataview
LIST
FROM "02-projects"
WHERE status = "active"
SORT file.name ASC
```

### Task Queries

```dataview
TASK
FROM "05-tasks"
WHERE !completed
WHERE due <= date(today) + dur(7 days)
SORT due ASC
```

---

## 📊 DataviewJS

### Basic Query with Error Handling

```dataviewjs
try {
  const pages = dv.pages('"prompts"')
    .where(p => p.type === "system")
    .sort(p => p.priority, 'desc');

  if (pages.length === 0) {
    dv.paragraph("*No prompts found. Create one with QuickAdd.*");
  } else {
    dv.table(
      ["Prompt", "Status", "Priority"],
      pages.map(p => [p.file.link, p.status, p.priority])
    );
  }
} catch (e) {
  dv.paragraph(`⚠️ Query error: ${e.message}`);
  console.error("Dataview error:", e);
}
```

### Filtering by Multiple Criteria

```dataviewjs
try {
  const currentFile = dv.current();
  const relatedPages = dv.pages()
    .where(p => p.file.path !== currentFile.file.path)
    .where(p => p.type === "prompt")
    .where(p => {
      // Complex filtering logic
      if (p.category === currentFile.category) return true;
      if (p.tags && p.tags.includes("#related")) return true;
      return false;
    })
    .sort(p => p.rating, 'desc')
    .limit(5);

  if (relatedPages.length > 0) {
    dv.table(
      ["Name", "Category", "Rating"],
      relatedPages.map(p => [p.file.link, p.category, p.rating])
    );
  } else {
    dv.paragraph("*No related pages found.*");
  }
} catch (e) {
  dv.paragraph(`⚠️ Error: ${e.message}`);
}
```

### Aggregation and Statistics

```dataviewjs
try {
  const prompts = dv.pages('"prompts"')
    .where(p => p.type === "prompt");

  const totalCount = prompts.length;
  const avgRating = prompts
    .map(p => parseFloat(p.rating) || 0)
    .reduce((sum, r) => sum + r, 0) / totalCount;

  const byStatus = prompts.groupBy(p => p.status);

  dv.header(2, "Prompt Statistics");
  dv.list([
    `Total Prompts: ${totalCount}`,
    `Average Rating: ${avgRating.toFixed(2)} / 10`,
    `Active: ${byStatus.get("active")?.length || 0}`,
    `Testing: ${byStatus.get("testing")?.length || 0}`,
    `Production: ${byStatus.get("production")?.length || 0}`
  ]);

} catch (e) {
  dv.paragraph(`⚠️ Error: ${e.message}`);
}
```

---

## ⚡ QuickAdd

### Basic Macro Structure

```javascript
module.exports = async (params) => {
  const { app, quickAddApi } = params;

  try {
    // Get user input
    const title = await quickAddApi.inputPrompt("Prompt title:");
    if (!title) return;  // User cancelled

    const type = await quickAddApi.suggester(
      ["System Prompt", "User Prompt", "Chain"],
      ["system", "user", "chain"]
    );
    if (!type) return;

    // Generate filename
    const fileName = `${title.replace(/[\\/:*?"<>|]/g, "-")}.md`;
    const folder = `prompts/${type}`;

    // Create file content
    const content = `---
title: ${title}
type: ${type}
created: ${new Date().toISOString().split('T')[0]}
---

# ${title}

`;

    // Create file
    await app.vault.create(`${folder}/${fileName}`, content);
    new Notice(`✅ Created: ${fileName}`);

  } catch (error) {
    new Notice(`❌ Error: ${error.message}`);
    console.error("QuickAdd macro error:", error);
  }
};
```

### File Existence Check

```javascript
module.exports = async (params) => {
  const { app, quickAddApi } = params;

  const filePath = "path/to/file.md";
  const fileExists = app.vault.getAbstractFileByPath(filePath);

  if (fileExists) {
    new Notice("File already exists!");
    return;
  }

  // Create file...
};
```

### Reading and Modifying Files

```javascript
module.exports = async (params) => {
  const { app, quickAddApi } = params;

  try {
    // Read file
    const filePath = "path/to/file.md";
    const file = app.vault.getAbstractFileByPath(filePath);

    if (!file) {
      new Notice("❌ File not found");
      return;
    }

    const content = await app.vault.read(file);

    // Modify content
    const newContent = content + "\n\nAppended text";

    // Write back
    await app.vault.modify(file, newContent);
    new Notice("✅ File updated");

  } catch (error) {
    new Notice(`❌ Error: ${error.message}`);
  }
};
```

---

## 🎓 Best Practices

### 1. Always Handle Cancellation

```javascript
const input = await tp.system.prompt("Enter value:");
if (!input) {
  new Notice("Cancelled.");
  return;  // Exit gracefully
}
```

### 2. Validate User Input

```javascript
const rating = await tp.system.prompt("Rating (0-10):");
const parsed = parseFloat(rating);

if (isNaN(parsed) || parsed < 0 || parsed > 10) {
  new Notice("❌ Invalid rating. Must be 0-10.");
  return;
}
```

### 3. Use Try-Catch for Async Operations

```javascript
try {
  await someAsyncOperation();
} catch (error) {
  new Notice(`❌ Error: ${error.message}`);
  console.error(error);
  return;
}
```

### 4. Provide User Feedback

```javascript
new Notice("✅ Success!");
new Notice("⚠️ Warning message");
new Notice("❌ Error occurred");
```

### 5. No Hardcoded Paths

```javascript
// BAD
const folder = "D:/vault/prompts";

// GOOD
const folder = tp.file.folder(true);
const folder = `${app.vault.getRoot().path}/prompts`;
```

---

## 🔗 Integration Patterns

### Templater + Meta-Bind

```markdown
<%*
// Generate metadata with Templater
const status = await tp.system.suggester(
  ["Active", "Testing", "Production"],
  ["active", "testing", "production"]
);
tR += `status: "${status}"`;
_%>
---

<!-- Use Meta-Bind to display/edit -->
**Status**: `VIEW[{status}]`
**Update**: `INPUT[suggester(option(active), option(testing), option(production)):status]`
```

### Templater + Dataview

```markdown
<%*
// Templater generates file
const category = await tp.system.prompt("Category:");
tR += `category: "${category}"`;
_%>
---

<!-- Dataview queries based on category -->
```dataview
LIST
WHERE category = this.category
WHERE file.path != this.file.path
```
```

### QuickAdd + Templater

```javascript
// QuickAdd macro triggers Templater
module.exports = async (params) => {
  const { app, quickAddApi } = params;

  // User selects template
  const template = await quickAddApi.suggester(
    ["System Prompt", "Few-Shot", "General"],
    ["_system-prompt-template.md", "_few-shot-template.md", "_prompt-general-template.md"]
  );

  // Trigger Templater on selected template
  app.commands.executeCommandById(`templater-obsidian:insert-${template}`);
};
```

---

## 📚 Additional Resources

- [[00-meta/obsidian-plugin-configurations]] - Plugin settings reference
- [[pkb-automation-templater-templates]] - More Templater examples
- [[pkb-automation-data-view-quiries]] - More Dataview examples
- [[pkb-automation-scripts]] - QuickAdd macro library

---

*Reference Version: 1.0.0 | Created: 2026-01-08*
*Part of SPES Documentation*
