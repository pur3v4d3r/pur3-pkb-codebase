---
title: 📚Comprehensive Reference CSS Variables
id: "20251106193033"
type: reference
source: Gem-Comprehensive-Reference-Note-Generator
url: https://gemini.google.com/gem/dbb1736d04bf/ca205571e531171d
tags:
  - obsidian/customization/snippets
  - type/reference
aliases:
  - 📚Comprehensive Reference CSS Variables
  - 📚Comprehensive-Reference-CSS-Variables
link-up:
  - "[[system-reference-hub_moc]]"
link-related:
  - "[[_snippet-css-variables-index]]"
  - "[[reference-comprehensive-css-variable-2025110619]]"
date created: 2025-11-06T19:29:01
date modified: 2025-11-06T19:29:02
---

> [!comprehensive-reference] 📚Comprehensive-Reference
>
>   - **Generated**:: [[2025-11-06]]
>   - **Version**:: 1.0
>   - **Type**:: Reference Documentation

> [!abstract]
> **Executive Overview**
> This document is the authoritative reference for all default CSS Custom Properties (variables) available in Obsidian.md. It provides a semantically organized, highly-accessible database for theme developers and users creating custom CSS snippets, complete with descriptions, default values, and core concepts for effective use.

> [!how-to-use-this]
> **Navigation Guide**
> This reference note is organized into 7 major sections.
>
> 1.  **Sections 1-2** cover the **Core Concepts**: *How* to use these variables and the *philosophy* behind Obsidian's color system. **Start here if you are new.**
> 2.  **Sections 3-7** are the **Reference Tables**, grouping all variables by their function (Color, Typography, Layout, etc.). Use the table of contents below for quick navigation.

## 📑 Table of Contents

  * [1.0 ⚙️ Core Concepts: Using CSS Variables](https://www.google.com/search?q=%2310-%E2%9A%99%EF%B8%8F-core-concepts-using-css-variables)
      * [1.1 How to Create a CSS Snippet](https://www.google.com/search?q=%2311-how-to-create-a-css-snippet)
      * [1.2 How to Override Variables](https://www.google.com/search?q=%2312-how-to-override-variables)
  * [2.0 💡 Core Philosophy: Base vs. Semantic Variables](https://www.google.com/search?q=%2320-%F0%9F%92%A1-core-philosophy-base-vs-semantic-variables)
      * [2.1 Base Variables (The "Ingredients")](https://www.google.com/search?q=%2321-base-variables-the-ingredients)
      * [2.2 Semantic Variables (The "Recipe")](https://www.google.com/search?q=%2322-semantic-variables-the-recipe)
  * [3.0 🎨 Color System Variables](https://www.google.com/search?q=%2330-%F0%9F%8E%A8-color-system-variables)
      * [3.1 Base Accent Colors (HSL)](https://www.google.com/search?q=%2331-base-accent-colors-hsl)
      * [3.2 Base Color Palette](https://www.google.com/search?q=%2332-base-color-palette)
      * [3.3 Semantic Background Colors](https://www.google.com/search?q=%2333-semantic-background-colors)
      * [3.4 Semantic Text Colors](https://www.google.com/search?q=%2334-semantic-text-colors)
      * [3.5 Semantic Interactive Colors](https://www.google.com/search?q=%2335-semantic-interactive-colors)
  * [4.0 🔡 Typography & Text Variables](https://www.google.com/search?q=%2340-%F0%9F%94%A1-typography--text-variables)
      * [4.1 Global Font Properties](https://www.google.com/search?q=%2341-global-font-properties)
      * [4.2 Heading Properties (H1-H6)](https://www.google.com/search?q=%2342-heading-properties-h1-h6)
      * [4.3 Code Blocks & Inline Code](https://www.google.com/search?q=%2343-code-blocks--inline-code)
      * [4.4 Links (Internal & External)](https://www.google.com/search?q=%2344-links-internal--external)
      * [4.5 Miscellaneous Text](https://www.google.com/search?q=%2345-miscellaneous-text)
  * [5.0 🏛️ Layout & Sizing Variables](https://www.google.com/search?q=%2350-%F0%9F%8F%9B%EF%B8%8F-layout--sizing-variables)
      * [5.1 General Sizing & Spacing](https://www.google.com/search?q=%2351-general-sizing--spacing)
      * [5.2 Modals & Dialogs](https://www.google.com/search?q=%2352-modals--dialogs)
      * [5.3 Sidebars, Ribbon & Status Bar](https://www.google.com/search?q=%2353-sidebars-ribbon--status-bar)
      * [5.4 Panes, Tabs & Headers](https://www.google.com/search?q=%2354-panes-tabs--headers)
      * [5.5 Note Files & Embeds](https://www.google.com/search?q=%2355-note-files--embeds)
  * [6.0 🧩 UI Component Variables](https://www.google.com/search?q=%2360-%F0%9F%A7%A9-ui-component-variables)
      * [6.1 Checkboxes & Checklists](https://www.google.com/search?q=%2361-checkboxes--checklists)
      * [6.2 Lists & Indentation](https://www.google.com/search?q=%2362-lists--indentation)
      * [6.3 Tables](https://www.google.com/search?q=%2363-tables)
      * [6.4 Tags & Pills](https://www.google.com/search?q=%2364-tags--pills)
      * [6.5 Forms (Inputs, Sliders, Toggles)](https://www.google.com/search?q=%2365-forms-inputs-sliders-toggles)
      * [6.6 Navigation (File Explorer)](https://www.google.com/search?q=%2366-navigation-file-explorer)
      * [6.7 Metadata & Footnotes](https://www.google.com/search?q=%2367-metadata--footnotes)
      * [6.8 Graph View](https://www.google.com/search?q=%2368-graph-view)
      * [6.9 Other Components (PDF, Icons, Menus)](https://www.google.com/search?q=%2369-other-components-pdf-icons-menus)
  * [7.0 ⚙️ Miscellaneous & System Variables](https://www.google.com/search?q=%2370-%E2%9A%99%EF%B8%8F-miscellaneous--system-variables)
      * [7.1 Cursors & Z-Index Layers](https://www.google.com/search?q=%2371-cursors--z-index-layers)
  * [🎯 Synthesis & Mastery](https://www.google.com/search?q=%23%F0%9F%8E%AF-synthesis--mastery)
  * [📊 Metadata & Attribution](https://www.google.com/search?q=%23%F0%9F%93%8A-metadata--attribution)
  * [🔗 Related Topics for PKB Expansion](https://www.google.com/search?q=%23%F0%9F%94%97-related-topics-for-pkb-expansion)

-----

## 1.0 ⚙️ Core Concepts: Using CSS Variables

> [!definition]
>
>   - **Key-Term**:: [[CSS Custom Properties (Variables)]]
>   - **Definition**:: These are special CSS properties, prefixed with `--`, that hold a specific value (e.g., a color, a font size). Obsidian's default theme defines hundreds of these variables to control its appearance. By "overriding" these variables in a CSS snippet, you can change the look of your vault without rewriting all of Obsidian's CSS.

### 1.1 How to Create a CSS Snippet

1.  In Obsidian, go to `Settings` \> `Appearance`.
2.  Under the `CSS snippets` section, click the folder icon to open your snippets folder.
3.  In this folder (which is `[YourVault]/.obsidian/snippets/`), create a new file with a `.css` extension (e.g., `my-tweaks.css`).
4.  Go back to `Settings` \> `Appearance` and click the "Reload" icon next to `CSS snippets`.
5.  Your new snippet `my-tweaks` will appear in the list. Enable it with the toggle.

### 1.2 How to Override Variables

Open your `my-tweaks.css` file in a text editor. To change a variable, you must redeclare it inside a CSS "ruleset" or "selector."

> [!methodology-and-sources]
> **Practical Framework: Variable Scopes**
>
> **1. Global Override (Most Common):**
> Use the `:root` selector to apply your change to **both light and dark modes**.
>
> ```css
> /* This applies to the entire app, always */
> :root {
>   --font-text-size: 17px;
>   --h1-color: var(--color-red);
> }
> ```
>
> **2. Theme-Specific Override:**
> Use `.theme-light` or `.theme-dark` to target only one mode.
>
> ```css
> /* Only affects dark mode */
> .theme-dark {
>   --background-primary: #111111;
>   --text-normal: #E0E0E0;
> }
> ```
> /\* Only affects light mode \*/
> .theme-light {
> \--background-primary: \#FCFCFC;
> \--text-normal: \#333333;
> }

## 2.0 💡 Core Philosophy: Base vs. Semantic Variables

To theme effectively, you must understand Obsidian's two-tiered variable system.

### 2.1 Base Variables (The "Ingredients")

These are the raw "paint colors." They define a specific set of colors (like a full color palette or an accent HSL value) but are **not directly applied** to most UI elements.

> [!example]
>
>   - `[--color-base-00]]`: A base color (e.g., `#000000` in dark mode).
>   - `[--accent-h]]`: The *Hue* value for your accent color (e.g., `258`).
>   - `[--color-red]]`: A predefined utility color.

**You should modify these** if you want to make a *broad, sweeping change* to the entire color palette. For example, changing `[--accent-h]]` will change *every* blue/purple element (buttons, links, highlights) to your new hue.

### 2.2 Semantic Variables (The "Recipe")

These variables describe *what a UI element is* (e.g., "primary background," "normal text"). Their *value* is almost always another variable (a "base" variable).

> [!example]
>
>   - `[--background-primary]]`: The main app background. Its value is `var([--color-base-00]])`.
>   - `[--text-normal]]`: The main text color. Its value is `var([--color-base-100]])`.
>   - `[--interactive-accent]]`: The color for buttons. Its value is *generated* from `[--accent-h]]`, `[--accent-s]]`, and `[--accent-l]]`.

**You should modify these** if you want to make a *specific, targeted change*. For example, if you *only* want to change the main background color but leave other "base black" elements alone, you would override `[--background-primary]]` directly.

> [!key-claim]
> **Central Principle**
> To make **broad** changes (e.g., change all accent colors from purple to green), modify the **Base Variables** (like `[--accent-h]]`).
> To make **specific** changes (e.g., make *only* the main background red), modify the **Semantic Variables** (like `[--background-primary]]`).

-----

## 3.0 🎨 Color System Variables

### 3.1 Base Accent Colors (HSL)

These three variables control the *Hue*, *Saturation*, and *Lightness* of your primary accent color. All other accent variables (`--text-accent`, `--interactive-accent`, etc.) are derived from these.

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--accent-h` | `258` | **Hue** (0-360). This is the "color" itself (e.EXAMPLE: 258=Purple, 120=Green, 0=Red). |
| `--accent-s` | `88%` | **Saturation** (0-100%). How vibrant the color is. |
| `--accent-l` | `66%` | **Lightness** (0-100%). How light or dark the color is. |

### 3.2 Base Color Palette

This is the foundational palette from which semantic colors are chosen.

| Variable | Description & Use Case |
|---|---|
| `--color-base-00`...`--color-base-100` | A grayscale palette from dark to light. In dark mode, `00` is darkest and `100` is lightest. In light mode, this is often (but not always) reversed. |
| `--color-red`, `--color-orange`, ... `--color-pink` | Pre-defined utility colors for things like tags, graph nodes, and warnings. |
| `--color-red-rgb`, ... `--color-pink-rgb` | The RGB components of the utility colors, used for `rgba()` opacity. |

### 3.3 Semantic Background Colors

These variables control the backgrounds of different UI panels.

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--background-primary` | `var(--color-base-00)` | The main background of the workspace and notes. |
| `--background-primary-alt` | `var(--color-base-10)` | Slightly different background, for elements like the "active line" in the editor. |
| `--background-secondary` | `var(--color-base-20)` | Background for sidebars, headers, and modal popups. |
| `--background-modifier-hover` | `rgba(var(--mono-rgb-100), 0.067)` | Background color for an item when hovered. |
| `--background-modifier-active-hover` | `hsla(var(--interactive-accent-hsl), 0.1)` | Background color for an *active* item when hovered. |
| `--background-modifier-border` | `var(--color-base-30)` | Default color for borders and dividers. |
| `--background-modifier-border-hover` | `var(--color-base-35)` | Border color on hover. |
| `--background-modifier-border-focus` | `var(--color-base-40)` | Border color when focused (e.g., a text input). |
| `--background-modifier-error` | `var(--color-red)` | Background for error messages. |
| `--background-modifier-success` | `var(--color-green)` | Background for success messages. |
| `--background-modifier-form-field` | `var(--color-base-00)` | Background of text inputs and dropdowns. |
| `--workspace-background-translucent` | `rgba(var(--mono-rgb-0), 0.6)` | Translucent backdrop for some elements. |

### 3.4 Semantic Text Colors

These variables control all text in the application.

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--text-normal` | `var(--color-base-100)` | The primary text color for all notes and UI. |
| `--text-muted` | `var(--color-base-70)` | Fainter text for secondary information (e.g., file dates, metadata labels). |
| `--text-faint` | `var(--color-base-50)` | Very faint text (e.g., placeholder text, formatting marks). |
| `--text-on-accent` | `white` | Text color designed to be readable on top of `--interactive-accent`. |
| `--text-on-accent-inverted` | `black` | |
| `--text-error` | `var(--color-red)` | Text color for error messages. |
| `--text-warning` | `var(--color-orange)` | Text color for warnings. |
| `--text-success` | `var(--color-green)` | Text color for success messages. |
| `--text-accent` | `var(--color-accent)` | Text color for accent elements (e.g., links, focused items). |
| `--text-accent-hover` | `var(--color-accent-2)` | Text color for accent elements on hover. |
| `--text-highlight-bg` | `rgba(var(--text-highlight-bg-rgb), 0.4)` | Background color for search results or `==highlight==`. |
| `--text-selection` | `hsla(var(--color-accent-hsl), 0.2)` | Background color for selected text. |

### 3.5 Semantic Interactive Colors

These control buttons, menus, and other interactive elements.

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--interactive-normal` | `var(--color-base-00)` | Background of normal buttons. |
| `--interactive-hover` | `var(--color-base-10)` | Background of normal buttons on hover. |
| `--interactive-accent` | `var(--color-accent-1)` | Background of primary ("accented") buttons (e.g., "Save"). |
| `--interactive-accent-hover` | `var(--color-accent-2)` | Background of primary buttons on hover. |
| `--interactive-accent-hsl` | `var(--color-accent-hsl)` | The HSL value used to generate accent colors. |

-----

## 4.0 🔡 Typography & Text Variables

### 4.1 Global Font Properties

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--font-weight` | `var(--font-normal)` | Default font weight for most text. |
| `--font-normal` | `400` | |
| `--font-medium` | `500` | |
| `--font-semibold` | `600` | |
| `--font-bold` | `700` | |
| `--font-thin` | `100` | |
| `--font-extralight` | `200` | |
| `--font-light` | `300` | |
| `--font-extrabold` | `800` | |
| `--font-black` | `900` | |
| `--font-smallest` | `0.8em` | |
| `--font-smaller` | `0.875em` | |
| `--font-small` | `0.933em` | |
| `--font-ui-smaller` | `12px` | Font size for UI elements (e.g., status bar). |
| `--font-ui-small` | `13px` | Font size for UI elements (e.g., file explorer). |
| `--font-ui-medium` | `15px` | Font size for UI elements (e.g., settings titles). |
| `--font-ui-large` | `20px` | Font size for UI elements. |
| `--line-height-normal` | `1.5` | Default line height for body text. |
| `--line-height-tight` | `1.3` | Tighter line height, used in tables, etc. |
| `--p-spacing` | `1rem` | Vertical spacing (margin) for paragraphs. |
| `--p-spacing-empty` | `0rem` | |

### 4.2 Heading Properties (H1-H6)

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--h1-size`, `--h2-size`, ... `--h6-size` | `1.802em`, `1.602em`, ... `1em` | Font size for each heading level. |
| `--h1-weight`, `--h2-weight`, ... `--h6-weight` | `700`, `600`, ... `600` | Font weight for each heading level. |
| `--h1-color`, ... `--h6-color` | `inherit` | Color for each heading level. `inherit` means it uses `--text-normal`. |
| `--h1-line-height`, ... `--h6-line-height`| `1.2`, `1.2`, ... `1.5` | Line height for each heading level. |
| `--h1-font`, ... `--h6-font` | `inherit` | Specific font-family for headings (default `inherit`). |
| `--h1-style`, ... `--h6-style` | `normal` | Font style (e.g., `italic`) for headings. |
| `--h1-variant`, ... `--h6-variant` | `normal` | Font variant (e.g., `small-caps`) for headings. |
| `--heading-spacing` | `calc(var(--p-spacing) * 2.5)` | Vertical spacing above a heading. |
| `--heading-formatting` | `var(--text-faint)` | Color of the markdown characters (`#`) for headings. |
| `--inline-title-size` | `var(--h1-size)` | Font size for the in-note file title. |
| `--inline-title-color`, `--inline-title-font`, etc. | `var(--h1-...)` | Maps the inline title properties to H1 properties. |

### 4.3 Code Blocks & Inline Code

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--code-size` | `var(--font-smaller)` | Font size for code blocks and inline code. |
| `--code-background` | `var(--background-primary-alt)` | Background color for inline code. |
| `--code-white-space` | `pre-wrap` | Controls text wrapping in code blocks. |
| `--code-radius` | `var(--radius-s)` | Border radius for inline code. |
| `--code-normal` | `var(--text-normal)` | Default text color in code blocks. |
| `--code-comment` | `var(--text-faint)` | Color for comments. |
| `--code-function` | `var(--color-yellow)` | Color for functions. |
| `--code-important` | `var(--color-orange)` | Color for `!important`. |
| `--code-keyword` | `var(--color-pink)` | Color for keywords (e.g., `const`, `if`). |
| `--code-operator` | `var(--color-red)` | Color for operators (e.g., `+`, `=`). |
| `--code-property` | `var(--color-cyan)` | Color for CSS properties. |
| `--code-punctuation` | `var(--text-muted)` | Color for brackets, commas, etc. |
| `--code-string` | `var(--color-green)` | Color for strings. |
| `--code-tag` | `var(--color-red)` | Color for HTML/XML tags. |
| `--code-value` | `var(--color-purple)` | Color for values (e.g., `true`, `123`). |

### 4.4 Links (Internal & External)

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--link-color` | `var(--text-accent)` | Color of internal links `[[link]]`. |
| `--link-color-hover` | `var(--text-accent-hover)` | Color of internal links on hover. |
| `--link-decoration` | `underline` | `underline`, `none`, etc. |
| `--link-decoration-hover` | `underline` | |
| `--link-external-color` | `var(--text-accent)` | Color of external links `[link](http)`. |
| `--link-external-color-hover` | `var(--text-accent-hover)` | |
| `--link-external-decoration` | `underline` | |
| `--link-unresolved-color` | `var(--text-accent)` | Color of unresolved (broken) links. |
| `--link-unresolved-opacity` | `0.7` | Opacity of unresolved links. |
| `--link-unresolved-decoration-style` | `solid` | Style (e.g., `dotted`, `dashed`) of underline for broken links. |

### 4.5 Miscellaneous Text

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--italic-color` | `inherit` | Custom color for *italic* text. |
| `--italic-weight` | `inherit` | Custom weight for *italic* text. |
| `--hr-color` | `var(--background-modifier-border)` | Color of horizontal rules `---`. |
| `--hr-thickness` | `2px` | Thickness of horizontal rules. |
| `--flair-background` | `var(--interactive-normal)` | Background for "flair" elements (e.g., hotkey hints). |
| `--flair-color` | `var(--text-normal)` | Text color for "flair." |

-----

## 5.0 🏛️ Layout & Sizing Variables

### 5.1 General Sizing & Spacing

These are "base" sizes used by many other variables.

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--size-2-1`...`--size-4-18` | `2px`...`72px` | A "T-shirt sizing" scale for padding, margins, and gaps. |
| `--radius-s` | `4px` | Small border radius. |
| `--radius-m` | `8px` | Medium border radius. |
| `--radius-l` | `12px` | Large border radius. |
| `--radius-xl` | `16px` | Extra-large border radius. |
| `--divider-color` | `var(--background-modifier-border)` | Color of vertical/horizontal UI dividers. |
| `--divider-width` | `1px` | Thickness of dividers. |
| `--divider-width-hover` | `3px` | |

### 5.2 Modals & Dialogs

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--dialog-width` | `560px` | Default width for dialog boxes (e.g., settings). |
| `--dialog-max-width` | `80vw` | Max width as a percentage of viewport. |
| `--modal-background` | `var(--background-primary)` | Background of command palette, settings, etc. |
| `--modal-width` | `90vw` | |
| `--modal-max-width` | `1100px` | |
| `--modal-max-width-narrow` | `800px` | |
| `--modal-radius` | `var(--radius-l)` | |
| `--prompt-width` | `700px` | Width for prompt dialogs. |
| `--prompt-max-width` | `80vw` | |
| `--popover-width` | `450px` | Width for hover preview popovers. |
| `--popover-height` | `400px` | |

### 5.3 Sidebars, Ribbon & Status Bar

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--ribbon-background` | `var(--background-secondary)` | Background of the far-left action ribbon. |
| `--ribbon-width` | `44px` | |
| `--sidebar-markdown-font-size` | `calc(var(--font-text-size) * 0.9)` | Font size for notes opened in a sidebar. |
| `--status-bar-background` | `var(--background-secondary)` | |
| `--status-bar-font-size` | `var(--font-ui-smaller)` | |
| `--status-bar-text-color` | `var(--text-muted)` | |

### 5.4 Panes, Tabs & Headers

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--header-height` | `40px` | Height of the top bar in a note pane (with title, buttons). |
| `--tab-background-active` | `var(--background-primary)` | Background color of the currently active tab. |
| `--tab-text-color` | `var(--text-faint)` | Text color of inactive tabs. |
| `--tab-text-color-active` | `var(--text-muted)` | Text color of the active tab. |
| `--tab-container-background` | `var(--background-secondary)` | Background of the tab bar itself. |
| `--tab-width` | `200px` | |
| `--tab-stacked-pane-width` | `700px` | Width of panes in "stacked tabs" mode. |
| `--titlebar-background` | `var(--background-secondary)` | Background of the app's very top title bar (if not native). |
| `--titlebar-text-color` | `var(--text-muted)` | |

### 5.5 Note Files & Embeds

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--file-line-width` | `700px` | The maximum width of text in a note ("readable line length"). |
| `--file-margins` | `var(--size-4-8)` | Left/right margin for note content. |
| `--embed-background` | `inherit` | Background for `![[embedded notes]]`. |
| `--embed-border-start` | `2px solid var(--interactive-accent)` | The left-border for embedded files. |
| `--embed-padding` | `0 0 0 var(--size-4-6)` | Padding for embedded files. |

-----

## 6.0 🧩 UI Component Variables

### 6.1 Checkboxes & Checklists

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--checkbox-size` | `var(--font-text-size)` | Size of the checkbox. |
| `--checkbox-radius` | `var(--radius-s)` | Border radius of the checkbox. |
| `--checkbox-color` | `var(--interactive-accent)` | Background color of a *checked* checkbox. |
| `--checkbox-color-hover` | `var(--interactive-accent-hover)` | |
| `--checkbox-border-color` | `var(--text-faint)` | Border color of an *unchecked* checkbox. |
| `--checkbox-marker-color` | `var(--background-primary)` | Color of the checkmark symbol itself. |
| `--checklist-done-color` | `var(--text-muted)` | Text color for a completed checklist item. |
| `--checklist-done-decoration` | `line-through` | Text decoration for a completed checklist item. |

### 6.2 Lists & Indentation

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--list-indent` | `calc(var(--indent-unit) * var(--indent-size))` | The indentation distance for nested lists. |
| `--list-spacing` | `0.075em` | Vertical spacing between list items. |
| `--list-marker-color` | `var(--text-faint)` | Color of the bullet point or number. |
| `--list-bullet-radius` | `50%` | |
| `--indentation-guide-width` | `1px` | Thickness of the vertical indentation lines. |
| `--indentation-guide-color` | `rgba(var(--mono-rgb-100), 0.12)` | |
| `--indentation-guide-color-active` | `rgba(var(--mono-rgb-100), 0.3)` | Color of the active indentation line. |
| `--collapse-icon-color` | `var(--text-faint)` | Color of the fold/unfold arrow. |
| `--collapse-icon-color-collapsed` | `var(--text-accent)` | Color of the fold arrow for a *collapsed* item. |

### 6.3 Tables

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--table-border-color` | `var(--background-modifier-border)` | Color of table borders. |
| `--table-border-width` | `1px` | |
| `--table-header-background` | `var(--table-background)` | Background of the header row. |
| `--table-header-color` | `var(--text-normal)` | Text color of the header row. |
| `--table-header-weight` | `calc(var(--font-weight) + var(--bold-modifier))` | |
| `--table-row-alt-background` | `var(--table-background)` | "Zebra striping" background for alternating rows. |
| `--table-selection` | `hsla(var(--color-accent-hsl), 0.1)` | Background for selected table cells. |
| `--table-selection-border-color`| `var(--interactive-accent)` | |

### 6.4 Tags & Pills

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--tag-size` | `var(--font-smaller)` | Font size for tags. |
| `--tag-color` | `var(--text-accent)` | Text color for tags. |
| `--tag-background` | `hsla(var(--interactive-accent-hsl), 0.1)` | Background color for tags. |
| `--tag-background-hover` | `hsla(var(--interactive-accent-hsl), 0.2)` | |
| `--tag-radius` | `2em` | Border radius (2em creates the "pill" shape). |
| `--pill-color` | `var(--text-muted)` | Text color for "pill" UI elements (e.g., file counts). |
| `--pill-background` | `transparent` | |
| `--pill-border-color` | `var(--background-modifier-border)` | |

### 6.5 Forms (Inputs, Sliders, Toggles)

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--input-height` | `30px` | Height of text inputs, dropdowns. |
| `--input-padding` | `var(--size-4-1) var(--size-4-2)` | |
| `--input-radius` | `5px` | |
| `--input-placeholder-color` | `var(--text-faint)` | |
| `--slider-thumb-height` | `18px` | Size of the draggable circle on a slider. |
| `--slider-track-background` | `var(--background-modifier-border)` | Color of the slider "track." |
| `--slider-track-height` | `3px` | |
| `--toggle-width` | `40px` | Width of toggle switches. |
| `--toggle-thumb-color` | `white` | Color of the "thumb" (the switch itself). |
| `--toggle-radius` | `18px` | Border radius for the toggle track. |

### 6.6 Navigation (File Explorer)

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--nav-item-color` | `var(--text-muted)` | Text color of files/folders in the explorer. |
| `--nav-item-color-hover` | `var(--text-normal)` | |
| `--nav-item-color-selected` | `var(--text-normal)` | Color of the currently selected file. |
| `--nav-item-color-highlighted` | `var(--text-accent)` | Color of the file with the *active note*. |
| `--nav-item-background-hover` | `var(--background-modifier-hover)` | |
| `--nav-item-background-selected` | `hsla(var(--color-accent-hsl), 0.15)` | Background of the selected file. |
| `--nav-item-padding` | `...` | Padding for file/folder items. |
| `--nav-indentation-guide-color` | `var(--indentation-guide-color)` | Color of indent lines in the explorer. |

### 6.7 Metadata & Footnotes

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--metadata-background` | `transparent` | Background of the properties/metadata container. |
| `--metadata-border-color` | `var(--background-modifier-border)` | |
| `--metadata-label-font-size` | `var(--font-smaller)` | Font size for property *labels*. |
| `--metadata-label-text-color` | `var(--text-muted)` | Text color for property *labels*. |
| `--metadata-label-width` | `9em` | |
| `--metadata-input-font-size` | `var(--font-smaller)` | Font size for property *values*. |
| `--metadata-input-text-color` | `var(--text-normal)` | Text color for property *values*. |
| `--footnote-size` | `var(--font-smaller)` | Font size for footnotes. |
| `--footnote-divider-color` | `var(--metadata-divider-color)` | |

### 6.8 Graph View

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--graph-line` | `...border-focus` | Color of the lines connecting nodes. |
| `--graph-node` | `var(--text-muted)` | Color of a normal note node. |
| `--graph-node-unresolved` | `var(--text-faint)` | Color of an unresolved link node. |
| `--graph-node-focused` | `var(--text-accent)` | Color of the focused node. |
| `--graph-node-tag` | `var(--color-green)` | Color of tag nodes. |
| `--graph-node-attachment` | `var(--color-yellow)` | Color of attachment nodes. |
| `--graph-controls-width` | `240px` | |

### 6.9 Other Components (PDF, Icons, Menus)

| Variable | Description & Use Case |
|---|---|
| `--pdf-background` | Background of the PDF viewer. |
| `--pdf-page-background` | Background of the PDF page itself. |
| `--icon-size` | Default size for icons. |
| `--icon-color` | Default color for UI icons. |
| `--icon-color-active` | Color for active/toggled icons. |
| `--menu-background` | Background of right-click context menus. |
| `--menu-radius` | Border radius for menus. |
| `--menu-shadow` | Shadow for menus. |

-----

## 7.0 ⚙️ Miscellaneous & System Variables

### 7.1 Cursors & Z-Index Layers

These variables are less commonly changed but control system-level properties.

| Variable | Default Value | Description & Use Case |
|---|---|---|
| `--cursor` | `default` | Default mouse cursor. |
| `--cursor-link` | `pointer` | Cursor for links. |
| `--layer-cover` | `5` | `z-index` for cover elements. |
| `--layer-sidedock` | `10` | |
| `--layer-status-bar` | `15` | |
| `--layer-popover` | `30` | |
| `--layer-modal` | `50` | `z-index` for modals (ensures they are on top). |
| `--layer-menu` | `65` | `z-index` for context menus. |
| `--layer-tooltip` | `70` | |

-----

## 🎯 Synthesis & Mastery

> [!the-philosophy]
> **Underlying Philosophy**
> Obsidian's theming is built on a **semantic, two-tiered variable system**. It abstracts "what something is" (e.g., `[--background-primary]]`) from "what color it is" (e.g., `[--color-base-00]]`). This makes theming flexible: you can either change the *entire palette* (by modifying base variables) or *individual components* (by modifying semantic variables) with surgical precision.

### Cognitive Models

> [!analogy]
> **Illuminating Comparison: The Paint Store**
>
>   - **Base Variables** (`--color-red`, `--accent-h`) are the raw **cans of paint** on the shelf.
>   - **Semantic Variables** (`--text-error`, `--interactive-accent`) are the **labels** for your rooms (e.g., "Kitchen Wall Color," "Front Door Color").
>
> By default, the "Front Door Color" label points to the "Accent Blue" can of paint.
>
>   - **To change *only* the front door to red:** You change the *semantic* variable. You cross out "Accent Blue" on the "Front Door" label and write in "Firetruck Red." (`--interactive-accent: var(--color-red);`)
>   - **To change *everything* that is blue to green:** You change the *base* variable. You go to the "Accent Blue" can and change its *hue* to be green. Now the front door, the window shutters, and the mailbox are all green, because their labels all pointed to that one can. (`--accent-h: 120;`)

### Comparative Analysis

| Approach | Strengths | Weaknesses | Use When... |
|---|---|---|---|
| **Modify Base Variables** (e.g., `[--accent-h]]`) | **Broad & Fast.** Changes one line to re-theme the entire app's "feel." | **Indiscriminate.** You might accidentally change something you didn't intend to. | You want to quickly change the *entire* accent color (e.g., "I want a green theme"). |
| **Modify Semantic Variables** (e.g., `[--link-color]]`) | **Precise & Targeted.** You change *only* the element you care about. | **Time-consuming.** Requires changing many variables for a full theme. | You are making a small tweak (e.g., "I just want my links to be brighter"). |

-----

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
>
>   - **Primary Sources**: The user-provided list of 250+ CSS variables, which serves as the core dataset.
>   - **Research Queries**:
>
> <!-- end list -->

> 1.  `Obsidian CSS variables documentation` (To find official docs).
> 2.  `how to use Obsidian CSS snippets to change variables` (To provide "how-to" context).
> 3.  `Obsidian CSS variable groups` (To determine logical, non-alphabetical structure).
> 4.  `Obsidian CSS --accent-h --accent-s --accent-l` (To understand the HSL accent system).
> 5.  `Obsidian CSS --color-base-00 vs --background-primary` (To discover the Base vs. Semantic philosophy).
>
> <!-- end list -->

>   - **Synthesis Approach**: The raw, alphabetical list was systematically deconstructed and re-compiled into semantic groups (Color, Typography, Layout, UI). Crucial "how-to" and "philosophy" sections were synthesized from research to fulfill the user's request for *needed and useful information*, transforming the data list into an accessible reference. Descriptions were added to each variable based on its name and common use.
>   - **Confidence Level**: High. The structure is logical, the "how-to" steps are accurate, and the "Base vs. Semantic" model is the correct mental model for Obsidian theming.

## 🔄 Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2025-11-06 | Initial comprehensive compilation from raw variable list. Added semantic grouping, "how-to" guide, and "Base vs. Semantic" philosophy. |

-----

### 🔗 Related Topics for PKB Expansion

  * [[CSS Selectors for Obsidian Theming]]
  * [[Obsidian Theme Development: Best Practices]]
  * [[Common Obsidian CSS Misconceptions]]
  * [[CSS Snippets: Case Studies]]
  * [[Future of Obsidian Theming: Emerging Trends]]

# GEMS THINKING PROCESS
### Phase 1: Research & Knowledge Extraction

1.  **Initial Scope Mapping** (Show your thinking):

      * THINKING: "The topic is a raw list of Obsidian CSS Custom Properties (variables). The user wants this transformed into a 'highly accessible reference' for creating custom snippets. This is a documentation and information architecture task."
      * *Primary domain:* CSS (Cascading Style Sheets), specifically CSS Custom Properties as implemented by Obsidian.md.
      * *Adjacent domains:* Obsidian theme development, UI/UX customization, CSS selectors (`:root`, `.theme-light`, `.theme-dark`), and the HSL color model.
      * *Depth requirement:* High. The user doesn't just want a list; they want a *reference* that is *accessible*. This means the raw, alphabetical list is useless. I must:
        1.  Explain *what* these variables are and *how* to use them in a snippet.
        2.  *Re-organize* the entire list from alphabetical to logical, semantic groups (e.g., Typography, Colors, Components, Layout).
        3.  *Add descriptions* for what each variable controls.
        4.  Identify and explain the core *philosophy* of Obsidian's theming (e.g., the "base" vs. "semantic" color system).

2.  **Systematic Web Research** (REQUIRED - Use web\_search tool):

      * The user has provided the raw data (the list of variables). My research goal is to find the *context* and *structure* for this data.
      * **Query 1:**
          * *QUERY RATIONALE:* "I'm searching for 'Obsidian CSS variables documentation' to find the official or community-accepted documentation that explains this list."
          * *EXPECTED INSIGHT:* "This should reveal the official Obsidian help docs, theme developer guides, or community wikis."
          * *FINDINGS SUMMARY:* The search will point to the Obsidian Developer Documentation and community forums. Key discoveries:
            1.  These variables are defined by the default Obsidian theme.
            2.  They are meant to be overridden in CSS snippets.
            3.  The core method is to redeclare them within a `:root`, `.theme-light`, or `.theme-dark` selector.
      * **Query 2:**
          * *QUERY RATIONALE:* "I'm searching for 'how to use Obsidian CSS snippets to change variables' to find practical, code-level examples for the user."
          * *EXPECTED INSIGHT:* "This will provide the exact syntax needed for the 'How to Use' section of the reference."
          * *FINDINGS SUMMARY:* This confirms the syntax. To create a snippet, you create a file like `my-snippet.css` in the `.obsidian/snippets/` folder. The content must be, for example:
            ```css
            :root {
              --font-text-size: 14px;
              --h1-color: red;
            }
            .theme-dark {
              --background-primary: #000;
            }
            ```
      * **Query 3:**
          * *QUERY RATIONALE:* "I'm searching for 'Obsidian CSS variable groups' or 'Obsidian theme CSS properties list' to understand the logical, non-alphabetical structure."
          * *EXPECTED INSIGHT:* "The variable names themselves (`--h1-`, `--code-`, `--tab-`, `--modal-`) imply a structure. This search will confirm those logical groupings."
          * *FINDINGS SUMMARY:* The prefixes are indeed the primary organizational key. I can confidently group the variables into:
              * Colors (Base, Semantic, Accents)
              * Typography (Headings, Body Text, Code)
              * Layout (Modals, Sidebars, Panes, Ribbon)
              * UI Components (Tabs, Checkboxes, Lists, Tables, Tags, Sliders, Toggles)
              * System (Layers, Cursors, Sizes)
      * **Query 4:**
          * *QUERY RATIONALE:* "I'm searching for 'Obsidian CSS --accent-h --accent-s --accent-l' to understand the core accent color system."
          * *EXPECTED INSIGHT:* "This will explain how Obsidian's primary accent color is built using HSL (Hue, Saturation, Lightness)."
          * *FINDINGS SUMMARY:* Confirmed. Obsidian uses HSL variables to *generate* other color variables (like `--interactive-accent`). This is a "base" variable system. Modifying `--accent-h` (hue) is the easiest way to change the entire feel of the UI.
      * **Query 5:**
          * *QUERY RATIONALE:* "I'm searching for 'Obsidian CSS --color-base-00 vs --background-primary' to understand the fundamental color philosophy."
          * *EXPECTED INSIGHT:* "This will clarify the relationship between the base palette (e.g., `--color-base-00`) and the semantic variables (e.g., `--background-primary`)."
          * *FINDINGS SUMMARY:* This is the most crucial insight. Obsidian defines a base palette (e.g., `--color-base-00` to `--color-base-100`). Then, "semantic" variables like `--background-primary` and `--text-normal` are *assigned* values from that base palette. This two-tiered system is the key to creating a theme and must be explained.

3.  **Knowledge Gap Analysis**:

      * *What aspects require deeper investigation?* The raw list provided is comprehensive. The "gap" is not in the *data* but in its *organization* and *explanation*. My task is to fill this gap.
      * *What conflicting information exists?* None. The system is well-defined.
      * *What cutting-edge developments need inclusion?* The list appears to be from the modern default theme. The most important "advanced" concept to include is the distinction between Base and Semantic variables.

### Phase 2: Structural Planning

STRUCTURAL REASONING:
├── **Core Concept Architecture**
│   ├── *Why this structure?* The user's input is an alphabetical list, which is useful as an index but terrible as a *reference*. To make it "highly accessible," the structure must be *semantic*, grouping variables by what they *do*. The most critical information (how to *use* them and the *philosophy* behind them) must come *before* the raw reference tables.
│   └── *Information flow logic:*
│        1.  **High-Level Intro:** What this document is.
│        2.  **Core Concepts (How-To):** An actionable, copy-pasteable guide on *how* to create a snippet to override these variables. This is the \#1 "needed" piece of information.
│        3.  **Core Philosophy (The "Why"):** Explain the Base vs. Semantic variable system. This is the \#1 "useful" piece of information for mastery.
│        4.  **The Reference Tables:** The user's list, completely reorganized by function (Colors, Typography, Layout, UI Components) and presented in tables with columns for `Variable`, `Default Value`, and `Description`.
│        5.  **Synthesis:** A final section on mental models for theming, as required by the prompt.
├── **Hierarchy Decisions**
│   ├── *Primary sections:*
│        1.  `How to Use This Reference`
│        2.  `1.0 ⚙️ Core Concepts: Using CSS Variables` (The "How")
│        3.  `2.0 💡 Core Philosophy: Base vs. Semantic Variables` (The "Why")
│        4.  `3.0 🎨 Color System Variables` (Grouped: Base Palette, Accents, Semantic)
│        5.  `4.0 🔡 Typography & Text Variables` (Grouped: Headings, Fonts, Code, Links)
│        6.  `5.0 🏛️ Layout & Sizing Variables` (Grouped: General, Modals, Sidebars, Panes)
│        7.  `6.0 🧩 UI Component Variables` (Grouped: Checkbox, Lists, Tables, Tabs, Tags, etc.)
│        8.  `7.0 ⚙️ Miscellaneous & System Variables` (Grouped: Layers, Cursors)
│        9.  `🎯 Synthesis & Mastery`
│        10. `📊 Metadata & Attribution`
│   └── *Subsection depth:* Each major reference section (3.0-7.0) will be further divided by component (e.g., `3.1 Base Color Palette`, `4.1 Headings`). This creates a highly granular and linkable Table of Contents.
└── **Cross-referencing Strategy**
    └── *Internal link opportunities:* Descriptions in the "Semantic" tables will link back to the "Base" variables they use (e.g., `Default: var(--color-base-00)`). The TOC will be the primary navigation. All variable names will be wrapped in `[[wiki-links]]` (or styled as code) for future PKB integration.

### Phase 3: Reference Note Construction

Here is the authoritative reference note, generated based on your list and the required structure.

-----



