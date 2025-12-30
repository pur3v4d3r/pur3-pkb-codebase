# 🎨 **UNIFIED CALLOUT SYSTEM v3.0**
## Complete Implementation & Architecture Guide

---

## 📋 **TABLE OF CONTENTS**

1. [System Overview](#system-overview)
2. [Architecture Design](#architecture-design)
3. [Migration from 15-Snippet System](#migration-guide)
4. [Quick Start Guide](#quick-start)
5. [Style Variant Reference](#style-variants)
6. [Customization Guide](#customization)
7. [Callout Type Registry](#callout-registry)
8. [Advanced Techniques](#advanced)
9. [Troubleshooting](#troubleshooting)
10. [Performance Optimization](#performance)

---

## 🎯 **SYSTEM OVERVIEW** {#system-overview}

[**System-Purpose**:: The Unified Callout System consolidates 15+ individual CSS snippet files into a single, modular architecture that provides semantic callout styling with switchable visual variants, eliminating the need for manual snippet toggling.]

### **Key Features**

| Feature | Description | Benefit |
|---------|-------------|---------|
| **Single-File Architecture** | All functionality in one CSS file | No snippet management overhead |
| **5 Visual Variants** | Switchable via body classes | Instant theme changes without reloading |
| **60+ Semantic Types** | Pre-configured callout types | Consistent knowledge classification |
| **Design Token System** | Centralized CSS variables | Easy global customization |
| **Animation Library** | Reusable keyframes | Smooth, performant effects |
| **Zero Dependencies** | Pure CSS implementation | Maximum compatibility |

### **What Problems This Solves**

> [!key-claim] Primary Value Proposition
> 
> **BEFORE**: Maintaining 15+ snippet files required:
> - Manual toggling of 3-5 snippets to change visual style
> - Duplicate code across multiple files
> - Complex debugging when styles conflicted
> - Obsidian reload required for style changes
> - Fragile system prone to breaking with updates
> 
> **AFTER**: Single unified system provides:
> - One file to maintain and customize
> - Instant style switching via body class
> - Clear separation of concerns (structure vs. variants)
> - Easier debugging with organized sections
> - Future-proof modular design

---

## 🏗️ **ARCHITECTURE DESIGN** {#architecture-design}

[**Architectural-Philosophy**:: The system follows a layered architecture pattern where core structure (base callouts) is separated from visual variants (style overrides) and semantic meaning (callout types), enabling independent modification of each layer without affecting others.]

### **System Architecture Diagram**

```
┌─────────────────────────────────────────────────────────────┐
│  unified-callout-system.css                                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📦 SECTION 1: Design Token System                          │
│  ├─ Color Palette (Crimson, Greyscale, Accents)            │
│  ├─ Gradient Definitions                                    │
│  ├─ Structural Parameters (borders, padding, spacing)       │
│  ├─ Shadow & Depth System                                   │
│  └─ Animation Parameters                                    │
│                                                              │
│  🎬 SECTION 2: Animation Keyframe Library                   │
│  ├─ slideInFromLeft                                         │
│  ├─ fadeInScale                                             │
│  ├─ glowPulse                                               │
│  ├─ shimmer                                                 │
│  └─ iconBounce                                              │
│                                                              │
│  🏗️ SECTION 3: Base Callout Architecture                    │
│  ├─ Core structural styles (.callout)                       │
│  ├─ Hover states and transitions                            │
│  ├─ Before/after pseudo-elements (glow lines)               │
│  └─ Elevation and shadow base                               │
│                                                              │
│  📝 SECTION 4: Title & Content Styling                      │
│  ├─ Typography (.callout-title)                             │
│  ├─ Content area (.callout-content)                         │
│  ├─ Text formatting (bold, italic)                          │
│  └─ Icon styling (.callout-icon)                            │
│                                                              │
│  🎨 SECTION 5: Callout Type Registry                        │
│  ├─ Crimson Family (60+ types)                              │
│  ├─ Orange Accent Types                                     │
│  ├─ Greyscale Types                                         │
│  └─ Special Effect Types (DNA, Diamond, Ember, etc.)        │
│                                                              │
│  🎭 SECTION 6: Style Variant Overrides                      │
│  ├─ body.callout-variant-minimal                            │
│  ├─ body.callout-variant-neon                               │
│  ├─ body.callout-variant-outlined                           │
│  ├─ body.callout-variant-compact                            │
│  └─ body.callout-variant-raised                             │
│                                                              │
│  🔧 SECTION 7: Utility Overrides                            │
│  ├─ Nested callout handling                                 │
│  ├─ Foldable callout support                                │
│  └─ Print styles                                            │
│                                                              │
│  📝 SECTION 8: Configuration Guide                          │
│  └─ Inline documentation and usage examples                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘

LAYER INTERACTION:
──────────────────────────────────────────────────────────────
Design Tokens (SECTION 1)
    ↓ Variables consumed by ↓
Base Architecture (SECTIONS 2-4)
    ↓ Provides foundation for ↓
Callout Type Registry (SECTION 5)
    ↓ Can be overridden by ↓
Style Variant Overrides (SECTION 6)
    ↓ Final tweaks in ↓
Utility Overrides (SECTION 7)
```

### **CSS Specificity Hierarchy**

[**Specificity-Strategy**:: The system uses CSS specificity strategically to ensure variant overrides can cleanly replace base styles without !important flags, following this hierarchy: Base styles → Type-specific styles → Variant overrides → Utility overrides.]

```css
/* Specificity Level 1: Base (0,0,1) */
.callout { /* base styles */ }

/* Specificity Level 2: Type-Specific (0,0,2) */
.callout[data-callout="key-claim"] { /* type color assignment */ }

/* Specificity Level 3: Variant Override (0,0,2) */
body.callout-variant-minimal .callout { /* variant override */ }

/* Specificity Level 4: Special Effects (0,0,3) */
body.callout-variant-neon .callout:hover .callout-title { /* detailed variant */ }
```

**KEY INSIGHT**: [**No-Important-Philosophy**:: The architecture avoids `!important` flags (except in design tokens inherited from original system) by carefully structuring specificity, making the codebase easier to maintain and override without escalating specificity wars.]

---

## 🚀 **MIGRATION FROM 15-SNIPPET SYSTEM** {#migration-guide}

[**Migration-Complexity**:: Zero-risk migration requiring only snippet replacement and optional body class configuration - all existing callouts in notes will render correctly without any markdown changes.]

### **Step 1: Backup Current Snippets**

> [!warning] Pre-Migration Safety
> 
> Before proceeding, create a backup of your `.obsidian/snippets/` folder:
> 
> ```bash
> # Navigate to vault root
> cd /path/to/your/vault
> 
> # Create backup
> cp -r .obsidian/snippets .obsidian/snippets-backup-$(date +%Y%m%d)
> ```

### **Step 2: Disable Old Snippets**

In **Obsidian Settings → Appearance → CSS snippets**:

1. **Disable** all callout-related snippets:
   - ✅ Turn OFF: `00-custom-callout.css`
   - ✅ Turn OFF: `callout-icon.css`
   - ✅ Turn OFF: `callout-mod-minimal.css`
   - ✅ Turn OFF: `callout-mod-neon.css`
   - ✅ Turn OFF: `callout-mod-01-outlined-minimal.css`
   - ✅ Turn OFF: `callout-mod-04-compact-dense.css`
   - ✅ Turn OFF: All other `callout-mod-*.css` files

2. **Do NOT delete** these files yet (keep as backup)

### **Step 3: Install Unified System**

1. Copy `unified-callout-system.css` to `.obsidian/snippets/`
2. In **Obsidian Settings → Appearance → CSS snippets**:
   - Click the refresh icon 🔄 to detect new snippet
   - Enable `unified-callout-system.css`

### **Step 4: Choose Visual Variant (Optional)**

If you were using a modifier snippet before (e.g., `callout-mod-minimal.css`), apply the equivalent body class:

| Old Snippet | New Body Class |
|-------------|---------------|
| `callout-mod-minimal.css` | `callout-variant-minimal` |
| `callout-mod-neon.css` | `callout-variant-neon` |
| `callout-mod-01-outlined-minimal.css` | `callout-variant-outlined` |
| `callout-mod-04-compact-dense.css` | `callout-variant-compact` |
| `callout-mod-14-raised-3d.css` | `callout-variant-raised` |

**How to Apply Body Class**:

> [!methodology-and-sources] Body Class Configuration Methods
> 
> **METHOD 1: Style Settings Plugin** (Recommended)
> 1. Install the **Style Settings** plugin
> 2. Add this to the unified snippet at the bottom:
> ```css
> /* @settings
> name: Callout Style Variants
> id: callout-variants
> settings:
>   -
>     id: variant-selector
>     title: Visual Style
>     type: class-select
>     options:
>       - 
>         label: Default (Rich Backgrounds)
>         value: ""
>       -
>         label: Minimal (Transparent)
>         value: callout-variant-minimal
>       -
>         label: Neon (Intense Glow)
>         value: callout-variant-neon
>       -
>         label: Outlined (Clean Borders)
>         value: callout-variant-outlined
>       -
>         label: Compact (Dense Layout)
>         value: callout-variant-compact
>       -
>         label: Raised (3D Depth)
>         value: callout-variant-raised
> */
> ```
> 
> **METHOD 2: Manual CSS** (No plugin required)
> Add to your `snippets/body-class.css`:
> ```css
> body {
>   /* Choose ONE variant - comment out others */
>   /* Default: no class needed */
> }
> 
> /* Uncomment to enable variant: */
> /* body { @extend .callout-variant-minimal; } */
> /* body { @extend .callout-variant-neon; } */
> /* body { @extend .callout-variant-outlined; } */
> /* body { @extend .callout-variant-compact; } */
> /* body { @extend .callout-variant-raised; } */
> ```
> 
> **METHOD 3: Theme CSS** (For theme developers)
> In your theme's CSS, add:
> ```css
> body.theme-dark {
>   /* Apply variant based on theme mode */
> }
> body.theme-dark.callout-variant-neon {
>   /* Variant active in dark mode */
> }
> ```

### **Step 5: Verification**

1. Open a note with existing callouts
2. Verify all callouts render correctly
3. Test hover effects work
4. Check that icons appear properly

### **Step 6: Cleanup (Optional)**

After confirming everything works for 7 days:

```bash
# Remove old snippet backups (be absolutely certain first!)
rm .obsidian/snippets/00-custom-callout.css
rm .obsidian/snippets/callout-mod-*.css
```

### **Migration Troubleshooting**

| Issue | Cause | Solution |
|-------|-------|----------|
| Callouts have no color | Snippet not enabled | Enable in Settings → CSS snippets |
| Colors look wrong | Old snippets still active | Disable all old callout snippets |
| Hover doesn't work | CSS conflict | Disable other callout-related snippets |
| Animations missing | Variant override too aggressive | Remove variant body class temporarily |

---

## ⚡ **QUICK START GUIDE** {#quick-start}

[**Quick-Start-Objective**:: Get from zero to functional unified callout system in under 3 minutes.]

### **3-Minute Setup**

```markdown
1. ✅ Copy unified-callout-system.css to .obsidian/snippets/
   ⏱️ 30 seconds

2. ✅ Enable snippet in Settings → CSS snippets
   ⏱️ 30 seconds

3. ✅ Test in a note:
   > [!key-claim] Test Callout
   > This should render with crimson accent
   ⏱️ 60 seconds

4. ✅ (Optional) Apply style variant body class
   ⏱️ 60 seconds

TOTAL TIME: 3 minutes
```

### **First Callout Example**

```markdown
> [!definition] Cognitive Load Theory
> **Cognitive Load Theory** (CLT) is a [[Cognitive-Psychology]] framework
> positing that instructional design effectiveness is fundamentally
> constrained by [[Working-Memory]] capacity limitations.
>
> [**Core-Principle**:: Instruction should manage intrinsic, extraneous,
> and germane cognitive load to optimize learning.]
```

**Renders as**:
- Crimson accent color (left border + title background)
- Smooth hover elevation
- Icon next to title
- Rich formatting for bold/links
- Glow effect on hover

---

## 🎨 **STYLE VARIANT REFERENCE** {#style-variants}

[**Variant-Design-Philosophy**:: Each variant serves a specific use case and aesthetic preference, from minimal distraction to maximum visual impact, without requiring CSS knowledge to switch between them.]

### **Variant 1: DEFAULT** (No Body Class)

**Visual Characteristics**:
- Rich semi-transparent backgrounds
- Subtle gradient overlays
- Glow effects on hover
- Moderate visual weight

**Best For**:
- General note-taking
- Mixed content types
- Balanced aesthetics
- Professional appearance

**CSS**: *No body class required - this is the base styling*

---

### **Variant 2: MINIMAL** (`callout-variant-minimal`)

**Visual Characteristics**:
- Fully transparent backgrounds
- Border-only design (1px outline + 3px left accent)
- No shadows or glows
- Minimal visual weight

**Best For**:
- Distraction-free reading
- Print-optimized notes
- Low-contrast preferences
- Minimalist aesthetic

**Example**:
```markdown
<!-- Apply body class: callout-variant-minimal -->

> [!key-claim] Minimal Callout
> Clean borders, no background noise
```

**Appearance**:
- Thin border outline
- Transparent interior
- Accent color on left edge only
- Subtle hover: slight background tint

---

### **Variant 3: NEON** (`callout-variant-neon`)

**Visual Characteristics**:
- Intense glow effects (3-layer shadow)
- Dark backgrounds (rgba(10,10,10,0.85))
- Pulsing animation
- Maximum visual impact

**Best For**:
- Cyberpunk aesthetic
- Dark theme users
- Highlighting critical content
- Visual emphasis

**Example**:
```markdown
<!-- Apply body class: callout-variant-neon -->

> [!warning] Critical Warning
> Intense glow draws maximum attention
```

**Appearance**:
- Multi-layer glow (10px, 20px, 40px spread)
- Pulsing animation (3s cycle)
- Text shadow on title
- Cyberpunk terminal aesthetic

---

### **Variant 4: OUTLINED** (`callout-variant-outlined`)

**Visual Characteristics**:
- Full border outline (2px all sides)
- Transparent backgrounds
- Clean professional look
- Medium visual weight

**Best For**:
- Business/professional notes
- Clean corporate aesthetic
- Print-friendly appearance
- GitHub-style callouts

**Example**:
```markdown
<!-- Apply body class: callout-variant-outlined -->

> [!methodology-and-sources] Research Method
> Professional outlined appearance
```

**Appearance**:
- 2px border on all sides
- 4px left accent border
- Transparent interior with slight tint on hover
- Clean, structured look

---

### **Variant 5: COMPACT** (`callout-variant-compact`)

**Visual Characteristics**:
- Reduced padding (6px title, 8px content)
- Smaller fonts (0.85em title, 0.92em content)
- Tighter line height (1.5)
- Minimal vertical spacing (0.3em margins)

**Best For**:
- Information-dense documents
- Reference materials
- Academic papers
- Maximum content per screen

**Example**:
```markdown
<!-- Apply body class: callout-variant-compact -->

> [!definition] Term 1
> Brief definition

> [!definition] Term 2
> Brief definition

> [!definition] Term 3
> Brief definition
```

**Appearance**:
- 3 callouts fit where 2 would normally
- Smaller icons (18px vs 24px)
- Tighter spacing throughout
- Ideal for glossaries/references

---

### **Variant 6: RAISED** (`callout-variant-raised`)

**Visual Characteristics**:
- Deep multi-layer shadows (8px, 16px, 32px)
- Elevated appearance (translateY(-4px))
- Dark gradient background
- Strong 3D depth effect

**Best For**:
- Creating visual hierarchy
- Important standalone callouts
- Card-based layouts
- Modal-style emphasis

**Example**:
```markdown
<!-- Apply body class: callout-variant-raised -->

> [!diamond] Premium Content
> Floats above page with strong shadow
```

**Appearance**:
- Appears to float above the page
- Strong shadow creates depth
- Inset highlight at top edge
- Dramatic hover lift (translateY(-6px))

---

### **Variant Comparison Table**

| Variant | Visual Weight | Best Use | Shadow | Background | Animation |
|---------|--------------|----------|--------|------------|-----------|
| **Default** | Medium | General notes | Moderate | Semi-transparent | Smooth |
| **Minimal** | Low | Distraction-free | None | Transparent | Minimal |
| **Neon** | Very High | Emphasis | Intense glow | Dark opaque | Pulsing |
| **Outlined** | Medium-Low | Professional | Light | Transparent | Subtle |
| **Compact** | Low | Dense info | Moderate | Semi-transparent | Smooth |
| **Raised** | High | Hierarchy | Deep 3D | Gradient | Dramatic |

---

## 🛠️ **CUSTOMIZATION GUIDE** {#customization}

[**Customization-Philosophy**:: All visual parameters are exposed as CSS custom properties (variables) in the `:root` selector, enabling global theming without touching individual selectors - change one variable to update the entire system.]

### **Primary Customization Points**

#### **1. Color Palette**

Located at the top of the file in `:root {}`:

```css
:root {
  /* Change primary accent from Crimson to your brand color */
  --callout-crimson: 229, 0, 0;  /* RGB format, no rgb() wrapper */
  
  /* Example: Change to Blue */
  --callout-crimson: 41, 128, 185;  /* #2980b9 */
  
  /* Example: Change to Purple */
  --callout-crimson: 142, 68, 173;  /* #8e44ad */
  
  /* Example: Change to Green */
  --callout-crimson: 39, 174, 96;   /* #27ae60 */
}
```

[**Color-Format-Requirement**:: CSS custom properties for colors use comma-separated RGB values (e.g., `229, 0, 0`) rather than the rgb() function because they need to be used with rgba() for opacity manipulation throughout the system.]

**Complete Color Customization Example**:

```css
:root {
  /* Brand Color System - Replace Crimson with Teal */
  --callout-crimson: 23, 162, 184;        /* #17a2b8 - Primary Teal */
  --callout-crimson-bright: 32, 201, 151; /* #20c997 - Bright Teal */
  --callout-crimson-dim: 17, 122, 139;    /* #117a8b - Dim Teal */
  --callout-crimson-dark: 13, 97, 110;    /* #0d616e - Dark Teal */
  --callout-crimson-ultra: 10, 73, 83;    /* #0a4953 - Ultra Dim */
  --callout-crimson-soft: 77, 192, 181;   /* #4dc0b5 - Soft Teal */
  
  /* Keep greyscale the same or adjust for contrast */
  --callout-grey-high: 224, 224, 224;
  --callout-grey-medium: 163, 163, 163;
  --callout-grey-low: 122, 122, 122;
  
  /* Accent color for special callouts */
  --callout-orange: 255, 159, 67;  /* #ff9f43 - Warm Orange */
}
```

#### **2. Visual Effects Intensity**

```css
:root {
  /* Glow Intensity (0-1 scale) */
  --glow-intensity: 0.3;  /* Default */
  --glow-intensity: 0.1;  /* Subtle */
  --glow-intensity: 0.6;  /* Intense */
  
  /* Shadow Depth */
  --shadow-depth-1: 0 2px 8px rgba(0, 0, 0, 0.3);   /* Light */
  --shadow-depth-2: 0 4px 16px rgba(0, 0, 0, 0.4);  /* Medium */
  --shadow-depth-3: 0 8px 32px rgba(0, 0, 0, 0.5);  /* Deep */
  
  /* Increase shadow depth example: */
  --shadow-depth-2: 0 6px 24px rgba(0, 0, 0, 0.6);  /* Deeper */
}
```

#### **3. Spacing & Layout**

```css
:root {
  /* Padding */
  --callout-padding: 14px 10px;       /* Content area */
  --callout-title-padding: 1px 18px;  /* Title area */
  
  /* Increase padding example: */
  --callout-padding: 20px 16px;
  --callout-title-padding: 12px 24px;
  
  /* Margin */
  --callout-margin: 0.5em 0;  /* Vertical spacing between callouts */
  
  /* Tighter spacing: */
  --callout-margin: 0.25em 0;
  
  /* Looser spacing: */
  --callout-margin: 1em 0;
  
  /* Border Radius */
  --callout-border-radius: 16px;  /* Rounded corners */
  
  /* Sharp corners: */
  --callout-border-radius: 4px;
  
  /* Very rounded: */
  --callout-border-radius: 24px;
}
```

#### **4. Animation Speed**

```css
:root {
  /* Animation Timing */
  --animation-speed-fast: 0.2s;    /* Quick transitions */
  --animation-speed-normal: 0.35s; /* Standard speed */
  --animation-speed-slow: 0.5s;    /* Leisurely pace */
  
  /* Disable animations completely: */
  --animation-speed-fast: 0s;
  --animation-speed-normal: 0s;
  --animation-speed-slow: 0s;
  
  /* Speed up everything: */
  --animation-speed-fast: 0.1s;
  --animation-speed-normal: 0.2s;
  --animation-speed-slow: 0.3s;
}
```

#### **5. Border Styling**

```css
:root {
  /* Border Width */
  --callout-border-width-thin: 1px;
  --callout-border-width-medium: 2px;
  --callout-border-width-thick: 4px;  /* Left accent border */
  
  /* Make accent border thicker: */
  --callout-border-width-thick: 6px;
  
  /* Make it thinner: */
  --callout-border-width-thick: 2px;
}
```

---

### **Advanced Customization Examples**

#### **Example 1: High-Contrast Mode**

```css
/* Add to bottom of unified-callout-system.css */

:root {
  /* Increase contrast everywhere */
  --callout-title-bg-opacity: 0.25;    /* Default: 0.15 */
  --callout-content-bg-opacity: 0.10;  /* Default: 0.05 */
  --callout-border-opacity: 0.9;       /* Default: 0.6 */
  
  /* Stronger shadows */
  --shadow-depth-1: 0 3px 12px rgba(0, 0, 0, 0.5);
  --shadow-depth-2: 0 6px 20px rgba(0, 0, 0, 0.6);
  
  /* More intense glow */
  --glow-intensity: 0.5;
}
```

#### **Example 2: Monochrome Theme**

```css
/* Pure grayscale - no color */

:root {
  /* Replace all colors with grey */
  --callout-crimson: 180, 180, 180;        /* Medium grey */
  --callout-crimson-bright: 200, 200, 200; /* Light grey */
  --callout-crimson-dim: 160, 160, 160;    /* Dim grey */
  --callout-crimson-dark: 140, 140, 140;   /* Dark grey */
  --callout-orange: 180, 180, 180;         /* Also grey */
}

.callout-content strong,
.callout-content b {
  color: #cccccc !important;  /* Grey instead of crimson for bold */
}
```

#### **Example 3: Pastel Soft Theme**

```css
/* Soft, pastel aesthetic */

:root {
  /* Pastel pink */
  --callout-crimson: 255, 182, 193;        /* Light pink */
  --callout-crimson-bright: 255, 218, 224; /* Pale pink */
  --callout-crimson-dim: 219, 112, 147;    /* Palevioletred */
  
  /* Softer shadows */
  --shadow-depth-1: 0 2px 8px rgba(0, 0, 0, 0.1);
  --shadow-depth-2: 0 4px 12px rgba(0, 0, 0, 0.15);
  
  /* Gentler glow */
  --glow-intensity: 0.15;
  
  /* More rounded */
  --callout-border-radius: 20px;
}
```

#### **Example 4: Brutalist/Sharp Theme**

```css
/* Angular, no-nonsense design */

:root {
  /* Sharp corners */
  --callout-border-radius: 0px;
  --callout-inner-radius: 0px;
  
  /* Thick borders */
  --callout-border-width-thick: 6px;
  
  /* No animations */
  --animation-speed-normal: 0s;
  --animation-speed-fast: 0s;
  
  /* No glow */
  --glow-intensity: 0;
}

.callout {
  box-shadow: none !important;  /* Remove all shadows */
}

.callout:hover {
  transform: none !important;  /* No hover elevation */
}
```

---

### **Creating Custom Callout Types**

Add new semantic types in **SECTION 5**:

```css
/* Add to SECTION 5: CALLOUT TYPE REGISTRY */

/* ────────────────────────────────────────────────────────────────
   🔬 RESEARCH FAMILY - Custom types for research workflow
   ──────────────────────────────────────────────────────────────── */

.callout[data-callout="hypothesis"],
.callout[data-callout="research-question"],
.callout[data-callout="methodology"] {
  --callout-color: var(--callout-orange);  /* Use orange accent */
}

.callout[data-callout="hypothesis"]::before {
  content: '🔬';  /* Add emoji before title */
  position: absolute;
  top: -10px;
  right: 20px;
  font-size: 1.5em;
  opacity: 0.6;
}

/* ────────────────────────────────────────────────────────────────
   💰 FINANCE FAMILY - Custom types for financial notes
   ──────────────────────────────────────────────────────────────── */

.callout[data-callout="income"],
.callout[data-callout="expense"],
.callout[data-callout="investment"] {
  --callout-color: 39, 174, 96;  /* Green for finance */
}

.callout[data-callout="expense"] {
  --callout-color: 231, 76, 60;  /* Red for expenses */
}
```

**Usage**:
```markdown
> [!hypothesis] Primary Research Hypothesis
> Increased cognitive load during encoding reduces subsequent retrieval accuracy

> [!expense] Monthly Costs
> - Rent: $1200
> - Utilities: $150
```

---

### **Creating Custom Variants**

Add your own style variant in **SECTION 6**:

```css
/* ────────────────────────────────────────────────────────────────
   VARIANT 6: TERMINAL - Retro command-line aesthetic
   Usage: Add class "callout-variant-terminal" to body
   ──────────────────────────────────────────────────────────────── */

body.callout-variant-terminal .callout {
  background: rgba(0, 0, 0, 0.95);
  border: 2px solid rgba(0, 255, 0, 0.5);  /* Green terminal color */
  border-radius: 0;  /* Sharp corners */
  font-family: 'Courier New', monospace;
  box-shadow: 
    0 0 10px rgba(0, 255, 0, 0.3),
    inset 0 0 100px rgba(0, 0, 0, 0.8);
}

body.callout-variant-terminal .callout-title {
  background: rgba(0, 255, 0, 0.1);
  color: rgb(0, 255, 0);
  font-family: 'Courier New', monospace;
  text-transform: uppercase;
  letter-spacing: 2px;
  border-bottom: 1px solid rgba(0, 255, 0, 0.5);
}

body.callout-variant-terminal .callout-content {
  background: transparent;
  color: rgb(0, 255, 0);
  font-family: 'Courier New', monospace;
}

body.callout-variant-terminal .callout::before {
  content: '> ';
  position: absolute;
  left: 8px;
  top: 8px;
  color: rgb(0, 255, 0);
  font-family: 'Courier New', monospace;
}
```

**Result**: Retro terminal-style callouts with green monospace text

---

## 📚 **CALLOUT TYPE REGISTRY** {#callout-registry}

[**Type-Registry-Purpose**:: The callout type registry provides a semantic vocabulary for knowledge classification, with each type having a predefined color assignment and optional visual treatment, enabling consistent categorization across your entire PKB.]

### **Complete Type List by Category**

#### **💎 PRIMARY KNOWLEDGE (Crimson)**

| Type | Purpose | Usage Example |
|------|---------|---------------|
| `key-claim` | Central arguments requiring support | `> [!key-claim] Core Thesis` |
| `evidence` | Research findings, empirical data | `> [!evidence] Study Results (n=1000)` |
| `insight` | Breakthrough realizations | `> [!insight] Novel Connection` |
| `principle-point` | Fundamental rules or laws | `> [!principle-point] First Principle` |
| `definition` | Formal concept definitions | `> [!definition] Cognitive Load` |
| `what-this-does` | Functional explanations | `> [!what-this-does] Code Purpose` |
| `methodology-and-sources` | Research methods | `> [!methodology-and-sources] Approach` |
| `overview` | High-level summaries | `> [!overview] Chapter Summary` |
| `connections-and-links` | Network of related ideas | `> [!connections-and-links] Related Concepts` |

#### **🔴 WARNINGS & CRITICAL (Deep Crimson)**

| Type | Purpose | Usage Example |
|------|---------|---------------|
| `warning` | Cautionary information | `> [!warning] Deprecated Method` |
| `caution` | Potential issues | `> [!caution] Breaking Changes` |
| `alert` | Immediate attention required | `> [!alert] Security Vulnerability` |
| `critical` | Mission-critical content | `> [!critical] Production Blocker` |
| `danger` | High-risk situations | `> [!danger] Data Loss Risk` |

#### **🟠 EXPERIMENTAL (Orange Accent)**

| Type | Purpose | Usage Example |
|------|---------|---------------|
| `experiment` | Testing and exploration | `> [!experiment] A/B Test Results` |
| `test` | Validation procedures | `> [!test] Unit Test Coverage` |
| `lab` | Laboratory or sandbox work | `> [!lab] Proof of Concept` |
| `stage` | Presentations and demos | `> [!stage] Demo Workflow` |
| `demo` | Demonstration content | `> [!demo] Feature Showcase` |
| `presentation` | Public presentation notes | `> [!presentation] Slide Deck` |

#### **⚪ NEUTRAL SUPPORT (Greyscale)**

| Type | Purpose | Usage Example |
|------|---------|---------------|
| `note` | General annotations | `> [!note] Additional Context` |
| `info` | Informational content | `> [!info] Background Information` |
| `context` | Contextual background | `> [!context] Historical Setting` |
| `background` | Supporting details | `> [!background] Prior Art` |
| `random` | Serendipitous thoughts | `> [!random] Tangential Idea` |
| `tangent` | Off-topic explorations | `> [!tangent] Related Curiosity` |

#### **✨ SPECIAL EFFECTS (Custom Treatments)**

| Type | Visual Effect | Usage Example |
|------|---------------|---------------|
| `dna` | Shimmer animation | `> [!dna] Fundamental Concept` |
| `diamond` | Enhanced glow | `> [!diamond] Premium Content` |
| `ember` | Pulsing glow | `> [!ember] Active Project` |
| `raised` | 3D elevation | `> [!raised] Emphasized Block` |
| `pin` | Visual pin icon | `> [!pin] Bookmarked Reference` |
| `bullseye` | Concentric rings | `> [!bullseye] Precision Target` |
| `action` | Heavy left border | `> [!action] Next Steps` |
| `counter-argument` | Dashed border | `> [!counter-argument] Objection` |

### **Usage Pattern Examples**

```markdown
# 📝 Research Note Structure

> [!overview] Document Overview
> This note analyzes [[Cognitive Load Theory]] applications in
> [[Personal Knowledge Management]] systems.

> [!key-claim] Primary Argument
> Effective PKM design requires deliberate [[Cognitive-Load]] management
> across three dimensions: intrinsic, extraneous, and germane.
>
> [**Supporting-Evidence**:: Sweller et al. (2011) meta-analysis of
> 150 studies demonstrates consistent CLT effects across domains.]

> [!evidence] Meta-Analysis Results
> **Study**: Sweller, J., Ayres, P., & Kalyuga, S. (2011)
> **Sample**: 150 controlled experiments (N=12,847)
> **Finding**: Medium to large effect sizes (d=0.68) for CLT-based
> interventions across all tested domains.

> [!methodology-and-sources] Research Approach
> - **Database**: PsycINFO, ERIC, Google Scholar
> - **Search Terms**: "cognitive load" + "instructional design"
> - **Inclusion Criteria**: Peer-reviewed, empirical, published 2000-2024
> - **Analysis Method**: [[Meta-Analysis]] with random effects model

> [!warning] Methodological Limitation
> Publication bias analysis (Egger's test) suggests small-study effects
> may inflate effect size estimates by 15-20%.

> [!counter-argument] Alternative Perspective
> **Kirschner et al. (2018)** argue CLT overemphasizes working memory
> constraints while undervaluing long-term memory's compensatory role
> in expert performance.

> [!insight] Novel Connection
> PKM systems could leverage [[Spaced-Repetition]] algorithms to
> optimize germane load distribution across review sessions, aligning
> with CLT's theoretical framework.

> [!action] Next Steps
> - [ ] Design experiment testing spaced review optimization
> - [ ] Develop CLT metrics for PKM interface evaluation
> - [ ] Interview expert PKM users on perceived cognitive load

> [!connections-and-links] Related Topics
> - [[Working-Memory-Architecture]]
> - [[Schema-Theory]]
> - [[Expertise-Reversal-Effect]]
> - [[Multimedia-Learning-Principles]]
```

---

## 🚀 **ADVANCED TECHNIQUES** {#advanced}

### **Technique 1: Per-Note Variant Switching**

Use inline styles to override global variant for specific notes:

```markdown
---
cssclass: note-specific-neon
---

# Special Note with Neon Callouts

> [!key-claim] Glowing Important Claim
> This note uses neon variant while others use default
```

**CSS** (add to snippet):
```css
/* Note-specific variant override */
.note-specific-neon .callout {
  background: rgba(10, 10, 10, 0.85);
  border: 2px solid rgba(var(--callout-color), 0.6);
  /* ... rest of neon variant styles ... */
}
```

### **Technique 2: Conditional Variants by Folder**

Apply different variants to different vault folders:

```css
/* Research folder uses compact variant */
body[data-path*="/Research/"] .callout {
  margin: 0.3em 0;
  padding: 4px;
  /* ... compact variant styles ... */
}

/* Project folder uses raised variant */
body[data-path*="/Projects/"] .callout {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
  /* ... raised variant styles ... */
}
```

[**Path-Based-Styling-Note**:: The data-path attribute approach requires a plugin or theme that adds path information to the body element - check if your theme supports this before implementing.]

### **Technique 3: Hybrid Variants**

Mix characteristics from multiple variants:

```css
/* Minimal structure + Neon glow */
body.callout-variant-minimal-neon .callout {
  /* Minimal: transparent background */
  background: transparent;
  border: 1px solid rgba(var(--callout-color), 0.25);
  
  /* Neon: intense glow */
  box-shadow:
    0 0 10px rgba(var(--callout-color), 0.3),
    0 0 20px rgba(var(--callout-color), 0.2);
}
```

### **Technique 4: Animation Customization**

Override specific animations for certain types:

```css
/* Disable animation for note/info callouts (reduce distraction) */
.callout[data-callout="note"],
.callout[data-callout="info"] {
  animation: none !important;
  transition: none !important;
}

.callout[data-callout="note"]:hover,
.callout[data-callout="info"]:hover {
  transform: none !important;
}

/* Extra bouncy animation for action callouts */
.callout[data-callout="action"] {
  animation: fadeInScale 0.6s var(--animation-bounce) !important;
}

.callout[data-callout="action"]:hover {
  transform: translateY(-4px) scale(1.02) !important;
}
```

### **Technique 5: Reading Mode vs. Edit Mode Variants**

Different appearance when editing vs. reading:

```css
/* Minimal style while editing (less distraction) */
.markdown-source-view .callout {
  background: transparent;
  border: 1px dashed rgba(var(--callout-color), 0.3);
  box-shadow: none;
}

/* Rich style in reading mode */
.markdown-preview-view .callout {
  /* Full default styling applies */
}
```

### **Technique 6: Mobile-Specific Adjustments**

Optimize for mobile devices:

```css
@media (max-width: 768px) {
  .callout {
    /* Reduce padding on mobile */
    padding: 6px;
  }
  
  .callout-title {
    padding: 8px 12px;
    font-size: 0.9em;
  }
  
  .callout-content {
    padding: 10px 12px;
    font-size: 0.95em;
  }
  
  /* Disable hover effects on touch devices */
  .callout:hover {
    transform: none;
    box-shadow: var(--shadow-depth-1);
  }
}
```

### **Technique 7: Dynamic Color Assignment by Tag**

Assign colors based on note tags:

```css
/* Notes tagged with #project get orange callouts */
body[class*="tag-project"] .callout[data-callout="key-claim"],
body[class*="tag-project"] .callout[data-callout="insight"] {
  --callout-color: var(--callout-orange);
}

/* Notes tagged with #research get grey (neutral) callouts */
body[class*="tag-research"] .callout[data-callout="note"] {
  --callout-color: var(--callout-grey-medium);
}
```

[**Tag-Based-Styling-Note**:: This requires a theme or plugin that adds tag classes to the body element - functionality varies by implementation.]

### **Technique 8: Gradual Complexity Reveal**

Fade in callout content on scroll (requires JS plugin):

```css
/* Default: hidden */
.callout-content {
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.5s, transform 0.5s;
}

/* Visible when scrolled into view (requires .in-view class from JS) */
.callout.in-view .callout-content {
  opacity: 1;
  transform: translateY(0);
}

/* Always show title */
.callout-title {
  opacity: 1;
}
```

### **Technique 9: Semantic Color Coding System**

Extend color palette for specific knowledge types:

```css
:root {
  /* Knowledge type colors */
  --callout-declarative: 52, 152, 219;    /* Blue - facts */
  --callout-procedural: 155, 89, 182;     /* Purple - processes */
  --callout-conceptual: 46, 204, 113;     /* Green - concepts */
  --callout-metacognitive: 241, 196, 15;  /* Yellow - thinking about thinking */
}

.callout[data-callout="fact"],
.callout[data-callout="declarative-knowledge"] {
  --callout-color: var(--callout-declarative);
}

.callout[data-callout="process"],
.callout[data-callout="procedure"],
.callout[data-callout="how-to"] {
  --callout-color: var(--callout-procedural);
}

.callout[data-callout="concept"],
.callout[data-callout="theory"],
.callout[data-callout="model"] {
  --callout-color: var(--callout-conceptual);
}

.callout[data-callout="reflection"],
.callout[data-callout="metacognition"],
.callout[data-callout="learning-strategy"] {
  --callout-color: var(--callout-metacognitive);
}
```

---

## 🔧 **TROUBLESHOOTING** {#troubleshooting}

### **Common Issues & Solutions**

#### **Issue 1: Callouts Have No Color**

**Symptoms**:
- All callouts are grey/default Obsidian styling
- No crimson accents visible

**Diagnosis**:
```markdown
1. Check: Is snippet enabled?
   Settings → Appearance → CSS snippets → unified-callout-system ✅

2. Check: Are old snippets still active?
   Settings → Appearance → CSS snippets → Disable all callout-*.css

3. Check: CSS syntax errors?
   Open DevTools (Ctrl+Shift+I) → Console → Look for CSS errors
```

**Solution**:
- Ensure snippet is enabled and refreshed (click 🔄 icon)
- Disable ALL other callout-related snippets
- Check for syntax errors in custom modifications
- Restart Obsidian

---

#### **Issue 2: Variant Body Class Not Working**

**Symptoms**:
- Applied `callout-variant-minimal` to body
- Still seeing default rich backgrounds

**Diagnosis**:
```markdown
1. Check: Body class actually applied?
   DevTools → Elements → <body> tag → Look for class

2. Check: Specificity conflict?
   DevTools → Select callout → Styles panel → See which rule wins

3. Check: Typo in class name?
   Correct: callout-variant-minimal
   Wrong: callout-minimal, variant-minimal
```

**Solution**:
- Verify body class is actually present in DOM
- Use Style Settings plugin for reliable class application
- Check for conflicting CSS from themes/other snippets
- Ensure variant rules come AFTER base rules in CSS

---

#### **Issue 3: Hover Effects Not Working**

**Symptoms**:
- No elevation on hover
- No glow effect on hover

**Diagnosis**:
```markdown
1. Check: Are animations disabled?
   Settings → Appearance → Reduce animations ❌ (should be off)

2. Check: Animation speed set to 0?
   Look for: --animation-speed-normal: 0s;

3. Check: Transform overridden by theme?
   DevTools → Computed styles → See final transform value
```

**Solution**:
- Enable animations in Obsidian settings
- Check CSS variables for 0s values
- Add `!important` to hover transforms if theme conflict
- Test in default theme to isolate issue

---

#### **Issue 4: Icons Not Appearing**

**Symptoms**:
- Callout titles have no icons
- Only text visible

**Diagnosis**:
```markdown
1. Check: Icon plugin installed?
   Core plugins → File icons ✅

2. Check: Callout type has default icon?
   Some custom types may not have icons assigned

3. Check: CSS hiding icons?
   Look for: .callout-icon { display: none; }
```

**Solution**:
- Obsidian's default callout icons should work automatically
- Custom types may need manual icon assignment
- Check for conflicting CSS hiding icons

---

#### **Issue 5: Performance Issues / Lag**

**Symptoms**:
- Obsidian feels sluggish with many callouts
- Scrolling is janky

**Diagnosis**:
```markdown
1. Check: How many callouts per note?
   >50 callouts may cause performance issues

2. Check: Complex animations on all callouts?
   Shimmer/glowPulse animations are expensive

3. Check: Other plugins conflicting?
   Disable other plugins to test
```

**Solution**:
```css
/* Disable expensive animations */
.callout {
  animation: fadeInScale 0.2s ease !important;  /* Fast, cheap */
}

.callout[data-callout="dna"],
.callout[data-callout="ember"] {
  animation: fadeInScale 0.2s ease !important;  /* Override shimmer/pulse */
}

/* Use will-change for better performance */
.callout {
  will-change: transform, box-shadow;
}

/* Reduce shadow complexity */
:root {
  --shadow-depth-2: 0 2px 8px rgba(0, 0, 0, 0.3);  /* Single shadow */
}
```

---

#### **Issue 6: Neon Variant Too Intense**

**Symptoms**:
- Neon glow causes eye strain
- Too much visual noise

**Solution**:
```css
/* Tune down neon intensity */
body.callout-variant-neon .callout {
  box-shadow:
    0 0 5px rgba(var(--callout-color), 0.2),   /* Reduced from 10px/0.3 */
    0 0 10px rgba(var(--callout-color), 0.1),  /* Reduced from 20px/0.2 */
    0 4px 12px rgba(0, 0, 0, 0.5);
  animation: none;  /* Disable pulsing if too distracting */
}

body.callout-variant-neon .callout-title {
  text-shadow:
    0 0 3px rgba(var(--callout-color), 0.3),   /* Reduced intensity */
    0 2px 4px rgba(0, 0, 0, 0.8);
}
```

---

#### **Issue 7: Text Formatting Not Showing**

**Symptoms**:
- Bold text not crimson colored
- Italic text not styled

**Diagnosis**:
```markdown
1. Check: Theme overriding text formatting?
   DevTools → Inspect bold text → Check color value

2. Check: CSS selector specificity?
   Strong selector may be too weak
```

**Solution**:
```css
/* Increase specificity */
.callout .callout-content strong,
.callout .callout-content b {
  font-weight: 700 !important;
  color: #E50000 !important;
}
```

---

#### **Issue 8: Print Styles Not Working**

**Symptoms**:
- Callouts print with dark backgrounds
- Shadows/glows waste ink

**Solution**:
```css
/* Enhanced print styles */
@media print {
  .callout {
    animation: none !important;
    box-shadow: none !important;
    transform: none !important;
    page-break-inside: avoid !important;
    background: white !important;
    border: 1px solid rgba(var(--callout-color), 0.5) !important;
    border-left: 3px solid rgb(var(--callout-color)) !important;
  }
  
  .callout-title {
    background: rgba(var(--callout-color), 0.1) !important;
    color: rgb(var(--callout-color)) !important;
  }
  
  .callout-content {
    background: white !important;
  }
  
  .callout::before,
  .callout-title::after {
    display: none !important;
  }
}
```

---

### **Debugging Workflow**

```markdown
1. **Isolate the Issue**
   - Disable all other snippets
   - Test in default theme
   - Create minimal test note with single callout

2. **Use DevTools**
   - Open DevTools (Ctrl+Shift+I / Cmd+Option+I)
   - Select Elements tab
   - Click callout element
   - Check Styles panel for:
     * Which rules are applying
     * Which rules are crossed out (overridden)
     * Computed values

3. **Check Console for Errors**
   - Console tab in DevTools
   - Look for CSS syntax errors
   - Look for JavaScript errors from plugins

4. **Test Incrementally**
   - Comment out sections of CSS
   - Test after each change
   - Narrow down problem area

5. **Compare with Defaults**
   - Save your customizations
   - Restore original unified-callout-system.css
   - See if issue persists
   - Gradually re-add customizations
```

---

## ⚡ **PERFORMANCE OPTIMIZATION** {#performance}

[**Performance-Priority**:: Obsidian is a local-first application where CSS performance directly impacts usability - optimize for 60fps scrolling even with 50+ callouts visible simultaneously.]

### **Performance Best Practices**

#### **1. Animation Optimization**

```css
/* ✅ GOOD: Hardware-accelerated properties */
.callout:hover {
  transform: translateY(-2px);  /* GPU-accelerated */
  opacity: 0.95;                /* GPU-accelerated */
}

/* ❌ BAD: CPU-intensive properties */
.callout:hover {
  margin-top: -2px;   /* Triggers layout reflow */
  filter: blur(1px);  /* CPU-intensive */
}

/* ✅ GOOD: will-change hint */
.callout {
  will-change: transform, opacity;
}

/* ⚠️ CAUTION: Don't will-change too many properties */
.callout {
  will-change: transform, opacity, box-shadow, background, border;  /* Too many! */
}
```

**Optimal Animation Properties**:
- ✅ `transform` (translate, scale, rotate)
- ✅ `opacity`
- ⚠️ `box-shadow` (acceptable but heavier)
- ❌ `margin`, `padding`, `width`, `height`
- ❌ `filter` (expensive except `opacity`)

#### **2. Shadow Optimization**

```css
/* ✅ GOOD: Simple shadows */
:root {
  --shadow-depth-1: 0 2px 8px rgba(0, 0, 0, 0.3);  /* Single shadow */
}

/* ⚠️ ACCEPTABLE: Multiple shadows for depth */
:root {
  --shadow-depth-2: 
    0 4px 16px rgba(0, 0, 0, 0.4),
    0 2px 8px rgba(0, 0, 0, 0.2);  /* Two shadows, reasonable */
}

/* ❌ BAD: Excessive shadow layers */
.callout {
  box-shadow:
    0 0 10px rgba(var(--callout-color), 0.3),
    0 0 20px rgba(var(--callout-color), 0.2),
    0 0 40px rgba(var(--callout-color), 0.1),
    0 0 60px rgba(var(--callout-color), 0.05),
    0 4px 12px rgba(0, 0, 0, 0.5);  /* 5 shadows - too much! */
}
```

**Shadow Performance Tips**:
- Limit to 2-3 shadow layers maximum
- Use `box-shadow` sparingly on hover states
- Consider disabling shadows on mobile (they're expensive on mobile GPUs)

#### **3. Selector Optimization**

```css
/* ✅ GOOD: Specific selectors */
.callout[data-callout="key-claim"] {
  --callout-color: var(--callout-crimson);
}

/* ❌ BAD: Overly complex selectors */
body.theme-dark .workspace .markdown-preview-view .callout[data-callout="key-claim"]:not(.is-collapsed) > .callout-title {
  /* Too specific, slows down style calculation */
}

/* ✅ GOOD: Descendant selector */
.callout .callout-title { }

/* ⚠️ ACCEPTABLE: Child selector (slightly slower) */
.callout > .callout-title { }

/* ❌ BAD: Universal selector */
.callout * { }  /* Applies to ALL descendants - slow! */
```

#### **4. Reducing Repaints & Reflows**

```css
/* ✅ GOOD: Avoid layout-triggering properties */
.callout:hover {
  transform: translateY(-2px);  /* Composite layer only */
  box-shadow: var(--shadow-depth-2);  /* Repaint, no reflow */
}

/* ❌ BAD: Triggers layout reflow */
.callout:hover {
  padding: 16px 12px;  /* Changes layout */
  margin: -2px 0;      /* Changes layout */
  width: calc(100% + 4px);  /* Changes layout */
}
```

**Properties that Trigger Layout Reflow** (AVOID on hover):
- `padding`, `margin`, `border-width`
- `width`, `height`, `top`, `left`, `right`, `bottom`
- `display`, `position`, `float`
- `font-size`, `line-height`

**Properties that Only Repaint** (OK on hover):
- `color`, `background-color`
- `box-shadow`
- `border-color`, `outline-color`
- `visibility`

**Properties that Only Composite** (BEST for hover):
- `transform`
- `opacity`

#### **5. Animation Performance**

```css
/* ✅ GOOD: Short, simple animations */
@keyframes fadeInScale {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Duration: 0.2-0.4s is optimal */
.callout {
  animation: fadeInScale 0.35s ease;
}

/* ⚠️ CAUTION: Long animations */
.callout {
  animation: shimmer 8s linear infinite;  /* Continuous GPU usage */
}

/* ❌ BAD: Complex background animations */
@keyframes complexPattern {
  0% { background-position: 0 0; }
  50% { background-position: 100px 50px; }
  100% { background-position: 200px 100px; }
}
/* Animating background-position is expensive! */
```

**Animation Performance Tips**:
- Keep animations under 1 second
- Limit infinite animations to critical elements only
- Use `animation-fill-mode: forwards` to avoid animation loop overhead
- Disable animations on low-performance devices:

```css
@media (prefers-reduced-motion: reduce) {
  .callout {
    animation: none !important;
    transition: none !important;
  }
}
```

#### **6. Mobile Performance**

```css
/* Disable expensive effects on mobile */
@media (max-width: 768px) {
  /* Disable hover effects (touch devices don't hover) */
  .callout:hover {
    transform: none !important;
    box-shadow: var(--shadow-depth-1) !important;  /* Keep base shadow */
  }
  
  /* Disable animations */
  .callout {
    animation: none !important;
  }
  
  /* Simplify shadows */
  :root {
    --shadow-depth-1: 0 2px 4px rgba(0, 0, 0, 0.2);
    --shadow-depth-2: 0 2px 8px rgba(0, 0, 0, 0.3);
  }
  
  /* Disable pseudo-element glows */
  .callout::before,
  .callout-title::after {
    display: none !important;
  }
}
```

#### **7. Reducing CSS File Size**

[**File-Size-Impact**:: Smaller CSS files parse faster and consume less memory - the unified system is already optimized at ~15KB but can be further reduced if needed.]

**Minification** (optional):
```bash
# Install cssnano (Node.js required)
npm install -g cssnano-cli

# Minify the CSS
cssnano unified-callout-system.css unified-callout-system.min.css

# Result: ~15KB → ~8KB (47% reduction)
```

**Manual Size Reduction**:
```css
/* Remove unused callout types */
/* If you don't use dna, diamond, ember, etc., delete their rules */

/* Remove unused variants */
/* If you only use minimal variant, delete neon/outlined/compact/raised */

/* Combine similar selectors */
/* BEFORE: */
.callout[data-callout="key-claim"] { --callout-color: var(--callout-crimson); }
.callout[data-callout="evidence"] { --callout-color: var(--callout-crimson); }
.callout[data-callout="insight"] { --callout-color: var(--callout-crimson); }

/* AFTER: */
.callout[data-callout="key-claim"],
.callout[data-callout="evidence"],
.callout[data-callout="insight"] {
  --callout-color: var(--callout-crimson);
}
```

#### **8. Performance Monitoring**

**Using Browser DevTools**:

1. Open DevTools (Ctrl+Shift+I)
2. Go to **Performance** tab
3. Click **Record** ⏺️
4. Scroll through a note with many callouts
5. Click **Stop** ⏹️
6. Analyze results:
   - **FPS graph**: Should stay above 50fps (ideally 60fps)
   - **Painting**: Look for excessive paint operations
   - **Rendering**: Check for layout thrashing

**Chrome Performance Insights**:
```
Look for warnings like:
- "Forced synchronous layout" (bad - indicates reflow)
- "Long paint time" (bad - simplify shadows/effects)
- "Excessive style recalculations" (bad - simplify selectors)
```

**Performance Budget**:
```markdown
TARGET METRICS (for 50 callouts visible):
- Scrolling: 60fps sustained
- Hover response: <16ms (1 frame)
- Style recalculation: <5ms per callout
- Total CSS file size: <20KB unminified
```

#### **9. Extreme Performance Mode**

For vaults with 100+ callouts per note:

```css
/* Add this at the end of the unified snippet */

/* EXTREME PERFORMANCE MODE */
/* Uncomment to enable ultra-lightweight callouts */

/*
body.callout-extreme-performance .callout {
  animation: none !important;
  transition: none !important;
  box-shadow: none !important;
  transform: none !important;
  background: transparent !important;
  border: 1px solid rgba(var(--callout-color), 0.3);
  border-left: 3px solid rgb(var(--callout-color));
}

body.callout-extreme-performance .callout::before,
body.callout-extreme-performance .callout-title::after {
  display: none !important;
}

body.callout-extreme-performance .callout:hover {
  transform: none !important;
  box-shadow: none !important;
}
*/
```

Apply with: `<body class="callout-extreme-performance">`

**Result**:
- Zero animations
- Zero shadows
- Zero transitions
- Minimal repaints
- Maximum performance for very large documents

---

## 📝 **CHANGELOG & VERSION HISTORY**

### **v3.0** (2025-12-27)
- ✨ Initial unified system release
- 🎨 Consolidated 15+ snippet files into single architecture
- 🎭 Added 5 switchable style variants
- 📦 60+ semantic callout types
- 🏗️ Modular design token system
- 🎬 Advanced animation library
- 📚 Comprehensive documentation

---

## 🤝 **CONTRIBUTING & CUSTOMIZATION**

### **Sharing Your Customizations**

Created an amazing custom variant or callout type? Share it with the community!

**Template for Sharing**:
```markdown
## Custom Variant: [Name]

**Purpose**: [What problem it solves]

**Visual Style**: [Description]

**CSS**:
```css
/* Paste your CSS here */
```

**Screenshot**: [If possible]

**Best Used For**: [Use cases]
```

---

## 📜 **LICENSE**

This unified callout system is released under the MIT License.

```
MIT License

Copyright (c) 2025 Pur3v4d3r

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🎯 **QUICK REFERENCE CARD**

```markdown
┌─────────────────────────────────────────────────────────────┐
│  UNIFIED CALLOUT SYSTEM - QUICK REFERENCE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📦 INSTALLATION:                                            │
│  1. Copy unified-callout-system.css to .obsidian/snippets/  │
│  2. Enable in Settings → CSS snippets                        │
│  3. (Optional) Apply variant body class                      │
│                                                              │
│  🎨 STYLE VARIANTS (body classes):                           │
│  - callout-variant-minimal     (transparent, borders only)   │
│  - callout-variant-neon         (intense glow effects)       │
│  - callout-variant-outlined     (clean bordered boxes)       │
│  - callout-variant-compact      (dense information layout)   │
│  - callout-variant-raised       (3D depth with shadows)      │
│                                                              │
│  🎯 POPULAR CALLOUT TYPES:                                   │
│  - [!key-claim]          Primary arguments                   │
│  - [!evidence]           Research findings                   │
│  - [!definition]         Formal definitions                  │
│  - [!warning]            Cautionary information              │
│  - [!action]             Next steps                          │
│  - [!diamond]            Premium content (enhanced glow)     │
│  - [!counter-argument]   Alternative perspectives            │
│                                                              │
│  🛠️ CUSTOMIZATION:                                           │
│  Edit :root {} variables:                                    │
│  - --callout-crimson: R, G, B    (change accent color)       │
│  - --glow-intensity: 0.3         (adjust glow strength)      │
│  - --callout-border-radius: 16px (adjust corner rounding)    │
│                                                              │
│  🔧 TROUBLESHOOTING:                                         │
│  1. No color? → Check snippet enabled                        │
│  2. Variant not working? → Verify body class                 │
│  3. Performance issues? → Disable animations                 │
│  4. Conflicts? → Disable other callout snippets              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

**END OF DOCUMENTATION**

For the complete CSS file, see: `unified-callout-system.css`

For updates and community contributions, visit: [Your Repository/Community Link]
