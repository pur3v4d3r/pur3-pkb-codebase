---
title: Reference_Templater-Cheat-Sheet_🆔20251025160911
id: 20251025161010
aliases:
  - academic/reports
  - pkb/reference/templater
  - reoprts
  - templater
type: report
status:
priority:
created: 2025-10-25T16:10:10
source: gemini-2.5-pro
url: https://gemini.google.com/app/6149dc7f56c1daa7
tags:
  - type/report
  - type/report/educational
  - pkb/plugin/templater
date created: 2025-10-25T16:10:10.000-04:00
date modified: 2025-10-26T06:08:22.393-04:00
---

> [!the-purpose]
> Here is a comprehensive reference note for the Obsidian Templater plugin, designed for your Personal Knowledge Base. I have been extra careful to ensure all code blocks and backticks are correctly formatted so you can copy and paste them directly into your Obsidian note.

-----

# Obsidian Templater: A Reference Guide ⚙️

## 1\. Introduction to Templater

**Templater** is a powerful community plugin for Obsidian that supercharges your templates. Instead of just static text, it allows you to insert *dynamic* information, execute JavaScript code, and run system commands, turning your templates into interactive scripts. This note serves as a practical reference for the most common and useful Templater functions you'll need.

## 2\. Core Syntax

Templater has two primary syntaxes you'll use inside your template files:

  - **Inline Command:** `<% … %>`
      - This is used for simple expressions or commands that return a value to be inserted. The plugin executes the code inside and replaces the entire tag with the resulting string.
  - **JavaScript Code Block:** `<%* … %>`
      - This is used for more complex, multi-line JavaScript. This block allows you to define variables, use logic (like `if` statements), and call functions *without* automatically inserting a value. You must use `tR` (Template Result) to output values.

## 3\. 🗓️ Date and Time (`tp.date`)

This is one of the most-used modules. It uses **Moment.js** syntax for formatting.

### Basic Command

The core function is `tp.date.now(FORMAT_STRING)`.

  - **Get ISO-like Datetime:** (As you requested)

  ```markdown
    <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
    ```

  - **Get Just the Year:**

    ```markdown
    <% tp.date.now("YYYY") %>
    ```

### Other Common Date Examples

  - **Standard Date (e.g., 2025-10-25):**

    ```markdown
    <% tp.date.now("YYYY-MM-DD") %>
    ```

  - **Readable Date (e.g., October 25th, 2025):**

    ```markdown
    <% tp.date.now("MMMM Do, YYYY") %>
    ```

  - **Just the Time (e.g., 16:02:30):**

    ```markdown
    <% tp.date.now("HH:mm:ss") %>
    ```

  - **Day of the Week (e.g., Saturday):**

    ```markdown
    <% tp.date.now("dddd") %>
    ```

  - **Relative Dates:**

    ```markdown
    Tomorrow: <% tp.date.tomorrow("YYYY-MM-DD") %>
    Yesterday: <% tp.date.yesterday("YYYY-MM-DD") %>
    ```

### Common Moment.js Format Tokens

| Token | Output Example | Description |
| :--- | :--- | :--- |
| `YYYY` | `2025` | 4-digit year |
| `YY` | `25` | 2-digit year |
| `MMMM` | `October` | Full month name |
| `MMM` | `Oct` | Short month name |
| `MM` | `10` | Month number (01-12) |
| `DD` | `25` | Day of month (01-31) |
| `Do` | `25th` | Day of month with ordinal |
| `dddd` | `Saturday` | Full day name |
| `ddd` | `Sat` | Short day name |
| `HH` | `16` | Hour (24-hour, 00-23) |
| `hh` | `04` | Hour (12-hour, 01-12) |
| `mm` | `02` | Minute (00-59) |
| `ss` | `30` | Second (00-59) |
| `A` | `PM` | AM/PM |

## 4\. 📄 File Information (`tp.file`)

This module lets you access information about the *current* note you are creating or editing.

  - **Get the File's Title:**

    ```markdown
    <% tp.file.title %>
    ```

    *Note: If you run this in a *new* note before it's saved, it might be "Untitled".*

  - **Get Creation Date:** (Formatted)

    ```markdown
    <% tp.file.creation_date("YYYY-MM-DD") %>
    ```

  - **Get Last Modified Date:**

    ```markdown
    <% tp.file.last_modified_date("dddd, MMMM Do YYYY @ HH:mm") %>
    ```

  - **Get File Path:** (Relative to your vault)

    ```markdown
    <% tp.file.path() %>
    ```

  - **Rename the File:**

    ```markdown
    <% tp.file.rename("New Note Title") %>
    ```

## 5\. 🖥️ System and User Interaction (`tp.system`)

These functions allow your templates to become interactive.

  - **Prompt for Input:**
    This asks the user for a text value. It's an `async` function, so it must be "awaited" inside a `<%* … %>` block.

    ```markdown
    <%*
    const name = await tp.system.prompt("What is your name?")
    tR += `Hello, ${name}!`
    %>
    ```

  - **Suggest a Choice:**
    This presents a dropdown list of options.

    ```markdown
    <%*
    const choice = await tp.system.suggester(["Option 1", "Option 2", "Option 3"], ["val1", "val2", "val3"], "Choose one:")
    tR += `You selected: ${choice}`
    %>
    ```

    *(Note: The first array is what the user sees, the second is the value that's returned.)*

## 6\. ✍️ Editor and Cursor (`tp.editor` & `tp.file.cursor`)

Control the editor directly.

  - **Place Cursor:**
    This is a special command. You place it where you want your cursor to end up *after* the template is inserted.

    ```markdown
    ### My New Section

    <% tp.file.cursor() %>
    ```

  - **Get Highlighted Text:**

    ```markdown
    <%*
    const selection = tp.editor.get_selection()
    tR += `You highlighted: ${selection}`
    %>
    ```

  - **Insert Text at Cursor:** (Useful inside a JS block)
 ```markdown
  <%* tp.editor.insert("This text was inserted by a script.") %>  
  ```

## 7\. 🚀 Advanced JavaScript Blocks

This is where Templater's true power shines. By using `<%* … %>`, you can write full JavaScript to dynamically build your note.

### Key Concepts

  - **`await`:** You *must* use `await` for functions that are asynchronous, like `tp.system.prompt()`.
  - **`tR`:** This special variable holds the "template result". In a `<%* … %>` block, nothing is output *unless* you add it to `tR`. Use `tR += "your string"` to append to the output.

### Example: Creating a Dynamic Zettelkasten Note

This template will prompt you for a title, then create a UID (Unique ID) and title.

```markdown
<%*
// 1. Create a unique ID based on the current datetime
const uid = tp.date.now("YYYYMMDDHHmmss")
// 2. Prompt the user for a title
const title = await tp.system.prompt("Enter note title:")
// 3. Rename the file to match the UID and Title
await tp.file.rename(`${uid} - ${title}`)
// 4. Build the output string
let output = ""
output += `# ${title}\n\n`
output += `**ID:** ${uid}\n`
output += `**Tags:** #zettel \n`
output += `**Created:** ${tp.date.now("YYYY-MM-DD @ HH:mm")}\n\n`
output += "## Note\n\n"
output += `<% tp.file.cursor() %>\n\n` // Place cursor here
output += "## Connections\n"
// 5. Send the final string to the template result
tR = output
%>
```

*(**Note:** This is a complex example. To use it, you would save this entire block as a template, then run it from the command palette.)*

-----

## 📚 Related Topics for Further Understanding

To get the most out of Templater, I recommend exploring these related areas:

  - **Moment.js Documentation:** Since `tp.date` is a wrapper for Moment.js, its official documentation is the ultimate resource for all possible date/time formatting strings.
  - **JavaScript Basics (ES6+):** Understanding variables (`const`, `let`), strings (especially template literals: `` `string ${variable}` ``), and `async`/`await` will dramatically increase what you can do.
  - **Obsidian Dataview:** Templater can be used to *create* metadata (like `key: value`) that the Dataview plugin can then *query*, allowing you to build dynamic "Maps of Content" (MOCs) and dashboards.
  - **Obsidian QuickAdd:** This plugin works wonderfully with Templater. You can create a QuickAdd command that runs a Templater template, allowing you to bind complex template scripts to a single hotkey.
