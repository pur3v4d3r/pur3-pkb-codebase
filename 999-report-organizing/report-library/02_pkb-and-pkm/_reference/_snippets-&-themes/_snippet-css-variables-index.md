---
title: "List of CSS Variables"
id: "20251106192739"
type: "reference"
source: "pur3v4d3r"
tags:
  - "obsidian/customization/snippets"
aliases:
  - List of CSS Variables
  - List-of-CSS-Variables
link-up:
  - "[[system-reference-hub_moc]]"
link-related:
  - "[[reference-comprehensive-css-variable-2025110619]]"
date created: 2025-11-06T19:02:52
date modified: 2025-11-06T19:27:19
---

```
/*================================*\
 |     Snippets for Obsidian      |
 |       by Pur3v4d3r             |  
 | -------------------------------|
\*================================*/
```


```
snippets/
├── 01-variables.css          # Custom CSS variables
├── 02-typography.css         # Font and text styles
├── 03-colors.css            # Color overrides
├── 10-layout.css            # Spacing and structure
├── 20-editor.css            # Editor-specific
├── 30-sidebar.css           # Sidebar styling
├── 40-plugins.css           # Plugin customization
├── 50-responsive.css        # Media queries
└── 99-experimental.css      # Testing area
```


Important and Working Animation
```
linear-gradient(190deg,
    #7800F4,
    #FFC700,
    #72FFF1,
    #7800F4
  )!important;;;
  background-size: 400% 100%;
  animation: shimmer linear infinite;
  animation-timing-function: cubic-bezier(0.075, 0.82, 0.165, 100);

  opacity: 0.25;
}
```


```
background-image: linear-gradient(
    to right, 
    var(--theme-purple, #9E6AD3), 
    var(--theme-gold, #FFC700), 
    var(--theme-teal, #2DD4BF)
  ) !important;
```


# Active Snippet Index

Here is the comprehensive reorganization of your CSS snippets, categorized into your specified files and formatted according to your exact structural and commenting standards.

Each snippet is presented as an individual, "copy-and-paste-ready" block.

-----

## Snippet: 01-variables.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 01-variables.css
 * Central hub for all custom CSS variables used across snippets.
 * This allows for easy theme-wide changes from one file.
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: CUSTOM VARIABLE DEFINITIONS
   ======================================== */

:root {
  /* * NOTE: No custom variables were found in the provided snippets.
   * This section is ready for you to add your own.
   *
   * Example:
   * --pkb-purple: #9E6AD3;
   * --pkb-gold: #FFC700;
   * --pkb-teal: #2DD4BF;
   */
}
```

-----

## Snippet: 02-typography.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 02-typography.css
 * Controls all typography, including fonts, text styles, 
 * math rendering, and list appearances.
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: BASE TYPOGRAPHY
   ======================================== */

/* --- Improve text rendering engine --- */
.markdown-preview-view,
.markdown-source-view {
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* --- Adjust global letter spacing for clarity --- */
body {
  letter-spacing: 0.01em;
}

/* ========================================
   SECTION 2: LAYOUT & READABILITY
   ======================================== */

/* --- Set Optimal Reading Line Length --- */
/*
 * Sets the max line width in preview and edit mode
 * to 85 characters (`85ch`) for improved readability.
 */
.markdown-source-view.mod-cm6 .cm-sizer,
.markdown-preview-view .markdown-preview-sizer {
  max-width: 85ch;
  margin-left: auto;
  margin-right: auto;
}

/* ========================================
   SECTION 3: LIST STYLING
   ======================================== */

/* --- Faded/Grayscale Emoji in Completed Tasks --- */
/*
 * This section styles completed tasks. It adds a subtle
 * grayscale filter and a faint background overlay to
 * visually differentiate them.
 */

/* Indent task list text to align */
ul > li.task-list-item p {
  text-indent: -1.5em;
}

/* Prepare checked item for overlay */
ul > li.task-list-item.is-checked {
  position: relative;
}

/* * Add subtle gold overlay and grayscale backdrop-filter 
 * to completed tasks.
 */
ul > li.task-list-item.is-checked::after {
  content: "";
  position: absolute;
  display: inline-block;
  -webkit-backdrop-filter: grayscale();
  backdrop-filter: grayscale();
  /* * NOTE: backdrop-filter can impact rendering performance.
   * filter: grayscale(); is a less performant alternative
   * if applied directly to the text.
   */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 199, 0, 0.15); /* subtle gold overlay */
  pointer-events: none; /* Allow clicks to pass through */
}

/* --- Nested Ordered List Counters (e.g., 1.1, 1.2.3) --- */
ol {
  counter-reset: item; /* Reset counter for top-level <ol> */
}

ol li {
  display: block;
}

ol li:before {
  content: counters(item, ".") ". "; /* Display nested count */
  counter-increment: item; /* Increment counter for this <li> */
  padding-right: 5px;
}

/* --- Unordered List Bullet to Dash/Arrow Converter --- */
/*
 * Converts standard list bullets (•) into a styled
 * arrow (->) for both Live Preview and Reading Mode.
 */
:is(.cm-formatting-list-ul, .markdown-rendered ul > li) > .list-bullet::after {
  /* 1. Remove the default bullet style */
  border: none !important;
  background-color: transparent !important;
  
  /* 2. Set new content and color */
  content: "->" !important;
  color: #7800F4 !important; /* Vibrant Purple */
  
  /* 3. Adjust sizing and alignment */
  font-size: 1.2em; /* Make the arrow slightly larger */
  vertical-align: middle;
  display: inline-block;
  
  /* 4. Adjust spacing */
  /* * NOTE: The multiple 'margin' properties were redundant.
   * Consolidated into padding and margin for clarity.
   */
  padding-right: 0.2em; 
  margin-right: 0.5em;
  margin-bottom: 0.1em; /* Slight adjustment for vertical alignment */
}

/* ========================================
   SECTION 4: MATH & LATEX STYLING
   ======================================== */

/* --- Robust Inline Math Fix (Reading & Live Preview) --- */
/* * Targets KaTeX/MathJax wrappers to resize inline math
 * without breaking line height.
 */
.markdown-rendered .math.math-inline .katex,
.markdown-rendered .math.math-inline mjx-container,
.markdown-source-view.mod-cm6 .cm-math,
.markdown-source-view.mod-cm6 .cm-math .katex {
  /* Set desired size (110% of base text) */
  font-size: calc(1.1 * var(--font-text-size)) !important;
  
  /* Crucial: Prevent large font from blowing up line spacing */
  line-height: 1.0 !important;
  vertical-align: middle !important;
}

/* --- Fallback for base rendering element in reading mode --- */
.markdown-rendered .katex {
  font-size: 1.1em !important;
}

/* --- Block Math ($$ … $$) Sizing --- */
/* * Ensures block-level math is significantly larger
 * for readability.
 */
.markdown-rendered mjx-container[display="true"],
.markdown-source-view.mod-cm6 .cm-content mjx-container[display="true"] {
  font-size: calc(2.75 * var(--font-text-size)) !important;
  line-height: 1.5 !important;
}
```

-----

## Snippet: 03-colors.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 03-colors.css
 * Manages custom color overrides and gradient definitions
 * for UI elements like horizontal rules.
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: UI ELEMENT COLORS
   ======================================== */

/* --- Gradient Horizontal Rules <hr> --- */
/*
 * Replaces the default <hr> line with an elegant,
 * fading purple gradient.
 */
hr {
  height: 2px;
  border: none; /* Remove the default border */
  background: linear-gradient(
    to right,
    transparent, /* Start with transparency */
    #7800F4, /* Primary accent purple in the center */
    transparent /* End with transparency */
  );
  margin-top: 2.5em; /* Add vertical space */
  margin-bottom: 2.5em;
}
```

-----

## Snippet: 10-layout.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 10-layout.css
 * Controls major layout components like modals, callouts,
 * scrollbars, and core UI animations.
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: METADATA CONTAINER
   ======================================== */

/* --- Style the main container for properties --- */
.metadata-container {
  background-color: #9E6AD34D; /* Translucent Purple */
  border: 1px solid #FFC700; /* Gold border */
  border-radius: 8px;
  padding: 12px 18px;
  margin-bottom: 32px; /* Space before content begins */
}

/* --- Add a "Metadata-by-Pur3v4d3r" label --- */
/* * NOTE: The original file had two different rules for this.
 * This rule merges them for both Live Preview and Reading Mode.
 */
.cm-content .metadata-container::before,
.markdown-preview-view .metadata-container::before {
  content: 'Metadata-by-Pur3v4d3r' !important;
  font-size: 0.7em !important;
  font-weight: bold !important;
  letter-spacing: 0.1em !important;
  color: #FFC700 !important; /* Amber Gold */
  display: block !important;
  margin-bottom: 12px !important;
}

/* ========================================
   SECTION 2: MODALS & COMMAND PALETTE
   ======================================== */

/* --- Command Palette Styling --- */
.prompt {
  border: #7800F4;
  opacity: 0.9;
}

.suggestion-highlight {
  text-decoration: none;
  color: var(--text-accent);
}

.suggestion-item.is-selected {
  border: solid var(--text-accent);
  border-radius: 14px;
}

.suggestion-hotkey {
  background-color: #7800F4;
  color: #FFC700;
  border-radius: 10px;
  font-weight: 500;
}

.prompt-instruction {
  font-weight: 500;
}

.prompt-instruction-command {
  background-color: rgba(250, 252, 255, 0.5);
  color: black;
  border-radius: 10px;
  padding: 0 3px 0 3px;
}

/* --- Translucent Modals & Menus --- */
/*
 * Modifies modal, command palette (omnibar), and other
 * pop-ups to have a blurred, translucent background.
 */
input.prompt-input,
input.prompt-input:active,
input.prompt-input:focus {
  border-radius: 3px;
  border: 2px solid rgba(38, 38, 59, 0.5);
  background-color: transparent;
  box-sizing: border-box;
  border-collapse: collapse;
}

/* Make legible background for menus */
div.popover.hover-popover,
.menu,
.suggestion-container {
  background-color: #FFFFFF01; /* Near transparent white */
  backdrop-filter: blur(30px);
  border: none;
}

/* ========================================
   SECTION 3: CORE UI ELEMENTS
   ======================================== */

/* --- Gradient Underline for Active Tab --- */
/*
 * Applies your 3-color gradient as an underline
 * to the currently active tab.
 */
body .workspace-tab-header.is-active {
  background-image: linear-gradient(
    to right,
    var(--ui2), /* Native Purple */
    var(--ax1), /* Native Gold */
    var(--icon-color) /* Native Teal */
  ) !important;
  
  background-position: 0 100% !important;
  background-size: 100% 2px !important;
  background-repeat: no-repeat !important;
  border-bottom: none !important;
  box-shadow: none !important;
}

/* --- Accent Scrollbar (Gold to Purple Gradient) --- */
/*
 * Scrollbar is subtle gold, but shows a full
 * purple gradient on hover.
 */
body ::-webkit-scrollbar-thumb {
  background-color: #FFC700 !important; /* Base gold color */
  background-image: none !important; /* No gradient by default */
  border-radius: 8px !important;
  border: 1px solid var(--bg1) !important;
  transition: all 0.2s ease !important;
}

body ::-webkit-scrollbar-thumb:hover {
  /* On hover, transition to purple gradient */
  background-color: var(--ui2) !important; /* Fallback color */
  background-image: linear-gradient(
    180deg,
    var(--ui2), /* Native bright purple */
    var(--color-purple) /* Theme's lighter purple */
  ) !important;
}

/* --- Compact Callouts --- */
.callout {
  padding: 0.75em 1em;
}

.callout-title {
  font-size: 0.95em;
  padding: 0;
}

.callout-content {
  padding-top: 0.5em;
}

/* ========================================
   SECTION 4: ANIMATIONS & TRANSITIONS
   ======================================== */

/* --- Keyframes for Animations --- */
/* * NOTE: Merged two duplicate @keyframes 'fadeIn' 
 * and one 'modalSlideIn' from the original file.
 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* --- Apply Animations --- */

/* Fade-in animation for notes (Reading Mode) */
.markdown-preview-view {
  animation: fadeIn 0.3s ease;
}

/* Tab switching fade effect (Editor Mode) */
.workspace-leaf-content {
  animation: fadeIn 0.3s ease-in;
}

/* Modal slide-in animation */
.modal {
  animation: modalSlideIn 0.2s ease;
}

/* --- Smooth Scrolling Behavior --- */
.workspace-leaf-content {
  scroll-behavior: smooth;
}
```

-----

## Snippet: 20-editor.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 20-editor.css
 * Contains styles specific to the Markdown editor
 * (Live Preview and Source Mode), such as active line
 * and inline code styling.
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: ACTIVE LINE STYLING
   ======================================== */

/* --- Active Line Gradient Underline (CodeMirror) --- */
/*
 * Applies a 3-color gradient as an underline to the
 * active line's text in the editor.
 */
body.active-line-on .markdown-source-view.mod-cm6 .cm-line.cm-active {
  /* 1. Set a slightly lighter background for clarity */
  background-color: #1A1B1E;
  
  /* 2. The gradient underline */
  background-image: linear-gradient(
    to right,
    var(--theme-purple, #9E6AD3),
    var(--theme-gold, #FFC700),
    var(--theme-teal, #2DD4BF)
  ) !important;
  
  /* 3. Position the gradient at the bottom */
  background-position: 0 100% !important;
  
  /* 4. Make it a 2px high line */
  background-size: 100% 2px !important;
  
  /* 5. Don't repeat the gradient */
  background-repeat: no-repeat !important;
  
  /* 6. CRITICAL: Disable box-shadow "wings" */
  box-shadow: none !important;
}

/* 7. Add padding to prevent text from touching the underline */
body.active-line-on .markdown-source-view.mod-cm6 .cm-line.cm-active > span {
  padding-bottom: 4px;
}

/* ========================================
   SECTION 2: INLINE ELEMENT STYLING
   ======================================== */

/* --- Styled & Click-to-Select Inline Code --- */
/* * NOTE: Pure CSS cannot copy to clipboard.
 * This uses 'user-select: all' as the next best thing.
 */

/* --- 1. Base Style (for both Editor and Preview) --- */
.markdown-source-view.mod-cm6 .cm-inline-code,
.markdown-preview-view .inline-code {
  /* Using theme's native colors for consistency */
  background-color: rgba(var(--theme-purple-rgb), 0.2); /* Dark, transparent purple */
  color: var(--ax1); /* Native Gold */
  border: 1px solid var(--icon-color); /* Native Teal */
  
  padding: 2px 5px;
  border-radius: 4px;
  font-family: 'Fira Code', var(--font-monospace-override), monospace;
  font-weight: 500;
  
  /* --- 2. The "Click-to-Select" Behavior --- */
  cursor: pointer;
  user-select: all; /* On click, select all text */
}

/* --- 3. Font Sizing (Editor vs. Preview) --- */
.markdown-source-view.mod-cm6 .cm-inline-code {
  font-size: 0.95em; /* Slightly smaller in editor */
}

.markdown-preview-view .inline-code {
  font-size: 1em; /* Normal size in preview */
}

/* --- 4. Hover Effect --- */
.markdown-source-view.mod-cm6 .cm-inline-code:hover,
.markdown-preview-view .inline-code:hover {
  background-color: rgba(var(--theme-purple-rgb), 0.35); /* Brighter on hover */
  border-color: var(--ax2); /* Brighter Gold */
}

/* ========================================
   SECTION 3: TASK STYLING (EDITOR)
   ======================================== */

/* --- Grayscale Completed Tasks (Live Preview) --- */
/*
 * This complements the Reading Mode style in 02-typography.css
 * by applying a grayscale filter to completed task lines
 * in the Live Preview editor.
 */
.HyperMD-task-line[data-task]:not([data-task=" "]) span {
  filter: grayscale();
}
```

-----

## Snippet: 30-sidebar.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 30-sidebar.css
 * Styles all sidebar components, including the
 * File Explorer, Outline (ToC) pane, and folder/file titles.
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: FILE EXPLORER (GENERAL)
   ======================================== */

/* --- Tighter folder spacing --- */
.nav-folder-children {
  padding-left: 12px;
}

/* --- Tighter file title spacing --- */
.nav-file-title {
  padding: 1px 3px;
  border-radius: 4px;
}

/* --- Smooth transitions for file/folder hover --- */
.nav-file-title,
.nav-folder-title {
  transition: background 0.15s ease, transform 0.15s ease;
}

/* --- Hover animation for file titles --- */
/* * NOTE: Merged two different hover rules.
 * This one has a larger transform and background change.
 */
.nav-file-title:hover {
  transform: translateX(4px);
  background-color: var(--background-modifier-hover);
}

/* ========================================
   SECTION 2: FILE EXPLORER (STYLED)
   ======================================== */

/* --- Active File Title Style --- */
/* Style the text of the currently open file */
.nav-file-title.is-active .nav-file-title-content {
  font-weight: 800;
  color: #7800F4; /* Deep Purple */
}

/* --- Color-code Folders by Prefix --- */
/*
 * Uses attribute selectors to style folders based on
 * their top-level path.
 */
.nav-folder[data-path^="Projects"] .nav-folder-title {
  color: #3b82f6; /* Blue for Projects */
}

.nav-folder[data-path^="Archive"] .nav-folder-title {
  color: #9ca3af; /* Gray for Archive */
}

.nav-folder[data-path^="Resources"] .nav-folder-title {
  color: #10b981; /* Green for Resources */
}

/* ========================================
   SECTION 3: OUTLINE / TOC PANE
   ======================================== */

/* --- Header Counters in Outline Pane --- */

/* 1. Reset counter for the root level */
[data-type="outline"] {
  counter-reset: rootLayout;
}

/* 2. Style root level items (H1, H2, etc.) */
[data-type="outline"] .tree-item .tree-item-self .tree-item-inner::before {
  content: counters(rootLayout, ".") ". ";
  counter-increment: rootLayout;
}

/* 3. Reset nested counter for children */
[data-type="outline"] .tree-item-children {
  counter-reset: internalLayout;
}

/* 4. Style nested level items (e.g., 1.1, 1.2) */
[data-type="outline"]
  .tree-item-children
  .tree-item
  .tree-item-self
  .tree-item-inner::before {
  content: counters(rootLayout, ".") "." counters(internalLayout, ".") ". " !important;
  counter-increment: internalLayout;
}
```

-----

## Snippet: 40-plugins.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 40-plugins.css
 * Contains styles to customize third-party plugins
 * like Dataview, Calendar, etc., for a harmonious look.
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: DATAVIEW PLUGIN
   ======================================== */

/* --- Dataview Table Zebra Striping --- */
.dataview.table-view-table tbody tr:nth-child(odd) {
  background-color: rgba(var(--background-secondary-rgb), 0.5);
}

/* --- Dataview Table Hover Effect --- */
.dataview.table-view-table tbody tr:hover {
  background-color: var(--background-modifier-hover);
}

/* --- Dataview Task Checkbox Styling --- */
.dataview.table-view-table input[type="checkbox"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
}

/* ========================================
   SECTION 2: GENERAL PLUGIN HARMONY
   ======================================== */

/* --- Standardize plugin panel backgrounds --- */
.calendar-view,
.backlink-pane,
.outline-view,
.dataview {
  background: var(--background-secondary);
  border-radius: var(--radius-m);
  padding: 12px;
}

/* --- Unified plugin header styling --- */
.calendar-view-header,
.backlink-pane-header,
.outline-view-header {
  font-size: var(--font-ui-medium);
  font-weight: var(--font-semibold);
  color: var(--text-normal);
  padding: 8px 12px;
  border-bottom: 1px solid var(--background-modifier-border);
  margin-bottom: 12px;
}
```

-----

## Snippet: 50-responsive.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 50-responsive.css
 * Holds all @media queries for responsive design,
 * ensuring the vault looks good on mobile and tablet.
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: MOBILE LAYOUT (SMALL SCREENS)
   ======================================== */

/* --- Responsive Line Length Adjustment --- */
/*
 * Overrides the '85ch' optimal line length on small
 * screens to use the full width, preventing wasted space.
 */
@media (max-width: 600px) {
  .markdown-source-view.mod-cm6 .cm-sizer,
  .markdown-preview-view .markdown-preview-sizer {
    max-width: 100%;
  }
}
```

-----

## Snippet: 99-experimental.css

```css
/*================================*\
| Gradient Snippets for Obsidian |
|       by Pur3v4d3r         |
| -------------------------------|
\*================================*/

/* 99-experimental.css
 * A testing area for new styles, broad overrides,
 * and feature detection (@supports).
 *
 * Compatible with: Obsidian 1.5+
 * Author: Pur3v4d3r
 * Last updated: 2025-11-14
 */

/* ========================================
   SECTION 1: ANIMATIONS & EFFECTS
   ======================================== */

/* --- Pulsing effect for loading states --- */
@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.is-loading {
  animation: pulse 1.5s ease-in-out infinite;
}

/* ========================================
   SECTION 2: BROAD OVERRIDES
   ======================================== */

/* --- Apply transitions to all interactive elements --- */
/*
 * NOTE: This is a very broad selector (*) and can
 * impact performance. It's placed here as an
 * experimental override.
 */
* {
  transition: background-color 0.2s ease, color 0.2s ease,
    border-color 0.2s ease, transform 0.2s ease;
}

/* ========================================
   SECTION 3: FEATURE DETECTION
   ======================================== */

/* --- Use modern features (backdrop-filter) with fallbacks --- */

/* If backdrop-filter is supported, use it for modals */
@supports (backdrop-filter: blur(10px)) {
  .modal-bg {
    backdrop-filter: blur(10px);
    background-color: rgba(0, 0, 0, 0.5);
  }
}

/* If not supported, use a solid dark background */
@supports not (backdrop-filter: blur(10px)) {
  .modal-bg {
    background-color: rgba(0, 0, 0, 0.8);
  }
}
```
























































# Snippet-Index



### File explorer
```
/* ========================================
   SECTION 1: FILE EXPLORER (GENERAL)
   ======================================== */

/* --- Tighter folder spacing --- */
.nav-folder-children {
  padding-left: 12px;
}

/* --- Tighter file title spacing --- */
.nav-file-title {
  padding: 1px 3px;
  border-radius: 4px;
}

/* --- Smooth transitions for file/folder hover --- */
.nav-file-title,
.nav-folder-title {
  transition: background 0.15s ease, transform 0.15s ease;
}

/* --- Hover animation for file titles --- */
/* * NOTE: Merged two different hover rules.
 * This one has a larger transform and background change.
 */
.nav-file-title:hover {
  transform: translateX(4px);
  background-color: var(--background-modifier-hover);
}
/* ========================================
   SECTION 2: FILE EXPLORER (STYLED)
   ======================================== */

/* --- Active File Title Style --- */
/* Style the text of the currently open file */
.nav-file-title.is-active .nav-file-title-content {
  font-weight: 800;
  color: #7800F4; /* Deep Purple */
}

/* --- Color-code Folders by Prefix --- */
/*
 * Uses attribute selectors to style folders based on
 * their top-level path.
 */
.nav-folder[data-path^="Projects"] .nav-folder-title {
  color: #3b82f6; /* Blue for Projects */
}

.nav-folder[data-path^="Archive"] .nav-folder-title {
  color: #9ca3af; /* Gray for Archive */
}

.nav-folder[data-path^="Resources"] .nav-folder-title {
  color: #10b981; /* Green for Resources */
}

```
### Active Line Styling
```
/* ========================================
  SECTION 1: ACTIVE LINE STYLING
  ======================================== */

/* --- Active Line Gradient Underline (CodeMirror) --- */
/*
 * Applies a purple gradient that fades to transparent
 * on both sides as an underline to the active line's
 * text in the editor.
 */
body.active-line-on .markdown-source-view.mod-cm6 .cm-line.cm-active {
  /* 1. Set a slightly lighter background for clarity */
  background-color: #230c3aff;
  
  /* 2. The gradient underline - purple fading to transparent */
  background-image: linear-gradient(
   to right,
   transparent,
   var(--theme-purple, #9E6AD3),
   transparent
  ) !important;
  /* 3. Position the gradient at the bottom */
  background-position: 0 100% !important;
  /* 4. Make it a 2px high line */
  background-size: 100% 2px !important;
  /* 5. Don't repeat the gradient */
  background-repeat: no-repeat !important;
  /* 6. CRITICAL: Disable box-shadow "wings" */
  box-shadow: none !important;
}
```


### Gradient Underline Active Tab
```
/* --- Gradient Underline for Active Tab --- */
/*
 * Applies your 3-color gradient as an underline
 * to the currently active tab.
 */
body .workspace-tab-header.is-active {
  background-image: linear-gradient(
    to right,
    var(--ui2), /* Native Purple */
    var(--ax1), /* Native Gold */
    var(--icon-color) /* Native Teal */
  ) !important;
  
  background-position: 0 100% !important;
  background-size: 100% 2px !important;
  background-repeat: no-repeat !important;
  border-bottom: none !important;
  box-shadow: none !important;
}
```

### Animation Effects
```
/* ========================================
   SECTION 1: ANIMATIONS & EFFECTS
   ======================================== */

/* --- Pulsing effect for loading states --- */
@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.is-loading {
  animation: pulse 1.5s ease-in-out infinite;
}
```

### Experimental
```
/* ========================================
   SECTION 3: FEATURE DETECTION
   ======================================== */

/* --- Use modern features (backdrop-filter) with fallbacks --- */

/* If backdrop-filter is supported, use it for modals */
@supports (backdrop-filter: blur(10px)) {
  .modal-bg {
    backdrop-filter: blur(10px);
    background-color: rgba(0, 0, 0, 0.5);
  }
}

/* If not supported, use a solid dark background */
@supports not (backdrop-filter: blur(10px)) {
  .modal-bg {
    background-color: rgba(0, 0, 0, 0.8);
  }
}
```

### Horizontal-Rules
```
/* -- HORIZONTAL RULES -- */
/* We replace the default <hr> line with an elegant, fading gradient. */
hr {
  height: 2px;
  border: none;                                /* Remove the default border */
  background: linear-gradient(
    to right,
    transparent,                                /* Start with transparency */
    #7800F4,                                   /* Our primary accent gold/yellow in the center */
    transparent 
  );
  margin-top: 2.5em;                           /* Give it some vertical space */
  margin-bottom: 2.5em;
}
```

### Tasks Faded Completiuon
```
/* ----------------------- */
/* Faded emoji in ✓ tasks */
/* ----------------------- */
ul > li.task-list-item p {
  text-indent: -1.5em;
}
ul > li.task-list-item.is-checked {
  position: relative;
  filter: url();
}
ul > li.task-list-item.is-checked::after {
  content: "";
  position: absolute;
  display: inline-block;
  backdrop-filter: grayscale();
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}
.markdown-source-view.mod-cm6
  .HyperMD-task-line[data-task]:not([data-task=" "])
  span {
  filter: grayscale();
}
```
### Shimmer Effect on Hover
```
/* --- On Hover: Activate Shimmer Animation --- */
.callout:hover::before {  
  animation: shimmer 3s ease-in-out infinite !important;
} 
@keyframes shimmer {
  0% { background-position: -500% 0t; }
  100% { background-position: 500% 0%; }
}
.callout-icon {
  color: var(--callout-color) ;;
}
.callout-content {
  color: var(--theme-text);;
}
/* End of Snippet */
```

### Animated Border Callout
```
/*================================*\
 |     Animated Border Snippet    |
 |        by Pur3v4d3r            |  
 | -------------------------------|
\*================================*/

/* --- Snippet: Animated Border for Callouts --- */ 
/* CSS: Adds an animated gradient border to callouts on hover. */
/* Affects: .callout, .callout-icon, .callout-content */
.callout {
  position: relative!important;
  border: 2px solid transparent!important; /* Initial transparent border */
  border-radius: 8px!important;
  overflow: hidden!important; /* Ensure the animated border doesn't overflow */
}
.callout::before {
  content: ''!important;
  position: absolute!important;
  top: -2px!important;
  left: -2px;
  right: -2px;
  bottom: -2px;
  background: linear-gradient(
    to right, 
    var(--theme-purple, #9E6AD3), 
    var(--theme-gold, #FFC700), 
    var(--theme-teal, #2DD4BF)
  )!important;
  background-size: 500% 500%;
  z-index: -1; /* Place behind the callout content */
  border-radius: 10px; /* Match callout border radius */
  opacity: 0.4;
  transition: opacity 0.3s ease;
}
```


### Callout Icon and Text Modification

```
/* --- Snippet: Callout Icon and Text Color Override --- */
/* CSS: Overrides callout icon and text color to a fixed color instead of theme variable. */
/* Affects: .callout-icon, .callout-content */
.callout-icon {
  color: #696969 /* Neutral Gray */ ;
}
.callout-content {
  color: #EAEAEAEA /* Light Gray */ ;
}
/* End of Snippet */
```

### Image Modifications
```
Image Pseudo Class Snippet:
Here is the code for the image snippets. Most of the attributes are customizable so feel free to change them to fit your theme/use case. You can also copy/paste and change the reference to make as many different pseudo classes as you want.

div[src$="#portrait"] {
  position: absolute;
  right: 0px;
  top: 0px;
  width: 200px;
  clip-path: ellipse(32% 45% at 50% 50%);
}

div[src$="#side"] {
  position: relative;
  float: left;
  width: 35%;
  margin-top: 5px;
  margin-left: 10px;
  margin-right: 12px;
}
Side-bar Quote Snippet:
This is for making a side bar quote that is often seen in webpages, books, physical print media. There are some drawbacks to this (see video for details) compared to the images. Also, feel free to change the details to match your theme (especially the font options since those I chose at random and probably won’t match your theme or anything else)

div[src$="-sbq"] {
    background-color: #6096cc;
    position: relative;
    right: -20px;
    float: right;
    clip-path: polygon(0% 0%,100% 0%,100% 80%,44% 80%,20% 100%,25% 80%,0% 80%);
    width: 35%;
    margin-top: 5px;
    margin-left: 10px; 
  }
  
  div[src$="-sbq"] div.markdown-embed-link {
    visibility: hidden;
  }
  
  div[src$="-sbq"] div.markdown-embed {
    margin-top: 0px;
    margin-bottom: 0px;
  }
  div[src$="-sbq"] .markdown-preview-view {
    padding: 3px;
    padding-left: 10px;
    padding-bottom: 40px;
  }
  div[src$="-sbq"] .markdown-preview-view p {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: larger;
    font-style: italic;
    color: black;
  }
```


### Resizable Mermaid
```
svg[id^="m"][width][height][viewBox] {
    max-width: 95%;
    max-height: 95%;
}

div.mermaid {
    margin-left: 0 !important;
    text-align: center;
    resize:both;
    overflow:auto;
    margin-bottom: 2px;
    position:relative;
    max-height: 600px;
    max-width: 100%;
}

div.mermaid::after {
    content:'';
    display:block;
    width:10px;
    height:10px;
    background-color:yellowgreen;
    position:absolute;
    right:0;
    bottom:0;
}
```


### Callout Title Size & Themed Color Fix
```
Callout Title Size & Themed Color Fix
    Forces title to inherit color, or falls back to --callout-color variable.
*/

.callout .callout-title,
.callout .callout-title-inner {
    /* Retain the size fix */
    font-size: 1.2em !important; 
    
    /* Strategy: Use the official variable for the text color. 
        Minimal Theme usually sets this variable to match the callout's accent color.
    */
    color: var(--callout-color) !important;
}

/* Optional: If --callout-color is not working, try using 'inherit' */
/*
.callout .callout-title,
.callout .callout-title-inner {
    color: inherit !important;
}
*/

/* Optional: Adjusting the icon size to match the larger text */
.callout-icon svg {
    height: 1.2em !important;
    width: 1.2em !important;
}

/* Setting the font weight */
.callout .callout-title {
    font-weight: 600 !important;
}
```

### Code Block Styling
```
/* Code Block Styling */

.theme-dark {
    /* Enforce true black for code blocks for OLED efficiency and contrast */
    --code-background: #000000;
    
    /* Use a light text color */
    --code-normal: #EAEAEA; 

    /* Inline Code Styling */
    .markdown-source-view.mod-cm6 .cm-inline-code,
    .markdown-preview-view code {
        /* Use a faint version of your color for the inline code background */
        background-color: #190061; /* Purple  */
        color: #EAEAEA; /* Keep text white */
        border: 1px solid #9E6AD333; /* Very subtle purple border */
        padding: 2px 4px;
        border-radius: 4px;
```

### Custom Tables Snippet
```
/* --- Architect's Blueprint: Custom Tables Snippet --- */
/*
  This snippet styles markdown tables into clean, readable
  "Data-Grids", aligning with a professional and minimalist aesthetic.
*/

/* -------------------------------------------------- */
/* 1. Table Container
/* -------------------------------------------------- */
/* Targets the container div that wraps the table */
.markdown-rendered table {
  /* Ensures the table can span the full width of the note */
  width: 100%;
  
  /* Collapses borders between cells for a cleaner look */
  border-collapse: collapse;
  
  /* Provides spacing around the table */
  margin-top: 1.5em;
  margin-bottom: 1.5em;
  
  /* Adds a very subtle border around the entire table */
  border: 1px solid var(--background-modifier-border);
  border-radius: 6px; /* Rounded corners for the container */
  
  /* Prevents content from overflowing the rounded corners */
  overflow: hidden;
}

/* -------------------------------------------------- */
/* 2. Table Header (thead)
/* -------------------------------------------------- */
.markdown-rendered th { /* th = table header cells */
  /* A subtle background to distinguish the header */
  background-color: var(--background-secondary-alt);
  
  /* Slightly bolder text for header labels */
  font-weight: 600;
  
  /* Text alignment for headers */
  text-align: left;
  
  /* Padding inside header cells */
  padding: 12px 15px;
  
  /* A bottom border to separate header from data */
  border-bottom: 2px solid var(--background-modifier-border);
}

/* -------------------------------------------------- */
/* 3. Table Body (tbody) & Cells (td)
/* -------------------------------------------------- */
.markdown-rendered td { /* td = table data cells */
  /* Padding inside data cells */
  padding: 10px 15px;
  
  /* A very light border between rows */
  border-top: 1px solid var(--background-modifier-border);
  
  /* Ensures text is vertically aligned in the middle of the cell */
  vertical-align: middle;
}

/* -------------------------------------------------- */
/* 4. Zebra Striping for Readability
/* -------------------------------------------------- */
/* This targets every odd-numbered row in the table body */
.markdown-rendered tbody tr:nth-of-type(odd) {
  /* Applies a very faint background color */
  background-color: var(--background-secondary);
}

/* We want to reset the background on hover to provide clear feedback */
.markdown-rendered tbody tr:hover {
  background-color: var(--background-modifier-hover);
}
```

### Link Style Override
```
/* >  * =============================================
 * Forceful Link Style Override
 * Overrides theme styles for Internal, External,
 * and Unresolved links in all modes using 
 * !important to ensure priority.
 * =============================================
 */
/* --- 1. Internal Links (Resolved) --- */
/* (e.g., [[My Note]]) */
/* Reading View */
.markdown-rendered a.internal-link:not(.is-unresolved) {
  color: 7449B3!important; /* */
  text-decoration: underline !important; /* */
}
/* Editing View (Live Preview & Source) */
.cm-s-obsidian span.cm-link:not(.cm-unresolved),
.cm-s-obsidian span.cm-hmd-internal-link:not(.cm-unresolved) {
  color: 7449B3!important; /* A distinct blue */
  text-decoration: none !important;
}
/* --- 2. External Links --- */
/* (e.g., [Google](https://google.com)) */
/* Reading View */
.markdown-rendered a.external-link {
  color: #9E6AD3!important; /* A distinct green */
  text-decoration: underline !important;
  text-decoration-style: dotted !important;
  text-decoration-thickness: 1px !important;
  text-decoration-color: #F17925 !important;
}
/* Editing View (Live Preview & Source) */
.cm-s-obsidian span.cm-url,
.cm-s-obsidian span.cm-link.cm-formatting-link-string {
  color: #9E6AD3!important; /* A distinct green */
  text-decoration: underline !important;
  text-decoration-style: dotted !important;
  text-decoration-thickness: 1px !important;
  text-decoration-color: #F17925 !important;
}
/* --- 3. Unresolved Links --- */
/* (e.g., [[New Note That Doesn't Exist]]) */

/* Reading View */
.markdown-rendered a.is-unresolved {
  color: D4A600!important; font-style: italic; opacity: 0.7; } /* A orange*/
  opacity: 1 !important; /* Make sure it's not faded */
  text-decoration: underline !important; /* Add the underline */
  text-decoration-style: solid !important; /* Style: solid, dotted, dashed */
  text-decoration-color: D4A600!important; /* Color of the underline */
}
/* Editing View (Live Preview & Source) */
.cm-s-obsidian span.cm-link.cm-unresolved,
.cm-s-obsidian span.cm-hmd-internal-link.cm-unresolved,
.is-unresolved { /* General LP catch-all */
  color: #FF7600!important; /* A distinct red */
  opacity: 1 !important;
  text-decoration: underline !important;
  text-decoration-style: solid !important;
  text-decoration-color: #FF7600!important;
}

```

### Translucent Tool-tips
```
/* Translucent Tooltips- from: Nosedive-Obsidian */
/* Modify modal, omnibar, open looks */
input.prompt-input, input.prompt-input:active, input.prompt-input:focus {
  border-radius: 3px;
  border: 2px solid rgba(38, 38, 59, 0.5); /* in the original code this is var(--text-muted) */
  background-color: transparent;
  box-sizing: border-box;
  border-collapse: collapse;
}
/* Make legible background for menus since we overrode the background */
div.popover.hover-popover, .menu, .suggestion-container {
  background-color: #FFFFFF01;
  backdrop-filter: blur(30px);
  border: none;
}
```

### Translucent modals
```
/* Translucent modals - from: Nosedive-Obsidian */
/* Modify modal, omnibar, open looks */
input.prompt-input, input.prompt-input:active, input.prompt-input:focus {
  border-radius: 3px;
  border: 2px solid rgba(38, 38, 59, 0.5); /* in the original code this is var(--text-muted) */
  background-color: transparent;
  box-sizing: border-box;
  border-collapse: collapse;
}

.modal-bg {
  background-color: #FFFFFF01;
  backdrop-filter: blur(20px);
}

/* Make legible background for menus since we overrode the background */
div.popover.hover-popover, .menu, .suggestion-container {
  background-color: #FFFFFF01;
  backdrop-filter: blur(30px);
  border: none;
}
```

### Compact Top sidebar navigation
```
/* Compact Top sidebar navigation */
.workspace-tab-header-inner{
    padding-left:3px;
    padding-right:3px;
}

/* Compact File Explorer Header */
[data-type=file-explorer] {
	.nav-header {
		padding:5px 12px 4px 12px;

		.nav-buttons-container {
			margin-left:-4px;
			/* justify-content:flex-end; */

			&:hover {
				.clickable-icon {
					opacity:0.7;
				}
			}

			.clickable-icon {
				padding:2px;
				color:var(--tx2, var(--text-normal)) !important;
				transition: .2s color ease-in;
				opacity:0.45;
				background:transparent;
				transition: .1s all ease-in;

				&:hover {
					background-color:transparent;
					opacity:1;
				}

				svg {
					width:18px;
					height:18px;
				}
			}

			.view-actions:hover .clickable-icon {
				color: var(--tx1, var(--text-faint)) !important;
			}
		}
	}
}
```


### Make some folders appear more subtle
```
		/* Make some folders appear more subtle */
		> div > .nav-folder.is-collapsed:has(> [data-path=Assets]),
		.nav-folder:not(:not(.is-collapsed)):has(> [data-path*="/attachments"]) {
			opacity:0.6;
		}
```

### Hide file tag when an icon is set
```
		/* Hide file tag when an icon is set */
		.nav-file:has(.nav-file-tag):has(.iconize-icon) {
			.nav-file-tag {display:none}
		}
	}
```

### Collapse chevrons more subtle
```
		/* collapse chevrons more subtle*/
		.collapse-icon {
			opacity:0.4;
			transition: opacity 0.2s ease-in-out;
		}
		.nav-folder:not(.is-collapsed) > .mod-collapsible > .collapse-icon {
			opacity:1;
		}
```

### Compact File Explorer Minimal
```
/*
    Compact File Explorer Minimal
    This is tweak of the file explorer that avoids messing with the chevrons, to avoid the
	janky problematic padding calculations issue

    https://github.com/replete/obsidian-minimal-theme-css-snippets
*/

[data-type=file-explorer] {

	.nav-files-container {
		/* compact file explorer */
		padding: 0;
		margin-left: -12px;

		.nav-file-title,
		.nav-folder-title {
			padding-top:3px;
			padding-bottom:3px;
		}

		/* hide root chevrons */
		> div > .nav-folder {
			> .mod-collapsible .collapse-icon {
				visibility:hidden;
			}
		}
```


### Style the container of the active file title
```
/* Style the container of the active file title */
.nav-file.is-active {
  background-color: rgba(0, 128, 255, 0.1);
  border-left: 3px solid #ffc800;
}
```
















































# End of Note
