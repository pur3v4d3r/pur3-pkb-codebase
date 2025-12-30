---
title: "Condensed Reference: Custom Callout's"
id: 20251116012546
type: reference
tags:
  - year/2025
  - obsidian/customization/css
aliases:
  - Callout CSS Reference
  - Obsidian Callout Styling
  - Callout Customization Guide
  - Callout Customization
  - Callout CSS Taxonomy
  - Obsidian Callout Modification
  - Obsidian Callout CSS
  - Style Settings for Callouts
  - CSS Snippet Reference
  - Callout Theme System
  - Modular Callout System
  - Swappable CSS Snippets
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

> [!abstract]
> This reference note provides an exhaustive taxonomy of all [[CSS]] customization options, syntax patterns, and modification techniques for [[obsidian]] callouts. It covers native callout features, [[CSS Variables]], [[CSS Selectors]], pseudo-elements, [[Style Settings Plugin]] integration, and advanced styling techniques. This serves as a complete foundational resource for custom callout visualization development.

# Callout Customization Reference Note


## Callout Anatomy & Core Structure
---
---
### HTML Structure Breakdown

> [!the-purpose]
> This example is of an actual Callout and how it looks on the HTML side, if you inspect it closely you see exactly how it looks in the final viewable version in Obsidian.
```c
<div class="callout" data-callout="type-name">
  <div class="callout-title">
    <div class="callout-icon">
      <svg class="svg-icon lucide-icon">…</svg>
    </div>
    <div class="callout-title-inner">Title Text</div>
    <div class="callout-fold"><!-- fold indicator --></div>
  </div>
  <div class="callout-content">
    <!-- Content goes here -->
  </div>
</div>
```

**Key Structural Elements:**
- `.callout` - The outermost container (root element)
- `.callout-title` - The header section containing icon and title
- `.callout-icon` - Container for the SVG icon
- `.callout-title-inner` - The actual title text wrapper
- `.callout-fold` - Collapse/expand indicator (when foldable)
- `.callout-content` - The body content container

---

## Callout Syntax & Features

### Foldable Callouts
**Syntax:**
```c
> [!info]+ Expanded by Default
> Content is visible

> [!warning]Collapsed by Default
> Content is hidden initially
```
### Nested Callouts
```c
> [!question] Outer Callout
> > [!answer] Nested Callout
> > Content in nested callout
> > 
> > > [!example] Triple Nested
> > > Deep nesting is supported
```
### Metadata/Inline Modifiers

Advanced users can create on-the-fly customizations using metadata syntax with the pipe character to modify colors and icons without editing CSS files.

**Syntax Pattern:**
```c
> [!callout-type|modifier]
```

---
---

## Selector Reference


### Essential CSS Variables

| *Variable*                  | *Description*                | *Value Format*                   | *Example*          |
| --------------------------- | ---------------------------- | -------------------------------- | ------------------ |
| `--callout-color`           | Main accent color (RGB only) | `R, G, B` (0-255)                | `255, 121, 198`    |
| `--callout-icon`            | Icon identifier or SVG       | `lucide-icon-name` or SVG string | `lucide-lightbulb` |
| `--callout-title-color`     | Title text color override    | RGB format                       | `255, 0, 0`        |
| `--callout-border-width`    | Border thickness             | CSS length unit                  | `2px`              |
| `--callout-border-opacity`  | Border transparency          | `0` to `1`                       | `0.5`              |
| `--callout-title-padding`   | Title area spacing           | CSS spacing                      | `12px 16px`        |
| `--callout-content-padding` | Content area spacing         | CSS spacing                      | `16px`             |
| `--callout-title-size`      | Title font size              | CSS font size                    | `1em`              |
| `--callout-fold-size`       | Fold indicator size          | CSS size                         | `18px`             |
| `--callout-radius`          | Corner roundness             | CSS border-radius                | `var(--radius-s)`  |
|                             |                              |                                  |                    |

| Selector Target             | CSS Selector Syntax                                  | Usage Example                                                                                                   |
| --------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **All Callouts**            | `.callout`                                           | `/* Affects every single callout */` <br> `.callout { border-radius: 10px; }`                                   |
| **A Specific Callout Type** | `.callout[data-callout="type"]`                      | `/* Only affects [!project] callouts */` <br> `.callout[data-callout="project"] { … }`                          |
| The **Title Bar**           | `.callout[data-callout="type"] .callout-title`       | `/* Targets the title bar of [!project] */` <br> `.callout[data-callout="project"] .callout-title { … }`        |
| The **Icon**                | `.callout[data-callout="type"] .callout-icon`        | `/* Targets the icon container of [!project] */` <br> `.callout[data-callout="project"] .callout-icon { … }`    |
| The **Title Text**          | `.callout[data-callout="type"] .callout-title-inner` | `/* Targets the title text of [!project] */` <br> `.callout[data-callout="project"] .callout-title-inner { … }` |
| The **Content Area**        | `.callout[data-callout="type"] .callout-content`     | `/* Targets the content area of [!project] */` <br> `.callout[data-callout="project"] .callout-content { … }`   |
| The **Fold Arrow**          | `.callout[data-callout="type"] .callout-fold`        | `/* Targets the fold icon of [!project] */` <br> `.callout[data-callout="project"] .callout-fold { … }`         |

-----

## Customization

> [!the-purpose]
> This section provides a complete reference of CSS variables and properties,
> > [!methodology-and-sources]
> > **Framework**
> > The following example will target a  `[!project]` callout.
> >
> > **CSS Snippet Structure:**
> >
> > ```css
> > /* Always define your variables inside the selector */
> > .callout[data-callout="project"] {
> >   /* --variable-name: value; */
> > }
> > ```
> 

### Icon Customization

| **Method**                  | **Property / Variable**           | **Example Value**             | **Notes**                                                                       |
| --------------------------- | --------------------------------- | ----------------------------- | ------------------------------------------------------------------------------- |
| *Change Lucide Icon*        | `--callout-icon`                  | `lucide-briefcase`            | This is the simplest method. Uses any name from the [[Lucide]] icon set.        |
| *Use Emoji* (Method A)      | `content` (via `::before`)        | `'💼'`                        | Requires hiding the default icon. See example below.                            |
| *Use Custom SVG* (Method B) | `mask-image` / `background-image` | `url('data:image/svg+xml;…')` | Provides full control. Often uses a base64-encoded SVG.                         |
| *Use Iconize Plugin*        | `none` (set in UI)                | `fas-rocket`                  | Use the [[Callout Manager]] plugin to set an [[Iconize]] shortcode as the icon. |
#### **Example (Changing Lucide Icon):**
```css
.callout[data-callout="project"] {
  --callout-icon: lucide-briefcase;
}
```
#### **Example (Using Emoji Icon):**
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

### Title & Header Customization

| **Target**        | **Property / Variable** | **Example Value**     | **Notes**                      |
| ----------------- | ----------------------- | --------------------- | ------------------------------ |
| Title Text Color  | `color`                 | `#FFFFFF`             | Targets `.callout-title-inner` |
| Title Background  | `background-color`      | `var(--color-accent)` | Targets `.callout-title`       |
| Title Font        | `font-family`           | `"Georgia", serif`    | Targets `.callout-title-inner` |
| Title Font Size   | `font-size`             | `1.5em`               | Targets `.callout-title-inner` |
| Title Font Weight | `font-weight`           | `700`                 | Targets `.callout-title-inner` |
| Title Alignment   | `text-align`            | `center`              | Targets `.callout-title-inner` |

### Border, Background, & Shadow

> [!important] 
> 
> These properties are typically set on the main `.callout[data-callout="project"]` selector.
> 

| Target          | Property / Variable      | Example Value                     | Notes                                                                                             |
| --------------- | ------------------------ | --------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Main Color**  | `--callout-color`        | `255, 0, 0`                       | **Crucial variable.** Expects an `R, G, B` triplet. Controls border and default title background. |
| Border Width    | `--callout-border-width` | `3px 0 0 3px`                     | `top right bottom left`. Use `0 0 0 5px` for just a left border.                                  |
| Border Style    | `border-style`           | `dashed`                          |                                                                                                   |
| Border Radius   | `border-radius`          | `10px`                            | Controls rounding of the corners.                                                                 |
| Main Background | `background-color`       | `rgba(var(--callout-color), 0.1)` | Use `rgba` with the `--callout-color` variable for a transparent background.                      |
| Box Shadow      | `box-shadow`             | `5px 5px 15px rgba(0,0,0,0.2)`    | Adds a drop shadow.                                                                               |

### Content Area Customization

> [!important] 
> 
> These properties are set on the `.callout[data-callout="project"] .callout-content` selector.
> 

| Target             | Property / Variable | Example Value | Notes                                           |
| ------------------ | ------------------- | ------------- | ----------------------------------------------- |
| Content Padding    | `--callout-padding` | `20px`        | Controls inner padding of the *entire* callout. |
| Content Background | `background-color`  | `#FAFAFA`     | Sets background for *just* the content area.    |
| Content Text Color | `color`             | `#333333`     |                                                 |
| Content Font Size  | `font-size`         | `0.9em`       |                                                 |

---

## Style Settings Plugin

> [!important]
> ### Foundational
> To make your callout customizable via [[Style Settings]], you must:
> 
> 1.  Define your callout styles using CSS variables (e.g., `--project-color`).
> 2.  Use those variables in your callout CSS.
> 3.  Add special `/* @settings … */` comments *before* the variable definitions in your `:root` block.
> 
> > [!central-principle]
> > **Central Principle**
> > Style Settings does **not** write CSS for you. It only provides a UI to change the *value* of CSS variables you have already defined and used.
> 

> [!methodology-and-sources]
>### Style Settings Syntax Reference
>
>You must place this block at the **top** of your CSS snippet file.
>
> | **Annotation**                                   | **Description**                                                    |
> | -------------------------------------------- | -------------------------------------------------------------- |
> | `/* @settings-group: [GroupName] */`         | Creates a new collapsible section in Style Settings.           |
> | `/* @settings-name: "[Setting Name]" */`     | The human-readable name for the setting.                       |
> | `/* @settings-description: "[Help Text]" */` | Explanatory text that appears below the setting.               |
> | `/* @settings-type: [type] */`               | Specifies the UI control. `color`, `text`, `slider`, `toggle`. |
> | `/* @settings-color-format: [format] */`     | `rgb` or `hex`. Use `rgb` for `--callout-color`.               |
> | `/* @settings-slider-min: [value] */`        | Minimum value for a `slider`.                                  |
> | `/* @settings-slider-max: [value] */`        | Maximum value for a `slider`.                                  |
> | `/* @settings-slider-step: [value] */`       | Increment value for a `slider`.                                |
>

> [!example]
>### Practical Example: Style Settings Callout
>
>Here is a *complete* snippet file that creates a `[!project]` callout fully controllable by Style Settings. **Use this as guidance when constructing your Callouts.**
>
> ```css
> /*
> This is the CSS snippet file (e.g., MyCallouts.css)
> */
> 
> /* == STYLE SETTINGS DEFINITIONS == */
> /* This block defines the UI in the plugin */
> :root {
>   /* @settings-group: Project Callout */
>   /* @settings-name: "Project Color" */
>   /* @settings-description: "Sets the main color for the project callout." */
>   /* @settings-type: color */
>   /* @settings-color-format: rgb */
>   --project-color: 139, 92, 246; /* Default: purple */
> 
>   /* @settings-name: "Project Icon" */
>   /* @settings-description: "Name of the Lucide icon to use." */
>   /* @settings-type: text */
>   --project-icon: lucide-briefcase; /* Default icon */
> 
>   /* @settings-name: "Project Title Font Size" */
>   /* @settings-description: "Font size for the callout title (e.g., 1.2em)." */
>   /* @settings-type: text */
>   --project-title-size: 1.2em;
> 
>   /* @settings-name: "Enable Title Uppercase" */
>   /* @settings-description: "Toggles the title text to uppercase." */
>   /* @settings-type: toggle */
>   --project-title-uppercase: 0; /* 0 = off, 1 = on */
> }
> 
> /* == CSS RULESET == */
> /* This block *uses* the variables defined above */
> 
> .callout[data-callout="project"] {
>   /* Use the variables from :root. 
>     The 'var()' function includes a fallback value 
>     just in case Style Settings fails.
>   */
>   --callout-color: var(--project-color, 139, 92, 246);
>   --callout-icon: var(--project-icon, lucide-briefcase);
> }
> 
> .callout[data-callout="project"] .callout-title-inner {
>   font-size: var(--project-title-size, 1.2em);
>   
>   /* Use a 'hack' to apply the toggle */
>   text-transform: if(var(--project-title-uppercase) = 1, uppercase, none);
> }
> ```
>





## Advanced Techniques & States

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






## Synthesis & Examples
> [!use-cases-and-examples]
> **Real-World Applications

### "Matrix" Code Block Callout `[!matrix]`

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

### "Sealed" Spoilers Callout `[!sealed]`

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




## Exploration and Developing Understanding

### Cognitive Models

Think of a callout as a small "house" you are building inside your note.

  * `.callout`: The plot of land and the foundation.
  * `.callout[data-callout="…"]`: The *specific address* of the house.
  * `--callout-color`: The primary paint color for the trim and mailbox.
  * `.callout-title`: The front door and porch.
  * `.callout-icon`: The house number or door knocker.
  * `.callout-content`: The rooms inside the house.
  * `Style Settings`: The remote control that lets you change the paint color, porch light, and indoor lighting without having to rebuild.

### Comparative Analysis: Icon Methods

| Approach                | Strengths                           | Weaknesses                                                       | Use When                                               |
| ----------------------- | ----------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------ |
| **`--callout-icon`**    | Easiest, theme-compatible.          | Limited to Lucide icon set.                                      | You just need a different standard icon.               |
| **Emoji (`::before`)**  | Quick, universal, colorful.         | Can be hard to align perfectly. May not match theme aesthetic.   | You want a quick, visually distinct icon.              |
| **Custom SVG**          | Total control. Any icon, any color. | Complex. Requires base64 encoding or file paths. Can be brittle. | You have a specific brand or icon set you *must* use.  |
| **[[Callout Manager]]** | UI-driven, easy.                    | Adds a plugin dependency.                                        | You want to manage many callouts without writing code. |

























































































