---
title: 📚 Obsidian CSS Variable Reference
id: "20251106192326"
type: reference
source: gemini-2.5-pro
url: https://gemini.google.com/app/5f5bad28ac926ba7
tags:
  - obsidian/customization/snippets
aliases:
  - CSS Variable Reference
  - 📚Obsidian CSS Variable Reference
  - 📚Obsidian-CSS-Variable-Reference
  - 📚 Obsidian CSS Variable Reference
link-up:
  - "[[system-reference-hub_moc]]"
link-related:
  - "[[_snippet-css-variables-index]]"
date created: 2025-11-06T19:23:02
date modified: 2025-11-06T19:34:34
---

# 📚 OBSIDIAN CSS VARIABLE REFERENCE

This document provides a structured reference for the core CSS Custom Properties available in Obsidian. These variables allow for deep customization of the vault's appearance without needing to override complex selectors.

> [!tip] 💡 How to Use This Reference
> To use any of these variables, you must create a [[CSS Snippets|CSS snippet]] file (e.g., `my-theme.css`) and place it in your vault's `YourVault/.obsidian/snippets/` folder.
>
> Inside your snippet file, you must declare your overrides within the `:root` selector. This ensures your values take precedence over the default theme's values.
>
> ```css
> /* This is the correct way to override variables */
> :root {
>   /* Change the main font size */
>   --font-text-size: 18px;
>   
>   /* Change the accent color to a nice blue */
>   --accent-h: 210;
>   --accent-s: 80%;
>   --accent-l: 55%;
> }
> ```

-----

## 🎨 CORE THEME & COLOR PALETTE

This is the most fundamental group of variables. Changing these will have the largest and most immediate impact on your vault's appearance. They define the primary surfaces, text colors, and the main accent color used for interactive elements.

> [!info] Understanding Accent HSL
> The accent color is defined using `hsl()` (Hue, Saturation, Lightness). This is powerful because it allows you to easily create variations.
>
>   - `--accent-h`: The hue (a degree on the color wheel, 0-360). This is the "color" itself (e.g., red, green, blue).
>   - `--accent-s`: The saturation (percentage). This is the *intensity* of the color.
>   - `--accent-l`: The lightness (percentage). This is how light or dark the color is.

```css
:root {
  /* --- Base Accent Color (HSL) --- */
  --accent-h: 258;
  --accent-s: 88%;
  --accent-l: 66%;

  /* --- Primary Backgrounds --- */
  --background-primary: var(--color-base-00);
  --background-primary-alt: var(--color-base-10);
  --background-secondary: var(--color-base-20);
  --workspace-background-translucent: rgba(var(--mono-rgb-0), 0.6);

  /* --- Primary Text --- */
  --text-normal: var(--color-base-100);
  --text-muted: var(--color-base-70);
  --text-faint: var(--color-base-50);
  --text-on-accent: white;
  --text-on-accent-inverted: black;

  /* --- Interactive Colors (Derived from Accent) --- */
  --interactive-accent-hsl: var(--color-accent-hsl);
  --interactive-accent: var(--color-accent-1);
  --interactive-accent-hover: var(--color-accent-2);
  --text-accent: var(--color-accent);
  --text-accent-hover: var(--color-accent-2);
  
  /* --- Interactive Surfaces --- */
  --interactive-normal: var(--color-base-00);
  --interactive-hover: var(--color-base-10);

  /* --- Modifiers & Borders --- */
  --background-modifier-hover: rgba(var(--mono-rgb-100), 0.067);
  --background-modifier-active-hover: hsla(var(--interactive-accent-hsl), 0.1);
  --background-modifier-border: var(--color-base-30);
  --background-modifier-border-hover: var(--color-base-35);
  --background-modifier-border-focus: var(--color-base-40);
  --background-modifier-form-field: var(--color-base-00);
  --background-modifier-form-field-hover: var(--background-modifier-form-field);

  /* --- State/Feedback Colors --- */
  --background-modifier-error-rgb: var(--color-red-rgb);
  --background-modifier-error: var(--color-red);
  --background-modifier-error-hover: var(--color-red);
  --background-modifier-success-rgb: var(--color-green-rgb);
  --background-modifier-success: var(--color-green);
  --text-error: var(--color-red);
  --text-warning: var(--color-orange);
  --text-success: var(--color-green);

  /* --- Other Base Elements --- */
  --text-selection: hsla(var(--color-accent-hsl), 0.2);
  --text-highlight-bg-rgb: 255, 208, 0;
  --text-highlight-bg: rgba(var(--text-highlight-bg-rgb), 0.4);
  --background-modifier-message: rgba(0, 0, 0, 0.9);
}
```

-----

## ✒️ TYPOGRAPHY & TEXT

These variables control all aspects of text rendering, from the base font sizes for the UI and the editor to the specific styling for all six heading levels.

### BASE FONT PROPERTIES

Controls for general text, UI elements, and font weights.

```css
:root {
  /* --- UI Font Sizes --- */
  --font-ui-smaller: 12px;
  --font-ui-small: 13px;
  --font-ui-medium: 15px;
  --font-ui-large: 20px;

  /* --- Editor Font Sizes --- */
  --font-smallest: 0.8em;
  --font-smaller: 0.875em;
  --font-small: 0.933em;
  /* --font-text-size: 16px; */ /* (This is a base variable, not in your list but essential) */

  /* --- Font Weights --- */
  --font-weight: var(--font-normal);
  --font-thin: 100;
  --font-extralight: 200;
  --font-light: 300;
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  --font-extrabold: 800;
  --font-black: 900;
  
  /* --- Line & Paragraph Spacing --- */
  --line-height-normal: 1.5;
  --line-height-tight: 1.3;
  --p-spacing: 1rem;
  --p-spacing-empty: 0rem;

  /* --- Misc Text Styles --- */
  --italic-color: inherit;
  --italic-weight: inherit;
  --heading-spacing: calc(var(--p-spacing) * 2.5);
  --heading-formatting: var(--text-faint); /* Color of the markdown '#' symbols */
}
```

### HEADING (H1-H6) PROPERTIES

Controls for the color, font, size, weight, and style of each heading level.

```css
:root {
  /* --- H1 --- */
  --h1-color: inherit;
  --h1-font: inherit;
  --h1-line-height: 1.2;
  --h1-size: 1.802em;
  --h1-style: normal;
  --h1-variant: normal;
  --h1-weight: 700;

  /* --- H2 --- */
  --h2-color: inherit;
  --h2-font: inherit;
  --h2-line-height: 1.2;
  --h2-size: 1.602em;
  --h2-style: normal;
  --h2-variant: normal;
  --h2-weight: 600;

  /* --- H3 --- */
  --h3-color: inherit;
  --h3-font: inherit;
  --h3-line-height: 1.3;
  --h3-size: 1.424em;
  --h3-style: normal;
  --h3-variant: normal;
  --h3-weight: 600;

  /* --- H4 --- */
  --h4-color: inherit;
  --h4-font: inherit;
  --h4-line-height: 1.4;
  --h4-size: 1.266em;
  --h4-style: normal;
  --h4-variant: normal;
  --h4-weight: 600;

  /* --- H5 --- */
  --h5-color: inherit;
  --h5-font: inherit;
  --h5-line-height: var(--line-height-normal);
  --h5-size: 1.125em;
  --h5-style: normal;
  --h5-variant: normal;
  --h5-weight: 600;

  /* --- H6 --- */
  --h6-color: inherit;
  --h6-font: inherit;
  --h6-line-height: var(--line-height-normal);
  --h6-size: 1em;
  --h6-style: normal;
  --h6-variant: normal;
  --h6-weight: 600;
  
  /* --- Inline Title (Note Title in Pane) --- */
  --inline-title-color: var(--h1-color);
  --inline-title-font: var(--h1-font);
  --inline-title-line-height: var(--h1-line-height);
  --inline-title-size: var(--h1-size);
  --inline-title-style: var(--h1-style);
  --inline-title-variant: var(--h1-variant);
  --inline-title-weight: var(--h1-weight);
  --inline-title-margin-bottom: 0.5em;
}
```

-----

## ⚙️ CORE UI COMPONENTS

These are global variables for common [[Obsidian UI]] elements that appear across the entire application, such as icons, scrollbars, toggles, and form inputs.

```css
:root {
  /* --- Global Sizing & Radius --- */
  --radius-s: 4px;
  --radius-m: 8px;
  --radius-l: 12px;
  --radius-xl: 16px;
  --size-2-1: 2px;
  --size-2-2: 4px;
  --size-2-3: 6px;
  --size-4-1: 4px;
  --size-4-2: 8px;
  --size-4-3: 12px;
  --size-4-4: 16px;
  --size-4-5: 20px;
  --size-4-6: 24px;
  --size-4-8: 32px;
  --size-4-9: 36px;
  --size-4-10: 40px;
  --size-4-12: 48px;
  --size-4-16: 64px;
  --size-4-18: 72px;

  /* --- Icons --- */
  --icon-size: var(--icon-m);
  --icon-stroke: var(--icon-m-stroke-width);
  --icon-xs: 14px;
  --icon-s: 16px;
  --icon-m: 18px;
  --icon-l: 18px;
  --icon-xl: 32px;
  --icon-xs-stroke-width: 2px;
  --icon-s-stroke-width: 2px;
  --icon-m-stroke-width: 1.75px;
  --icon-l-stroke-width: 1.75px;
  --icon-xl-stroke-width: 1.25px;
  --icon-color: var(--text-muted);
  --icon-color-hover: var(--text-muted);
  --icon-color-active: var(--text-accent);
  --icon-color-focused: var(--text-normal);
  --icon-opacity: 0.85;
  --icon-opacity-hover: 1;
  --icon-opacity-active: 1;
  --clickable-icon-radius: var(--radius-s);
  --collapse-icon-color: var(--text-faint);
  --collapse-icon-color-collapsed: var(--text-accent);

  /* --- Scrollbars --- */
  --scrollbar-width: 12px;
  --scrollbar-height: 12px;
  --scrollbar-border-width: 3px 3px 3px 2px;
  --scrollbar-radius: var(--radius-l);
  --scrollbar-active-thumb-bg: rgba(var(--mono-rgb-100), 0.2);
  --scrollbar-bg: rgba(var(--mono-rgb-100), 0.05);
  --scrollbar-thumb-bg: rgba(var(--mono-rgb-100), 0.1);

  /* --- Toggles & Sliders (Settings) --- */
  --toggle-border-width: 2px;
  --toggle-width: 40px;
  --toggle-radius: 18px;
  --toggle-thumb-color: white;
  --toggle-thumb-radius: 18px;
  --toggle-thumb-height: 18px;
  --toggle-thumb-width: 18px;
  --toggle-s-border-width: 2px;
  --toggle-s-width: 34px;
  --toggle-s-thumb-height: 15px;
  --toggle-s-thumb-width: 15px;
  --slider-thumb-border-width: 1px;
  --slider-thumb-border-color: var(--background-modifier-border-hover);
  --slider-thumb-height: 18px;
  --slider-thumb-width: 18px;
  --slider-thumb-y: -6px;
  --slider-thumb-radius: 50%;
  --slider-s-thumb-size: 15px;
  --slider-s-thumb-position: -5px;
  --slider-track-background: var(--background-modifier-border);
  --slider-track-height: 3px;
  
  /* --- Input Fields (Settings, Search) --- */
  --input-height: 30px;
  --input-padding: var(--size-4-1) var(--size-4-2);
  --input-radius: 5px;
  --input-font-weight: var(--font-normal);
  --input-border-width: 1px;
  --input-border-width-focus: 2px;
  --input-placeholder-color: var(--text-faint);
  --input-date-separator: var(--text-faint);
  
  /* --- Dropdown Menus --- */
  --dropdown-background-blend-mode: hard-light;
  --dropdown-background-position: right 0.5em top 50%, 0 0;
  --dropdown-background-size: 1em auto, 100%;
  --dropdown-padding: 0 1.9em 0 0.8em;
  
  /* --- Color Swatches (e.g., in Graph settings) --- */
  --swatch-radius: 14px;
  --swatch-height: 22px;
  --swatch-width: 22px;
  --swatch-shadow: inset 0 0 0 1px rgba(var(--mono-rgb-100), 0.15);

  /* --- UI Layers (z-index) --- */
  --layer-cover: 5;
  --layer-sidedock: 10;
  --layer-status-bar: 15;
  --layer-popover: 30;
  --layer-slides: 45;
  --layer-modal: 50;
  --layer-notice: 60;
  --layer-menu: 65;
  --layer-tooltip: 70;
  --layer-dragged-item: 80;
  
  /* --- Cursors --- */
  --cursor: default;
  --cursor-link: pointer;
}
```

-----

## 📄 NOTE & EDITOR ELEMENTS

This group controls the appearance of Markdown elements *inside* a note, such as lists, links, code blocks, tables, and tags.

### CHECKBOXES & TASKS

```css
:root {
  --checkbox-radius: var(--radius-s);
  --checkbox-size: var(--font-text-size);
  --checkbox-marker-color: var(--background-primary);
  --checkbox-color: var(--interactive-accent);
  --checkbox-color-hover: var(--interactive-accent-hover);
  --checkbox-border-color: var(--text-faint);
  --checkbox-border-color-hover: var(--text-muted);
  --checkbox-margin-inline-start: 0.85em;
  --checklist-done-decoration: line-through;
  --checklist-done-color: var(--text-muted);
}
```

### CODE BLOCKS

```css
:root {
  --code-white-space: pre-wrap;
  --code-border-width: 0px;
  --code-border-color: var(--background-modifier-border);
  --code-bracket-background: var(--background-modifier-hover);
  --code-radius: var(--radius-s);
  --code-size: var(--font-smaller);
  --code-background: var(--background-primary-alt);
  
  /* --- Syntax Highlighting --- */
  --code-normal: var(--text-normal);
  --code-comment: var(--text-faint);
  --code-function: var(--color-yellow);
  --code-important: var(--color-orange);
  --code-keyword: var(--color-pink);
  --code-operator: var(--color-red);
  --code-property: var(--color-cyan);
  --code-punctuation: var(--text-muted);
  --code-string: var(--color-green);
  --code-tag: var(--color-red);
  --code-value: var(--color-purple);
}
```

### LINKS (INTERNAL & EXTERNAL)

```css
:root {
  /* --- General Link Style --- */
  --link-color: var(--text-accent);
  --link-color-hover: var(--text-accent-hover);
  --link-decoration: underline;
  --link-decoration-hover: underline;
  --link-decoration-thickness: auto;
  --link-weight: var(--font-weight);

  /* --- External Links --- */
  --link-external-color: var(--text-accent);
  --link-external-color-hover: var(--text-accent-hover);
  --link-external-decoration: underline;
  --link-external-decoration-hover: underline;
  --link-external-filter: none;

  /* --- Unresolved Links --- */
  --link-unresolved-color: var(--text-accent);
  --link-unresolved-opacity: 0.7;
  --link-unresolved-filter: none;
  --link-unresolved-decoration-style: solid;
  --link-unresolved-decoration-color: hsla(var(--interactive-accent-hsl), 0.3);
}
```

### LISTS (BULLETED & NUMBERED)

```css
:root {
  --list-indent: calc(var(--indent-unit) * var(--indent-size));
  --list-indent-editing: 0.75em;
  --list-indent-source: 0;
  --list-spacing: 0.075em;
  --list-marker-color: var(--text-faint);
  --list-marker-color-hover: var(--text-muted);
  --list-marker-color-collapsed: var(--text-accent);
  --list-bullet-border: none;
  --list-bullet-radius: 50%;
  --list-bullet-size: 0.3em;
  --list-bullet-transform: none;
  --list-numbered-style: decimal;
  --list-bullet-end-padding: 1.3rem;
  
  /* --- Indentation Guides --- */
  --indent-size: 4;
  --indent-unit: 0.5625em;
  --indentation-guide-width: 1px;
  --indentation-guide-width-active: 1px;
  --indentation-guide-color: rgba(var(--mono-rgb-100), 0.12);
  --indentation-guide-color-active: rgba(var(--mono-rgb-100), 0.3);
  --indentation-guide-editing-indent: 0.85em;
  --indentation-guide-reading-indent: -0.85em;
  --indentation-guide-source-indent: 0.25em;
}
```

### TABLES

```css
:root {
  --table-background: transparent;
  --table-border-width: 1px;
  --table-border-color: var(--background-modifier-border);
  --table-white-space: break-spaces;
  --table-header-background: var(--table-background);
  --table-header-background-hover: inherit;
  --table-header-border-width: var(--table-border-width);
  --table-header-border-color: var(--table-border-color);
  --table-header-font: inherit;
  --table-header-size: var(--table-text-size);
  --table-header-weight: calc(var(--font-weight) + var(--bold-modifier));
  --table-header-color: var(--text-normal);
  --table-line-height: var(--line-height-tight);
  --table-text-size: var(--font-text-size);
  --table-text-color: inherit;
  --table-column-min-width: 6ch;
  --table-column-max-width: none;
  --table-column-alt-background: var(--table-background);
  --table-column-first-border-width: var(--table-border-width);
  --table-column-last-border-width: var(--table-border-width);
  --table-row-background-hover: var(--table-background);
  --table-row-alt-background: var(--table-background);
  --table-row-alt-background-hover: var(--table-background);
  --table-row-last-border-width: var(--table-border-width);
  --table-selection: hsla(var(--color-accent-hsl), 0.1);
  --table-selection-blend-mode: var(--highlight-mix-blend-mode);
  --table-selection-border-color: var(--interactive-accent);
  --table-selection-border-width: 2px;
  --table-selection-border-radius: 4px;
  --table-cell-vertical-alignment: top;
  --table-drag-handle-background: transparent;
  --table-drag-handle-background-active: var(--table-selection-border-color);
  --table-drag-handle-color: var(--text-faint);
  --table-drag-handle-color-active: var(--text-on-accent);
  --table-drop-indicator-half-width: 2px;
  --table-add-button-background: transparent;
  --table-add-button-border-width: var(--table-border-width);
  --table-add-button-border-color: var(--background-modifier-border);
}
```

### TAGS & PILLS

Tags (e.g., `#mytag`) and Pills (UI elements used in Search, etc.) share similar styling.

```css
:root {
  /* --- Tags --- */
  --tag-size: var(--font-smaller);
  --tag-color: var(--text-accent);
  --tag-color-hover: var(--text-accent);
  --tag-decoration: none;
  --tag-decoration-hover: none;
  --tag-background: hsla(var(--interactive-accent-hsl), 0.1);
  --tag-background-hover: hsla(var(--interactive-accent-hsl), 0.2);
  --tag-border-color: hsla(var(--interactive-accent-hsl), 0.15);
  --tag-border-color-hover: hsla(var(--interactive-accent-hsl), 0.15);
  --tag-border-width: 0px;
  --tag-padding-x: 0.65em;
  --tag-padding-y: 0.25em;
  --tag-radius: 2em;
  --tag-weight: inherit;

  /* --- Pills (UI) --- */
  --pill-color: var(--text-muted);
  --pill-color-hover: var(--text-normal);
  --pill-color-remove: var(--text-faint);
  --pill-color-remove-hover: var(--text-accent);
  --pill-decoration: none;
  --pill-decoration-hover: none;
  --pill-background: transparent;
  --pill-background-hover: transparent;
  --pill-border-color: var(--background-modifier-border);
  --pill-border-color-hover: var(--background-modifier-border-hover);
  --pill-border-width: var(--border-width);
  --pill-padding-x: 0.65em;
  --pill-padding-y: 0.25em;
  --pill-radius: 2em;
  --pill-weight: inherit;
}
```

### EMBEDS, FOOTNOTES, & DIVIDERS

```css
:root {
  /* --- Embeds --- */
  --embed-max-height: 4000px;
  --embed-canvas-max-height: 400px;
  --embed-background: inherit;
  --embed-border-start: 2px solid var(--interactive-accent);
  --embed-border-end: none;
  --embed-border-top: none;
  --embed-border-bottom: none;
  --embed-padding: 0 0 0 var(--size-4-6);
  --embed-font-style: inherit;
  --embed-block-shadow-hover: 0 0 0 1px var(--background-modifier-border), inset 0 0 0 1px var(--background-modifier-border);

  /* --- Footnotes --- */
  --footnote-divider-color-active: var(--metadata-divider-color-focus);
  --footnote-divider-color: var(--metadata-divider-color);
  --footnote-divider-width: 1px;
  --footnote-gap: var(--size-4-1);
  --footnote-id-color-no-occurrences: var(--text-faint);
  --footnote-id-color: var(--text-muted);
  --footnote-id-delimiter: ".";
  --footnote-input-background-active: var(--metadata-input-background-active);
  --footnote-input-background: var(--metadata-input-background);
  --footnote-line-height: var(--line-height-normal);
  --footnote-padding-block: var(--size-2-3);
  --footnote-padding-inline: var(--size-2-3);
  --footnote-radius: var(--radius-s);
  --footnote-size: var(--font-smaller);

  /* --- Horizontal Rule (---) --- */
  --hr-color: var(--background-modifier-border);
  --hr-thickness: 2px;
}
```

### EDITOR & FILE PANE

These control the reading width and layout of the main note area.

```css
:root {
  --file-line-width: 700px; /* "Readable Line Length" */
  --file-folding-offset: 24px;
  --file-margins: var(--size-4-8);
  
  /* --- File Header (e.g., in stacked tabs) --- */
  --file-header-font: var(--font-interface);
  --file-header-font-size: var(--font-ui-small);
  --file-header-font-weight: 400;
  --file-header-border: var(--border-width) solid transparent;
  --file-header-justify: center;
}
```

-----

## 🏛️ APPLICATION LAYOUT & PANES

This group controls the main "chrome" of the Obsidian application: the sidebars, tabs, title bar, status bar, and other core layout components.

### TITLEBAR, RIBBON, & STATUS BAR

```css
:root {
  /* --- Window Titlebar --- */
  --titlebar-background: var(--background-secondary);
  --titlebar-background-focused: var(--background-secondary-alt);
  --titlebar-border-width: 0px;
  --titlebar-border-color: var(--background-modifier-border);
  --titlebar-text-color: var(--text-muted);
  --titlebar-text-color-focused: var(--text-normal);
  --titlebar-text-weight: var(--font-bold);
  --header-height: 40px; /* Also controls tab header height */

  /* --- Left Action Ribbon --- */
  --ribbon-background: var(--background-secondary);
  --ribbon-background-collapsed: var(--background-primary);
  --ribbon-width: 44px;
  --ribbon-padding: var(--size-4-2) var(--size-4-1) var(--size-4-3);
  
  /* --- Bottom Status Bar --- */
  --status-bar-background: var(--background-secondary);
  --status-bar-border-color: var(--divider-color);
  --status-bar-border-width: 1px 0 0 1px;
  --status-bar-font-size: var(--font-ui-smaller);
  --status-bar-text-color: var(--text-muted);
  --status-bar-position: fixed;
  --status-bar-radius: var(--radius-m) 0 0 0;
}
```

### TABS & PANE DIVIDERS

```css
:root {
  /* --- Tab Headers --- */
  --tab-background-active: var(--background-primary);
  --tab-text-color: var(--text-faint);
  --tab-text-color-active: var(--text-muted);
  --tab-text-color-focused: var(--text-muted);
  --tab-text-color-focused-active: var(--text-muted);
  --tab-text-color-focused-highlighted: var(--text-accent);
  --tab-text-color-focused-active-current: var(--text-normal);
  --tab-font-size: var(--font-ui-small);
  --tab-font-weight: inherit;
  --tab-container-background: var(--background-secondary);
  --tab-divider-color: var(--background-modifier-border-hover);
  --tab-outline-color: var(--divider-color);
  --tab-outline-width: 1px;
  --tab-curve: 6px;
  --tab-radius: var(--radius-s);
  --tab-radius-active: 6px 6px 0 0;
  --tab-width: 200px;
  --tab-max-width: 320px;
  
  /* --- Stacked Tabs --- */
  --tab-stacked-pane-width: 700px;
  --tab-stacked-header-width: var(--header-height);
  --tab-stacked-font-size: var(--font-ui-small);
  --tab-stacked-font-weight: 400;
  --tab-stacked-text-align: start;
  --tab-stacked-text-transform: rotate(0deg);
  --tab-stacked-text-writing-mode: vertical-lr;
  --tab-stacked-shadow: -8px 0 8px 0 rgba(0, 0, 0, 0.05);

  /* --- Tab Switcher (Ctrl+Tab) --- */
  --tab-switcher-menubar-background: var(--mobile-sidebar-background);
  --tab-switcher-background: var(--background-secondary);
  --tab-switcher-preview-radius: var(--radius-xl);
  --tab-switcher-preview-background-shadow: 0 4px 30px 2px rgba(0, 0, 0, 0.2);
  --tab-switcher-preview-shadow: 0 0 0 1px rgba(var(--mono-rgb-100), 0.05);
  --tab-switcher-preview-shadow-active: 0 0 0 2px var(--color-accent);
  
  /* --- Pane Dividers (Drag Handles) --- */
  --divider-color: var(--background-modifier-border);
  --divider-color-hover: var(--interactive-accent);
  --divider-width: 1px;
  --divider-width-hover: 3px;
  --divider-vertical-height: calc(100% - var(--header-height));
}
```

### SIDEBARS (FILE EXPLORER, OUTLINE, ETC.)

```css
:root {
  /* --- General --- */
  --sidebar-markdown-font-size: calc(var(--font-text-size) * 0.9);
  --sidebar-tab-text-display: none; /* Hides text for sidebar icons */

  /* --- Navigation (File Explorer) --- */
  --nav-item-size: var(--font-ui-small);
  --nav-item-color: var(--text-muted);
  --nav-item-color-hover: var(--text-normal);
  --nav-item-color-active: var(--text-normal);
  --nav-item-color-selected: var(--text-normal);
  --nav-item-color-highlighted: var(--text-accent);
  --nav-item-background-hover: var(--background-modifier-hover);
  --nav-item-background-active: var(--background-modifier-hover);
  --nav-item-background-selected: hsla(var(--color-accent-hsl), 0.15);
  --nav-item-padding: var(--size-4-1) var(--size-4-2) var(--size-4-1) var(--size-4-6);
  --nav-item-parent-padding: var(--nav-item-padding);
  --nav-item-children-padding-start: var(--size-2-2);
  --nav-item-children-margin-start: var(--size-4-3);
  --nav-item-weight: inherit;
  --nav-item-weight-hover: inherit;
  --nav-item-weight-active: inherit;
  --nav-item-white-space: pre;
  --nav-indentation-guide-width: var(--indentation-guide-width);
  --nav-indentation-guide-color: var(--indentation-guide-color);
  --nav-collapse-icon-color: var(--collapse-icon-color);
  --nav-collapse-icon-color-collapsed: var(--text-faint);
  --nav-heading-color: var(--text-normal);
  --nav-heading-color-hover: var(--text-normal);
  --nav-heading-color-collapsed: var(--text-faint);
  --nav-heading-color-collapsed-hover: var(--text-muted);
  --nav-heading-weight: var(--font-medium);
  --nav-heading-weight-hover: var(--font-medium);
  
  /* --- Vault Profile (Switcher) --- */
  --vault-profile-display: flex;
  --vault-profile-actions-display: flex;
  --vault-profile-font-size: var(--font-ui-small);
  --vault-profile-font-weight: var(--font-medium);
  --vault-profile-color: var(--text-normal);
  --vault-profile-color-hover: var(--vault-profile-color);
}
```

### GRAPH VIEW

```css
:root {
  --graph-controls-width: 240px;
  --graph-text: var(--text-normal);
  --graph-line: var(--color-base-35, var(--background-modifier-border-focus));
  --graph-node: var(--text-muted);
  --graph-node-unresolved: var(--text-faint);
  --graph-node-focused: var(--text-accent);
  --graph-node-tag: var(--color-green);
  --graph-node-attachment: var(--color-yellow);
}
```

-----

## 🚦 MODALS, POPOVERS, & MENUS

This group controls all "floating" UI elements that appear over the main workspace, such as dialog boxes, the command palette, context menus, and note hover previews.

```css
:root {
  /* --- Modals (e.g., Settings, Plugins) --- */
  --modal-background: var(--background-primary);
  --modal-width: 90vw;
  --modal-height: 85vh;
  --modal-max-width: 1100px;
  --modal-max-height: 1000px;
  --modal-max-width-narrow: 800px;
  --modal-border-width: var(--border-width);
  --modal-border-color: var(--color-base-40, var(--background-modifier-border-focus));
  --modal-radius: var(--radius-l);
  --modal-community-sidebar-width: 280px;

  /* --- Dialogs (Smaller Modals) --- */
  --dialog-width: 560px;
  --dialog-max-width: 80vw;
  --dialog-max-height: 85vh;
  
  /* --- Prompts (Command Palette, Quick Switcher) --- */
  --prompt-input-height: 40px;
  --prompt-width: 700px;
  --prompt-max-width: 80vw;
  --prompt-max-height: 70vh;
  --prompt-border-width: var(--border-width);
  --prompt-border-color: var(--color-base-40, var(--background-modifier-border-focus));

  /* --- Hover Popovers (Note Preview) --- */
  --popover-width: 450px;
  --popover-height: 400px;
  --popover-max-height: 95vh;
  --popover-pdf-width: 450px;
  --popover-pdf-height: 400px;
  --popover-font-size: var(--font-text-size);
  
  /* --- Context Menus (Right-click) --- */
  --menu-padding: var(--size-2-3);
  --menu-shadow: var(--shadow-s);
  --menu-radius: var(--radius-m);
  --menu-background: var(--background-secondary);
  --menu-border-color: var(--background-modifier-border-hover);
  --menu-border-width: 1px;
  --menu-backdrop-filter: none;
  
  /* --- Search --- */
  --search-clear-button-color: var(--text-muted);
  --search-clear-button-size: 13px;
  --search-icon-color: var(--text-muted);
  --search-icon-size: 18px;
  --search-result-background: var(--background-primary);
  
  /* --- Misc --- */
  --drag-ghost-background: rgba(0, 0, 0, 0.85);
  --drag-ghost-text-color: #fff;
  --flair-background: var(--interactive-normal);
  --flair-color: var(--text-normal);
}
```

-----

## 🧩 SPECIALIZED COMPONENTS

These variables control specific, discrete features like the Properties (frontmatter) editor and the built-in PDF viewer.

### PROPERTIES (METADATA)

```css
:root {
  --metadata-background: transparent;
  --metadata-display-reading: block;
  --metadata-display-editing: block;
  --metadata-max-width: none;
  --metadata-padding: var(--size-4-2) 0;
  --metadata-border-color: var(--background-modifier-border);
  --metadata-border-radius: 0;
  --metadata-border-width: 0;
  --metadata-divider-color: var(--background-modifier-border);
  --metadata-divider-color-hover: transparent;
  --metadata-divider-color-focus: transparent;
  --metadata-divider-width: 0;
  --metadata-gap: 3px;
  --metadata-property-padding: 0;
  --metadata-property-radius: 6px;
  --metadata-property-radius-hover: 6px;
  --metadata-property-radius-focus: 6px;
  --metadata-property-background: transparent;
  --metadata-property-background-hover: transparent;
  --metadata-property-background-active: var(--background-modifier-hover);
  --metadata-property-box-shadow-hover: 0 0 0 1px var(--background-modifier-border-hover);
  --metadata-property-box-shadow-focus: 0 0 0 2px var(--background-modifier-border-focus);
  --metadata-label-background: transparent;
  --metadata-label-background-hover: transparent;
  --metadata-label-background-active: var(--background-modifier-hover);
  --metadata-label-font: var(--font-interface);
  --metadata-label-font-size: var(--font-smaller);
  --metadata-label-font-weight: inherit;
  --metadata-label-text-color: var(--text-muted);
  --metadata-label-text-color-hover: var(--text-muted);
  --metadata-label-width: 9em;
  --metadata-input-height: calc(var(--font-text-size) * 1.75);
  --metadata-input-text-color: var(--text-normal);
  --metadata-input-font: var(--font-interface);
  --metadata-input-font-size: var(--font-smaller);
  --metadata-input-background: transparent;
  --metadata-input-background-hover: transparent;
  --metadata-input-background-active: var(--background-modifier-hover);
  --metadata-input-longtext-lines: 3;
  --metadata-sidebar-label-font-size: var(--font-ui-small);
  --metadata-sidebar-input-font-size: var(--font-ui-small);
}
```

### PDF VIEWER

```css
:root {
  --pdf-background: var(--background-primary);
  --pdf-page-background: var(--background-primary);
  --pdf-shadow: 0 0 0 1px rgba(0, 0, 0, 0.05), 0 2px 8px rgba(0, 0, 0, 0.1);
  --pdf-spread-shadow: 0 0 0 1px rgba(0, 0, 0, 0.05);
  --pdf-sidebar-background: var(--background-primary);
  --pdf-thumbnail-shadow: 0 0 0 1px rgba(0, 0, 0, 0.15), 0 2px 8px rgba(0, 0, 0, 0.2);
}
```

### SYNC

```css
:root {
  --sync-avatar-color-current-user: transparent;
  --sync-avatar-color-1: var(--color-red);
  --sync-avatar-color-2: var(--color-orange);
  --sync-avatar-color-3: var(--color-yellow);
  --sync-avatar-color-4: var(--color-green);
  --sync-avatar-color-5: var(--color-cyan);
  --sync-avatar-color-6: var(--color-blue);
  --sync-avatar-color-7: var(--color-purple);
  --sync-avatar-color-8: var(--color-pink);
}
```

-----

### 🔗 RELATED TOPICS FOR PKB EXPANSION

  - [[Obsidian Theming]]
      - The high-level practice of creating and applying themes and snippets in Obsidian.
  - [[CSS Selectors for Obsidian]]
      - A necessary companion to this reference. While variables change *properties*, selectors are needed to target *which* elements to change. This includes knowing selectors like `.view-header`, `.cm-s-obsidian`, `.nav-file-title`, etc.
  - [[CSS Custom Properties]]
      - The underlying W3C web standard that makes these variables possible. Understanding their cascading and fallback behavior is key to advanced snippet creation.
