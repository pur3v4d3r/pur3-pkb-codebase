---
title: "🎨 Complete Modular Callout Styling System: Foundation + Swappable Styles"
id: "20251113190951"
type: "reference"
source: "claude-sonnet-4.5"
tags:
  - year/2025
  - type/reference
  - obsidian/customization/css
aliases:
  - Modular Callout System
  - Style Architecture
  - Swappable CSS Snippets
  - Callout Theme System
---

# 🎨 Complete Modular Callout Styling System: Foundation + Swappable Styles

---
`tags: #pkb #css-customization #design-system #pkb/infrastructure #pkb/infrastructure`
aliases: [Modular Callout System, Foundation-Style Architecture, Swappable CSS Snippets, Callout Theme System]
---

> [!abstract] **System Architecture Overview**
> This is a **two-layer CSS architecture** that separates *semantic categorization* (which callouts belong to which color theme) from *visual presentation* (how those callouts actually look). By maintaining this separation, you can completely transform your vault's aesthetic by toggling a single style snippet while preserving your carefully organized callout taxonomy.

---

## 🏗️ Part 1: The Foundation Layer (Always Enabled)

> [!important] **Critical Implementation Rule**
> These two foundation snippets must **ALWAYS be enabled**. They provide the color variables and thematic groupings that ALL style snippets depend on. Without these, none of the style sets will work.

### 📦 Foundation Snippet 1: Theme Color Palette

> [!what-this-does] **Purpose**
> Defines your three accent colors ([[Color Theory|Purple, Gold, Teal]]) plus base colors as [[CSS Custom Properties|CSS variables]] accessible throughout your entire vault. This creates a **single source of truth** for color management.

**File Name**: `00-foundation-color-palette.css`  
**Location**: `.obsidian/snippets/`

```css
/* ═══════════════════════════════════════════════════════════════
   FOUNDATION 1: THEME COLOR PALETTE
   Defines core colors as CSS custom properties (variables)
   ═══════════════════════════════════════════════════════════════ */

:root {
  /* === PRIMARY ACCENT COLORS === */
  --theme-purple: #7800F4;
  --theme-gold: #FFC700;
  --theme-teal: #72FFF1;
  
  /* === CORE UI COLORS === */
  --theme-text: #EAEAEA;
  --theme-bg: #17181B;

  /* === RGB VERSIONS (for rgba() transparency) === */
  --theme-purple-rgb: 120, 0, 244;
  --theme-gold-rgb: 255, 199, 0;
  --theme-teal-rgb: 114, 255, 241;
  --theme-text-rgb: 234, 234, 234;
  --theme-bg-rgb: 23, 24, 27;
  
  /* === DEFAULT FALLBACK === */
  --callout-color: var(--theme-purple);
  --callout-color-rgb: var(--theme-purple-rgb);
}
```

---

### 🗂️ Foundation Snippet 2: Complete Callout Categorization

> [!what-this-does] **Purpose**
> Assigns **every single one** of your 100+ custom callouts to a thematic color group (Purple, Gold, or Teal). This is the **semantic layer** - it answers "what type of information is this?" rather than "how should it look?"

**File Name**: `00-foundation-callout-categories.css`  
**Location**: `.obsidian/snippets/`

```css
/* ═══════════════════════════════════════════════════════════════
   FOUNDATION 2: COMPLETE CALLOUT CATEGORIZATION
   Assigns thematic colors to ALL 100+ callout types
   ═══════════════════════════════════════════════════════════════ */

/* ┌─────────────────────────────────────────────────────────────┐
   │ CATEGORY 1: LOGIC, ARGUMENT & ACADEMIC ANALYSIS (Purple)   │
   │ Core intellectual work: claims, evidence, reasoning         │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="key-claim"],
.callout[data-callout="casual-link"],
.callout[data-callout="evidence"],
.callout[data-callout="counter-argument"],
.callout[data-callout="no-evidence"],
.callout[data-callout="principle-point"],
.callout[data-callout="cosmos-concept"],
.callout[data-callout="equation"],
.callout[data-callout="thought-experiment"],
.callout[data-callout="definition"],
.callout[data-callout="analogy"],
.callout[data-callout="math"],
.callout[data-callout="analysis-rhetorical"],
.callout[data-callout="analysis-logical"],
.callout[data-callout="analysis-contextual"],
.callout[data-callout="analysis-cognitive"],
.callout[data-callout="core-principle"],
.callout[data-callout="argument"],
.callout[data-callout="feynman-technique"],
.callout[data-callout="atomic-concept"],
.callout[data-callout="comprehensive-reference"] {
  --callout-color: var(--theme-purple);
  --callout-color-rgb: var(--theme-purple-rgb);
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ CATEGORY 2: PROJECTS, WORKFLOW & STATUS (Gold)             │
   │ Task management, reading status, project tracking           │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="to-do"],
.callout[data-callout="read-complete"],
.callout[data-callout="reading-in-progress"],
.callout[data-callout="read-asap"],
.callout[data-callout="project-link"],
.callout[data-callout="hub-moc"],
.callout[data-callout="revist"],
.callout[data-callout="document"],
.callout[data-callout="capture"],
.callout[data-callout="tasks"],
.callout[data-callout="phase-one"],
.callout[data-callout="phase-two"],
.callout[data-callout="phase-three"],
.callout[data-callout="phase-four"],
.callout[data-callout="gemini-pro-response"],
.callout[data-callout="key-changes"],
.callout[data-callout="your-new-workflow"],
.callout[data-callout="plan"],
.callout[data-callout="kanban"],
.callout[data-callout="note-toolbar"],
.callout[data-callout="project-kickstarter"],
.callout[data-callout="zettelkasten-incubator"],
.callout[data-callout="problem-clarity-solution"],
.callout[data-callout="work-log-entry"],
.callout[data-callout="left-off-reading-at"],
.callout[data-callout="input-and-instruction"],
.callout[data-callout="iteration-and-versioning"] {
  --callout-color: var(--theme-gold);
  --callout-color-rgb: var(--theme-gold-rgb);
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ CATEGORY 3: IDEAS, META & QUESTIONS (Teal)                 │
   │ Reflective thinking, questions, connections, summaries      │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="confusion"],
.callout[data-callout="connection-ideas"],
.callout[data-callout="insight"],
.callout[data-callout="connections-and-links"],
.callout[data-callout="pre-read-questions"],
.callout[data-callout="pre-read-thoughts"],
.callout[data-callout="the-purpose"],
.callout[data-callout="choice-a"],
.callout[data-callout="choice-b"],
.callout[data-callout="the-philosophy"],
.callout[data-callout="ask-yourself-this"],
.callout[data-callout="question"],
.callout[data-callout="summary"],
.callout[data-callout="abstract"],
.callout[data-callout="how-to-use-this"],
.callout[data-callout="the-goal"],
.callout[data-callout="the-mission"],
.callout[data-callout="outcome"],
.callout[data-callout="methodology-and-sources"],
.callout[data-callout="starting-message"],
.callout[data-callout="how-to-use"],
.callout[data-callout="message"],
.callout[data-callout="how-this-dashboard-works"],
.callout[data-callout="changes-from-prompting-dashboard"],
.callout[data-callout="helpful-tip"],
.callout[data-callout="the-start"],
.callout[data-callout="related-topics-to-consider"],
.callout[data-callout="key"],
.callout[data-callout="topic-idea"],
.callout[data-callout="links-to-related-notes"],
.callout[data-callout="thoughts"],
.callout[data-callout="start-of-chat"],
.callout[data-callout="further-exploration"],
.callout[data-callout="what-this-does"],
.callout[data-callout="disposition"],
.callout[data-callout="description"],
.callout[data-callout="use-cases-and-examples"],
.callout[data-callout="purpose"],
.callout[data-callout="fleeting-thought"],
.callout[data-callout="in-note-metadata"],
.callout[data-callout="topic-name"],
.callout[data-callout="related-topics-for-pkb-expansion"],
.callout[data-callout="answer"],
.callout[data-callout="tags-taxonomy"],
.callout[data-callout="questions"] {
  --callout-color: var(--theme-teal);
  --callout-color-rgb: var(--theme-teal-rgb);
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ CATEGORY 4: PHOTOGRAPHY SPECIFIC (Gold)                    │
   │ Creative workflow for photography projects                  │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="shot-idea"],
.callout[data-callout="lighting-setup"],
.callout[data-callout="composition"],
.callout[data-callout="post-processing"] {
  --callout-color: var(--theme-gold);
  --callout-color-rgb: var(--theme-gold-rgb);
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ CATEGORY 5: WARNINGS & ATTENTION (Gold)                    │
   │ Critical information requiring immediate attention          │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="important-links"],
.callout[data-callout="warning"],
.callout[data-callout="constraints-and-pitfalls"],
.callout[data-callout="quick-reference"],
.callout[data-callout="review"] {
  --callout-color: var(--theme-gold);
  --callout-color-rgb: var(--theme-gold-rgb);
}
```

---

## 🎨 Part 2: Style Layer (Enable ONE at a Time)

> [!methodology-and-sources] **Usage Instructions**
> Below are **12 complete style systems**. Each one provides **full styling for ALL callout categories** defined in the foundation layer. **Enable only ONE style snippet at a time** - they will conflict if multiple are enabled simultaneously.

---

### 🔲 **STYLE SET 1: Minimalist Left-Bar**

> [!what-this-does] **Visual Description**
> Clean, professional aesthetic with **no background fill**. Only a bold **4px left border** in the callout's thematic color, with the title text colored to match. Maximum readability, zero distraction.

**Performance**: ⚡⚡⚡⚡⚡ (Excellent)  
**Best For**: Professional documentation, academic research, daily notes  
**File Name**: `01-style-minimalist-left-bar.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 1: MINIMALIST LEFT-BAR
   Clean callout with colored border and title only
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-left: 4px solid var(--callout-color); 
  background-color: transparent;
  border-radius: 4px;
  border-top: none;
  border-right: none;
  border-bottom: none;
  box-shadow: none;
  padding: 8px 12px;
}

.callout-title {
  background-color: transparent;
  color: var(--callout-color);
  font-weight: 600;
  padding: 4px 0 8px 0;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
  padding-top: 4px;
}

/* === Ensure all categories use their thematic color === */
/* Purple, Gold, and Teal groups are already defined in Foundation 2 */
/* This style simply respects --callout-color for all */
```

---

### ✨ **STYLE SET 2: Subtle Glow & Float (Hover)**

> [!what-this-does] **Visual Description**
> Callouts have a **subtle background tint** and minimal shadow in base state. On hover, they **float upward** (translateY) and gain a **glowing shadow** in their thematic color. Creates engaging, interactive feel.

**Performance**: ⚡⚡⚡⚡⚡ (Excellent - GPU accelerated)  
**Best For**: Interactive documentation, learning materials, engagement-focused content  
**File Name**: `02-style-glow-float-hover.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 2: SUBTLE GLOW & FLOAT (HOVER)
   Floating elevation with colored glow on hover
   ═══════════════════════════════════════════════════════════════ */

.callout {
  background-color: rgba(var(--theme-bg-rgb), 0.5);
  border: 1px solid rgba(var(--callout-color-rgb), 0.2);
  border-left: 4px solid var(--callout-color);
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  padding: 10px 14px;
  transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;
  cursor: default;
}

.callout:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 12px rgba(var(--callout-color-rgb), 0.3);
}

.callout-title {
  color: var(--callout-color);
  font-weight: 600;
  background-color: transparent;
  padding-bottom: 8px;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
}

/* === All categories automatically inherit their color from --callout-color === */
```

---

### 📋 **STYLE SET 3: Header-Only Fill**

> [!what-this-does] **Visual Description**
> **Title area has colored background** (20% opacity of theme color) creating clear visual section. Content area remains transparent, blending with note background. Very popular modern UI pattern.

**Performance**: ⚡⚡⚡⚡⚡ (Excellent)  
**Best For**: Content-heavy notes, structured documentation, MOCs  
**File Name**: `03-style-header-only-fill.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 3: HEADER-ONLY FILL
   Colored title bar with transparent content area
   ═══════════════════════════════════════════════════════════════ */

.callout {
  background-color: transparent;
  border: 1px solid rgba(var(--callout-color-rgb), 0.3);
  border-radius: 6px;
  overflow: hidden;
  box-shadow: none;
}

.callout-title {
  background-color: rgba(var(--callout-color-rgb), 0.2);
  color: var(--callout-color);
  font-weight: 600;
  margin: -12px -12px 12px -12px;
  padding: 10px 12px 10px 12px;
}

.callout-icon {
  color: var(--callout-color);
  margin-left: -2px;
}

.callout-content {
  padding-top: 0;
  padding-left: 12px;
  padding-right: 12px;
  padding-bottom: 12px;
  color: var(--theme-text);
}

/* === Respects all callout color categories === */
```

---

### 🌈 **STYLE SET 4: Vibrant Gradient Fill**

> [!what-this-does] **Visual Description**
> **Diagonal gradient background** (135deg) from higher opacity theme color (20%) to lower opacity (5%). Creates depth and visual interest while maintaining readability. Left border accent retained.

**Performance**: ⚡⚡⚡⚡ (Very Good - Static gradients)  
**Best For**: Visual hierarchy, creative work, featured content  
**File Name**: `04-style-vibrant-gradient.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 4: VIBRANT GRADIENT FILL
   Diagonal gradient background in theme color
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border: none;
  border-radius: 8px;
  background-image: linear-gradient(135deg, 
    rgba(var(--callout-color-rgb), 0.2), 
    rgba(var(--callout-color-rgb), 0.05) 70%
  );
  border-left: 4px solid var(--callout-color);
  overflow: hidden;
  box-shadow: none;
  padding: 12px 16px;
}

.callout-title {
  color: var(--callout-color);
  font-weight: 600;
  background-color: transparent;
  padding-top: 8px;
  padding-bottom: 10px;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
  padding-top: 4px;
}

/* === All theme colors (Purple, Gold, Teal) create unique gradients === */
```

---

### 🔮 **STYLE SET 5: Glassmorphism**

> [!what-this-does] **Visual Description**
> **Frosted glass effect** using backdrop-filter blur. Callout has semi-transparent background (10% theme color) with 10px blur on content behind it. Modern, layered aesthetic. Best with textured backgrounds.

**Performance**: ⚡⚡⚡ (Good - backdrop-filter moderately expensive)  
**Best For**: Modern UI aesthetic, layered content, creative projects  
**File Name**: `05-style-glassmorphism.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 5: GLASSMORPHISM
   Frosted glass effect with backdrop blur
   ═══════════════════════════════════════════════════════════════ */

.callout {
  background-color: rgba(var(--callout-color-rgb), 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(var(--callout-color-rgb), 0.3);
  border-left: 4px solid var(--callout-color);
  border-radius: 10px;
  box-shadow: none;
  padding: 12px 16px;
}

.callout-title {
  color: var(--callout-color);
  font-weight: 600;
  background-color: transparent;
  padding-bottom: 8px;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
}

/* === Works beautifully with all three theme colors === */
```

---

### 📜 **STYLE SET 6: Scrolling Content (Fixed Height)**

> [!what-this-does] **Visual Description**
> Callout **height constrained to 300px** (customizable). Title remains fixed, **content scrolls** independently. Perfect for long-form callouts like `document`, `equation`, `comprehensive-reference`.

**Performance**: ⚡⚡⚡⚡ (Very Good)  
**Best For**: Long-form content, reference materials, embedded documents  
**File Name**: `06-style-scrolling-content.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 6: SCROLLING CONTENT (FIXED HEIGHT)
   Constrained height with scrollable content area
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-left: 4px solid var(--callout-color);
  background-color: rgba(var(--callout-color-rgb), 0.05);
  border-radius: 6px;
  border-top: 1px solid rgba(var(--callout-color-rgb), 0.2);
  border-right: 1px solid rgba(var(--callout-color-rgb), 0.2);
  border-bottom: 1px solid rgba(var(--callout-color-rgb), 0.2);
  
  /* === ADJUST THIS VALUE TO CHANGE MAX HEIGHT === */
  max-height: 300px;
  
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.callout-title {
  color: var(--callout-color);
  flex-shrink: 0;
  background-color: transparent;
  font-weight: 600;
  padding: 10px 12px 8px 12px;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  overflow-y: auto;
  padding: 8px 12px 12px 12px;
  padding-right: 8px;
  color: var(--theme-text);
}

/* === Custom scrollbar styling === */
.callout-content::-webkit-scrollbar {
  width: 6px;
}

.callout-content::-webkit-scrollbar-track {
  background: rgba(var(--callout-color-rgb), 0.1);
  border-radius: 3px;
}

.callout-content::-webkit-scrollbar-thumb {
  background: rgba(var(--callout-color-rgb), 0.4);
  border-radius: 3px;
}

.callout-content::-webkit-scrollbar-thumb:hover {
  background: rgba(var(--callout-color-rgb), 0.6);
}
```

---

### ⚡ **STYLE SET 7: Animated Gradient Border**

> [!what-this-does] **Visual Description**
> **Animated border effect** using pseudo-element with moving linear gradient. Border "shimmers" continuously with theme color. On hover, animation intensifies. Premium, attention-grabbing aesthetic.

**Performance**: ⚡⚡⚡ (Good - Animated pseudo-elements)  
**Best For**: Premium content, call-to-action callouts, hero sections  
**File Name**: `07-style-animated-border.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 7: ANIMATED GRADIENT BORDER
   Shimmering border animation with theme color
   ═══════════════════════════════════════════════════════════════ */

@keyframes shimmer {
  0% { background-position: -500% 0; }
  100% { background-position: 500% 0; }
}

.callout {
  border-radius: 8px;
  position: relative;
  background-color: var(--theme-bg);
  overflow: hidden;
  z-index: 1;
  border: none;
  padding: 12px 16px;
}

.callout::before {
  content: '';
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  border-radius: inherit;
  z-index: -1;
  background: linear-gradient(90deg,
    var(--theme-bg),
    var(--callout-color),
    var(--theme-bg),
    var(--theme-bg)
  );
  background-size: 400% 100%;
  transition: opacity 0.3s ease;
  opacity: 0.4;
}

.callout:hover::before {
  animation: shimmer 4s linear infinite;
  opacity: 1;
}

.callout-title {
  color: var(--callout-color);
  background: transparent;
  font-weight: 600;
  padding-bottom: 8px;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
}

/* === Each category (Purple, Gold, Teal) animates with its own color === */
```

---

### 💎 **STYLE SET 8: Elevated Cards with Shadow**

> [!what-this-does] **Visual Description**
> **Multi-layered box-shadows** create floating card appearance. Subtle background tint (8% theme color) with strong shadow projection. Creates clear spatial hierarchy and depth perception.

**Performance**: ⚡⚡⚡⚡ (Very Good - Multiple static shadows)  
**Best For**: Important callouts, card-based layouts, visual separation  
**File Name**: `08-style-elevated-cards.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 8: ELEVATED CARDS WITH SHADOW
   Floating card aesthetic with depth
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-radius: 8px;
  overflow: hidden;
  border: none;
  background-color: rgba(var(--callout-color-rgb), 0.08);
  box-shadow: 
    0 2px 4px rgba(var(--callout-color-rgb), 0.15),
    0 8px 16px rgba(var(--callout-color-rgb), 0.1),
    0 16px 32px rgba(var(--callout-color-rgb), 0.05);
  padding: 14px 18px;
}

.callout-title {
  background-color: rgba(var(--callout-color-rgb), 0.15);
  color: var(--callout-color);
  font-weight: 600;
  margin: -14px -18px 12px -18px;
  padding: 12px 18px;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
  padding-top: 4px;
}

/* === All categories receive appropriate elevation === */
```

---

### 🌟 **STYLE SET 9: Radial Gradient Spotlight**

> [!what-this-does] **Visual Description**
> **Radial gradient** emanating from top-left corner creates "spotlight" effect. Brighter center (18% opacity) fading to darker edges (2% opacity). Title has solid color background. Adds focus and depth.

**Performance**: ⚡⚡⚡⚡ (Excellent - Static radial gradients)  
**Best For**: Featured content, hero callouts, attention direction  
**File Name**: `09-style-radial-spotlight.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 9: RADIAL GRADIENT SPOTLIGHT
   Spotlight effect from corner
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-radius: 8px;
  overflow: hidden;
  border: none;
  background: radial-gradient(circle at top left, 
    rgba(var(--callout-color-rgb), 0.18) 0%, 
    rgba(var(--callout-color-rgb), 0.08) 50%, 
    rgba(var(--callout-color-rgb), 0.02) 100%
  );
  border-left: 3px solid var(--callout-color);
  padding: 12px 16px;
}

.callout-title {
  background-color: rgba(var(--callout-color-rgb), 0.15);
  color: var(--callout-color);
  font-weight: 600;
  margin: -12px -16px 12px -16px;
  padding: 10px 16px;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
  padding-top: 4px;
}

/* === Creates unique spotlight for each theme color === */
```

---

### 🎪 **STYLE SET 10: Neon Glow Effect**

> [!what-this-does] **Visual Description**
> **Cyberpunk-inspired** styling with **layered text-shadow** on titles (4 shadow layers) and **glowing box-shadow** on container. Dark background (95% opacity) with vibrant borders. Creates luminous, attention-grabbing aesthetic.

**Performance**: ⚡⚡⚡ (Good - Multiple text-shadows moderately expensive)  
**Best For**: Creative work, cyberpunk themes, portfolio notes, standout content  
**File Name**: `10-style-neon-glow.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 10: NEON GLOW EFFECT
   Cyberpunk aesthetic with glowing text and borders
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-radius: 8px;
  overflow: hidden;
  border: 2px solid var(--callout-color);
  background-color: rgba(var(--theme-bg-rgb), 0.95);
  box-shadow: 
    0 0 10px rgba(var(--callout-color-rgb), 0.5),
    0 0 20px rgba(var(--callout-color-rgb), 0.3),
    0 0 30px rgba(var(--callout-color-rgb), 0.2);
  padding: 12px 16px;
}

.callout-title {
  color: var(--callout-color);
  text-shadow: 
    0 0 5px rgba(var(--callout-color-rgb), 0.8),
    0 0 10px rgba(var(--callout-color-rgb), 0.6),
    0 0 15px rgba(var(--callout-color-rgb), 0.4),
    0 0 20px rgba(var(--callout-color-rgb), 0.3);
  background-color: rgba(var(--theme-bg-rgb), 0.9);
  font-weight: 700;
  letter-spacing: 0.5px;
  margin: -12px -16px 10px -16px;
  padding: 12px 16px;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  background-color: rgba(var(--theme-bg-rgb), 0.8);
  color: var(--theme-text);
  padding-top: 8px;
}

/* === Purple, Gold, and Teal each create unique neon effects === */
```

---

### 🔷 **STYLE SET 11: Geometric Border Patterns**

> [!what-this-does] **Visual Description**
> **Striped pattern** on top border (8px stripes) using repeating-linear-gradient. Combined with left-bar accent and subtle background fill. Adds visual texture and geometric interest without overwhelming content.

**Performance**: ⚡⚡⚡⚡ (Very Good - Static gradient patterns)  
**Best For**: Visual differentiation, theme consistency, creative organization  
**File Name**: `11-style-geometric-borders.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 11: GEOMETRIC BORDER PATTERNS
   Striped top border with left accent
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-radius: 6px;
  overflow: hidden;
  position: relative;
  background-color: rgba(var(--callout-color-rgb), 0.06);
  border-left: 4px solid var(--callout-color);
  padding: 12px 16px;
}

.callout-title {
  background-color: rgba(var(--callout-color-rgb), 0.12);
  color: var(--callout-color);
  font-weight: 600;
  position: relative;
  margin: -12px -16px 12px -16px;
  padding: 14px 16px;
}

.callout-title::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: repeating-linear-gradient(
    90deg,
    var(--callout-color) 0px,
    var(--callout-color) 8px,
    transparent 8px,
    transparent 16px
  );
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
  padding-top: 4px;
}

/* === Each color category creates unique striped pattern === */
```

---

### ✨ **STYLE SET 12: Multi-Effect Combo (Hover + Glow + Shadow)**

> [!what-this-does] **Visual Description**
> **Complex interaction pattern** combining multiple modifiers. Base state: subtle glow + moderate shadow. Hover state: scale (1.03x) + intensified multi-layer glow + elevated shadow + enhanced text-shadow. Premium, high-engagement experience.

**Performance**: ⚡⚡⚡ (Good - Multiple effects, GPU-accelerated where possible)  
**Best For**: Hero callouts, important announcements, premium content highlights  
**File Name**: `12-style-multi-effect-combo.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 12: MULTI-EFFECT COMBO
   Hover + Glow + Shadow combined
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-radius: 10px;
  overflow: hidden;
  border: 2px solid rgba(var(--callout-color-rgb), 0.4);
  background-color: rgba(var(--callout-color-rgb), 0.08);
  box-shadow: 
    0 2px 8px rgba(var(--callout-color-rgb), 0.2),
    0 0 15px rgba(var(--callout-color-rgb), 0.15);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: default;
  padding: 14px 18px;
}

.callout:hover {
  transform: scale(1.03);
  background-color: rgba(var(--callout-color-rgb), 0.15);
  border-color: var(--callout-color);
  box-shadow: 
    0 4px 20px rgba(var(--callout-color-rgb), 0.4),
    0 0 30px rgba(var(--callout-color-rgb), 0.3),
    0 0 50px rgba(var(--callout-color-rgb), 0.2);
}

.callout-title {
  background-color: rgba(var(--callout-color-rgb), 0.15);
  color: var(--callout-color);
  font-weight: 700;
  letter-spacing: 0.3px;
  text-shadow: 0 0 10px rgba(var(--callout-color-rgb), 0.5);
  transition: text-shadow 0.3s ease;
  margin: -14px -18px 12px -18px;
  padding: 14px 18px;
}

.callout:hover .callout-title {
  text-shadow: 
    0 0 10px rgba(var(--callout-color-rgb), 0.8),
    0 0 20px rgba(var(--callout-color-rgb), 0.6),
    0 0 30px rgba(var(--callout-color-rgb), 0.4);
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
  padding-top: 4px;
}

/* === All categories receive full multi-effect treatment === */
```

---

## 📊 Part 3: Quick Reference Guide

> [!helpful-tip] **Decision Matrix: Choosing Your Style**

| Your Priority | Recommended Style Sets |
|--------------|------------------------|
| **Maximum Performance** | 1 (Minimalist), 3 (Header-Only), 8 (Elevated) |
| **Modern Aesthetic** | 5 (Glassmorphism), 9 (Radial), 11 (Geometric) |
| **Interactivity** | 2 (Glow-Float), 7 (Animated), 12 (Multi-Effect) |
| **Professional/Academic** | 1 (Minimalist), 3 (Header-Only), 6 (Scrolling) |
| **Creative/Portfolio** | 10 (Neon), 7 (Animated), 4 (Gradient) |
| **Long-Form Content** | 6 (Scrolling), 3 (Header-Only), 8 (Elevated) |
| **Attention-Grabbing** | 10 (Neon), 12 (Multi-Effect), 7 (Animated) |
| **Clean & Minimal** | 1 (Minimalist), 2 (Glow-Float), 3 (Header-Only) |

### 🔧 Installation Checklist

> [!tasks] **Setup Procedure**
> - [ ] Create `.obsidian/snippets/` folder if it doesn't exist
> - [ ] Add `00-foundation-color-palette.css` and **enable it**
> - [ ] Add `00-foundation-callout-categories.css` and **enable it**
> - [ ] Add ONE style snippet (01-12) and **enable it**
> - [ ] Disable all other style snippets (only ONE at a time)
> - [ ] Refresh Obsidian or restart to see changes
> - [ ] Test on a note with multiple callout types

### ⚙️ Customization Tips

> [!example] **Easy Color Changes**

Want to change your accent colors? Edit the foundation palette:

```css
/* In 00-foundation-color-palette.css */
:root {
  --theme-purple: #9D4EDD; /* Change to your preferred purple */
  --theme-gold: #FFD60A;   /* Change to your preferred gold */
  --theme-teal: #06FFA5;   /* Change to your preferred teal */
  
  /* Update RGB values to match (use color picker to get RGB) */
  --theme-purple-rgb: 157, 78, 221;
  --theme-gold-rgb: 255, 214, 10;
  --theme-teal-rgb: 6, 255, 165;
}
```

All 12 style sets automatically adapt to your new colors!

### 🎯 Performance Comparison

| Style Set | Rating | Animation | GPU Accel. | Notes |
|-----------|--------|-----------|------------|-------|
| 1. Minimalist | ⚡⚡⚡⚡⚡ | None | N/A | Daily driver |
| 2. Glow-Float | ⚡⚡⚡⚡⚡ | Hover | Yes | Very smooth |
| 3. Header-Only | ⚡⚡⚡⚡⚡ | None | N/A | Excellent |
| 4. Gradient | ⚡⚡⚡⚡ | None | N/A | Static gradients |
| 5. Glassmorphism | ⚡⚡⚡ | None | Partial | Blur cost |
| 6. Scrolling | ⚡⚡⚡⚡ | None | N/A | Overflow only |
| 7. Animated Border | ⚡⚡⚡ | Continuous | Yes | Pseudo-element |
| 8. Elevated Cards | ⚡⚡⚡⚡ | None | N/A | Multiple shadows |
| 9. Radial Spotlight | ⚡⚡⚡⚡ | None | N/A | Static radial |
| 10. Neon Glow | ⚡⚡⚡ | None | N/A | Text-shadow cost |
| 11. Geometric | ⚡⚡⚡⚡ | None | N/A | Pattern efficient |
| 12. Multi-Effect | ⚡⚡⚡ | Hover | Yes | Complex combo |

---

## 🔍 Part 4: Troubleshooting

> [!attention] **Common Issues**

### Problem: Callouts look unchanged after enabling snippet
**Solution:**
- Verify foundation snippets (00-) are enabled
- Refresh Obsidian (Ctrl/Cmd + R)
- Check only ONE style snippet is enabled
- Ensure `.css` file extension (not `.txt`)

### Problem: Multiple style snippets conflict
**Solution:**
- Disable ALL style snippets except one
- Foundation snippets should ALWAYS remain enabled
- Use snippet toggle in Settings → Appearance → CSS Snippets

### Problem: Colors don't match my theme
**Solution:**
- Edit `00-foundation-color-palette.css`
- Change hex values in `:root` block
- Update both hex AND rgb values
- Maintain contrast for [[Accessibility Standards|accessibility]]

### Problem: Performance lag with animated styles
**Solution:**
- Switch to static style (1, 3, 4, 6, 8, 9, 11)
- Reduce document length
- Disable other performance-heavy plugins temporarily

---

## 🎓 Part 5: Advanced Techniques

> [!methodology-and-sources] **Creating Callout-Specific Overrides**

You can add custom rules AFTER a style snippet to override specific callout types:

```css
/* Add to bottom of any style snippet */

/* Make "important-links" stand out MORE than other Gold callouts */
.callout[data-callout="important-links"] {
  border: 3px solid var(--theme-gold);
  background-color: rgba(var(--theme-gold-rgb), 0.2);
  box-shadow: 0 0 25px rgba(var(--theme-gold-rgb), 0.5);
}

/* Make "fleeting-thought" more subtle than other Teal callouts */
.callout[data-callout="fleeting-thought"] {
  opacity: 0.7;
  font-style: italic;
}

/* Give "equation" callouts monospace font */
.callout[data-callout="equation"] .callout-content {
  font-family: 'Courier New', monospace;
  font-size: 0.95em;
}
```

---
# 🎨 Multi-Color Thematic Style Sets with Advanced Effects

---

aliases: [Multi-Color Callout Styles, Thematic Color Mixing, Advanced Callout Effects]
---

> [!abstract] **New Style Sets Overview**
> These advanced style sets apply **all three theme colors simultaneously** in creative, thematic ways. Each set combines **hover/float effects**, **custom shadows**, and **styled scrollbars**, while differentiating between your three callout categories (Purple/Logic, Gold/Workflow, Teal/Meta) through unique visual treatments.

---

## 🌈 **STYLE SET 13: Rainbow Gradient Spectrum**

> [!what-this-does] **Visual Description**
> Each callout displays a **horizontal gradient** that blends its primary color with the other two theme colors. Purple callouts flow Purple→Teal→Gold, Gold callouts flow Gold→Purple→Teal, Teal callouts flow Teal→Gold→Purple. Adds **hover float**, **colored shadows**, and **themed scrollbars**.

**Performance**: ⚡⚡⚡⚡ (Very Good)  
**Best For**: Creative work, visual hierarchy, colorful aesthetic  
**File Name**: `13-style-rainbow-gradient-spectrum.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 13: RAINBOW GRADIENT SPECTRUM
   Multi-color gradients with hover float and custom scrollbars
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-radius: 10px;
  overflow: hidden;
  border: 2px solid var(--callout-color);
  padding: 14px 18px;
  transition: transform 0.25s ease-out, box-shadow 0.25s ease-out;
  cursor: default;
  
  /* Constrain height for scrolling */
  max-height: 400px;
  display: flex;
  flex-direction: column;
}

.callout:hover {
  transform: translateY(-6px);
}

.callout-title {
  color: var(--callout-color);
  font-weight: 700;
  letter-spacing: 0.3px;
  background-color: transparent;
  padding-bottom: 10px;
  flex-shrink: 0;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
  overflow-y: auto;
  padding-right: 8px;
  padding-top: 4px;
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ PURPLE CATEGORY: Purple → Teal → Gold Flow                 │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="key-claim"],
.callout[data-callout="casual-link"],
.callout[data-callout="evidence"],
.callout[data-callout="counter-argument"],
.callout[data-callout="no-evidence"],
.callout[data-callout="principle-point"],
.callout[data-callout="cosmos-concept"],
.callout[data-callout="equation"],
.callout[data-callout="thought-experiment"],
.callout[data-callout="definition"],
.callout[data-callout="analogy"],
.callout[data-callout="math"],
.callout[data-callout="analysis-rhetorical"],
.callout[data-callout="analysis-logical"],
.callout[data-callout="analysis-contextual"],
.callout[data-callout="analysis-cognitive"],
.callout[data-callout="core-principle"],
.callout[data-callout="argument"],
.callout[data-callout="feynman-technique"],
.callout[data-callout="atomic-concept"],
.callout[data-callout="comprehensive-reference"] {
  background: linear-gradient(135deg,
    rgba(120, 0, 244, 0.2) 0%,
    rgba(114, 255, 241, 0.15) 50%,
    rgba(255, 199, 0, 0.1) 100%
  );
  box-shadow: 
    0 4px 12px rgba(120, 0, 244, 0.25),
    0 2px 6px rgba(114, 255, 241, 0.15);
}

.callout[data-callout="key-claim"]:hover,
.callout[data-callout="casual-link"]:hover,
.callout[data-callout="evidence"]:hover,
.callout[data-callout="counter-argument"]:hover,
.callout[data-callout="no-evidence"]:hover,
.callout[data-callout="principle-point"]:hover,
.callout[data-callout="cosmos-concept"]:hover,
.callout[data-callout="equation"]:hover,
.callout[data-callout="thought-experiment"]:hover,
.callout[data-callout="definition"]:hover,
.callout[data-callout="analogy"]:hover,
.callout[data-callout="math"]:hover,
.callout[data-callout="analysis-rhetorical"]:hover,
.callout[data-callout="analysis-logical"]:hover,
.callout[data-callout="analysis-contextual"]:hover,
.callout[data-callout="analysis-cognitive"]:hover,
.callout[data-callout="core-principle"]:hover,
.callout[data-callout="argument"]:hover,
.callout[data-callout="feynman-technique"]:hover,
.callout[data-callout="atomic-concept"]:hover,
.callout[data-callout="comprehensive-reference"]:hover {
  box-shadow: 
    0 8px 24px rgba(120, 0, 244, 0.4),
    0 4px 12px rgba(114, 255, 241, 0.3),
    0 2px 8px rgba(255, 199, 0, 0.2);
}

/* Purple scrollbar */
.callout[data-callout="key-claim"] .callout-content::-webkit-scrollbar,
.callout[data-callout="casual-link"] .callout-content::-webkit-scrollbar,
.callout[data-callout="evidence"] .callout-content::-webkit-scrollbar,
.callout[data-callout="counter-argument"] .callout-content::-webkit-scrollbar,
.callout[data-callout="no-evidence"] .callout-content::-webkit-scrollbar,
.callout[data-callout="principle-point"] .callout-content::-webkit-scrollbar,
.callout[data-callout="cosmos-concept"] .callout-content::-webkit-scrollbar,
.callout[data-callout="equation"] .callout-content::-webkit-scrollbar,
.callout[data-callout="thought-experiment"] .callout-content::-webkit-scrollbar,
.callout[data-callout="definition"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analogy"] .callout-content::-webkit-scrollbar,
.callout[data-callout="math"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analysis-rhetorical"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analysis-logical"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analysis-contextual"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analysis-cognitive"] .callout-content::-webkit-scrollbar,
.callout[data-callout="core-principle"] .callout-content::-webkit-scrollbar,
.callout[data-callout="argument"] .callout-content::-webkit-scrollbar,
.callout[data-callout="feynman-technique"] .callout-content::-webkit-scrollbar,
.callout[data-callout="atomic-concept"] .callout-content::-webkit-scrollbar,
.callout[data-callout="comprehensive-reference"] .callout-content::-webkit-scrollbar {
  width: 8px;
}

.callout[data-callout="key-claim"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="casual-link"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="evidence"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="counter-argument"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="no-evidence"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="principle-point"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="cosmos-concept"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="equation"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="thought-experiment"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="definition"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analogy"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="math"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analysis-rhetorical"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analysis-logical"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analysis-contextual"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analysis-cognitive"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="core-principle"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="argument"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="feynman-technique"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="atomic-concept"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="comprehensive-reference"] .callout-content::-webkit-scrollbar-track {
  background: linear-gradient(180deg,
    rgba(120, 0, 244, 0.15),
    rgba(114, 255, 241, 0.15)
  );
  border-radius: 4px;
}

.callout[data-callout="key-claim"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="casual-link"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="evidence"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="counter-argument"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="no-evidence"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="principle-point"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="cosmos-concept"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="equation"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="thought-experiment"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="definition"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analogy"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="math"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analysis-rhetorical"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analysis-logical"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analysis-contextual"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analysis-cognitive"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="core-principle"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="argument"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="feynman-technique"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="atomic-concept"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="comprehensive-reference"] .callout-content::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg,
    rgba(120, 0, 244, 0.7),
    rgba(114, 255, 241, 0.6)
  );
  border-radius: 4px;
}

.callout[data-callout="key-claim"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="casual-link"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="evidence"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="counter-argument"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="no-evidence"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="principle-point"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="cosmos-concept"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="equation"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="thought-experiment"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="definition"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analogy"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="math"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analysis-rhetorical"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analysis-logical"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analysis-contextual"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analysis-cognitive"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="core-principle"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="argument"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="feynman-technique"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="atomic-concept"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="comprehensive-reference"] .callout-content::-webkit-scrollbar-thumb:hover {
  background: var(--theme-purple);
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ GOLD CATEGORY: Gold → Purple → Teal Flow                   │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="to-do"],
.callout[data-callout="read-complete"],
.callout[data-callout="reading-in-progress"],
.callout[data-callout="read-asap"],
.callout[data-callout="project-link"],
.callout[data-callout="hub-moc"],
.callout[data-callout="revist"],
.callout[data-callout="document"],
.callout[data-callout="capture"],
.callout[data-callout="tasks"],
.callout[data-callout="phase-one"],
.callout[data-callout="phase-two"],
.callout[data-callout="phase-three"],
.callout[data-callout="phase-four"],
.callout[data-callout="gemini-pro-response"],
.callout[data-callout="key-changes"],
.callout[data-callout="your-new-workflow"],
.callout[data-callout="plan"],
.callout[data-callout="kanban"],
.callout[data-callout="note-toolbar"],
.callout[data-callout="project-kickstarter"],
.callout[data-callout="zettelkasten-incubator"],
.callout[data-callout="problem-clarity-solution"],
.callout[data-callout="work-log-entry"],
.callout[data-callout="left-off-reading-at"],
.callout[data-callout="input-and-instruction"],
.callout[data-callout="iteration-and-versioning"],
.callout[data-callout="shot-idea"],
.callout[data-callout="lighting-setup"],
.callout[data-callout="composition"],
.callout[data-callout="post-processing"],
.callout[data-callout="important-links"],
.callout[data-callout="warning"],
.callout[data-callout="constraints-and-pitfalls"],
.callout[data-callout="quick-reference"],
.callout[data-callout="review"] {
  background: linear-gradient(135deg,
    rgba(255, 199, 0, 0.2) 0%,
    rgba(120, 0, 244, 0.15) 50%,
    rgba(114, 255, 241, 0.1) 100%
  );
  box-shadow: 
    0 4px 12px rgba(255, 199, 0, 0.25),
    0 2px 6px rgba(120, 0, 244, 0.15);
}

.callout[data-callout="to-do"]:hover,
.callout[data-callout="read-complete"]:hover,
.callout[data-callout="reading-in-progress"]:hover,
.callout[data-callout="read-asap"]:hover,
.callout[data-callout="project-link"]:hover,
.callout[data-callout="hub-moc"]:hover,
.callout[data-callout="revist"]:hover,
.callout[data-callout="document"]:hover,
.callout[data-callout="capture"]:hover,
.callout[data-callout="tasks"]:hover,
.callout[data-callout="phase-one"]:hover,
.callout[data-callout="phase-two"]:hover,
.callout[data-callout="phase-three"]:hover,
.callout[data-callout="phase-four"]:hover,
.callout[data-callout="gemini-pro-response"]:hover,
.callout[data-callout="key-changes"]:hover,
.callout[data-callout="your-new-workflow"]:hover,
.callout[data-callout="plan"]:hover,
.callout[data-callout="kanban"]:hover,
.callout[data-callout="note-toolbar"]:hover,
.callout[data-callout="project-kickstarter"]:hover,
.callout[data-callout="zettelkasten-incubator"]:hover,
.callout[data-callout="problem-clarity-solution"]:hover,
.callout[data-callout="work-log-entry"]:hover,
.callout[data-callout="left-off-reading-at"]:hover,
.callout[data-callout="input-and-instruction"]:hover,
.callout[data-callout="iteration-and-versioning"]:hover,
.callout[data-callout="shot-idea"]:hover,
.callout[data-callout="lighting-setup"]:hover,
.callout[data-callout="composition"]:hover,
.callout[data-callout="post-processing"]:hover,
.callout[data-callout="important-links"]:hover,
.callout[data-callout="warning"]:hover,
.callout[data-callout="constraints-and-pitfalls"]:hover,
.callout[data-callout="quick-reference"]:hover,
.callout[data-callout="review"]:hover {
  box-shadow: 
    0 8px 24px rgba(255, 199, 0, 0.4),
    0 4px 12px rgba(120, 0, 244, 0.3),
    0 2px 8px rgba(114, 255, 241, 0.2);
}

/* Gold scrollbar */
.callout[data-callout="to-do"] .callout-content::-webkit-scrollbar,
.callout[data-callout="read-complete"] .callout-content::-webkit-scrollbar,
.callout[data-callout="reading-in-progress"] .callout-content::-webkit-scrollbar,
.callout[data-callout="read-asap"] .callout-content::-webkit-scrollbar,
.callout[data-callout="project-link"] .callout-content::-webkit-scrollbar,
.callout[data-callout="hub-moc"] .callout-content::-webkit-scrollbar,
.callout[data-callout="revist"] .callout-content::-webkit-scrollbar,
.callout[data-callout="document"] .callout-content::-webkit-scrollbar,
.callout[data-callout="capture"] .callout-content::-webkit-scrollbar,
.callout[data-callout="tasks"] .callout-content::-webkit-scrollbar,
.callout[data-callout="phase-one"] .callout-content::-webkit-scrollbar,
.callout[data-callout="phase-two"] .callout-content::-webkit-scrollbar,
.callout[data-callout="phase-three"] .callout-content::-webkit-scrollbar,
.callout[data-callout="phase-four"] .callout-content::-webkit-scrollbar,
.callout[data-callout="gemini-pro-response"] .callout-content::-webkit-scrollbar,
.callout[data-callout="key-changes"] .callout-content::-webkit-scrollbar,
.callout[data-callout="your-new-workflow"] .callout-content::-webkit-scrollbar,
.callout[data-callout="plan"] .callout-content::-webkit-scrollbar,
.callout[data-callout="kanban"] .callout-content::-webkit-scrollbar,
.callout[data-callout="note-toolbar"] .callout-content::-webkit-scrollbar,
.callout[data-callout="project-kickstarter"] .callout-content::-webkit-scrollbar,
.callout[data-callout="zettelkasten-incubator"] .callout-content::-webkit-scrollbar,
.callout[data-callout="problem-clarity-solution"] .callout-content::-webkit-scrollbar,
.callout[data-callout="work-log-entry"] .callout-content::-webkit-scrollbar,
.callout[data-callout="left-off-reading-at"] .callout-content::-webkit-scrollbar,
.callout[data-callout="input-and-instruction"] .callout-content::-webkit-scrollbar,
.callout[data-callout="iteration-and-versioning"] .callout-content::-webkit-scrollbar,
.callout[data-callout="shot-idea"] .callout-content::-webkit-scrollbar,
.callout[data-callout="lighting-setup"] .callout-content::-webkit-scrollbar,
.callout[data-callout="composition"] .callout-content::-webkit-scrollbar,
.callout[data-callout="post-processing"] .callout-content::-webkit-scrollbar,
.callout[data-callout="important-links"] .callout-content::-webkit-scrollbar,
.callout[data-callout="warning"] .callout-content::-webkit-scrollbar,
.callout[data-callout="constraints-and-pitfalls"] .callout-content::-webkit-scrollbar,
.callout[data-callout="quick-reference"] .callout-content::-webkit-scrollbar,
.callout[data-callout="review"] .callout-content::-webkit-scrollbar {
  width: 8px;
}

.callout[data-callout="to-do"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="read-complete"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="reading-in-progress"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="read-asap"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="project-link"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="hub-moc"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="revist"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="document"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="capture"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="tasks"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="phase-one"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="phase-two"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="phase-three"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="phase-four"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="gemini-pro-response"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="key-changes"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="your-new-workflow"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="plan"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="kanban"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="note-toolbar"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="project-kickstarter"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="zettelkasten-incubator"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="problem-clarity-solution"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="work-log-entry"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="left-off-reading-at"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="input-and-instruction"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="iteration-and-versioning"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="shot-idea"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="lighting-setup"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="composition"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="post-processing"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="important-links"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="warning"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="constraints-and-pitfalls"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="quick-reference"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="review"] .callout-content::-webkit-scrollbar-track {
  background: linear-gradient(180deg,
    rgba(255, 199, 0, 0.15),
    rgba(120, 0, 244, 0.15)
  );
  border-radius: 4px;
}

.callout[data-callout="to-do"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="read-complete"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="reading-in-progress"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="read-asap"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="project-link"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="hub-moc"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="revist"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="document"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="capture"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="tasks"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="phase-one"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="phase-two"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="phase-three"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="phase-four"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="gemini-pro-response"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="key-changes"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="your-new-workflow"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="plan"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="kanban"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="note-toolbar"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="project-kickstarter"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="zettelkasten-incubator"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="problem-clarity-solution"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="work-log-entry"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="left-off-reading-at"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="input-and-instruction"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="iteration-and-versioning"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="shot-idea"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="lighting-setup"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="composition"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="post-processing"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="important-links"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="warning"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="constraints-and-pitfalls"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="quick-reference"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="review"] .callout-content::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg,
    rgba(255, 199, 0, 0.7),
    rgba(120, 0, 244, 0.6)
  );
  border-radius: 4px;
}

.callout[data-callout="to-do"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="read-complete"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="reading-in-progress"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="read-asap"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="project-link"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="hub-moc"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="revist"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="document"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="capture"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="tasks"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="phase-one"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="phase-two"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="phase-three"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="phase-four"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="gemini-pro-response"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="key-changes"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="your-new-workflow"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="plan"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="kanban"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="note-toolbar"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="project-kickstarter"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="zettelkasten-incubator"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="problem-clarity-solution"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="work-log-entry"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="left-off-reading-at"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="input-and-instruction"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="iteration-and-versioning"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="shot-idea"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="lighting-setup"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="composition"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="post-processing"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="important-links"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="warning"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="constraints-and-pitfalls"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="quick-reference"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="review"] .callout-content::-webkit-scrollbar-thumb:hover {
  background: var(--theme-gold);
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ TEAL CATEGORY: Teal → Gold → Purple Flow                   │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="confusion"],
.callout[data-callout="connection-ideas"],
.callout[data-callout="insight"],
.callout[data-callout="connections-and-links"],
.callout[data-callout="pre-read-questions"],
.callout[data-callout="pre-read-thoughts"],
.callout[data-callout="the-purpose"],
.callout[data-callout="choice-a"],
.callout[data-callout="choice-b"],
.callout[data-callout="the-philosophy"],
.callout[data-callout="ask-yourself-this"],
.callout[data-callout="question"],
.callout[data-callout="summary"],
.callout[data-callout="abstract"],
.callout[data-callout="how-to-use-this"],
.callout[data-callout="the-goal"],
.callout[data-callout="the-mission"],
.callout[data-callout="outcome"],
.callout[data-callout="methodology-and-sources"],
.callout[data-callout="starting-message"],
.callout[data-callout="how-to-use"],
.callout[data-callout="message"],
.callout[data-callout="how-this-dashboard-works"],
.callout[data-callout="changes-from-prompting-dashboard"],
.callout[data-callout="helpful-tip"],
.callout[data-callout="the-start"],
.callout[data-callout="related-topics-to-consider"],
.callout[data-callout="key"],
.callout[data-callout="topic-idea"],
.callout[data-callout="links-to-related-notes"],
.callout[data-callout="thoughts"],
.callout[data-callout="start-of-chat"],
.callout[data-callout="further-exploration"],
.callout[data-callout="what-this-does"],
.callout[data-callout="disposition"],
.callout[data-callout="description"],
.callout[data-callout="use-cases-and-examples"],
.callout[data-callout="purpose"],
.callout[data-callout="fleeting-thought"],
.callout[data-callout="in-note-metadata"],
.callout[data-callout="topic-name"],
.callout[data-callout="related-topics-for-pkb-expansion"],
.callout[data-callout="answer"],
.callout[data-callout="tags-taxonomy"],
.callout[data-callout="questions"] {
  background: linear-gradient(135deg,
    rgba(114, 255, 241, 0.2) 0%,
    rgba(255, 199, 0, 0.15) 50%,
    rgba(120, 0, 244, 0.1) 100%
  );
  box-shadow: 
    0 4px 12px rgba(114, 255, 241, 0.25),
    0 2px 6px rgba(255, 199, 0, 0.15);
}

.callout[data-callout="confusion"]:hover,
.callout[data-callout="connection-ideas"]:hover,
.callout[data-callout="insight"]:hover,
.callout[data-callout="connections-and-links"]:hover,
.callout[data-callout="pre-read-questions"]:hover,
.callout[data-callout="pre-read-thoughts"]:hover,
.callout[data-callout="the-purpose"]:hover,
.callout[data-callout="choice-a"]:hover,
.callout[data-callout="choice-b"]:hover,
.callout[data-callout="the-philosophy"]:hover,
.callout[data-callout="ask-yourself-this"]:hover,
.callout[data-callout="question"]:hover,
.callout[data-callout="summary"]:hover,
.callout[data-callout="abstract"]:hover,
.callout[data-callout="how-to-use-this"]:hover,
.callout[data-callout="the-goal"]:hover,
.callout[data-callout="the-mission"]:hover,
.callout[data-callout="outcome"]:hover,
.callout[data-callout="methodology-and-sources"]:hover,
.callout[data-callout="starting-message"]:hover,
.callout[data-callout="how-to-use"]:hover,
.callout[data-callout="message"]:hover,
.callout[data-callout="how-this-dashboard-works"]:hover,
.callout[data-callout="changes-from-prompting-dashboard"]:hover,
.callout[data-callout="helpful-tip"]:hover,
.callout[data-callout="the-start"]:hover,
.callout[data-callout="related-topics-to-consider"]:hover,
.callout[data-callout="key"]:hover,
.callout[data-callout="topic-idea"]:hover,
.callout[data-callout="links-to-related-notes"]:hover,
.callout[data-callout="thoughts"]:hover,
.callout[data-callout="start-of-chat"]:hover,
.callout[data-callout="further-exploration"]:hover,
.callout[data-callout="what-this-does"]:hover,
.callout[data-callout="disposition"]:hover,
.callout[data-callout="description"]:hover,
.callout[data-callout="use-cases-and-examples"]:hover,
.callout[data-callout="purpose"]:hover,
.callout[data-callout="fleeting-thought"]:hover,
.callout[data-callout="in-note-metadata"]:hover,
.callout[data-callout="topic-name"]:hover,
.callout[data-callout="related-topics-for-pkb-expansion"]:hover,
.callout[data-callout="answer"]:hover,
.callout[data-callout="tags-taxonomy"]:hover,
.callout[data-callout="questions"]:hover {
  box-shadow: 
    0 8px 24px rgba(114, 255, 241, 0.4),
    0 4px 12px rgba(255, 199, 0, 0.3),
    0 2px 8px rgba(120, 0, 244, 0.2);
}

/* Teal scrollbar */
.callout[data-callout="confusion"] .callout-content::-webkit-scrollbar,
.callout[data-callout="connection-ideas"] .callout-content::-webkit-scrollbar,
.callout[data-callout="insight"] .callout-content::-webkit-scrollbar,
.callout[data-callout="connections-and-links"] .callout-content::-webkit-scrollbar,
.callout[data-callout="pre-read-questions"] .callout-content::-webkit-scrollbar,
.callout[data-callout="pre-read-thoughts"] .callout-content::-webkit-scrollbar,
.callout[data-callout="the-purpose"] .callout-content::-webkit-scrollbar,
.callout[data-callout="choice-a"] .callout-content::-webkit-scrollbar,
.callout[data-callout="choice-b"] .callout-content::-webkit-scrollbar,
.callout[data-callout="the-philosophy"] .callout-content::-webkit-scrollbar,
.callout[data-callout="ask-yourself-this"] .callout-content::-webkit-scrollbar,
.callout[data-callout="question"] .callout-content::-webkit-scrollbar,
.callout[data-callout="summary"] .callout-content::-webkit-scrollbar,
.callout[data-callout="abstract"] .callout-content::-webkit-scrollbar,
.callout[data-callout="how-to-use-this"] .callout-content::-webkit-scrollbar,
.callout[data-callout="the-goal"] .callout-content::-webkit-scrollbar,
.callout[data-callout="the-mission"] .callout-content::-webkit-scrollbar,
.callout[data-callout="outcome"] .callout-content::-webkit-scrollbar,
.callout[data-callout="methodology-and-sources"] .callout-content::-webkit-scrollbar,
.callout[data-callout="starting-message"] .callout-content::-webkit-scrollbar,
.callout[data-callout="how-to-use"] .callout-content::-webkit-scrollbar,
.callout[data-callout="message"] .callout-content::-webkit-scrollbar,
.callout[data-callout="how-this-dashboard-works"] .callout-content::-webkit-scrollbar,
.callout[data-callout="changes-from-prompting-dashboard"] .callout-content::-webkit-scrollbar,
.callout[data-callout="helpful-tip"] .callout-content::-webkit-scrollbar,
.callout[data-callout="the-start"] .callout-content::-webkit-scrollbar,
.callout[data-callout="related-topics-to-consider"] .callout-content::-webkit-scrollbar,
.callout[data-callout="key"] .callout-content::-webkit-scrollbar,
.callout[data-callout="topic-idea"] .callout-content::-webkit-scrollbar,
.callout[data-callout="links-to-related-notes"] .callout-content::-webkit-scrollbar,
.callout[data-callout="thoughts"] .callout-content::-webkit-scrollbar,
.callout[data-callout="start-of-chat"] .callout-content::-webkit-scrollbar,
.callout[data-callout="further-exploration"] .callout-content::-webkit-scrollbar,
.callout[data-callout="what-this-does"] .callout-content::-webkit-scrollbar,
.callout[data-callout="disposition"] .callout-content::-webkit-scrollbar,
.callout[data-callout="description"] .callout-content::-webkit-scrollbar,
.callout[data-callout="use-cases-and-examples"] .callout-content::-webkit-scrollbar,
.callout[data-callout="purpose"] .callout-content::-webkit-scrollbar,
.callout[data-callout="fleeting-thought"] .callout-content::-webkit-scrollbar,
.callout[data-callout="in-note-metadata"] .callout-content::-webkit-scrollbar,
.callout[data-callout="topic-name"] .callout-content::-webkit-scrollbar,
.callout[data-callout="related-topics-for-pkb-expansion"] .callout-content::-webkit-scrollbar,
.callout[data-callout="answer"] .callout-content::-webkit-scrollbar,
.callout[data-callout="tags-taxonomy"] .callout-content::-webkit-scrollbar,
.callout[data-callout="questions"] .callout-content::-webkit-scrollbar {
  width: 8px;
}

.callout[data-callout="confusion"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="connection-ideas"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="insight"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="connections-and-links"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="pre-read-questions"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="pre-read-thoughts"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="the-purpose"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="choice-a"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="choice-b"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="the-philosophy"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="ask-yourself-this"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="question"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="summary"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="abstract"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="how-to-use-this"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="the-goal"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="the-mission"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="outcome"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="methodology-and-sources"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="starting-message"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="how-to-use"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="message"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="how-this-dashboard-works"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="changes-from-prompting-dashboard"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="helpful-tip"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="the-start"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="related-topics-to-consider"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="key"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="topic-idea"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="links-to-related-notes"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="thoughts"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="start-of-chat"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="further-exploration"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="what-this-does"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="disposition"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="description"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="use-cases-and-examples"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="purpose"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="fleeting-thought"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="in-note-metadata"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="topic-name"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="related-topics-for-pkb-expansion"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="answer"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="tags-taxonomy"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="questions"] .callout-content::-webkit-scrollbar-track {
  background: linear-gradient(180deg,
    rgba(114, 255, 241, 0.15),
    rgba(255, 199, 0, 0.15)
  );
  border-radius: 4px;
}

.callout[data-callout="confusion"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="connection-ideas"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="insight"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="connections-and-links"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="pre-read-questions"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="pre-read-thoughts"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="the-purpose"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="choice-a"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="choice-b"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="the-philosophy"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="ask-yourself-this"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="question"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="summary"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="abstract"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="how-to-use-this"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="the-goal"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="the-mission"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="outcome"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="methodology-and-sources"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="starting-message"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="how-to-use"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="message"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="how-this-dashboard-works"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="changes-from-prompting-dashboard"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="helpful-tip"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="the-start"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="related-topics-to-consider"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="key"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="topic-idea"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="links-to-related-notes"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="thoughts"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="start-of-chat"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="further-exploration"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="what-this-does"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="disposition"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="description"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="use-cases-and-examples"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="purpose"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="fleeting-thought"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="in-note-metadata"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="topic-name"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="related-topics-for-pkb-expansion"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="answer"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="tags-taxonomy"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="questions"] .callout-content::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg,
    rgba(114, 255, 241, 0.7),
    rgba(255, 199, 0, 0.6)
  );
  border-radius: 4px;
}

.callout[data-callout="confusion"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="connection-ideas"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="insight"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="connections-and-links"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="pre-read-questions"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="pre-read-thoughts"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="the-purpose"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="choice-a"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="choice-b"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="the-philosophy"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="ask-yourself-this"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="question"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="summary"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="abstract"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="how-to-use-this"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="the-goal"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="the-mission"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="outcome"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="methodology-and-sources"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="starting-message"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="how-to-use"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="message"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="how-this-dashboard-works"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="changes-from-prompting-dashboard"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="helpful-tip"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="the-start"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="related-topics-to-consider"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="key"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="topic-idea"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="links-to-related-notes"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="thoughts"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="start-of-chat"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="further-exploration"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="what-this-does"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="disposition"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="description"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="use-cases-and-examples"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="purpose"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="fleeting-thought"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="in-note-metadata"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="topic-name"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="related-topics-for-pkb-expansion"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="answer"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="tags-taxonomy"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="questions"] .callout-content::-webkit-scrollbar-thumb:hover {
  background: var(--theme-teal);
}
```

---

## 🎭 **STYLE SET 14: Tri-Color Border Stack**

> [!what-this-does] **Visual Description**
> Each callout displays **three stacked colored borders** on the left edge - one for each theme color, creating a rainbow effect. The **primary color is thickest** (4px) with secondary colors layered above (2px each). Includes **hover float**, **tri-color shadows**, and **gradient scrollbars**.

**Performance**: ⚡⚡⚡⚡ (Very Good)  
**Best For**: Clear category identification, playful aesthetic, visual richness  
**File Name**: `14-style-tri-color-border-stack.css`

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 14: TRI-COLOR BORDER STACK
   Stacked color borders with hover float and gradient scrollbars
   ═══════════════════════════════════════════════════════════════ */

.callout {
  border-radius: 8px;
  overflow: hidden;
  background-color: rgba(var(--theme-bg-rgb), 0.7);
  padding: 14px 18px 14px 24px; /* Extra left padding for borders */
  position: relative;
  transition: transform 0.25s ease-out, box-shadow 0.25s ease-out;
  cursor: default;
  
  /* Constrain height for scrolling */
  max-height: 450px;
  display: flex;
  flex-direction: column;
}

.callout:hover {
  transform: translateY(-5px);
}

.callout-title {
  color: var(--callout-color);
  font-weight: 700;
  background-color: transparent;
  padding-bottom: 10px;
  flex-shrink: 0;
}

.callout-icon {
  color: var(--callout-color);
}

.callout-content {
  color: var(--theme-text);
  overflow-y: auto;
  padding-right: 8px;
  padding-top: 4px;
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ PURPLE CATEGORY: Purple (Primary) + Teal + Gold            │
   └─────────────────────────────────────────────────────────────┘ */

.callout[data-callout="key-claim"]::before,
.callout[data-callout="casual-link"]::before,
.callout[data-callout="evidence"]::before,
.callout[data-callout="counter-argument"]::before,
.callout[data-callout="no-evidence"]::before,
.callout[data-callout="principle-point"]::before,
.callout[data-callout="cosmos-concept"]::before,
.callout[data-callout="equation"]::before,
.callout[data-callout="thought-experiment"]::before,
.callout[data-callout="definition"]::before,
.callout[data-callout="analogy"]::before,
.callout[data-callout="math"]::before,
.callout[data-callout="analysis-rhetorical"]::before,
.callout[data-callout="analysis-logical"]::before,
.callout[data-callout="analysis-contextual"]::before,
.callout[data-callout="analysis-cognitive"]::before,
.callout[data-callout="core-principle"]::before,
.callout[data-callout="argument"]::before,
.callout[data-callout="feynman-technique"]::before,
.callout[data-callout="atomic-concept"]::before,
.callout[data-callout="comprehensive-reference"]::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: var(--theme-purple);
}

.callout[data-callout="key-claim"]::after,
.callout[data-callout="casual-link"]::after,
.callout[data-callout="evidence"]::after,
.callout[data-callout="counter-argument"]::after,
.callout[data-callout="no-evidence"]::after,
.callout[data-callout="principle-point"]::after,
.callout[data-callout="cosmos-concept"]::after,
.callout[data-callout="equation"]::after,
.callout[data-callout="thought-experiment"]::after,
.callout[data-callout="definition"]::after,
.callout[data-callout="analogy"]::after,
.callout[data-callout="math"]::after,
.callout[data-callout="analysis-rhetorical"]::after,
.callout[data-callout="analysis-logical"]::after,
.callout[data-callout="analysis-contextual"]::after,
.callout[data-callout="analysis-cognitive"]::after,
.callout[data-callout="core-principle"]::after,
.callout[data-callout="argument"]::after,
.callout[data-callout="feynman-technique"]::after,
.callout[data-callout="atomic-concept"]::after,
.callout[data-callout="comprehensive-reference"]::after {
  content: '';
  position: absolute;
  left: 4px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(180deg, var(--theme-teal) 0%, var(--theme-gold) 100%);
}

.callout[data-callout="key-claim"],
.callout[data-callout="casual-link"],
.callout[data-callout="evidence"],
.callout[data-callout="counter-argument"],
.callout[data-callout="no-evidence"],
.callout[data-callout="principle-point"],
.callout[data-callout="cosmos-concept"],
.callout[data-callout="equation"],
.callout[data-callout="thought-experiment"],
.callout[data-callout="definition"],
.callout[data-callout="analogy"],
.callout[data-callout="math"],
.callout[data-callout="analysis-rhetorical"],
.callout[data-callout="analysis-logical"],
.callout[data-callout="analysis-contextual"],
.callout[data-callout="analysis-cognitive"],
.callout[data-callout="core-principle"],
.callout[data-callout="argument"],
.callout[data-callout="feynman-technique"],
.callout[data-callout="atomic-concept"],
.callout[data-callout="comprehensive-reference"] {
  box-shadow: 
    -3px 0 8px rgba(120, 0, 244, 0.3),
    0 4px 12px rgba(120, 0, 244, 0.2),
    0 2px 6px rgba(114, 255, 241, 0.15),
    0 1px 4px rgba(255, 199, 0, 0.15);
}

.callout[data-callout="key-claim"]:hover,
.callout[data-callout="casual-link"]:hover,
.callout[data-callout="evidence"]:hover,
.callout[data-callout="counter-argument"]:hover,
.callout[data-callout="no-evidence"]:hover,
.callout[data-callout="principle-point"]:hover,
.callout[data-callout="cosmos-concept"]:hover,
.callout[data-callout="equation"]:hover,
.callout[data-callout="thought-experiment"]:hover,
.callout[data-callout="definition"]:hover,
.callout[data-callout="analogy"]:hover,
.callout[data-callout="math"]:hover,
.callout[data-callout="analysis-rhetorical"]:hover,
.callout[data-callout="analysis-logical"]:hover,
.callout[data-callout="analysis-contextual"]:hover,
.callout[data-callout="analysis-cognitive"]:hover,
.callout[data-callout="core-principle"]:hover,
.callout[data-callout="argument"]:hover,
.callout[data-callout="feynman-technique"]:hover,
.callout[data-callout="atomic-concept"]:hover,
.callout[data-callout="comprehensive-reference"]:hover {
  box-shadow: 
    -5px 0 12px rgba(120, 0, 244, 0.4),
    0 8px 24px rgba(120, 0, 244, 0.35),
    0 4px 12px rgba(114, 255, 241, 0.25),
    0 2px 8px rgba(255, 199, 0, 0.25);
}

/* Purple tri-color scrollbar */
.callout[data-callout="key-claim"] .callout-content::-webkit-scrollbar,
.callout[data-callout="casual-link"] .callout-content::-webkit-scrollbar,
.callout[data-callout="evidence"] .callout-content::-webkit-scrollbar,
.callout[data-callout="counter-argument"] .callout-content::-webkit-scrollbar,
.callout[data-callout="no-evidence"] .callout-content::-webkit-scrollbar,
.callout[data-callout="principle-point"] .callout-content::-webkit-scrollbar,
.callout[data-callout="cosmos-concept"] .callout-content::-webkit-scrollbar,
.callout[data-callout="equation"] .callout-content::-webkit-scrollbar,
.callout[data-callout="thought-experiment"] .callout-content::-webkit-scrollbar,
.callout[data-callout="definition"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analogy"] .callout-content::-webkit-scrollbar,
.callout[data-callout="math"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analysis-rhetorical"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analysis-logical"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analysis-contextual"] .callout-content::-webkit-scrollbar,
.callout[data-callout="analysis-cognitive"] .callout-content::-webkit-scrollbar,
.callout[data-callout="core-principle"] .callout-content::-webkit-scrollbar,
.callout[data-callout="argument"] .callout-content::-webkit-scrollbar,
.callout[data-callout="feynman-technique"] .callout-content::-webkit-scrollbar,
.callout[data-callout="atomic-concept"] .callout-content::-webkit-scrollbar,
.callout[data-callout="comprehensive-reference"] .callout-content::-webkit-scrollbar {
  width: 10px;
}

.callout[data-callout="key-claim"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="casual-link"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="evidence"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="counter-argument"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="no-evidence"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="principle-point"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="cosmos-concept"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="equation"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="thought-experiment"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="definition"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analogy"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="math"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analysis-rhetorical"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analysis-logical"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analysis-contextual"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="analysis-cognitive"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="core-principle"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="argument"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="feynman-technique"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="atomic-concept"] .callout-content::-webkit-scrollbar-track,
.callout[data-callout="comprehensive-reference"] .callout-content::-webkit-scrollbar-track {
  background: linear-gradient(180deg,
    rgba(120, 0, 244, 0.12),
    rgba(114, 255, 241, 0.12),
    rgba(255, 199, 0, 0.12)
  );
  border-radius: 5px;
}

.callout[data-callout="key-claim"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="casual-link"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="evidence"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="counter-argument"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="no-evidence"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="principle-point"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="cosmos-concept"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="equation"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="thought-experiment"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="definition"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analogy"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="math"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analysis-rhetorical"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analysis-logical"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analysis-contextual"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="analysis-cognitive"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="core-principle"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="argument"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="feynman-technique"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="atomic-concept"] .callout-content::-webkit-scrollbar-thumb,
.callout[data-callout="comprehensive-reference"] .callout-content::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg,
    rgba(120, 0, 244, 0.8),
    rgba(114, 255, 241, 0.7),
    rgba(255, 199, 0, 0.7)
  );
  border-radius: 5px;
}

.callout[data-callout="key-claim"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="casual-link"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="evidence"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="counter-argument"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="no-evidence"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="principle-point"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="cosmos-concept"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="equation"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="thought-experiment"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="definition"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analogy"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="math"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analysis-rhetorical"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analysis-logical"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analysis-contextual"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="analysis-cognitive"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="core-principle"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="argument"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="feynman-technique"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="atomic-concept"] .callout-content::-webkit-scrollbar-thumb:hover,
.callout[data-callout="comprehensive-reference"] .callout-content::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg,
    var(--theme-purple),
    var(--theme-teal),
    var(--theme-gold)
  );
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ GOLD CATEGORY: Gold (Primary) + Purple + Teal              │
   └─────────────────────────────────────────────────────────────┘ */

/* Due to token limits, I'll provide the pattern - repeat the above structure for Gold callouts with:
   - ::before using var(--theme-gold) at 4px
   - ::after using gradient from purple to teal at 2px
   - Box-shadow emphasizing gold first, then purple, then teal
   - Scrollbar gradient: gold → purple → teal
*/

[Continue pattern for all Gold callouts…]

/* ┌─────────────────────────────────────────────────────────────┐
   │ TEAL CATEGORY: Teal (Primary) + Gold + Purple              │
   └─────────────────────────────────────────────────────────────┘ */

[Continue pattern for all Teal callouts…]
```

> [!important] **Token Limit Notice**
> Due to response length constraints, Style Set 14 shows the complete pattern for Purple callouts. The Gold and Teal categories follow the exact same structure with colors rotated. The complete file would be ~4000 lines covering all 100+ callouts. Would you like me to:
> 
> 1. Generate the complete Set 14 in a separate response
> 2. Create a **condensed version** using the --callout-color variable (shorter, more maintainable)
> 3. Continue with additional multi-color style sets

---

# 🔗 Related Topics for PKB Expansion

1. **[[CSS Pseudo-Element Mastery]]**
   - *Connection*: Multi-color border effects rely heavily on ::before and ::after pseudo-elements
   - *Depth Potential*: Explore advanced pseudo-element techniques, z-index layering, and complex positioning
   - *Knowledge Graph Role*: Essential for [[Advanced CSS Techniques]] and [[Visual Effects]]

2. **[[Gradient Design Systems]]**
   - *Connection*: Multi-color gradients require understanding of color theory, blend modes, and visual hierarchy
   - *Depth Potential*: Study gradient mathematics, color space interpolation, and perceptual color theory
   - *Knowledge Graph Role*: Bridges [[Color Theory]] and [[CSS Implementation]]

3. **[[Scrollbar Customization Cross-Browser]]**
   - *Connection*: Custom scrollbars enhance UX but require careful cross-browser considerations
   - *Depth Potential*: Deep dive into ::-webkit-scrollbar vs scrollbar-color/scrollbar-width standards
   - *Knowledge Graph Role*: Critical for [[Browser Compatibility]] and [[UI Polish]]

4. **[[Animation Performance Budgets]]**
   - *Connection*: Hover effects and shadows must balance visual appeal with performance
   - *Depth Potential*: Study frame rates, compositor layers, and performance profiling tools
   - *Knowledge Graph Role*: Core concept for [[Performance Optimization]] and [[User Experience]]

---

Would you like me to create the complete Set 14, or generate additional multi-color style sets with different approaches (e.g., radial tri-color gradients, animated color cycling, or color-split title bars)?
# 🔗 Related Topics for PKB Expansion

1. **[[CSS Custom Properties Architecture]]**
   - *Connection*: Foundation system relies on CSS variables for color management and theme switching
   - *Depth Potential*: Explore [[CSS Variable Scope]], [[Theme Tokens]], and [[Design System Variables]]
   - *Knowledge Graph Role*: Core concept linking [[Modular CSS]] and [[Design Systems]]

2. **[[Obsidian Plugin Styling Integration]]**
   - *Connection*: CSS snippets must work harmoniously with plugin-generated callouts and components
   - *Depth Potential*: Study [[Plugin CSS Selectors]], [[Community Plugin Themes]], [[CSS Conflicts Resolution]]
   - *Knowledge Graph Role*: Bridges [[Obsidian Advanced Features]] and [[CSS Customization]]

3. **[[Visual Semantic Mapping in PKB]]**
   - *Connection*: Color categorization (Purple/Gold/Teal) creates cognitive shortcuts for information type recognition
   - *Depth Potential*: Explore [[Color Psychology in Knowledge Work]], [[Visual Information Architecture]], [[Cognitive Load Management]]
   - *Knowledge Graph Role*: Intersection of [[Information Design]] and [[Learning Science]]

4. **[[CSS Performance Optimization for Large Vaults]]**
   - *Connection*: Style choice impacts rendering performance in documents with 50+ callouts
   - *Depth Potential*: Deep dive into [[CSS Selector Efficiency]], [[Reflow/Repaint Triggers]], [[Animation Budget]]
   - *Knowledge Graph Role*: Critical for [[Performance Engineering]] and [[Scalable PKB Design]]

---

**System Summary:**
- **Foundation Layer**: 2 snippets (always enabled)
- **Style Layer**: 12 complete style systems (enable ONE at a time)
- **Total Callouts Covered**: 100+ custom types across 5 categories
- **Color System**: 3 semantic categories (Logic/Purple, Workflow/Gold, Meta/Teal)
- **Modularity**: Complete visual transformation with single snippet toggle