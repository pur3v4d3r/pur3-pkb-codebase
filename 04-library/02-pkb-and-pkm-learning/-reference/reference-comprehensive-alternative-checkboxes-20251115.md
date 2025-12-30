---
title: "Reference: Alternitive Chackboxes"
id: 20251115032946
type: "reference"
tags:
  - year/2025
aliases:
  - Alternative Checkboxes
---

Tags: \#obsidian/plugin/tasks, \#obsidian/css, \#obsidian/theming, \#reference/checkboxes
Aliases: Obsidian Tasks Custom Checkboxes, Alternate Checkboxes, Custom Task Statuses, Obsidian Task Types

> [!comprehensive-reference] 📚Comprehensive-Reference
>
>   - **Generated**:: [[2025-11-15]]
>   - **Version**:: 1.0
>   - **Type**:: Reference Documentation

> [!abstract]
> **Executive Overview**
> This document provides an exhaustive reference for the "Alternate Checkboxes" (Custom Statuses) system for the [[Obsidian Tasks Plugin]]. It clarifies the critical distinction between the plugin's **semantic status logic** (e.g., `TODO`, `DONE`) and a theme's **visual CSS styling** (e.g., `[!]`, `[?]`). It includes comprehensive reference tables for the status characters supported by the Tasks plugin itself, as well as popular collections like the Minimal theme, Anuppuccin, and the SlRvb's snippet.

> [!how-to-use-this]
> **Navigation Guide**
> This reference note is organized into 6 major sections covering all aspects of custom task statuses. Use the table of contents below for quick navigation, or search for specific characters (e.g., `[T]`, `[?]`) to find their meaning in the reference tables.

## 📑 Table of Contents

  * [[#⚙️ The Core Concept: Logic vs. Styling]]
  * [\#🧩 System 1: The Obsidian Tasks Plugin "Status" Model]]
      * [[#Foundational Concepts]]
      * [\#Status Types: The 5 Semantic States]]
  * [\#🎨 System 2: Theme & CSS "Alternate Checkbox" Styling]]
      * [[#Foundational Concepts]]
      * [[\#How Styling Works]]
  * [[\#📚 Comprehensive Status Collection Reference]]
      * [[\#Default Tasks Plugin Statuses]]
      * [[\#Collection 1: Minimal Theme (and Things Theme)]]
      * [[\#Collection 2: AnuPpuccin Theme]]
      * [[\#Collection 3: SlRvb's Alternate Checkboxes (Recommended Snippet)]]
  * [[\#🚀 Implementation & Management]]
      * [[\#Method 1: "One-Click" Status Collection Import (Recommended)]]
      * [[\#Method 2: Manually Adding a Status]]
  * [[\#🎯 Synthesis & Mastery]]
      * [[\#The "Alternative Checkboxes Reference Set" Initiative]]
      * [[\#Creating Your Own Status Characters]]
  * [[\#📊 Metadata & Attribution]]
  * [[\#🔄 Version History]]
  * [[\#🔗 Related Topics for PKB Expansion]]

-----

## ⚙️ The Core Concept: Logic vs. Styling

> [!definition]
>
>   - **Key-Term**:: [[Obsidian Custom Task Status]]
>   - **Definition**:: A custom task status is a single character (e.g., `/`, `!`, `?`) placed inside the brackets of a markdown task (`- [ ]`). This character is used by two separate but related systems: the **[[Obsidian Tasks Plugin]]** for behavioral logic and **[[Obsidian Themes]]/[[CSS Snippets]]** for visual styling.

### Foundational Concepts

Understanding "alternate checkboxes" requires separating **behavior** from **appearance**.

1.  **System 1: Plugin Logic (The "Brain")**

      * This is managed by the [[Obsidian Tasks Plugin]].
      * It answers: "What *is* this task? Is it `TODO`, `DONE`, `IN_PROGRESS`, or `CANCELLED`?"
      * It also answers: "When I click this task, what status should it change to?"
      * This system **does not** create the visual icon (like a -▷`or`❓` ). It only manages the *character* (like  `\>`or`?\`).

2.  **System 2: Theme Styling (The "Skin")**

      * This is managed by your active [[Obsidian Themes|Theme]] or a [[CSS Snippets|CSS Snippet]].
      * It answers: "When I see a task with the character `[?]` in it, what icon, color, or decoration should I show?"
      * This system **does not** know what `DONE` or `TODO` means. It only styles the character it's told to.

**A functional system requires both.** Your theme must provide the *style* for `[?]`, and you must *teach* the Tasks plugin what `[?]` *means* (e.g., it's a `TODO` status called "Question"). The user's example, `- [T]`, is a custom status for "Time" (from the SlRvb's collection) that is given a clock icon by a CSS snippet.

> [!key-claim]
> **Central Principle**
> The [[Obsidian Tasks Plugin]] handles the **semantic meaning** and **click behavior** of task statuses. Your **Theme/CSS** handles the **visual appearance** (icons, colors) of those statuses. You must configure both for a seamless experience.

-----

## 🧩 System 1: The Obsidian Tasks Plugin "Status" Model

> [!definition]
>
>   - **Key-Term**:: [[Task Status]]
>   - **Definition**:: A configuration in the Tasks plugin settings that links a **Status Symbol** (one character) to a **Status Name** ("In Progress"), a **Next Status Symbol** ("x"), and a **Status Type** (`IN_PROGRESS`).

### Foundational Concepts

The Tasks plugin's "Custom Statuses" settings are the central control panel for task *behavior*. When you add a new custom status, you must define four properties:

1.  **Status Symbol**: The single character that will be used in the markdown, e.g., `/`.
2.  **Status Name**: The human-readable name, e.g., "In Progress". This is used for searching (`status.name includes "In Progress"`).
3.  **Next Status Symbol**: The character the task will change to when clicked, e.g., `x` (for Done).
4.  **Status Type**: The core semantic category. This is the most important setting.

### Status Types: The 5 Semantic States

The Tasks plugin only understands five fundamental states. Every custom status you create **must** be assigned to one of them.

| Status Type | Description | Default Symbol(s) |
|---|---|---|
| `TODO` | Any task that is not finished and actionable. This is the default for all new custom statuses. | `     ` (space) |
| `IN_PROGRESS` | Any task that has been started but is not yet complete. | `/` |
| `DONE` | A task that has been successfully completed. Toggling to this state adds a "done date." | `x` |
| `CANCELLED` | A task that is no longer relevant or has been intentionally dropped. | `-` |
| `NON_TASK` | A character that should *not* be treated as a task. It will not appear in queries. Useful for list items styled as bullets (e.scss.g., `[*]`). | (None by default) |

> [!warning]
> **Critical Constraints**
> If you use a custom character in your notes (e.g., `- [!]`) but **do not** define it in the Tasks plugin settings, the plugin will treat it as a `TODO` task named "Unknown." It will not have the correct click behavior or query-ability until you define it.

-----

## 🎨 System 2: Theme & CSS "Alternate Checkbox" Styling

> [!definition]
>
>   - **Key-Term**:: [[Alternate Checkboxes]]
>   - **Definition**:: A feature provided by an [[Obsidian Themes|Obsidian Theme]] or [[CSS Snippets|CSS Snippet]] that uses CSS attribute selectors to replace a task's standard checkbox with a custom icon, color, or style based on its status character.

### Foundational Concepts

This system is what provides the rich visual feedback you see. A theme or snippet will contain CSS code that specifically targets task items based on their `data-task` attribute, which is set by the character in the brackets.

A simplified CSS snippet for a `[?]` "Question" task would look like this:

```css
/* 1. Target the task list item in reading/live preview */
.task-list-item[data-task="?"] .task-list-item-checkbox {
  /* 2. Hide the original square checkbox */
  border: none;
  background-color: transparent;
}

/* 3. Add a new icon (e.g., from an icon font or SVG) */
.task-list-item[data-task="?"] .task-list-item-checkbox::after {
  content: '❓'; /* Or an SVG icon */
  font-size: 16px;
  color: var(--text-accent); /* Use the theme's accent color */
}
```

### How Styling Works

You do not need to write this CSS. You simply need to:

1.  **Use a theme** (like Minimal, Anuppuccin) that has built-in support for alternate checkboxes.
2.  **OR Install a CSS Snippet** (like SlRvb's Alternate Checkboxes) that provides these styles and works with *any* theme.

> [!key-claim]
> **Central Principle**
> The theme/CSS provides a *menu* of available visual styles. The Tasks plugin's "Custom Status" settings are how you *order* from that menu, giving each visual style a specific *behavior* and *meaning*.

-----

## 📚 Comprehensive Status Collection Reference

The following tables document the most common "Status Symbol" collections available.

### Default Tasks Plugin Statuses

The [[Obsidian Tasks Plugin]] supports these four statuses out-of-the-box.

| Symbol          | Status Name | Default Type  | Next Symbol | Visual                 |
| --------------- | ----------- | ------------- | ----------- | ---------------------- |
| `     ` (space) | Todo        | `TODO`        | `x`         | `[ ]` (Empty box)      |
| `x`             | Done        | `DONE`        | `     `     | `[x]` (Checked box)    |
| `/`             | In Progress | `IN_PROGRESS` | `x`         | `[/]` (Box with slash) |
| `-`             | Cancelled   | `CANCELLED`   | `     `     | `[-]` (Box with dash)  |

-----

### Collection 1: Minimal Theme (and Things Theme)

The [[Minimal]] theme's collection is one of the most popular and has been adopted by other themes, such as [[Things]].

| Symbol  | Status Name | Default Type  | Next Symbol | Visual (in Minimal)                 |
| ------- | ----------- | ------------- | ----------- | ----------------------------------- |
| `     ` | Todo        | `TODO`        | `x`         | `[ ]` (Empty box)                   |
| `x`     | Done        | `DONE`        | `     `     | `[x]` (Checked box)                 |
| `/`     | Incomplete  | `IN_PROGRESS` | `x`         | `[/]` (Half-filled)                 |
| `-`     | Canceled    | `CANCELLED`   | `     `     | `[-]` (Dash)                        |
| `>`     | Forwarded   | `TODO`        | `x`         | `[>]` (Right arrow)                 |
| `<`     | Scheduling  | `TODO`        | `x`         | `[<]` (Left arrow/reschedule)       |
| `?`     | Question    | `TODO`        | `x`         | `[?]` (Question mark icon)          |
| `!`     | Important   | `TODO`        | `x`         | `[!]` (Exclamation icon, often red) |
| `*`     | Star        | `TODO`        | `x`         | `[*]` (Star icon)                   |
| `"`     | Quote       | `NON_TASK`    | `"`         | `["]` (Quote icon)                  |
| `l`     | Location    | `NON_TASK`    | `l`         | `[l]` (Location pin icon)           |
| `b`     | Bookmark    | `NON_TASK`    | `b`         | `[b]` (Bookmark icon)               |
| `i`     | Information | `NON_TASK`    | `i`         | `[i]` (Info icon)                   |
| `S`     | Savings     | `NON_TASK`    | `S`         | `[S]` (Dollar/savings icon)         |
| `I`     | Idea        | `NON_TASK`    | `I`         | `[I]` (Lightbulb icon)              |
| `p`     | Pro         | `NON_TASK`    | `p`         | `[p]` (Thumbs up)                   |
| `c`     | Con         | `NON_TASK`    | `c`         | `[c]` (Thumbs down)                 |

-----

### Collection 2: AnuPpuccin Theme

The [[AnuPpuccin]] theme includes its own set, which is a mix of the Minimal set and unique additions.

| Symbol  | Status Name   | Default Type  | Next Symbol | Visual (in AnuPpuccin)            |
| ------- | ------------- | ------------- | ----------- | --------------------------------- |
| `     ` | Unchecked     | `TODO`        | `x`         | `[ ]` (Empty box)                 |
| `x`     | Checked       | `DONE`        | `     `     | `[x]` (Checked box)               |
| `>`     | Rescheduled   | `TODO`        | `x`         | `[>]` (Right arrow)               |
| `<`     | Scheduled     | `TODO`        | `x`         | `[<]` (Calendar icon)             |
| `!`     | Important     | `TODO`        | `x`         | `[!]` (Exclamation icon)          |
| `-`     | Cancelled     | `CANCELLED`   | `     `     | `[-]` (Dash/cross)                |
| `/`     | In Progress   | `IN_PROGRESS` | `x`         | `[/]` (Half-filled)               |
| `?`     | Question      | `TODO`        | `x`         | `[?]` (Question mark icon)        |
| `*`     | Star          | `TODO`        | `x`         | `[*]` (Star icon)                 |
| `n`     | Note          | `NON_TASK`    | `n`         | `[n]` (Note/pen icon)             |
| `l`     | Location      | `NON_TASK`    | `l`         | `[l]` (Location pin icon)         |
| `i`     | Information   | `NON_TASK`    | `i`         | `[i]` (Info icon)                 |
| `I`     | Idea          | `NON_TASK`    | `I`         | `[I]` (Lightbulb icon)            |
| `S`     | Amount        | `NON_TASK`    | `S`         | `[S]` (Dollar/money icon)         |
| `p`     | Pro           | `NON_TASK`    | `p`         | `[p]` (Plus icon)                 |
| `c`     | Con           | `NON_TASK`    | `c`         | `[c]` (Minus icon)                |
| `b`     | Bookmark      | `NON_TASK`    | `b`         | `[b]` (Bookmark icon)             |
| `"`     | Quote         | `NON_TASK`    | `"`         | `["]` (Quote icon)                |
| `0`-`9` | Speech bubble | `NON_TASK`    | (self)      | `[0]` (Speech bubble with number) |

-----

### Collection 3: SlRvb's Alternate Checkboxes (Recommended Snippet)

This is a very comprehensive **CSS Snippet** (not a theme) that is recommended by the Tasks plugin developers. It is designed to work with *any* theme. The list is extensive; this is a partial selection of common types. The user's example `[T]` (Time) comes from this set.

| Symbol | Status Name | Default Type | Next Symbol | Visual (in Snippet) |
|---|---|---|---|---|
| `     ` | Unchecked | `TODO` | `x` | `[ ]` (Empty box) |
| `x` | Regular | `DONE` | `     ` | `[x]` (Checked box) |
| `X` | Checked | `DONE` | `     ` | `[X]` (Checked box, styled) |
| `-` | Dropped | `CANCELLED` | `     ` | `[-]` (Cross icon) |
| `D` | Date | `TODO` | `x` | `[D]` (Calendar icon) |
| `d` | Doing | `IN_PROGRESS` | `x` | `[d]` (Play/forward icon) |
| `/` | Half Done | `IN_PROGRESS` | `x` | `[/]` (Half-filled) |
| `?` | Question | `TODO` | `x` | `[?]` (Question mark icon) |
| `!` | Important | `TODO` | `x` | `[!]` (Exclamation icon) |
| `i` | Idea | `TODO` | `x` | `[i]` (Lightbulb icon) |
| `R` | Research | `TODO` | `x` | `[R]` (Magnifying glass icon) |
| `N` | Note | `NON_TASK` | `N` | `[N]` (Pen/note icon) |
| `b` | Bookmark | `NON_TASK` | `b` | `[b]` (Bookmark icon) |
| `B` | Brainstorm | `TODO` | `x` | `[B]` (Brain icon) |
| `P` | Pro | `NON_TASK` | `P` | `[P]` (Plus icon) |
| `C` | Con | `NON_TASK` | `C` | `[C]` (Minus icon) |
| `Q` | Quote | `NON_TASK` | `Q` | `[Q]` (Quote icon) |
| `L` | Location | `NON_TASK` | `L` | `[L]` (Location pin icon) |
| `E` | Example | `NON_TASK` | `E` | `[E]` (Beaker/test tube icon) |
| **`T`** | **Time** | `TODO` | `x` | `[T]` (Clock icon) |

-----

## 🚀 Implementation & Management

> [!methodology-and-sources]
> **Practical Framework**
> You must enable **both** the visual style (Theme/Snippet) and the plugin logic (Tasks settings) for custom statuses to work.

### Method 1: "One-Click" Status Collection Import (Recommended)

The Tasks plugin developers have made this process simple.

1.  **Install Visuals**:
      * **Theme**: Go to `Settings` \> `Appearance` \> `Themes` and install/enable a theme like [[Minimal]] or [[AnuPpuccin]].
      * **Snippet**: (Recommended for flexibility) Go to `Settings` \> `Appearance` \> `CSS Snippets`. Click the folder icon, download the `SlRvb's Alternate Checkboxes` snippet (search online for it), place the `.css` file in the folder, and then enable it in Obsidian.
2.  **Import Logic**:
      * Go to `Settings` \> `Community Plugins` \> `Tasks`.
      * Scroll down to the **Task Statuses** section.
      * You will see a "pretty" list of checkboxes. Below that, click the **Add** button.
      * A menu will appear. Instead of "New," select the "Status Collection" you installed (e.g., `Minimal`, `AnuPpuccin`, `SlRvb's Alternate Checkboxes`).
      * The Tasks plugin will automatically load all the statuses from that collection (Symbol, Name, Type, Next Symbol) into its settings.
      * Restart Obsidian to ensure all changes are applied.

### Method 2: Manually Adding a Status

If you only want to add one or two custom statuses (e.g., just `[!]` for "Important"):

1.  **Install Visuals**: Make sure your theme or a snippet already styles `[!]`.
2.  **Add Logic**:
      * Go to the Tasks plugin settings (`Settings` \> `Tasks`).
      * In the **Task Statuses** section, click `Add` \> `New`.
      * A modal will appear.
      * **Status Symbol**: `!`
      * **Status Name**: `Important`
      * **Next Status Symbol**: `x` (so it becomes "Done" when clicked)
      * **Status Type**: `TODO` (it is still a "to-do" item, just an important one)
      * Click `Save`.

-----

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **Underlying Philosophy**
> The character in the brackets is a piece of metadata. By standardizing this metadata (e.g., `?` is always "Question"), we can build powerful, theme-agnostic workflows. The Tasks plugin provides the *database* logic, and themes provide the *visual interface* for this metadata.

### The "Alternative Checkboxes Reference Set" Initiative

There is a community effort to standardize the most common "alternate checkboxes" into a single, well-documented CSS snippet. This "Reference Set" aims to be a stable foundation that users can adopt and theme-makers can support, preventing the fragmentation of having dozens of different "collections." This is an advanced topic for users who want maximum stability and interoperability between themes.

> [!analogy]
> **Illuminating Comparison**
>
>   - The **Theme/CSS** is a **Font**. It defines what the letter "A" looks like (e.g., Times New Roman vs. Comic Sans).
>   - The **Tasks Plugin** is a **Word Processor**. It defines what the letter "A" *means* and what happens when you type it.
>
> You need both to write a document. The character `[T]` is just a letter; the theme makes it *look* like a clock, and the plugin makes it *behave* like a task.

### Creating Your Own Status Characters

You can use *any* single character, even emojis, as a status symbol (though this is not recommended for compatibility).

1.  **Pick a Character**: Choose an unused character, e.g., `&`.
2.  **Create the CSS**: Create a CSS snippet (e.g., `my-checkboxes.css`) to style it.
    ```css
    .task-list-item[data-task="&"] .task-list-item-checkbox::after {
      content: '🤝'; /* Show a handshake emoji */
      font-size: 16px;
    }
    ```
3.  **Enable the Snippet**: Enable `my-checkboxes.css` in `Settings` \> `Appearance`.
4.  **Teach Tasks**: Go to `Settings` \> `Tasks` and manually add the `&` symbol.
      * **Symbol**: `&`
      * **Name**: `Delegated`
      * **Next Symbol**: `x`
      * **Type**: `TODO`

You have now created a fully custom, theme-independent task status.

-----

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
>
>   - **Primary Sources**:
>       - [Obsidian Tasks Plugin Official Documentation](https://publish.obsidian.md/tasks/)
>       - [Tasks Plugin: Status Collections](https://publish.obsidian.md/tasks/Reference/Status+Collections/About+Status+Collections)
>       - [Tasks Plugin: Minimal Theme Statuses](https://publish.obsidian.md/tasks/Reference/Status+Collections/Minimal+Theme)
>       - [Tasks Plugin: AnuPpuccin Theme Statuses](https://publish.obsidian.md/tasks/Reference/Status+Collections/AnuPpuccin+Theme)
>       - [Tasks Plugin: SlRvb's Alternate Checkboxes](https://www.google.com/search?q=https://publish.obsidian.md/tasks/Reference/Status%2BCollections/SlRvb%2527s%2BAlternate%2BCheckboxes)
>       - [Alternative Checkboxes Reference Set (GitHub)](https://github.com/damiankorcz/Alternative-Checkboxes-Reference-Set)
>   - **Research Queries**:
>       - `obsidian tasks plugin custom task statuses documentation`
>       - `obsidian tasks plugin alternate checkboxes themes`
>       - `obsidian minimal theme custom task statuses list`
>       - `obsidian anuppuccin theme task checkboxes`
>       - `obsidian tasks [T]`
>   - **Synthesis Approach**: Synthesized official plugin documentation with theme-specific implementations to create a unified reference. The core distinction between "Logic" (Plugin) and "Styling" (Theme) was identified as the central organizing principle.
>   - **Confidence Level**: High. The information is sourced directly from the plugin's official documentation and cross-referenced with community standardization efforts.

## 🔄 Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2025-11-15 | Initial comprehensive compilation and synthesis of all research. |

-----

### 🔗 Related Topics for PKB Expansion

  * [[Obsidian Tasks Plugin]]
  * [[Obsidian Themes]]
  * [[CSS Snippets]]
  * [[Obsidian Minimal Theme]]
  * [[Obsidian AnuPpuccin Theme]]
  * [[Dataview Plugin]] (for querying these custom task statuses)
  * [[How to create a CSS Snippet in Obsidian]]