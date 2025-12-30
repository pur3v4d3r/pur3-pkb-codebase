---
title: Callout Taxonomy
id: "20251115121714"
type: reference
tags:
  - year/2025
  - type/reference
  - obsidian/customization/snippets
  - pkb/plugin/style-settings
aliases:
  - Obsidian Callout CSS
  - Callout Customization
  - Style Settings for Callouts
  - CSS Snippet Reference
link-up: []
link-related:
  - "[[202511131029_css-snippet-modification-for-obsidian_comprehensive-reference]]"
  - "[[202511131909_complete-modular-callout-system_foundation-and-swappable-styles]]"
  - "[[202511140502_css-snippet-library_comprehensive-reference]]"
  - "[[_snippet-callout-system-workbench]]"
  - "[[_snippet-css-variables-index]]"
  - "[[reference-technical-modular-callout-system-swappable-styles-2025111312]]"
  - "[[scratchpad-for-moving-snippets]]"
  - "[[reference-comprehensive-css-variable-2025110619]]"
  - "[[reference-comprehensive-css-variables-20251106]]"
  - "[[snippet-index-note_202511132126]]"
  - "[[202511150329_alternative-checkboxes_reference]]"
---



-----

### Phase 3: Reference Note Construction

Tags: \#css/obsidian \#obsidian/callouts \#snippets \#plugins/style-settings \#reference/taxonomy
Aliases: Obsidian Callout CSS, Callout Customization, Style Settings for Callouts, CSS Snippet Reference

> [!comprehensive-reference] 📚Comprehensive-Reference
>
>   - **Generated**:: [[2025-11-15]]
>   - **Version**:: 1.0
>   - **Type**:: Reference Documentation

> [!abstract]
> **Executive Overview**
> This document is the complete and authoritative reference for customizing [[obsidian]] callouts using [[CSS]]. It provides a full taxonomy of all targetable elements, properties, and CSS variables, with a special focus on creating snippets compatible with the [[Style Settings]] plugin.

> [!how-to-use-this]
> **Navigation Guide**
> This reference note is organized into 6 major sections. Start with the [[\#1. 🏛️ Anatomy of a Callout|Anatomy]] to understand the structure. Use the [[\#3. 📖 Comprehensive Customization Taxonomy|Taxonomy]] as a dictionary for specific properties. Refer to the [[\#4. ⚙️ Style Settings Plugin Integration|Style Settings]] section for making your snippets configurable.

## 📑 Table of Contents

1.  [[\#1. 🏛️ Anatomy of a Callout|Anatomy of a Callout]]
2.  [[\#2. 🎯 Core Targeting Selectors|Core Targeting Selectors]]
3.  [[\#3. 📖 Comprehensive Customization Taxonomy|Comprehensive Customization Taxonomy]]
      * [[\#3.1. Icon Customization|Icon Customization]]
      * [[\#3.2. Title & Header Customization|Title & Header Customization]]
      * [[\#3.3. Border, Background, & Shadow|Border, Background, & Shadow]]
      * [[\#3.4. Content Area Customization|Content Area Customization]]
4.  [[\#4. ⚙️ Style Settings Plugin Integration|Style Settings Plugin Integration]]
      * [[\#Style Settings Syntax Reference|Style Settings Syntax Reference]]
      * [[\#Practical Example: Style Settings Callout|Practical Example: Style Settings Callout]]
5.  [[\#5. 🔬 Advanced Techniques & States|Advanced Techniques & States]]
      * [[\#Styling Foldable States|Styling Foldable States]]
      * [[\#Styling Nested Callouts|Styling Nested Callouts]]
      * [[\#Using Pseudo-elements|Using Pseudo-elements]]
      * [[\#View-Specific Styling|View-Specific Styling]]
6.  [[\#6. 🍳 Practical Cookbook: Synthesis & Examples|Practical Cookbook: Synthesis & Examples]]

-----

## 1\. 🏛️ Anatomy of a Callout

> [!definition]
>
>   - **Key-Term**:: [[Callout DOM Structure]]
>   - **Definition**:: The nested HTML elements and CSS classes that Obsidian generates to render a callout block. Understanding this structure is required to write correct [[CSS Selectors]].

### Foundational Concepts

A callout begins as `> [!my-callout]` in Markdown. When rendered, Obsidian transforms this into a structure of nested `div` elements. All customization is simply the process of selecting these elements and changing their CSS properties.

Here is the simplified HTML structure:

```html
<div class="callout" data-callout="my-callout">

  <div class="callout-title">
    <div class="callout-icon">
      <svg>...</svg>
    </div>
    <div class="callout-title-inner">
      My Callout Title
    </div>
    <div class="callout-fold">
      <svg>...</svg>
    </div>
  </div>

  <div class="callout-content">
    <p>This is the content of the callout.</p>
  </div>

</div>
```

> [!key-claim]
> **Central Principle**
> All callout customization is achieved by writing a CSS selector that targets one of these elements (e.g., `.callout[data-callout="my-callout"]`) and then overriding its default CSS properties (e.g., `--callout-color` or `background-color`).

-----

## 2\. 🎯 Core Targeting Selectors

> [!definition]
>
>   - **Key-Term**:: [[CSS Selector]]
>   - **Definition**:: The part of a CSS rule that identifies which HTML element(s) in the document will be styled.

### Foundational Concepts

To create a **new** callout type, you must invent a `data-callout` name (e.g., `project`) and then define its properties in your CSS snippet.

The basic syntax is `> [!project]`. This creates `<div class="callout" data-callout="project">`.

Your primary tool is the **attribute selector**.

### Selector Reference

| Selector Target | CSS Selector Syntax | Usage Example |
| --- | --- | --- |
| **All Callouts** | `.callout` | `/* Affects every single callout */` <br> `.callout { border-radius: 10px; }` |
| **A Specific Callout Type** | `.callout[data-callout="type"]` | `/* Only affects [!project] callouts */` <br> `.callout[data-callout="project"] { ... }` |
| The **Title Bar** | `.callout[data-callout="type"] .callout-title` | `/* Targets the title bar of [!project] */` <br> `.callout[data-callout="project"] .callout-title { ... }` |
| The **Icon** | `.callout[data-callout="type"] .callout-icon` | `/* Targets the icon container of [!project] */` <br> `.callout[data-callout="project"] .callout-icon { ... }` |
| The **Title Text** | `.callout[data-callout="type"] .callout-title-inner`| `/* Targets the title text of [!project] */` <br> `.callout[data-callout="project"] .callout-title-inner { ... }` |
| The **Content Area**| `.callout[data-callout="type"] .callout-content` | `/* Targets the content area of [!project] */` <br> `.callout[data-callout="project"] .callout-content { ... }` |
| The **Fold Arrow** | `.callout[data-callout="type"] .callout-fold` | `/* Targets the fold icon of [!project] */` <br> `.callout[data-callout="project"] .callout-fold { ... }` |

> [!key-claim]
> **Central Principle**
> The most robust way to customize is by overriding **CSS Variables** (e.g., `--callout-color`) rather than base properties (e.g., `background-color`). This ensures your callout respects theme settings (like light/dark mode) and is easier to maintain.

-----

## 3\. 📖 Comprehensive Customization Taxonomy

This section provides a complete reference of CSS variables and properties, organized by the visual component you wish to modify.

> [!methodology-and-sources]
> **Framework**
> The following examples will target a hypothetical `[!project]` callout.
>
> **CSS Snippet Structure:**
>
> ```css
> /* Always define your variables inside the selector */
> .callout[data-callout="project"] {
>   /* --variable-name: value; */
> }
> ```

### 3.1. Icon Customization

| Method | Property / Variable | Example Value | Notes |
| --- | --- | --- | --- |
| **Change Lucide Icon** | `--callout-icon` | `lucide-briefcase` | This is the simplest method. Uses any name from the [[Lucide]] icon set. |
| **Use Emoji** (Method A) | `content` (via `::before`) | `'💼'` | Requires hiding the default icon. See example below. |
| **Use Custom SVG** (Method B)| `mask-image` / `background-image` | `url('data:image/svg+xml;...')` | Provides full control. Often uses a base64-encoded SVG. |
| **Use Iconize Plugin** | `none` (set in UI) | `fas-rocket` | Use the [[Callout Manager]] plugin to set an [[Iconize]] shortcode as the icon. |

**Example (Changing Lucide Icon):**

```css
.callout[data-callout="project"] {
  --callout-icon: lucide-briefcase;
}
```

**Example (Using Emoji Icon):**

```css
/* Select the [!project] callout's title */
.callout[data-callout="project"] .callout-title {
  position: relative; /* Needed for pseudo-element positioning */
}

/* Hide the default SVG icon */
.callout[data-callout="project"] .callout-icon {
  display: none;
}

/* Create a new pseudo-element to hold the emoji */
.callout[data-callout="project"] .callout-title::before {
  content: '💼';
  position: absolute;
  left: 0px; /* Adjust as needed */
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2em; /* Adjust as needed */
}

/* Add padding to the title text to make room for the new emoji */
.callout[data-callout="project"] .callout-title-inner {
  margin-left: 30px; /* Adjust to fit your emoji */
}
```

### 3.2. Title & Header Customization

| Target | Property / Variable | Example Value | Notes |
| --- | --- | --- | --- |
| Title Text Color | `color` | `#FFFFFF` | Targets `.callout-title-inner` |
| Title Background | `background-color` | `var(--color-accent)` | Targets `.callout-title` |
| Title Font | `font-family` | `"Georgia", serif` | Targets `.callout-title-inner` |
| Title Font Size | `font-size` | `1.5em` | Targets `.callout-title-inner` |
| Title Font Weight | `font-weight` | `700` | Targets `.callout-title-inner` |
| Title Alignment | `text-align` | `center` | Targets `.callout-title-inner` |

### 3.3. Border, Background, & Shadow

These properties are typically set on the main `.callout[data-callout="project"]` selector.

| Target | Property / Variable | Example Value | Notes |
| --- | --- | --- | --- |
| **Main Color** | `--callout-color` | `255, 0, 0` | **Crucial variable.** Expects an `R, G, B` triplet. Controls border and default title background. |
| Border Width | `--callout-border-width` | `3px 0 0 3px` | `top right bottom left`. Use `0 0 0 5px` for just a left border. |
| Border Style | `border-style` | `dashed` | |
| Border Radius | `border-radius` | `10px` | Controls rounding of the corners. |
| Main Background | `background-color` | `rgba(var(--callout-color), 0.1)` | Use `rgba` with the `--callout-color` variable for a transparent background. |
| Box Shadow | `box-shadow` | `5px 5px 15px rgba(0,0,0,0.2)` | Adds a drop shadow. |

### 3.4. Content Area Customization

These properties are set on the `.callout[data-callout="project"] .callout-content` selector.

| Target | Property / Variable | Example Value | Notes |
| --- | --- | --- | --- |
| Content Padding | `--callout-padding` | `20px` | Controls inner padding of the *entire* callout. |
| Content Background | `background-color` | `#FAFAFA` | Sets background for *just* the content area. |
| Content Text Color | `color` | `#333333` | |
| Content Font Size | `font-size` | `0.9em` | |

-----

## 4\. ⚙️ Style Settings Plugin Integration

> [!definition]
>
>   - **Key-Term**:: [[Style Settings]]
>   - **Definition**:: An Obsidian plugin that reads special comments in CSS snippets to generate a user-friendly settings UI, allowing users to change [[CSS Variables]] without editing code.

### Foundational Concepts

To make your callout customizable via [[Style Settings]], you must:

1.  Define your callout styles using CSS variables (e.g., `--project-color`).
2.  Use those variables in your callout CSS.
3.  Add special `/* @settings ... */` comments *before* the variable definitions in your `:root` block.

> [!key-claim]
> **Central Principle**
> Style Settings does **not** write CSS for you. It only provides a UI to change the *value* of CSS variables you have already defined and used.

### Style Settings Syntax Reference

You must place this block at the **top** of your CSS snippet file.

| Annotation | Description |
| --- | --- |
| `/* @settings-group: [GroupName] */` | Creates a new collapsible section in Style Settings. |
| `/* @settings-name: "[Setting Name]" */` | The human-readable name for the setting. |
| `/* @settings-description: "[Help Text]" */` | Explanatory text that appears below the setting. |
| `/* @settings-type: [type] */` | Specifies the UI control. `color`, `text`, `slider`, `toggle`. |
| `/* @settings-color-format: [format] */` | `rgb` or `hex`. Use `rgb` for `--callout-color`. |
| `/* @settings-slider-min: [value] */` | Minimum value for a `slider`. |
| `/* @settings-slider-max: [value] */` | Maximum value for a `slider`. |
| `/* @settings-slider-step: [value] */` | Increment value for a `slider`. |

### Practical Example: Style Settings Callout

Here is a *complete* snippet file that creates a `[!project]` callout fully controllable by Style Settings.

```css
/*
This is the CSS snippet file (e.g., MyCallouts.css)
*/

/* == STYLE SETTINGS DEFINITIONS == */
/* This block defines the UI in the plugin */
:root {
  /* @settings-group: Project Callout */
  /* @settings-name: "Project Color" */
  /* @settings-description: "Sets the main color for the project callout." */
  /* @settings-type: color */
  /* @settings-color-format: rgb */
  --project-color: 139, 92, 246; /* Default: purple */

  /* @settings-name: "Project Icon" */
  /* @settings-description: "Name of the Lucide icon to use." */
  /* @settings-type: text */
  --project-icon: lucide-briefcase; /* Default icon */

  /* @settings-name: "Project Title Font Size" */
  /* @settings-description: "Font size for the callout title (e.g., 1.2em)." */
  /* @settings-type: text */
  --project-title-size: 1.2em;

  /* @settings-name: "Enable Title Uppercase" */
  /* @settings-description: "Toggles the title text to uppercase." */
  /* @settings-type: toggle */
  --project-title-uppercase: 0; /* 0 = off, 1 = on */
}

/* == CSS RULESET == */
/* This block *uses* the variables defined above */

.callout[data-callout="project"] {
  /* Use the variables from :root. 
    The 'var()' function includes a fallback value 
    just in case Style Settings fails.
  */
  --callout-color: var(--project-color, 139, 92, 246);
  --callout-icon: var(--project-icon, lucide-briefcase);
}

.callout[data-callout="project"] .callout-title-inner {
  font-size: var(--project-title-size, 1.2em);
  
  /* Use a 'hack' to apply the toggle */
  text-transform: if(var(--project-title-uppercase) = 1, uppercase, none);
}
```

-----

## 5\. 🔬 Advanced Techniques & States

### Styling Foldable States

Obsidian adds an `.is-folded` class to the `.callout` element when it's collapsed.

```css
/* Style the callout WHEN it is folded */
.callout[data-callout="project"].is-folded {
  box-shadow: 0 0 10px rgba(var(--project-color), 0.5);
  background-color: transparent;
}

/* Style the title differently WHEN folded */
.callout[data-callout="project"].is-folded .callout-title {
  font-style: italic;
}

/* Change the fold arrow icon */
.callout[data-callout="project"] .callout-fold svg {
  color: red; /* Or use 'stroke' */
}
```

### Styling Nested Callouts

You can style callouts that are inside other callouts differently.

```css
/* Target any callout INSIDE a [!project] callout */
.callout[data-callout="project"] .callout {
  border: 1px dashed rgba(var(--project-color), 0.5);
  box-shadow: none;
  border-radius: 0;
}
```

### Using Pseudo-elements

Use `::before` and `::after` for decorative elements.

```css
.callout[data-callout="project"] {
  position: relative; /* Required for pseudo-elements */
  overflow: hidden; /* Recommended */
}

/* Add a gradient flair to the top */
.callout[data-callout="project"]::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 5px;
  background-image: linear-gradient(
    90deg, 
    rgb(var(--project-color)), 
    transparent
  );
}
```

### View-Specific Styling

You can style for Live Preview and Reading Mode differently.

```css
/* --- Reading View --- */
.callout[data-callout="project"] {
  /* Base styles */
}

/* --- Live Preview --- */
/* Target callouts inside the live preview editor */
.cm-embed-block.cm-callout[data-callout="project"] {
  /* Add specific styles for live preview, e.g., less padding */
  padding: 5px;
}
```

-----

## 6\. 🍳 Practical Cookbook: Synthesis & Examples

> [!use-cases-and-examples]
> **Real-World Applications**

### 1\. "Matrix" Code Block Callout `[!matrix]`

**Goal**: A callout that looks like a terminal, with a monospace font and green-on-black text.

```css
/* --- Define the [!matrix] callout --- */
.callout[data-callout="matrix"] {
  --callout-color: 0, 255, 70; /* Bright green */
  --callout-icon: lucide-terminal;
  
  background-color: #0a0a0a;
  border-radius: 0;
  border: 1px solid rgb(var(--callout-color));
  box-shadow: 0 0 15px rgba(var(--callout-color), 0.4);
}

/* Style the title */
.callout[data-callout="matrix"] .callout-title {
  background-color: #1a1a1a;
}
.callout[data-callout="matrix"] .callout-title-inner {
  color: rgb(var(--callout-color));
  font-family: var(--font-monospace);
  font-weight: 700;
}

/* Style the content */
.callout[data-callout="matrix"] .callout-content {
  color: #00FF46;
  font-family: var(--font-monospace);
  font-size: 0.9em;
}
```

### 2\. "Sealed" Spoilers Callout `[!sealed]`

**Goal**: A callout that hides its content until hovered or unfolded. It starts completely blacked out.

```css
/* --- Define the [!sealed] callout --- */
.callout[data-callout="sealed"] {
  --callout-color: 255, 255, 0; /* Yellow */
  --callout-icon: lucide-lock;

  background-color: #111;
  border-radius: 5px;
  transition: all 0.3s ease-in-out;
}

/* Style the title */
.callout[data-callout="sealed"] .callout-title-inner {
  color: #FFF;
  font-weight: 700;
}

/* --- The Magic: Hide content when folded --- */
.callout[data-callout="sealed"].is-folded .callout-content {
  display: none; /* Already default, but good to be explicit */
}

/* Style the folded callout */
.callout[data-callout="sealed"].is-folded {
  background-color: #000;
  border: 1px dashed #555;
}
.callout[data-callout="sealed"].is-folded .callout-title-inner {
  color: #777;
  font-style: italic;
}

/* Reveal on hover when folded */
.callout[data-callout="sealed"].is-folded:hover {
  background-color: #111;
  border-color: rgb(var(--callout-color));
}
.callout[data-callout="sealed"].is-folded:hover .callout-title-inner {
  color: #FFF;
  font-style: normal;
}
```

-----

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **Underlying Philosophy**
> Callout customization is an exercise in **semantic styling**. The goal is not just to make something "look cool," but to create visual signposts that give your notes meaning. A `[!warning]` callout *should* feel alarming. A `[!project]` callout *should* feel organized and important. By mastering these selectors, you are building a personal, visual grammar for your knowledge.

### Cognitive Models

Think of a callout as a small "house" you are building inside your note.

  * `.callout`: The plot of land and the foundation.
  * `.callout[data-callout="..."]`: The *specific address* of the house.
  * `--callout-color`: The primary paint color for the trim and mailbox.
  * `.callout-title`: The front door and porch.
  * `.callout-icon`: The house number or door knocker.
  * `.callout-content`: The rooms inside the house.
  * `Style Settings`: The remote control that lets you change the paint color, porch light, and indoor lighting without having to rebuild.

> [!analogy]
> **Illuminating Comparison**
> **CSS Variables are "Contracts"**: When you use `--callout-color`, you are creating a *contract*. You are telling the callout, "Your border color and title background *must* use this value."
>
> **Style Settings is the "Contract Editor"**: It provides a UI to edit the *value* on that contract.
>
> This is far superior to "hard-coding" a color (`background-color: red`), which is like painting the house directly. If you want to change the color later, you have to repaint (edit the CSS file) instead of just changing the contract (editing the Style Settings UI).

### Comparative Analysis: Icon Methods

| Approach | Strengths | Weaknesses | Use When |
| --- | --- | --- | --- |
| **`--callout-icon`** | Easiest, theme-compatible. | Limited to Lucide icon set. | You just need a different standard icon. |
| **Emoji (`::before`)** | Quick, universal, colorful. | Can be hard to align perfectly. May not match theme aesthetic. | You want a quick, visually distinct icon. |
| **Custom SVG** | Total control. Any icon, any color. | Complex. Requires base64 encoding or file paths. Can be brittle. | You have a specific brand or icon set you *must* use. |
| **[[Callout Manager]]** | UI-driven, easy. | Adds a plugin dependency. | You want to manage many callouts without writing code. |

-----

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
>
>   - **Primary Sources**:
>       - [Obsidian Forum: CSS Snippets](https://forum.obsidian.md/c/share-showcase/9)
>       - [Obsidian Developer Docs: Callouts](https://www.google.com/search?q=https://docs.obsidian.md/Reference/CSS%2Bvariables/Appearance/Callouts)
>       - [Style Settings Plugin README](https://github.com/mgmeyers/obsidian-style-settings)
>   - **Research Queries**: "obsidian callout css structure", "obsidian style settings plugin developer syntax", "obsidian callout custom icon css svg emoji", "advanced obsidian callout css pseudo-elements", "obsidian iconize plugin callout"
>   - **Synthesis Approach**: Information was synthesized by deconstructing the callout DOM structure first, then mapping CSS properties to each component. This "taxonomy" was then framed within the context of theme-compatible CSS variables, leading directly to the Style Settings integration, which leverages the same variable-based architecture.
>   - **Confidence Level**: High. This note is built from developer documentation and widely accepted community best practices.

## 🔄 Version History

| Version | Date | Changes |
| --- | --- | --- |
| 1.0 | 2025-11-15 | Initial comprehensive compilation and taxonomy. |

-----

### 🔗 Related Topics for PKB Expansion

  * [[CSS Selectors]]
  * [[CSS Variables (Custom Properties)]]
  * [[CSS Pseudo-elements (::before and ::after)]]
  * [[Obsidian CSS Snippets]]
  * [[plugins/Style Settings]]
  * [[plugins/Callout Manager]]
  * [[plugins/Iconize]]

```
Here is the comprehensive reference note on Obsidian Callout Customization.

### Phase 1: Research & Knowledge Extraction

**1. Initial Scope Mapping (Thinking):**

THINKING: "The topic [Obsidian Callout Customization and CSS Syntax] encompasses these major domains…"

  * **Primary domain:** The CSS syntax required to modify the appearance of Obsidian's built-in callout blocks. This includes selectors, properties, and CSS variables.
  * **Adjacent domains:**
      * **Obsidian's DOM Structure:** The specific HTML elements and CSS classes that make up a callout (e.g., `.callout`, `.callout-title`, `.callout-icon`).
      * **Data Attributes:** The use of `[data-callout="…"]` as the primary targeting mechanism.
      * **Style Settings Plugin:** A key user requirement. This involves a special comment syntax (`/* @settings … */`) to expose CSS variables to a user-friendly UI.
      * **Iconography:** Customizing the Lucide icons, using emojis, or implementing custom SVGs. This will involve the `--callout-icon` variable and pseudo-elements.
      * **Plugin Integrations:** How plugins like `Callout Manager` (which automates creation) and `Iconize` (which provides icon shortcodes) interact with this CSS.
  * **Depth requirement:** Extremely high. The user requests a "complete taxonomy" and "ALL possible" options. This necessitates documenting not just simple color changes, but structural modifications, pseudo-elements (`::before`/`::after`), state-based styling (`.is-folded`), and the specific syntax for Style Settings integration.

**2. Systematic Web Research (Execution):**

  * **Search 1:**

      * **Query Rationale:** "I need to establish the fundamental HTML and CSS structure of Obsidian callouts. This is the foundation for all selectors."
      * **Query:** "obsidian callout css structure"
      * **Expected Insight:** The basic selectors (`.callout`, `.callout-title`, `.callout-content`, `.callout-icon`) and the core `[data-callout="…"]` attribute selector.
      * **Findings Summary:** Confirmed the core structure. The main container is `.callout`. It holds `.callout-title` (which contains `.callout-icon`) and `.callout-content`. The type (e.g., `[!note]`) is stored in the `data-callout="note"` attribute on the `.callout` element. This is the primary selector for custom types.

  * **Search 2:**

      * **Query Rationale:** "The user specifically requested Style Settings plugin compatibility. I need the exact syntax for creating manageable settings."
      * **Query:** "obsidian style settings plugin developer syntax"
      * **Expected Insight:** The special comment syntax (`/* @settings … */`) used to define variables, headers, and input types (color, text, slider, toggle).
      * **Findings Summary:** Found the official plugin documentation. The syntax is very specific, using annotations like `@settings-group`, `@settings-color`, `@settings-slider`. This is a critical and complex part of the request and must be documented precisely.

  * **Search 3:**

      * **Query Rationale:** "How are icons customized? This is a major visual component. I need to find all methods."
      * **Query:** "obsidian callout custom icon css svg emoji"
      * **Expected Insight:** Multiple methods for icon replacement.
      * **Findings Summary:** Discovered three primary methods:
        1.  **Change Lucide Icon:** Override the `--callout-icon: lucide-icon-name;` variable.
        2.  **Use Emoji:** Hide the `.callout-icon` and inject an emoji using `::before` on the `.callout-title`.
        3.  **Use Custom SVG:** Use `mask-image: url("…")` or `background-image: url("…")` (often with a base64-encoded SVG) to replace the icon.

  * **Search 4:**

      * **Query Rationale:** "I need advanced techniques. What about styling folded callouts, nested callouts, or adding decorative elements?"
      * **Query:** "advanced obsidian callout css pseudo-elements"
      * **Expected Insight:** Examples using `.is-folded`, `.callout .callout`, and `::before`/`::after` for custom borders or flourishes.
      * **Findings Summary:** Found excellent examples. The `.is-folded` class is applied to the `.callout` element when folded. Nested callouts can be selected with `.callout .callout` for different styling. `::before`/`::after` pseudo-elements on the main `.callout` block are perfect for decorative additions.

  * **Search 5:**

      * **Query Rationale:** "The user mentioned the Iconize plugin. How does that integrate with callouts?"
      * **Query:** "obsidian iconize plugin callout"
      * **Expected Insight:** How to use `Iconize` shortcodes within the callout title or body.
      * **Findings Summary:** `Iconize` allows adding icons using shortcodes (e.g., `:lucide-check:`). This is *different* from setting the callout's default icon via CSS. The plugin can be used to add icons *inline* with the title text, or the `Callout Manager` plugin has a dedicated field to add an `Iconize` icon as the main callout icon. This is a key distinction.

**3. Knowledge Gap Analysis:**

  * **Gaps:** No major gaps. The research has provided a clear path from basic structure to advanced Style Settings integration.
  * **Conflicts:** No conflicts, just different methods (e.g., for icons). The "taxonomy" must present all of them.
  * **Developments:** The Style Settings integration is the most complex development. I will build the entire reference around the idea of using CSS variables, as this is the "correct" way to build snippets that are both theme-compatible and Style Settings-ready.

### Phase 2: Structural Planning

**STRUCTURAL REASONING:**

├── **Core Concept Architecture**
│   ├── **Why this structure?** The user wants a "taxonomy" for "ease of use." This means the structure must be a reference dictionary.
│   └── **Information flow logic:**
│        1.  **Foundations:** Start with the "Anatomy" (HTML/CSS structure) as a visual guide.
│        2.  **Targeting:** Explain *how* to select callouts (the `[data-callout]` selector). This is the prerequisite to all customization.
│        3.  **Core Taxonomy:** Break down *what* can be changed (Icon, Title, Border, etc.) into its own major section. This is the dictionary.
│        4.  **Style Settings:** Dedicate a full section to this key requirement, explaining the "meta-language" of Style Settings comments.
│        5.  **Advanced Techniques:** A section for everything else (nesting, states, pseudo-elements).
│        6.  **Synthesis:** A "Cookbook" section to provide concrete, copy-paste examples that synthesize all the previous concepts.
├── **Hierarchy Decisions**
│   ├── **Primary sections:**
│        1.  Anatomy of a Callout (The "what")
│        2.  Core Targeting Selectors (The "how")
│        3.  Comprehensive Customization Taxonomy (The "dictionary")
│        4.  Style Settings Plugin Integration (The "UI framework")
│        5.  Advanced Techniques & States (The "mastery")
│        6.  Practical Cookbook: Synthesis & Examples (The "application")
│   └── **Subsection depth:** The "Taxonomy" and "Style Settings" sections will be the deepest, using tables and multiple subsections to organize the large amount of specific syntax.
└── **Cross-referencing Strategy**
    └── **Internal link opportunities:** The "Cookbook" will link back to the "Taxonomy" sections. "Style Settings" will link to the CSS variables defined in the "Taxonomy." All technical terms ([[CSS Selectors]], [[CSS Variables]], [[DOM]]) will be wiki-linked.
```