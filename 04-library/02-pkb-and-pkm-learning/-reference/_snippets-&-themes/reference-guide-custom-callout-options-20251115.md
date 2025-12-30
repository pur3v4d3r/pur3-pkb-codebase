---
title: "CSS Taxonomy: Callouts"
id: "20251115122626"
type: reference
status: seedling
rating: ""
source: claude-4.5-sonnet
url: https://claude.ai/chat/90b14cf6-1103-452e-a1e7-930b9a4057b9
tags:
  - year/2025
  - status/seedling
  - pkb/infrastructure
  - type/reference
  - obsidian/customization/snippets
  - pkb/plugin/style-settings
  - type/reference/taxonomy
aliases:
  - Callout CSS Reference
  - Obsidian Callout Styling
  - Callout Customization Guide
  - Callout CSS Taxonomy
  - Obsidian Callout Modification
link-up: []
link-related:
  - "[[reference-comprehensive-css-variables-20251106]]"
  - "[[reference-comprehensive-css-variable-2025110619]]"
  - "[[202511131029_css-snippet-modification-for-obsidian_comprehensive-reference]]"
  - "[[202511131909_complete-modular-callout-system_foundation-and-swappable-styles]]"
  - "[[202511140502_css-snippet-library_comprehensive-reference]]"
  - "[[202511150329_alternative-checkboxes_reference]]"
  - "[[202511151216_gemini_callout-taxonomy_reference]]"
  - "[[_snippet-callout-system-workbench]]"
  - "[[_snippet-css-variables-index]]"
  - "[[reference-technical-modular-callout-system-swappable-styles-2025111312]]"
  - "[[scratchpad-for-moving-snippets]]"
  - "[[snippet-index-note_202511132126]]"
---


---



# 🎨 Complete Obsidian Callout Customization Reference

> [!abstract]
> This reference note provides an exhaustive taxonomy of all [[CSS]] customization options, syntax patterns, and modification techniques for [[obsidian]] callouts. It covers native callout features, [[CSS Variables]], [[CSS Selectors]], pseudo-elements, [[Style Settings Plugin]] integration, and advanced styling techniques. This serves as a complete foundational resource for custom callout visualization development.

---

## 🧱 Callout Anatomy & Core Structure

> [!core-principle]
> Understanding the [[DOM]] structure of Obsidian callouts is essential for effective customization. Each callout is composed of multiple nested elements that can be targeted independently.

### HTML Structure Breakdown

```html
<div class="callout" data-callout="type-name">
  <div class="callout-title">
    <div class="callout-icon">
      <svg class="svg-icon lucide-icon">...</svg>
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

## ⚙️ Native Callout Syntax & Features

> [!definition]
> Native callout features are built into Obsidian and require no [[CSS Snippets]] or plugins to function.

### Basic Callout Syntax

```markdown
> [!type] Optional Title
> Content goes here
```

### Foldable Callouts

> [!methodology-and-sources]
> Callouts can be made collapsible by adding `+` (expanded by default) or `-` (collapsed by default) immediately after the type identifier.

**Syntax:**
```markdown
> [!info]+ Expanded by Default
> Content is visible

> [!warning]- Collapsed by Default
> Content is hidden initially
```

### Nested Callouts

Callouts can be nested within each other, with each level maintaining its own styling, icon, and background properties.

```markdown
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
```markdown
> [!callout-type|modifier]
```

---

## 🎨 Core CSS Variables for Callouts

> [!important-links]
> **Primary Callout Variables Reference**

Obsidian uses specific CSS variables to define callout appearance, with `--callout-color` using RGB numeric values (0-255) and `--callout-icon` accepting Lucide icon identifiers or custom SVG code.

### Essential CSS Variables

| Variable | Description | Value Format | Example |
|----------|-------------|--------------|---------|
| `--callout-color` | Main accent color (RGB only) | `R, G, B` (0-255) | `255, 121, 198` |
| `--callout-icon` | Icon identifier or SVG | `lucide-icon-name` or SVG string | `lucide-lightbulb` |
| `--callout-title-color` | Title text color override | RGB format | `255, 0, 0` |
| `--callout-border-width` | Border thickness | CSS length unit | `2px` |
| `--callout-border-opacity` | Border transparency | `0` to `1` | `0.5` |
| `--callout-title-padding` | Title area spacing | CSS spacing | `12px 16px` |
| `--callout-content-padding` | Content area spacing | CSS spacing | `16px` |
| `--callout-title-size` | Title font size | CSS font size | `1em` |
| `--callout-fold-size` | Fold indicator size | CSS size | `18px` |
| `--callout-radius` | Corner roundness | CSS border-radius | `var(--radius-s)` |

> [!helpful-tip]
> RGB color values must be provided as comma-separated integers (0-255). Hex colors (#FFFFFF) and named colors (red, blue) will not work with the native `--callout-color` variable.

### Lucide Icon System

Obsidian uses Lucide version 0.446.0 (as of June 2025). All icons from this version or earlier can be used in custom callouts.

**Icon Syntax:**
```css
--callout-icon: lucide-<icon-name>;
```

**Custom SVG Icons:**
```css
--callout-icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path d="..."/>
</svg>';
```

> [!example]
> **Common Icon Examples:**
> - `lucide-lightbulb` - Ideas and insights
> - `lucide-alert-triangle` - Warnings
> - `lucide-check-circle` - Success/completion
> - `lucide-info` - Information
> - `lucide-flame` - Important/urgent
> - `lucide-target` - Goals
> - `lucide-code` - Programming

---

## 🎯 CSS Selector Targeting

> [!core-principle]
> Precise CSS selector usage enables granular control over specific callout types, states, and nested elements.

### Primary Selectors

#### **1. Target All Callouts**
```css
.callout {
  /* Styles apply to every callout */
}
```

#### **2. Target Specific Callout Type**
```css
.callout[data-callout="type-name"] {
  /* Styles for specific type only */
}
```

#### **3. Target Callout Type with Prefix Match**
Using `^=` allows matching callout types that start with a specific string, useful for creating variant families.

```css
.callout[data-callout^="note"] {
  /* Matches: note, note-scrollable, note-custom, etc. */
}
```

#### **4. Target Callout Type with Suffix Match**
```css
.callout[data-callout$="-scrollable"] {
  /* Matches any type ending in -scrollable */
}
```

#### **5. Target Callout Type with Substring**
```css
.callout[data-callout*="important"] {
  /* Matches any type containing "important" */
}
```

### Element-Specific Selectors

```css
/* Title container */
.callout-title {
  /* Title bar styling */
}

/* Title text only */
.callout-title-inner {
  /* Text-specific styling */
}

/* Icon container */
.callout-icon {
  /* Icon wrapper styling */
}

/* SVG icon itself */
.callout-icon .svg-icon {
  /* Direct icon styling */
}

/* Content area */
.callout-content {
  /* Body content styling */
}

/* Fold indicator */
.callout-fold {
  /* Collapse/expand button */
}
```

### State-Based Selectors

```css
/* Collapsed callout */
.callout.is-collapsed {
  /* Styles when folded */
}

/* Hover state */
.callout:hover {
  /* Interactive hover effect */
}

/* Focus state */
.callout:focus-within {
  /* When content has focus */
}
```

### Nested Callout Selectors

```css
/* Direct child callout */
.callout > .callout-content > .callout {
  /* First level nesting */
}

/* Any nested callout */
.callout .callout {
  /* All nested levels */
}

/* Specific nesting depth */
.callout .callout .callout {
  /* Third-level nested callout */
}
```

---

## 🎨 Comprehensive CSS Property Catalog

> [!quick-reference]
> **Complete Property Reference for Callout Customization**

### **Colors & Visual Identity**

#### Background Properties
```css
.callout {
  /* Solid background */
  background-color: rgba(255, 121, 198, 0.2);
  
  /* Gradient background */
  background: linear-gradient(135deg, 
    rgba(var(--callout-color), 0.1) 0%, 
    rgba(var(--callout-color), 0.3) 100%);
  
  /* Multiple backgrounds */
  background: 
    linear-gradient(to right, rgba(var(--callout-color), 0.2), transparent),
    var(--background-primary);
  
  /* Background with blend mode */
  background-color: rgb(var(--callout-color));
  background-blend-mode: multiply;
  
  /* Transparent background */
  background: transparent;
}
```

#### Border Styling
```css
.callout {
  /* Basic border */
  border: 2px solid rgb(var(--callout-color));
  
  /* Border with opacity */
  border: 1px solid rgba(var(--callout-color), 0.5);
  
  /* Individual borders */
  border-left: 4px solid rgb(var(--callout-color));
  border-top: none;
  border-right: none;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  
  /* Border with color-mix */
  outline: 1px solid color-mix(in srgb, 
    rgb(var(--callout-color), 0.35) 90%, black);
  
  /* Rounded corners */
  border-radius: var(--radius-s); /* Use theme variable */
  border-radius: 8px; /* Fixed value */
  border-radius: 12px 12px 0 0; /* Top corners only */
}
```

#### Color Overlays & Effects
Advanced theming can use pseudo-elements to create overlay effects that combine base backgrounds with callout-specific colors.

```css
/* Base background for consistency */
.callout {
  background-color: var(--background-primary) !important;
  position: relative;
  overflow: hidden;
}

/* Color overlay technique */
.callout::before {
  content: "";
  position: absolute;
  inset: 0;
  background-color: rgb(var(--callout-color), 0.3);
  border: 2px solid rgba(var(--callout-color), 0.6);
  pointer-events: none;
  z-index: 0;
  border-radius: var(--radius-s);
}

/* Ensure content stays above overlay */
.callout > * {
  position: relative;
  z-index: 1;
}
```

### **Typography & Text Styling**

```css
.callout-title-inner {
  /* Font properties */
  font-family: var(--font-interface);
  font-size: 1.1em;
  font-weight: 600;
  font-style: italic;
  
  /* Text transform */
  text-transform: uppercase;
  text-transform: capitalize;
  
  /* Letter spacing */
  letter-spacing: 0.05em;
  
  /* Text alignment */
  text-align: center;
  text-align: left;
  
  /* Text color */
  color: rgb(var(--callout-color));
  color: var(--text-normal);
  
  /* Text shadow */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

.callout-content {
  /* Content text styling */
  font-size: 0.95em;
  line-height: 1.6;
  color: var(--text-normal);
  
  /* First line styling */
  text-indent: 1em;
}
```

### **Spacing & Layout**

```css
.callout {
  /* Padding */
  padding: 16px;
  padding: 12px 16px; /* vertical horizontal */
  
  /* Margin */
  margin: 1em 0;
  margin-bottom: 2em;
  
  /* Width control */
  width: 100%;
  max-width: 800px;
  min-width: 300px;
  
  /* Height control */
  height: auto;
  min-height: 50px;
  max-height: 400px;
}

.callout-title {
  /* Title padding */
  padding: var(--callout-title-padding);
  padding: 8px 12px;
  
  /* Title layout */
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.callout-content {
  /* Content padding */
  padding: var(--callout-content-padding);
  padding: 12px 16px;
  
  /* Content overflow */
  overflow: visible;
  overflow: hidden;
  overflow-y: auto;
  overflow-x: hidden;
}
```

### **Shadows & Depth**

```css
.callout {
  /* Drop shadow */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  
  /* Multiple shadows */
  box-shadow: 
    0 1px 3px rgba(0, 0, 0, 0.12),
    0 1px 2px rgba(0, 0, 0, 0.24);
  
  /* Colored shadow using callout color */
  box-shadow: 0 4px 12px rgba(var(--callout-color), 0.2);
  
  /* Inset shadow */
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  
  /* No shadow */
  box-shadow: none;
  
  /* Filter drop-shadow (for non-rectangular shapes) */
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}
```

### **Icon Customization**

```css
.callout-icon {
  /* Icon container sizing */
  width: 24px;
  height: 24px;
  min-width: 24px;
  
  /* Icon positioning */
  display: flex;
  align-items: center;
  justify-content: center;
  
  /* Icon spacing */
  margin-right: 8px;
}

.callout-icon .svg-icon {
  /* Icon size */
  width: 18px;
  height: 18px;
  
  /* Icon color */
  color: rgb(var(--callout-color));
  fill: currentColor;
  stroke: currentColor;
  
  /* Icon masking (for custom coloring) */
  background-color: rgb(var(--callout-color));
  -webkit-mask-image: url("data:image/svg+xml,...");
  mask-image: url("data:image/svg+xml,...");
  
  /* Icon effects */
  opacity: 0.9;
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.2));
}

/* Hide icon entirely */
.callout[data-callout="no-icon"] .callout-icon {
  display: none;
}
```

### **Animations & Transitions**

Interactive animations can enhance callout functionality, with hover effects and smooth transitions improving user experience.

```css
.callout {
  /* Smooth transitions */
  transition: all 0.3s ease;
  transition: transform 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
  
  /* Property-specific transitions */
  transition: 
    background-color 0.2s ease,
    border-color 0.2s ease,
    box-shadow 0.3s ease;
}

.callout:hover {
  /* Hover lift effect */
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  
  /* Hover scale */
  transform: scale(1.02);
  
  /* Hover glow */
  box-shadow: 0 0 20px rgba(var(--callout-color), 0.3);
}

/* Prevent hover on specific types */
.callout[data-callout="multi-column"]:hover {
  transform: translateY(0px);
}

/* Fade-in animation */
.callout {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### **Flexbox & Grid Layout**

```css
.callout {
  /* Flexbox layout */
  display: flex;
  flex-direction: column;
  gap: 12px;
  
  /* Flex sizing */
  flex: 1;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: auto;
}

.callout-title {
  /* Title flexbox */
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 8px;
  flex-wrap: nowrap;
}

/* Multi-column callout layout */
.callout[data-callout="multi-column"] .callout-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  
  /* OR flexbox columns */
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
```

### **Position & Display Properties**

```css
.callout {
  /* Display mode */
  display: block;
  display: flex;
  display: grid;
  display: inline-block;
  
  /* Position */
  position: relative;
  position: absolute;
  position: sticky;
  top: 0;
  
  /* Z-index layering */
  z-index: 1;
  z-index: 10;
  
  /* Overflow control */
  overflow: visible;
  overflow: hidden;
  overflow: auto;
}

/* Floating callout */
.callout[data-callout="aside"] {
  position: absolute;
  right: 0;
  top: 0;
  width: 300px;
  margin-left: 20px;
}
```

### **Pseudo-Elements for Decoration**

```css
/* Before element (above content) */
.callout::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, 
    rgba(var(--callout-color), 0.1), 
    transparent);
  pointer-events: none;
  z-index: -1;
}

/* After element (below content) */
.callout::after {
  content: "";
  width: 48px;
  height: 12px;
  border-radius: 8px;
  position: absolute;
  top: 8px;
  right: 8px;
  background: rgb(var(--callout-color));
  opacity: 0.5;
}

/* Adding text content */
.callout[data-callout="custom"]::before {
  content: "CUSTOM";
  position: absolute;
  top: 8px;
  right: 8px;
  font-size: 0.7em;
  font-weight: 700;
  color: rgba(var(--callout-color), 0.5);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

/* Decorative accent line */
.callout::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: linear-gradient(to bottom,
    rgb(var(--callout-color)),
    rgba(var(--callout-color), 0.3));
}
```

### **Responsive Design Properties**

```css
/* Container queries (modern approach) */
@container (max-width: 600px) {
  .callout {
    padding: 8px;
    font-size: 0.9em;
  }
}

/* Media queries (traditional approach) */
@media (max-width: 768px) {
  .callout {
    margin: 0.5em 0;
  }
  
  .callout-title {
    font-size: 0.95em;
  }
}

/* Print styling */
@media print {
  .callout {
    page-break-inside: avoid;
    border: 1px solid #ccc !important;
    background: white !important;
  }
}
```

---

## 📜 Advanced CSS Techniques

> [!methodology-and-sources]
> **Advanced Customization Patterns**

### Scrollable Callouts

Scrollable callouts limit content height while maintaining styling, useful for long code blocks or extensive lists.

```css
/* Shared scrollable behavior */
.callout[data-callout$="-scrollable"] .callout-content {
  --shown-line-count: 8;
  max-height: calc(var(--line-height-normal) * 1rem * var(--shown-line-count));
  overflow-y: auto;
  
  /* Custom scrollbar */
  scrollbar-width: thin;
  scrollbar-color: rgba(var(--callout-color), 0.3) transparent;
}

/* Webkit scrollbar styling */
.callout[data-callout$="-scrollable"] .callout-content::-webkit-scrollbar {
  width: 8px;
}

.callout[data-callout$="-scrollable"] .callout-content::-webkit-scrollbar-track {
  background: transparent;
}

.callout[data-callout$="-scrollable"] .callout-content::-webkit-scrollbar-thumb {
  background: rgba(var(--callout-color), 0.3);
  border-radius: 4px;
}

.callout[data-callout$="-scrollable"] .callout-content::-webkit-scrollbar-thumb:hover {
  background: rgba(var(--callout-color), 0.5);
}
```

**Usage:**
```markdown
> [!note-scrollable] Long Content
> Lots of text here that will scroll...
```

### Column-Based Layouts

```css
/* Multi-column callout */
.callout[data-callout="multi-column"] .callout-content {
  column-count: 2;
  column-gap: 20px;
  column-rule: 1px solid rgba(var(--callout-color), 0.2);
}

/* Prevent column breaks */
.callout[data-callout="multi-column"] .callout-content > * {
  break-inside: avoid;
  page-break-inside: avoid;
}

/* Responsive columns */
@media (max-width: 768px) {
  .callout[data-callout="multi-column"] .callout-content {
    column-count: 1;
  }
}
```

### Image Gallery Callouts

```css
.callout[data-callout="gallery"] .callout-content {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 12px;
  padding: 12px;
}

.callout[data-callout="gallery"] .callout-content img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
  transition: transform 0.2s ease;
}

.callout[data-callout="gallery"] .callout-content img:hover {
  transform: scale(1.05);
  z-index: 10;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
```

### Metadata/Inline Color Modifiers

Some theme systems support inline metadata modifiers using pipe syntax to change colors dynamically.

```css
/* Color modifier: c-purple */
.callout[data-callout-metadata*="c-purple"] {
  --callout-color: 147, 51, 234;
  border-color: rgb(147, 51, 234);
}

/* Background modifier: bg-blue */
.callout[data-callout-metadata*="bg-blue"] {
  background-color: rgba(59, 130, 246, 0.2);
}

/* Combined modifier: bg-c-green */
.callout[data-callout-metadata*="bg-c-green"] {
  --callout-color: 34, 197, 94;
  background-color: rgba(34, 197, 94, 0.2);
}
```

**Usage:**
```markdown
> [!custom|c-purple] Purple Title
> [!note|bg-blue] Blue Background
> [!info|bg-c-green] Green Everything
```

### Card-Style Callouts

```css
.callout[data-callout="card"] {
  background: var(--background-primary);
  border: none;
  border-radius: 12px;
  box-shadow: 
    0 2px 4px rgba(0, 0, 0, 0.1),
    0 8px 16px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: all 0.3s ease;
}

.callout[data-callout="card"]:hover {
  transform: translateY(-4px);
  box-shadow: 
    0 4px 8px rgba(0, 0, 0, 0.12),
    0 12px 24px rgba(0, 0, 0, 0.15);
}

.callout[data-callout="card"] .callout-title {
  background: linear-gradient(135deg, 
    rgba(var(--callout-color), 0.8), 
    rgba(var(--callout-color), 0.6));
  color: white;
  padding: 16px;
}

.callout[data-callout="card"] .callout-content {
  padding: 20px;
}
```

### Timeline Callouts

```css
.callout[data-callout="timeline"] {
  position: relative;
  padding-left: 40px;
  border-left: 3px solid rgb(var(--callout-color));
  background: transparent;
}

.callout[data-callout="timeline"]::before {
  content: "";
  position: absolute;
  left: -8px;
  top: 12px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: rgb(var(--callout-color));
  border: 3px solid var(--background-primary);
  z-index: 1;
}

.callout[data-callout="timeline"] .callout-title {
  font-weight: 700;
  color: rgb(var(--callout-color));
}
```

### Infobox/Character Sheet Callouts

Infobox callouts can be styled to display structured information like character profiles or stat blocks.

```css
.callout[data-callout="infobox"] {
  width: 300px;
  float: right;
  margin: 0 0 1em 1em;
  background: var(--background-secondary);
  border: 1px solid var(--background-modifier-border);
  border-radius: 8px;
  overflow: hidden;
}

.callout[data-callout="infobox"] .callout-title {
  text-align: center;
  background: rgba(var(--callout-color), 0.2);
  padding: 12px;
  border-bottom: 2px solid rgb(var(--callout-color));
}

.callout[data-callout="infobox"] .callout-content img {
  width: 100%;
  height: auto;
  margin: 0;
}

.callout[data-callout="infobox"] .callout-content table {
  width: 100%;
  margin: 8px 0;
  font-size: 0.9em;
}
```

---

## 🔧 Style Settings Plugin Integration

> [!core-principle]
> The [[Style Settings Plugin]] enables dynamic customization through a UI without editing CSS files directly. It uses [[YAML]] syntax embedded in CSS comments.

Style Settings scans CSS files for comments beginning with `/* @settings` containing YAML configuration that defines adjustable parameters.

### Style Settings Syntax Structure

```css
/* @settings

name: Your Section Name
id: unique-identifier
settings:
  - id: setting-id
    title: Setting Display Name
    description: Explanation of what this does
    type: setting-type
    default: default-value

*/
```

### Setting Types Reference

#### **1. class-toggle** - Body Class Toggle

Class toggles add or remove a CSS class on the body element, enabling feature switching via checkbox in the UI.

```css
/* @settings

name: Callout Features
id: callout-features
settings:
  - id: brutal-callouts
    title: Brutalist Style
    description: Sharp corners, thick borders, heavy color emphasis
    type: class-toggle
    default: false
    addCommand: true

*/

/* Apply when toggle is ON */
body.brutal-callouts .callout {
  border-width: 4px;
  border-radius: 0;
  box-shadow: 6px 6px 0 rgba(0, 0, 0, 0.3);
}
```

#### **2. class-select** - Dropdown Selection

```css
/* @settings

name: Callout Style Variants
id: callout-variants
settings:
  - id: callout-style-variant
    title: Callout Style
    description: Choose overall callout appearance
    type: class-select
    allowEmpty: false
    default: modern
    options:
      - label: Modern (Default)
        value: modern
      - label: Minimal
        value: minimal
      - label: Bold
        value: bold
      - label: Glassmorphism
        value: glass

*/

body.modern .callout { /* Modern styles */ }
body.minimal .callout { /* Minimal styles */ }
body.bold .callout { /* Bold styles */ }
body.glass .callout { 
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}
```

#### **3. variable-text** - Text Input for CSS Variable

```css
/* @settings

name: Callout Spacing
id: callout-spacing
settings:
  - id: callout-gap
    title: Callout Vertical Gap
    description: Space between callouts (CSS unit)
    type: variable-text
    default: 1em

*/

.callout {
  margin-bottom: var(--callout-gap);
}
```

#### **4. variable-number** - Numeric Slider

```css
/* @settings

name: Callout Dimensions
id: callout-dimensions
settings:
  - id: callout-border-width
    title: Border Width
    description: Thickness of callout borders
    type: variable-number
    default: 2
    min: 0
    max: 10
    step: 1
    format: px

*/

.callout {
  border-width: var(--callout-border-width);
}
```

#### **5. variable-number-slider** - Visual Slider

```css
/* @settings

name: Callout Opacity
id: callout-opacity
settings:
  - id: callout-bg-opacity
    title: Background Opacity
    description: Transparency of callout backgrounds
    type: variable-number-slider
    default: 0.2
    min: 0
    max: 1
    step: 0.05

*/

.callout {
  background-color: rgba(var(--callout-color), var(--callout-bg-opacity));
}
```

#### **6. variable-color** - Color Picker

```css
/* @settings

name: Callout Colors
id: callout-colors
settings:
  - id: callout-accent-color
    title: Accent Color
    description: Override default callout accent
    type: variable-color
    format: rgb
    default: '#5E81AC'

*/

.callout[data-callout="custom"] {
  --callout-color: var(--callout-accent-color);
}
```

#### **7. variable-select** - Variable Dropdown

```css
/* @settings

name: Callout Fonts
id: callout-fonts
settings:
  - id: callout-title-font
    title: Title Font Family
    description: Font for callout titles
    type: variable-select
    default: var(--font-interface)
    options:
      - label: Interface Font
        value: var(--font-interface)
      - label: Text Font
        value: var(--font-text)
      - label: Monospace
        value: var(--font-monospace)

*/

.callout-title {
  font-family: var(--callout-title-font);
}
```

#### **8. heading** - Section Organizer

```css
/* @settings

name: Advanced Callout Customization
id: advanced-callouts
settings:
  - id: colors-heading
    title: Color Settings
    type: heading
    level: 2
  
  - id: callout-primary-color
    title: Primary Color
    type: variable-color
    default: '#FF5733'
  
  - id: spacing-heading
    title: Spacing Settings
    type: heading
    level: 2
  
  - id: callout-padding
    title: Internal Padding
    type: variable-number
    default: 16
    format: px

*/
```

### Complete Style Settings Example

```css
/* @settings

name: Power Callouts
id: power-callouts
settings:
  - id: general-heading
    title: General Appearance
    type: heading
    level: 1
  
  - id: callout-rounded
    title: Rounded Corners
    description: Enable rounded corners on all callouts
    type: class-toggle
    default: true
  
  - id: callout-shadows
    title: Drop Shadows
    description: Add subtle shadows to callouts
    type: class-toggle
    default: true
  
  - id: style-heading
    title: Style Variants
    type: heading
    level: 1
  
  - id: callout-style
    title: Callout Style
    type: class-select
    default: default
    options:
      - label: Default
        value: default
      - label: Brutalist
        value: brutal
      - label: Soft
        value: soft
  
  - id: dimensions-heading
    title: Dimensions
    type: heading
    level: 1
  
  - id: callout-border-width
    title: Border Width
    type: variable-number-slider
    default: 2
    min: 0
    max: 8
    step: 1
    format: px
  
  - id: callout-padding
    title: Internal Padding
    type: variable-number
    default: 16
    min: 0
    max: 48
    step: 2
    format: px
  
  - id: colors-heading
    title: Color Overrides
    type: heading
    level: 1
  
  - id: callout-info-color
    title: Info Callout Color
    type: variable-color
    format: rgb
    default: '#0ea5e9'
  
  - id: callout-warning-color
    title: Warning Callout Color
    type: variable-color
    format: rgb
    default: '#f59e0b'

*/

/* Apply settings */
body.callout-rounded .callout {
  border-radius: 12px;
}

body.callout-shadows .callout {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

body.brutal .callout {
  border-width: 4px;
  border-radius: 0;
}

body.soft .callout {
  border-radius: 16px;
  background: linear-gradient(135deg,
    rgba(var(--callout-color), 0.1),
    rgba(var(--callout-color), 0.2));
}

.callout {
  border-width: var(--callout-border-width);
  padding: var(--callout-padding);
}

.callout[data-callout="info"] {
  --callout-color: var(--callout-info-color);
}

.callout[data-callout="warning"] {
  --callout-color: var(--callout-warning-color);
}
```

---

## 🔌 Callout Manager Plugin Features

> [!what-this-does]
> The Callout Manager plugin provides a user interface for creating and managing custom callouts without manually editing CSS files.

**Key Features:**
- Visual callout editor with live preview
- Icon browser for Lucide icons
- Color picker for RGB values
- Import/export callout configurations
- Bulk callout management
- Callout templates

**Integration with CSS:**
When using Callout Manager alongside custom CSS, ensure:
1. Plugin-created callouts take precedence (loaded last)
2. Use `!important` in CSS to override plugin styles if needed
3. Check for conflicts between plugin and snippet callout names

```css
/* Override Callout Manager styling if needed */
.callout[data-callout="managed-type"] {
  background-color: transparent !important;
  /* Your custom styles */
}
```

---

## 🎯 Theme Compatibility Considerations

> [!warning]
> Theme-specific CSS variables and conventions can affect callout styling. Always test customizations across different themes.

### Common Theme Variables

```css
/* Accessing theme colors */
.callout {
  /* Background colors */
  background: var(--background-primary);
  background: var(--background-secondary);
  background: var(--background-primary-alt);
  background: var(--background-modifier-border);
  
  /* Text colors */
  color: var(--text-normal);
  color: var(--text-muted);
  color: var(--text-faint);
  
  /* Accent colors */
  border-color: var(--interactive-accent);
  color: var(--interactive-accent-hover);
  
  /* Radius */
  border-radius: var(--radius-s);
  border-radius: var(--radius-m);
  border-radius: var(--radius-l);
  
  /* Fonts */
  font-family: var(--font-text);
  font-family: var(--font-interface);
  font-family: var(--font-monospace);
}
```

### Dark/Light Mode Handling

```css
/* Light mode specific */
.theme-light .callout {
  outline: 1px solid color-mix(in srgb, 
    rgb(var(--callout-color), 0.35) 90%, black);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
}

/* Dark mode specific */
.theme-dark .callout {
  outline: 1px solid color-mix(in srgb, 
    rgb(var(--callout-color), 0.35) 90%, white);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Using color scheme media query */
@media (prefers-color-scheme: dark) {
  .callout {
    /* Dark mode adjustments */
  }
}

@media (prefers-color-scheme: light) {
  .callout {
    /* Light mode adjustments */
  }
}
```

---

## 📝 Practical Implementation Examples

> [!example]
> **Complete Custom Callout Snippets**

### Example 1: Gradient Accent Callout

```css
.callout[data-callout="gradient"] {
  --callout-color: 139, 92, 246;
  --callout-icon: lucide-sparkles;
  
  background: linear-gradient(135deg,
    rgba(139, 92, 246, 0.1) 0%,
    rgba(236, 72, 153, 0.1) 100%);
  border: none;
  border-left: 4px solid transparent;
  border-image: linear-gradient(to bottom,
    rgb(139, 92, 246),
    rgb(236, 72, 153)) 1;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.2);
}

.callout[data-callout="gradient"] .callout-title {
  background: linear-gradient(90deg,
    rgb(139, 92, 246),
    rgb(236, 72, 153));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
}
```

### Example 2: Minimal Icon-Only Callout

```css
.callout[data-callout="icon-only"] {
  --callout-color: 59, 130, 246;
  --callout-icon: lucide-info;
  
  padding: 12px;
  background: transparent;
  border: none;
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.callout[data-callout="icon-only"] .callout-title {
  padding: 0;
  background: none;
}

.callout[data-callout="icon-only"] .callout-title-inner {
  display: none;
}

.callout[data-callout="icon-only"] .callout-icon {
  width: 32px;
  height: 32px;
  background: rgb(var(--callout-color));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.callout[data-callout="icon-only"] .callout-icon .svg-icon {
  color: white;
  width: 20px;
  height: 20px;
}
```

### Example 3: Code Block Callout

```css
.callout[data-callout="code-block"] {
  --callout-color: 100, 100, 100;
  --callout-icon: lucide-code-2;
  
  background: var(--background-primary-alt);
  border: 1px solid var(--background-modifier-border);
  border-left: 4px solid rgb(var(--callout-color));
  font-family: var(--font-monospace);
}

.callout[data-callout="code-block"] .callout-content {
  background: rgba(0, 0, 0, 0.3);
  padding: 16px;
  border-radius: 4px;
  overflow-x: auto;
}

.callout[data-callout="code-block"] .callout-content code {
  font-size: 0.9em;
  line-height: 1.5;
}
```

### Example 4: Alert Banner Callout

```css
.callout[data-callout="alert-banner"] {
  --callout-color: 239, 68, 68;
  --callout-icon: lucide-alert-triangle;
  
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(239, 68, 68, 0.95);
  backdrop-filter: blur(8px);
  color: white;
  border: none;
  border-bottom: 3px solid rgb(220, 38, 38);
  border-radius: 0;
  margin: 0 -20px 20px -20px;
  padding: 16px 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.callout[data-callout="alert-banner"] .callout-title {
  color: white;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.callout[data-callout="alert-banner"] .callout-icon .svg-icon {
  color: white;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.7; transform: scale(1.1); }
}
```

### Example 5: Quote Callout

```css
.callout[data-callout="quote"] {
  --callout-color: 156, 163, 175;
  --callout-icon: lucide-quote;
  
  background: transparent;
  border: none;
  border-left: 4px solid rgb(var(--callout-color));
  padding-left: 20px;
  font-style: italic;
}

.callout[data-callout="quote"] .callout-title {
  display: none;
}

.callout[data-callout="quote"] .callout-content {
  font-size: 1.1em;
  line-height: 1.7;
  color: var(--text-muted);
}

.callout[data-callout="quote"] .callout-content::before {
  content: """;
  font-size: 3em;
  line-height: 0;
  color: rgba(var(--callout-color), 0.3);
  position: relative;
  top: 20px;
  left: -10px;
}
```

---

## 🐛 Troubleshooting & Best Practices

> [!helpful-tip]
> **Common Issues and Solutions**

### Issue: Colors Not Applying

**Problem:** RGB colors not displaying correctly

```css
/* ❌ WRONG - These don't work */
--callout-color: #FF5733;
--callout-color: red;
--callout-color: rgb(255, 87, 51);

/* ✅ CORRECT - Only this format works */
--callout-color: 255, 87, 51;
```

### Issue: Icons Not Showing

**Problem:** Custom icon doesn't display

**Solutions:**
1. Verify icon name exists in Lucide version 0.446.0 or earlier
2. Ensure `lucide-` prefix is included
3. Check for typos in icon name

```css
/* Check icon existence */
--callout-icon: lucide-lightbulb; /* ✓ Valid */
--callout-icon: lightbulb; /* ✗ Missing prefix */
--callout-icon: lucide-nonexistent; /* ✗ Invalid icon */
```

### Issue: Styles Not Loading

**Problem:** CSS snippet doesn't take effect

**Checklist:**
1. Snippet file placed in `.obsidian/snippets/` folder
2. Snippet enabled in Settings → Appearance → CSS Snippets
3. Snippet reloaded after editing
4. No syntax errors in CSS
5. Correct selector specificity

```css
/* Increase specificity if needed */
body .callout[data-callout="custom"] { /* More specific */ }
.callout[data-callout="custom"] !important { /* Last resort */ }
```

### Issue: Callout Manager Conflicts

**Problem:** Plugin overrides custom CSS

**Solution:** Use `!important` or increase specificity

```css
/* Override plugin styles */
.callout[data-callout="managed-callout"] {
  background-color: transparent !important;
  border: 2px solid rgb(var(--callout-color)) !important;
}
```

### Issue: Metadata Modifiers Not Working

**Problem:** `[!type|modifier]` syntax not recognized

**Solution:** Requires specific CSS to parse metadata

```css
/* Enable metadata parsing */
.callout[data-callout-metadata*="color-blue"] {
  --callout-color: 59, 130, 246;
}

/* Attribute exists check */
.callout[data-callout-metadata] {
  /* Styles for any callout with metadata */
}
```

### Best Practices

> [!core-principle]
> **CSS Organization and Maintenance**

**1. Use CSS Custom Properties for Reusability**
```css
:root {
  --my-brand-color-rgb: 99, 102, 241;
  --my-border-width: 2px;
  --my-border-radius: 8px;
}

.callout[data-callout="branded"] {
  --callout-color: var(--my-brand-color-rgb);
  border-width: var(--my-border-width);
  border-radius: var(--my-border-radius);
}
```

**2. Comment Your Code Extensively**
```css
/* ============================================
   CUSTOM CALLOUT: Project Status
   Purpose: Visual project tracking
   Dependencies: None
   Last Updated: 2025-06-15
   ============================================ */
.callout[data-callout="project-status"] {
  /* Base styling */
}
```

**3. Use Naming Conventions**
```css
/* Prefix custom callouts consistently */
.callout[data-callout="my-warning"] { }
.callout[data-callout="my-success"] { }
.callout[data-callout="my-info"] { }
```

**4. Test Across Themes**
- Enable different themes and check appearance
- Use theme variables when possible for compatibility
- Provide fallbacks for theme-specific properties

**5. Keep Snippets Modular**
- One file per callout family or feature set
- Easy to enable/disable specific customizations
- Reduces conflicts between snippets

**6. Document Requirements**
```css
/*
REQUIREMENTS:
- Obsidian v1.4.0+
- Lucide Icons v0.446.0+
- Optional: Style Settings plugin for UI controls

USAGE:
> [!custom-type] Title
> Content here

VARIANTS:
- custom-type-scrollable (limited height)
- custom-type-wide (full width)
*/
```

---

## 🔗 Related Topics for PKB Expansion

1. **[[CSS Custom Properties (CSS Variables)]]**
   - *Connection*: Foundation for dynamic theming and reusable values in callout customization
   - *Depth Potential*: Deep dive into variable scoping, fallback values, and runtime modification
   - *Knowledge Graph Role*: Core CSS concept linking to all styling practices

2. **[[Lucide Icon System]]**
   - *Connection*: Icon library used by Obsidian for callout icons
   - *Depth Potential*: Complete icon catalog, SVG manipulation, custom icon creation
   - *Knowledge Graph Role*: Visual design resource for UI customization

3. **[[CSS Pseudo-elements (::before, ::after)]]**
   - *Connection*: Advanced decoration and layout techniques demonstrated in callout styling
   - *Depth Potential*: Comprehensive guide to pseudo-element capabilities, content generation, positioning
   - *Knowledge Graph Role*: Advanced CSS technique applicable beyond callouts

4. **[[Obsidian Plugin Development - Callout API]]**
   - *Connection*: Programmatic callout creation and manipulation beyond CSS
   - *Depth Potential*: Plugin architecture, API methods, dynamic callout registration
   - *Knowledge Graph Role*: Bridge between CSS styling and JavaScript functionality

```
<thinking>
This is a comprehensive request for a Reference Note about Obsidian callout customization. Let me break down what's needed:

**REQUEST CLASSIFICATION:**
- Type: comprehensive_note (Reference Note)
- Scope: reference (exhaustive technical resource)
- Research Required: YES - Need to verify current Obsidian callout syntax, CSS customization options, and Style Settings plugin capabilities

**USER CONTEXT:**
- Building custom Obsidian visualization system
- Has advanced plugins active (Callout Manager, Style Settings are key here)
- Needs complete taxonomy for active reference during customization work
- Wants findability and ease of use prioritized

**RESEARCH NEEDS:**
1. Core Obsidian callout syntax and native features
2. CSS selectors and properties for callout customization
3. Style Settings plugin syntax and capabilities
4. Callout Manager plugin features
5. Advanced customization techniques (collapsible, nested, icons, colors)
6. CSS snippet structure and best practices

Let me search for current, comprehensive information about these topics.

**STRUCTURAL PLANNING:**

I. Metadata (tags, aliases)
II. Overview & Purpose
III. Core Callout Anatomy (structure, syntax)
IV. Native Callout Features (types, modifiers, folding)
V. CSS Customization Fundamentals
   - Selectors
   - Properties
   - Targeting specific elements
VI. Complete CSS Property Reference
   - Colors & Backgrounds
   - Typography
   - Spacing & Layout
   - Borders & Shadows
   - Icons & Pseudo-elements
VII. Style Settings Plugin Integration
   - YAML syntax
   - Variable system
   - Class-based customization
VIII. Callout Manager Plugin Features
IX. Advanced Techniques
   - Custom callout types
   - Nested callouts
   - Responsive design
   - Theme compatibility
X. Practical Examples & Snippets
XI. Troubleshooting & Best Practices
XII. Expansion Topics

**WIKI-LINK OPPORTUNITIES:**
- [[Obsidian]]
- [[CSS]]
- [[YAML]]
- [[Style Settings Plugin]]
- [[Callout Manager Plugin]]
- [[CSS Snippets]]
- [[Markdown]]
- [[CSS Selectors]]
- [[CSS Variables]]
- [[Pseudo-elements]]
- [[Flexbox]]
- [[Color Theory]]
- [[Typography]]
- [[User Interface Design]]
- [[Theme Development]]

**CALLOUT STRATEGY:**
- [!abstract] - Overview
- [!core-principle] - Fundamental concepts
- [!definition] - Technical terminology
- [!methodology-and-sources] - How things work
- [!example] - Code examples
- [!helpful-tip] - Best practices
- [!warning] - Common pitfalls
- [!important-links] - Quick reference tables
- [!what-this-does] - Feature explanations
- [!quick-reference] - Syntax summaries

**METADATA PLANNING:**
Tags: #obsidian #css #callout-customization #style-settings #reference-note #technical-guide
Aliases: [Callout CSS Reference, Obsidian Callout Styling, Callout Customization Guide, Callout CSS Taxonomy]

Now I need to search for comprehensive, current information about Obsidian callout customization.
</thinking>Now I have comprehensive research material. Let me create the exhaustive reference note.
```