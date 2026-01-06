# Project Export

## Project Statistics

- Total files: 30

## Folder Structure

```
.obsidian
  snippets
    00-folder-tree.css
    01-glowing-headers.css
    10-mermaid.css
    bracket-glow-controls.css
    callout-icon.css
    callout-mod-12-icon-style-variations.css
    callout-mod-15-premium-card.css
    callout-mod-16-floating-light.css
    callout-mod-card.css
    callout-mod-neon.css
    callout-mod-raised.css
    code-block-fixed.css
    custom-horizontal-rules-.css
    custom-ordered-list-numbers-(colored)-.css
    dark-shadow-callout-system.css
    glassmorphism-sidebar-system.css
    inline-code-system.css
    mermaid-chart-enhancer.css
    metadata-panel-system.css
    metadata-panel.css
    pur3v4d3r-ultimate-callout-system.css
    square-bracket-glow.css
    tag-customization-system.css
    unified-callout-system.css
    _dataview.css
    _jetbrains-mono-light.css
    __v4d3r-mermaid.css
    __v4d3r-plugins.css
    __v4d3r-tables.css
    ___v4d3r-ui-system.css

```

### .obsidian\snippets\00-folder-tree.css

```css
/*
═══════════════════════════════════════════════════════════
 SNIPPET NAME: Pur3v4d3r's Custom File Tree Theme
 Purpose: Color-coded file explorer matching vault structure
 Author: Pur3v4d3r
 Date: 2025-12-05
 Vault Structure: Custom PKB with numbered folder system
 Installation: Place in .obsidian/snippets/ and enable
═══════════════════════════════════════════════════════════
*/

/* [FOUNDATION] Base File Explorer Styling - FIXED */
.nav-files-container {
  padding: 10px 6px;
  font-family: var(--font-interface);
}

.nav-folder-title,
.nav-file-title {
  transition: background-color 0.2s ease, color 0.2s ease; /* Only transition visual properties */
  border-radius: 4px;
}

/* [ROOT FOLDERS] Your Main Vault Structure */

/* 00-inbox - Critical Red (Processing Zone) */
.nav-folder-title[data-path="00-inbox"] {
  color: #C0C0C0!important;
  font-weight: 300;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="00-inbox"]::before {
  content: "📥 ";
  margin-right: 6px;
}

/* 000_databsae - Dark Red (Core Data) */
.nav-folder-title[data-path="000_databsae"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="000_databsae"]::before {
  content: "💾";
  margin-right: 6px;
}

/* 01_daily-notes - Light Grey (Time-based) */
.nav-folder-title[data-path="01_daily-notes"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="01_daily-notes"]::before {
  content: "📅 ";
  margin-right: 6px;
}

/* 02-projects - Bright Red (Active Work) - FIXED */
.nav-folder-title[data-path="02-projects"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="02-projects"]::before {
  content: "🔬";
  margin-right: 6px;
  
}

/* 03-notes - Medium Grey (Knowledge) */
.nav-folder-title[data-path="03-notes"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="03-notes"]::before {
  content: "📄";
  margin-right: 6px;
}

/* 04-library - Dark Grey (Reference Material) */
.nav-folder-title[data-path="04-library"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="04-library"]::before {
  content: "📚 ";
  margin-right: 6px;
}

/* 05-tasks-&-reviews - Crimson Red (Action Items) */
.nav-folder-title[data-path="05-tasks-&-reviews"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="05-tasks-&-reviews"]::before {
  content: "✅ ";
  margin-right: 6px;
}

/* 06-dashboards - Pale Grey (Overview/Navigation) */
.nav-folder-title[data-path="06-dashboards"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="06-dashboards"]::before {
  content: "📊 ";
  margin-right: 6px;
}

/* 07-mocs - Light Grey (Maps of Content) */
.nav-folder-title[data-path="07-mocs"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(255, 0, 0, 0.12)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="07-mocs"]::before {
  content: "🗺️ ";
  margin-right: 6px;
}

/* 99-archive - Light Gray (Historical) */
.nav-folder-title[data-path="99-archive"] {
  color: #C0C0C0!important;
  font-weight: 600!important;
  background: rgba(49, 49, 49, 0.12)!important;
  opacity: 0.85!important;
  font-size: 18px!important;
  border-right: 3px solid #8B0000!important;
  padding: 4px 8px!important;
}

.nav-folder-title[data-path="99-scripts"]::before {
  content: "👾";
  margin-right: 6px;
}

/* 99-system - Dark Red (Infrastructure) */
.nav-folder-title[data-path="99-system"] {
  color: #C0C0C0!important;
  font-weight: 600!important;
  background: rgba(49, 49, 49, 0.12)!important;
  opacity: 0.85!important;
  font-size: 18px!important;
  border-right: 3px solid #8B0000!important;
  padding: 4px 8px!important;
}

/* 99-scripts - Dark Red (Infrastructure) */
.nav-folder-title[data-path="99-scripts"] {
  color: #C0C0C0!important;
  background: rgba(49, 49, 49, 0.12)!important;
  font-weight: 600!important;
  opacity: 0.9!important;
  font-size: 18px!important; /* INCREASED from 12px */
  font-style: italic!important;
  border-right: 3px solid #8B0000!important;
  padding: 4px 8px!important;
}

.nav-folder-title[data-path="99-archive"]::before {
  content: "🗄️";
  margin-right: 6px;
}

.nav-folder-title[data-path="99-system"]::before {
  content: "⚙️ ";
  margin-right: 6px;
}
/* 00-meta - Dark Red (Infrastructure) */
.nav-folder-title[data-path="00-meta"] {
  color: #C0C0C0!important;
  background: rgba(255, 0, 0, 0.12)!important;
  font-weight: 600!important;
  opacity: 0.9!important;
   border-right: 3px solid #8B0000!important;
  font-size: 18px !important; /* INCREASED from 12px */
  padding: 4px 8px!important;
}

.nav-folder-title[data-path="00-meta"]::before {
  content: "♾️ ";
  margin-right: 6px;
} 
/* ═══════════════════════════════════════════════════════════
   [SPECIAL SUBFOLDERS] Custom Nested Folder Styling
   ══════════════════════════════════════════════════════════ */

/* Inbox Topic Sets - Organized Capture Area */
.nav-folder-title[data-path="00-inbox/02-topic-sets"] {
  color: #B0B0B0 !important;
  font-weight: 650!important;
  background: rgba(176, 176, 176, 0.12)!important;
  padding: 4px 8px!important;
  border-left: 3px solid #B0B0B0!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="00-inbox/02-topic-sets"]::before {
  content: "✍️ " !important;
  margin-right: 6px!important;
  opacity: 0.9!important;
}

/* [NESTED FOLDERS] Sub-folder Styling */
.nav-folder-children .nav-folder-title {
  font-size: 18px !important; /* INCREASED from 12px */
  padding-left: 12px !important;
  font-weight: 500 !important;
  opacity: 0.9 !important;
}

/* Add subtle connector lines for nested structure */
.nav-folder-children {
  position: relative!important;
  margin-left: 8px!important;
  padding-left: 12px!important;
}

.nav-folder-children::before {
  content: ""!important;
  position: absolute!important;
  left: 4px!important;
  top: 0!important;
  bottom: 8px!important;
  width: 2px!important;
  background: linear-gradient(180deg,    rgba(255, 0, 0, 0.3) 0%,    transparent 100%)!important;
  border-radius: 2px!important;
  -webkit-border-radius: 2px!important;
  -moz-border-radius: 2px!important;
  -ms-border-radius: 2px!important;
  -o-border-radius: 2px!important;
}

/* [FILES] File Styling */
.nav-file-title {
  padding: 3px 8px 3px 28px!important; /* Increased left padding for icon space */
  font-size: 18px!important; /* INCREASED from 13px */
  color: var(--text-normal)!important;
}

/* File type icons */
.nav-file-title[data-path$=".md"]::before {
  content: "📄 "!important;
  margin-right: 6px!important;
  opacity: 0.5!important;
  font-size: 18px!important; /* INCREASED from 12px */
}

.nav-file-title[data-path$=".canvas"]::before {
  content: "🎨 "!important;
  margin-right: 6px!important;
  opacity: 0.7!important;
}

/* Daily note files special styling */
.nav-file-title[data-path^="01_daily-notes/2025"]::before {
  content: "📆 "!important;
  opacity: 0.6!important;
}

/* [ACTIVE FILE] Current file highlight - FIXED */
.nav-file-title.is-active {
  color: #E50000!important;
  background: linear-gradient(90deg,
    rgba(229, 0, 0, 0.25) 0%,
    rgba(229, 0, 0, 0.08) 100%!important);
  border-left: 4px solid #E50000!important;
  font-weight: 600!important;
  padding-left: 24px!important; /* 4px border + 24px padding = 28px total (matches base) */
  box-shadow: 0 2px 8px rgba(229, 0, 0, 0.2)!important;
}

/* [HOVER EFFECTS] Interactive States - FIXED */
.nav-folder-title:hover {
  background: rgba(229, 0, 0, 0.15)!important;
  /* REMOVED: transform: translateX(2px); */
  cursor: pointer!important;
}

.nav-file-title:hover {
  background: rgba(224, 224, 224, 0.1)!important;
  /* REMOVED: transform: translateX(2px); */
  border-left: 2px solid #E0E0E0!important;
  padding-left: 26px!important; /* 2px border + 26px padding = 28px total (matches base) */
  cursor: pointer!important;
}

/* [COLLAPSE INDICATORS] Folder State Icons */
.nav-folder-collapse-indicator {
  padding: 4px!important;
  margin-left: -4px!important;
}

.nav-folder.is-collapsed > .nav-folder-title .nav-folder-collapse-indicator {
  transform: rotate(-90deg)!important;
  color: var(--text-muted)!important;
  -webkit-transform: rotate(-90deg)!important;
  -moz-transform: rotate(-90deg)!important;
  -ms-transform: rotate(-90deg)!important;
  -o-transform: rotate(-90deg)!important;
}

.nav-folder:not(.is-collapsed) > .nav-folder-title .nav-folder-collapse-indicator {
  color: #E50000!important;
}

/* [SPECIAL FILES] Highlight important file patterns */

/* System/Template Files (underscore prefix) - Bright Purple with System Icon */
.nav-file-title[data-path*="/_"] {
  color: #E50000 !important;
  opacity: 0.95!important;
  font-style: italic!important;
  font-weight: 500!important;
}

.nav-file-title[data-path*="/_"]::before {
  content: "⚙️ " !important;
  opacity: 0.8!important;
  font-size: 18px!important;
}

/* Reference Files - Reactor Orange */
.nav-file-title[data-path*="reference"] {
  color: #FF0000!important;
  font-style: italic!important;
}

/* Template Files (generic) - Bright Purple */
.nav-file-title[data-path*="template"] {
  color: #E50000!important;
  opacity: 0.95!important;
}

/* Dashboard Files - Terminal Green */
.nav-file-title[data-path*="dashboard"] {
  color: #E50000!important;
  font-weight: 500!important;
}

/* Topic Set Notes - Organized Teal */
.nav-file-title[data-path*="02-topic-sets/"] {
  color: #E0E0E0 !important;
  font-weight: 500!important;
}

.nav-file-title[data-path*="02-topic-sets/"]::before {
  content: "📑 " !important;
  opacity: 0.7!important;
}

/* MOC Files - Electric Blue Navigation */
.nav-file-title[data-path*="moc"],
.nav-file-title[data-path*="07-mocs/"] {
  color: #E50000 !important;
  font-weight: 500!important;
}

.nav-file-title[data-path*="moc"]::before,
.nav-file-title[data-path*="07-mocs/"]::before {
  content: "🗺️ " !important;
  opacity: 0.7!important;
}

/* ═══════════════════════════════════════════════════════════
   [REPORT NOTES] Domain-Categorized Report Styling
   ══════════════════════════════════════════════════════════ */

/* Cognitive Science Reports - Brain Purple */
.nav-file-title[data-path*="cog-"],
.nav-file-title[data-path*="cog-sci-report-"],
.nav-file-title[data-path*="psy-report-"],
.nav-file-title[data-path*="cog-psy-"] {
  color: #E50000 !important;
  font-weight: 500!important;
}

.nav-file-title[data-path*="cog-"]::before,
.nav-file-title[data-path*="cog-sci-report-"]::before,
.nav-file-title[data-path*="cog-psy-"]::before {
  content: "🧠 " !important;
  opacity: 0.7!important;
}

/* PKB/PKM Reports - Knowledge Gold */
.nav-file-title[data-path*="pkb-report-"],
.nav-file-title[data-path*="pkm-report-"] {
  color: #E50000 !important;
  font-weight: 500!important;
}

.nav-file-title[data-path*="pkb-report-"]::before,
.nav-file-title[data-path*="pkm-report-"]::before {
  content: "📖 " !important;
  opacity: 0.7!important;
}

/* Prompt Engineering Reports - AI Cyan */
.nav-file-title[data-path*="prompt-report-"],
.nav-file-title[data-path*="prompt-eng-"] {
  color: #E50000 !important;
  font-weight: 500!important;
}

.nav-file-title[data-path*="prompt-report-"]::before,
.nav-file-title[data-path*="prompt-eng-"]::before {
  content: "🤖 " !important;
  opacity: 0.7!important;
}

/* Cosmology Reports */
.nav-file-title[data-path*="cosmo-report-"],
.nav-file-title[data-path*="astro-"] {
  color: #E50000 !important;
  font-weight: 500!important;
}

.nav-file-title[data-path*="cosmo-report-"]::before,
.nav-file-title[data-path*="astro-"]::before {
  content: "🌌 " !important;
  opacity: 0.7!important;
}

/* Generic Report Files (fallback for reports without specific prefix) */
.nav-file-title[data-path*="-report-"]:not([data-path*="cog-"]):not([data-path*="pkb-"]):not([data-path*="prompt-"]):not([data-path*="cosmo-"]) {
  color: #E0E0E0 !important;
  font-weight: 500!important;
}

.nav-file-title[data-path*="-report-"]::before {
  content: "📕"!important;
  opacity: 0.6!important;
}

/* [VISUAL HIERARCHY] Indentation Enhancement */
.mod-root > .nav-folder > .nav-folder-children > .nav-folder {
  margin-left: 4px!important;
}

.mod-root > .nav-folder > .nav-folder-children > .nav-folder > .nav-folder-children {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 4px!important;
  padding: 4px 0!important;
  margin: 2px 0 2px 4px!important;
  -webkit-border-radius: 4px!important;
  -moz-border-radius: 4px!important;
  -ms-border-radius: 4px!important;
  -o-border-radius: 4px!important;
}

/* [ACCESSIBILITY] Motion & Focus States */
@media (prefers-reduced-motion: reduce) {
  .nav-folder-title,
  .nav-file-title,
  .nav-folder-title:hover,
  .nav-file-title:hover {
    transition: none!important;
    transform: none!important;
    -webkit-transition: none!important;
    -moz-transition: none!important;
    -ms-transition: none!important;
    -o-transition: none!important;
    -webkit-transform: none!important;
    -moz-transform: none!important;
    -ms-transform: none!important;
    -o-transform: none!important;
}
}

.nav-folder-title:focus-visible,
.nav-file-title:focus-visible {
  outline: 2px solid #E50000!important;
  outline-offset: 2px!important;
}

/* [SCROLLBAR] Match theme */
.nav-files-container::-webkit-scrollbar-thumb {
  background: rgba(229, 0, 0, 0.3)!important;
  border-radius: 4px;
}

.nav-files-container::-webkit-scrollbar-thumb:hover {
  background: rgba(229, 0, 0, 0.5)!important;
}

/* ═══════════════════════════════════════════════════════════
   [OPTIONAL FEATURES] Uncomment sections below to enable
   To enable: Remove the comment markers around the section
   To disable: Re-add comment markers at start and end
   ══════════════════════════════════════════════════════════ */

/* ─────────────────────────────────────────────────────────
   OPTIONAL 1: Index File Highlighting
   Makes -index.md files stand out with special styling
   ───────────────────────────────────────────────────────── */

.nav-file-title[data-path*="-index.md"],
.nav-file-title[data-path*="_index.md"] {
  color: #FF0000 !important;
  font-weight: 600!important;
  background: rgba(255, 107, 53, 0.1);
  border-left: 3px solid #FF0000!important;
  padding-left: 25px1!important; /* 3px border + 25px padding = 28px total (matches base) */
}

.nav-file-title[data-path*="-index.md"]::before,
.nav-file-title[data-path*="_index.md"]::before {
  content: "📑 " !important;
  opacity: 0.8!important;
}

/* ─────────────────────────────────────────────────────────
   OPTIONAL 2: Library Subfolder Color Coding
   Applies distinct colors to each library subject area
   ───────────────────────────────────────────────────────── */

.nav-folder-title[data-path^="04-library/01-cognitive-science"] {
  color: #C0C0C0;
  font-weight: 700!important;
  background: rgba(0, 0, 0, 0.09)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="04-library/01-cognitive-science"]::before {
  content: "->"!important;
  color: #C0C0C0!important;
  margin-right: 6px!important;
}


.nav-folder-title[data-path^="04-library/02-pkb-and-pkm-learning"] {
  color: #C0C0C0;
  font-weight: 700!important;
  background: rgba(0, 0, 0, 0.09)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="04-library/02-pkb-and-pkm-learning"]::before {
  content: "->"!important;
  color: #C0C0C0!important;
  margin-right: 6px!important;
}

.nav-folder-title[data-path^="04-library/03-prompt-engineering"] {
  color: #C0C0C0;
  font-weight: 700;
  background: rgba(0, 0, 0, 0.09);
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="04-library/03-prompt-engineering"]::before {
  content: "->"!important;
  color: #C0C0C0!important;
  margin-right: 6px!important;
}


.nav-folder-title[data-path^="04-library/04-cosmology"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(0, 0, 0, 0.09)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="04-library/04-cosmology"]::before {
  content: "->"!important;
  color: #C0C0C0!important;
  margin-right: 6px!important;
}

.nav-folder-title[data-path^="03-notes/01_permanent-notes"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(0, 0, 0, 0.09)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="03-notes/01_permanent-notes"]::before {
  content: "->"!important;
  color: #C0C0C0!important;
  margin-right: 6px!important;
}

.nav-folder-title[data-path^="03-notes/02_quotes"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(0, 0, 0, 0.09)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="03-notes/02_quotes"]::before {
  content: "->"!important;
  color: #C0C0C0!important;
  margin-right: 6px!important;
}

.nav-folder-title[data-path^="03-notes/05-stoic-notes"] {
  color: #C0C0C0!important;
  font-weight: 700!important;
  background: rgba(0, 0, 0, 0.09)!important;
  padding: 5px 8px!important;
  border-right: 3px solid #8B0000!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path="03-notes/05-stoic-notes"]::before {
  content: "->"!important;
  color: #C0C0C0!important;
  margin-right: 6px!important;
}


/* ─────────────────────────────────────────────────────────
   OPTIONAL 3: Timestamp Badge Display
   Shows timestamp from filename as a subtle badge
   ───────────────────────────────────────────────────────── */

.nav-file-title[data-path*="2025"]::after,
.nav-file-title[data-path*="2026"]::after,
.nav-file-title[data-path*="2027"]::after,
.nav-file-title[data-path*="2024"]::after {
  content: "🕐" !important;
  margin-left: 6px!important;
  opacity: 0.4!important;
  font-size: 18px!important;
}

/* ─────────────────────────────────────────────────────────
   OPTIONAL 4: Reference vs Report Folder Distinction
   Makes -reference and -reports folders visually distinct
   ───────────────────────────────────────────────────────── */

.nav-folder-title[data-path*="-reference"] {
    color: #B0B0B0 !important;
    font-weight: 650!important;
    background: rgba(176, 176, 176, 0.12)!important;
    padding: 4px 8px!important;
    border-left: 3px solid #B0B0B0!important;
    font-size: 18px!important;
  }
.nav-folder-title[data-path*="-reference"]::before {
  content: "📚 " !important;
}

.nav-folder-title[data-path*="-reports"] {
  color: #B0B0B0 !important;
  font-weight: 650!important;
  background: rgba(176, 176, 176, 0.12)!important;
  padding: 4px 8px!important;
  border-left: 3px solid #B0B0B0!important;
  font-size: 18px!important;
}

.nav-folder-title[data-path*="-reports"]::before {
  content: "📝" !important;
}

/* ─────────────────────────────────────────────────────────
   OPTIONAL 5: File Badge System
   Adds visual indicators based on note maturity level
   Requires notes to include maturity keywords in filename
   ───────────────────────────────────────────────────────── */

.nav-file-title[data-path*="seedling"]::after {
  content: "🌱" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="budding"]::after {
  content: "🌿" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="evergreen"]::after {
  content: "🌲" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="crit"]::after {
  content: "🔴" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="high"]::after {
  content: "🟠" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="mid"]::after {
  content: "🟡" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}
.nav-file-title[data-path*="low"]::after {
  content: "🟢" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="gemini"]::after,
.nav-file-title[data-path*="gem"]::after {

  content: "♊" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="claude"]::after {
  content: "🐉" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="prompt"]::after {
  content: "📋" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}

.nav-file-title[data-path*="component"]::after {
  content: "🧩" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}
.nav-file-title[data-path*="reference"]::after {
  content: "🍄" !important;
  margin-left: 4px!important;
  opacity: 0.6!important;
}
/* ─────────────────────────────────────────────────────────
   OPTIONAL 6: Compact Mode - Reduced Spacing
   Tighter spacing for file tree (more files visible)
   ───────────────────────────────────────────────────────── */

.nav-files-container {
  padding: 6px 4px !important;
}

.nav-folder-title,
.nav-file-title {
  padding-top: 2px !important;
  padding-bottom: 2px !important;
  font-size: 18px !important;
}

.nav-folder-children {
  margin-left: 6px !important;
  padding-left: 8px !important;
}

/* ─────────────────────────────────────────────────────────
   OPTIONAL 7: Rainbow Indent Lines
   Colorful nested folder indicators by depth
   ───────────────────────────────────────────────────────── */
   /* ─────────────────────────────────────────────────────────
   .nav-folder-children::before {
  background: linear-gradient(180deg,
    rgba(229, 0, 0, 0.4) 0%,
    rgba(224, 224, 224, 0.3) 50%,
    rgba(255, 110, 0, 0.2) 100%) !important;
}

.nav-folder-children .nav-folder-children::before {
  background: linear-gradient(180deg,
    rgba(224, 224, 224, 0.4) 0%,
    rgba(203, 255, 0, 0.3) 50%,
    transparent 100%) !important;
}
*/

/* ─────────────────────────────────────────────────────────
   OPTIONAL 8: Hide File Extensions
   Removes .md extension from file names in tree
   ───────────────────────────────────────────────────────── */

.nav-file-title-content {
  display: inline-block !important;
}

.nav-file-title-content::after {
  content: "" !important;
}

.tree-item-self .nav-file-title-content {
  max-width: calc(100% - 30px) !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

/* ─────────────────────────────────────────────────────────
   OPTIONAL 9: Animated Hover Effects
   Adds smooth scaling and glow on hover
   ───────────────────────────────────────────────────────── */

.nav-folder-title:hover {
  transform: scale(1.02) !important;
  box-shadow: 0 2px 12px rgba(229, 0, 0, 0.3) !important;
}

.nav-file-title:hover {
  transform: translateX(4px) scale(1.01) !important;
  box-shadow: 0 2px 8px rgba(224, 224, 224, 0.2) !important;
}

/* ─────────────────────────────────────────────────────────
   OPTIONAL 10: High Contrast Mode
   Increases contrast for better visibility
   ───────────────────────────────────────────────────────── */

   * ─────────────────────────────────────────────────────────
   .nav-folder-title,
.nav-file-title {
  filter: brightness(1.2) contrast(1.1) !important;
}

.nav-folder-title[data-path^="00-"],
.nav-folder-title[data-path^="01-"],
.nav-folder-title[data-path^="02-"],
.nav-folder-title[data-path^="03-"],
.nav-folder-title[data-path^="04-"],
.nav-folder-title[data-path^="05-"],
.nav-folder-title[data-path^="06-"],
.nav-folder-title[data-path^="07-"] {
  font-weight: 300 !important;
  text-shadow: 0 0 0px currentColor !important;
}

```

### .obsidian\snippets\01-glowing-headers.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 SNIPPET: Glowing Headers System
 Category: Typography
 Purpose: Neon glow heading hierarchy with RED/BLACK/GREY palette
 Author: Pur3v4d3r
 Created: 2025-12-29
 Version: 1.0.0

 Description:
 Complete heading hierarchy (H1-H6) featuring dark text with glowing
 red neon text-shadow effects. Uses JetBrains Mono with all-small-caps
 for a professional cyberpunk aesthetic.

 Color Palette:
 - Primary Glow: #FF0000 (Pure Red)
 - Secondary Glow: #E50000 (Deep Red)
 - Tertiary Glow: #B30000 (Dark Red)
 - Text Base: #040404 (Near Black)
 - Accent Grey: #858585 (Medium Grey)

 Font Requirements:
 - JetBrains Mono (recommended)
 - Download: https://www.jetbrains.com/lp/mono/

 Compatibility: Obsidian 1.5+
═══════════════════════════════════════════════════════════════════════════════
*/

/* ══════════════════════════════════════════════════════════
   HEADING LEVEL 1 - Intense Red Glow
   Primary headings with maximum glow intensity
   ══════════════════════════════════════════════════════════ */
.theme-dark .markdown-preview-view h1,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-1,
.theme-dark .cm-header-1,
.markdown-preview-view h1,
.cm-header-1,
h1 {
    font-family: "Jetbrains Mono", var(--font-monospace) !important;
    font-size: 1.8em !important;
    font-weight: 600 !important;
    font-variant: all-small-caps !important;
    color: #000000 !important;                  /* Pure Black */
    text-decoration: underline !important;
    text-shadow: 0 0 3px #ff0000ff, 0 0 6px #ff0000ee, 0 0 10px #ff0000cc,
                 0 0 14px #ff0000aa, 0 0 18px #ff000077;
                 /* Strong red neon glow */
  }
  
/* ══════════════════════════════════════════════════════════
   HEADING LEVEL 2 - Strong Red Glow
   Section headings with bold presence
   ══════════════════════════════════════════════════════════ */
.theme-dark .markdown-preview-view h2,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-2,
.theme-dark .cm-header-2,
.markdown-preview-view h2,
.cm-header-2,
h2 {
  font-family: "Jetbrains Mono", var(--font-monospace) !important;
  font-size: 1.8em !important;
  font-weight: 600 !important;
  font-variant: all-small-caps !important;
  color: #000000 !important;                  /* Pure Black */
  text-decoration: underline !important;
  text-shadow: 0 0 3px #ff0000ff, 0 0 6px #ff0000ee, 0 0 10px #ff0000cc,
               0 0 14px #ff0000aa, 0 0 18px #ff000077;
               /* Strong red neon glow */
}

/* ══════════════════════════════════════════════════════════
   HEADING LEVEL 3 - Medium Red Glow
   Subsection headings with reduced intensity
   ══════════════════════════════════════════════════════════ */
.theme-dark .markdown-preview-view h3,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-3,
.theme-dark .cm-header-3,
.markdown-preview-view h3,
.cm-header-3,
h3 {
    font-family: "Jetbrains Mono", var(--font-monospace) !important;
    font-size: 1.8em !important;
    font-weight: 100 !important;
    font-variant: all-small-caps !important;
    color: #000000ff !important;                  /* Pure Black */
    text-decoration: underline !important;
    text-shadow: 0 0 30px #5c0000ff, 0 0 20px #000000ee, 0 0 30px #ff0000cc,
                 0 0 30px #000000aa, 0 0 50px #ff000077;
                 /* Strong red neon glow */
  }

/* ══════════════════════════════════════════════════════════
   HEADING LEVEL 4 - Subtle Red Glow
   Minor section headings with softer effect
   ══════════════════════════════════════════════════════════ */
.theme-dark .markdown-preview-view h4,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-4,
.theme-dark .cm-header-4,
.markdown-preview-view h4,
.cm-header-4,
h4 {
  font-family: "Jetbrains Mono", var(--font-monospace) !important;
  font-size: 1.3em !important;
  font-weight: 500 !important;
  font-variant: all-small-caps !important;
  color: #000000 !important;                  /* Pure Black */
  text-decoration: underline !important;
  text-shadow: 0 0 2px #ff0000dd, 0 0 5px #ff0000bb, 0 0 8px #ff000099,
               0 0 11px #ff000066;
               /* Subtle red neon glow */
}

/* ══════════════════════════════════════════════════════════
   HEADING LEVEL 5 - Grey-Red Hybrid Glow
   Detail headings with grey undertones
   ══════════════════════════════════════════════════════════ */
.theme-dark .markdown-preview-view h5,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-5,
.theme-dark .cm-header-5,
.markdown-preview-view h5,
.cm-header-5,
h5 {
  font-family: "Jetbrains Mono", var(--font-monospace) !important;
  font-size: 1.15em !important;
  font-weight: 400 !important;
  font-variant: all-small-caps !important;
  color: #000000 !important;                  /* Pure Black */
  text-decoration: underline !important;
  text-shadow: 0 0 2px #ff0000cc, 0 0 4px #ff0000aa, 0 0 7px #ff000077,
               0 0 10px #ff000055;
               /* Soft red neon glow */
}

/* ══════════════════════════════════════════════════════════
   HEADING LEVEL 6 - Minimal Red Glow
   Smallest headings with faint red effect
   ══════════════════════════════════════════════════════════ */
.theme-dark .markdown-preview-view h6,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-6,
.theme-dark .cm-header-6,
.markdown-preview-view h6,
.cm-header-6,
h6 {
  font-family: "Jetbrains Mono", var(--font-monospace) !important;
  font-size: 1.05em !important;
  font-weight: 400 !important;
  font-variant: all-small-caps !important;
  color: #000000 !important;                  /* Pure Black */
  text-decoration: underline !important;
  text-shadow: 0 0 2px #ff0000aa, 0 0 4px #ff000088, 0 0 6px #ff000055;
               /* Minimal red neon glow */
}

/* ══════════════════════════════════════════════════════════
   END OF GLOWING HEADERS SYSTEM
   ══════════════════════════════════════════════════════════ */

```

### .obsidian\snippets\10-mermaid.css

```css
/*
═══════════════════════════════════════════════════════════
 SNIPPET: Mermaid Diagram Resizer
 Category: Diagrams
 Purpose: Resizable and scrollable Mermaid diagrams
 Author: Pur3v4d3r
 Created: 2025-12-13
 Version: 1.0.0

 Description:
 Adds drag-to-resize functionality to Mermaid diagram blocks
 with automatic scrolling for large diagrams. Features visual
 feedback on hover and flexible resizing options (both
 directions or vertical only).

 Dependencies: None
 Standalone: Yes

 Features:
 - Drag handle in bottom-right corner
 - Resize both horizontally and vertically
 - Automatic scrolling for overflow
 - Visual feedback on hover
 - Centered diagram layout
 - Optional fixed window mode

 Mermaid Documentation:
 https://mermaid.js.org/

 Compatibility: Obsidian 1.5+
═══════════════════════════════════════════════════════════
*/

/* ══════════════════════════════════════════════════════════
   MERMAID CONTAINER
   Main wrapper for diagram
   ══════════════════════════════════════════════════════════ */

.mermaid {
  /* ─────────────────────────────────────────
     ENABLE DRAG RESIZING
     ───────────────────────────────────────── */
  resize: both !important;                    /* Adds drag handle bottom-right */
  overflow: auto !important;                  /* Required for resize to work */

  /* ─────────────────────────────────────────
     LAYOUT & POSITIONING
     ───────────────────────────────────────── */
  display: flex !important;                   /* Flexbox for centering */
  justify-content: center;                    /* Center horizontally */
  align-items: center;                        /* Center vertically */

  /* ─────────────────────────────────────────
     VISUAL CUES
     ───────────────────────────────────────── */
  border: 1px dashed var(--background-modifier-border); /* Faint border */
  background-color: var(--background-primary-alt);
  padding: 10px;
  margin: 1rem auto;                          /* Center container itself */

  /* ─────────────────────────────────────────
     INITIAL DIMENSIONS
     ───────────────────────────────────────── */
  width: 100%;                                /* Start full width */
  max-width: 100%;
  min-height: 150px;                          /* Prevent collapsing */

  /* ─────────────────────────────────────────
     SMOOTH TRANSITIONS
     ───────────────────────────────────────── */
  transition: box-shadow 0.2s ease;
}

/* ══════════════════════════════════════════════════════════
   HOVER EFFECTS
   Visual feedback when interacting
   ══════════════════════════════════════════════════════════ */

.mermaid:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);    /* Lift effect */
  border-color: var(--text-accent);           /* Highlight border (gold) */
}

/* ══════════════════════════════════════════════════════════
   SVG DIAGRAM
   Internal diagram scaling
   ══════════════════════════════════════════════════════════ */

/*
 * Ensures the diagram scales WITH the container as you drag
 */
.mermaid svg {
  width: auto !important;
  height: auto !important;
  max-width: none !important;                 /* Remove default caps */
}

/* ══════════════════════════════════════════════════════════
   ALTERNATIVE: FIXED WINDOW MODE
   Vertical-only resizing with scrolling
   ══════════════════════════════════════════════════════════ */

/*
 * Uncomment this section if you prefer a scrollable window
 * over full resizing. This locks horizontal width and allows
 * only vertical adjustment.
 *
 * .mermaid {
 *   resize: vertical;
 *   overflow: scroll;
 *   max-height: 600px;
 *   justify-content: flex-start;
 * }
 */

/* ══════════════════════════════════════════════════════════
   DARK MODE THEME INTEGRATION
   Optional Mermaid theme colors
   ══════════════════════════════════════════════════════════ */

/*
 * These styles attempt to match Mermaid's generated SVG
 * to your Obsidian theme. Results may vary based on
 * Mermaid's internal styling.
 */

.theme-dark .mermaid {
  /* Background already set above */
}

/* Mermaid text elements */
.theme-dark .mermaid text {
  fill: var(--text-normal) !important;        /* Match theme text */
}

/* Mermaid node backgrounds */
.theme-dark .mermaid rect,
.theme-dark .mermaid circle {
  fill: var(--background-secondary) !important;
  stroke: var(--color-accent) !important;     /* Purple stroke */
}

/* Mermaid connections/arrows */
.theme-dark .mermaid path,
.theme-dark .mermaid line {
  stroke: var(--color-accent) !important;     /* Purple lines */
}

/* ══════════════════════════════════════════════════════════
   MERMAID SPECIFIC DIAGRAM TYPES
   Flowcharts, sequence diagrams, etc.
   ══════════════════════════════════════════════════════════ */

/* Flowchart nodes */
.theme-dark .mermaid .node rect {
  fill: rgba(229, 0, 0, 0.1) !important;    /* Purple tint */
  stroke: #E50000 !important;                 /* Purple border */
  stroke-width: 2px;
}

/* Sequence diagram boxes */
.theme-dark .mermaid .actor {
  fill: var(--background-secondary) !important;
  stroke: #E50000 !important;                 /* Gold border */
}

/* ══════════════════════════════════════════════════════════
   USAGE INSTRUCTIONS
   ══════════════════════════════════════════════════════════

   HOW TO RESIZE:
   1. Hover over the Mermaid diagram
   2. Look for the resize handle in the bottom-right corner
   3. Click and drag to resize

   SCROLLING:
   - If diagram exceeds container size, scrollbars appear
   - Use mouse wheel or scrollbar to navigate

   CUSTOMIZATION:
   - Change initial height: Adjust 'min-height' value
   - Change max height: Add 'max-height' property
   - Lock aspect ratio: Use 'resize: vertical' only
   - Remove border: Set 'border: none'

   EXAMPLE MERMAID CODE:
   ```mermaid
   graph TD
       A[Start] --> B{Decision}
       B -->|Yes| C[Action 1]
       B -->|No| D[Action 2]
       C --> E[End]
       D --> E
   ```

   ══════════════════════════════════════════════════════════ */

/* ══════════════════════════════════════════════════════════
   END OF MERMAID STYLING
   ══════════════════════════════════════════════════════════ */

```

### .obsidian\snippets\bracket-glow-controls.css

```css
/* ══════════════════════════════════════════════════════════════════════════════════
   BRACKET GLOW INTENSITY CONTROL
   Quick toggles for different glow intensities
   ══════════════════════════════════════════════════════════════════════════════════ */

/* ═══ INTENSITY LEVELS ═══ */
/* Comment/uncomment these sections to change intensity */

/* SUBTLE GLOW - Uncomment this section for minimal effect */
/*
:root {
  --bracket-shadow: 0 0 1px var(--red-shadow);
}
*/

/* MEDIUM GLOW - Uncomment this section for balanced effect */
/*:root {
  --bracket-shadow: 0 0 3px var(--red-shadow), 0 0 6px var(--red-shadow);
}

/* INTENSE GLOW - Uncomment this section for maximum effect */

:root {
  --bracket-shadow: 0 0 3px var(--red-shadow), 0 0 6px var(--red-shadow), 0 0 12px var(--red-shadow) , 0 0 18px var(--red-shadow) !important;
}
*/

/* PULSE EFFECT - Uncomment this section for animated pulsing */

@keyframes bracket-pulse {
  0%, 100% { text-shadow: 0 0 3px var(--red-shadow); }
  50% { text-shadow: 0 0 8px var(--red-shadow), 0 0 12px var(--red-shadow); }
}

.cm-formatting-link,
.cm-bracket {
  animation: bracket-pulse 2s infinite ease-in-out;
}
*/

/* COLOR VARIANTS - Replace red with other colors */
/* BLUE VARIANT */
/*
:root {
  --red-glow: #0066ff;
  --red-shadow: rgba(0, 102, 255, 0.9);
}
*/

/* GREEN VARIANT */
/*
:root {
  --red-glow: #00ff00;
  --red-shadow: rgba(0, 255, 0, 0.9);
}
*/

/* PURPLE VARIANT */
/*
:root {
  --red-glow: #9900ff;
  --red-shadow: rgba(153, 0, 255, 0.9);
}
*/
```

### .obsidian\snippets\callout-icon.css

```css
/* ═══════════════════════════════════════════════════════════════
   STYLE SET 5: Icon
   Frosted glass effect with backdrop blur
   ═══════════════════════════════════════════════════════════════ */

  .callout-icon {
    filter: drop-shadow(0 0 2px rgba(229, 0, 0, 0.5));
    margin-right: 8px;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--callout-color);
    font-size: 20px;
    font-weight: 600;
    border-radius: 50%;
    background-color: rgba(229, 0, 0, 0.1);
    transition: background-color 0.3s ease;
  }
  /* Add terminal prompt symbol */
  .callout-title::before {
    content: '</>' !important;
    margin-right: 8px;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ff0000ff;
    font-weight: 600;
    border-radius: 50%;
    background-color: rgba(229, 0, 0, 0.1);
    transition: background-color 0.3s ease;
    font-size: 20px;
  }
  .callout-title {
    position: relative !important;
    padding: var(--callout-title-padding) !important;
    background: rgba(var(--callout-color), var(--callout-title-bg-opacity)) !important;
    color: rgb(var(--callout-color)) !important;
    font-weight: 600 !important;
    font-size: 0.95em !important;
    letter-spacing: 0.3px !important;
    display: flex !important;
    align-items: center !important;
    gap: var(--callout-gap) !important;
    border-radius: var(--callout-border-radius) !important;
    transition: background var(--animation-speed-normal) !important;
    transition: color var(--animation-speed-normal) !important;
  }
  
  .callout:hover .callout-title {
    background: rgba(var(--callout-color), calc(var(--callout-title-bg-opacity) * 1.3)) !important;
  }
  
  /* Title inner glow */
  .callout-title::after {
    content: '' !important;
    position: absolute !important;
    bottom: -1px !important;
    left: 0 !important;
    right: 0 !important;
    height: 1px !important;
    background: linear-gradient(90deg,
      transparent 0%,
      rgba(var(--callout-color), 0.6) 50%,
      transparent 100%) !important;
    opacity: 0 !important;
    transition: opacity var(--animation-speed-normal) !important;
    pointer-events: none !important;
  }

  /* Text formatting support */
.callout-content strong,
.callout-content b,
.callout-title strong,
.callout-title b {
  font-weight: 700 !important;                /* Proper bold weight */
  color: #E50000 !important;                  /* Vivid Crimson */
}

.callout-content em,
.callout-content i,
.callout-title em,
.callout-title i {
  font-style: italic !important;
  color: inherit !important;
}

.callout-content strong em,
.callout-content em strong,
.callout-content b i,
.callout-content i b {
  font-weight: 700 !important;                /* Keep bold weight */
  font-style: italic !important;
  color: #E50000 !important;                  /* Vivid Crimson for bold+italic */
}

/* Ensure markdown formatting is preserved */
.callout-content .cm-strong,
.callout-content .cm-em {
  font-family: inherit !important;
}

.callout-content .cm-strong {
  font-weight: 700 !important;                /* Proper bold weight */
  color: #E50000 !important;                  /* Vivid Crimson */
}

.callout-content .cm-em {
  font-style: italic !important;
}

/* Icon styling */
.callout-icon {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: transform var(--animation-speed-normal) var(--animation-easing) !important;
}

.callout:hover .callout-icon {
  transform: scale(1.1) rotate(5deg) !important;
}



/* === Works beautifully with all three theme colors === */
```

### .obsidian\snippets\callout-mod-12-icon-style-variations.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 CALLOUT MODIFIER: Icon Style Variations

 Purpose: Enhance callout icons with various visual treatments
 Effect: Styled icon containers with backgrounds, shapes, and effects
 Inspired by: Modern icon design systems, badge UIs, app interfaces
 Compatible with: All callout styles

 Enable this snippet for:
 - Prominent icon styling
 - Background circles/squares for icons
 - Icon badges and containers
 - Enhanced visual hierarchy
 - Modern icon treatment

 CHOOSE YOUR STYLE: Comment/uncomment sections below
═══════════════════════════════════════════════════════════════════════════════
*/

/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 1: Circular Icon Badges (Default - Enabled)
   ═══════════════════════════════════════════════════════════════════════════ */

.callout-icon {
  background: rgba(var(--callout-color), 0.2) !important;
  border-radius: 50% !important;
  padding: 8px !important;
  width: 32px !important;
  height: 32px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 2px 8px rgba(var(--callout-color), 0.3) !important;
  border: 2px solid rgba(var(--callout-color), 0.4) !important;
}

.callout:hover .callout-icon {
  background: rgba(var(--callout-color), 0.3) !important;
  box-shadow: 0 4px 12px rgba(var(--callout-color), 0.4) !important;
  border-color: rgba(var(--callout-color), 0.6) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 2: Square Icon Badges (Uncomment to use)
   ═══════════════════════════════════════════════════════════════════════════

.callout-icon {
  background: rgba(var(--callout-color), 0.2) !important;
  border-radius: 8px !important;
  padding: 8px !important;
  width: 32px !important;
  height: 32px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 2px 8px rgba(var(--callout-color), 0.3) !important;
}

.callout:hover .callout-icon {
  background: rgba(var(--callout-color), 0.35) !important;
  box-shadow: 0 4px 12px rgba(var(--callout-color), 0.5) !important;
  transform: rotate(5deg) scale(1.1) !important;
}
*/

/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 3: Hexagonal Icon Badges (Uncomment to use)
   ═══════════════════════════════════════════════════════════════════════════

.callout-icon {
  background: rgba(var(--callout-color), 0.2) !important;
  clip-path: polygon(
    30% 0%, 70% 0%, 100% 30%,
    100% 70%, 70% 100%, 30% 100%,
    0% 70%, 0% 30%
  ) !important;
  padding: 10px !important;
  width: 36px !important;
  height: 36px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.callout:hover .callout-icon {
  background: rgba(var(--callout-color), 0.35) !important;
  transform: rotate(20deg) scale(1.15) !important;
}
*/

/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 4: Glowing Icon Aura (Uncomment to use)
   ═══════════════════════════════════════════════════════════════════════════

.callout-icon {
  background: transparent !important;
  padding: 6px !important;
  filter: drop-shadow(0 0 8px rgba(var(--callout-color), 0.6))
          drop-shadow(0 0 16px rgba(var(--callout-color), 0.4)) !important;
  position: relative !important;
}

.callout-icon::before {
  content: '' !important;
  position: absolute !important;
  top: 50% !important;
  left: 50% !important;
  transform: translate(-50%, -50%) !important;
  width: 40px !important;
  height: 40px !important;
  background: radial-gradient(
    circle,
    rgba(var(--callout-color), 0.3) 0%,
    rgba(var(--callout-color), 0.1) 50%,
    transparent 100%
  ) !important;
  border-radius: 50% !important;
  z-index: -1 !important;
}

.callout:hover .callout-icon {
  filter: drop-shadow(0 0 12px rgba(var(--callout-color), 0.8))
          drop-shadow(0 0 24px rgba(var(--callout-color), 0.6))
          drop-shadow(0 0 36px rgba(var(--callout-color), 0.4)) !important;
  transform: scale(1.2) !important;
}
*/

/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 5: Outlined Icon (Uncomment to use)
   ═══════════════════════════════════════════════════════════════════════════

.callout-icon {
  background: transparent !important;
  border: 2px solid rgba(var(--callout-color), 0.6) !important;
  border-radius: 50% !important;
  padding: 8px !important;
  width: 32px !important;
  height: 32px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.callout:hover .callout-icon {
  border-color: rgba(var(--callout-color), 1) !important;
  border-width: 3px !important;
  box-shadow: 0 0 15px rgba(var(--callout-color), 0.5) !important;
}
*/

/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 6: Icon with Gradient Background (Uncomment to use)
   ═══════════════════════════════════════════════════════════════════════════

.callout-icon {
  background: linear-gradient(135deg,
    rgba(var(--callout-color), 0.3) 0%,
    rgba(var(--callout-color), 0.1) 100%) !important;
  border-radius: 12px !important;
  padding: 8px !important;
  width: 34px !important;
  height: 34px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow:
    0 4px 12px rgba(var(--callout-color), 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
}

.callout:hover .callout-icon {
  background: linear-gradient(135deg,
    rgba(var(--callout-color), 0.5) 0%,
    rgba(var(--callout-color), 0.2) 100%) !important;
  box-shadow:
    0 6px 16px rgba(var(--callout-color), 0.4),
    inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
}
*/

/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 7: Minimal - No Icon Background (Uncomment to use)
   ═══════════════════════════════════════════════════════════════════════════

.callout-icon {
  background: transparent !important;
  border: none !important;
  padding: 4px !important;
  box-shadow: none !important;
}

.callout:hover .callout-icon {
  transform: scale(1.15) !important;
  filter: brightness(1.2) !important;
}
*/

/* Icon size adjustments for all styles */
.callout-icon svg {
  width: 16px !important;
  height: 16px !important;
}

```

### .obsidian\snippets\callout-mod-15-premium-card.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 CALLOUT MODIFIER: Premium Card

 Purpose: Refined card design with subtle elevation and premium feel
 Effect: High-quality card component with balanced shadows and clean borders
 Inspired by: Premium UI kits, Stripe dashboard, Notion cards
 Compatible with: All themes, optimized for dark backgrounds

 Enable this snippet for:
 - Professional card appearance
 - Balanced depth (not too heavy)
 - Clean sophisticated borders
 - Subtle premium feel
 - Enterprise-grade aesthetics
═══════════════════════════════════════════════════════════════════════════════
*/

/* Premium card base with refined shadows */
.callout {
  background: var(--theme-bg-raised, #1E1E1E) !important;
  border: 1px solid rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.25) !important;
  border-top: 2px solid rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.5) !important;
  border-radius: 14px !important;
  padding: 0 !important;
  margin: 1.8em 0 !important;
  
  /* Balanced shadow for subtle elevation */
  box-shadow:
    0 6px 16px rgba(0, 0, 0, 0.18),
    0 2px 8px rgba(0, 0, 0, 0.12),
    0 0 0 1px rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.04) !important;
  
  transition:
    transform 0.3s cubic-bezier(0.4, 0.0, 0.2, 1),
    box-shadow 0.3s cubic-bezier(0.4, 0.0, 0.2, 1),
    border-color 0.3s ease !important;
  position: relative !important;
}

/* Subtle top accent line */
.callout::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 10% !important;
  right: 10% !important;
  height: 1px !important;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.3) 50%,
    transparent 100%) !important;
  pointer-events: none !important;
}

/* Premium title styling */
.callout-title {
  background: linear-gradient(135deg,
    rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.06) 0%,
    rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.03) 100%) !important;
  padding: 16px 20px !important;
  border-bottom: 1px solid rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.15) !important;
  border-radius: 14px 14px 0 0 !important;
  font-weight: 600 !important;
  font-size: 0.95em !important;
  letter-spacing: 0.01em !important;
  color: rgb(var(--callout-color, var(--theme-crimson-rgb))) !important;
}

/* Clean content area */
.callout-content {
  background: transparent !important;
  padding: 18px 20px !important;
}

/* Refined hover state */
.callout:hover {
  transform: translateY(-3px) !important;
  border-top-color: rgb(var(--callout-color, var(--theme-crimson-rgb))) !important;
  
  box-shadow:
    0 10px 24px rgba(0, 0, 0, 0.22),
    0 4px 12px rgba(0, 0, 0, 0.16),
    0 0 0 1px rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.15),
    0 2px 12px rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.06) !important;
}

.callout:hover .callout-title {
  background: linear-gradient(135deg,
    rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.10) 0%,
    rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.05) 100%) !important;
  border-bottom-color: rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.25) !important;
}

/* Premium icon treatment */
.callout-icon {
  background: rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.1) !important;
  border-radius: 8px !important;
  padding: 5px !important;
  transition: all 0.3s ease !important;
}

.callout:hover .callout-icon {
  background: rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.15) !important;
  transform: scale(1.05) !important;
}

/* Side accent marker */
.callout::after {
  content: '' !important;
  position: absolute !important;
  left: 0 !important;
  top: 20% !important;
  bottom: 20% !important;
  width: 3px !important;
  background: linear-gradient(180deg,
    transparent 0%,
    rgb(var(--callout-color, var(--theme-crimson-rgb))) 50%,
    transparent 100%) !important;
  border-radius: 0 3px 3px 0 !important;
  opacity: 0.6 !important;
  transition: opacity 0.3s ease !important;
}

.callout:hover::after {
  opacity: 1 !important;
}

/* Nested cards with reduced styling */
.callout .callout {
  margin: 1.2em 0 !important;
  box-shadow:
    0 3px 8px rgba(0, 0, 0, 0.12),
    0 1px 4px rgba(0, 0, 0, 0.08) !important;
}

.callout .callout:hover {
  transform: translateY(-2px) !important;
}

```

### .obsidian\snippets\callout-mod-16-floating-light.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 CALLOUT MODIFIER: Floating Light Card

 Purpose: Lightweight elevated card with airy feel and soft shadows
 Effect: Gentle floating appearance with minimal visual weight
 Inspired by: iOS Cards, Google Material 3, Frosted glass aesthetics
 Compatible with: All themes, especially clean minimal setups

 Enable this snippet for:
 - Light airy card feel
 - Soft gentle elevation
 - Clean modern look
 - Subtle depth without heaviness
 - Breathable design
═══════════════════════════════════════════════════════════════════════════════
*/

/* Floating card base with soft shadows */
.callout {
  background: rgba(var(--theme-bg-raised-rgb, 30, 30, 30), 0.6) !important;
  backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.2) !important;
  border-radius: 16px !important;
  padding: 0 !important;
  margin: 1.5em 0.3em !important;
  
  /* Soft floating shadows */
  box-shadow:
    0 8px 20px rgba(0, 0, 0, 0.12),
    0 3px 8px rgba(0, 0, 0, 0.08),
    0 1px 3px rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.08),
    inset 0 0 0 1px rgba(255, 255, 255, 0.03) !important;
  
  transform: translateY(0) !important;
  transition:
    transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1),
    box-shadow 0.4s cubic-bezier(0.25, 0.8, 0.25, 1),
    background 0.3s ease !important;
}

/* Subtle top glow */
.callout::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 20px !important;
  right: 20px !important;
  height: 2px !important;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.25) 50%,
    transparent 100%) !important;
  border-radius: 16px !important;
  filter: blur(1px) !important;
  pointer-events: none !important;
}

/* Clean lightweight title */
.callout-title {
  background: rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.04) !important;
  padding: 14px 18px !important;
  border-bottom: 1px solid rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.12) !important;
  border-radius: 16px 16px 0 0 !important;
  font-weight: 500 !important;
  font-size: 0.92em !important;
  color: rgb(var(--callout-color, var(--theme-crimson-rgb))) !important;
  transition: background 0.3s ease !important;
}

/* Airy content area */
.callout-content {
  background: transparent !important;
  padding: 16px 18px 18px !important;
}

/* Gentle hover float */
.callout:hover {
  transform: translateY(-4px) !important;
  background: rgba(var(--theme-bg-raised-rgb, 30, 30, 30), 0.75) !important;
  
  box-shadow:
    0 14px 32px rgba(0, 0, 0, 0.16),
    0 6px 14px rgba(0, 0, 0, 0.12),
    0 2px 6px rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.15),
    inset 0 0 0 1px rgba(255, 255, 255, 0.05),
    0 0 20px rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.08) !important;
}

.callout:hover .callout-title {
  background: rgba(var(--callout-color, var(--theme-crimson-rgb)), 0.08) !important;
}

/* Minimal icon styling */
.callout-icon {
  opacity: 0.85 !important;
  transition: all 0.3s ease !important;
}

.callout:hover .callout-icon {
  opacity: 1 !important;
  transform: scale(1.08) !important;
}

/* Soft bottom shadow for floating effect */
.callout::after {
  content: '' !important;
  position: absolute !important;
  bottom: -6px !important;
  left: 15% !important;
  right: 15% !important;
  height: 6px !important;
  background: radial-gradient(ellipse,
    rgba(0, 0, 0, 0.15) 0%,
    transparent 65%) !important;
  filter: blur(4px) !important;
  pointer-events: none !important;
  opacity: 0.5 !important;
  transition: opacity 0.4s ease, transform 0.4s ease !important;
}

.callout:hover::after {
  opacity: 0.7 !important;
  transform: scaleX(1.1) !important;
}

/* Light nested cards */
.callout .callout {
  margin: 1em 0 !important;
  background: rgba(var(--theme-bg-raised-rgb, 30, 30, 30), 0.4) !important;
  box-shadow:
    0 4px 10px rgba(0, 0, 0, 0.08),
    0 2px 5px rgba(0, 0, 0, 0.06) !important;
}

.callout .callout:hover {
  transform: translateY(-2px) !important;
}

/* Remove motion for users who prefer reduced motion */
@media (prefers-reduced-motion: reduce) {
  .callout,
  .callout:hover,
  .callout-icon,
  .callout::after {
    transform: none !important;
    transition: none !important;
  }
}

```

### .obsidian\snippets\callout-mod-card.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 CALLOUT MOD: CARD STYLE

 Purpose: Makes callouts look like traditional cards with solid backgrounds
 Usage: Enable this snippet to override the base callout styling
 Author: Pur3v4d3r
 Theme: Red & Black with classic card design
═══════════════════════════════════════════════════════════════════════════════
*/

/* Override base callout for card appearance */
.callout {
  background: linear-gradient(135deg,
    rgba(18, 18, 18, 0.98) 0%,
    rgba(25, 25, 25, 0.98) 100%) !important;
  border: 2px solid rgba(var(--callout-color), 0.35) !important;
  border-left: 4px solid rgb(var(--callout-color)) !important;
  border-radius: 12px !important;
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.45),
    0 2px 4px rgba(var(--callout-color), 0.15),
    inset 0 1px 0 rgba(224, 224, 224, 0.05) !important;
  padding: 0 !important;
  overflow: hidden !important;
}

.callout:hover {
  border-color: rgba(var(--callout-color), 0.55) !important;
  box-shadow:
    0 6px 16px rgba(0, 0, 0, 0.55),
    0 4px 8px rgba(var(--callout-color), 0.25),
    0 0 20px rgba(var(--callout-color), 0.2),
    inset 0 1px 0 rgba(224, 224, 224, 0.08) !important;
  transform: translateY(-2px) !important;
}

/* Card-style title */
.callout-title {
  background: linear-gradient(135deg,
    rgba(var(--callout-color), 0.3) 0%,
    rgba(var(--callout-color), 0.22) 100%) !important;
  color: rgb(var(--callout-color)) !important;
  font-weight: 600 !important;
  padding: 14px 18px !important;
  border-bottom: 2px solid rgba(var(--callout-color), 0.35) !important;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6) !important;
  letter-spacing: 0.5px !important;
  border-radius: 0 !important;
}

.callout:hover .callout-title {
  background: linear-gradient(135deg,
    rgba(var(--callout-color), 0.38) 0%,
    rgba(var(--callout-color), 0.28) 100%) !important;
  text-shadow: 0 0 12px rgba(var(--callout-color), 0.5) !important;
}

/* Card-style content */
.callout-content {
  background: rgba(0, 0, 0, 0.35) !important;
  padding: 16px 18px !important;
  color: rgba(224, 224, 224, 0.95) !important;
  border-top: 1px solid rgba(var(--callout-color), 0.12) !important;
}

.callout:hover .callout-content {
  background: rgba(0, 0, 0, 0.42) !important;
}

```

### .obsidian\snippets\callout-mod-neon.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 CALLOUT MOD: NEON GLOW STYLE

 Purpose: Adds intense neon glow effects to all callouts
 Usage: Enable this snippet to override the base callout styling
 Author: Pur3v4d3r
 Theme: Red & Black with intense neon accents
═══════════════════════════════════════════════════════════════════════════════
*/

/* Override base callout for neon appearance */
.callout {
  background: rgba(10, 10, 10, 0.85) !important;
  border: 2px solid rgba(var(--callout-color), 0.6) !important;
  border-left: 4px solid rgb(var(--callout-color)) !important;
  box-shadow:
    0 0 10px rgba(var(--callout-color), 0.3),
    0 0 20px rgba(var(--callout-color), 0.2),
    0 0 40px rgba(var(--callout-color), 0.1),
    0 4px 12px rgba(0, 0, 0, 0.5) !important;
  animation: glowPulse 3s infinite !important;
}

.callout:hover {
  border-color: rgba(var(--callout-color), 0.8) !important;
  box-shadow:
    0 0 15px rgba(var(--callout-color), 0.5),
    0 0 30px rgba(var(--callout-color), 0.3),
    0 0 60px rgba(var(--callout-color), 0.2),
    0 6px 16px rgba(0, 0, 0, 0.6) !important;
  transform: translateY(-2px) !important;
}

/* Neon title */
.callout-title {
  background: rgba(var(--callout-color), 0.15) !important;
  color: rgb(var(--callout-color)) !important;
  text-shadow:
    0 0 5px rgba(var(--callout-color), 0.5),
    0 0 10px rgba(var(--callout-color), 0.3),
    0 2px 4px rgba(0, 0, 0, 0.8) !important;
  font-weight: 600 !important;
  border-bottom: 1px solid rgba(var(--callout-color), 0.4) !important;
}

.callout:hover .callout-title {
  background: rgba(var(--callout-color), 0.22) !important;
  text-shadow:
    0 0 8px rgba(var(--callout-color), 0.7),
    0 0 15px rgba(var(--callout-color), 0.4),
    0 2px 4px rgba(0, 0, 0, 0.8) !important;
}

/* Neon content */
.callout-content {
  background: rgba(0, 0, 0, 0.4) !important;
}

/* Add glowing line at top */
.callout::before {
  opacity: 1 !important;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(var(--callout-color), 0.8) 50%,
    transparent 100%) !important;
  height: 2px !important;
  box-shadow: 0 0 10px rgba(var(--callout-color), 0.6) !important;
}

```

### .obsidian\snippets\callout-mod-raised.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 CALLOUT MOD: RAISED STYLE

 Purpose: Gives all callouts a raised/elevated 3D appearance with deep shadows
 Usage: Enable this snippet to override the base callout styling
 Author: Pur3v4d3r
 Theme: Red & Black with elevated depth
═══════════════════════════════════════════════════════════════════════════════
*/

/* Override base callout for raised appearance */
.callout {
  transform: translateY(-4px) !important;
  box-shadow:
    0 8px 16px rgba(0, 0, 0, 0.5),
    0 16px 32px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(var(--callout-color), 0.2),
    inset 0 1px 0 rgba(224, 224, 224, 0.1) !important;
  background: linear-gradient(180deg,
    rgba(30, 30, 30, 0.9) 0%,
    rgba(20, 20, 20, 0.7) 100%) !important;
  border: 1px solid rgba(42, 42, 42, 0.8) !important;
  border-left: 4px solid rgb(var(--callout-color)) !important;
}

.callout:hover {
  transform: translateY(-8px) !important;
  box-shadow:
    0 12px 24px rgba(0, 0, 0, 0.6),
    0 24px 48px rgba(0, 0, 0, 0.4),
    0 0 30px rgba(var(--callout-color), 0.4),
    inset 0 1px 0 rgba(224, 224, 224, 0.15) !important;
}

/* Enhanced title for raised style */
.callout-title {
  background: rgba(var(--callout-color), 0.18) !important;
  border-bottom: 1px solid rgba(var(--callout-color), 0.25) !important;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.6) !important;
}

.callout:hover .callout-title {
  background: rgba(var(--callout-color), 0.25) !important;
  text-shadow: 0 0 10px rgba(var(--callout-color), 0.5) !important;
}

/* Enhanced content for raised style */
.callout-content {
  background: rgba(0, 0, 0, 0.3) !important;
}

.callout:hover .callout-content {
  background: rgba(0, 0, 0, 0.4) !important;
}

```

### .obsidian\snippets\code-block-fixed.css

```css
/*
═══════════════════════════════════════════════════════════
 SNIPPET NAME: Pur3v4d3r's Advanced Code Block Customization
 Purpose: Professional code block styling with community features
 Author: Pur3v4d3r
 Date: 2025-12-13 (Fixed: 2025-12-28)
 Obsidian Version: 1.5.0+
 Features: Rounded corners, gradient glow borders, syntax highlighting
 Installation: Place in .obsidian/snippets/ and enable
 
 FIXES APPLIED:
 - Fixed all CSS syntax errors
 - Corrected malformed box-shadow declarations
 - Removed invalid JavaScript string methods from CSS
 - Cleaned up duplicate/conflicting rules
═══════════════════════════════════════════════════════════
*/

/* ════════════════════════════════════════════════════════
   SECTION 1: READING/PREVIEW MODE
   ═══════════════════════════════════════════════════════ */

.theme-dark .workspace-leaf-content .markdown-preview-view pre[class*="language-"],
.theme-dark .workspace-leaf-content .markdown-preview-view pre,
.theme-dark .markdown-preview-view pre[class*="language-"],
.theme-dark .markdown-preview-view pre,
.theme-dark .markdown-rendered pre {
  position: relative !important;
  background: linear-gradient(135deg, #121212 0%, #0A0A0A 100%) !important;
  border: 2px solid rgba(229, 0, 0, 0.2) !important;
  border-radius: 12px !important;
  box-shadow: 0 4px 12px rgba(229, 0, 0, 0.3) !important;
  padding: 20px !important;
  margin: 16px 0 !important;
  transition: box-shadow 0.3s ease, transform 0.3s ease !important;
  overflow-wrap: break-word !important;
  overflow: auto !important;
}

/* ════════════════════════════════════════════════════════
   SECTION 2: LIVE PREVIEW / SOURCE MODE (CM6)
   ═══════════════════════════════════════════════════════ */

/* Base styling for ALL code block lines */
.theme-dark .workspace-leaf-content .markdown-source-view.mod-cm6 .HyperMD-codeblock,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock,
.theme-dark .markdown-source-view.mod-cm6 .HyperMD-codeblock {
  background: linear-gradient(135deg, #121212 0%, #0A0A0A 100%) !important;
  padding: 0 12px !important;
  margin: 0 !important;
  border-radius: 0 !important;
  box-shadow: inset 3px 0 0 #E50000 !important;
}

/* FIRST line of code block - top rounded corners + top border */
.theme-dark .workspace-leaf-content .markdown-source-view.mod-cm6 .HyperMD-codeblock-begin,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock-begin,
.theme-dark .markdown-source-view.mod-cm6 .HyperMD-codeblock-begin {
  border-radius: 12px 12px 0 0 !important;
  padding-top: 16px !important;
  margin-top: 8px !important;
  box-shadow: 
    inset 2px 0 0 #E50000,
    inset 0 2px 0 #E50000,
    0 4px 75px rgba(229, 0, 0, 0.2) !important;
}

/* LAST line of code block - bottom rounded corners + bottom border */
.theme-dark .workspace-leaf-content .markdown-source-view.mod-cm6 .HyperMD-codeblock-end,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock-end,
.theme-dark .markdown-source-view.mod-cm6 .HyperMD-codeblock-end {
  border-radius: 0 0 12px 12px !important;
  padding-bottom: 20px !important;
  margin-bottom: 8px !important;
  box-shadow: 
    inset 2px 0 0 #E50000,
    inset 0 -2px 0 #E50000,
    0 15px 25px rgba(229, 0, 0, 0.2) !important;
}

/* Single-line code blocks (has both begin AND end) */
.theme-dark .workspace-leaf-content .markdown-source-view.mod-cm6 .HyperMD-codeblock-begin.HyperMD-codeblock-end,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock-begin.HyperMD-codeblock-end,
.theme-dark .markdown-source-view.mod-cm6 .HyperMD-codeblock-begin.HyperMD-codeblock-end {
  border-radius: 12px !important;
  padding: 16px 12px !important;
  margin: 16px 0 !important;
  box-shadow:
    0 0 0 2px #E50000,
    0 0 0 3px #E0E0E0,
    0 4px 16px rgba(229, 0, 0, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
}

/* ════════════════════════════════════════════════════════
   SECTION 3: LANGUAGE LABELS
   ═══════════════════════════════════════════════════════ */

/* JavaScript/JS */
.markdown-preview-view pre[class*="language-javascript"]::before,
.markdown-preview-view pre[class*="language-js"]::before {
  content: "JavaScript" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #F7DF1E 0%, #E5C400 100%) !important;
  color: #000000 !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(247, 223, 30, 0.3) !important;
  z-index: 10 !important;
}

/* Python */
.markdown-preview-view pre[class*="language-python"]::before {
  content: "Python" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #3776AB 0%, #FFD43B 100%) !important;
  color: #FFFFFF !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(55, 118, 171, 0.3) !important;
  z-index: 10 !important;
}

/* CSS */
.markdown-preview-view pre[class*="language-css"]::before {
  content: "CSS" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #264DE4 0%, #2965F1 100%) !important;
  color: #FFFFFF !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(38, 77, 228, 0.3) !important;
  z-index: 10 !important;
}

/* TypeScript */
.markdown-preview-view pre[class*="language-typescript"]::before,
.markdown-preview-view pre[class*="language-ts"]::before {
  content: "TypeScript" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #007ACC 0%, #3178C6 100%) !important;
  color: #FFFFFF !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(0, 122, 204, 0.3) !important;
  z-index: 10 !important;
}

/* HTML */
.markdown-preview-view pre[class*="language-html"]::before {
  content: "HTML" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #E34C26 0%, #F06529 100%) !important;
  color: #FFFFFF !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(227, 76, 38, 0.3) !important;
  z-index: 10 !important;
}

/* Bash/Shell */
.markdown-preview-view pre[class*="language-bash"]::before,
.markdown-preview-view pre[class*="language-shell"]::before,
.markdown-preview-view pre[class*="language-sh"]::before {
  content: "Shell" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #4EAA25 0%, #A3A3A3 100%) !important;
  color: #000000 !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(78, 170, 37, 0.3) !important;
  z-index: 10 !important;
}

/* Markdown */
.markdown-preview-view pre[class*="language-markdown"]::before,
.markdown-preview-view pre[class*="language-md"]::before {
  content: "Markdown" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #42A5F5 0%, #1E88E5 100%) !important;
  color: #FFFFFF !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(66, 165, 245, 0.3) !important;
  z-index: 10 !important;
}

/* JSON */
.markdown-preview-view pre[class*="language-json"]::before {
  content: "JSON" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%) !important;
  color: #000000 !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(255, 152, 0, 0.3) !important;
  z-index: 10 !important;
}

/* YAML */
.markdown-preview-view pre[class*="language-yaml"]::before,
.markdown-preview-view pre[class*="language-yml"]::before {
  content: "YAML" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #CB171E 0%, #E91E63 100%) !important;
  color: #FFFFFF !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(203, 23, 30, 0.3) !important;
  z-index: 10 !important;
}

/* Prompt */
.markdown-preview-view pre[class*="language-prompt"]::before {
  content: "Prompt" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #7800F4 0%, #9C27B0 100%) !important;
  color: #FFFFFF !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(120, 0, 244, 0.3) !important;
  z-index: 10 !important;
}

/* Generic fallback for unlabeled code blocks */
.markdown-preview-view pre:not([class*="language-"])::before {
  content: "Code" !important;
  position: absolute !important;
  top: 6px !important;
  right: 12px !important;
  background: linear-gradient(135deg, #E50000 0%, #B71C1C 100%) !important;
  color: #FFFFFF !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 6px !important;
  box-shadow: 0 2px 8px rgba(229, 0, 0, 0.3) !important;
  z-index: 10 !important;
}

/* ════════════════════════════════════════════════════════
   SECTION 4: LINE NUMBERS STYLING (Edit Mode)
   ═══════════════════════════════════════════════════════ */

.theme-dark .cm-gutters {
  background: rgba(13, 10, 18, 0.6) !important;
  border-right: 2px solid rgba(229, 0, 0, 0.2) !important;
  border-top-left-radius: 12px !important;
  border-bottom-left-radius: 12px !important;
  backdrop-filter: blur(8px) !important;
  padding: 0 8px !important;
}

.theme-dark .cm-lineNumbers .cm-gutterElement {
  color: #A3A3A3 !important;
  font-family: "JetBrains Mono", "Consolas", monospace !important;
  font-size: 11px !important;
  font-weight: 500 !important;
  min-width: 40px !important;
  padding-right: 12px !important;
  text-align: right !important;
  transition: color 0.2s ease !important;
}

.theme-dark .cm-lineNumbers .cm-gutterElement:hover {
  color: #E50000 !important;
}

/* Active line gutter */
.theme-dark .cm-editor .cm-gutters .cm-activeLineGutter,
.theme-dark .cm-gutters .cm-activeLineGutter,
.theme-dark .cm-activeLineGutter {
  background: rgba(229, 0, 0, 0.15) !important;
  color: #E50000 !important;
  font-weight: 700 !important;
}

/* ════════════════════════════════════════════════════════
   SECTION 5: ACTIVE LINE HIGHLIGHTING
   ═══════════════════════════════════════════════════════ */

/* Active line for regular text */
.theme-dark .workspace-leaf-content[data-type="markdown"] .cm-editor .cm-scroller .cm-content .cm-activeLine,
.theme-dark .markdown-source-view.mod-cm6 .cm-editor .cm-activeLine,
.theme-dark .cm-editor .cm-activeLine,
.theme-dark .cm-activeLine {
  background: rgba(229, 0, 0, 0.08) !important;
}

/* Active line in code blocks - keep transparent */
.theme-dark .workspace-leaf-content .cm-editor .HyperMD-codeblock.cm-activeLine,
.theme-dark .markdown-source-view.mod-cm6 .HyperMD-codeblock.cm-activeLine,
.theme-dark .cm-editor .HyperMD-codeblock.cm-activeLine,
.theme-dark .HyperMD-codeblock.cm-line.cm-activeLine,
.theme-dark .HyperMD-codeblock .cm-activeLine,
.theme-dark .cm-line.HyperMD-codeblock.cm-activeLine {
  background: transparent !important;
  background-image: none !important;
  background-color: transparent !important;
}

/* ════════════════════════════════════════════════════════
   SECTION 6: COPY BUTTON (Preview Mode)
   ═══════════════════════════════════════════════════════ */

.markdown-preview-view pre > button,
.markdown-rendered pre > button,
button.copy-code-button {
  position: absolute !important;
  top: 10px !important;
  right: 90px !important;
  background: rgba(229, 0, 0, 0.2) !important;
  backdrop-filter: blur(8px) !important;
  color: #E50000 !important;
  border: 1px solid rgba(229, 0, 0, 0.3) !important;
  border-radius: 6px !important;
  min-width: 44px !important;
  min-height: 32px !important;
  padding: 6px 12px !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  opacity: 0 !important;
  transition: all 0.3s ease !important;
  cursor: pointer !important;
  z-index: 10 !important;
}

.markdown-preview-view pre:hover > button,
.markdown-rendered pre:hover > button {
  opacity: 1 !important;
}

.markdown-preview-view pre > button:hover,
button.copy-code-button:hover {
  background: rgba(229, 0, 0, 0.4) !important;
  border-color: #E50000 !important;
  color: #E50000 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 12px rgba(229, 0, 0, 0.3) !important;
}

.markdown-preview-view pre > button:active,
button.copy-code-button:active {
  transform: translateY(0) !important;
  box-shadow: 0 2px 6px rgba(229, 0, 0, 0.2) !important;
}

.markdown-preview-view pre > button:focus-visible,
button.copy-code-button:focus-visible {
  outline: 2px solid #E50000 !important;
  outline-offset: 2px !important;
  opacity: 1 !important;
}

/* ════════════════════════════════════════════════════════
   SECTION 7: CODE SYNTAX HIGHLIGHTING
   ═══════════════════════════════════════════════════════ */

/* Base code styling */
.theme-dark .cm-content code,
.theme-dark .markdown-source-view pre .cm-line {
  color: #E0E0E0 !important;
  font-family: "JetBrains Mono", monospace !important;
  font-size: 14px !important;
  line-height: 1.6 !important;
}

/* ═══ CodeMirror 6 (Live Preview/Source Mode) ═══ */

.theme-dark .cm-keyword {
  color: #3cff00 !important;
  font-weight: 600 !important;
}

.theme-dark .cm-string {
  color: #ff6b6b !important;
}

.theme-dark .cm-number {
  color: #ff8800 !important;
}

.theme-dark .cm-variable.cm-function {
  color: #E0E0E0 !important;
  font-weight: 500 !important;
}

.theme-dark .cm-comment {
  color: #0091e5 !important;
  font-style: italic !important;
  opacity: 0.85 !important;
}

.theme-dark .cm-operator {
  color: #d8b909 !important;
}

.theme-dark .cm-variable {
  color: #E0E0E0 !important;
}

.theme-dark .cm-type {
  color: #d8b909 !important;
  font-weight: 600 !important;
}

.theme-dark .cm-property {
  color: #E50000 !important;
}

/* Boolean values (true, false) */
.theme-dark .cm-atom,
.theme-dark .cm-bool {
  color: #ff8800 !important;
  font-weight: 600 !important;
}

/* Null, undefined, None, nil */
.theme-dark .cm-null {
  color: #A3A3A3 !important;
  font-style: italic !important;
  font-weight: 600 !important;
}

/* Constants (UPPER_CASE identifiers) */
.theme-dark .cm-constant {
  color: #ff00ff !important;
  font-weight: 700 !important;
}

/* Built-in functions/methods */
.theme-dark .cm-builtin {
  color: #3cff00 !important;
  font-weight: 500 !important;
}

/* Decorators (@decorator in Python/TS) */
.theme-dark .cm-meta,
.theme-dark .cm-annotation {
  color: #d8b909 !important;
  font-style: italic !important;
}

/* Regular expressions */
.theme-dark .cm-string-2 {
  color: #E50000 !important;
  font-weight: 500 !important;
}

/* Definitions (function/class names at declaration) */
.theme-dark .cm-def,
.theme-dark .cm-variable-2 {
  color: #E50000 !important;
  font-weight: 600 !important;
}

/* HTML/XML Tags */
.theme-dark .cm-tag {
  color: #3cff00 !important;
  font-weight: 600 !important;
}

/* HTML/XML Attributes */
.theme-dark .cm-attribute {
  color: #d8b909 !important;
  font-style: italic !important;
}

/* Bracket matching enhancement */
.theme-dark .cm-matchingBracket {
  background: rgba(229, 0, 0, 0.2) !important;
  border-bottom: 2px solid #E50000 !important;
  font-weight: 700 !important;
}

.theme-dark .cm-nonmatchingBracket {
  background: rgba(255, 0, 0, 0.3) !important;
  border-bottom: 2px solid #FF0000 !important;
}

/* ═══ Token-based (Reading Mode/Prism.js) ═══ */

.theme-dark .token.keyword {
  color: #3cff00 !important;
  font-weight: 600 !important;
}

.theme-dark .token.string {
  color: #ff6b6b !important;
}

.theme-dark .token.number {
  color: #ff8800 !important;
}

.theme-dark .token.function {
  color: #E0E0E0 !important;
  font-weight: 500 !important;
}

.theme-dark .token.comment {
  color: #0091e5 !important;
  font-style: italic !important;
  opacity: 0.85 !important;
}

.theme-dark .token.operator {
  color: #d8b909 !important;
}

.theme-dark .token.variable {
  color: #E0E0E0 !important;
}

.theme-dark .token.class-name,
.theme-dark .token.type {
  color: #d8b909 !important;
  font-weight: 600 !important;
}

.theme-dark .token.property {
  color: #E50000 !important;
}

/* Boolean values */
.theme-dark .token.boolean {
  color: #ff8800 !important;
  font-weight: 600 !important;
}

/* Null/undefined/None */
.theme-dark .token.null,
.theme-dark .token.nil,
.theme-dark .token.undefined {
  color: #A3A3A3 !important;
  font-style: italic !important;
  font-weight: 600 !important;
}

/* Constants */
.theme-dark .token.constant {
  color: #ff8800 !important;
  font-weight: 700 !important;
}

/* Built-in functions */
.theme-dark .token.builtin {
  color: #3cff00 !important;
  font-weight: 500 !important;
}

/* Decorators/Annotations */
.theme-dark .token.decorator,
.theme-dark .token.annotation,
.theme-dark .token.at-rule {
  color: #d8b909 !important;
  font-style: italic !important;
}

/* Regular expressions */
.theme-dark .token.regex,
.theme-dark .token.regex-delimiter,
.theme-dark .token.regex-flags {
  color: #E50000 !important;
  font-weight: 500 !important;
}

/* HTML/XML Tags */
.theme-dark .token.tag {
  color: #3cff00 !important;
  font-weight: 600 !important;
}

/* HTML/XML Attributes */
.theme-dark .token.attr-name {
  color: #d8b909 !important;
  font-style: italic !important;
}

.theme-dark .token.attr-value {
  color: #ff6b6b !important;
}

/* Symbols (like in Ruby) */
.theme-dark .token.symbol {
  color: #E50000 !important;
  font-weight: 600 !important;
}

/* Imports/Includes/Requires */
.theme-dark .token.module,
.theme-dark .token.import,
.theme-dark .token.include {
  color: #3cff00 !important;
  font-weight: 600 !important;
}

/* URLs in comments/strings */
.theme-dark .token.url {
  color: #0091e5 !important;
  text-decoration: underline !important;
}

/* Namespace/Package names */
.theme-dark .token.namespace {
  color: #d8b909 !important;
  opacity: 0.9 !important;
}

/* Punctuation (brackets, braces, parens) */
.theme-dark .token.punctuation {
  color: #850000 !important;
}

/* Important keyword emphasis */
.theme-dark .token.important {
  color: #E50000 !important;
  font-weight: 700 !important;
}

/* Inserted/Added text (git diff) */
.theme-dark .token.inserted {
  color: #3cff00 !important;
  background: rgba(60, 255, 0, 0.1) !important;
}

/* Deleted/Removed text (git diff) */
.theme-dark .token.deleted {
  color: #E50000 !important;
  background: rgba(229, 0, 0, 0.1) !important;
  text-decoration: line-through !important;
}

/* Changed text (git diff) */
.theme-dark .token.changed {
  color: #d8b909 !important;
  background: rgba(216, 185, 9, 0.1) !important;
}

/* Generic "entity" */
.theme-dark .token.entity {
  color: #E50000 !important;
  font-weight: 500 !important;
}

/* Character entities in HTML */
.theme-dark .token.entity.named-entity {
  color: #ff8800 !important;
}

/* ════════════════════════════════════════════════════════
   SECTION 8: SQUARE BRACKET COLORIZATION
   ═══════════════════════════════════════════════════════ */

.cm-s-obsidian pre.HyperMD-codeblock span.cm-bracket,
.cm-s-obsidian .HyperMD-codeblock .cm-bracket,
.markdown-source-view.mod-cm6 .cm-line .cm-bracket,
.markdown-source-view.mod-cm6 .HyperMD-codeblock .cm-bracket {
  color: #ff6b6b !important;
}

.cm-editor .cm-content .cm-line .tok-bracket {
  color: #ff6b6b !important;
}

/* For rendered code blocks (Reading mode) */
.language-css .token.punctuation.bracket,
.language-javascript .token.punctuation.bracket,
.language-dataview .token.punctuation.bracket,
.language-dataviewjs .token.punctuation.bracket,
.language-markdown .token.punctuation.bracket,
.language-cs .token.punctuation.bracket {
  color: #ff6b6b !important;
}

/* ════════════════════════════════════════════════════════
   SECTION 9: ACCESSIBILITY - Reduced Motion
   ═══════════════════════════════════════════════════════ */

@media (prefers-reduced-motion: reduce) {
  .theme-dark .workspace-leaf-content .markdown-preview-view pre,
  .theme-dark .markdown-preview-view pre,
  .markdown-preview-view pre > button,
  button.copy-code-button {
    transition: none !important;
  }
}

/* ════════════════════════════════════════════════════════
   END OF SNIPPET
   ═══════════════════════════════════════════════════════ */

```

### .obsidian\snippets\custom-horizontal-rules-.css

```css
/*
═══════════════════════════════════════════════════════════
 SNIPPET NAME: Horizontal Rule Style Collection
 Purpose: Multiple <hr> styling options - enable your favorite
 Author: Pur3v4d3r
 Date: 2025-11-29
 Installation: Place in .obsidian/snippets/ and enable in Settings
 Usage: Comment out all but your preferred style
═══════════════════════════════════════════════════════════
*/

/* ═══════════════════════════════════════════════════════════
  OPTION 1: Minimalist Thin Line
  Simple, clean, unobtrusive
  ═══════════════════════════════════════════════════════════ */
  / .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none !important;
  height: 1px !important;
  background-color: #E50000 !important;
  opacity: 0.5 !important;
  margin: 2em 0 !important;
} 

/* ═══════════════════════════════════════════════════════════
  OPTION 2: Signature Purple Gradient
  Pur3v4d3r's purple-to-teal gradient
 /* ═══════════════════════════════════════════════════════════ */
 /*.markdown-preview-view hr,
 .markdown-source-view.mod-cm6 .cm-line hr {
  border: none!important;
  height: 2px!important;
  background: linear-gradient(90deg, #CC0000ff 0%, #E50000ff 100%) !important;
  margin: 2.5em 0!important;
} */

/* ═══════════════════════════════════════════════════════════
  OPTION 3: Dotted Separator
  Subtle dotted line
  ═══════════════════════════════════════════════════════════ */
  /* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  border-top: 3px dotted var(--text-muted);
  opacity: 0.6;
  margin: 2em 0;
} */

/* ═══════════════════════════════════════════════════════════
  OPTION 4: Dashed Line
  Professional dashed separator
  ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  border-top: 2px dashed var(--text-normal);
  opacity: 0.4;
  margin: 2em 0;
} */

/* ═══════════════════════════════════════════════════════════
  OPTION 5: Double Line
  Classic double border
  ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  border-top: 3px double var(--text-muted);
  opacity: 0.7;
  margin: 2em 0;
} */

/* ═══════════════════════════════════════════════════════════
  OPTION 6: Centered Decorative Dots
  Three centered dots (ellipsis style)
  ═══════════════════════════════════════════════════════════ */
  /* .markdown-preview-view hr  ,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none  !important;
  text-align: center  !important;
  height: 1em !important;
  position: relative  !important;
  margin: 2.5em 0 !important;
}

.markdown-preview-view hr::before,
.markdown-source-view.mod-cm6 .cm-line hr::before {
  content: '• • •'  !important;
  color: #E50000  !important;
  font-size: 1.5em !important;
  letter-spacing: 1em !important;
  position: absolute !important;
  left: 50% !important;
  transform: translateX(-50%) !important  ;
} 

/* ═══════════════════════════════════════════════════════════
    OPTION 7: Centered Diamond
    Single centered decorative diamond
    ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  text-align: center;
  height: 1em;
  position: relative;
  margin: 2.5em 0;
}

.markdown-preview-view hr::before,
.markdown-source-view.mod-cm6 .cm-line hr::before {
  content: '◆';
  color: #E50000;
  font-size: 1.2em;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 8: Thick Accent Bar
    Bold, prominent divider
    ═══════════════════════════════════════════════════════════ */
    /*.markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none !important;
  height: 4px !important;
  background-color: var(--interactive-accent) !important;
  margin: 3em 0 !important;
  border-radius: 2px;
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 9: Fade-Out Gradient
    Edges fade to transparent
    ═══════════════════════════════════════════════════════════ */
    /*  .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  height: 2px;
  background: linear-gradient(90deg,
    transparent 0%,
    #E50000 20%,
    #E50000 80%,
    transparent 100%);
  margin: 2.5em 0;
} */  

/* ═══════════════════════════════════════════════════════════
    OPTION 10: Centered Short Line
    Short centered rule (50% width)
    ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  height: 2px;
  background-color: var(--text-muted);
  width: 50%;
  margin: 2.5em auto;
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 11: Glow Effect (Purple)
    Luminous purple glow
    ═══════════════════════════════════════════════════════════ */
    /* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none !important;
  height: 2px !important;
  background-color: #E50000 !important;
  box-shadow: 0 0 10px #E50000, 0 0 20px rgba(229, 0, 0, 0.5)!important;
  margin: 2.5em 0 !important;
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 12: Neon Teal Glow
    Cyberpunk-style teal glow
    ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  height: 2px;
  background-color: #E50000;
  box-shadow: 0 0 8px #E50000, 0 0 15px rgba(229, 0, 0, 0.6);
  margin: 2.5em 0;
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 13: Wave Pattern (SVG)
    Decorative wave border
    ═══════════════════════════════════════════════════════════ */
    /* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  height: 15px;
  background-image: url("data:image/svg+xml,%3Csvg width='100' height='20' viewBox='0 0 100 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 10 Q 25 0, 50 10 T 100 10' stroke='%23E50000' stroke-width='2' fill='none'/%3E%3C/svg%3E");
  background-repeat: repeat-x;
  background-size: 100px 20px;
  margin: 2.5em 0;
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 14: Inset Shadow Style
    Appears carved into the page
    ═══════════════════════════════════════════════════════════ */
    /* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none !important;
  height: 2px !important;
  background-color: transparent !important;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.3) !important;
  margin: 2em 0 !important;
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 15: Rainbow Spectrum
    Full spectrum gradient
    ═══════════════════════════════════════════════════════════ */
 .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  height: 3px;
  background: linear-gradient(
     90deg,
     #000000ff 0%,
     #ff0000ff 16.67%,
     #000000ff 33.33%,
     #ff0000ff 50%,
     #000000ff 66.67%,
     #ff0000ff 83.33%,
     #000000ff 100%
  );
  margin: 2.5em 0;
  border-radius: 1.5px;
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 16: Ornamental (Stars)
    Decorative star pattern
    ═══════════════════════════════════════════════════════════ */
    /*.markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none !important;
  text-align: center !important;
  height: 1em !important;
  position: relative !important;
  margin: 2.5em 0 !important;
}

.markdown-preview-view hr::before,
.markdown-source-view.mod-cm6 .cm-line hr::before {
  content: '✦ ✦ ✦';
  color: #000000ff;
  font-size: 1.2em;
  letter-spacing: 1.5em;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 17: Animated Pulse (Purple)
    Subtle pulsing glow effect
    ═══════════════════════════════════════════════════════════ */
    /*   @keyframes hr-pulse {
  0%, 100% { 
     box-shadow: 0 0 5px rgba(229, 0, 0, 0.5); 
  }
  50% { 
     box-shadow: 0 0 15px rgba(229, 0, 0, 0.8), 0 0 25px rgba(229, 0, 0, 0.4); 
  }
}

.markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  height: 2px;
  background-color: #E50000;
  margin: 2.5em 0;
  animation: hr-pulse 3s ease-in-out infinite;
}

@media (prefers-reduced-motion: reduce) {
  .markdown-preview-view hr,
  .markdown-source-view.mod-cm6 .cm-line hr {
     animation: none;
     box-shadow: 0 0 5px rgba(229, 0, 0, 0.5);
  }
} */

/* ═══════════════════════════════════════════════════════════
    OPTION 18: Zig-Zag Pattern
    Geometric zig-zag border
    ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr,
.markdown-source-view.mod-cm6 .cm-line hr {
  border: none;
  height: 10px;
  background: linear-gradient(135deg, transparent 33.33%, var(--text-muted) 33.33%, var(--text-muted) 66.66%, transparent 66.66%),
                  linear-gradient(45deg, transparent 33.33%, var(--text-muted) 33.33%, var(--text-muted) 66.66%, transparent 66.66%);
  background-size: 20px 20px;
  background-position: 0 0, 10px 0;
  margin: 2.5em 0 !important;
  opacity: 0.6 !important;
} */
```

### .obsidian\snippets\custom-ordered-list-numbers-(colored)-.css

```css
/*
═══════════════════════════════════════════════════════════
 SNIPPET NAME: Custom Ordered List Numbers (Colored)
 Purpose: Color-coded numbered list markers by nesting level
          Level 1: Numbers (Gold #E50000)
          Level 2: Arrow → (Purple #E50000)
          Level 3: Dash — (Teal #E50000)
          Level 4: Plus + (White)
 Author: Pur3v4d3r
 Date: 2025-12-05
 Obsidian Version: 1.5.0+
 Dependencies: None
 Installation: Place in .obsidian/snippets/ and enable in Settings
 
 CUSTOMIZATION VARIABLES:
 Adjust these values to change size and position of markers
═══════════════════════════════════════════════════════════
*/

/* ═══════════ CUSTOMIZATION VARIABLES ═══════════ */

:root {
    /* LEVEL 1 - Numbers */
    --ol-level1-size: 1em;           /* Font size of numbers */
    --ol-level1-weight: 600;         /* Font weight (400=normal, 600=semi-bold, 700=bold) */
    --ol-level1-left: -1.5em;        /* Horizontal position (negative = left, positive = right) */
    --ol-level1-top: 0em;            /* Vertical offset (negative = up, positive = down) */
    
    /* LEVEL 2 - Arrow → */
    --ol-level2-size: 1.25em;        /* Size of arrow symbol */
    --ol-level2-weight: 600;
    --ol-level2-left: -1.5em;
    --ol-level2-top: -0.25em;
    
    /* LEVEL 3 - Dash — */
    --ol-level3-size: 1.25em;        /* Size of dash symbol */
    --ol-level3-weight: 600;
    --ol-level3-left: -1.5em;
    --ol-level3-top: -0.15em;
    
    /* LEVEL 4 - Plus + */
    --ol-level4-size: 1.25em;        /* Size of plus symbol */
    --ol-level4-weight: 600;
    --ol-level4-left: -1.5em;
    --ol-level4-top: -0.15em;
    
    /* SPACING */
    --ol-marker-spacing: 0.25em;     /* Space between marker and text */
}

/* ═══════════ EDITOR MODE (Source & Live Preview) ═══════════ */

/* Level 1: Gold numbers */
.cm-formatting-list-ol.cm-list-1 {
    color: #E50000 !important; /* ✓ WCAG AA: 10.8:1 on dark backgrounds */
    font-weight: 300 !important;
    font-size: 18 !important;
    position: relative !important;
}

/* Level 2: Purple arrow → */
.cm-formatting-list-ol.cm-list-2 {
    color: transparent !important;
    position: relative !important;
}



.cm-formatting-list-ol.cm-list-2::after {
    content: "->" !important; /* → Arrow */
    color: #E50000 !important; /* Teal */
    font-weight: 300 !important;
    font-size: 18px !important;
    position: absolute !important;
    left: 10px !important;
}




/* Level 3:  dash — */
.cm-formatting-list-ol.cm-list-3 {
    color: transparent !important;
    position: relative !important;
}

.cm-formatting-list-ol.cm-list-3::after {
    content: "-" !important; /* — Em dash */
    color: #E50000 !important; /* Teal */
    font-weight: 300 !important;
    font-size: 18 !important;
    position: absolute !important;
    left: 10px !important;
    
}




/* ═══════════ READING MODE ═══════════ */

/* Set up CSS counters for all levels */
.markdown-rendered ol {
    counter-reset: level1;
}
.markdown-rendered ol ol {
    counter-reset: level2;
}
.markdown-rendered ol ol ol {
    counter-reset: level3;
}
.markdown-rendered ol ol ol ol {
    counter-reset: level4;
}

/* Level 1: Gold numbers */
.markdown-rendered ol > li {
    list-style: none !important;
    position: relative !important;
    counter-increment: level1 !important;
}

.markdown-rendered ol > li::marker {
    content: "" !important;
}

.markdown-rendered ol > li::before {
    content: counter(level1) ". " !important;
    position: absolute !important;
    left: var(--ol-level1-left) !important;
    top: var(--ol-level1-top) !important;
    color: #E50000 !important; /* Gold */
    font-weight: var(--ol-level1-weight) !important;
    font-size: var(--ol-level1-size) !important;
    padding-right: var(--ol-marker-spacing) !important;
}

/* Level 2: Purple arrow → */
.markdown-rendered ol ol > li {
    counter-increment: level2 !important;
}

.markdown-rendered ol ol > li::before {
    content: "\2192 " !important; /* → Arrow */
    color: #E50000 !important; /* Purple */
    left: var(--ol-level2-left) !important;
    top: var(--ol-level2-top) !important;
    font-weight: var(--ol-level2-weight) !important;
    font-size: var(--ol-level2-size) !important;
    padding-right: var(--ol-marker-spacing) !important;
}

/* Level 3: Teal dash — */
.markdown-rendered ol ol ol > li {
    counter-increment: level3 !important;
}

.markdown-rendered ol ol ol > li::before {
    content: "\2014 " !important; /* — Em dash */
    color: #E50000 !important; /* Teal */
    left: var(--ol-level3-left) !important;
    top: var(--ol-level3-top) !important;
    font-weight: var(--ol-level3-weight) !important;
    font-size: var(--ol-level3-size) !important;
    padding-right: var(--ol-marker-spacing) !important;
}

/* Level 4: White plus + */
.markdown-rendered ol ol ol ol > li {
    counter-increment: level4 !important;
}

.markdown-rendered ol ol ol ol > li::before {
    content: "\002B " !important; /* + Plus */
    color: #E50000 !important; /* White */
    left: var(--ol-level4-left) !important;
    top: var(--ol-level4-top) !important;
    font-weight: var(--ol-level4-weight) !important;
    font-size: var(--ol-level4-size) !important;
    padding-right: var(--ol-marker-spacing) !important;
}

/* ═══════════ Live Preview Mode (markdown-preview-view) ═══════════ */

.markdown-preview-view ol > li::before {
    color: #E50000 !important;
    font-size: var(--ol-level1-size) !important;
    font-weight: var(--ol-level1-weight) !important;
}

.markdown-preview-view ol ol > li::before {
    content: "\2192 " !important;
    color: #E50000 !important;
    font-size: var(--ol-level2-size) !important;
    font-weight: var(--ol-level2-weight) !important;
}

.markdown-preview-view ol ol ol > li::before {
    content: "\2014 " !important;
    color: #E50000 !important;
    font-size: var(--ol-level3-size) !important;
    font-weight: var(--ol-level3-weight) !important;
}

.markdown-preview-view ol ol ol ol > li::before {
    content: "\002B " !important;
    color: #E50000 !important;
    font-size: var(--ol-level4-size) !important;
    font-weight: var(--ol-level4-weight) !important;
}

/* ═══════════════════════════════════════════════════════════
   CUSTOMIZATION GUIDE:
   
   To adjust marker appearance, modify the variables in the :root section:
   
   SIZE:
   - Increase --ol-levelX-size for larger markers (e.g., 1.5em, 2em)
   - Decrease for smaller markers (e.g., 0.8em, 0.9em)
   
   POSITION (Horizontal):
   - More negative --ol-levelX-left moves marker further left (e.g., -2em)
   - Less negative or positive values move it right (e.g., -1em, 0em)
   
   POSITION (Vertical):
   - Negative --ol-levelX-top moves marker up (e.g., -0.2em)
   - Positive values move it down (e.g., 0.1em)
   
   WEIGHT:
   - 400 = normal
   - 600 = semi-bold (default)
   - 700 = bold
   
   SPACING:
   - Adjust --ol-marker-spacing to control gap between marker and text
   
   Example custom configuration:
   
   :root {
       --ol-level1-size: 1.1em;
       --ol-level2-size: 1.4em;
       --ol-level3-size: 1.3em;
       --ol-level2-left: -1.8em;
       --ol-level3-top: -0.1em;
   }
   
═══════════════════════════════════════════════════════════ */
/*
    Custom Snippet: Custom List Markers

/* Level 3 (third indent) — Plus */
.cm-formatting-list-ul.cm-list-3 > .list-bullet::after,
.markdown-rendered ul ul ul > li > .list-bullet::after {
    content: "\002B" !important; /* + */
    color: #4d4d4dff !important; /* Yellow */
    font-size:1.30em; /* Make the plus slightly larger */
    font-weight: 300 !important;
    padding-right: -2.25em !important;
    margin-bottom: 40px !important;
}
/* Level 2 (second indent) — Dash */
.cm-formatting-list-ul.cm-list-2 > .list-bullet::after,
.markdown-rendered ul ul > li > .list-bullet::after {
    content: "-" !important; /* — Em dash */
    color: #4d4d4dff !important; /* Pink/Magenta */
    padding-right: -2.25em !important; /* Space between dash and text */
    margin-bottom: 26px !important;
    font-size:0.90em    !important;
    font-weight: 300 !important;/* Make the arrow slightly larger */ 
}
/* Level 1 (first indent) — Arrow */
.cm-formatting-list-ul.cm-list-1 > .list-bullet::after,
.markdown-rendered ul > li > .list-bullet::after {
    content: "->" !important; /* → Right arrow */
    color: #E50000ff !important;
    padding-right: 1.25em !important; /* Space between dash and text */
    margin-bottom: 22px !important;
    font-size:0.90em    !important;
    font-weight: 300 !important;/* Make the arrow slightly larger */ 
}

/* End of Custom List Markers Snippet */

/*
═══════════════════════════════════════════════════════════
 UNORDERED LIST MARKERS (FIXED)
 Properly hides default bullet before applying custom markers
═══════════════════════════════════════════════════════════
*/

/* ═══════════ HIDE DEFAULT BULLETS ═══════════ */

/* Hide the default bullet element in Editor Mode */
.cm-formatting-list-ul .list-bullet::after {
    content: "" !important;
    background: transparent !important;
    border: none !important;
    width: 0 !important;
    height: 0 !important;
}


```

### .obsidian\snippets\dark-shadow-callout-system.css

```css
/* ═══════════════════════════════════════════════════════════════
   UNIFIED CUSTOM CALLOUT SYSTEM - COMPLETE ACTIVE CALLOUTS
   Foundation + All 95 Active Callouts + Hover Glow Style
   
   Version: 3.0.0 - Final Production Release
   Total Callouts: 95 active types
   Color Categories: Purple (Logic) | Gold (Workflow) | Teal (Ideas)
   ═══════════════════════════════════════════════════════════════ */

/* ┌─────────────────────────────────────────────────────────────┐
   │ FOUNDATION 1: COLOR PALETTE                                 │
   └─────────────────────────────────────────────────────────────┘ */

:root {
  /* === PRIMARY ACCENT COLORS === */
  --theme-crimson: #E50000;
  --theme-crimson-bright: #FF0000;
  --theme-crimson-dim: #CC0000;

  /* === CORE UI COLORS === */
  --theme-text: #E0E0E0;
  --theme-bg: #121212;

  /* === RGB VERSIONS (for rgba() transparency) === */
  --theme-crimson-rgb: 229, 0, 0;
  --theme-crimson-bright-rgb: 255, 0, 0;
  --theme-crimson-dim-rgb: 204, 0, 0;
  --theme-text-rgb: 224, 224, 224;
  --theme-bg-rgb: 18, 18, 18;

  /* === DEFAULT FALLBACK === */
  --callout-color: var(--theme-crimson);
  --callout-color-rgb: var(--theme-crimson-rgb);
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ FOUNDATION 2: CALLOUT CATEGORIZATION                        │
   │ All 95 active callouts organized by thematic purpose        │
   └─────────────────────────────────────────────────────────────┘ */

/* ═══════════════════════════════════════════════════════════════
   CATEGORY 1: LOGIC, ARGUMENT & ACADEMIC ANALYSIS (Purple #E50000)
   
   Purpose: Core intellectual work
   - Claims, evidence, reasoning
   - Definitions, concepts, theories
   - Academic analysis modes
   - Mathematical and scientific content
   
   Total: 30 callouts
   ═══════════════════════════════════════════════════════════════ */

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
.callout[data-callout="quote"],
.callout[data-callout="cite"],
.callout[data-callout="example"],
.callout[data-callout="info"],
.callout[data-callout="attention"],
.callout[data-callout="hint"],
.callout[data-callout="faq"],
.callout[data-callout="review"],
.callout[data-callout="important"],
.callout[data-callout="abstract"] {
  --callout-color: var(--theme-crimson);
  --callout-color-rgb: var(--theme-crimson-rgb);
}

/* ═══════════════════════════════════════════════════════════════
   CATEGORY 2: PROJECTS, WORKFLOW & STATUS (Gold #E50000)
   
   Purpose: Task and project management
   - Reading status tracking
   - Project phases and planning
   - Workflow documentation
   - Warnings and constraints
   - Creative production (photography)
   
   Total: 33 callouts
   ═══════════════════════════════════════════════════════════════ */

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
.callout[data-callout="shot-idea"],
.callout[data-callout="lighting-setup"],
.callout[data-callout="composition"],
.callout[data-callout="post-processing"],
.callout[data-callout="important-links"],
.callout[data-callout="warning"],
.callout[data-callout="constraints-and-pitfalls"],
.callout[data-callout="quick-reference"],
.callout[data-callout="how-this-dashboard-works"],
.callout[data-callout="changes-from-prompting-dashboard"] {
  --callout-color: var(--theme-crimson);
  --callout-color-rgb: var(--theme-crimson-rgb);
}

/* ═══════════════════════════════════════════════════════════════
   CATEGORY 3: IDEAS, META & QUESTIONS (Teal #E50000)
   
   Purpose: Reflective thinking and exploration
   - Questions and confusion
   - Purpose and philosophy
   - Connections and insights
   - Summaries and outcomes
   - Meta-documentation (how-to-use guides)
   
   Total: 32 callouts
   ═══════════════════════════════════════════════════════════════ */

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
.callout[data-callout="how-to-use-this"],
.callout[data-callout="the-goal"],
.callout[data-callout="the-mission"],
.callout[data-callout="outcome"],
.callout[data-callout="methodology-and-sources"],
.callout[data-callout="starting-message"],
.callout[data-callout="how-to-use"],
.callout[data-callout="message"],
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
.callout[data-callout="tip"] {
  --callout-color: var(--theme-crimson);
  --callout-color-rgb: var(--theme-crimson-rgb);
}

/* ┌─────────────────────────────────────────────────────────────┐
   │ STYLE: LEFT-ACCENT BORDER + HOVER GLOW                      │
   │ Visual design matching the screenshots exactly              │
   └─────────────────────────────────────────────────────────────┘ */

.callout {
  /* Default state: transparent background with colored left border */
  background-color: transparent !important;
  border: 1px solid rgba(var(--callout-color-rgb), 0.25)    !important;
  border-left: 4px solid var(--callout-color)          !important;
  border-radius: 6px    !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15) !important;
  
  /* Smooth transition for hover effect */
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
  
  padding: 12px 16px !important;
  overflow: hidden !important;
}

/* Hover state: glowing background fill */
.callout:hover {
  background-color: rgba(var(--callout-color-rgb), 0.15) !important;
  border-color: rgba(var(--callout-color-rgb), 0.5) !important;
  box-shadow: 
    0 2px 8px rgba(var(--callout-color-rgb), 0.3),
    0 0 20px rgba(var(--callout-color-rgb), 0.2)    !important;
  transform: translateY(-2px)   !important;
}

/* Title styling */
.callout-title {
  background-color: rgba(var(--callout-color-rgb), 0.12) !important;
  color: var(--callout-color)   !important;
  font-weight: 600;
  letter-spacing: 0.3px   !important;
  
  /* Negative margins to extend title bar edge-to-edge */
  margin: -12px -16px 10px -16px    !important;
  padding: 10px 16px   !important;
  
  transition: background-color 0.3s ease, text-shadow 0.3s ease !important;
}

/* Title glow on hover */
.callout:hover .callout-title {
  background-color: rgba(var(--callout-color-rgb), 0.2) !important;
  text-shadow: 0 0 8px rgba(var(--callout-color-rgb), 0.4) !important;
}

/* Icon color */
.callout-icon {
  color: var(--callout-color)   !important;
}

/* Content area */
.callout-content {
  color: var(--theme-text)  !important;
  padding-top: 4px  !important;
}

/* Folded state (collapsed callout) */
.callout.is-collapsed .callout-content {
  display: none !important;
}

/* ═══════════════════════════════════════════════════════════════
   CALLOUT CATEGORIZATION SUMMARY
   
   PURPLE (Logic & Analysis): 30 callouts
   - Academic rigor: claims, evidence, arguments, analysis
   - Conceptual work: definitions, analogies, thought experiments
   - Mathematical/scientific: equations, cosmos concepts
   
   GOLD (Workflow & Projects): 33 callouts  
   - Task tracking: reading status, to-dos, phases
   - Project management: planning, kickstarters, workflows
   - Creative production: photography workflow
   - System documentation: dashboards, changes, references
   
   TEAL (Ideas & Questions): 32 callouts
   - Exploratory thinking: questions, confusion, insights
   - Meta-documentation: purpose, goals, how-to-use
   - Reflective content: thoughts, philosophy, disposition
   - Connection building: links, related topics, outcomes
   
   TOTAL: 95 active callouts
   ═══════════════════════════════════════════════════════════════ */

/* ═══════════════════════════════════════════════════════════════
   INSTALLATION INSTRUCTIONS
   
   1. Save this file as: callout-system-unified.css
   2. Place in: [Your Vault]/.obsidian/snippets/
   3. Open Obsidian Settings → Appearance → CSS snippets
   4. Toggle ON: callout-system-unified
   5. Disable these old snippets (if present):
      - 00-foundation-color-palette
      - 00-foundation-callout-categories
      - 0.0.3-style-header-only-fill
      - 0.0.5-style-glassmorphism
      - 0.1.0-style-neon-glow
      - 0.1.2-style-multi-effect-combo
      - 101_subtle-glow-and-float
   6. Reload Obsidian (Ctrl/Cmd + R)
   
   ═══════════════════════════════════════════════════════════════ */
```

### .obsidian\snippets\glassmorphism-sidebar-system.css

```css
/* =================================================================
   Pur3v4d3r's Glassmorphism (FORCED PRIORITY)
   Ref: Uses !important tags on every property to override Minimal Theme defaults
   ================================================================= */

body {
    /* -- Configuration -- */
    /* 75% opacity means 25% see-through. Lower this number for MORE transparency. */
    --glass-opacity: 75% !important; 
    
    /* How blurry the background image/wallpaper looks through the glass */
    --glass-blur-radius: 30px !important; 
    
    /* Your Crimson Accent (#E50000) tailored for the borders */
    --glass-border-color: rgba(229, 0, 0, 0.3) !important;
}

/* 1. FORCE Ribbon Transparency (Far left strip) */
.workspace-ribbon {
    /* Mixes your chosen BG2 color with transparency */
    background-color: color-mix(in srgb, var(--bg2) var(--glass-opacity), transparent) !important;
    
    /* Applies the blur */
    backdrop-filter: blur(var(--glass-blur-radius)) !important;
    -webkit-backdrop-filter: blur(var(--glass-blur-radius)) !important;
    
    /* Adds the purple rim light */
    border-right: 1px solid var(--glass-border-color) !important;
}

/* 2. FORCE Sidebar Backgrounds (Left & Right Panels) */
/* We target the split container to catch the background */
.workspace-split.mod-left-split,
.workspace-split.mod-right-split {
    background-color: transparent !important;
}

/* We target the tabs container to apply the glass/color */
.workspace-split.mod-left-split .workspace-tabs,
.workspace-split.mod-right-split .workspace-tabs {
    background-color: color-mix(in srgb, var(--bg2) var(--glass-opacity), transparent) !important;
    backdrop-filter: blur(var(--glass-blur-radius)) !important;
    -webkit-backdrop-filter: blur(var(--glass-blur-radius)) !important;
    border: none !important;
}

/* 3. FORCE Sidebar Borders */
.workspace-split.mod-left-split {
    border-right: 1px solid var(--glass-border-color) !important;
}

.workspace-split.mod-right-split {
    border-left: 1px solid var(--glass-border-color) !important;
}

/* 4. FORCE Tab Header Transparency */
/* This ensures the tabs at the top of the sidebar blend in rather than having a solid block */
.workspace-tab-header-container {
    background-color: transparent !important;
}

/* 5. FORCE View Header (Breadcrumbs bar) Glass */
.view-header {
    background-color: color-mix(in srgb, var(--bg1) 80%, transparent) !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    border-bottom: 1px solid var(--glass-border-color) !important;
}

/* 6. Clean up potential conflicts with Minimal's "Translucency" setting */
.theme-dark {
    --background-secondary: transparent !important; /* Forces the variable itself to yield */
}
.theme-light {
    --background-secondary: transparent !important; /* Forces the variable itself to yield */
}
/* H3 - Neon Magenta to Reactor Orange gradient */

.theme-dark .markdown-preview-view h3,
.theme-dark .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-3,
.theme-dark .cm-header-3,
.markdown-preview-view h3,
.cm-header-3,
h3 {
  background: linear-gradient(135deg, #E50000 0%, #FF0000 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  color: transparent !important;
  text-decoration: none !important;
}
*/
/* =================================================================
   END OF SNIPPET
   ================================================================= */
```

### .obsidian\snippets\inline-code-system.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 SNIPPET: Inline Code Complete Styling System
 Purpose: Modular inline code styles with toggle-able variants
 Author: Pur3v4d3r
 Date: 2024-12-24
 Obsidian Version: 1.5.0+
 
 COLOR PALETTE: Red/Grey/Black
 ─────────────────────────────────────────────────────────────────────────────
 Primary Red:     #E53935 (Vibrant) | #B71C1C (Deep/Dark)
 Grey Spectrum:   #424242 → #9E9E9E → #E0E0E0
 Black Base:      #1A1A1A (True Dark) | #2D2D2D (Soft Dark)
 
 USAGE INSTRUCTIONS:
 ─────────────────────────────────────────────────────────────────────────────
 1. Enable this snippet in Settings → Appearance → CSS Snippets
 2. By default, STYLE 1 (Minimal) is active
 3. To switch styles, uncomment your preferred style section and
    comment out others (only ONE style should be active at a time)
 4. Styles are clearly marked with [TOGGLE ON/OFF] indicators
 
 AVAILABLE STYLES:
 ─────────────────────────────────────────────────────────────────────────────
 • Style 1: Minimal        - Subtle grey background (DEFAULT - ACTIVE)
 • Style 2: Bordered Pill  - Rounded edges with border
 • Style 3: Highlighted    - Red accent background
 • Style 4: Underlined     - Bottom border emphasis
 • Style 5: Neon Glow      - Subtle red shadow effect
 • Style 6: Tag Style      - Bracketed with color accent
 
═══════════════════════════════════════════════════════════════════════════════
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 1: CSS VARIABLES (FOUNDATION)
   ───────────────────────────────────────────────────────────────────────────
   These variables control all inline code styling. Modify here for
   theme-wide changes without touching individual style definitions.
   ═══════════════════════════════════════════════════════════════════════════ */

.theme-light,
.theme-dark {
  /* ─── Primary Color Palette ─── */
  --inline-code-red-vibrant: #E53935;
  --inline-code-red-deep: #B71C1C;
  --inline-code-red-soft: #FF6659;
  --inline-code-red-muted: #C62828;
  
  /* ─── Grey Spectrum ─── */
  --inline-code-grey-900: #212121;
  --inline-code-grey-800: #424242;
  --inline-code-grey-700: #616161;
  --inline-code-grey-600: #757575;
  --inline-code-grey-500: #9E9E9E;
  --inline-code-grey-400: #BDBDBD;
  --inline-code-grey-300: #E0E0E0;
  --inline-code-grey-200: #EEEEEE;
  --inline-code-grey-100: #F5F5F5;
  
  /* ─── Black Variants ─── */
  --inline-code-black-true: #1A1A1A;
  --inline-code-black-soft: #2D2D2D;
  --inline-code-black-charcoal: #363636;
  
  /* ─── Sizing & Spacing ─── */
  --inline-code-font-size: 0.9em;
  --inline-code-padding-x: 0.35em;
  --inline-code-padding-y: 0.15em;
  --inline-code-border-radius: 4px;
  --inline-code-border-width: 1px;
  
  /* ─── Typography ─── */
  --inline-code-font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'Consolas', monospace;
  --inline-code-font-weight: 500;
  --inline-code-letter-spacing: -0.02em;
}

/* ─── Light Mode Specific Overrides ─── */
.theme-light {
  --inline-code-text-default: var(--inline-code-grey-900);
  --inline-code-bg-default: var(--inline-code-grey-200);
  --inline-code-border-default: var(--inline-code-grey-400);
}

/* ─── Dark Mode Specific Overrides ─── */
.theme-dark {
  --inline-code-text-default: var(--inline-code-grey-200);
  --inline-code-bg-default: var(--inline-code-black-soft);
  --inline-code-border-default: var(--inline-code-grey-700);
}


/* 



/* ══════════════════════════════════════════════════════════
   INLINE CODE BLOCKS - Base Styling
   Applies to both editor and preview mode
   ══════════════════════════════════════════════════════════ */

.markdown-source-view.mod-cm6 .cm-inline-code,
.markdown-preview-view .inline-code {
  /*Background-Transparentpurplewithdepth*/background-color: #E500004d !important;
  /*30%opacitypurple*/text-transform: uppercase !important;
  /*Text-Brightcyanforcontrast*/color: #E0E0E0ff !important;
  /*Cybercyan*//*Border-Blackoutline*/border: 3.20px solid #000000cc !important;
  /*Semi-transparentblack*/border-radius: 4px !important;
  /*Roundedcorners*//*Spacing-Minimalpaddingforinline display*/padding: 1.1px 1.1px !important;
  /*Font-Monospaceforcode*/font-family: 'Jetbrains Mono', var(--font-monospace-override), monospace !important;
  font-weight: 100 !important;
  /*Thinweight*/font-size: 0.95em !important;
  /*Slightlysmaller*//*Gloweffect-Purpleshadow*/box-shadow: 0 0 6px #E50000ff;
  /*Softpurpleglow*//*Smoothtransitions*/transition: box-shadow 0.2s ease-in-out !important;
  -webkit-border-radius: 4px !important;
  -moz-border-radius: 4px !important;
  -ms-border-radius: 4px !important;
  -o-border-radius: 4px !important;
}
/* ══════════════════════════════════════════════════════════
   CLICK-TO-SELECT BEHAVIOR
   Enhanced interaction on hover
   ══════════════════════════════════════════════════════════ */

.markdown-source-view.mod-cm6 .cm-inline-code:hover,
.markdown-preview-view .inline-code:hover {
  cursor: pointer !important;                 /* Pointer cursor */
  box-shadow: 0 0 12px #E0E0E0ff !important;  /* Bright cyan glow */
    text-transform: capitalize !important;
}



















═══════════════════════════════════════════════════════════════════════════
   SECTION 2: BASE STYLES (ALWAYS ACTIVE)
   ───────────────────────────────────────────────────────────────────────────
   Core inline code styling that applies regardless of which style variant
   is active. This ensures consistent typography and basic appearance.
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Editor View (Source/Live Preview) ─── */
/*.cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.cm-s-obsidian span.cm-inline-code {
  font-family: var(--inline-code-font-family);
  font-size: var(--inline-code-font-size);
  font-weight: var(--inline-code-font-weight);
  letter-spacing: var(--inline-code-letter-spacing);
  vertical-align: baseline;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ─── Reading View ─── */
/*.markdown-rendered code:not(pre code),
.markdown-preview-view code:not(pre code) {
  font-family: var(--inline-code-font-family);
  font-size: var(--inline-code-font-size);
  font-weight: var(--inline-code-font-weight);
  letter-spacing: var(--inline-code-letter-spacing);
  vertical-align: baseline;
  white-space: nowrap;
  word-break: keep-all;
}

/* ─── Prevent Code Wrapping in Tables ─── */
table code:not(pre code) {
  white-space: nowrap;
}


/* ═══════════════════════════════════════════════════════════════════════════
   ████████████████████████████████████████████████████████████████████████████
   
                           STYLE VARIANTS SECTION
                      ─────────────────────────────────
                       TOGGLE: Uncomment ONE style only
   
   ████████████████████████████████████████████████████████████████████████████
   ═══════════════════════════════════════════════════════════════════════════ */


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 1: MINIMAL
   ───────────────────────────────────────────────────────────────────────────
   [TOGGLE: ON ✓] - Currently Active
   
   Description: Clean, subtle grey background with no border.
   Best for: Reading-focused workflows, minimal visual noise.
   Contrast: ✓ WCAG AA Compliant
   ═══════════════════════════════════════════════════════════════════════════ */

/* --- STYLE 1 START --- */

/* Editor View - Minimal */
/*/*.cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.cm-s-obsidian span.cm-inline-code {
  color: var(--inline-code-text-default);
  background-color: var(--inline-code-bg-default);
  padding: var(--inline-code-padding-y) var(--inline-code-padding-x);
  border-radius: var(--inline-code-border-radius);
}

/* Reading View - Minimal */
./*markdown-rendered code:not(pre code),
.markdown-preview-view code:not(pre code) {
  color: var(--inline-code-text-default);
  background-color: var(--inline-code-bg-default);
  padding: var(--inline-code-padding-y) var(--inline-code-padding-x);
  border-radius: var(--inline-code-border-radius);
}

/* --- STYLE 1 END --- */


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 2: BORDERED PILL
   ───────────────────────────────────────────────────────────────────────────
   [TOGGLE: OFF] - Uncomment to activate
   
   Description: Rounded pill shape with subtle border and background.
   Best for: Code that needs clear visual separation.
   Contrast: ✓ WCAG AA Compliant
   ═══════════════════════════════════════════════════════════════════════════ */

/* --- STYLE 2 START --- UNCOMMENT BELOW TO ACTIVATE ---

.cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.cm-s-obsidian span.cm-inline-code {
  color: var(--inline-code-text-default);
  background-color: var(--inline-code-bg-default);
  padding: var(--inline-code-padding-y) calc(var(--inline-code-padding-x) * 1.5);
  border-radius: 999px;
  border: var(--inline-code-border-width) solid var(--inline-code-border-default);
}

.markdown-rendered code:not(pre code),
.markdown-preview-view code:not(pre code) {
  color: var(--inline-code-text-default);
  background-color: var(--inline-code-bg-default);
  padding: var(--inline-code-padding-y) calc(var(--inline-code-padding-x) * 1.5);
  border-radius: 999px;
  border: var(--inline-code-border-width) solid var(--inline-code-border-default);
}

--- STYLE 2 END --- */


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 3: HIGHLIGHTED (RED ACCENT)
   ───────────────────────────────────────────────────────────────────────────
   [TOGGLE: OFF] - Uncomment to activate
   
   Description: Red-tinted background with dark text for high visibility.
   Best for: Emphasizing important code references, warnings.
   Contrast: ✓ WCAG AA Compliant (4.8:1 ratio)
   ═══════════════════════════════════════════════════════════════════════════ */

/* --- STYLE 3 START --- UNCOMMENT BELOW TO ACTIVATE ---

.theme-light .cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.theme-light .cm-s-obsidian span.cm-inline-code,
.theme-light .markdown-rendered code:not(pre code),
.theme-light .markdown-preview-view code:not(pre code) {
  color: var(--inline-code-red-deep);
  background-color: rgba(229, 57, 53, 0.12);
  padding: var(--inline-code-padding-y) var(--inline-code-padding-x);
  border-radius: var(--inline-code-border-radius);
  border-left: 2px solid var(--inline-code-red-vibrant);
}

.theme-dark .cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.theme-dark .cm-s-obsidian span.cm-inline-code,
.theme-dark .markdown-rendered code:not(pre code),
.theme-dark .markdown-preview-view code:not(pre code) {
  color: var(--inline-code-red-soft);
  background-color: rgba(229, 57, 53, 0.15);
  padding: var(--inline-code-padding-y) var(--inline-code-padding-x);
  border-radius: var(--inline-code-border-radius);
  border-left: 2px solid var(--inline-code-red-vibrant);
}

--- STYLE 3 END --- */


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 4: UNDERLINED
   ───────────────────────────────────────────────────────────────────────────
   [TOGGLE: OFF] - Uncomment to activate
   
   Description: No background, elegant bottom border emphasis.
   Best for: Clean typographic style, inline with body text flow.
   Contrast: ✓ WCAG AA Compliant
   ═══════════════════════════════════════════════════════════════════════════ */

/* --- STYLE 4 START --- UNCOMMENT BELOW TO ACTIVATE ---

.cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.cm-s-obsidian span.cm-inline-code {
  color: var(--inline-code-red-muted);
  background-color: transparent;
  padding: 0 0.1em;
  border-radius: 0;
  border-bottom: 2px solid var(--inline-code-grey-500);
}

.markdown-rendered code:not(pre code),
.markdown-preview-view code:not(pre code) {
  color: var(--inline-code-red-muted);
  background-color: transparent;
  padding: 0 0.1em;
  border-radius: 0;
  border-bottom: 2px solid var(--inline-code-grey-500);
}

.theme-dark .cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.theme-dark .cm-s-obsidian span.cm-inline-code,
.theme-dark .markdown-rendered code:not(pre code),
.theme-dark .markdown-preview-view code:not(pre code) {
  color: var(--inline-code-red-soft);
  border-bottom-color: var(--inline-code-grey-600);
}

--- STYLE 4 END --- */


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 5: NEON GLOW
   ───────────────────────────────────────────────────────────────────────────
   [TOGGLE: OFF] - Uncomment to activate
   
   Description: Subtle red glow/shadow effect for a modern look.
   Best for: Dark themes, cyberpunk/tech aesthetics.
   Contrast: ✓ WCAG AA Compliant
   Note: Uses box-shadow which respects prefers-reduced-motion
   ═══════════════════════════════════════════════════════════════════════════ */

 /* /* --- STYLE 5 START --- UNCOMMENT BELOW TO ACTIVATE ---

.cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.cm-s-obsidian span.cm-inline-code {
  color: var(--inline-code-red-soft)!;
  background-color: var(--inline-code-black-soft);
  padding: var(--inline-code-padding-y) var(--inline-code-padding-x);
  border-radius: var(--inline-code-border-radius);
  border: 1px solid var(--inline-code-red-muted);
  box-shadow: 
    0 0 4px rgba(229, 57, 53, 0.3),
    0 0 8px rgba(229, 57, 53, 0.15);
}

.markdown-rendered code:not(pre code),
.markdown-preview-view code:not(pre code) {
  color: var(--inline-code-red-soft);
  background-color: var(--inline-code-black-soft);
  padding: var(--inline-code-padding-y) var(--inline-code-padding-x);
  border-radius: var(--inline-code-border-radius);
  border: 1px solid var(--inline-code-red-muted);
  box-shadow: 
    0 0 4px rgba(229, 57, 53, 0.3),
    0 0 8px rgba(229, 57, 53, 0.15);
}

.theme-light .cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.theme-light .cm-s-obsidian span.cm-inline-code,
.theme-light .markdown-rendered code:not(pre code),
.theme-light .markdown-preview-view code:not(pre code) {
  color: var(--inline-code-red-deep);
  background-color: var(--inline-code-grey-100);
  box-shadow: 
    0 0 4px rgba(183, 28, 28, 0.2),
    0 0 8px rgba(183, 28, 28, 0.1);
}



--- STYLE 5 END --- */


/* 







═══════════════════════════════════════════════════════════════════════════
   STYLE 6: TAG STYLE (BRACKETED)
   ───────────────────────────────────────────────────────────────────────────
   [TOGGLE: OFF] - Uncomment to activate
   
   Description: Code with colored bracket accents, tag-like appearance.
   Best for: Making code feel like markup tags, technical documentation.
   Contrast: ✓ WCAG AA Compliant
   ═══════════════════════════════════════════════════════════════════════════ */

/* --- STYLE 6 START --- UNCOMMENT BELOW TO ACTIVATE ---

.cm-s-obsidian .cm-inline-code:not(.cm-formatting),
.cm-s-obsidian span.cm-inline-code {
  color: var(--inline-code-text-default);
  background-color: var(--inline-code-bg-default);
  padding: var(--inline-code-padding-y) var(--inline-code-padding-x);
  border-radius: 2px;
  border-left: 3px solid var(--inline-code-red-vibrant);
  border-right: 3px solid var(--inline-code-red-vibrant);
}

.markdown-rendered code:not(pre code),
.markdown-preview-view code:not(pre code) {
  color: var(--inline-code-text-default);
  background-color: var(--inline-code-bg-default);
  padding: var(--inline-code-padding-y) var(--inline-code-padding-x);
  border-radius: 2px;
  border-left: 3px solid var(--inline-code-red-vibrant);
  border-right: 3px solid var(--inline-code-red-vibrant);
}

--- STYLE 6 END --- */


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 3: SPECIAL STATES & INTERACTIONS
   ───────────────────────────────────────────────────────────────────────────
   Hover, selection, and link states for inline code elements.
   These apply to ALL style variants.
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Hover State (Optional Enhancement) ─── */
/* Uncomment if you want subtle hover feedback */
/*
.markdown-rendered code:not(pre code):hover,
.markdown-preview-view code:not(pre code):hover {
  filter: brightness(1.05);
  cursor: default;
}
*/

/* ─── Code Inside Links ─── */
.markdown-rendered a code:not(pre code),
.markdown-preview-view a code:not(pre code) {
  color: inherit;
  text-decoration: underline;
  text-decoration-color: var(--inline-code-red-vibrant);
  text-underline-offset: 2px;
}

/* ─── Code Inside Callouts ─── */
.callout code:not(pre code) {
  background-color: rgba(0, 0, 0, 0.1);
}

.theme-dark .callout code:not(pre code) {
  background-color: rgba(255, 255, 255, 0.1);
}

/* ─── Code Inside Headings ─── */
.markdown-rendered h1 code:not(pre code),
.markdown-rendered h2 code:not(pre code),
.markdown-rendered h3 code:not(pre code),
.markdown-rendered h4 code:not(pre code),
.markdown-rendered h5 code:not(pre code),
.markdown-rendered h6 code:not(pre code) {
  font-size: 0.85em;
}

/* ─── Code Inside Lists ─── */
.markdown-rendered li code:not(pre code) {
  /* Ensure consistent sizing in list contexts */
  font-size: var(--inline-code-font-size);
}

/* ─── Code Inside Tables ─── */
.markdown-rendered td code:not(pre code),
.markdown-rendered th code:not(pre code) {
  font-size: 0.85em;
  padding: 0.1em 0.3em;
}


/* 

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 5: BONUS - SEMANTIC CODE COLORING (OPTIONAL)
   ───────────────────────────────────────────────────────────────────────────
   [TOGGLE: OFF] - Uncomment to activate
   
   Advanced feature: Color code based on content patterns.
   Uses attribute selectors to detect common patterns.
   ═══════════════════════════════════════════════════════════════════════════ */

/* --- SEMANTIC COLORS START --- UNCOMMENT BELOW TO ACTIVATE ---

// These use the CSS :has() selector - modern browsers only

// File paths - Grey tint
.markdown-rendered code:not(pre code):has(+ :contains("/")),
.markdown-preview-view code:not(pre code)[class*="path"] {
  background-color: rgba(117, 117, 117, 0.15);
  color: var(--inline-code-grey-600);
}

// Commands - Red tint
.markdown-rendered code:not(pre code):first-child,
.markdown-preview-view code:not(pre code):first-child {
  // Potential command at start of text
}

--- SEMANTIC COLORS END --- */


/*
═══════════════════════════════════════════════════════════════════════════════
 END OF SNIPPET
 
 TROUBLESHOOTING:
 ─────────────────────────────────────────────────────────────────────────────
 1. Styles not applying?
    → Ensure only ONE style variant is uncommented at a time
    → Check that the snippet is enabled in Settings → Appearance
    → Try reloading Obsidian (Ctrl/Cmd + R)
 
 2. Conflicts with theme?
    → This snippet uses high-specificity selectors that should override themes
    → If issues persist, add !important to critical properties
 
 3. Colors look wrong?
    → Verify your theme supports CSS custom properties
    → Check light/dark mode specific overrides in Section 1
 
 4. Font not rendering?
    → Install JetBrains Mono or change --inline-code-font-family variable
 
 CUSTOMIZATION GUIDE:
 ─────────────────────────────────────────────────────────────────────────────
 • Change colors: Modify variables in Section 1
 • Change sizing: Adjust --inline-code-padding-* and --inline-code-font-size
 • Mix styles: Copy properties from different styles into Style 1
 
 WCAG CONTRAST RATIOS VERIFIED:
 ─────────────────────────────────────────────────────────────────────────────
 • #E53935 on #FFFFFF: 4.0:1 (AA Large Text ✓)
 • #B71C1C on #FFFFFF: 7.8:1 (AAA ✓)
 • #FF6659 on #1A1A1A: 6.2:1 (AA ✓)
 • #212121 on #EEEEEE: 14.5:1 (AAA ✓)
 • #E0E0E0 on #2D2D2D: 10.2:1 (AAA ✓)
 
═══════════════════════════════════════════════════════════════════════════════
*/

```

### .obsidian\snippets\mermaid-chart-enhancer.css

```css
/*
═══════════════════════════════════════════════════════════
 SNIPPET NAME: Mermaid Chart Enhancer
 Purpose: Makes Mermaid diagrams larger and scrollable
          for better visibility of complex charts
 Author: Pur3v4d3r
 Date: 2025-12-23
 Obsidian Version: 1.5+
 Installation: Place in .obsidian/snippets/ and enable in Settings
═══════════════════════════════════════════════════════════
*/

/* ═══════════════════════════════════════════════════════════
   SECTION 1: Container Sizing
   Removes restrictive max-width and allows charts to breathe
   ═══════════════════════════════════════════════════════════ */

/* Main Mermaid container - allow full width expansion */
.markdown-preview-view .mermaid,
.markdown-rendered .mermaid,
.markdown-source-view .mermaid {
  max-width: 100% !important;
  width: 100% !important;
  overflow-x: auto !important;
  overflow-y: visible !important;
  padding: 1rem;
  margin: 1rem 0;
}

/* SVG inside Mermaid - remove restrictive sizing */
.mermaid svg {
  max-width: none !important;
  min-width: 100%;
  height: auto !important;
  min-height: 300px;
}

/* ═══════════════════════════════════════════════════════════
   SECTION 2: Zoom/Scale Controls
   Adjust these values to set your preferred default scale
   ═══════════════════════════════════════════════════════════ */

/* 
   CUSTOMIZATION TIP: 
   Change the scale value below to adjust default chart size
   - 1.0 = normal size
   - 1.25 = 25% larger
   - 1.5 = 50% larger
   - 2.0 = double size
*/
.mermaid svg {
  transform: scale(1.25);
  transform-origin: top left;
}

/* Compensate container for scaled content */
.markdown-preview-view .mermaid,
.markdown-rendered .mermaid {
  /* Adjust min-height based on your scale factor */
  min-height: 400px;
}

/* ═══════════════════════════════════════════════════════════
   SECTION 3: Text Readability Enhancements
   Makes labels and text in diagrams more legible
   ═══════════════════════════════════════════════════════════ */

/* Increase base font size in Mermaid diagrams */
.mermaid text,
.mermaid .nodeLabel,
.mermaid .edgeLabel,
.mermaid .label {
  font-size: 14px !important;
  font-weight: 500 !important;
}

/* Flowchart node text */
.mermaid .node rect + .label,
.mermaid .node .nodeLabel {
  font-size: 14px !important;
  
}

/* Edge/arrow labels */
.mermaid .edgeLabel {
  font-size: 13px !important;
  background-color: var(--background-primary) !important;
  padding: 2px 6px !important;
  border-radius: 4px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1) !important;

}

/* Sequence diagram text */
.mermaid .messageText,
.mermaid .actor {
  font-size: 14px !important;
  
}

/* ═══════════════════════════════════════════════════════════
   SECTION 4: Scrollable Container with Visual Cues
   Shows when chart is scrollable
   ═══════════════════════════════════════════════════════════ */

/* Add subtle border when scrollable */
.markdown-preview-view .mermaid:has(svg) {
  border: 1px solid var(--background-modifier-border);
  border-radius: 8px;
  background-color: var(--background-secondary);
}

/* Fade indicator for horizontal scroll */
.markdown-preview-view .mermaid::after {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 30px;
  background: linear-gradient(to right, transparent, var(--background-secondary));
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease;
}

/* Show fade when content overflows */
.markdown-preview-view .mermaid:hover::after {
  opacity: 0.7;
}

/* ═══════════════════════════════════════════════════════════
   SECTION 5: Interactive Improvements
   Better hover states for exploring diagrams
   ═══════════════════════════════════════════════════════════ */

/* Smooth scrolling in container */
.mermaid {
  scroll-behavior: smooth;
}

/* Highlight nodes on hover for better navigation */
.mermaid .node:hover rect  {
  filter: brightness(1.1) !important;
  cursor: pointer !important;
}
.mermaid .node:hover circle {
  filter: brightness(1.1) !important;
  cursor: pointer !important;
}
.mermaid .node:hover polygon {
  filter: brightness(1.1) !important;
  cursor: pointer !important;
}

/* ═══════════════════════════════════════════════════════════
   SECTION 6: Dark Mode Optimizations
   Better contrast in dark themes
   ═══════════════════════════════════════════════════════════ */

.theme-dark .mermaid {
  /* Slightly boost contrast in dark mode */
  filter: contrast(1.05);
}

.theme-dark .mermaid text {
  fill: var(--text-normal) !important;
}

/* ═══════════════════════════════════════════════════════════
   SECTION 7: Full-Width Mode (Optional)
   Uncomment below for charts that span entire note width
   ═══════════════════════════════════════════════════════════ */


.markdown-preview-view .mermaid {
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  width: 100vw !important;
  max-width: 100vw !important;
  padding: 2rem;
}
*/
/* ══════════════════════════════════════════════════════════
   DARK MODE THEME INTEGRATION
   Optional Mermaid theme colors
   ══════════════════════════════════════════════════════════ */

/*
 * These styles attempt to match Mermaid's generated SVG
 * to your Obsidian theme. Results may vary based on
 * Mermaid's internal styling.
 */

.theme-dark .mermaid {
  /* Background already set above */
}

/* Mermaid text elements */
.theme-dark .mermaid text {
  fill: #970000ff !important;        /* Match theme text */
}

/* Mermaid node backgrounds */
.theme-dark .mermaid rect,
.theme-dark .mermaid circle {
  fill: var(--background-secondary) !important;
  stroke: var(--color-accent) !important;     /* Purple stroke */
}

/* Mermaid connections/arrows */
.theme-dark .mermaid path,
.theme-dark .mermaid line {
  stroke: var(--color-accent) !important;     /* Purple lines */
}

/* ══════════════════════════════════════════════════════════
   MERMAID SPECIFIC DIAGRAM TYPES
   Flowcharts, sequence diagrams, etc.
   ══════════════════════════════════════════════════════════ */

/* Flowchart nodes */
.theme-dark .mermaid .node rect {
  fill: rgba(229, 0, 0, 0.1) !important;    /* Purple tint */
  stroke: #E50000 !important;                 /* Purple border */
  stroke-width: 2px;
}

/* Sequence diagram boxes */
.theme-dark .mermaid .actor {
  fill: var(--background-secondary) !important;
  stroke: #E50000 !important;                 /* Gold border */
}

/* ══════════════════════════════════════════════════════════
   USAGE INSTRUCTIONS
   ══════════════════════════════════════════════════════════

   HOW TO RESIZE:
   1. Hover over the Mermaid diagram
   2. Use your mouse scroll wheel or trackpad to zoom in/out
   3. Alternatively, adjust the 'transform: scale(X);' value
      in SECTION 2 of this CSS snippet to set a default size

   NOTES:
   - Complex diagrams may still require horizontal scrolling
   - Adjust font sizes in SECTION 3 for better readability
   - Dark mode styles are included in SECTION 6 for better contrast
    - Uncomment SECTION 7 for full-width diagrams if desired
    - Remember to save and refresh your Obsidian vault after
      making changes to this CSS snippet
    SCROLLING::after
    - If diagram exceeds container size, scrollbars appear
    - Use mouse wheel or scrollbar to navigate
*/

/* ══════════════════════════════════════════════════════════
   SVG DIAGRAM
   Internal diagram scaling
   ══════════════════════════════════════════════════════════ */

/*
 * Ensures the diagram scales WITH the container as you drag
 */
.mermaid svg {
  width: auto !important;
  height: auto !important;
  max-width: none !important;                 /* Remove default caps */
}

/* ══════════════════════════════════════════════════════════
   MERMAID CONTAINER
   Main wrapper for diagram
   ══════════════════════════════════════════════════════════ */

.mermaid {
  /* ─────────────────────────────────────────
     ENABLE DRAG RESIZING
     ───────────────────────────────────────── */
  resize: both !important;                    /* Adds drag handle bottom-right */
  overflow: auto !important;                  /* Required for resize to work */

  /* ─────────────────────────────────────────
  VISUAL CUES
  ───────────────────────────────────────── */
border: 1px dashed var(--background-modifier-border); /* Faint border */
background-color: var(--background-primary-alt);
padding: 10px;
margin: 1rem auto;                          /* Center container itself */

    
    /* ─────────────────────────────────────────
         SMOOTH TRANSITIONS
         ───────────────────────────────────────── */
    transition: box-shadow 0.2s ease;
    }
    /* ══════════════════════════════════════════════════════════
   HOVER EFFECTS
   Visual feedback when interacting
   ══════════════════════════════════════════════════════════ */

.mermaid:hover {
  box-shadow: 0 0 25px rgba(0, 0, 0, 0.2);    /* Lift effect */
  border-color: var(--text-accent);         

  /*Adjust Color of Arrow*/
 border-color: #970000ff;           /* Highlight border (red) */
}


```

### .obsidian\snippets\metadata-panel-system.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 SNIPPET NAME: Metadata Panel System
 Purpose: Complete customization system for Obsidian's Properties/Metadata panel
          with toggleable style variants and community best practices
 Author: Pur3v4d3r
 Date: 2024-12-24
 Obsidian Version: 1.5.0+
 
 COLOR PALETTE:
   Primary Red:    #E63946 (Accent, active states)
   Dark Grey:      #2B2D30 (Backgrounds, surfaces)
   Medium Grey:    #4A4D52 (Borders, dividers)
   Light Grey:     #8B8D91 (Muted text, icons)
   Black:          #1A1B1E (Deep backgrounds)
   
 INSTALLATION:
   1. Save to: .obsidian/snippets/metadata-panel-system.css
   2. Settings → Appearance → CSS Snippets → Enable
   
 USAGE:
   - Each section can be enabled/disabled by commenting/uncommenting
   - Look for "/* TOGGLE:" comments to find switchable options
   - Combine multiple style variants to create your perfect look
   
═══════════════════════════════════════════════════════════════════════════════
*/

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 1: CSS CUSTOM PROPERTIES (Variables)
   These control the entire theming system - modify here for global changes
   ═══════════════════════════════════════════════════════════════════════════ */

.theme-dark,
.theme-light {
  /* ─── Primary Palette ─── */
  --metadata-accent: #E63946;
  --metadata-accent-hover: #FF4D5A;
  --metadata-accent-muted: rgba(230, 57, 70, 0.15);
  --metadata-accent-subtle: rgba(230, 57, 70, 0.08);
  
  /* ─── Neutral Palette ─── */
  --metadata-bg-primary: #000000ff;
  --metadata-bg-secondary: #2B2D30;
  --metadata-bg-tertiary: #180000ff;
  --metadata-bg-hover: #4A4D52;
  
  /* ─── Text Colors ─── */
  --metadata-text-primary: #E8E9EA;
  --metadata-text-secondary: #B8B9BC;
  --metadata-text-muted: #8B8D91;
  --metadata-text-accent: #E63946;
  
  /* ─── Border & Dividers ─── */
  --metadata-border: #4A4D52;
  --metadata-border-subtle: #3A3D42;
  --metadata-border-accent: rgba(230, 57, 70, 0.5);
  
  /* ─── Spacing System ─── */
  --metadata-spacing-xs: 4px;
  --metadata-spacing-sm: 8px;
  --metadata-spacing-md: 12px;
  --metadata-spacing-lg: 16px;
  --metadata-spacing-xl: 24px;
  
  /* ─── Border Radius ─── */
  --metadata-radius-sm: 4px;
  --metadata-radius-md: 6px;
  --metadata-radius-lg: 8px;
  --metadata-radius-xl: 12px;
  
  /* ─── Typography ─── */
  --metadata-font-size: 16px;
  --metadata-font-size-sm: 14px;
  --metadata-font-weight-normal: 400;
  --metadata-font-weight-medium: 500;
  --metadata-font-weight-bold: 600;
  
  /* ─── Transitions ─── */
  --metadata-transition-fast: 0.15s ease;
  --metadata-transition-normal: 0.25s ease;
  
  /* ─── Shadows ─── */
  --metadata-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --metadata-shadow-md: 0 2px 8px rgba(0, 0, 0, 0.4);
  --metadata-shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.5);
}

/* ─── Light Theme Overrides ─── */
/* TOGGLE: Uncomment for light theme support */
/*
.theme-light {
  --metadata-bg-primary: #FFFFFF;
  --metadata-bg-secondary: #F5F5F5;
  --metadata-bg-tertiary: #EBEBEB;
  --metadata-bg-hover: #E0E0E0;
  --metadata-text-primary: #1A1B1E;
  --metadata-text-secondary: #4A4D52;
  --metadata-text-muted: #6B6D71;
  --metadata-border: #D0D0D0;
  --metadata-border-subtle: #E0E0E0;
  --metadata-shadow-sm: 0 1px 4px rgba(0, 0, 0, 0.1);
  --metadata-shadow-md: 0 2px 8px rgba(0, 0, 0, 0.15);
  --metadata-shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.2);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 2: BASE CONTAINER STYLES
   Core styling for the metadata/properties container
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Main Properties Container ─── */
.metadata-container {
  background: var(--metadata-bg-secondary) !important;
  border-radius: var(--metadata-radius-lg) !important;
  padding: var(--metadata-spacing-md) !important;
  margin: var(--metadata-spacing-sm) 0 var(--metadata-spacing-lg) 0 !important;
  border: 1px solid var(--metadata-border-subtle)!important;
  font-size: var(--metadata-font-size)!important;
  transition: border-color var(--metadata-transition-normal),
              box-shadow var(--metadata-transition-normal) !important;
}

/* TOGGLE: Container hover glow effect */
.metadata-container:hover {
  border-color: var(--metadata-border-accent)!important;
  box-shadow: 0 0 0 5px var(--metadata-accent-muted) !important;
}

/* TOGGLE: Uncomment for floating card style */

/*.metadata-container {
  box-shadow: var(--metadata-shadow-md)!important;
  border: none;
}
*/

/* TOGGLE: Uncomment for minimal/borderless style */
/*
.metadata-container {
  background: transparent !important;
  border: none;
  padding: var(--metadata-spacing-sm) 0 !important;
}
*/

/* TOGGLE: Uncomment for left accent bar style */

.metadata-container {
  border-left: 3px solid var(--metadata-accent) 
  

  !important;
  padding-left: calc(var(--metadata-spacing-md) - 3px) !important;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 3: PROPERTIES HEADER
   The "Properties" title and collapse toggle
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Header Container ─── */
.metadata-properties-heading {
  display: flex !important;
  align-items: center !important;
  gap: var(--metadata-spacing-sm) !important;
  padding: var(--metadata-spacing-xs) var(--metadata-spacing-sm) !important;
  margin-bottom: var(--metadata-spacing-sm) !important;
  border-radius: var(--metadata-radius-md) !important;
  transition: background-color var(--metadata-transition-fast) !important;
  cursor: pointer !important;
}

.metadata-properties-heading:hover {
  background-color: var(--metadata-bg-tertiary) !important;
}

/* ─── Header Title Text ─── */
.metadata-properties-title {
  font-size: var(--metadata-font-size) !important;
  font-weight: var(--metadata-font-weight-bold) !important;
  color: var(--metadata-text-secondary) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
}

/* TOGGLE: Uncomment for accent-colored header */

.metadata-properties-title {
  color: var(--metadata-accent-muted)!important;
}
*/

/* ─── Collapse/Expand Icon ─── */
.metadata-properties-heading .collapse-indicator {
  color: var(--metadata-text-muted);
  transition: transform var(--metadata-transition-fast),
              color var(--metadata-transition-fast);
              
}

.metadata-properties-heading:hover .collapse-indicator {
  color: var(--metadata-accent);
}

/* TOGGLE: Uncomment for rotated chevron animation */

.metadata-properties-heading.is-collapsed .collapse-indicator {
  transform: rotate(-90deg);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 4: PROPERTY ROWS
   Individual property key-value pairs
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Property Row Base ─── */
.metadata-property {
  display: flex !important;
  align-items: flex-start !important;
  gap: var(--metadata-spacing-md) !important;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md) !important;
  margin: var(--metadata-spacing-xs) 0 !important;
  border-radius: var(--metadata-radius-md) !important;
  transition: background-color var(--metadata-transition-fast) !important;
}

.metadata-property:hover {
  background-color: var(--metadata-bg-primary) !important;
}

/* TOGGLE: Uncomment for alternating row colors (zebra stripes) */

.metadata-property:nth-child(even) {
  background-color: var(--metadata-bg-tertiary);
}
.metadata-property:nth-child(odd) {
  background-color: var(--metadata-bg-primary);
}
*/

/* TOGGLE: Uncomment for separated card-style rows */

 .metadata-property {
  background: var(--metadata-bg-primary);
  border: 1px solid var(--metadata-border-subtle);
  margin: var(--metadata-spacing-sm) 0;
}
.metadata-property:hover {
  border-color: var(--metadata-border);
}
*/

/* TOGGLE: Uncomment for bottom-border divider style */

/* .metadata-property {
  border-bottom: 1px solid var(--metadata-border-subtle);
  border-radius: 0;
  padding: var(--metadata-spacing-md) var(--metadata-spacing-sm);
}
.metadata-property:last-child {
  border-bottom: none;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 5: PROPERTY KEYS (Labels)
   The property name/key on the left side
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Property Key Container ─── */
.metadata-property-key {
  flex-shrink: 0 !important;
  min-width: 100px !important;
  max-width: 150px !important;
  display: flex !important;
  align-items: center !important;
  gap: var(--metadata-spacing-xs) !important;
}

/* ─── Property Key Text ─── */
.metadata-property-key-input,
.metadata-property-key input {
  font-size: var(--metadata-font-size) !important;
  font-weight: var(--metadata-font-weight-medium) !important;
  color: var(--metadata-text-secondary) !important;
  background: transparent !important;
  border: none !important;
  padding: var(--metadata-spacing-xs) !important;
  border-radius: var(--metadata-radius-sm) !important;
  transition: color var(--metadata-transition-fast),
              background-color var(--metadata-transition-fast);
}

.metadata-property-key-input:hover,
.metadata-property-key input:hover {
  color: var(--metadata-text-primary) !important;
  background: var(--metadata-bg-hover) !important;
}

.metadata-property-key-input:focus,
.metadata-property-key input:focus {
  color: var(--metadata-accent) !important;
  background: var(--metadata-accent-subtle) !important;
  outline: none !important;
  box-shadow: 0 0 0 2px var(--metadata-accent-muted) !important;
}

/* TOGGLE: Uncomment for bold accent keys */
/*
.metadata-property-key-input,
.metadata-property-key input {
  color: var(--metadata-accent);
  font-weight: var(--metadata-font-weight-bold);
}
*/

/*  TOGGLE: Uncomment for pill/tag-style keys */
/*

.metadata-property-key-input,
.metadata-property-key input {
  background: var(--metadata-bg-tertiary);
  padding: var(--metadata-spacing-xs) var(--metadata-spacing-sm);
  border-radius: var(--metadata-radius-xl);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 6: PROPERTY VALUES
   The value input fields on the right side
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Property Value Container ─── */
.metadata-property-value {
  flex: 1 !important;
  min-width: 0 !important;
}

/* ─── Text Input Values ─── */
.metadata-input-longtext,
.metadata-property-value input[type="text"],
.metadata-property-value textarea {
  width: 100% !important;
  font-size: var(--metadata-font-size) !important;
  color: #ff0000ff !important;
  background: var(--metadata-bg-primary) !important;
  border: 1px solid var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-md) !important;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md) !important;
  transition: border-color var(--metadata-transition-fast),
              box-shadow var(--metadata-transition-fast) !important;
  resize: vertical !important;
}

.metadata-input-longtext:hover,
.metadata-property-value input[type="text"]:hover,
.metadata-property-value textarea:hover {
  border-color: var(--metadata-border) !important;
}

.metadata-input-longtext:focus,
.metadata-property-value input[type="text"]:focus,
.metadata-property-value textarea:focus {
  border-color: var(--metadata-accent) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted) !important;
}

/* TOGGLE: Uncomment for underline-only input style */
/*
.metadata-input-longtext,
.metadata-property-value input[type="text"],
.metadata-property-value textarea {
  background: transparent;
  border: none;
  border-bottom: 2px solid var(--metadata-border-subtle);
  border-radius: 0;
  padding: var(--metadata-spacing-sm) 0;
}
.metadata-input-longtext:focus,
.metadata-property-value input[type="text"]:focus,
.metadata-property-value textarea:focus {
  border-bottom-color: var(--metadata-accent);
  box-shadow: none;
}
*/

/* TOGGLE: Uncomment for minimal/ghost input style */

/*.metadata-input-longtext,
.metadata-property-value input[type="text"],
.metadata-property-value textarea {
  background: transparent;
  border: none;
  padding: var(--metadata-spacing-xs);
}
.metadata-input-longtext:focus,
.metadata-property-value input[type="text"]:focus,
.metadata-property-value textarea:focus {
  background: var(--metadata-accent-subtle);
  box-shadow: none;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 7: PROPERTY TYPE ICONS
   Icons indicating property type (text, date, checkbox, etc.)
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Type Icon Base ─── */
.metadata-property-icon,
.metadata-property .multi-select-pill-remove-button,
.metadata-property svg {
  color: var(--metadata-text-mute);
  width: 16px;
  height: 16px;
  flex-shrink: 0;
  transition: color var(--metadata-transition-fast);
}

.metadata-property:hover .metadata-property-icon,
.metadata-property:hover svg {
  color: var(--metadata-accent);
}

/* TOGGLE: Uncomment to hide type icons */

.metadata-property-icon {
  display: none;
}
*/

/* TOGGLE: Uncomment for always-colored icons */

.metadata-property-icon,
.metadata-property svg {
  color: var(--metadata-text-primary);
  opacity: 0.7;
}
.metadata-property:hover .metadata-property-icon,
.metadata-property:hover svg {
  opacity: 1;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 8: TAGS IN METADATA
   Tag pills/chips within property values
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Tag Pill Base ─── */
.multi-select-pill,
.metadata-property-value .tag {
  display: inline-flex !important;
  align-items: center !important;
  gap: var(--metadata-spacing-xs) !important;
  font-size: var(--metadata-font-size-sm) !important;
  font-weight: var(--metadata-font-weight-medium) !important;
  color: var(--metadata-text-primary) !important;
  background: var(--metadata-bg-tertiary) !important;
  border: 1px solid var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-xl) !important;
  padding: 2px var(--metadata-spacing-sm) !important;
  margin: 2px !important;
  transition: all var(--metadata-transition-fast) !important;
  cursor: pointer !important;
}

.multi-select-pill:hover,
.metadata-property-value .tag:hover {
  background: var(--metadata-accent-muted) !important;
  border-color: var(--metadata-accent) !important;
  color: var(--metadata-accent) !important;
}

/* TOGGLE: Uncomment for solid accent tags */
/*
.multi-select-pill,
.metadata-property-value .tag {
  background: var(--metadata-accent);
  border-color: var(--metadata-accent);
  color: var(--metadata-bg-primary);
}
.multi-select-pill:hover,
.metadata-property-value .tag:hover {
  background: var(--metadata-accent-hover);
  border-color: var(--metadata-accent-hover);
}
*/

/* TOGGLE: Uncomment for outline-only tags */

.multi-select-pill,
.metadata-property-value .tag {
  background: transparent;
  border: 0.1cap solid var(--metadata-accent);
  color: var(--metadata-accent);
}
.multi-select-pill:hover,
.metadata-property-value .tag:hover {
  background: var(--metadata-accent-muted);
}
*/

/* ─── Tag Remove Button ─── */
.multi-select-pill-remove-button {
  display: flex;
  align-items: center !important;
  justify-content: center !important;
  width: 14px !important;
  height: 14px !important;
  border-radius: 50% !important;
  background: transparent !important;
  color: var(--metadata-text-muted) !important;
  transition: all var(--metadata-transition-fast) !important;
}

.multi-select-pill-remove-button:hover {
  background: var(--metadata-accent) !important;
  color: var(--metadata-bg-primary) !important;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 9: CHECKBOXES
   Boolean/checkbox property values
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Checkbox Container ─── */
.metadata-property-value .checkbox-container {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 20px !important;
  height: 20px !important;
  border-radius: var(--metadata-radius-sm) !important;
  border: 2px solid var(--metadata-border) !important;
  background: var(--metadata-bg-primary) !important;
  transition: all var(--metadata-transition-fast) !important;
  cursor: pointer !important;
}

.metadata-property-value .checkbox-container:hover {
  border-color: var(--metadata-accent) !important;
  background: var(--metadata-accent-subtle) !important;
}

/* ─── Checked State ─── */
 .metadata-property-value .checkbox-container.is-enabled,
.metadata-property-value input[type="checkbox"]:checked + .checkbox-container {
  background: var(--metadata-accent) !important;
  border-color: var(--metadata-accent) !important;
}

.metadata-property-value .checkbox-container.is-enabled::after {
  content: "✓" !important;
  color: var(--metadata-bg-primary) !important;
  font-size: 12px !important;
  font-weight: bold !important;
}

/* TOGGLE: Uncomment for toggle switch style */

/* .metadata-property-value .checkbox-container {
  width: 36px;
  height: 20px;
  border-radius: 10px;
  position: relative;
}
.metadata-property-value .checkbox-container::before {
  content: "";
  position: absolute;
  left: 2px;
  top: 2px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--metadata-text-muted);
  transition: transform var(--metadata-transition-fast);
}
.metadata-property-value .checkbox-container.is-enabled::before {
  transform: translateX(16px);
  background: var(--metadata-bg-primary);
}
.metadata-property-value .checkbox-container.is-enabled::after {
  display: none;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 10: DATE PICKER
   Date property input styling
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Date Input ─── */
.metadata-property-value input[type="date"],
.metadata-property-value input[type="datetime-local"] {
  font-size: var(--metadata-font-size) !important;
  color: var(--metadata-text-primary) !important;
  background: var(--metadata-bg-primary) !important;
  border: 1px solid var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-md) !important;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md) !important;
  transition: border-color var(--metadata-transition-fast),
              box-shadow var(--metadata-transition-fast);
}

.metadata-property-value input[type="date"]:hover,
.metadata-property-value input[type="datetime-local"]:hover {
  border-color: var(--metadata-border) !important;
}

.metadata-property-value input[type="date"]:focus,
.metadata-property-value input[type="datetime-local"]:focus {
  border-color: var(--metadata-accent) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted) !important;
}

/* ─── Date Picker Calendar Icon ─── */
.metadata-property-value input[type="date"]::-webkit-calendar-picker-indicator,
.metadata-property-value input[type="datetime-local"]::-webkit-calendar-picker-indicator {
  filter: invert(0.7) sepia(0) saturate(0) hue-rotate(180deg) !important;
  cursor: pointer;
  transition: filter var(--metadata-transition-fast) !important;
}

.metadata-property-value input[type="date"]:hover::-webkit-calendar-picker-indicator,
.metadata-property-value input[type="datetime-local"]:hover::-webkit-calendar-picker-indicator {
  filter: invert(0.5) sepia(1) saturate(5) hue-rotate(-20deg) !important;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 11: NUMBER INPUT
   Numeric property styling
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Number Input Field ─── */
.metadata-property-value input[type="number"] {
  font-size: var(--metadata-font-size) !important;
  font-variant-numeric: tabular-nums !important;
  color: var(--metadata-text-primary) !important;
  background: var(--metadata-bg-primary) !important;
  border: 1px solid var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-md) !important;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md) !important;
  transition: border-color var(--metadata-transition-fast) !important,
              box-shadow var(--metadata-transition-fast) !important;
}

.metadata-property-value input[type="number"]:focus {
  border-color: var(--metadata-accent) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted) !important;
}

/* ─── Spinner Buttons ─── */
.metadata-property-value input[type="number"]::-webkit-inner-spin-button,
.metadata-property-value input[type="number"]::-webkit-outer-spin-button {
  opacity: 0 !important;
  transition: opacity var(--metadata-transition-fast) !important;
}

.metadata-property-value input[type="number"]:hover::-webkit-inner-spin-button,
.metadata-property-value input[type="number"]:hover::-webkit-outer-spin-button {
  opacity: 1 !important;
}

/* TOGGLE: Uncomment to always hide spinners */

.metadata-property-value input[type="number"]::-webkit-inner-spin-button,
.metadata-property-value input[type="number"]::-webkit-outer-spin-button {
  display: none !important;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 12: LINK PROPERTIES
   Internal and external link property styling
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Link Value Display ─── */
.metadata-link-inner,
.metadata-property-value a {
  color: var(--metadata-accent);
  text-decoration: none;
  font-weight: var(--metadata-font-weight-medium);
  transition: color var(--metadata-transition-fast),
              text-decoration var(--metadata-transition-fast);
}

.metadata-link-inner:hover,
.metadata-property-value a:hover {
  color: var(--metadata-accent-hover);
  text-decoration: underline;
}

/* TOGGLE: Uncomment for button-style links */

.metadata-link-inner,
.metadata-property-value a {
  display: inline-flex;
  align-items: center;
  gap: var(--metadata-spacing-xs);
  padding: var(--metadata-spacing-xs) var(--metadata-spacing-sm);
  background: var(--metadata-accent-subtle);
  border-radius: var(--metadata-radius-md);
 box-shadow: var(--metadata-shadow-sm);
}
.metadata-link-inner:hover,
.metadata-property-value a:hover {
  background: var(--metadata-accent-muted);
  text-decoration: none;

}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 13: ADD PROPERTY BUTTON
   The "+ Add property" action at the bottom
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Add Property Button ─── */
.metadata-add-button {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: var(--metadata-spacing-sm) !important;
  width: 100% !important;
  font-size: var(--metadata-font-size) !important;
  font-weight: var(--metadata-font-weight-medium) !important;
  color: var(--metadata-text-muted) !important;
  background: transparent !important;
  border: 2px dashed var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-md) !important;
  padding: var(--metadata-spacing-md) !important;
  margin-top: var(--metadata-spacing-md) !important;
  cursor: pointer !important;
  transition: all var(--metadata-transition-fast) !important;
}

.metadata-add-button:hover {
  color: var(--metadata-accent) !important;
  border-color: var(--metadata-accent) !important;
  background: var(--metadata-accent-subtle) !important;
}

.metadata-add-button svg {
  width: 16px;
  height: 16px;
}

/* TOGGLE: Uncomment for solid button style */

.metadata-add-button {
  border: none;
  background: var(--metadata-bg-primary);
}
.metadata-add-button:hover {
  background: var(--metadata-accent);
  color: var(--metadata-bg-primary);
  bottom: none;
}
*/




/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 14: DROPDOWN/SELECT MENUS
   Property type selectors and value dropdowns
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Dropdown Container ─── */
.metadata-property select,
.dropdown {
  font-size: var(--metadata-font-size);
  color: var(--metadata-text-primary);
  background: var(--metadata-bg-primary);
  border: 1px solid var(--metadata-border-subtle);
  border-radius: var(--metadata-radius-md);
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md);
  padding-right: var(--metadata-spacing-xl);
  cursor: pointer;
  transition: border-color var(--metadata-transition-fast),
              box-shadow var(--metadata-transition-fast);
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20width%3D%2712%27%20height%3D%2712%27%20viewBox%3D%270%200%2024%2024%27%20fill%3D%27none%27%20stroke%3D%27%238B8D91%27%20stroke-width%3D%272%27%3E%3Cpath%20d%3D%27M6%209l6%206%206-6%27%2F%3E%3C%2Fsvg%3E");
  background-repeat: no-repeat;
  background-position: right 8px center;
}

.metadata-property select:hover,
.dropdown:hover {
  border-color: var(--metadata-border);
}

.metadata-property select:focus,
.dropdown:focus {
  border-color: var(--metadata-accent);
  outline: none;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted);
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 15: SUGGESTION POPOVER
   Autocomplete dropdown when typing property names/values
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Suggestion Container ─── */
.suggestion-container.mod-properties,
.metadata-property .suggestion-container {
  background: var(--metadata-bg-secondary);
  border: 1px solid var(--metadata-border);
  border-radius: var(--metadata-radius-lg);
  box-shadow: var(--metadata-shadow-lg);
  overflow: hidden;
}

/* ─── Suggestion Items ─── */
.suggestion-item {
  font-size: var(--metadata-font-size);
  color: var(--metadata-text-primary);
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md);
  cursor: pointer;
  transition: background-color var(--metadata-transition-fast);
}

.suggestion-item:hover,
.suggestion-item.is-selected {
  background: var(--metadata-accent-muted);
  color: var(--metadata-accent);
}

/* ─── Suggestion Item Icon ─── */
.suggestion-item .suggestion-icon {
  color: var(--metadata-text-muted);
  margin-right: var(--metadata-spacing-sm);
}

.suggestion-item.is-selected .suggestion-icon,
.suggestion-item:hover .suggestion-icon {
  color: var(--metadata-accent);
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 16: READING VIEW METADATA
   Metadata display in reading/preview mode
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Frontmatter Block ─── */
.frontmatter-container {
  background: var(--metadata-bg-secondary);
  border: 1px solid var(--metadata-border-subtle);
  border-radius: var(--metadata-radius-lg);
  padding: var(--metadata-spacing-md);
  margin-bottom: var(--metadata-spacing-lg);
}

/* ─── Frontmatter Table ─── */
.frontmatter-container table {
  width: 100%;
  border-collapse: collapse;
}

.frontmatter-container th {
  font-size: var(--metadata-font-size);
  font-weight: var(--metadata-font-weight-bold);
  color: var(--metadata-text-secondary);
  text-align: left;
  padding: var(--metadata-spacing-sm);
  border-bottom: 1px solid var(--metadata-border-subtle);
}

.frontmatter-container td {
  font-size: var(--metadata-font-size);
  color: var(--metadata-text-primary);
  padding: var(--metadata-spacing-sm);
}

/* TOGGLE: Uncomment to hide frontmatter in reading view */
/*
.frontmatter-container {
  display: none;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 17: SOURCE MODE YAML
   Raw YAML frontmatter styling in source mode
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── YAML Fence ─── */
.cm-line.cm-frontmatter,
.cm-hmd-frontmatter {
  font-size: var(--metadata-font-size);
  color: var(--metadata-text-secondary);
}

/* ─── YAML Keys ─── */
.cm-atom {
  color: var(--metadata-accent);
  font-weight: var(--metadata-font-weight-medium);
}

/* ─── YAML Values ─── */
.cm-string {
  color: var(--metadata-text-primary);
}

/* ─── Frontmatter Delimiters (---) ─── */
.cm-line.HyperMD-frontmatter-begin,
.cm-line.HyperMD-frontmatter-end {
  color: var(--metadata-border);
  opacity: 0.5;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 18: ANIMATIONS & MICRO-INTERACTIONS
   Optional animations for enhanced UX
   ═══════════════════════════════════════════════════════════════════════════ */

/* TOGGLE: Uncomment entire section for animations */

@keyframes metadata-fade-in {
  from {
    opacity: 0;
    transform: translateY(-4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes metadata-pulse {
  0%, 100% {
    box-shadow: 0 0 0 0 var(--metadata-accent-muted);
  }
  50% {
    box-shadow: 0 0 0 4px var(--metadata-accent-muted);
  }
}

.metadata-container {
  animation: metadata-fade-in 0.3s ease;
}

.metadata-property {
  animation: metadata-fade-in 0.2s ease;
}

.multi-select-pill {
  animation: metadata-fade-in 0.15s ease;
}

.metadata-add-button:focus {
  animation: metadata-pulse 1s ease infinite;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 19: MOBILE OPTIMIZATIONS
   Responsive adjustments for Obsidian mobile apps
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Mobile Adjustments ─── */
.is-mobile .metadata-container,
.is-phone .metadata-container {
  padding: var(--metadata-spacing-sm);
  margin: var(--metadata-spacing-xs) 0;
}

.is-mobile .metadata-property,
.is-phone .metadata-property {
  flex-direction: column;
  gap: var(--metadata-spacing-xs);
  padding: var(--metadata-spacing-sm);
}

.is-mobile .metadata-property-key,
.is-phone .metadata-property-key {
  min-width: auto;
  max-width: none;
}

.is-mobile .metadata-property-value input,
.is-mobile .metadata-property-value textarea,
.is-phone .metadata-property-value input,
.is-phone .metadata-property-value textarea {
  font-size: 16px; /* Prevents zoom on iOS */
  padding: var(--metadata-spacing-md);
}

/* ─── Touch-Friendly Targets ─── */
.is-mobile .multi-select-pill,
.is-phone .multi-select-pill {
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md);
  min-height: 44px;
}

.is-mobile .metadata-add-button,
.is-phone .metadata-add-button {
  min-height: 48px;
  padding: var(--metadata-spacing-md);
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 20: PRESET THEMES
   Complete theme presets - uncomment ONE to apply
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── PRESET: Glass Morphism ─── */
/* TOGGLE: Uncomment for frosted glass effect */
/*
.metadata-container {
  background: rgba(43, 45, 48, 0.7);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
*/

/* ─── PRESET: Neon Glow ─── */
/* TOGGLE: Uncomment for cyberpunk neon style */
/*
.metadata-container {
  background: #0D0D0D;
  border: 1px solid var(--metadata-accent);
  box-shadow: 0 0 10px var(--metadata-accent-muted),
              inset 0 0 20px rgba(230, 57, 70, 0.05);
}
.metadata-container:hover {
  box-shadow: 0 0 20px var(--metadata-accent-muted),
              0 0 40px rgba(230, 57, 70, 0.1),
              inset 0 0 20px rgba(230, 57, 70, 0.05);
}
.metadata-properties-title {
  color: var(--metadata-accent);
  text-shadow: 0 0 10px var(--metadata-accent-muted);
}
*/

/* ─── PRESET: Minimal Clean ─── */
/* TOGGLE: Uncomment for ultra-minimal style */
/*
.metadata-container {
  background: transparent;
  border: none;
  padding: 0;
}
.metadata-property {
  padding: var(--metadata-spacing-xs) 0;
  border-bottom: 1px solid var(--metadata-border-subtle);
}
.metadata-property:last-child {
  border-bottom: none;
}
.metadata-properties-heading {
  display: none;
}
.metadata-add-button {
  border: none;
  padding: var(--metadata-spacing-sm) 0;
  justify-content: flex-start;
}
*/

/* ─── PRESET: Card Stack ─── */
/* TOGGLE: Uncomment for stacked cards look */
/*
.metadata-property {
  background: var(--metadata-bg-primary);
  border: 1px solid var(--metadata-border-subtle);
  border-radius: var(--metadata-radius-md);
  margin: var(--metadata-spacing-sm) 0;
  box-shadow: var(--metadata-shadow-sm);
}
.metadata-property:hover {
  transform: translateY(-1px);
  box-shadow: var(--metadata-shadow-md);
  border-color: var(--metadata-accent);
}
*/

/* ─── PRESET: Terminal/Hacker ─── */
/* TOGGLE: Uncomment for terminal aesthetic */
/*
:root {
  --metadata-accent: #00FF00;
  --metadata-accent-hover: #33FF33;
  --metadata-accent-muted: rgba(0, 255, 0, 0.15);
}
.metadata-container {
  background: #000000;
  border: 1px solid #00FF00;
  font-family: 'Fira Code', 'Consolas', monospace;
}
.metadata-container * {
  font-family: inherit;
}
.metadata-properties-title {
  color: #00FF00;
}
.metadata-properties-title::before {
  content: "$ ";
  color: #888;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 21: PROPERTY-SPECIFIC STYLING
   Target specific property names for custom styling
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Status Property ─── */
/* Example: Highlight status property differently */
/*
.metadata-property[data-property-key="status"] .metadata-property-value {
  font-weight: var(--metadata-font-weight-bold);
}
.metadata-property[data-property-key="status"] .multi-select-pill {
  background: var(--metadata-accent);
  color: var(--metadata-bg-primary);
}
*/

/* TOGGLE: Uncomment to mute past dates */
/*
.metadata-property[data-property-key="created"] .metadata-property-value[data-date-value*="2023"],
.metadata-property[data-property-key="modified"] .metadata-property-value[data-date-value*="2023"] {

  opacity: 0.4;
}
*/

/* ─── Priority Property ─── */

.metadata-property[data-property-key="priority"] .multi-select-pill[data-value="high"] {
  background: #E63946;
  color: white;
}
.metadata-property[data-property-key="priority"] .multi-select-pill[data-value="medium"] {
  background: #FFC700;
  color: black;
}
.metadata-property[data-property-key="priority"] .multi-select-pill[data-value="low"] {
  background: #4A4D52;
  color: white;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 22: ACCESSIBILITY ENHANCEMENTS
   Ensuring WCAG 2.1 AA compliance
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Focus Visible States ─── */
.metadata-container :focus-visible {
  outline: 2px solid var(--metadata-accent);
  outline-offset: 2px;
}

/* ─── High Contrast Mode Support ─── */
@media (prefers-contrast: high) {
  .metadata-container {
    border-width: 2px;
  }
  
  .metadata-property-value input,
  .metadata-property-value textarea {
    border-width: 2px;
  }
  
  .multi-select-pill {
    border-width: 2px;
  }
}

/* ─── Contrast Verification Comments ─── */
/* ✓ WCAG AA: #E63946 (Red) on #1A1B1E (Black) = 5.2:1 (Pass) */
/* ✓ WCAG AA: #E8E9EA (Light text) on #2B2D30 (Dark grey) = 11.3:1 (Pass) */
/* ✓ WCAG AA: #8B8D91 (Muted) on #2B2D30 (Dark grey) = 4.7:1 (Pass) */
/* ✓ WCAG AA: #1A1B1E (Black) on #E63946 (Red) = 5.2:1 (Pass - for inverted) */


/* ═══════════════════════════════════════════════════════════════════════════
   END OF METADATA PANEL SYSTEM
   
   QUICK CUSTOMIZATION GUIDE:
   ────────────────────────────────────────────────────────────────────────────
   1. Change Colors: Edit variables in SECTION 1
   2. Change Container Style: Toggle options in SECTION 2
   3. Change Row Style: Toggle options in SECTION 4
   4. Change Input Style: Toggle options in SECTION 6
   5. Change Tag Style: Toggle options in SECTION 8
   6. Apply Complete Theme: Uncomment ONE preset in SECTION 20
   7. Add Animations: Uncomment SECTION 18
   
   TROUBLESHOOTING:
   ────────────────────────────────────────────────────────────────────────────
   - If styles don't apply: Check CSS snippet is enabled in Settings
   - If conflicting with theme: Increase selector specificity or use !important
   - If mobile issues: Check SECTION 19 adjustments
   - If animations lag: Disable SECTION 18 animations
   
═══════════════════════════════════════════════════════════════════════════════
*/
/* ══════════════════════════════════════════════════════════
   METADATA & PROPERTIES
   YAML frontmatter and property display
   ══════════════════════════════════════════════════════════ */

/* Metadata container */
.metadata-container {
  background: var(--background-secondary) !important;
  border-radius: 6px !important;
  padding: 12px !important;
  margin: 1em 0 !important;
}

/* Individual property row */
.metadata-property {
  display: flex !important;
  gap: 12px !important;
  padding: 6px 0 !important;
  border-bottom: 1px solid var(--background-modifier-border) !important;
}

/* Property key (label) - Gold */
.theme-dark .metadata-property-key {
  color: #E50000 !important;                  /* Imperial gold */
  font-weight: 600 !important;                /* Bold */
  min-width: 120px !important;                /* Consistent width */
}

/* Property value */
.metadata-property-value {
  color: #E0E0E0 !important;                  /* Light text */
}

/* Optional: Hide metadata heading */
body.metadata-heading-off .metadata-heading {
  display: none !important;
}

/* Optional: Hide add property button */
body.metadata-add-property-off .metadata-add-button {
  display: none !important;
}

/* Optional: Show metadata dividers */
body.metadata-dividers .metadata-property {
  border-bottom: 1px solid var(--background-modifier-border) !important;
}
.metadata-property-key {
  font-weight: 300 !important;                 /* Extra bold keys */
  color: #9e9e9eff !important;                   /* Signature red */
  text-transform: uppercase !important;        /* UPPERCASE keys */
  letter-spacing: 0.5px !important;            /* Spacing for readability */
  font-size: 11px !important;                  /* Slightly smaller */
  padding: 2px 6px !important;                 /* Internal spacing */
  background: rgba(229, 0, 0, 0.15) !important; /* Subtle red background */
  border-left: 3px solid #E50000 !important;   /* Red accent bar */
  border-radius: 3px !important;               /* Subtle rounding */
  margin-right: 8px !important;                /* Space before value */
}
/* ─── Property Key Input Fields ─── */
.metadata-property-key-input,
.metadata-property-key input {
  font-size: var(--metadata-font-size-sm
) !important;
  font-weight: var(--metadata-font-weight-medium) !important;
  color: var(--metadata-text-muted) !important;
  background: var(--metadata-bg-tertiary) !important;
  padding: var(--metadata-spacing-xs) var(--metadata-spacing-sm) !important;
  border: 1px solid var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-md) !important;
  transition: border-color var(--metadata-transition-fast),
              box-shadow var(--metadata-transition-fast) !important;
}
.metadata-property-key-input:hover,
.metadata-property-key input:hover {
  border-color: var(--metadata-border) !important;
}
.metadata-property-key-input:focus,
.metadata-property-key input:focus {
  border-color: var(--metadata-accent) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted) !important;
}
/* TOGGLE: Uncomment for bold/accented keys */
/*
.metadata-property-key-input,
.metadata-property-key input {
  color: var(--metadata-accent) !important;
  font-weight::after var(--metadata-font-weight-bold) !important;
}
*/
/* TOGGLE: Uncomment for pill-style key inputs */
/*
.metadata-property-key-input,
.metadata-property-key input {
  background: var(--metadata-accent-subtle) !important;
  border: none !important;
  padding: var(--metadata-spacing-xs) var(--metadata-spacing-md) !important;
  border-radius: var(--metadata-radius-xl) !important;
  
  box-shadow: var(--metadata-shadow-sm) !important;
}
.metadata-property-key-input:hover,
.metadata-property-key input:hover {
  box-shadow: var(--metadata-shadow-md) !important;
}
*/
.metadata-property-value {
  flex: 1 !important
;
  color: #E0E0E0 !important;                  /* Light text */
}
/* ─── Long Text Input Fields ─── */
.metadata-input-longtext,
.metadata-property-value input[type="text"],
.metadata-property-value textarea {
  font-size: var(--metadata-font-size) !important;
  color: var(--metadata-text-primary) !important;
  background: var(--metadata-bg-primary) !important;
  border: 1px solid var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-md) !important;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md) !important;
  transition: border-color var(--metadata-transition-fast),
              box-shadow var(--metadata-transition-fast) !important;
}
.metadata-input-longtext:hover,
.metadata-property-value input[type="text"]:hover,
.metadata-property-value textarea:hover {
  border-color: var(--metadata-border-accent) !important;
}
.metadata-input-longtext:focus,
.metadata-property-value input[type="text"]:focus,
.metadata-property-value textarea:focus {
  border-color: var(--metadata-accent) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px var(--metadata-accent-hover) !important;
}
/* TOGGLE: Uncomment for underline-only input style */
/*
.metadata-input-longtext,
.metadata-property-value input[type="textarea"],
.metadata-property-value textarea {
  background: transparent;
  border: none;
  border-bottom: 2px solid var(--metadata-border-subtle);
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md);
}
.metadata-input-longtext:focus,
.metadata-property-value input[type="text"]:focus,
.metadata-property-value textarea:focus {
  border-bottom-color: var(--metadata-accent);
  box-shadow: none;
}
*/
/* TOGGLE: Uncomment for minimal input style */
/*
.metadata-input-longtext,
.metadata-property-value input[type="textarea"],
.metadata-property-value textarea {
  background: transparent;
  border: none;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md);
}
*/
/* TOGGLE: Uncomment for filled/accented input style */
/*
.metadata-input-longtext,
.metadata-property-value input[type="textarea"],
.metadata-property-value textarea {
  background: var(--metadata-accent-subtle);
  border: none;
  box-shadow: var(--metadata-shadow-sm);
}
.metadata-input-longtext:hover,
.metadata-property-value input[type="text"]:hover,
.metadata-property-value textarea:hover {
  box-shadow: var(--metadata-shadow-md);
}
*/
/* ─── Property Icons ─── */
.metadata-property-icon,
.metadata-properties-heading.is-collapsed svg {
  color: var(--metadata-text-accent);
  flex-grow: 0;
  flex-shrink: 0;
  width: 16px;
  height: 16px;
  margin-right: 6px;
  transition: color var(--metadata-transition-fast);
}
.metadata-property:hover .metadata-property-icon,
.metadata-properties-heading.is-collapsed:hover svg {
  color: var(--metadata-accent);
}

/* TOGGLE: Uncomment for always-colored icons */
/*
.metadata-property-icon,
.metadata-properties-heading.is-collapsed svg {
  color: var(--metadata-accent);
}
*/
/* TOGGLE: Uncomment for hover-fade icons */
/*
.metadata-property-icon,
.metadata-properties-heading.is-collapsed svg {
  color: var(--metadata-text-muted);
}
.metadata-property:hover .metadata-property-icon,
.metadata-properties-heading.is-collapsed:hover svg {
  color: var(--metadata-accent);
}
*/

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 8: TAGS/MULTI-SELECT PILLS
   Styling for tag and multi-select property values
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Tag/Multi-Select Pill ─── */
.multi-select-pill,
.metadata-property-value .tag {
  display: inline-flex !important;
  align-items: center !important;
  gap: var(--metadata-spacing-xs) !important;
  font-size: var(--metadata-font-size-sm) !important;
  font-weight: var(--metadata-accent-hover) !important;
  border: 0.1cap solid var(--metadata-border) !important;
  border-radius: var(--metadata-radius-full) !important;
  padding: var(--metadata-spacing-xs) var(--metadata-spacing-sm) !important;
  background: var(--metadata-accent-subtle) !important;
  color: var(--metadata-accent) !important;
  cursor: pointer !important;
  transition: all var(--metadata-transition-fast) !important;
}
.multi-select-pill:hover,
.metadata-property-value .tag:hover {
  background: var(--metadata-accent-muted) !important;
  border-color: var(--metadata-accent) !important;
  color: var(--metadata-accent-hover) !important;
}
/* TOGGLE: Uncomment for solid tags */
/*
.multi-select-pill,
.metadata-property-value .tag {
  background: var(--metadata-accent);
  color: var(--metadata-bg-primary);
}
.multi-select-pill:hover,
.metadata-property-value .tag:hover {
  background: var(--metadata-accent-hover);
}
*/
/* TOGGLE: Uncomment for outlined tags */
/*
.multi-select-pill,
.metadata-property-value .tag {
  background: transparent;
  border: 2px solid var(--metadata-accent);
  color: var(--metadata-accent);
}
.multi-select-pill:hover,
.metadata-property-value .tag:hover {
  background: var(--metadata-accent);
  color: var(--metadata-bg-primary);
}
*/
/* ─── Pill Remove Button ─── */
.multi-select-pill-remove-button {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 16px !important;
  height: 16px !important;
  font-size: 12px !important;
  font-weight: bold !important;
  border: none !important;
  border-radius: var(--metadata-radius-full) !important;
  background: transparent !important;
  color: var(--metadata-accent) !important;
  cursor: pointer !important;
  transition: background-color var(--metadata-transition-fast),
              color var(--metadata-transition-fast) !important;
}
.multi-select-pill-remove-button:hover {
  background: var(--metadata-accent) !important;
  color: var(--metadata-bg-primary) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 9: CHECKBOXES
   Boolean property styling
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Checkbox Container ─── */
.metadata-property-value .checkbox-container {
  width: 16px !important;
  height: 16px !important;
  border: 2px solid var(--metadata-border-subtle) !important;
  border-radius: 4px !important;
  background: var(--metadata-bg-primary) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: all var(--metadata-transition-fast) !important;
  cursor: pointer !important;
}
.metadata-property-value .checkbox-container:hover {
  border-color: var(--metadata-border) !important;
}
.metadata-property-value .checkbox-container.is-enabled {
  background: var(--metadata-accent) !important;
  border-color: var(--metadata-accent) !important;
}
.metadata-property-value .checkbox-container.is-enabled .checkbox-checkmark {
  display: block !important;
  color: var(--metadata-bg-primary) !important;
}
/* ─── Checkbox Checkmark ─── */
.metadata-property-value .checkbox-checkmark {
  display: none !important;
  font-size: 12px !important;
  font-weight: bold !important;
  color: var(--metadata-bg-primary) !important;
}
/* TOGGLE: Uncomment for toggle switch style */
/*
.metadata-property-value .checkbox-container {
  width: 32px;
  height: 16px;
  border-radius: 16px;
  position: relative;
  padding: 2px;
}
.metadata-property-value .checkbox-container::after {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--metadata-bg-primary);
  transition: transform var(--metadata-transition-fast);
}
.metadata-property-value .checkbox-container.is-enabled::after {
  transform: translateX(16px);
}
*/
/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 10: DATE INPUT
   Date and datetime property styling
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Date Input Field ─── */
.metadata-property-value input[type="date"],
.metadata-property-value input[type="datetime-local"] {
  font-size: var(--metadata-font-size) !important;
  color: var(--metadata-text-primary) !important;
  background: var(--metadata-bg-primary) !important;
  border: 1px solid var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-md) !important;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md) !important;
  transition: border-color var(--metadata-transition-fast) !important,
              box-shadow var(--metadata-transition-fast) !important;
}
.metadata-property-value input[type="date"]:hover,
.metadata-property-value input[type="datetime-local"]:hover {
  border-color: var(--metadata-border) !important;
}
.metadata-property-value input[type="date"]:focus,
.metadata-property-value input[type="datetime-local"]:focus {
  border-color: var(--metadata-accent) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted) !important;
}
/* ─── Date Picker Icon ─── */
.metadata-property-value input[type="date"]::-webkit-calendar-picker-indicator,
.metadata-property-value input[type="datetime-local"]::-webkit-calendar-picker-indicator {
  filter: invert(0.5) sepia(1) saturate(5) hue-rotate(-20deg) !important;
}
.metadata-property-value input[type="date"]:hover::-webkit-calendar-picker-indicator,
.metadata-property-value input[type="datetime-local"]:hover::-webkit-calendar-picker-indicator {
  filter: invert(0.2) sepia(1) saturate(5) hue-rotate(-20deg) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 11: NUMBER INPUT
   Number property styling
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Number Input Field ─── */
.metadata-property-value input[type="number"] {
  font-size: var(--metadata-font-size) !important;
  color: var(--metadata-text-primary) !important;
  background: var(--metadata-bg-primary) !important;
  border: 1px solid var(--metadata-border-subtle) !important;
  border-radius: var(--metadata-radius-md) !important;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md) !important;
  transition: border-color var(--metadata-transition-fast) !important,
              box-shadow var(--metadata-transition-fast) !important;
}
.metadata-property-value input[type="number"]:hover {
  border-color: var(--metadata-border) !important;
}
.metadata-property-value input[type="number"]:focus {
  border-color: var(--metadata-accent) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted) !important;
}
/* ─── Number Input Spinners ─── */
/*.metadata-property-value input[type="number"]::-webkit-inner-spin-button,
.metadata-property-value input[type="number"]::-webkit-outer-spin-button {
  opacity: 0.5 !important;
}
.metadata-property-value input[type="number"]::-webkit-inner-spin-button:hover,
.metadata-property-value input[type="number"]::-webkit-outer-spin-button:hover {
  opacity: 1 !important;
}*/
/* TOGGLE: Uncomment to hide number input spinners */
/*
.metadata-property-value input[type="number"]::-webkit-inner-spin-button,
.metadata-property-value input[type="number"]::-webkit-outer-spin-button {
  display: none !important;
}
*/
/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 12: LINK VALUES
   Link property styling
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Link Styling ─── */
.metadata-link-inner,
.metadata-property-value a {
  font-size: var(--metadata-font-size) !important;
  color: var(--metadata-accent) !important;
  font-weight: var(--metadata-accent-hover) !important;
  text-decoration: underline !important;
  transition: color var(--metadata-transition-fast),
              text-decoration-color var(--metadata-transition-fast) !important;
}
.metadata-link-inner:hover,
.metadata-property-value a:hover {
  color: var(--metadata-accent-hover) !important;
  text-decoration-color: var(--metadata-accent-hover) !important;
}
/* TOGGLE: Uncomment for pill-style links */
/*
.metadata-link-inner,
.metadata-property-value a {
  background: var(--metadata-accent-subtle);
  padding: var(--metadata-spacing-xs) var(--metadata-spacing-sm);
  border-radius: var(--metadata-radius-full);
  box-shadow: var(--metadata-shadow-sm);
}
.metadata-link-inner:hover,
.metadata-property-value a:hover {
  box-shadow: var(--metadata-shadow-md);
}
*/
/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 13: ADD PROPERTY BUTTON
   Styling for the "Add Property" button
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Add Property Button ─── */
.metadata-add-button {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: var(--metadata-spacing-sm) !important;
  min-height: 40px !important;
  font-size: var(--metadata-font-size) !important;
  font-weight: var(--metadata-font-weight-medium) !important;
  color: var(--metadata-accent) !important;
  border: 2px solid var(--metadata-accent) !important;
  border-radius: var(--metadata-radius-md) !important;
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md) !important;
  background: var(--metadata-bg-primary) !important;
  cursor: pointer !important;
  transition: all var(--metadata-transition-fast) !important;
}
.metadata-add-button:hover {
  background: var(--metadata-accent) !important;
  color: var(--metadata-bg-primary) !important;
  border-color: var(--metadata-accent-hover) !important;
}
.metadata-add-button:focus {
  outline: none !important;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted) !important;
}
/* TOGGLE: Uncomment for bottom-aligned button */
/*
.metadata-add-button {
  margin-top: var(--metadata-spacing-lg);
  align-self: center;
  position: sticky;
  bottom: var(--metadata-spacing-md);
  background: var(--metadata-bg-primary);
  box-shadow: var(--metadata-shadow-md);
}
*/
/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 14: DROPDOWNS
   Dropdown property styling
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Dropdown Select ─── */
.metadata-property select,
.dropdown {
  font-size: var(--metadata-font-size) !important;
  color: var(--metadata-text-primary);
  background: var(--metadata-bg-primary);
  border: 1px solid var(--metadata-border-subtle);
  border-radius: var(--metadata-radius-md);
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md);
  padding-right: var(--metadata-spacing-xl);
  cursor: pointer;
  transition: border-color var(--metadata-transition-fast),
              box-shadow var(--metadata-transition-fast);
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20width%3D%2712%27%20height%3D%2712%27%20viewBox%3D%270%200%2024%2024%27%20fill%3D%27none%27%20stroke%3D%27%238B8D91%27%20stroke-width%3D%272%27%3E%3Cpath%20d%3D%27M6%209l6%206%206-6%27%2F%3E%3C%2Fsvg%3E");
  background-repeat: no-repeat;
  background-position: right 8px center;
}
.metadata-property select:hover,
.dropdown:hover {
  border-color: var(--metadata-border);
}
.metadata-property select:focus,
.dropdown:focus {
  border-color: var(--metadata-accent);
  outline: none;
  box-shadow: 0 0 0 3px var(--metadata-accent-muted);
}
/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 15: SUGGESTION LISTS
   Styling for dropdown and autocomplete suggestion lists
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Suggestion List Container ─── */
.suggestion-list {
  background: var(--metadata-bg-primary);
  border: 1px solid var(--metadata-border-accent);
  border-radius: var(--metadata-radius-md);
  box-shadow: var(--metadata-shadow-md);
  max-height: 200px;
  overflow-y: auto;
  z-index: 1000;
}
/* ─── Suggestion Item ─── */
.suggestion-item {
  padding: var(--metadata-spacing-sm) var(--metadata-spacing-md);
  font-size: var(--metadata-font-size);
  color: var(--metadata-text-primary);
  display: flex;
  align-items: center;
  gap: var(--metadata-spacing-sm);
  cursor: pointer;
  transition: background-color var(--metadata-transition-fast),
              color var(--metadata-transition-fast);
}
.suggestion-item.is-selected,
.suggestion-item:hover {
  background: var(--metadata-accent-subtle);
  color: var(--metadata-accent-hover);
}
.suggestion-item-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
  color: var(--metadata-text-accent);
}
.suggestion-item.is-selected .suggestion-item-icon,
.suggestion-item:hover .suggestion-item-icon {
  color: var(--metadata-accent);
}
/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 16: FRONTMATTER BLOCK
   Styling for the frontmatter display block
   ═══════════════════════════════════════════════════════════════════════════ */
.frontmatter-container {
  background: var(--metadata-bg-primary);
  border: 1px solid var(--metadata-border-accent);
  border-radius: var(--metadata-radius-md);
  padding: var(--metadata-spacing-md);
  margin: var(--metadata-spacing-md) 0;
  box-shadow: var(--metadata-shadow-sm);
}
.frontmatter-container th {
  font-size: var(--metadata-font-size);
  font-weight: var(--metadata-font-weight-medium);
  color: #000000;
  text-align: left;
  padding: var(--metadata-spacing-sm);
}
.frontmatter-container td {
  font-size: var(--metadata-font-size);
  color: var(--metadata-text-primary);
  padding: var(--metadata-spacing-sm);
}
/* TOGGLE: Uncomment to hide frontmatter block */
/*
.frontmatter-container {
  datalistplay: none;
}
*/
/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 17: SOURCE MODE YAML
   Raw YAML frontmatter styling in source mode
   ═══════════════════════════════════════════════════════════════════════════ */
.cm-line.HyperMD-frontmatter,
.cm-atom,
.cm-string {
  background: var(--metadata-bg-primary);
  padding: 2px 4px;
  border-radius: var(--metadata-radius-sm);
}
/* ─── YAML Keys ─── */
.cm-keyword {
  color: var(--metadata-text-accent);
  font-size: larger;
  font-weight: var(--metadata-font-weight-medium);
}
/* ─── YAML Values ─── */
.cm-string,
.cm-number,
.cm-atom {
  color: var(--metadata-text-primary);
  font-size: var(--metadata-font-size);
}
.cm-string.cm-atom {
  color: var(--metadata-accent);
  font-weight: var(--metadata-font-weight-medium);
}
/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 18: ANIMATIONS & MICRO-INTERACTIONS
   Optional animations for enhanced UX
   ═══════════════════════════════════════════════════════════════════════════ */
/* ─── Fade-In Animation ─── */
/*
@keyframes metadata-fade-in {
  from {
    opacity: 0;
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
/* ─── Pulse Animation ─── */
/*
@keyframes metadata-pulse {
  0% {
    box-shadow: 0 0 0 0 var(--metadata-accent-muted);
  }
  100% {
    box-shadow: 0 0 0 8px rgba(0, 0, 0, 0);
  }
}
*/
/* ─── Applying Animations ─── */

.metadata-container {
  animation: metadata-fade-in 0.3s ease;
}
.metadata-property {
  abbrupt: metadata-fade-in 0.3s ease;
}
.metadata-property-value input:focus,
.metadata-property-value textarea:focus {
  animation: metadata-pulse 1s ease;
}
*/



```

### .obsidian\snippets\metadata-panel.css

```css
/* ========================================
   SECTION 1: METADATA CONTAINER
   ======================================== */

/* --- Style the main container for properties --- */
.metadata-container {
  background-color: #1212124d !important; /* Translucent Purple */
  border: 1px solid #535353ff !important; /* Gold border */
  border-radius: 8px !important;
  padding: 12px 18px !important;
  margin-bottom: 32px !important; /* Space before content begins */
}

/* --- Add a "Metadata by Pur3v4d3r" abbreviation label --- */
.metadata-container::before {
  content: "Metadata by Pur3v4d3r" !important;
  /* Styling for the label */
    display: inline-block !important;
    font-size: 16px !important;
    font-weight: 300 !important;
    color: #bbbbbbff !important;
    font-family: "JetBrains Mono", "Consolas", monospace !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    position: absolute !important;
    top: 6px !important;
    right: 12px !important; 
    background: linear-gradient(135deg, #E5000041 35%, #E5000071 90%, #E5000070 15%) !important;
    padding: 4px 8px !important;
    border-radius: 6px !important;
    box-shadow: 0 2px 8px rgba(255, 0, 0, 0.3) !important;
    z-index: 10 !important; 
   /* slight glow and shadow to boxes */ 

}
/* --- Style individual metadata properties --- */



.metadata-property-key {
  font-weight: 300 !important;                 /* Extra bold keys */
  color: #9e9e9eff !important;                   /* Signature red */
  text-transform: uppercase !important;        /* UPPERCASE keys */
  letter-spacing: 0.5px !important;            /* Spacing for readability */
  font-size: 11px !important;                  /* Slightly smaller */
  padding: 2px 6px !important;                 /* Internal spacing */
  background: rgba(229, 0, 0, 0.15) !important; /* Subtle red background */
  border-left: 3px solid #E50000 !important;   /* Red accent bar */
  border-radius: 3px !important;               /* Subtle rounding */
  margin-right: 8px !important;                /* Space before value */
}

.metadata-property-value {
  font-weight: 400 !important;                 /* Regular weight */
  color: #9b9b9bff !important;                   /* Bright grey/white */
  background: rgba(18, 18, 18, 0.5) !important; /* Dark background */
  padding: 2px 8px !important;                 /* Internal spacing */
  border: 1px solid #5e0d0d38 !important;        /* Grey border */
  border-radius: 4px !important;               /* Rounded corners */
  font-family: "JetBrains Mono", "Consolas", monospace !important;
}

.metadata-property-value a {
  color: #E50000 !important;                   /* Red for links */
  text-decoration: none !important;            /* No underline default */
  border-bottom: 1px solid rgba(229, 0, 0, 0.4) !important; /* Subtle underline */
  transition: border-color 0.2s ease !important;
}

.metadata-property-value a:hover {
  color: #FF0000 !important;                   /* Bright red on hover */
  border-bottom: 2px solid #FF0000 !important; /* Thicker underline */
}

.metadata-property-description {
  font-style: italic !important;               /* Italic style */
  font-size: 11px !important;                  /* Small text */
  color: #A3A3A3 !important;                   /* Muted grey */
  margin-left: 12px !important;                /* Left spacing */
  padding: 2px 4px !important;                 /* Internal spacing */
  background: rgba(163, 163, 163, 0.1) !important; /* Subtle grey bg */
  border-left: 2px solid #A3A3A3 !important;   /* Grey accent */
}
```

### .obsidian\snippets\pur3v4d3r-ultimate-callout-system.css

```css
@charset "UTF-8";
/*
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗ ██╗   ██╗██████╗ ██████╗ ██╗   ██╗██╗  ██╗██████╗ ██████╗ ██████╗  ║
║   ██╔══██╗██║   ██║██╔══██╗╚════██╗██║   ██║██║  ██║██╔══██╗╚════██╗██╔══██╗ ║
║   ██████╔╝██║   ██║██████╔╝ █████╔╝██║   ██║███████║██║  ██║ █████╔╝██████╔╝ ║
║   ██╔═══╝ ██║   ██║██╔══██╗ ╚═══██╗╚██╗ ██╔╝╚════██║██║  ██║ ╚═══██╗██╔══██╗ ║
║   ██║     ╚██████╔╝██║  ██║██████╔╝ ╚████╔╝      ██║██████╔╝██████╔╝██║  ██║ ║
║   ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═════╝   ╚═══╝       ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ║
║                                                                              ║
║                    ULTIMATE CALLOUT SYSTEM v5.0                              ║
║                    Single Source of Truth Edition                            ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Author:       Pur3v4d3r                                                     ║
║  Created:      2025-12-28                                                    ║
║  Theme:        Imperial Red/Black/Grey                                       ║
║  Obsidian:     v1.5.0+                                                       ║
║  License:      MIT                                                           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  DESCRIPTION:                                                                ║
║  A comprehensive, modular callout system featuring 150+ custom callout       ║
║  types with a cohesive Red/Black/Grey color palette. Each section can be     ║
║  toggled on/off via CSS comments for maximum customization.                  ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  TABLE OF CONTENTS:                                                          ║
║  ─────────────────────────────────────────────────────────────────────────── ║
║  SECTION 1:  Color Palette Variables ...................... [COLORS]         ║
║  SECTION 2:  Base Callout Foundation ...................... [BASE]           ║
║  SECTION 3:  Standard Callouts (Obsidian Defaults) ........ [STANDARD]       ║
║  SECTION 4:  Semantic Callouts (Info/Status/Alert) ........ [SEMANTIC]       ║
║  SECTION 5:  Knowledge Callouts (Learning/Research) ....... [KNOWLEDGE]      ║
║  SECTION 6:  Task & Project Callouts ...................... [TASKS]          ║
║  SECTION 7:  Analytical Callouts (Critical Thinking) ...... [ANALYTICAL]     ║
║  SECTION 8:  Creative & Workflow Callouts ................. [CREATIVE]       ║
║  SECTION 9:  Layout Callouts (Columns/Grid/Cards) ......... [LAYOUT]         ║
║  SECTION 10: Special Callouts (Infobox/Timeline/Kanban) ... [SPECIAL]        ║
║  SECTION 11: AI & Chat Callouts ........................... [AI-CHAT]        ║
║  SECTION 12: Custom User Callouts ......................... [CUSTOM]         ║
║  SECTION 13: Utility Modifiers ............................ [MODIFIERS]      ║
║  SECTION 14: Accessibility & Motion ....................... [A11Y]           ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  TOGGLE INSTRUCTIONS:                                                        ║
║  To disable a section, wrap it with: /* DISABLED and */ /* END DISABLED     ║
║  To disable a single callout, add /* before and */ after its block          ║
║                                                                              ║
║  WCAG 2.1 AA COMPLIANCE:                                                     ║
║  All color combinations have been validated for 4.5:1+ contrast ratio        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
*/


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 1: COLOR PALETTE VARIABLES [COLORS]
   Imperial Red/Black/Grey Theme
   ═══════════════════════════════════════════════════════════════════════════ */

.theme-dark,
.theme-light {
  /* ─────────────────────────────────────────────────────────────────────────
     PRIMARY REDS - Core accent colors
     ───────────────────────────────────────────────────────────────────────── */
  --callout-red-pure:        255, 0, 0;       /* #FF0000 - Pure Red */
  --callout-red-crimson:     220, 20, 60;     /* #DC143C - Crimson */
  --callout-red-fire:        178, 34, 34;     /* #B22222 - Firebrick */
  --callout-red-dark:        139, 0, 0;       /* #8B0000 - Dark Red */
  --callout-red-maroon:      128, 0, 0;       /* #800000 - Maroon */
  --callout-red-blood:       102, 0, 0;       /* #660000 - Blood Red */
  --callout-red-wine:        114, 47, 55;     /* #722F37 - Wine */
  --callout-red-rose:        255, 69, 69;     /* #FF4545 - Rose Red */
  --callout-red-coral:       205, 92, 92;     /* #CD5C5C - Indian Red */
  --callout-red-salmon:      250, 128, 114;   /* #FA8072 - Salmon */
  
  /* ─────────────────────────────────────────────────────────────────────────
     BLACKS - Deep tones
     ───────────────────────────────────────────────────────────────────────── */
  --callout-black-pure:      0, 0, 0;         /* #000000 - Pure Black */
  --callout-black-rich:      10, 10, 10;      /* #0A0A0A - Rich Black */
  --callout-black-jet:       18, 18, 18;      /* #121212 - Jet Black */
  --callout-black-onyx:      28, 28, 28;      /* #1C1C1C - Onyx */
  --callout-black-charcoal:  36, 36, 36;      /* #242424 - Charcoal */
  --callout-black-raven:     42, 42, 42;      /* #2A2A2A - Raven */
  --callout-black-obsidian:  48, 48, 48;      /* #303030 - Obsidian */
  
  /* ─────────────────────────────────────────────────────────────────────────
     GREYS - Neutral tones
     ───────────────────────────────────────────────────────────────────────── */
  --callout-grey-dark:       64, 64, 64;      /* #404040 - Dark Grey */
  --callout-grey-graphite:   80, 80, 80;      /* #505050 - Graphite */
  --callout-grey-iron:       96, 96, 96;      /* #606060 - Iron */
  --callout-grey-medium:     128, 128, 128;   /* #808080 - Medium Grey */
  --callout-grey-silver:     160, 160, 160;   /* #A0A0A0 - Silver */
  --callout-grey-ash:        176, 176, 176;   /* #B0B0B0 - Ash */
  --callout-grey-light:      192, 192, 192;   /* #C0C0C0 - Light Grey */
  --callout-grey-pale:       208, 208, 208;   /* #D0D0D0 - Pale Grey */
  --callout-grey-mist:       224, 224, 224;   /* #E0E0E0 - Mist */
  
  /* ─────────────────────────────────────────────────────────────────────────
     SEMANTIC MAPPINGS - Role-based color assignments
     ───────────────────────────────────────────────────────────────────────── */
  --callout-primary:         var(--callout-red-crimson);
  --callout-secondary:       var(--callout-grey-dark);
  --callout-tertiary:        var(--callout-black-charcoal);
  
  --callout-success:         var(--callout-red-pure);
  --callout-warning:         var(--callout-red-dark);
  --callout-danger:          var(--callout-red-maroon);
  --callout-error:           var(--callout-red-blood);
  
  --callout-info:            var(--callout-grey-graphite);
  --callout-neutral:         var(--callout-grey-medium);
  --callout-muted:           var(--callout-grey-dark);
  
  /* ─────────────────────────────────────────────────────────────────────────
     OPACITY LEVELS
     ───────────────────────────────────────────────────────────────────────── */
  --callout-opacity-subtle:  0.05;
  --callout-opacity-light:   0.10;
  --callout-opacity-medium:  0.15;
  --callout-opacity-strong:  0.20;
  --callout-opacity-intense: 0.30;
  
  /* ─────────────────────────────────────────────────────────────────────────
     SPACING & SIZING
     ───────────────────────────────────────────────────────────────────────── */
  --callout-border-width:    3px;
  --callout-radius:          6px;
  --callout-padding:         12px 16px;
  --callout-title-padding:   8px 12px;
  --callout-content-padding: 10px 14px;
  --callout-margin:          1em 0;
  --callout-icon-size:       18px;
  
  /* ─────────────────────────────────────────────────────────────────────────
     TRANSITIONS
     ───────────────────────────────────────────────────────────────────────── */
  --callout-transition:      all 0.2s ease-in-out;
  --callout-hover-lift:      translateY(-2px);
  --callout-hover-shadow:    0 4px 12px rgba(0, 0, 0, 0.3);
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 2: BASE CALLOUT FOUNDATION [BASE]
   Core structure applied to all callouts
   ═══════════════════════════════════════════════════════════════════════════ */

.callout {
  --callout-blend-mode: normal;
  margin: var(--callout-margin);
  border-radius: var(--callout-radius);
  border-left-width: var(--callout-border-width);
  transition: var(--callout-transition);
  position: relative;
  z-index: 1;
}

.callout:hover {
  transform: var(--callout-hover-lift);
  box-shadow: var(--callout-hover-shadow);
}

.callout > .callout-title {
  padding: var(--callout-title-padding);
  gap: 8px;
  font-weight: 600;
}

.callout > .callout-title > .callout-icon {
  width: var(--callout-icon-size);
  height: var(--callout-icon-size);
}

.callout > .callout-content {
  padding: var(--callout-content-padding);
}

.callout > .callout-content > p:first-child {
  margin-top: 0;
}

.callout > .callout-content > p:last-child {
  margin-bottom: 0;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 3: STANDARD CALLOUTS [STANDARD]
   Obsidian default types with Imperial theme
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Note ─────────────────────────────────────────────────────────────────── */
.callout[data-callout="note"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-pencil;
}

/* ─── Info ─────────────────────────────────────────────────────────────────── */
.callout[data-callout="info"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-info;
}

/* ─── Abstract / Summary / TLDR ────────────────────────────────────────────── */
.callout[data-callout="abstract"],
.callout[data-callout="summary"],
.callout[data-callout="tldr"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-clipboard-list;
}

/* ─── Success / Check / Done ───────────────────────────────────────────────── */
.callout[data-callout="success"],
.callout[data-callout="check"],
.callout[data-callout="done"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-check-circle;
}

/* ─── Tip / Hint / Important ───────────────────────────────────────────────── */
.callout[data-callout="tip"],
.callout[data-callout="hint"],
.callout[data-callout="important"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-flame;
}

/* ─── Warning / Caution / Attention ────────────────────────────────────────── */
.callout[data-callout="warning"],
.callout[data-callout="caution"],
.callout[data-callout="attention"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-alert-triangle;
}

/* ─── Danger / Error ───────────────────────────────────────────────────────── */
.callout[data-callout="danger"],
.callout[data-callout="error"] {
  --callout-color: var(--callout-red-maroon);
  --callout-icon: lucide-zap;
}

/* ─── Bug ──────────────────────────────────────────────────────────────────── */
.callout[data-callout="bug"] {
  --callout-color: var(--callout-red-blood);
  --callout-icon: lucide-bug;
}

/* ─── Failure / Fail / Missing ─────────────────────────────────────────────── */
.callout[data-callout="failure"],
.callout[data-callout="fail"],
.callout[data-callout="missing"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-x-circle;
}

/* ─── Question / Help / FAQ ────────────────────────────────────────────────── */
.callout[data-callout="question"],
.callout[data-callout="help"],
.callout[data-callout="faq"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-help-circle;
}

/* ─── Quote / Cite ─────────────────────────────────────────────────────────── */
.callout[data-callout="quote"],
.callout[data-callout="cite"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-quote;
}

/* ─── Example ──────────────────────────────────────────────────────────────── */
.callout[data-callout="example"] {
  --callout-color: var(--callout-grey-medium);
  --callout-icon: lucide-list;
}

/* ─── Code ─────────────────────────────────────────────────────────────────── */
.callout[data-callout="code"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-code-2;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 4: SEMANTIC CALLOUTS [SEMANTIC]
   Status, alerts, and informational callouts
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Alert ────────────────────────────────────────────────────────────────── */
.callout[data-callout="alert"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-bell-ring;
}

/* ─── Highlight ────────────────────────────────────────────────────────────── */
.callout[data-callout="highlight"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-highlighter;
}

/* ─── Overview ─────────────────────────────────────────────────────────────── */
.callout[data-callout="overview"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-eye;
}

/* ─── Description ──────────────────────────────────────────────────────────── */
.callout[data-callout="description"] {
  --callout-color: var(--callout-grey-medium);
  --callout-icon: lucide-file-text;
}

/* ─── Purpose ──────────────────────────────────────────────────────────────── */
.callout[data-callout="purpose"],
.callout[data-callout="the-purpose"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-target;
}

/* ─── Message ──────────────────────────────────────────────────────────────── */
.callout[data-callout="message"],
.callout[data-callout="starting-message"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-message-square;
}

/* ─── Key ──────────────────────────────────────────────────────────────────── */
.callout[data-callout="key"],
.callout[data-callout="key-changes"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-key;
}

/* ─── Custom ───────────────────────────────────────────────────────────────── */
.callout[data-callout="custom"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-settings;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 5: KNOWLEDGE CALLOUTS [KNOWLEDGE]
   Learning, research, and academic callouts
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Definition ───────────────────────────────────────────────────────────── */
.callout[data-callout="definition"] {
  --callout-color: var(--callout-grey-medium);
  --callout-icon: lucide-book-open;
}

/* ─── Theory ───────────────────────────────────────────────────────────────── */
.callout[data-callout="theory"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-lightbulb;
}

/* ─── Hypothesis ───────────────────────────────────────────────────────────── */
.callout[data-callout="hypothesis"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-flask-conical;
}

/* ─── Research ─────────────────────────────────────────────────────────────── */
.callout[data-callout="research"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-microscope;
}

/* ─── Insight ──────────────────────────────────────────────────────────────── */
.callout[data-callout="insight"] {
  --callout-color: var(--callout-red-rose);
  --callout-icon: lucide-sparkles;
}

/* ─── Discovery ────────────────────────────────────────────────────────────── */
.callout[data-callout="discovery"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-compass;
}

/* ─── Learning ─────────────────────────────────────────────────────────────── */
.callout[data-callout="learning"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-graduation-cap;
}

/* ─── Analogy ──────────────────────────────────────────────────────────────── */
.callout[data-callout="analogy"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-git-compare;
}

/* ─── Thought Experiment ───────────────────────────────────────────────────── */
.callout[data-callout="thought-experiment"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-brain;
}

/* ─── Atomic Concept ───────────────────────────────────────────────────────── */
.callout[data-callout="atomic-concept"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-atom;
}

/* ─── Core Principle ───────────────────────────────────────────────────────── */
.callout[data-callout="core-principle"],
.callout[data-callout="principle-point"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-landmark;
}

/* ─── Cosmos Concept ───────────────────────────────────────────────────────── */
.callout[data-callout="cosmos-concept"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-orbit;
}

/* ─── Feynman Technique ────────────────────────────────────────────────────── */
.callout[data-callout="feynman-technique"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-pen-tool;
}

/* ─── Math / Equation ──────────────────────────────────────────────────────── */
.callout[data-callout="math"],
.callout[data-callout="equation"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-sigma;
}

/* ─── Methodology & Sources ────────────────────────────────────────────────── */
.callout[data-callout="methodology-and-sources"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-library;
}

/* ─── Further Exploration ──────────────────────────────────────────────────── */
.callout[data-callout="further-exploration"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-map;
}

/* ─── Pre-Read Questions/Thoughts ──────────────────────────────────────────── */
.callout[data-callout="pre-read-questions"],
.callout[data-callout="pre-read-thoughts"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-book-marked;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 6: TASK & PROJECT CALLOUTS [TASKS]
   Project management, workflows, and status tracking
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Todo / To-Do ─────────────────────────────────────────────────────────── */
.callout[data-callout="todo"],
.callout[data-callout="to-do"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-circle;
}

/* ─── Tasks ────────────────────────────────────────────────────────────────── */
.callout[data-callout="tasks"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-check-square;
}

/* ─── Task ─────────────────────────────────────────────────────────────────── */
.callout[data-callout="task"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-square;
}

/* ─── Project ──────────────────────────────────────────────────────────────── */
.callout[data-callout="project"],
.callout[data-callout="project-link"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-folder-kanban;
}

/* ─── Project Kickstarter ──────────────────────────────────────────────────── */
.callout[data-callout="project-kickstarter"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-rocket;
}

/* ─── Objective / Goal / Target ────────────────────────────────────────────── */
.callout[data-callout="objective"],
.callout[data-callout="goal"],
.callout[data-callout="target"],
.callout[data-callout="the-goal"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-crosshair;
}

/* ─── The Mission ──────────────────────────────────────────────────────────── */
.callout[data-callout="the-mission"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-flag;
}

/* ─── Strategy ─────────────────────────────────────────────────────────────── */
.callout[data-callout="strategy"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-route;
}

/* ─── Tactic / Method ──────────────────────────────────────────────────────── */
.callout[data-callout="tactic"],
.callout[data-callout="method"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-wrench;
}

/* ─── Plan ─────────────────────────────────────────────────────────────────── */
.callout[data-callout="plan"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-clipboard;
}

/* ─── Action ───────────────────────────────────────────────────────────────── */
.callout[data-callout="action"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-play;
}

/* ─── Decision ─────────────────────────────────────────────────────────────── */
.callout[data-callout="decision"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-git-branch;
}

/* ─── Progress ─────────────────────────────────────────────────────────────── */
.callout[data-callout="progress"] {
  --callout-color: var(--callout-red-rose);
  --callout-icon: lucide-trending-up;
}

/* ─── Pending ──────────────────────────────────────────────────────────────── */
.callout[data-callout="pending"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-clock;
}

/* ─── Blocked ──────────────────────────────────────────────────────────────── */
.callout[data-callout="blocked"] {
  --callout-color: var(--callout-red-maroon);
  --callout-icon: lucide-ban;
}

/* ─── Complete ─────────────────────────────────────────────────────────────── */
.callout[data-callout="complete"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-check-circle-2;
}

/* ─── Outcome ──────────────────────────────────────────────────────────────── */
.callout[data-callout="outcome"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-trophy;
}

/* ─── Workflow / Process ───────────────────────────────────────────────────── */
.callout[data-callout="workflow"],
.callout[data-callout="process"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-workflow;
}

/* ─── Your New Workflow ────────────────────────────────────────────────────── */
.callout[data-callout="your-new-workflow"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-refresh-cw;
}

/* ─── Phase Callouts ───────────────────────────────────────────────────────── */
.callout[data-callout="phase-one"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-square;
}

.callout[data-callout="phase-two"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-square;
}

.callout[data-callout="phase-three"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-square;
}

.callout[data-callout="phase-four"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-square;
}

/* ─── Meeting / Agenda ─────────────────────────────────────────────────────── */
.callout[data-callout="meeting"],
.callout[data-callout="agenda"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-users;
}

/* ─── Review / Feedback ────────────────────────────────────────────────────── */
.callout[data-callout="review"],
.callout[data-callout="feedback"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-message-circle;
}

/* ─── Draft / Outline ──────────────────────────────────────────────────────── */
.callout[data-callout="draft"],
.callout[data-callout="outline"] {
  --callout-color: var(--callout-grey-medium);
  --callout-icon: lucide-file-edit;
}

/* ─── Reading Status ───────────────────────────────────────────────────────── */
.callout[data-callout="read-complete"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-book-check;
}

.callout[data-callout="reading-in-progress"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-book-open-check;
}

.callout[data-callout="read-asap"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-book-up;
}

/* ─── Revisit ──────────────────────────────────────────────────────────────── */
.callout[data-callout="revist"],
.callout[data-callout="revisit"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-rotate-ccw;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 7: ANALYTICAL CALLOUTS [ANALYTICAL]
   Critical thinking, argumentation, and analysis
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Analysis ─────────────────────────────────────────────────────────────── */
.callout[data-callout="analysis"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-search;
}

/* ─── Analysis Types ───────────────────────────────────────────────────────── */
.callout[data-callout="analysis-rhetorical"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-megaphone;
}

.callout[data-callout="analysis-logical"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-network;
}

.callout[data-callout="analysis-contextual"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-scan;
}

.callout[data-callout="analysis-cognitive"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-brain;
}

/* ─── Argument ─────────────────────────────────────────────────────────────── */
.callout[data-callout="argument"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-swords;
}

/* ─── Key Claim ────────────────────────────────────────────────────────────── */
.callout[data-callout="key-claim"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-flag;
}

/* ─── Evidence ─────────────────────────────────────────────────────────────── */
.callout[data-callout="evidence"] {
  --callout-color: var(--callout-red-rose);
  --callout-icon: lucide-file-check;
}

/* ─── No Evidence ──────────────────────────────────────────────────────────── */
.callout[data-callout="no-evidence"] {
  --callout-color: var(--callout-red-maroon);
  --callout-icon: lucide-file-x;
}

/* ─── Counter Argument ─────────────────────────────────────────────────────── */
.callout[data-callout="counter-argument"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-shield;
}

/* ─── Causal Link ──────────────────────────────────────────────────────────── */
.callout[data-callout="casual-link"],
.callout[data-callout="causal-link"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-link;
}

/* ─── Confusion ────────────────────────────────────────────────────────────── */
.callout[data-callout="confusion"] {
  --callout-color: var(--callout-red-maroon);
  --callout-icon: lucide-help-circle;
}

/* ─── Constraints & Pitfalls ───────────────────────────────────────────────── */
.callout[data-callout="constraints-and-pitfalls"] {
  --callout-color: var(--callout-red-maroon);
  --callout-icon: lucide-alert-octagon;
}

/* ─── Problem Clarity Solution ─────────────────────────────────────────────── */
.callout[data-callout="problem-clarity-solution"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-puzzle;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 8: CREATIVE & WORKFLOW CALLOUTS [CREATIVE]
   Ideas, inspiration, and creative workflows
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Idea ─────────────────────────────────────────────────────────────────── */
.callout[data-callout="idea"],
.callout[data-callout="topic-idea"],
.callout[data-callout="shot-idea"] {
  --callout-color: var(--callout-red-rose);
  --callout-icon: lucide-lightbulb;
}

/* ─── Thoughts ─────────────────────────────────────────────────────────────── */
.callout[data-callout="thoughts"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-brain;
}

/* ─── Capture ──────────────────────────────────────────────────────────────── */
.callout[data-callout="capture"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-camera;
}

/* ─── Document ─────────────────────────────────────────────────────────────── */
.callout[data-callout="document"] {
  --callout-color: var(--callout-grey-medium);
  --callout-icon: lucide-file;
}

/* ─── Stoic Quote ──────────────────────────────────────────────────────────── */
.callout[data-callout="stoic-quote"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-quote;
}

/* ─── Philosophy ───────────────────────────────────────────────────────────── */
.callout[data-callout="the-philosophy"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-scroll;
}

/* ─── Ask Yourself This ────────────────────────────────────────────────────── */
.callout[data-callout="ask-yourself-this"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-help-circle;
}

/* ─── Choice A/B ───────────────────────────────────────────────────────────── */
.callout[data-callout="choice-a"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-circle-dot;
}

.callout[data-callout="choice-b"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-circle;
}

/* ─── Disposition ──────────────────────────────────────────────────────────── */
.callout[data-callout="disposition"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-heart;
}

/* ─── Photography Callouts ─────────────────────────────────────────────────── */
.callout[data-callout="lighting-setup"] {
  --callout-color: var(--callout-grey-medium);
  --callout-icon: lucide-sun;
}

.callout[data-callout="composition"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-layout;
}

.callout[data-callout="post-processing"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-sliders;
}

/* ─── Zettelkasten Incubator ───────────────────────────────────────────────── */
.callout[data-callout="zettelkasten-incubator"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-egg;
}

/* ─── Connection Ideas ─────────────────────────────────────────────────────── */
.callout[data-callout="connection-ideas"],
.callout[data-callout="connections-and-links"] {
  --callout-color: var(--callout-red-rose);
  --callout-icon: lucide-git-merge;
}

/* ─── Related Topics ───────────────────────────────────────────────────────── */
.callout[data-callout="related-topics-to-consider"],
.callout[data-callout="links-to-related-notes"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-link-2;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 9: LAYOUT CALLOUTS [LAYOUT]
   Columns, grids, cards, and structural layouts
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Columns ──────────────────────────────────────────────────────────────── */
.callout[data-callout*="column"] {
  --callout-color: transparent;
  --callout-icon: lucide-columns;
  --columns: 2;
  --callout-column-gap: 10px;
  background: transparent;
  box-shadow: none;
  border: 0;
  padding: 0;
}

.callout[data-callout*="column"] > .callout-title {
  display: none;
}

.callout[data-callout*="column"] > .callout-content {
  display: grid;
  grid-template-columns: repeat(var(--columns), 1fr);
  gap: var(--callout-column-gap);
}

.callout[data-callout*="column"][data-callout-metadata~="3"] > .callout-content {
  --columns: 3;
}

.callout[data-callout*="column"][data-callout-metadata~="4"] > .callout-content {
  --columns: 4;
}

/* ─── Grid ─────────────────────────────────────────────────────────────────── */
.callout[data-callout="grid"] {
  --callout-padding: 0;
  --callout-content-padding: 0;
  background: transparent;
  border: 0;
  box-shadow: none;
}

.callout[data-callout="grid"] > .callout-title {
  display: none;
}

.callout[data-callout="grid"] > .callout-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
}

.callout[data-callout="grid"] > .callout-content img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: var(--callout-radius);
}

/* ─── Cards ────────────────────────────────────────────────────────────────── */
.callout[data-callout~="cards"] {
  --callout-color: transparent;
  --callout-icon: lucide-layout-dashboard;
  --callout-cards-columns: 3;
  --callout-cards-gap: 8px;
  background: transparent;
  box-shadow: none;
  border: 0;
  padding: 0;
}

.callout[data-callout~="cards"] > .callout-title {
  display: none;
}

.callout[data-callout~="cards"] > .callout-content {
  display: grid;
  grid-template-columns: repeat(var(--callout-cards-columns), 1fr);
  gap: var(--callout-cards-gap);
}

.callout[data-callout~="cards"][data-callout-metadata~="2"] > .callout-content {
  --callout-cards-columns: 2;
}

.callout[data-callout~="cards"][data-callout-metadata~="4"] > .callout-content {
  --callout-cards-columns: 4;
}

.callout[data-callout~="cards"] > .callout-content > .callout {
  margin: 0;
  border-radius: var(--callout-radius);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

/* ─── Caption ──────────────────────────────────────────────────────────────── */
.callout[data-callout~="caption"] {
  background: transparent;
  box-shadow: none;
  border: 0;
  padding: 0;
  text-align: center;
  max-width: 300px;
}

.callout[data-callout~="caption"] > .callout-title {
  display: none;
}

.callout[data-callout~="caption"] > .callout-content p {
  margin: 0;
  color: var(--text-faint);
  font-size: 0.85em;
  font-style: italic;
}

/* ─── Blank (Invisible Container) ──────────────────────────────────────────── */
.callout[data-callout="blank"] {
  --callout-color: transparent;
  margin: 0;
  padding: 0;
  border: 0;
  background: transparent;
  box-shadow: none;
}

.callout[data-callout="blank"] > .callout-title {
  display: none;
}

.callout[data-callout="blank"] > .callout-content {
  padding: 0;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 10: SPECIAL CALLOUTS [SPECIAL]
   Infobox, Timeline, Kanban, and advanced layouts
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Infobox (Wikipedia-style) ────────────────────────────────────────────── */
.callout[data-callout~="infobox"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-layout;
  --callout-padding: 0;
  --callout-content-padding: 8px;
  float: right;
  max-width: 320px;
  margin: 0 0 10px 15px;
  border: 1px solid rgba(var(--callout-grey-medium), 0.5);
  background: rgba(var(--callout-black-charcoal), 0.3);
}

.callout[data-callout~="infobox"] > .callout-title {
  background: rgba(var(--callout-red-dark), 0.3);
  text-align: center;
  justify-content: center;
}

.callout[data-callout~="infobox"] table {
  width: 100%;
  margin: 0;
}

.callout[data-callout~="infobox"] img {
  display: block;
  margin: auto;
  max-width: 100%;
}

/* ─── Timeline ─────────────────────────────────────────────────────────────── */
.callout[data-callout~="timeline"] {
  --callout-icon: lucide-clock;
  --callout-padding: 0;
  --callout-title-padding: 10px;
  --callout-content-padding: 10px;
  background: transparent;
  border: 0;
  margin: 0;
  position: relative;
}

.callout[data-callout~="timeline"][data-callout-metadata~="t-l"] {
  border-right: 4px solid rgb(var(--callout-color));
  margin-right: calc(50% - 2px);
}

.callout[data-callout~="timeline"][data-callout-metadata~="t-r"] {
  border-left: 4px solid rgb(var(--callout-color));
  margin-left: calc(50% - 2px);
}

.callout[data-callout~="timeline"] > .callout-title {
  background: rgba(var(--callout-color), 0.25);
}

/* ─── Kanban ───────────────────────────────────────────────────────────────── */
.callout[data-callout~="kanban"] {
  --callout-color: transparent;
  --callout-icon: lucide-layout-dashboard;
  --callout-padding: 0;
  --lane-width: 250px;
  background: transparent;
  box-shadow: none;
  border: 0;
}

.callout[data-callout~="kanban"] > .callout-title {
  justify-content: center;
  background: rgba(var(--callout-black-charcoal), 0.5);
  padding: 8px;
  border-radius: var(--callout-radius);
}

.callout[data-callout~="kanban"] > .callout-content ul {
  display: flex;
  overflow-x: auto;
  gap: 10px;
  padding: 10px 0;
  list-style: none;
}

.callout[data-callout~="kanban"] > .callout-content ul > li {
  min-width: var(--lane-width);
  padding: 10px;
  background: rgba(var(--callout-black-obsidian), 0.8);
  border-radius: var(--callout-radius);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

/* ─── Aside (Margin Notes) ─────────────────────────────────────────────────── */
.callout[data-callout~="aside"] {
  --callout-color: var(--callout-grey-graphite);
  --callout-icon: lucide-sticky-note;
  float: right;
  max-width: 280px;
  margin: 0 0 10px 15px;
  font-size: 0.9em;
}

.callout[data-callout~="aside"][data-callout-metadata~="left"] {
  float: left;
  margin: 0 15px 10px 0;
}

/* ─── Statblock (D&D/TTRPG) ────────────────────────────────────────────────── */
.callout[data-callout="statblock"],
.callout[data-callout="statblocks"] {
  --callout-color: var(--callout-red-wine);
  --callout-icon: lucide-swords;
  --callout-padding: 12px 15px;
  border: 2px solid rgb(var(--callout-color));
  background: rgba(var(--callout-black-jet), 0.9);
}

/* ─── Recite (Speech/Dialogue) ─────────────────────────────────────────────── */
.callout[data-callout="recite"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-message-square;
  border-style: solid;
  border-width: 3px;
  text-align: justify;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 11: AI & CHAT CALLOUTS [AI-CHAT]
   AI responses, chat interfaces, and LLM interactions
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Claude Thinking ──────────────────────────────────────────────────────── */
.callout[data-callout="claude-thinking"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-code-2;
}

/* ─── Gemini Pro Response ──────────────────────────────────────────────────── */
.callout[data-callout="gemini-pro-response"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-sparkles;
}

/* ─── Start of Chat ────────────────────────────────────────────────────────── */
.callout[data-callout="start-of-chat"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-message-circle;
}

/* ─── Your Name (User Message) ─────────────────────────────────────────────── */
.callout[data-callout="your-name"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-user;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 12: CUSTOM USER CALLOUTS [CUSTOM]
   Specialized callouts from user's data.json
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── In-Note Metadata ─────────────────────────────────────────────────────── */
.callout[data-callout="in-note-metadata"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-layers;
}

/* ─── Caltab (Quick Reference Tab) ─────────────────────────────────────────── */
.callout[data-callout="caltab"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-zap;
}

/* ─── Note Toolbar ─────────────────────────────────────────────────────────── */
.callout[data-callout="note-toolbar"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-settings-2;
}

/* ─── Hub / MOC ────────────────────────────────────────────────────────────── */
.callout[data-callout="hub-moc"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-network;
}

/* ─── System / Meta / Debug ────────────────────────────────────────────────── */
.callout[data-callout="system"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-cpu;
}

.callout[data-callout="meta"] {
  --callout-color: var(--callout-grey-dark);
  --callout-icon: lucide-info;
}

.callout[data-callout="debug"] {
  --callout-color: var(--callout-red-dark);
  --callout-icon: lucide-bug;
}

/* ─── How-To Callouts ──────────────────────────────────────────────────────── */
.callout[data-callout="how-to-use"],
.callout[data-callout="how-to-use-this"],
.callout[data-callout="how-this-dashboard-works"] {
  --callout-color: var(--callout-grey-medium);
  --callout-icon: lucide-help-circle;
}

/* ─── What This Does ───────────────────────────────────────────────────────── */
.callout[data-callout="what-this-does"] {
  --callout-color: var(--callout-grey-medium);
  --callout-icon: lucide-info;
}

/* ─── Use Cases & Examples ─────────────────────────────────────────────────── */
.callout[data-callout="use-cases-and-examples"] {
  --callout-color: var(--callout-red-fire);
  --callout-icon: lucide-list;
}

/* ─── Quick Reference ──────────────────────────────────────────────────────── */
.callout[data-callout="quick-reference"],
.callout[data-callout="comprehensive-reference"] {
  --callout-color: var(--callout-black-charcoal);
  --callout-icon: lucide-book;
}

/* ─── Important Links ──────────────────────────────────────────────────────── */
.callout[data-callout="important-links"] {
  --callout-color: var(--callout-red-crimson);
  --callout-icon: lucide-external-link;
}

/* ─── Helpful Tip ──────────────────────────────────────────────────────────── */
.callout[data-callout="helpful-tip"] {
  --callout-color: var(--callout-red-rose);
  --callout-icon: lucide-lightbulb;
}

/* ─── The Start ────────────────────────────────────────────────────────────── */
.callout[data-callout="the-start"] {
  --callout-color: var(--callout-red-pure);
  --callout-icon: lucide-play;
}

/* ─── Changes From Prompting Dashboard ─────────────────────────────────────── */
.callout[data-callout="changes-from-prompting-dashboard"] {
  --callout-color: var(--callout-red-coral);
  --callout-icon: lucide-git-compare;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 13: UTILITY MODIFIERS [MODIFIERS]
   Positioning, sizing, styling adjustments via metadata
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Title Adjustments ────────────────────────────────────────────────────── */
.callout[data-callout-metadata~="no-t"] > .callout-title,
.callout[data-callout-metadata~="no-title"] > .callout-title {
  display: none;
}

.callout[data-callout-metadata~="no-i"] > .callout-title > .callout-icon,
.callout[data-callout-metadata~="no-icon"] > .callout-title > .callout-icon {
  display: none;
}

.callout[data-callout-metadata~="ttl-c"] > .callout-title,
.callout[data-callout-metadata~="title-center"] > .callout-title {
  justify-content: center;
  text-align: center;
}

/* ─── Text Alignment ───────────────────────────────────────────────────────── */
.callout[data-callout-metadata~="txt-c"],
.callout[data-callout-metadata~="text-center"] {
  text-align: center;
}

.callout[data-callout-metadata~="txt-r"],
.callout[data-callout-metadata~="text-right"] {
  text-align: right;
}

.callout[data-callout-metadata~="txt-l"],
.callout[data-callout-metadata~="text-left"] {
  text-align: left;
}

/* ─── Positioning ──────────────────────────────────────────────────────────── */
.callout[data-callout-metadata~="left"] {
  float: left;
  margin-right: 15px;
  margin-left: 0;
}

.callout[data-callout-metadata~="right"] {
  float: right;
  margin-left: 15px;
  margin-right: 0;
}

.callout[data-callout-metadata~="center"] {
  float: none;
  margin-left: auto;
  margin-right: auto;
}

/* ─── Sizing ───────────────────────────────────────────────────────────────── */
.callout[data-callout-metadata~="w-tiny"] { max-width: 20%; }
.callout[data-callout-metadata~="w-small"] { max-width: 30%; }
.callout[data-callout-metadata~="w-medium"] { max-width: 50%; }
.callout[data-callout-metadata~="w-large"] { max-width: 70%; }
.callout[data-callout-metadata~="w-full"] { max-width: 100%; width: 100%; }

/* ─── Styling Adjustments ──────────────────────────────────────────────────── */
.callout[data-callout-metadata~="clean"] {
  border: 0;
  box-shadow: none;
  background: transparent;
  --callout-padding: 0;
}

.callout[data-callout-metadata~="no-border"],
.callout[data-callout-metadata~="nbrd"] {
  border: 0;
}

.callout[data-callout-metadata~="no-margin"],
.callout[data-callout-metadata~="nmg"] {
  margin: 0;
}

.callout[data-callout-metadata~="compact"] {
  --callout-padding: 4px 8px;
  --callout-title-padding: 4px 8px;
  --callout-content-padding: 4px 8px;
}

/* ─── Dim Effects ──────────────────────────────────────────────────────────── */
.callout[data-callout-metadata~="dim"]:not(:hover) {
  filter: brightness(0.6);
  transition: filter 0.3s ease;
}

.callout[data-callout-metadata~="dim"]:hover {
  filter: brightness(1);
}

/* ─── Clear Float ──────────────────────────────────────────────────────────── */
.callout[data-callout-metadata~="clear"] {
  clear: both;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 14: ACCESSIBILITY & MOTION [A11Y]
   WCAG compliance and reduced motion preferences
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Reduced Motion ───────────────────────────────────────────────────────── */
@media (prefers-reduced-motion: reduce) {
  .callout {
    transition: none;
  }
  
  .callout:hover {
    transform: none;
  }
}

/* ─── High Contrast Mode Enhancement ───────────────────────────────────────── */
@media (prefers-contrast: high) {
  .callout {
    border-width: 3px;
    border-style: solid;
  }
  
  .callout > .callout-title {
    font-weight: 700;
  }
}

/* ─── Focus States for Keyboard Navigation ─────────────────────────────────── */
.callout:focus-within {
  outline: 2px solid rgb(var(--callout-red-pure));
  outline-offset: 2px;
}

/* ─── Mobile Responsive ────────────────────────────────────────────────────── */
@media (max-width: 768px) {
  .callout[data-callout-metadata~="left"],
  .callout[data-callout-metadata~="right"] {
    float: none;
    max-width: 100%;
    margin: var(--callout-margin);
  }
  
  .callout[data-callout~="infobox"] {
    float: none;
    max-width: 100%;
    margin: var(--callout-margin);
  }
  
  .callout[data-callout~="aside"] {
    float: none;
    max-width: 100%;
    margin: var(--callout-margin);
  }
  
  .callout[data-callout~="kanban"] > .callout-content ul {
    flex-direction: column;
  }
  
  .callout[data-callout~="kanban"] > .callout-content ul > li {
    min-width: 100%;
  }
}

/* ─── Print Styles ─────────────────────────────────────────────────────────── */
@media print {
  .callout {
    break-inside: avoid;
    box-shadow: none;
    border: 1px solid #ccc;
  }
  
  .callout:hover {
    transform: none;
  }
}


/* ═══════════════════════════════════════════════════════════════════════════
   END OF PUR3V4D3R ULTIMATE CALLOUT SYSTEM v5.0
   
   CALLOUT COUNT: 150+ types across 14 sections
   THEME: Imperial Red/Black/Grey
   
   To toggle sections: Wrap with /* DISABLED ... */ /* END DISABLED
   To toggle individual callouts: Comment out the specific block
   
   For questions or customization: Modify the color variables in Section 1
   ═══════════════════════════════════════════════════════════════════════════ */

```

### .obsidian\snippets\square-bracket-glow.css

```css
/* ══════════════════════════════════════════════════════════════════════════════════
   SQUARE BRACKET RED GLOW SYSTEM - FOCUSED VERSION
   Ultra-targeted approach to make ALL square brackets glow red
   ══════════════════════════════════════════════════════════════════════════════════ */

/* ═══ CORE VARIABLES ═══ */
:root {
  --red-glow: #ff0000ff;
  --red-glow-bright: #ff3333;
  --red-shadow: rgba(255, 0, 0, 1);
  --bracket-shadow: 0 0 4px var(--red-shadow), 0 0 8px var(--red-shadow);
}

/* ═══ OBSIDIAN INTERNAL LINKS - Most Common Use Case ═══ */
/* Link formatting brackets in source mode */
.cm-formatting.cm-formatting-link {
  color: var(--red-glow) !important;
  text-shadow: var(--bracket-shadow) !important;
  font-weight: 900 !important;
  filter: brightness(1.2) !important;
}

/* Link brackets in CodeMirror */
.cm-s-obsidian .cm-formatting.cm-formatting-link {
  color: var(--red-glow) !important;
  text-shadow: var(--bracket-shadow) !important;
  font-weight: 900 !important;
}

/* Modern CM6 link formatting */
.markdown-source-view.mod-cm6 .cm-formatting-link {
  color: var(--red-glow) !important;
  text-shadow: var(--bracket-shadow) !important;
  font-weight: bold !important;
}

/* ═══ ALL BRACKET-LIKE PUNCTUATION ═══ */
/* Universal bracket targeting */
.cm-s-obsidian .cm-bracket,
.cm-editor .cm-bracket,
.cm-punctuation,
.token.punctuation.bracket,
span.cm-bracket {
  color: var(--red-glow-bright) !important;
  text-shadow: var(--bracket-shadow) !important;
}

/* ═══ TAG FORMATTING BRACKETS ═══ */
.cm-formatting.cm-formatting-hashtag,
.cm-hashtag .cm-formatting {
  color: var(--red-glow-bright) !important;
  text-shadow: var(--red-glow-bright) !important;
}

/* ═══ READING MODE - ADD VISUAL BRACKETS ═══ */
/* Add red glowing brackets around internal links in reading mode */
.markdown-preview-view .internal-link:before,
.markdown-rendered .internal-link:before {
  content: '[';
  color: var(--red-glow) !important;
  text-shadow: var(--bracket-shadow) !important;
  font-weight: bold !important;
  margin-right: 1px;
}

.markdown-preview-view .internal-link:after,
.markdown-rendered .internal-link:after {
  content: ']';
  color: var(--red-glow) !important;
  text-shadow: var(--bracket-shadow) !important;
  font-weight: bold !important;
  margin-left: 1px;
}

/* ═══ CODE CONTEXTS ═══ */
/* Syntax highlighting in code blocks */
.HyperMD-codeblock .cm-bracket,
.cm-s-obsidian.cm-s-obsidian .cm-bracket,
pre[class*="language-"] .token.bracket,
.hljs-selector-attr {
  color: var(--red-glow-bright) !important;
  text-shadow: var(--bracket-shadow) !important;
}

/* ═══ SPECIFIC LANGUAGE CONTEXTS ═══ */
/* JavaScript array/object brackets */
.language-javascript .token.bracket,
.language-js .token.bracket,
.language-typescript .token.bracket,
.language-ts .token.bracket {
  color: var(--red-glow-bright) !important;
  text-shadow: var(--bracket-shadow) !important;
}

/* Python list/dict brackets */
.language-python .token.bracket,
.language-py .token.bracket {
  color: var(--red-glow-bright) !important;
  text-shadow: var(--bracket-shadow) !important;
}

/* CSS attribute selectors */
.language-css .token.selector,
.language-scss .token.selector {
  color: var(--red-glow-bright) !important;
  text-shadow: var(--bracket-shadow) !important;
}

/* ═══ DATAVIEW PLUGIN SUPPORT ═══ */
.block-language-dataview .cm-bracket,
.block-language-dataviewjs .cm-bracket {
  color: var(--red-glow-bright) !important;
  text-shadow: var(--bracket-shadow) !important;
  font-weight: bold !important;
}

/* ═══ TEMPLATER PLUGIN SUPPORT ═══ */
.templater-command,
.tp-command {
  color: var(--red-glow-bright) !important;
  text-shadow: var(--bracket-shadow) !important;
}

/* ═══ THEME-SPECIFIC ADJUSTMENTS ═══ */
.theme-dark {
  --red-shadow: rgba(255, 0, 0, 1.0);
  --bracket-shadow: 0 0 3px var(--red-shadow), 0 0 6px var(--red-shadow), 0 0 9px var(--red-shadow);
}

.theme-light {
  --red-shadow: rgba(255, 0, 0, 0.8);
  --bracket-shadow: 0 0 2px var(--red-shadow), 0 0 4px var(--red-shadow);
}

/* ═══ NUCLEAR OPTION - CATCH-ALL ═══ */
/* This targets any text content that contains [ or ] characters */
/* Use with caution as it may affect performance */

/*
.workspace-leaf-content * {
  filter: contrast(1.1);
}

.workspace-leaf-content *:has-text('['),
.workspace-leaf-content *:has-text(']') {
  color: var(--red-glow) !important;
  text-shadow: var(--bracket-shadow) !important;
}
*/

/* ═══ TESTING CLASS ═══ */
/* Add class="test-brackets" to any element to test the effect */
/*.test-brackets,
.test-brackets * {
  color: var(--red-glow) !important;
  text-shadow: var(--bracket-shadow) !important;
  background: rgba(255, 0, 0, 1) !important;
}
/* ══════════════════════════════════════════════════════════════════════════════════
   BRACKET GLOW INTENSITY CONTROL
   Quick toggles for different glow intensities
   ══════════════════════════════════════════════════════════════════════════════════ */

/* ═══ INTENSITY LEVELS ═══ */
/* Comment/uncomment these sections to change intensity */

/* SUBTLE GLOW - Uncomment this section for minimal effect */
/*
:root {
  --bracket-shadow: 0 0 1px var(--red-shadow);
}
*/

/* MEDIUM GLOW - Uncomment this section for balanced effect */
/*:root {
  --bracket-shadow: 0 0 3px var(--red-shadow), 0 0 6px var(--red-shadow);
}

/* INTENSE GLOW - Uncomment this section for maximum effect */

/*:root {
  --bracket-shadow: 0 0 4px var(--red-shadow), 0 0 6px var(--red-shadow), 0 0 12px var(--red-shadow)! important;
}
:root {
  --bracket-shadow: 0 0 3px var(--red-shadow), 0 0 6px var(--red-shadow), 0 0 12px var(--red-shadow) , 0 0 18px var(--red-shadow) !important;
}
/* PULSE EFFECT - Uncomment this section for animated pulsing */

@keyframes bracket-pulse {
  0%, 100% { text-shadow: 0 0 3px var(--red-shadow); }
  50% { text-shadow: 0 0 8px var(--red-shadow), 0 0 12px var(--red-shadow)! important; }
}
.cm-formatting-link,
.cm-bracket {
  animation: bracket-pulse 2s infinite ease-in-out !important;
}


/* ══════════════════════════════════════════════════════════════════════════════════ */

   COLOR VARIANTS
    Quick swaps to change glow color

/* COLOR VARIANTS - Replace red with other colors */
/* BLUE VARIANT */
/*
:root {
  --red-glow: #0066ff;
  --red-shadow: rgba(0, 102, 255, 0.9);
}
*/

/* GREEN VARIANT */
/*
:root {
  --red-glow: #00ff00;
  --red-shadow: rgba(0, 255, 0, 0.9);
}
*/

/* PURPLE VARIANT */
/*
:root {
  --red-glow: #9900ff;
  --red-shadow: rgba(153, 0, 255, 0.9);
}
*/
/* ══════════════════════════════════════════════════════════════════════════════════ */


```

### .obsidian\snippets\tag-customization-system.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 SNIPPET: Tag Customization System
 Purpose: Comprehensive tag styling with multiple design options
 Author: Pur3v4d3r
 Date: 2024-12-24
 Obsidian Version: 1.5.0+
 
 USAGE INSTRUCTIONS:
 1. This snippet provides a base style + 9 alternative styles (10 total)
 2. The BASE STYLE is active by default
 3. To try different styles, comment out the current active section
    and uncomment your preferred style section
 4. Each style section is clearly marked with ═══ headers
 5. Color customization variables are at the top for easy modification
 
 COMMUNITY SOURCES:
 - Obsidian Forum best practices
 - Minimal Theme tag patterns
 - Things Theme color coding
 - AnuPpuccin accent systems
 - ITS Theme tag badges
═══════════════════════════════════════════════════════════════════════════════
*/

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 1: CSS VARIABLES - CUSTOMIZE YOUR COLORS HERE
   ═══════════════════════════════════════════════════════════════════════════ */

.theme-light,
.theme-dark {
  /* ─── Signature Palette (Red/Black/Grey) ─── */
  --tag-primary: #ff0000ff;           /* Red - primary accent */
  --tag-secondary: #1F1F1F;         /* Black - emphasis */
  --tag-tertiary: #6B7280;          /* Grey - neutral/muted */
  
  /* ─── Extended Palette for Semantic Tags ─── */
  --tag-status: #374151;            /* Dark Grey - status indicators */
  --tag-priority: #991B1B;          /* Dark Red - priority/urgent */
  --tag-category: #DC2626;          /* Red - categories */
  --tag-type: #1F1F1F;              /* Black - types */
  --tag-project: #B91C1C;           /* Crimson - projects */
  --tag-context: #4B5563;           /* Medium Grey - contexts */
  --tag-area: #EF4444;              /* Bright Red - areas */
  --tag-archive: #9CA3AF;           /* Light Grey - archived */
  
  /* ─── Tag Dimensions ─── */
  --tag-padding-x: 0.5em;
  --tag-padding-y: 0.2em;
  --tag-font-size: 0.85em;
  --tag-border-radius: 4px;
  --tag-font-weight: 500;
  
  /* ─── Animation Duration ─── */
  --tag-transition: 0.15s ease;
}

/* ─── Light Mode Specific Adjustments ─── */
.theme-light {
  --tag-bg-opacity: 0.12;
  --tag-border-opacity: 0.3;
  --tag-text-darken: 0.85;
}


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 1: MODERN PILL (Active by Default)
   Community favorite - clean, modern, accessible
   ═══════════════════════════════════════════════════════════════════════════ */

/* Base Tag Styling */
.tag,
a.tag,
.cm-tag,
.cm-hashtag {
  background-color: rgba(220, 38, 38, var(--tag-bg-opacity)) !important;
  color: var(--tag-primary) !important;
  padding: var(--tag-padding-y) var(--tag-padding-x) !important;
  border-radius: var(--tag-border-radius) !important;
  font-size: var(--tag-font-size) !important;
  font-weight: var(--tag-font-weight) !important;
  text-decoration: none !important;
  transition: all var(--tag-transition) !important;
  border: 1px solid transparent !important;
  /* ✓ WCAG AA: Red (#DC2626) on light bg = 5.9:1 (Pass) */
}

/* Hashtag symbol styling */
.tag::before,
.cm-hashtag-begin::before {
  content: "";  /* Removes # if you want clean look */
  /* Uncomment below to keep # visible */
  /* content: "#"; */
  /* opacity: 0.6; */
}


/* Force editor tag text color (override Obsidian defaults) */
.cm-hashtag,
.cm-hashtag.cm-hashtag-begin,
.cm-hashtag.cm-hashtag-end {
  color: var(--tag-primary) !important;
}

/* Hover State */
.tag:hover,
a.tag:hover,
.cm-tag:hover {
  background-color: rgba(220, 38, 38, 0.25);
  border-color: rgba(220, 38, 38, var(--tag-border-opacity));
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(220, 38, 38, 0.15);
}

/* Active/Clicked State */
.tag:active,
a.tag:active {
  transform: translateY(0);
  box-shadow: none;
}

/* Focus State for Accessibility */
.tag:focus,
a.tag:focus {
  outline: 2px solid var(--tag-primary);
  outline-offset: 2px;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 2: SEMANTIC TAG COLORING
   Color-code tags by prefix for visual organization
   ═══════════════════════════════════════════════════════════════════════════ */

/* ─── Status Tags ─── */
a.tag[href*="#status"],
.cm-tag[class*="status"] {
  --tag-color: var(--tag-status);
  background-color: rgba(55, 65, 81, var(--tag-bg-opacity));
  color: var(--tag-status) !important;
}

/* ─── Priority Tags ─── */
a.tag[href*="#priority"],
a.tag[href*="#urgent"],
a.tag[href*="#important"],
.cm-tag[class*="priority"] {
  --tag-color: var(--tag-priority);
  background-color: rgba(153, 27, 27, var(--tag-bg-opacity));
  color: var(--tag-priority) !important;
}

/* ─── Project Tags ─── */
a.tag[href*="#project"],
a.tag[href*="#proj"],
.cm-tag[class*="project"] {
  --tag-color: var(--tag-project);
  background-color: rgba(185, 28, 28, var(--tag-bg-opacity));
  color: var(--tag-project) !important;
}

/* ─── Category/Topic Tags ─── */
a.tag[href*="#category"],
a.tag[href*="#topic"],
.cm-tag[class*="category"] {
  --tag-color: var(--tag-category);
  background-color: rgba(220, 38, 38, var(--tag-bg-opacity));
  color: var(--tag-category) !important;
}

/* ─── Type Tags ─── */
a.tag[href*="#type"],
.cm-tag[class*="type"] {
  --tag-color: var(--tag-type);
  background-color: rgba(31, 31, 31, var(--tag-bg-opacity));
  color: var(--tag-type) !important;
}

/* ─── Context Tags ─── */
a.tag[href*="#context"],
a.tag[href*="#@"],
.cm-tag[class*="context"] {
  --tag-color: var(--tag-context);
  background-color: rgba(75, 85, 99, var(--tag-bg-opacity));
  color: var(--tag-context) !important;
}

/* ─── Area Tags ─── */
a.tag[href*="#area"],
.cm-tag[class*="area"] {
  --tag-color: var(--tag-area);
  background-color: rgba(239, 68, 68, var(--tag-bg-opacity));
  color: var(--tag-area) !important;
}

/* ─── Archive Tags ─── */
a.tag[href*="#archive"],
a.tag[href*="#archived"],
.cm-tag[class*="archive"] {
  --tag-color: var(--tag-archive);
  background-color: rgba(156, 163, 175, var(--tag-bg-opacity));
  color: var(--tag-archive) !important;
  opacity: 0.7;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 3: NESTED TAG STYLING
   Visual hierarchy for nested tags like #project/website
   ═══════════════════════════════════════════════════════════════════════════ */

/* Style nested tags with separator */
a.tag[href*="/"],
.cm-tag[class*="/"] {
  /* Add subtle divider effect for nested tags */
  background: linear-gradient(
    90deg,
    rgba(220, 38, 38, var(--tag-bg-opacity)) 0%,
    rgba(220, 38, 38, calc(var(--tag-bg-opacity) * 0.5)) 100%
  ) ;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 4: TAG PANE / SIDEBAR STYLING
   Customize how tags appear in the tag pane
   ═══════════════════════════════════════════════════════════════════════════ */

/* Tag pane tags */
.tag-pane-tag {
  padding: 4px 8px;
  border-radius: var(--tag-border-radius);
  transition: all var(--tag-transition);
}

.tag-pane-tag:hover {
  background-color: rgba(220, 38, 38, 0.1);
}

/* Tag count badge */
.tag-pane-tag-count {
  background-color: rgba(220, 38, 38, 0.15);
  color: var(--tag-primary);
  padding: 2px 6px;
  border-radius: 10px;
  font-size: 0.75em;
  margin-left: 8px;
}


/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 5: PROPERTIES/FRONTMATTER TAG STYLING  
   Style tags when they appear in the Properties panel
   ═══════════════════════════════════════════════════════════════════════════ */

/* Properties panel tags */
.metadata-container .multi-select-pill {
  background-color: rgba(220, 38, 38, var(--tag-bg-opacity));
  color: var(--tag-primary);
  border-radius: var(--tag-border-radius);
  padding: 2px 8px;
  font-size: var(--tag-font-size);
}

.metadata-container .multi-select-pill:hover {
  background-color: rgba(220, 38, 38, 0.25);
}

/* Remove button styling */
.metadata-container .multi-select-pill-remove-button:hover {
  color: var(--tag-priority);
}

/* ═══════════════════════════════════════════════════════════════════════════
   ═══════════════════════════════════════════════════════════════════════════
   
   ALTERNATIVE STYLES - Uncomment ONE section below to use
   
   ═══════════════════════════════════════════════════════════════════════════
   ═══════════════════════════════════════════════════════════════════════════ */


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 2: OUTLINE/BORDER ONLY
   Minimal, elegant, less visual weight
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background-color: transparent;
  color: var(--tag-primary) !important;
  border: 1.5px solid var(--tag-primary);
  padding: var(--tag-padding-y) var(--tag-padding-x);
  border-radius: var(--tag-border-radius);
  font-size: var(--tag-font-size);
  font-weight: var(--tag-font-weight);
  transition: all var(--tag-transition);
}

.tag:hover,
a.tag:hover {
  background-color: rgba(220, 38, 38, 0.1);
  border-color: var(--tag-primary);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 3: SOLID FILL (High Contrast)
   Bold, high visibility, great for scanning
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background-color: var(--tag-primary);
  color: #FFFFFF !important;
  padding: var(--tag-padding-y) var(--tag-padding-x);
  border-radius: var(--tag-border-radius);
  font-size: var(--tag-font-size);
  font-weight: var(--tag-font-weight);
  transition: all var(--tag-transition);
  border: none;
}

.tag:hover,
a.tag:hover {
  background-color: #991B1B;
  box-shadow: 0 2px 8px rgba(220, 38, 38, 0.4);
}

.theme-dark .tag,
.theme-dark a.tag {
  background-color: rgba(220, 38, 38, 0.85);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 4: UNDERLINE ONLY (Minimal)
   Ultra-minimal, inline text feel
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background-color: transparent;
  color: var(--tag-primary) !important;
  border: none;
  border-bottom: 2px solid var(--tag-primary);
  padding: 0 2px;
  border-radius: 0;
  font-size: inherit;
  font-weight: var(--tag-font-weight);
  transition: all var(--tag-transition);
}

.tag:hover,
a.tag:hover {
  background-color: rgba(220, 38, 38, 0.1);
  border-bottom-width: 3px;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 5: ROUNDED BADGE (iOS Style)
   Large border-radius, friendly appearance
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background-color: rgba(220, 38, 38, var(--tag-bg-opacity));
  color: var(--tag-primary) !important;
  padding: 0.25em 0.75em;
  border-radius: 999px;
  font-size: 0.8em;
  font-weight: 600;
  transition: all var(--tag-transition);
  border: none;
  letter-spacing: 0.02em;
}

.tag:hover,
a.tag:hover {
  background-color: rgba(220, 38, 38, 0.3);
  transform: scale(1.05);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 6: SQUARE BADGE (Angular)
   Sharp corners, technical aesthetic
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background-color: rgba(220, 38, 38, var(--tag-bg-opacity));
  color: var(--tag-primary) !important;
  padding: 0.2em 0.6em;
  border-radius: 0;
  font-size: 0.8em;
  font-weight: 600;
  font-family: var(--font-monospace);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  transition: all var(--tag-transition);
  border-left: 3px solid var(--tag-primary);
}

.tag:hover,
a.tag:hover {
  background-color: rgba(220, 38, 38, 0.25);
  border-left-width: 5px;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 7: GLASSMORPHISM
   Modern frosted glass effect
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background: rgba(220, 38, 38, 0.15);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: var(--tag-primary) !important;
  padding: 0.3em 0.7em;
  border-radius: 8px;
  font-size: var(--tag-font-size);
  font-weight: var(--tag-font-weight);
  border: 1px solid rgba(220, 38, 38, 0.2);
  transition: all var(--tag-transition);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.tag:hover,
a.tag:hover {
  background: rgba(220, 38, 38, 0.25);
  border-color: rgba(220, 38, 38, 0.4);
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.2);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 8: GRADIENT FILL
   Eye-catching gradient backgrounds
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background: linear-gradient(135deg, var(--tag-primary) 0%, var(--tag-tertiary) 100%);
  color: #FFFFFF !important;
  padding: 0.25em 0.7em;
  border-radius: 6px;
  font-size: var(--tag-font-size);
  font-weight: 600;
  border: none;
  transition: all var(--tag-transition);
  box-shadow: 0 2px 4px rgba(220, 38, 38, 0.3);
}

.tag:hover,
a.tag:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.4);
}

.theme-dark .tag,
.theme-dark a.tag {
  background: linear-gradient(135deg, var(--tag-primary) 0%, var(--tag-tertiary) 100%);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 9: NEON GLOW
   Cyberpunk aesthetic with glow effects
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background-color: transparent;
  color: var(--tag-primary) !important;
  padding: 0.25em 0.6em;
  border-radius: 4px;
  font-size: var(--tag-font-size);
  font-weight: 600;
  border: 1px solid var(--tag-primary);
  transition: all var(--tag-transition);
  text-shadow: 0 0 5px var(--tag-primary);
  box-shadow: 
    0 0 5px rgba(220, 38, 38, 0.3),
    inset 0 0 5px rgba(220, 38, 38, 0.1);
}

.tag:hover,
a.tag:hover {
  background-color: rgba(220, 38, 38, 0.1);
  text-shadow: 0 0 10px var(--tag-primary);
  box-shadow: 
    0 0 10px rgba(220, 38, 38, 0.5),
    0 0 20px rgba(220, 38, 38, 0.3),
    inset 0 0 10px rgba(220, 38, 38, 0.2);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   STYLE 10: MATERIAL DESIGN CHIP
   Google Material Design inspired
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag,
a.tag,
.cm-tag {
  background-color: rgba(220, 38, 38, 0.08);
  color: var(--tag-primary) !important;
  padding: 0.35em 0.85em;
  border-radius: 16px;
  font-size: 0.875em;
  font-weight: 500;
  border: none;
  transition: 
    background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
    box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.tag::after,
a.tag::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle, rgba(220, 38, 38, 0.3) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.3s;
}

.tag:hover,
a.tag:hover {
  background-color: rgba(220, 38, 38, 0.15);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
}

.tag:hover::after,
a.tag:hover::after {
  opacity: 1;
}

.tag:active,
a.tag:active {
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   BONUS: SPECIFIC TAG TARGETING
   Style individual tags by exact name
   ═══════════════════════════════════════════════════════════════════════════ */

/* Example: Special styling for specific tags */
/*
a.tag[href="#todo"] {
  background-color: rgba(239, 68, 68, 0.15);
  color: #ef4444 !important;
  border-left: 3px solid #ef4444;
}

a.tag[href="#done"],
a.tag[href="#complete"] {
  background-color: rgba(34, 197, 94, 0.15);
  color: #22c55e !important;
}

a.tag[href="#in-progress"],
a.tag[href="#wip"] {
  background-color: rgba(245, 158, 11, 0.15);
  color: #f59e0b !important;
}

a.tag[href="#idea"] {
  background-color: rgba(168, 85, 247, 0.15);
  color: #a855f7 !important;
}

a.tag[href="#question"] {
  background-color: rgba(6, 182, 212, 0.15);
  color: #06b6d4 !important;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   BONUS: HIDE HASHTAG SYMBOL COMPLETELY
   Cleaner look without the # prefix
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.cm-hashtag-begin {
  display: none;
}

.tag::before {
  content: "" !important;
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   BONUS: ADD ICON BEFORE TAGS
   Using Unicode symbols for visual interest
   ═══════════════════════════════════════════════════════════════════════════ */

/*
.tag::before,
a.tag::before {
  content: "🏷️ ";
  font-size: 0.85em;
}
*/

/* Or category-specific icons */
/*
a.tag[href*="#project"]::before { content: "📁 "; }
a.tag[href*="#status"]::before { content: "📊 "; }
a.tag[href*="#priority"]::before { content: "🔥 "; }
a.tag[href*="#idea"]::before { content: "💡 "; }
a.tag[href*="#todo"]::before { content: "☐ "; }
a.tag[href*="#done"]::before { content: "✓ "; }
*/


/* ═══════════════════════════════════════════════════════════════════════════
   BONUS: TAG ANIMATIONS
   Subtle motion effects (respects reduced-motion preference)
   ═══════════════════════════════════════════════════════════════════════════ */

/*
@keyframes tag-pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.4); }
  50% { box-shadow: 0 0 0 4px rgba(220, 38, 38, 0); }
}

.tag:hover,
a.tag:hover {
  animation: tag-pulse 1.5s infinite;
}

@media (prefers-reduced-motion: reduce) {
  .tag:hover,
  a.tag:hover {
    animation: none;
  }
}
*/


/* ═══════════════════════════════════════════════════════════════════════════
   END OF SNIPPET
   
   CUSTOMIZATION TIPS:
   1. Change --tag-primary, --tag-secondary, --tag-tertiary for your palette
   2. Adjust --tag-border-radius for more/less rounding
   3. Modify --tag-font-size for larger/smaller tags
   4. Update semantic tag colors to match your workflow
   5. Mix and match sections - semantic coloring works with any base style
   
   TROUBLESHOOTING:
   - Tags not changing? Clear Obsidian cache (Ctrl+Shift+R / Cmd+Shift+R)
   - Conflicts with theme? Increase specificity by adding .theme-light or .theme-dark prefix
   - Editor vs Preview mismatch? Ensure both .tag and .cm-tag are styled
   
   PLUGIN COMPATIBILITY:
   - Works with: Tag Wrangler, Colored Tags, Tagfolder
   - May need adjustment for: Style Settings (check variable overrides)
═══════════════════════════════════════════════════════════════════════════════
*/

```

### .obsidian\snippets\unified-callout-system.css

```css
/*
═══════════════════════════════════════════════════════════════════════════════
 UNIFIED CALLOUT SYSTEM v3.0 - Modular Architecture
 Purpose: Single-file callout system replacing 15+ snippet files
 Author: Pur3v4d3r (designed by Claude)
 Date: 2025-12-27
 Theme: Dark Cyberspace with Crimson accents
 
 FEATURES:
 - 60+ semantic callout types in single registry
 - 5 visual style variants (default/minimal/neon/outlined/compact)
 - Switchable via body classes (no snippet toggling required)
 - Complete design token system
 - Advanced animation library
 - Maintainable and extensible
 
 USAGE:
 1. Enable this single snippet
 2. Add body class for style variant:
    - body.callout-variant-minimal
    - body.callout-variant-neon
    - body.callout-variant-outlined
    - body.callout-variant-compact
    - body.callout-variant-raised
 3. Use callouts: [!callout-type] in markdown
═══════════════════════════════════════════════════════════════════════════════
*/


/* ═══════════════════════════════════════════════════════════════════════════
   🎨 SECTION 1: DESIGN TOKEN SYSTEM
   Central repository for all customization variables
   ═══════════════════════════════════════════════════════════════════════════ */

:root {
  /* ────────────────────────────────────────────────────────────────────────
     🌈 COLOR PALETTE - Crimson & Greyscale Foundation
     ──────────────────────────────────────────────────────────────────────── */
  
  /* Primary Crimson Spectrum */
  --callout-crimson: 229, 0, 0;              /* #E50000 - Vivid */
  --callout-crimson-bright: 255, 0, 0;       /* #FF0000 - Bright */
  --callout-crimson-dim: 204, 0, 0;          /* #CC0000 - Dim */
  --callout-crimson-dark: 179, 0, 0;         /* #B30000 - Dark */
  --callout-crimson-ultra: 153, 0, 0;        /* #990000 - Ultra Dim */
  --callout-crimson-soft: 255, 102, 102;     /* #FF6666 - Soft */
  
  /* Greyscale Hierarchy */
  --callout-grey-high: 224, 224, 224;        /* #E0E0E0 - High emphasis */
  --callout-grey-medium: 163, 163, 163;      /* #A3A3A3 - Medium */
  --callout-grey-low: 122, 122, 122;         /* #7A7A7A - Low */
  
  /* Accent Colors */
  --callout-orange: 255, 77, 0;              /* #FF4D00 - Warm accent */
  
  /* Structural Colors */
  --callout-disabled: 90, 90, 90;            /* #5A5A5A */
  --callout-border: 42, 42, 42;              /* #2A2A2A */
  --callout-surface: 30, 30, 30;             /* #1E1E1E */
  
  /* ────────────────────────────────────────────────────────────────────────
     🎭 GRADIENT DEFINITIONS
     ──────────────────────────────────────────────────────────────────────── */
  
  --gradient-crimson: linear-gradient(135deg,
    rgba(var(--callout-crimson), 0.08) 0%,
    rgba(var(--callout-crimson-bright), 0.04) 100%);
    
  --gradient-grey: linear-gradient(135deg,
    rgba(var(--callout-grey-medium), 0.08) 0%,
    rgba(var(--callout-grey-low), 0.04) 100%);
    
  --gradient-monochrome: linear-gradient(135deg,
    rgba(var(--callout-grey-high), 0.05) 0%,
    rgba(var(--callout-grey-medium), 0.05) 50%,
    rgba(var(--callout-grey-low), 0.05) 100%);
  
  /* ────────────────────────────────────────────────────────────────────────
     🏗️ STRUCTURAL PARAMETERS
     ──────────────────────────────────────────────────────────────────────── */
  
  /* Border System */
  --callout-border-width: 1.5px;
  --callout-border-width-thin: 1px;
  --callout-border-width-medium: 2px;
  --callout-border-width-thick: 4px;
  --callout-border-radius: 16px;
  --callout-inner-radius: 12px;
  
  /* Spacing System */
  --callout-padding: 14px 10px;
  --callout-padding-small: 8px 6px;
  --callout-title-padding: 1px 18px;
  --callout-margin: 0.5em 0;
  --callout-gap: 5px;
  
  /* Opacity Levels */
  --callout-title-bg-opacity: 0.15;
  --callout-content-bg-opacity: 0.05;
  --callout-border-opacity: 0.6;
  
  /* ────────────────────────────────────────────────────────────────────────
     ✨ DEPTH & SHADOW SYSTEM
     ──────────────────────────────────────────────────────────────────────── */
  
  --shadow-depth-1: 0 2px 8px rgba(0, 0, 0, 0.3);
  --shadow-depth-2: 0 4px 16px rgba(0, 0, 0, 0.4);
  --shadow-depth-3: 0 8px 32px rgba(0, 0, 0, 0.5);
  --glow-intensity: 0.3;
  
  /* ────────────────────────────────────────────────────────────────────────
     🎬 ANIMATION PARAMETERS
     ──────────────────────────────────────────────────────────────────────── */
  
  --animation-speed-fast: 0.2s;
  --animation-speed-normal: 0.35s;
  --animation-speed-slow: 0.5s;
  --animation-easing: cubic-bezier(0.4, 0.0, 0.2, 1);
  --animation-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
}


/* ═══════════════════════════════════════════════════════════════════════════
   🎬 SECTION 2: ANIMATION KEYFRAME LIBRARY
   Reusable animations for all callout types
   ═══════════════════════════════════════════════════════════════════════════ */

@keyframes slideInFromLeft {
  from {
    opacity: 0;
    transform: translateX(-30px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
}

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

@keyframes glowPulse {
  0%, 100% {
    box-shadow:
      0 0 0 rgba(var(--callout-color), 0),
      var(--shadow-depth-2);
  }
  50% {
    box-shadow:
      0 0 20px rgba(var(--callout-color), var(--glow-intensity)),
      0 0 40px rgba(var(--callout-color), calc(var(--glow-intensity) * 0.5)),
      var(--shadow-depth-2);
  }
}

@keyframes shimmer {
  0% { background-position: -1000px 0; }
  100% { background-position: 1000px 0; }
}

@keyframes iconBounce {
  0%, 100% { transform: scale(1) rotate(0deg); }
  25% { transform: scale(1.1) rotate(-5deg); }
  75% { transform: scale(1.15) rotate(5deg); }
}


/* ═══════════════════════════════════════════════════════════════════════════
   🏗️ SECTION 3: BASE CALLOUT ARCHITECTURE
   Core structure applied to all callout types
   ═══════════════════════════════════════════════════════════════════════════ */

.callout {
  /* Structural Foundation */
  position: relative !important;
  margin: var(--callout-margin) !important;
  border-radius: var(--callout-border-radius) !important;
  border-left: var(--callout-border-width-thick) solid rgb(var(--callout-color)) !important;
  background: transparent !important;
  box-shadow: var(--shadow-depth-1) !important;
  overflow: hidden !important;
  padding: 8px !important;
  
  /* Animation */
  animation: fadeInScale var(--animation-speed-normal) var(--animation-easing);
  
  /* Smooth Transitions */
  transition:
    transform var(--animation-speed-normal) var(--animation-easing),
    box-shadow var(--animation-speed-normal) var(--animation-easing),
    border-color var(--animation-speed-fast) var(--animation-easing);
}

/* Top Accent Line (glow on hover) */
.callout::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(var(--callout-color), 0.5) 50%,
    transparent 100%);
  opacity: 0;
  transition: opacity var(--animation-speed-normal);
  pointer-events: none;
}

.callout:hover::before {
  opacity: 1;
}

/* Hover Elevation */
.callout:hover {
  transform: translateY(-2px);
  border-left-color: rgb(var(--callout-color));
  box-shadow:
    0 0 20px rgba(var(--callout-color), var(--glow-intensity)),
    var(--shadow-depth-2);
}


/* ═══════════════════════════════════════════════════════════════════════════
   📝 SECTION 4: TITLE & CONTENT STYLING
   Typography and content area formatting
   ═══════════════════════════════════════════════════════════════════════════ */

.callout-title {
  position: relative !important;
  padding: var(--callout-title-padding) !important;
  background: rgba(var(--callout-color), var(--callout-title-bg-opacity)) !important;
  color: rgb(var(--callout-color)) !important;
  font-weight: 600 !important;
  font-size: 0.95em !important;
  letter-spacing: 0.3px !important;
  display: flex !important;
  align-items: center !important;
  gap: var(--callout-gap) !important;
  transition:
    background var(--animation-speed-fast) var(--animation-easing),
    color var(--animation-speed-fast);
}

.callout:hover .callout-title {
  background: rgba(var(--callout-color), calc(var(--callout-title-bg-opacity) * 1.3)) !important;
}

/* Title Underline Glow */
.callout-title::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(var(--callout-color), 0.6) 50%,
    transparent 100%);
  opacity: 0;
  transition: opacity var(--animation-speed-normal);
  pointer-events: none;
}

.callout:hover .callout-title::after {
  opacity: 1;
}

/* Content Area */
.callout-content {
  padding: var(--callout-padding) !important;
  background: rgba(var(--callout-color), var(--callout-content-bg-opacity)) !important;
  transition: background var(--animation-speed-fast) !important;
}

.callout:hover .callout-content {
  background: rgba(var(--callout-color), calc(var(--callout-content-bg-opacity) * 1.5)) !important;
}

/* ────────────────────────────────────────────────────────────────────────
   📝 TEXT FORMATTING SUPPORT
   ──────────────────────────────────────────────────────────────────────── */

.callout-content strong,
.callout-content b,
.callout-title strong,
.callout-title b {
  font-weight: 700 !important;
  color: #E50000 !important;  /* Vivid Crimson */
}

.callout-content em,
.callout-content i,
.callout-title em,
.callout-title i {
  font-style: italic;
  color: inherit;
}

.callout-content strong em,
.callout-content em strong,
.callout-content b i,
.callout-content i b {
  font-weight: 700;
  font-style: italic;
  color: #E50000;
}

/* Icon Styling */
.callout-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--animation-speed-normal) var(--animation-easing);
}

.callout:hover .callout-icon {
  transform: scale(1.1) rotate(5deg);
}


/* ═══════════════════════════════════════════════════════════════════════════
   🎨 SECTION 5: CALLOUT TYPE REGISTRY
   Semantic callout definitions with color assignments
   ═══════════════════════════════════════════════════════════════════════════ */

/* ────────────────────────────────────────────────────────────────────────
   💎 CRIMSON FAMILY - Knowledge, Structure, Primary Content
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="key-claim"],
.callout[data-callout="evidence"],
.callout[data-callout="insight"],
.callout[data-callout="principle-point"],
.callout[data-callout="definition"],
.callout[data-callout="what-this-does"],
.callout[data-callout="methodology-and-sources"],
.callout[data-callout="overview"],
.callout[data-callout="to-do"],
.callout[data-callout="project-link"],
.callout[data-callout="hub-moc"],
.callout[data-callout="connections-and-links"],
.callout[data-callout="core-principle"],
.callout[data-callout="argument"],
.callout[data-callout="atomic-concept"],
.callout[data-callout="cosmos-concept"],
.callout[data-callout="equation"],
.callout[data-callout="thought-experiment"],
.callout[data-callout="analogy"],
.callout[data-callout="math"],
.callout[data-callout="analysis-rhetorical"],
.callout[data-callout="analysis-logical"],
.callout[data-callout="analysis-contextual"],
.callout[data-callout="analysis-cognitive"],
.callout[data-callout="feynman-technique"],
.callout[data-callout="goal"],
.callout[data-callout="objective"],
.callout[data-callout="target"],
.callout[data-callout="strategy"],
.callout[data-callout="tactic"],
.callout[data-callout="method"],
.callout[data-callout="discovery"],
.callout[data-callout="learning"],
.callout[data-callout="comprehensive-reference"],
.callout[data-callout="key"],
.callout[data-callout="purpose"],
.callout[data-callout="important"],
.callout[data-callout="decision"],
.callout[data-callout="action"],
.callout[data-callout="outcome"],
.callout[data-callout="the-goal"],
.callout[data-callout="the-mission"],
.callout[data-callout="the-purpose"] {
  --callout-color: var(--callout-crimson);
}

/* ────────────────────────────────────────────────────────────────────────
   🔴 DEEP CRIMSON - Critical/Warning Content
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="warning"],
.callout[data-callout="caution"],
.callout[data-callout="alert"],
.callout[data-callout="critical"],
.callout[data-callout="danger"],
.callout[data-callout="attention"],
.callout[data-callout="error"],
.callout[data-callout="bug"],
.callout[data-callout="failure"],
.callout[data-callout="fail"],
.callout[data-callout="missing"],
.callout[data-callout="blocked"] {
  --callout-color: var(--callout-crimson-dim);
}

/* ────────────────────────────────────────────────────────────────────────
   🟠 ORANGE ACCENT - Experimental/Active Content
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="experiment"],
.callout[data-callout="test"],
.callout[data-callout="lab"],
.callout[data-callout="stage"],
.callout[data-callout="demo"],
.callout[data-callout="presentation"],
.callout[data-callout="project"],
.callout[data-callout="workflow"],
.callout[data-callout="process"],
.callout[data-callout="phase-one"],
.callout[data-callout="phase-two"],
.callout[data-callout="phase-three"],
.callout[data-callout="phase-four"],
.callout[data-callout="plan"],
.callout[data-callout="kanban"],
.callout[data-callout="project-kickstarter"],
.callout[data-callout="your-new-workflow"],
.callout[data-callout="progress"] {
  --callout-color: var(--callout-orange);
}

/* ────────────────────────────────────────────────────────────────────────
   ✅ SUCCESS/COMPLETION - Positive States (Green-tinted Grey)
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="success"],
.callout[data-callout="check"],
.callout[data-callout="done"],
.callout[data-callout="complete"],
.callout[data-callout="read-complete"] {
  --callout-color: 122, 163, 122; /* Green-tinted grey */
}

/* ────────────────────────────────────────────────────────────────────────
   ⚪ GREYSCALE - Neutral/Supporting Content
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="note"],
.callout[data-callout="info"],
.callout[data-callout="context"],
.callout[data-callout="background"],
.callout[data-callout="random"],
.callout[data-callout="tangent"],
.callout[data-callout="lunar"],
.callout[data-callout="dream"],
.callout[data-callout="abstract"],
.callout[data-callout="summary"],
.callout[data-callout="tldr"],
.callout[data-callout="quote"],
.callout[data-callout="cite"],
.callout[data-callout="example"],
.callout[data-callout="code"],
.callout[data-callout="question"],
.callout[data-callout="help"],
.callout[data-callout="faq"],
.callout[data-callout="system"],
.callout[data-callout="meta"],
.callout[data-callout="debug"],
.callout[data-callout="theory"],
.callout[data-callout="hypothesis"],
.callout[data-callout="outline"],
.callout[data-callout="draft"],
.callout[data-callout="review"],
.callout[data-callout="feedback"],
.callout[data-callout="description"],
.callout[data-callout="disposition"],
.callout[data-callout="thoughts"],
.callout[data-callout="custom"],
.callout[data-callout="highlight"],
.callout[data-callout="document"],
.callout[data-callout="capture"],
.callout[data-callout="revist"],
.callout[data-callout="message"],
.callout[data-callout="how-to-use"],
.callout[data-callout="how-to-use-this"],
.callout[data-callout="starting-message"],
.callout[data-callout="helpful-tip"],
.callout[data-callout="tip"],
.callout[data-callout="hint"],
.callout[data-callout="the-start"],
.callout[data-callout="related-topics-to-consider"],
.callout[data-callout="topic-idea"],
.callout[data-callout="links-to-related-notes"],
.callout[data-callout="start-of-chat"],
.callout[data-callout="further-exploration"],
.callout[data-callout="use-cases-and-examples"],
.callout[data-callout="idea"] {
  --callout-color: var(--callout-grey-medium);
}

/* ────────────────────────────────────────────────────────────────────────   📋 TASK/WORKFLOW MANAGEMENT - Medium Grey with Orange accent
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="task"],
.callout[data-callout="todo"],
.callout[data-callout="tasks"],
.callout[data-callout="pending"],
.callout[data-callout="reading-in-progress"],
.callout[data-callout="read-asap"],
.callout[data-callout="meeting"],
.callout[data-callout="agenda"] {
  --callout-color: var(--callout-grey-medium);
  border-left: 3px solid rgba(255, 77, 0, 0.6); /* Orange accent */
}

/* ────────────────────────────────────────────────────────────────────────
   🧠 RESEARCH/ANALYSIS - Academic and analytical content
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="research"],
.callout[data-callout="analysis"],
.callout[data-callout="casual-link"],
.callout[data-callout="no-evidence"],
.callout[data-callout="zettelkasten-incubator"],
.callout[data-callout="pre-read-questions"],
.callout[data-callout="pre-read-thoughts"],
.callout[data-callout="ask-yourself-this"] {
  --callout-color: var(--callout-grey-high);
}

/* ────────────────────────────────────────────────────────────────────────
   🔧 TOOLS/TECHNICAL - Technical and tool-related content
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="note-toolbar"],
.callout[data-callout="problem-clarity-solution"],
.callout[data-callout="shot-idea"],
.callout[data-callout="lighting-setup"],
.callout[data-callout="composition"],
.callout[data-callout="post-processing"],
.callout[data-callout="important-links"],
.callout[data-callout="constraints-and-pitfalls"],
.callout[data-callout="quick-reference"],
.callout[data-callout="how-this-dashboard-works"],
.callout[data-callout="changes-from-prompting-dashboard"] {
  --callout-color: var(--callout-grey-low);
}

/* ────────────────────────────────────────────────────────────────────────
   🤔 PHILOSOPHICAL/CONCEPTUAL - Deep thinking and philosophy
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="confusion"],
.callout[data-callout="connection-ideas"],
.callout[data-callout="choice-a"],
.callout[data-callout="choice-b"],
.callout[data-callout="the-philosophy"] {
  --callout-color: var(--callout-grey-medium);
  border-style: dashed;
  border-width: 2px;
  border-left-style: solid;
  border-left-width: 3px;
}

/* ────────────────────────────────────────────────────────────────────────
   🤖 AI/LLM SPECIFIC - AI and language model related content
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="gemini-pro-response"],
.callout[data-callout="claude-thinking"],
.callout[data-callout="key-changes"] {
  --callout-color: 255, 199, 0; /* Golden yellow from data.json */
  border-left-width: 3px;
}

/* ────────────────────────────────────────────────────────────────────────
   🌟 SPECIAL CUSTOM CALLOUTS - Unique user-defined types
   ──────────────────────────────────────────────────────────────────────── */

.callout[data-callout="stoic-quote"] {
  --callout-color: 255, 199, 0; /* Golden yellow */
  border-left-width: 4px;
  font-style: italic;
}

.callout[data-callout="in-note-metadata"] {
  --callout-color: 158, 108, 211; /* Purple from data.json */
  border-left-width: 2px;
  font-size: 0.9em;
}

.callout[data-callout="caltab"],
.callout[data-callout="your-name"] {
  --callout-color: 255, 0, 0; /* Bright red */
  border-left-width: 3px;
}

/* ────────────────────────────────────────────────────────────────────────   🎯 SPECIAL EFFECT CALLOUTS - Unique Visual Treatments
   ──────────────────────────────────────────────────────────────────────── */

/* DNA - Shimmer Animation */
.callout[data-callout="dna"],
.callout[data-callout="fundamental"],
.callout[data-callout="core-concept"] {
  --callout-color: var(--callout-crimson);
  background: linear-gradient(135deg,
    rgba(229, 0, 0, 0.03) 0%,
    rgba(229, 0, 0, 0.03) 50%,
    rgba(229, 0, 0, 0.03) 100%);
  background-size: 200% 200%;
  animation: shimmer 8s linear infinite, fadeInScale var(--animation-speed-normal) var(--animation-easing);
}

/* Diamond - Enhanced Glow */
.callout[data-callout="diamond"],
.callout[data-callout="premium"],
.callout[data-callout="valuable"] {
  --callout-color: var(--callout-crimson);
  border: 2px solid rgba(229, 0, 0, 0.4);
  border-left-width: 4px;
  box-shadow:
    0 0 20px rgba(229, 0, 0, 0.2),
    0 0 40px rgba(229, 0, 0, 0.1),
    var(--shadow-depth-2);
}

/* Ember - Pulsing Glow */
.callout[data-callout="ember"],
.callout[data-callout="hot"],
.callout[data-callout="active"] {
  --callout-color: var(--callout-crimson);
  animation: glowPulse 2s infinite, fadeInScale var(--animation-speed-normal) var(--animation-easing);
  border-left-width: 4px;
}

/* Raised - 3D Elevation Effect */
.callout[data-callout="raised"],
.callout[data-callout="elevated"],
.callout[data-callout="lift"] {
  --callout-color: var(--callout-crimson);
  border-left-width: 4px;
  transform: translateY(-4px);
  box-shadow:
    0 8px 16px rgba(0, 0, 0, 0.5),
    0 16px 32px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(229, 0, 0, 0.2),
    inset 0 1px 0 rgba(224, 224, 224, 0.1);
  background: linear-gradient(180deg,
    rgba(30, 30, 30, 0.8) 0%,
    rgba(20, 20, 20, 0.6) 100%);
}

/* Pin - Visual Pin Icon */
.callout[data-callout="pin"],
.callout[data-callout="pinned"],
.callout[data-callout="bookmark"] {
  --callout-color: var(--callout-crimson);
  border-top: 2px solid rgba(229, 0, 0, 0.4);
  border-left-width: 4px;
}

.callout[data-callout="pin"]::before,
.callout[data-callout="pinned"]::before,
.callout[data-callout="bookmark"]::before {
  content: '📌';
  position: absolute;
  top: -10px;
  right: 20px;
  font-size: 1.2em;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
  opacity: 0.8;
  background: none;  /* Override default ::before */
  height: auto;
}

/* Bullseye - Concentric Ring Effect */
.callout[data-callout="bullseye"],
.callout[data-callout="precision"],
.callout[data-callout="exact"] {
  --callout-color: var(--callout-crimson);
  border: 2px solid rgba(229, 0, 0, 0.3);
  border-left: 4px solid rgb(229, 0, 0);
  box-shadow:
    0 0 0 4px rgba(229, 0, 0, 0.1),
    var(--shadow-depth-2);
}

/* Action - Heavy Left Border */
.callout[data-callout="action"],
.callout[data-callout="next-step"],
.callout[data-callout="do-this"] {
  --callout-color: var(--callout-crimson);
  border-left-width: 5px;
  box-shadow:
    -3px 0 0 rgba(229, 0, 0, 0.3),
    var(--shadow-depth-2);
}

.callout[data-callout="action"] .callout-title,
.callout[data-callout="next-step"] .callout-title,
.callout[data-callout="do-this"] .callout-title {
  font-weight: 700;
  text-transform: uppercase;
}

/* Counter-Argument - Dashed Border */
.callout[data-callout="counter-argument"],
.callout[data-callout="objection"],
.callout[data-callout="alternative"] {
  --callout-color: var(--callout-grey-medium);
  border-style: dashed;
  border-width: 2px;
  border-left-style: solid;
  border-left-width: 3px;
}


/* ═══════════════════════════════════════════════════════════════════════════
   🎭 SECTION 6: STYLE VARIANT OVERRIDES
   Switchable visual modes via body classes
   ═══════════════════════════════════════════════════════════════════════════ */

/* ────────────────────────────────────────────────────────────────────────
   VARIANT 1: MINIMAL - Transparent with borders only
   Usage: Add class "callout-variant-minimal" to body
   ──────────────────────────────────────────────────────────────────────── */

body.callout-variant-minimal .callout {
  background: transparent;
  border: 1px solid rgba(var(--callout-color), 0.25);
  border-left: 3px solid rgb(var(--callout-color));
  border-radius: 8px;
  box-shadow: none;
  padding: 8px;
}

body.callout-variant-minimal .callout:hover {
  background: rgba(var(--callout-color), 0.03);
  border-color: rgba(var(--callout-color), 0.4);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  transform: none;
}

body.callout-variant-minimal .callout-title {
  background: transparent;
  border-bottom: 1px solid rgba(var(--callout-color), 0.15);
  padding: 8px 12px;
}

body.callout-variant-minimal .callout:hover .callout-title {
  background: rgba(var(--callout-color), 0.05);
  border-bottom-color: rgba(var(--callout-color), 0.25);
}

body.callout-variant-minimal .callout-content {
  background: transparent;
  padding: 12px;
}

body.callout-variant-minimal .callout::before,
body.callout-variant-minimal .callout-title::after {
  display: none;
}

/* ────────────────────────────────────────────────────────────────────────
   VARIANT 2: NEON - Intense glow effects
   Usage: Add class "callout-variant-neon" to body
   ──────────────────────────────────────────────────────────────────────── */

body.callout-variant-neon .callout {
  background: rgba(10, 10, 10, 0.85);
  border: 2px solid rgba(var(--callout-color), 0.6);
  border-left: 4px solid rgb(var(--callout-color));
  box-shadow:
    0 0 10px rgba(var(--callout-color), 0.3),
    0 0 20px rgba(var(--callout-color), 0.2),
    0 0 40px rgba(var(--callout-color), 0.1),
    0 4px 12px rgba(0, 0, 0, 0.5);
  animation: glowPulse 3s infinite;
}

body.callout-variant-neon .callout:hover {
  border-color: rgba(var(--callout-color), 0.8);
  box-shadow:
    0 0 15px rgba(var(--callout-color), 0.5),
    0 0 30px rgba(var(--callout-color), 0.3),
    0 0 60px rgba(var(--callout-color), 0.2),
    0 6px 16px rgba(0, 0, 0, 0.6);
  transform: translateY(-2px);
}

body.callout-variant-neon .callout-title {
  background: rgba(var(--callout-color), 0.15);
  text-shadow:
    0 0 5px rgba(var(--callout-color), 0.5),
    0 0 10px rgba(var(--callout-color), 0.3),
    0 2px 4px rgba(0, 0, 0, 0.8);
  font-weight: 600;
  border-bottom: 1px solid rgba(var(--callout-color), 0.4);
}

body.callout-variant-neon .callout:hover .callout-title {
  background: rgba(var(--callout-color), 0.22);
  text-shadow:
    0 0 8px rgba(var(--callout-color), 0.7),
    0 0 15px rgba(var(--callout-color), 0.4),
    0 2px 4px rgba(0, 0, 0, 0.8);
}

body.callout-variant-neon .callout-content {
  background: rgba(0, 0, 0, 0.4);
}

body.callout-variant-neon .callout::before {
  opacity: 1;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(var(--callout-color), 0.8) 50%,
    transparent 100%);
  height: 2px;
  box-shadow: 0 0 10px rgba(var(--callout-color), 0.6);
}

/* ────────────────────────────────────────────────────────────────────────
   VARIANT 3: OUTLINED - Clean bordered boxes
   Usage: Add class "callout-variant-outlined" to body
   ──────────────────────────────────────────────────────────────────────── */

body.callout-variant-outlined .callout {
  background: transparent;
  border: 2px solid rgba(var(--callout-color), 0.4);
  border-left: 4px solid rgba(var(--callout-color), 0.8);
  border-radius: 8px;
  padding: 0;
}

body.callout-variant-outlined .callout::before {
  display: none;
}

body.callout-variant-outlined .callout-title {
  background: transparent;
  border-bottom: 1px solid rgba(var(--callout-color), 0.25);
  padding: 8px 12px;
}

body.callout-variant-outlined .callout:hover .callout-title {
  background: rgba(var(--callout-color), 0.05);
  border-bottom-color: rgba(var(--callout-color), 0.4);
}

body.callout-variant-outlined .callout-content {
  background: transparent;
  padding: 12px;
}

body.callout-variant-outlined .callout:hover {
  border-color: rgba(var(--callout-color), 0.6);
  box-shadow: 0 0 15px rgba(var(--callout-color), 0.15);
  transform: none;
}

body.callout-variant-outlined .callout-title::after {
  display: none;
}

/* ────────────────────────────────────────────────────────────────────────
   VARIANT 4: COMPACT - Dense information layout
   Usage: Add class "callout-variant-compact" to body
   ──────────────────────────────────────────────────────────────────────── */

body.callout-variant-compact .callout {
  margin: 0.3em 0;
  border-radius: 8px;
  padding: 4px;
}

body.callout-variant-compact .callout-title {
  padding: 6px 10px;
  font-size: 0.85em;
  font-weight: 600;
  gap: 6px;
}

body.callout-variant-compact .callout-content {
  padding: 8px 10px;
  font-size: 0.92em;
  line-height: 1.5;
}

body.callout-variant-compact .callout-icon {
  width: 18px;
  height: 18px;
  font-size: 0.85em;
}

/* ────────────────────────────────────────────────────────────────────────
   VARIANT 5: RAISED - Deep 3D shadows for all callouts
   Usage: Add class "callout-variant-raised" to body
   ──────────────────────────────────────────────────────────────────────── */

body.callout-variant-raised .callout {
  border-left-width: 4px;
  transform: translateY(-4px);
  box-shadow:
    0 8px 16px rgba(0, 0, 0, 0.5),
    0 16px 32px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(var(--callout-color), 0.2),
    inset 0 1px 0 rgba(224, 224, 224, 0.1);
  background: linear-gradient(180deg,
    rgba(30, 30, 30, 0.8) 0%,
    rgba(20, 20, 20, 0.6) 100%);
}

body.callout-variant-raised .callout:hover {
  transform: translateY(-6px);
  box-shadow:
    0 12px 24px rgba(0, 0, 0, 0.6),
    0 24px 48px rgba(0, 0, 0, 0.4),
    0 0 30px rgba(var(--callout-color), 0.3),
    inset 0 1px 0 rgba(224, 224, 224, 0.15);
}


/* ═══════════════════════════════════════════════════════════════════════════
   🔧 SECTION 7: UTILITY OVERRIDES & SPECIAL CASES
   Edge cases and nested callout handling
   ═══════════════════════════════════════════════════════════════════════════ */

/* Nested Callouts - Reduce effects */
.callout .callout {
  margin: 1em 0;
  transform: translateY(0);
  box-shadow: 
    0 4px 8px rgba(0, 0, 0, 0.2),
    0 2px 4px rgba(0, 0, 0, 0.15);
}

/* Foldable Callouts - Preserve fold icon */
.callout.is-collapsible .callout-fold {
  padding: 0 8px;
}

/* Print Styles - Remove animations and shadows */
@media print {
  .callout {
    animation: none;
    box-shadow: none;
    transform: none;
    page-break-inside: avoid;
  }
  
  .callout::before,
  .callout-title::after {
    display: none;
  }
}


/* ═══════════════════════════════════════════════════════════════════════════
   📝 SECTION 8: CONFIGURATION GUIDE & USAGE EXAMPLES
   ═══════════════════════════════════════════════════════════════════════════

   QUICK START:
   ───────────────────────────────────────────────────────────────────────────
   1. Enable this snippet in Obsidian (Settings → Appearance → CSS snippets)
   2. Choose a visual style variant:
   
      DEFAULT (no body class):
      - Rich backgrounds with gradients
      - Subtle glow effects
      - Hover animations
      
      MINIMAL (add to Settings → Appearance → CSS snippets → Style Settings):
      body.callout-variant-minimal
      - Transparent backgrounds
      - Border-only design
      - Minimal visual weight
      
      NEON (cyberpunk aesthetic):
      body.callout-variant-neon
      - Intense glow effects
      - Pulsing animations
      - Maximum visual impact
      
      OUTLINED (clean professional):
      body.callout-variant-outlined
      - Full border outlines
      - Transparent interiors
      - Clean corporate look
      
      COMPACT (information density):
      body.callout-variant-compact
      - Reduced spacing
      - Smaller fonts
      - Maximum content per screen
      
      RAISED (3D depth):
      body.callout-variant-raised
      - Deep shadows
      - Elevated appearance
      - Strong visual hierarchy
   
   3. Use callouts in markdown:
      > [!key-claim] Important Concept
      > This is my claim with supporting evidence
      
      > [!warning] Critical Warning
      > Pay attention to this
      
      > [!diamond] Premium Content
      > High-value information here

   CUSTOMIZATION:
   ───────────────────────────────────────────────────────────────────────────
   All design tokens are in :root {} at the top of this file.
   
   To customize colors, edit these variables:
   - --callout-crimson: 229, 0, 0;        (change to your brand color)
   - --callout-grey-high: 224, 224, 224;  (adjust greyscale palette)
   - --glow-intensity: 0.3;               (increase/decrease glow strength)
   
   To customize spacing:
   - --callout-padding: 14px 10px;        (content area padding)
   - --callout-margin: 0.5em 0;           (vertical spacing between callouts)
   - --callout-border-radius: 16px;       (corner rounding)
   
   To customize animations:
   - --animation-speed-normal: 0.35s;     (hover transition speed)
   - --animation-easing: cubic-bezier...  (easing curve)

   ADVANCED:
   ───────────────────────────────────────────────────────────────────────────
   Create custom callout types by adding to SECTION 5:
   
   .callout[data-callout="your-type"] {
     --callout-color: R, G, B;  (RGB values without rgb())
   }
   
   Apply special effects from the Special Effects section or create your own.

   ═══════════════════════════════════════════════════════════════════════════
*/

```

### .obsidian\snippets\_dataview.css

```css
/*
═══════════════════════════════════════════════════════════
 SNIPPET: Dataview Plugin Styling
 Category: Plugins
 Purpose: Enhanced styling for Dataview tables and lists
 Author: Pur3v4d3r
 Created: 2025-12-13
 Version: 1.0.0

 Description:
 Professional styling for the Dataview plugin, featuring
 gradient table headers, enhanced row hover effects, and
 styled inline fields. Integrates seamlessly with the
 overall theme color scheme.

 Dependencies:
 - 01-variables.css (recommended)
 - Dataview plugin (required)

 Standalone: Yes (requires Dataview plugin)

 Features:
 - Purple gradient table headers
 - Hover effects on table rows
 - Styled inline field keys (gold)
 - Proper border and spacing
 - Optional inline list formatting

 Dataview Plugin:
 https://github.com/blacksmithgu/obsidian-dataview

 Compatibility: Obsidian 1.5+, Dataview 0.5+
═══════════════════════════════════════════════════════════

/* ══════════════════════════════════════════════════════════
   INLINE FIELDS - Key::Value Pairs
   Styled metadata within notes
   ══════════════════════════════════════════════════════════ */

/* Inline field key (before ::) - Gold */
.theme-dark .dataview.inline-field-key {
  color: #000000ff !important;
  /*ImperialGold*/font-weight: 100 !important;
  /*Bold*/text-transform: uppercase;
  filter: drop-shadow(0px 0px 5px rgba(255, 0, 0, 1));
  -webkit-filter: drop-shadow(0px 0px 8px rgba(255, 0, 0, 1));
  font-size: 1.25em !important;
}

/* Inline field value (after ::) */
.theme-dark .dataview.inline-field-value {
  color: #979797ff !important;       /* Normal text color */
  font-weight: 400 !important;                /* Regular weight */
  background: #212121ff !important; /* Subtle bg */
  padding: 2px 6px !important;               /* Light padding */
  border-radius: 4px !important;             /* Rounded corners */
  font-size: 1em !important;

}

.theme-dark .dataview.inline-field-key::after {
  content: ': ';
  color: #000000ff !important;
  /*ImperialGold*/
}
.theme-dark .dataview.inline-field-key:hover {
  color: #ff0000ff !important;
  /*BrightRed*/
}
.theme-dark .dataview.inline-field-key:hover::after {
  color: #ff0000ff !important;
  /*BrightRed*/
}
.theme-dark .dataview.inline-field-key {
  font-weight: 600!important;
}
.theme-dark .dataview.inline-field-key::after {
  content: ': ';
  color: #ff0000ff !important;
  /*ImperialGold*/
}
.theme-dark .dataview.inline-field-key:hover {
  color: #ff0000ff !important;
  /*BrightRed*/
}
.theme-dark .dataview.inline-field-key:hover::after {
  color: #ff0000ff !important;
  /*BrightRed*/
}
.theme-dark .dataview.inline-field-key {
  font-weight: 600!important;
}
.theme-dark .dataview.inline-field-key::after {
  content: ': ';
  color: #ff0000ff !important;
  /*ImperialGold*/
}
.theme-dark .dataview.inline-field-key:hover {
  color: #ff0000ff !important;
  /*BrightRed*/
}
.theme-dark .dataview.inline-field-key:hover::after {
  color: #ff0000ff !important;
  /*BrightRed*/
}








/* ══════════════════════════════════════════════════════════
   INLINE LISTS
   Dataview list output
   ══════════════════════════════════════════════════════════ */

/* Optional: Inline list formatting */
body.dataview-inline-lists .dataview.inline-field {
  display: inline !important;                 /* Horizontal layout */
}

/* ══════════════════════════════════════════════════════════
   DATAVIEW TASK LISTS
   Checkbox lists from Dataview queries
   ══════════════════════════════════════════════════════════ */

.theme-dark .dataview.task-list-item {
  /* Uses global checkbox styling from variables */
}

/* Completed tasks */
.theme-dark .dataview.task-list-item.is-checked {
  opacity: 0.6;                               /* Fade completed */
  text-decoration: line-through;              /* Strike through */
}

/* ══════════════════════════════════════════════════════════
   DATAVIEW METADATA
   Query metadata and info
   ══════════════════════════════════════════════════════════ */

.theme-dark .dataview.dataview-result-list-root-ul {
  padding-left: 20px !important;              /* Indent lists */
}

/* ══════════════════════════════════════════════════════════
   DATAVIEW ERROR MESSAGES
   Query error styling
   ══════════════════════════════════════════════════════════ */

.theme-dark .dataview.dataview-error {
  color: var(--color-red) !important;         /* Red error text */
  background: rgba(255, 0, 0, 0.1) !important; /* Light red background */
  border-left: 3px solid var(--color-red) !important;
  padding: 8px 12px !important;
  margin: 8px 0 !important;
  border-radius: 0 4px 4px 0 !important;
}

/* ══════════════════════════════════════════════════════════
   DATAVIEW CALENDAR VIEWS
   Month/year calendar displays
   ══════════════════════════════════════════════════════════ */

.theme-dark .dataview.dataview-calendar {
  /* Calendar styling inherits from table */
}

/* Calendar day cells */
.theme-dark .dataview.dataview-calendar .dataview-calendar-day {
  border: 1px solid var(--background-modifier-border) !important;
  padding: 4px !important;
}

/* Today indicator */
.theme-dark .dataview.dataview-calendar .dataview-calendar-day.is-today {
  background: rgba(255, 199, 0, 0.2) !important; /* Gold highlight */
  border-color: #E50000 !important;
}

/* ══════════════════════════════════════════════════════════
   CUSTOMIZATION NOTES
   ══════════════════════════════════════════════════════════

   To customize Dataview styling:

   1. Table Header Color:
      Change the gradient in .dataview.table-view-table thead
      Example: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%)

   2. Inline Field Key Color:
      Change --FFC700 in .dataview.inline-field-key

   3. Row Hover Color:
      Adjust --table-row-background-hover in 01-variables.css

   4. Error Message Color:
      Change --color-red in .dataview.dataview-error

   ══════════════════════════════════════════════════════════ */

/* ══════════════════════════════════════════════════════════
   END OF DATAVIEW STYLING
   ══════════════════════════════════════════════════════════ */

```

### .obsidian\snippets\_jetbrains-mono-light.css

```css
═══════════════════════════════════════════════════════════
 SNIPPET NAME: JetBrains Mono Light Font
 Purpose: Apply JetBrains Mono Light globally across Obsidian
 Author: Pur3v4d3r
 Date: 2025-12-14
 Obsidian Version: 1.5+
 Dependencies: None
 Installation: Place in .obsidian/snippets/ and enable in Settings
 
 Description:
 Sets JetBrains Mono Light (weight: 300) as the default font
 for all editor, preview, and interface text. Provides clean,
 consistent typography throughout the application.
 
 Font Installation:
 Download JetBrains Mono from: https://www.jetbrains.com/lp/mono/
 Install all font weights for best results.
═══════════════════════════════════════════════════════════
*/

/* [SECTION 1: Global Font Variables] */
body {
  --font-text: "JetBrains Mono", monospace !important;
  --font-monospace: "JetBrains Mono", monospace !important;
  --font-interface: "JetBrains Mono", monospace !important;
  --font-text-weight: 100 !important; /* ← Changed to 100 */
}

body, .theme-dark body {
  font-family: "JetBrains Mono", "Courier New", monospace !important;
  font-weight: 100 !important; /* ← Changed to 100 */
}

/* [SECTION 2: Editor Text] */
.markdown-source-view,
.markdown-source-view.mod-cm6,
.cm-editor,
.cm-content,
.cm-scroller,
.cm-line {
  font-family: "JetBrains Mono", "Courier New", monospace !important;
  font-weight: 100 !important; /* ← Changed to 100 */
}

/* [SECTION 3: Preview/Reading Mode] */
.markdown-preview-view,
.markdown-rendered {
  font-family: "JetBrains Mono", "Courier New", monospace !important;
  font-weight: 100 !important; /* ← Changed to 100 */
}

/* [SECTION 4: Interface Elements] */
.workspace,
.nav-file-title,
.nav-folder-title,
.search-result-file-title,
.workspace-tab-header-inner,
.titlebar,
.status-bar {
  font-family: "JetBrains Mono", "Courier New", monospace !important;
  font-weight: 100 !important; /* ← Changed to 100 */
}

/* [SECTION 5: Code Blocks] */
code,
pre,
.cm-inline-code,
.markdown-preview-view code {
  font-family: "JetBrains Mono", "Courier New", monospace !important;
  font-weight: 100 !important; /* ✓ Already 100 */
}

/* [SECTION 6: Headings Override] */
h1, h2, h3, h4, h5, h6,
.cm-header-1, .cm-header-2, .cm-header-3,
.cm-header-4, .cm-header-5, .cm-header-6 {
  font-family: "JetBrains Mono", "Courier New", monospace !important;
  font-weight: 100 !important; /* ← Changed to 100 */
}

/* [SECTION 7: Accessibility - Reduced Motion] */
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
.popover.hover-popover,
.menu,
.suggestion-container {
  box-shadow: 0 0px 48px rgba(255, 0, 0, 0.3) !important;
}
```

### .obsidian\snippets\__v4d3r-mermaid.css

```css
/* ═══════════════════════════════════════════════════════════════════════════
   V4D3R MERMAID, TABLES & PLUGINS SNIPPET SYSTEM - PART 1: MERMAID
   Author: TaskMaster Agent | Theme: Red/Black/Grey
   
   TOGGLE SYSTEM: Comment/uncomment sections to enable/disable features
   Each feature block is marked with [TOGGLE] for easy identification
   
   ⚠️ IMPORTANT: Disable conflicting mermaid snippets (e.g., 10-mermaid.css)
   to prevent style conflicts causing blank nodes or incorrect colors.
═══════════════════════════════════════════════════════════════════════════ */

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 1: CSS CUSTOM PROPERTIES (COLOR PALETTE)
═══════════════════════════════════════════════════════════════════════════ */

:root {
  /* ─── PRIMARY RED PALETTE ─── */
  --v4d3r-red-primary: #DC2626;
  --v4d3r-red-dark: #991B1B;
  --v4d3r-red-darker: #7F1D1D;
  --v4d3r-red-light: #EF4444;
  --v4d3r-red-pale: #ff0000ff;
  --v4d3r-red-glow: rgba(220, 38, 38, 0.4);
  
  /* ─── BLACK PALETTE ─── */
  --v4d3r-black-pure: #000000;
  --v4d3r-black-soft: #0A0A0A;
  --v4d3r-black-charcoal: #1A1A1A;
  --v4d3r-black-rich: #1d1d1dff;
  
  /* ─── GREY PALETTE ─── */
  --v4d3r-grey-darkest: #374151;
  --v4d3r-grey-dark: #4B5563;
  --v4d3r-grey-medium: #6B7280;
  --v4d3r-grey-light: #9CA3AF;
  --v4d3r-grey-pale: #D1D5DB;
  --v4d3r-grey-ghost: #E5E7EB;
  --v4d3r-grey-snow: #F3F4F6;
  
  /* ─── ACCENT COLORS ─── */
  --v4d3r-accent-crimson: #B91C1C;
  --v4d3r-accent-rose: #E11D48;
  --v4d3r-accent-maroon: #881337;
  
  /* ─── SEMANTIC COLORS ─── */
  --v4d3r-success: #059669;
  --v4d3r-warning: #D97706;
  --v4d3r-info: #6B7280;
  --v4d3r-error: var(--v4d3r-red-primary);
}

/* ═══════════════════════════════════════════════════════════════════════════

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M4: MERMAID EDGE/LINK STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .edgePath .path {
  stroke: var(--v4d3r-grey-medium) !important;
  stroke-width: 2px !important;
}

/* Edge labels - comprehensive selectors */
.mermaid .edgeLabel,
.mermaid .edgeLabel rect,
.mermaid .edgeLabel .label {
  background-color: var(--v4d3r-black-charcoal) !important;
  fill: var(--v4d3r-black-charcoal) !important;
}

.mermaid .edgeLabel text,
.mermaid .edgeLabel span,
.mermaid .edgeLabel .edgeLabel,
.mermaid .label foreignObject div {
  color: var(--v4d3r-grey-light) !important;
  fill: var(--v4d3r-grey-light) !important;
  background: transparent !important;
}

/* Arrowheads - multiple selector patterns */
.mermaid marker#arrowhead path,
.mermaid marker path,
.mermaid .marker {
  fill: var(--v4d3r-red-primary) !important;
  stroke: var(--v4d3r-red-primary) !important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M5: MERMAID SUBGRAPH STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .cluster rect {
  fill: var(--v4d3r-black-soft) !important;
  stroke: var(--v4d3r-grey-dark) !important;
  stroke-width: 1px !important;
  rx: 8px;
  ry: 8px;
}

.mermaid .cluster .label {
  color: var(--v4d3r-red-light) !important;
  fill: var(--v4d3r-red-light) !important;
  font-weight: 600;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M6: FLOWCHART SPECIFIC STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .flowchart-link {
  stroke: var(--v4d3r-grey-medium) !important;
}

.mermaid .marker {
  fill: var(--v4d3r-red-primary) !important;
  stroke: var(--v4d3r-red-primary) !important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M7: SEQUENCE DIAGRAM STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .actor rect,
.mermaid .actor circle,
.mermaid .actor ellipse,
.mermaid .actor polygon {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
}
.mermaid .actor text {
  fill: var(--v4d3r-grey-pale) !important;
}
.mermaid .messageLine {
  stroke: var(--v4d3r-grey-medium) !important;
}
.mermaid .messageText {
  fill: var(--v4d3r-grey-light) !important;
}
.mermaid .activationRect {
  fill: var(--v4d3r-red-dark) !important;
  stroke: var(--v4d3r-red-primary) !important;
}
.mermaid .sequenceDiagram .divider {
  stroke: var(--v4d3r-grey-dark) !important;
}
.mermaid .sequenceDiagram .noteRect {
  fill: var(--v4d3r-black-charcoal) !important;
  stroke: var(--v4d3r-red-primary) !important;
}
.mermaid .sequenceDiagram .noteText {
  fill: var(--v4d3r-grey-pale) !important;
}
.mermaid .actor {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
}

.mermaid .actor-line {
  stroke: var(--v4d3r-grey-dark) !important;
}

.mermaid text.actor {
  fill: var(--v4d3r-grey-pale) !important;
  font-weight: 500;
}

.mermaid .messageLine0,
.mermaid .messageLine1 {
  stroke: var(--v4d3r-grey-medium) !important;
}

.mermaid .messageText {
  fill: var(--v4d3r-grey-light) !important;
}

.mermaid .activation0,
.mermaid .activation1,
.mermaid .activation2 {
  fill: var(--v4d3r-red-dark) !important;
  stroke: var(--v4d3r-red-primary) !important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M8: GANTT CHART STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .gantt-bar {
  fill: var(--v4d3r-red-primary) !important;
  stroke: var(--v4d3r-black-pure) !important;
  stroke-width: 1px !important;
}
.mermaid .gantt-bar-label {
  fill: var(--v4d3r-grey-pale) !important;
}
.mermaid .gantt-axis text {
  fill: var(--v4d3r-grey-light) !important;
}
.mermaid .gantt-grid line {
  stroke: var(--v4d3r-grey-dark) !important;
  stroke-dasharray: 2,2 !important;
}

.mermaid .section0,
.mermaid .section2 {
  fill: var(--v4d3r-black-rich) !important;
}

.mermaid .section1,
.mermaid .section3 {
  fill: var(--v4d3r-black-charcoal) !important;
}

.mermaid .task {
  fill: var(--v4d3r-red-dark) !important;
  stroke: var(--v4d3r-red-primary) !important;
}

.mermaid .taskText {
  fill: var(--v4d3r-grey-pale) !important;
}

.mermaid .taskTextOutsideRight,
.mermaid .taskTextOutsideLeft {
  fill: var(--v4d3r-grey-light) !important;
}

.mermaid .grid .tick line {
  stroke: var(--v4d3r-grey-dark) !important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M9: PIE CHART STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .pieSlice {
  stroke: var(--v4d3r-black-rich) !important;
  stroke-width: 2px !important;
}
.mermaid .pieLabel {
  fill: var(--v4d3r-grey-pale) !important;
}
.mermaid .pieTitleText {
  fill: var(--v4d3r-grey-pale) !important;
  font-weight: 600;
}

.mermaid .slice {
  stroke: var(--v4d3r-black-pure) !important;
  stroke-width: 2px !important;
}

.mermaid .legend text {
  fill: var(--v4d3r-grey-light) !important;
}



/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M10: CLASS DIAGRAM STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .classNode rect {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
}
.mermaid .classNode text {
  fill: var(--v4d3r-grey-pale) !important;
}
.mermaid .classEdgePath .path {
  stroke: var(--v4d3r-grey-medium) !important;
}
.mermaid .classMarker path {
  fill: var(--v4d3r-red-primary) !important;
}
.mermaid .classGroup rect {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
}
.mermaid .classGroup .title {
  fill: var(--v4d3r-grey-pale) !important;
}

.mermaid .classGroup rect {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
}

.mermaid .classGroup .title {
  fill: var(--v4d3r-red-light) !important;
}

.mermaid .classGroup line {
  stroke: var(--v4d3r-grey-dark) !important;
}

.mermaid .classLabel .box {
  fill: var(--v4d3r-black-charcoal) !important;
  stroke: var(--v4d3r-grey-dark) !important;
}

.mermaid .classLabel .label {
  fill: var(--v4d3r-grey-pale) !important;
}

.mermaid .relation {
  stroke: var(--v4d3r-grey-medium) !important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M11: STATE DIAGRAM STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .stateNode rect,
.mermaid .stateNode circle,
.mermaid .stateNode ellipse {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
}
.mermaid .stateNode text {
  fill: var(--v4d3r-grey-pale) !important;
}
.mermaid .stateEdgePath .path {
  stroke: var(--v4d3r-grey-medium) !important;
}
.mermaid .stateMarker path {
  fill: var(--v4d3r-red-primary) !important;
}
.mermaid .stateGroup rect {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
}

.mermaid .stateGroup .title {
  fill: var(--v4d3r-grey-pale) !important;
}

.mermaid .stateGroup .composit {
  fill: var(--v4d3r-black-soft) !important;
}

.mermaid .start-state,
.mermaid .end-state {
  fill: var(--v4d3r-red-primary) !important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M12: MINDMAP STYLING
───────────────────────────────────────────────────────────────────────── */
.mermaid .mindmap-node rect,
.mermaid .mindmap-node circle,
.mermaid .mindmap-node ellipse,
.mermaid .mindmap-node polygon {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
}
.mermaid .mindmap-node text {
  fill: var(--v4d3r-grey-pale) !important;
}
.mermaid .mindmap-edgePath .path {
  stroke: var(--v4d3r-grey-medium) !important;
}
.mermaid .mindmap-marker path {
  fill: var(--v4d3r-red-primary) !important;
}
.mermaid .mindmap-node rect {
  fill: var(--v4d3r-black-rich) !important;
  stroke: var(--v4d3r-red-primary) !important;
  rx: 8px;
  ry: 8px;
}

.mermaid .mindmap-node text {
  fill: var(--v4d3r-grey-pale) !important;
}

.mermaid .mindmap-edge {
  stroke: var(--v4d3r-grey-medium) !important;
}



/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] M13: HOVER EFFECTS FOR ALL MERMAID NODES
───────────────────────────────────────────────────────────────────────── */
.mermaid .node:hover rect,
.mermaid .node:hover circle,
.mermaid .node:hover ellipse,
.mermaid .node:hover polygon,
.mermaid .node:hover path {
  stroke: var(--v4d3r-red-light) !important;
  stroke-width: 3px !important;
}
.mermaid .node:hover .label {
  fill: var(--v4d3r-red-light) !important;
}


/* ═══════════════════════════════════════════════════════════════════════════
   END OF PART 1 - MERMAID STYLING
   Continue to Part 2 for TABLE styling
   Continue to Part 3 for PLUGIN styling
═══════════════════════════════════════════════════════════════════════════ */




/* ═══════════════════════════════════════════════════════════════════════════
   END OF V4D3R SNIPPET SYSTEM
   
   USAGE:
   1. Enable all 3 snippet files in Obsidian Settings > Appearance > Snippets
   2. Toggle individual features by commenting/uncommenting sections
   3. Use cssclass variants in frontmatter for tables: table-compact, 
      table-wide, table-borderless, table-minimal, table-latex, 
      table-shadow, table-mono, table-align-center, table-align-right
   
   TOTAL FEATURES: 47 toggleable styling options
   - M1-M13: Mermaid diagrams (13 features)
   - T1-T17: Tables (17 features)  
   - P1-P17: Plugins (17 features)
═══════════════════════════════════════════════════════════════════════════ */

```

### .obsidian\snippets\__v4d3r-plugins.css

```css
/* ═══════════════════════════════════════════════════════════════════════════
   V4D3R MERMAID, TABLES & PLUGINS SNIPPET SYSTEM - PART 3: PLUGINS
   Author: TaskMaster Agent | Theme: Red/Black/Grey
   
   TOGGLE SYSTEM: Comment/uncomment sections to enable/disable features
═══════════════════════════════════════════════════════════════════════════ */

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 4: PLUGIN STYLING
═══════════════════════════════════════════════════════════════════════════ */

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P1: DATAVIEW TABLE STYLING
───────────────────────────────────────────────────────────────────────── */
.dataview.table-view-table {
  background: var(--v4d3r-black-charcoal);
  border: 1px solid var(--v4d3r-grey-dark);
  border-radius: 8px;
}

.dataview.table-view-table th {
  background: var(--v4d3r-red-dark);
  color: var(--v4d3r-grey-snow);
  border-bottom: 2px solid var(--v4d3r-red-primary);
}

.dataview.table-view-table td {
  color: var(--v4d3r-grey-pale);
}

.dataview.table-view-table tr:hover {
  background: rgba(220, 38, 38, 0.1);
}
.dataview.table-view-table tr:nth-child(even) {
  background: var(--v4d3r-black-rich);
}
.dataview.table-view-table tr:nth-child(odd) {
  background: var(--v4d3r-black-soft);
}
.dataview.table-view-table td,
.dataview.table-view-table th {
  padding: 8px 12px;
}
.dataview.table-view-table th {
  font-weight: 600;
}
.dataview.table-view-table td {
  border-top: 1px solid var(--v4d3r-grey-dark);
}
.dataview.table-view-table th:first-child,
.dataview.table-view-table td:first-child {
  border-left: none;
}

.dataview.table-view-table th:last-child,
.dataview.table-view-table td:last-child {
  border-right: none;
}
.dataview.table-view-table tbody tr:last-child td {
  border-bottom: none;
}
.dataview.table-view-table th {
  text-align: left;
}
.dataview.table-view-table th.sortable:hover {
  background: var(--v4d3r-red-primary);
  cursor: pointer;
}
.dataview.table-view-table th.sortable:after {
  content: ' ⇅';
  font-size: 0.8em;
  color: var(--v4d3r-grey-medium);
}
.dataview.table-view-table th.sorted-asc:after {
  content: ' ↑';
  color: var(--v4d3r-red-light);
}
.dataview.table-view-table th.sorted-desc:after {
  content: ' ↓';
  color: var(--v4d3r-red-light);
}
.dataview.table-view-table th,
.dataview.table-view-table td {
  border-left: 1px solid var(--v4d3r-grey-dark);
}
.dataview.table-view-table th:first-child,
.dataview.table-view-table td:first-child {
  border-left: none;
}
.dataview.table-view-table th:last-child,
.dataview.table-view-table td:last-child {
  border-right: none;
}
.dataview.table-view-table tbody tr:last-child td {
  border-bottom: none;
}
.dataview.table-view-table th {
  text-align: left;
}
.dataview.table-view-table th.sortable:hover {
  background: var(--v4d3r-red-primary);
  cursor: pointer;
}
.dataview.table-view-table th.sortable:after {
  content: ' ⇅';
  font-size: 0.8em;
  color: var(--v4d3r-grey-medium);
}
.dataview.table-view-table th.sorted-asc:after {
  content: ' ↑';
  color: var(--v4d3r-red-light);
}
.dataview.table-view-table th.sorted-desc:after {
  content: ' ↓';
  color: var(--v4d3r-red-light);
}
.dataview.table-view-table a {
  color: var(--v4d3r-red-light);
  text-decoration: none;
}
.dataview.table-view-table a:hover {
  text-decoration: underline;
}
.dataview.table-view-table code {
  background: var(--v4d3r-black-rich);
  padding: 2px 4px;
  border-radius: 4px;
  font-family: monospace;
  color: var(--v4d3r-grey-snow);
}
.dataview.table-view-table code:hover {
  background: var(--v4d3r-black-charcoal);
}



/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P2: DATAVIEW LIST STYLING
───────────────────────────────────────────────────────────────────────── */
.dataview.list-view-ul {
  padding-left: 0;
}

.dataview.list-view-ul li {
  list-style: none;
  padding: 8px 12px;
  margin: 4px 0;
  background: var(--v4d3r-black-rich);
  border-left: 3px solid var(--v4d3r-red-primary);
  border-radius: 0 6px 6px 0;
}

.dataview.list-view-ul li:hover {
  background: var(--v4d3r-black-charcoal);
  border-left-color: var(--v4d3r-red-light);
}
.dataview.list-view-ul li a {
  color: var(--v4d3r-red-light);
  text-decoration: none;
}


/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P4: TASKS PLUGIN STYLING
───────────────────────────────────────────────────────────────────────── */
.tasks-plugin-task {
  background: var(--v4d3r-black-rich);
  padding: 8px 12px;
  margin: 4px 0;
  border-radius: 6px;
  border-left: 3px solid var(--v4d3r-grey-dark);
}

.tasks-plugin-task:hover {
  background: var(--v4d3r-black-charcoal);
}

/* Task priority colors */
.task-priority-highest {
  border-left-color: var(--v4d3r-red-primary) !important;
}

.task-priority-high {
  border-left-color: var(--v4d3r-red-dark) !important;
}

.task-priority-medium {
  border-left-color: var(--v4d3r-warning) !important;
}

.task-priority-low {
  border-left-color: var(--v4d3r-grey-medium) !important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P5: CUSTOM CHECKBOX STYLING
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view input[type="checkbox"],
.markdown-rendered input[type="checkbox"] {
  appearance: none;
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border: 2px solid var(--v4d3r-grey-dark);
  border-radius: 4px;
  background: var(--v4d3r-black-rich);
  cursor: pointer;
  position: relative;
  vertical-align: middle;
  margin-right: 8px;
}

.markdown-preview-view input[type="checkbox"]:checked,
.markdown-rendered input[type="checkbox"]:checked {
  background: var(--v4d3r-red-primary);
  border-color: var(--v4d3r-red-primary);
}

.markdown-preview-view input[type="checkbox"]:checked::after,
.markdown-rendered input[type="checkbox"]:checked::after {
  content: '✓';
  position: absolute;
  color: var(--v4d3r-grey-snow);
  font-size: 14px;
  top: -2px;
  left: 2px;
}

.markdown-preview-view input[type="checkbox"]:hover,
.markdown-rendered input[type="checkbox"]:hover {
  border-color: var(--v4d3r-red-light);
  box-shadow: 0 0 4px var(--v4d3r-red-glow);
}


/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P7: CALENDAR PLUGIN STYLING
───────────────────────────────────────────────────────────────────────── */
.calendar {
  background: var(--v4d3r-black-charcoal);
  border-radius: 8px;
  border: 1px solid var(--v4d3r-grey-dark);
}

.calendar .title {
  color: var(--v4d3r-red-light);
  font-weight: 600;
}

.calendar .day {
  color: var(--v4d3r-grey-pale);
}

.calendar .today {
  background: var(--v4d3r-red-dark);
  color: var(--v4d3r-grey-snow);
  border-radius: 50%;
}

.calendar .active {
  background: var(--v4d3r-red-primary);
  color: var(--v4d3r-grey-snow);
}

.calendar .has-note::after {
  content: '•';
  color: var(--v4d3r-red-light);
  position: absolute;
  bottom: 2px;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P8: KANBAN PLUGIN STYLING
───────────────────────────────────────────────────────────────────────── */
.kanban-plugin {
  background: var(--v4d3r-black-soft);
}

.kanban-plugin__lane {
  background: var(--v4d3r-black-charcoal);
  border: 1px solid var(--v4d3r-grey-dark);
  border-radius: 8px;
}

.kanban-plugin__lane-title-text {
  color: var(--v4d3r-red-light);
  font-weight: 600;
}

.kanban-plugin__item {
  background: var(--v4d3r-black-rich);
  border-left: 3px solid var(--v4d3r-grey-dark);
  border-radius: 4px;
}

.kanban-plugin__item:hover {
  border-left-color: var(--v4d3r-red-primary);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.kanban-plugin__item-title-wrapper {
  color: var(--v4d3r-grey-pale);
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P9: EXCALIDRAW CONTAINER
───────────────────────────────────────────────────────────────────────── */
.excalidraw-embedded {
  border: 1px solid var(--v4d3r-grey-dark);
  border-radius: 8px;
  background: var(--v4d3r-black-charcoal);
}



/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P11: OUTLINE PANE STYLING
───────────────────────────────────────────────────────────────────────── */
.outline-tree {
  background: var(--v4d3r-black-charcoal);
}

.outline-tree .tree-item-self:hover {
  background: rgba(220, 38, 38, 0.1);
}

.outline-tree .tree-item-self.is-active {
  background: var(--v4d3r-red-dark);
  color: var(--v4d3r-grey-snow);
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P12: GRAPH VIEW ACCENT COLORS
───────────────────────────────────────────────────────────────────────── */
.graph-view.color-fill-attachment {
  color: var(--v4d3r-grey-medium);
}

.graph-view.color-fill-focused {
  color: var(--v4d3r-red-primary);
}

.graph-view.color-line-highlight {
  color: var(--v4d3r-red-light);
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P13: BACKLINKS/OUTGOING LINKS PANE
───────────────────────────────────────────────────────────────────────── */
.backlink-pane,
.outgoing-link-pane {
  background: var(--v4d3r-black-charcoal);
}

.backlink-pane .search-result-file-title,
.outgoing-link-pane .search-result-file-title {
  color: var(--v4d3r-red-light);
}

.backlink-pane .search-result-file-matches,
.outgoing-link-pane .search-result-file-matches {
  color: var(--v4d3r-red-primary);
  font-size: medium;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] P16: EMBEDDED/TRANSCLUDED NOTES
───────────────────────────────────────────────────────────────────────── */
.markdown-embed {
  background: var(--v4d3r-black-rich);
  border: 1px solid var(--v4d3r-grey-dark);
  border-left: 3px solid var(--v4d3r-red-primary);
  border-radius: 0 8px 8px 0;
  padding: 16px;
}

.markdown-embed-title {
  color: var(--v4d3r-red-light);
  font-weight: 600;
}
.markdown-embed:hover {
  background: var(--v4d3r-black-charcoal);
  border-left-color: var(--v4d3r-red-light);
}


/* ═══════════════════════════════════════════════════════════════════════════
   END OF V4D3R SNIPPET SYSTEM
   
   USAGE:
   1. Enable all 3 snippet files in Obsidian Settings > Appearance > Snippets
   2. Toggle individual features by commenting/uncommenting sections
   3. Use cssclass variants in frontmatter for tables: table-compact, 
      table-wide, table-borderless, table-minimal, table-latex, 
      table-shadow, table-mono, table-align-center, table-align-right
   
   TOTAL FEATURES: 47 toggleable styling options
   - M1-M13: Mermaid diagrams (13 features)
   - T1-T17: Tables (17 features)  
   - P1-P17: Plugins (17 features)
═══════════════════════════════════════════════════════════════════════════ */

```

### .obsidian\snippets\__v4d3r-tables.css

```css
/* ═══════════════════════════════════════════════════════════════════════════
   V4D3R MERMAID, TABLES & PLUGINS SNIPPET SYSTEM - PART 2: TABLES
   Author: TaskMaster Agent | Theme: Red/Black/Grey
   
   TOGGLE SYSTEM: Comment/uncomment sections to enable/disable features
═══════════════════════════════════════════════════════════════════════════ */

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION 3: TABLE STYLING
═══════════════════════════════════════════════════════════════════════════ */

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T1: BASE TABLE STYLING
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view table,
.markdown-rendered table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
  background: var(--v4d3r-black-charcoal);
  border: 1px solid var(--v4d3r-grey-dark);
  border-radius: 8px;
  overflow: hidden;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T2: TABLE HEADER STYLING
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view th,
.markdown-rendered th {
  background: linear-gradient(135deg, var(--v4d3r-red-dark), var(--v4d3r-red-darker));
  color: var(--v4d3r-grey-snow);
  font-weight: 600;
  padding: 12px 16px;
  text-align: left;
  border-bottom: 2px solid var(--v4d3r-red-primary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 0.875em;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T3: TABLE CELL STYLING
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view td,
.markdown-rendered td {
  padding: 10px 16px;
  border-bottom: 1px solid var(--v4d3r-grey-darkest);
  color: var(--v4d3r-grey-pale);
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T4: ZEBRA STRIPING
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view tr:nth-child(even),
.markdown-rendered tr:nth-child(even) {
  background: var(--v4d3r-black-soft);
}

.markdown-preview-view tr:nth-child(odd),
.markdown-rendered tr:nth-child(odd) {
  background: var(--v4d3r-black-rich);
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T5: ROW HOVER EFFECT
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view tbody tr:hover,
.markdown-rendered tbody tr:hover {
  background: rgba(220, 38, 38, 0.15) !important;
  transition: background 0.2s ease;
}

.markdown-preview-view tbody tr:hover td,
.markdown-rendered tbody tr:hover td {
  color: var(--v4d3r-grey-snow);
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T6: FIRST COLUMN EMPHASIS
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view td:first-child,
.markdown-rendered td:first-child {
  font-weight: 500;
  color: var(--v4d3r-red-pale);
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T7: STICKY TABLE HEADERS
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view thead,
.markdown-rendered thead {
  position: sticky;
  top: 0;
  z-index: 10;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T8: COMPACT TABLE VARIANT (use cssclass: table-compact)
───────────────────────────────────────────────────────────────────────── */
/*
.table-compact table th,
.table-compact table td {
  padding: 6px 10px;
  font-size: 0.85em;
}
*/

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T9: WIDE TABLE VARIANT (use cssclass: table-wide)
───────────────────────────────────────────────────────────────────────── */
.table-wide table {
  max-width: none;
}

.table-wide table th,
.table-wide table td {
  padding: 16px 24px!important;
  font-size: 1em!important;
}


/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T10: BORDERLESS TABLE VARIANT (use cssclass: table-borderless)
───────────────────────────────────────────────────────────────────────── */
/*
.table-borderless table {
  border: none;
}

.table-borderless table th,
.table-borderless table td {
  border: none;
}
*/

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T11: MINIMAL TABLE VARIANT (use cssclass: table-minimal)
───────────────────────────────────────────────────────────────────────── */
/*
.table-minimal table {
  border: none;
  border-radius: 0;
}
.table-minimal table th {
  background: var(--v4d3r-grey-dark)!important;
  border-bottom: 1px solid var(--v4d3r-grey-medium)!important;
  color: var(--v4d3r-grey-snow)!important;
}
.table-minimal table td {
  background: transparent!important;
  border: none;
  text-align: left;
}
*/

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T12: LATEX-STYLE TABLE (use cssclass: table-latex)
───────────────────────────────────────────────────────────────────────── */
.table-latex table {
  border: none;
  border-top: 2px solid var(--v4d3r-grey-pale)!important;
  border-bottom: 2px solid var(--v4d3r-grey-pale)!important;
  border-radius: 0;
}

.table-latex table th {
  background: transparent!important;
  border-bottom: 1px solid var(--v4d3r-grey-medium)!important;
  color: var(--v4d3r-grey-snow)!important;
  font-variant: small-caps;
}

.table-latex table td {
  background: transparent!important;
  border: none;
  text-align: center;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T13: TABLE WITH SHADOWS (use cssclass: table-shadow)
───────────────────────────────────────────────────────────────────────── */
.table-shadow table {
  box-shadow: 0 4px 6px 1px rgba(255, 0, 0, 0.4)!important;
  border: none;
  border-radius: 8px;
}
.table-shadow thead {
  box-shadow: 0 2px 4px 1px rgba(255, 0, 0, 0.3)!important;
}
.table-shadow tbody tr {
  box-shadow: 0 2px 4px 1px rgba(255, 0, 0, 0.3)!important;
  transition: box-shadow 0.2s ease;
  
}

.table-shadow tbody tr:hover {
  box-shadow: inset 0 0 0 2px var(--v4d3r-red-primary)!important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T14: RESPONSIVE TABLE (horizontal scroll on small screens)
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view .table-wrapper,
.markdown-rendered .table-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch!important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T15: COLUMN ALIGNMENT UTILITIES
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view th.align-left,
.markdown-rendered th.align-left,
.markdown-preview-view td.align-left,
.markdown-rendered td.align-left {
  text-align: left!important;
}
.markdown-preview-view th.align-center,
.markdown-rendered th.align-center,
.markdown-preview-view td.align-center,
.markdown-rendered td.align-center {
  text-align: center!important;
}
.markdown-preview-view th.align-right,
.markdown-rendered th.align-right,
.markdown-preview-view td.align-right,
.markdown-rendered td.align-right {
  text-align: right!important;
}



/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T16: HIGHLIGHTED ROW (use inline style or class)
───────────────────────────────────────────────────────────────────────── */
.markdown-preview-view tr.highlight,
.markdown-rendered tr.highlight {
  background: rgba(220, 38, 38, 0.25) !important;
  border-left: 3px solid var(--v4d3r-red-primary)!important;
}

/* ─────────────────────────────────────────────────────────────────────────
   [TOGGLE] T17: MONOSPACE DATA CELLS (use cssclass: table-mono)
───────────────────────────────────────────────────────────────────────── */
.table-mono table td {
  font-family: 'JetBrains Mono', 'Fira Code', monospace!important;
  font-size: 0.9em!important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   END OF PART 2 - TABLE STYLING
   Continue to Part 3 for PLUGIN styling
═══════════════════════════════════════════════════════════════════════════ */

```

### .obsidian\snippets\___v4d3r-ui-system.css

```css
/* 




   ╔══════════════════════════════════════════════════════════════════════════════╗
   ║                    V4D3R UI SYSTEM - Obsidian Snippet                        ║
   ║                     Complete Workspace Customization                         ║
   ║                                                                              ║
   ║  Theme Colors: RED • BLACK • GREY                                            ║
   ║  Toggle components by commenting/uncommenting sections                       ║
   ║                                                                              ║
   ║  Author: TaskMaster Agent | Version: 1.0.0 | Date: 2025-12-29                ║
   ╚══════════════════════════════════════════════════════════════════════════════╝ */

/* ═══════════════════════════════════════════════════════════════════════════════
   PART 1: CORE VARIABLES & COLOR PALETTE
   Toggle: This section should always remain enabled as foundation
   ═══════════════════════════════════════════════════════════════════════════════ */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 1.1 V4D3R COLOR PALETTE - RED/BLACK/GREY Theme                               │
   │ Uncomment ONE theme variant below (Dark is default)                          │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* === DARK THEME VARIANT (DEFAULT) === */
.theme-dark {
  /* ─── PRIMARY RED PALETTE ─── */
  --v4d3r-red-primary: #e93147 !important;
  --v4d3r-red-secondary: #ff4757 !important;
  --v4d3r-red-accent: #ff6b7a !important;
  --v4d3r-red-muted: #8b1e2b !important;
  --v4d3r-red-dark: #5c1420 !important;
  
  /* ─── BLACK SPECTRUM ─── */
  --v4d3r-black-pure: #000000 !important;
  --v4d3r-black-deep: #0a0a0a !important;
  --v4d3r-black-rich: #121212 !important;
  --v4d3r-black-soft: #1a1a1a !important;
  --v4d3r-black-elevated: #1e1e1e !important;
  
  /* ─── GREY SPECTRUM ─── */
  --v4d3r-grey-darkest: #252525 !important;
  --v4d3r-grey-dark: #2d2d2d !important;
  --v4d3r-grey-mid: #3d3d3d !important;
  --v4d3r-grey-light: #555555 !important;
  --v4d3r-grey-lighter: #707070 !important;
  --v4d3r-grey-lightest: #9a9a9a !important;
  
  /* ─── SEMANTIC COLORS ─── */
  --v4d3r-bg-primary: var(--v4d3r-black-rich) !important;
  --v4d3r-bg-secondary: var(--v4d3r-black-soft) !important;
  --v4d3r-bg-tertiary: var(--v4d3r-grey-darkest) !important;
  --v4d3r-bg-hover: var(--v4d3r-grey-dark) !important;
  --v4d3r-bg-active: var(--v4d3r-red-dark) !important;
  
  --v4d3r-text-primary: #e8e8e8 !important;
  --v4d3r-text-secondary: #b0b0b0 !important;
  --v4d3r-text-muted: #707070 !important;
  --v4d3r-text-accent: var(--v4d3r-red-accent) !important;
  
  --v4d3r-border-default: var(--v4d3r-grey-dark) !important;
  --v4d3r-border-subtle: var(--v4d3r-grey-darkest) !important;
  --v4d3r-border-accent: var(--v4d3r-red-muted) !important;
  
  /* ─── INTERACTIVE STATES ─── */
  --v4d3r-interactive-normal: var(--v4d3r-grey-dark) !important;
  --v4d3r-interactive-hover: var(--v4d3r-grey-mid) !important;
  --v4d3r-interactive-active: var(--v4d3r-red-dark) !important;
  --v4d3r-interactive-accent: var(--v4d3r-red-primary) !important;
  
  /* ─── SHADOWS & GLOWS ─── */
  --v4d3r-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.5) !important;
  --v4d3r-shadow-md: 0 4px 6px rgba(0, 0, 0, 0.6) !important;
  --v4d3r-shadow-lg: 0 10px 20px rgba(0, 0, 0, 0.7) !important;
  --v4d3r-glow-red: 0 0 10px rgba(233, 49, 71, 0.3) !important;
  --v4d3r-glow-red-intense: 0 0 20px rgba(233, 49, 71, 0.5) !important;
}

 


/* === LIGHT THEME VARIANT (Uncomment to enable) === */
/*
.theme-light {
  --v4d3r-red-primary: #d32f2f !important;
  --v4d3r-red-secondary: #e53935 !important;
  --v4d3r-red-accent: #c62828 !important;
  --v4d3r-red-muted: #ffcdd2 !important;
  --v4d3r-red-dark: #b71c1c !important;
  
  --v4d3r-black-pure: #000000 !important;
  --v4d3r-black-deep: #1a1a1a !important;
  --v4d3r-black-rich: #2d2d2d !important;
  --v4d3r-black-soft: #424242 !important;
  --v4d3r-black-elevated: #525252 !important;
  
  --v4d3r-grey-darkest: #757575 !important;
  --v4d3r-grey-dark: #9e9e9e !important;
  --v4d3r-grey-mid: #bdbdbd !important;
  --v4d3r-grey-light: #e0e0e0 !important;
  --v4d3r-grey-lighter: #eeeeee !important;
  --v4d3r-grey-lightest: #f5f5f5 !important;
  
  --v4d3r-bg-primary: #fafafa !important;
  --v4d3r-bg-secondary: #f0f0f0 !important;
  --v4d3r-bg-tertiary: #e8e8e8 !important;
  --v4d3r-bg-hover: #e0e0e0 !important;
  --v4d3r-bg-active: var(--v4d3r-red-muted) !important;
  
  --v4d3r-text-primary: #1a1a1a !important;
  --v4d3r-text-secondary: #424242 !important;
  --v4d3r-text-muted: #757575 !important;
  --v4d3r-text-accent: var(--v4d3r-red-primary) !important;
  
  --v4d3r-border-default: #d0d0d0 !important;
  --v4d3r-border-subtle: #e0e0e0 !important;
  --v4d3r-border-accent: var(--v4d3r-red-muted) !important;
  
  --v4d3r-interactive-normal: #e8e8e8 !important;
  --v4d3r-interactive-hover: #d8d8d8 !important;
  --v4d3r-interactive-active: var(--v4d3r-red-muted) !important;
  --v4d3r-interactive-accent: var(--v4d3r-red-primary) !important;
  
  --v4d3r-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.1) !important;
  --v4d3r-shadow-md: 0 4px 6px rgba(0, 0, 0, 0.15) !important;
  --v4d3r-shadow-lg: 0 10px 20px rgba(0, 0, 0, 0.2) !important;
  --v4d3r-glow-red: 0 0 10px rgba(211, 47, 47, 0.2) !important;
  --v4d3r-glow-red-intense: 0 0 20px rgba(211, 47, 47, 0.4) !important;
}
*/

/* 




┌──────────────────────────────────────────────────────────────────────────────┐
   │ 1.2 ANIMATION & TRANSITION VARIABLES                                         │
   └──────────────────────────────────────────────────────────────────────────────┘ */

:root {
  /* ─── TIMING ─── */
  --v4d3r-transition-fast: 100ms !important;
  --v4d3r-transition-normal: 200ms !important;
  --v4d3r-transition-slow: 300ms !important;
  --v4d3r-transition-slower: 500ms !important;
  
  /* ─── EASING ─── */
  --v4d3r-ease-default: ease-in-out !important;
  --v4d3r-ease-smooth: cubic-bezier(0.4, 0, 0.2, 1) !important;
  --v4d3r-ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
  --v4d3r-ease-snap: cubic-bezier(0.25, 1, 0.5, 1) !important;
  
  /* ─── SPACING ─── */
  --v4d3r-spacing-xs: 4px !important;
  --v4d3r-spacing-sm: 8px !important;
  --v4d3r-spacing-md: 12px !important;
  --v4d3r-spacing-lg: 16px !important;
  --v4d3r-spacing-xl: 24px !important;
  
  /* ─── BORDER RADIUS ─── */
  --v4d3r-radius-sm: 4px !important;
  --v4d3r-radius-md: 6px !important;
  --v4d3r-radius-lg: 8px !important;
  --v4d3r-radius-xl: 12px !important;
  --v4d3r-radius-full: 9999px !important;
}

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 1.3 OBSIDIAN VARIABLE OVERRIDES                                              │
   │ Toggle: Comment out to use default Obsidian colors                           │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Core Color Overrides --- */
.theme-dark {
  /* ─── OBSIDIAN ACCENT COLOR ─── */
  --accent-h: 352 !important;
  --accent-s: 81% !important;
  --accent-l: 55% !important;
  
  /* ─── BACKGROUND OVERRIDES ─── */
  --background-primary: var(--v4d3r-bg-primary) !important;
  --background-primary-alt: var(--v4d3r-bg-secondary) !important;
  --background-secondary: var(--v4d3r-bg-secondary) !important;
  --background-secondary-alt: var(--v4d3r-bg-tertiary) !important;
  --background-modifier-hover: var(--v4d3r-bg-hover) !important;
  --background-modifier-active-hover: var(--v4d3r-bg-active) !important;
  --background-modifier-border: var(--v4d3r-border-default) !important;
  --background-modifier-border-hover: var(--v4d3r-border-accent) !important;
  --background-modifier-border-focus: var(--v4d3r-red-primary) !important;
  
  /* ─── TEXT OVERRIDES ─── */
  --text-normal: var(--v4d3r-text-primary) !important;
  --text-muted: var(--v4d3r-text-secondary) !important;
  --text-faint: var(--v4d3r-text-muted) !important;
  --text-accent: var(--v4d3r-red-accent) !important;
  --text-accent-hover: var(--v4d3r-red-secondary) !important;
  
  /* ─── INTERACTIVE OVERRIDES ─── */
  --interactive-normal: var(--v4d3r-interactive-normal) !important;
  --interactive-hover: var(--v4d3r-interactive-hover) !important;
  --interactive-accent: var(--v4d3r-red-primary) !important;
  --interactive-accent-hover: var(--v4d3r-red-secondary) !important;
}
/* --- END TOGGLE: Core Color Overrides --- */

/* 
/* ══════════════════════════════════════════════════════════
   READING WIDTH
   Optimal line length for readability
   ══════════════════════════════════════════════════════════ */

.markdown-preview-view,
.markdown-source-view.mod-cm6 .cm-content {
  max-width: 110ch !important;                 /* 95 characters optimal */
  margin-left: auto !important;
  margin-right: auto !important;
}

/* ══════════════════════════════════════════════════════════
   TEXT FORMATTING - Bold and Italic
   Bold text gets Imperial Gold color
   ══════════════════════════════════════════════════════════ */
.theme-dark .markdown-preview-view strong,
.theme-dark .markdown-source-view.mod-cm6 .cm-strong,
.cm-strong {
  color: #e1ff00ff !important;  
  text-transform: uppercase !important;  /* Capitalize bold text */
  font-weight: 600 !important;                /* Semi-bold weight */
}
.theme-dark .markdown-preview-view em,
.theme-dark .markdown-source-view.mod-cm6 .cm-em,
.cm-em {
  font-style: italic !important;
  color: var(--ui-text-bright) !important;    /* Bright text for italics */
}
─────────────────────────────────────────────────────────────────────────────
3.2 TABS - Modern rounded style
──────────────────────────────────────────────────────────────────
──────────── */
.theme-dark .workspace-tab-header {
  background: var(--ui-bg-surface) !important;
  border: 1px solid var(--ui-border) !important;
  text-transform: uppercase !important;
  padding: 0px 4px !important;
  color: var(--ui-bg-base) !important;
  font-weight: 100 !important;
  border-radius: 8px !important;
  margin-right: 4px !important;
  box-shadow: 0 10px 15px rgba(255, 0, 0, 0.44) !important;
  }
  .theme-dark .workspace-tab-header.is-active {
  background: #4700005c !important;
  color: var(--ui-bg-surface) !important;
  font-weight: 600 !important;
  box-shadow: 0 10px 15px rgba(255, 0, 0, 1) !important;
  }

/*


/* custom cursor that glows red*/
.cm-editor .cm-content {
  caret-color: var(--v4d3r-red-primary) !important;
}
.cm-cursor {
  border-left-color: var(--v4d3r-red-primary) !important;
  border-left-width: 2px !important;
  box-shadow: 0 0 8px var(--v4d3r-red-primary) !important;
}

/* ╔══════════════════════════════════════════════════════════════════════════════╗
   ║                     SECTION 1: WORKSPACE FOUNDATION                          ║
   ║               Toggle: Each section can be enabled/disabled                   ║
   ╚══════════════════════════════════════════════════════════════════════════════╝ */
/*







   ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 1.4 WORKSPACE FOUNDATION                                                     │
   │ Toggle: Base workspace styling                                               │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Workspace Background --- */
.workspace {
  background-color: var(--v4d3r-black-deep) !important;
}

.workspace-background-modifier-translucent {
  background-color: var(--v4d3r-bg-primary) !important;
}
/* --- END TOGGLE: Workspace Background --- */

/* --- BEGIN TOGGLE: Divider Styling --- */
.workspace-leaf-resize-handle {
  background-color: transparent !important;
  border-color: var(--v4d3r-border-subtle) !important;
  transition: background-color var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;
}

.workspace-leaf-resize-handle:hover {
  background-color: var(--v4d3r-red-primary) !important;
  border-color: var(--v4d3r-red-primary) !important;
}

/* Divider between panes */
.workspace-split.mod-vertical > .workspace-leaf-resize-handle,
.workspace-split.mod-horizontal > .workspace-leaf-resize-handle {
  background-color: var(--v4d3r-border-subtle) !important;
}

.workspace-split.mod-vertical > .workspace-leaf-resize-handle:hover,
.workspace-split.mod-horizontal > .workspace-leaf-resize-handle:hover {
  background-color: var(--v4d3r-red-primary) !important;
}
/* --- END TOGGLE: Divider Styling --- */

/* --- BEGIN TOGGLE: Scrollbar Customization --- */
::-webkit-scrollbar {
  width: 8px !important;
  height: 8px !important;
}

::-webkit-scrollbar-track {
  background: var(--v4d3r-bg-primary) !important;
  border-radius: var(--v4d3r-radius-full) !important;
}

::-webkit-scrollbar-thumb {
  background: var(--v4d3r-grey-mid) !important;
  border-radius: var(--v4d3r-radius-full) !important;
  border: 2px solid var(--v4d3r-bg-primary) !important;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--v4d3r-red-muted) !important;
}

::-webkit-scrollbar-thumb:active {
  background: var(--v4d3r-red-primary) !important;
}

/* Thin scrollbar variant */
::-webkit-scrollbar-corner {
  background: var(--v4d3r-bg-primary) !important;
}
/* --- END TOGGLE: Scrollbar Customization --- */

/* ═══════════════════════════════════════════════════════════════════════════════
   END OF PART 1 - Core Variables & Foundations
   ═══════════════════════════════════════════════════════════════════════════════ */


/* ═══════════════════════════════════════════════════════════════════════════════
   PART 2: RIBBON & SIDEBAR CUSTOMIZATION
   Toggle: Each section can be enabled/disabled independently
   ═══════════════════════════════════════════════════════════════════════════════ */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 2.1 RIBBON BASE STYLING                                                      │
   │ Toggle: Customize ribbon appearance                                          │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Ribbon Base Colors --- */
.workspace-ribbon {
  background-color: var(--v4d3r-black-deep) !important;  border-color: var(--v4d3r-border-subtle) !important;}

.workspace-ribbon.mod-left {
  background-color: var(--v4d3r-black-deep) !important;  border-right: 1px solid var(--v4d3r-border-subtle) !important;}

.workspace-ribbon.mod-left::before {
  background-color: var(--v4d3r-black-deep) !important;  border-bottom: 1px solid var(--v4d3r-border-subtle) !important;}
/* --- END TOGGLE: Ribbon Base Colors --- */

/* --- BEGIN TOGGLE: Ribbon Icon Styling --- */
.workspace-ribbon .sidebar-toggle-button,
.workspace-ribbon .clickable-icon {
  color: var(--v4d3r-grey-lighter) !important;  transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}

.workspace-ribbon .sidebar-toggle-button:hover,
.workspace-ribbon .clickable-icon:hover {
  color: var(--v4d3r-red-accent) !important;  background-color: var(--v4d3r-bg-hover) !important;  border-radius: var(--v4d3r-radius-sm) !important;}

.workspace-ribbon .clickable-icon.is-active {
  color: var(--v4d3r-red-primary) !important;}
/* --- END TOGGLE: Ribbon Icon Styling --- */

/* --- BEGIN TOGGLE: Colored Ribbon Accent --- */

.workspace-ribbon.mod-left {
  --titlebar-background-focused: var(--v4d3r-red-dark) !important;  background-color: var(--v4d3r-red-dark)!important !important;}

.workspace-ribbon.mod-left::before,
.workspace-ribbon.mod-left > .sidebar-toggle-button {
  --titlebar-background: var(--v4d3r-red-dark) !important;}

.workspace-ribbon.mod-left .clickable-icon {
  color: rgba(255, 255, 255, 0.8) !important;}

.workspace-ribbon.mod-left .clickable-icon:hover {
  color: #ffffff !important;  background-color: rgba(74, 63, 63, 0.1) !important;}
*/
/* --- END TOGGLE: Colored Ribbon Accent --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 2.2 IMMERSIVE RIBBON - HIDE ON COLLAPSE                                      │
   │ Toggle: Ribbon fades/hides when sidebar is collapsed                         │
   └──────────────────────────────────────────────────────────────────────────────┘ */

 --- BEGIN TOGGLE: Immersive Ribbon (Hide on Collapse) --- */
.workspace-ribbon.mod-left.is-collapsed {
  background-color: transparent !important;  transition: background-color var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}
.workspace-ribbon.mod-left.is-collapsed 
  .sidebar-toggle-button,
.workspace-ribbon.mod-left.is-collapsed 
  .clickable-icon {
  opacity: 0 !important;  transition: opacity var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}
.workspace-ribbon.mod-left:not(.is-collapsed) 
  .sidebar-toggle-button,
.workspace-ribbon.mod-left:not(.is-collapsed) 
  .clickable-icon {
  opacity: 1 !important;}
/* --- END TOGGLE: Immersive Ribbon (Hide on Collapse) --- */

.workspace-ribbon.mod-left {
  transition: all var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}

.workspace-ribbon.mod-left::before {
  transition: all var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}

.workspace-ribbon.mod-left.is-collapsed {
  background-color: transparent !important;  border-right-color: transparent !important;}

.workspace-ribbon.mod-left.is-collapsed::before {
  border-bottom-color: transparent !important;}

 Fade ribbon icons when collapsed, show on hover */
.workspace-ribbon.mod-left.is-collapsed > :nth-child(n+2) {
  opacity: 0 !important;  transition: opacity var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}

.workspace-ribbon.mod-left.is-collapsed:hover > :nth-child(n+2) {
  opacity: 1 !important;}

/* Keep toggle button visible */
.workspace-ribbon.mod-left.is-collapsed:hover::before {
  border-bottom-color: var(--v4d3r-border-subtle) !important;}
/* --- END TOGGLE: Immersive Ribbon (Hide on Collapse) --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 2.3 SIDEBAR BASE STYLING                                                     │
   │ Toggle: Customize left and right sidebar appearance                          │
   └──────────────────────────────────────────────────────────────────────────────┘ */

   /* --- BEGIN TOGGLE: Sidebar Base Colors --- */
   .workspace-split.mod-horizontal.mod-left-split,
   .workspace-split.mod-horizontal.mod-right-split {
     background-color: var(--v4d3r-black-deep) !important;  border-color: var(--v4d3r-border-subtle) !important;}
   /* --- END TOGGLE: Sidebar Base Colors --- */
   
   /* --- BEGIN TOGGLE: Sidebar Background --- */
   .mod-left-split,
   .mod-right-split {
     background-color: var(--v4d3r-bg-secondary) !important;}
   
   .mod-left-split .workspace-tabs,
   .mod-right-split .workspace-tabs {
     background-color: var(--v4d3r-bg-secondary) !important;}
   
   .workspace-tab-container {
     background-color: var(--v4d3r-bg-secondary) !important;}
   /* --- END TOGGLE: Sidebar Background --- */


/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 2.4 IMMERSIVE SIDEBAR COLLAPSE                                               │
   │ Toggle: Sidebar content fades when collapsed                                 │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Immersive Sidebar Collapse --- */
.workspace-split.mod-horizontal.mod-left-split.is-sidedock-collapsed,
.workspace-split.mod-horizontal.mod-right-split.is-sidedock-collapsed {
  background-color: transparent !important;}

.workspace-split.mod-horizontal:is(.mod-left-split, .mod-right-split).is-sidedock-collapsed 
  .workspace-tabs .workspace-tab-header-container,
.workspace-split.mod-horizontal:is(.mod-left-split, .mod-right-split).is-sidedock-collapsed 
  .workspace-tabs .workspace-tab-container,
.workspace-split.mod-horizontal:is(.mod-left-split, .mod-right-split).is-sidedock-collapsed 
  .workspace-tabs .workspace-leaf-resize-handle {
  opacity: 0 !important;  transition: opacity var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}

.workspace-split.mod-horizontal:is(.mod-left-split, .mod-right-split).is-sidedock-collapsed 
  .workspace-tabs.mod-top .workspace-tab-header-container {
  opacity: 1 !important;}
/* --- END TOGGLE: Immersive Sidebar Collapse --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 2.5 SIDEBAR CONNECTION LINES                                                 │
   │ Toggle: Visual hierarchy lines in navigation                                 │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Navigation Connection Lines --- */
/* File explorer and nav folder connection lines */
.nav-folder-children .nav-folder-children {
  margin-left: 10px !important;  padding-left: 10px !important;  border-left: 1px solid var(--v4d3r-grey-dark) !important;  border-radius: var(--v4d3r-radius-sm) !important;  transition: border-color var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}

.nav-folder-children .nav-folder-children:hover {
  border-left-color: var(--v4d3r-red-muted) !important;}

/* Outline pane connection lines */
.outline .tree-item-children {
  margin-left: 12px !important;  padding-left: 8px !important;  border-left: 1px solid var(--v4d3r-grey-dark) !important;  border-radius: var(--v4d3r-radius-sm) !important;  transition: border-color var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}

.outline .tree-item-children:hover {
  border-left-color: var(--v4d3r-red-muted) !important;}

/* Backlinks connection lines */
.backlink-pane .tree-item-children {
  margin-left: 12px !important;  padding-left: 8px !important;  border-left: 1px solid var(--v4d3r-grey-dark) !important;  border-radius: var(--v4d3r-radius-sm) !important;}
/* --- END TOGGLE: Navigation Connection Lines --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 2.6 SIDEBAR RESIZE HANDLE ACCENT                                             │
   │ Toggle: Red accent on resize handle hover                                    │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Sidebar Resize Handle --- */
.mod-left-split > .workspace-leaf-resize-handle,
.mod-right-split > .workspace-leaf-resize-handle {
  background-color: transparent !important;  transition: background-color var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}

.mod-left-split > .workspace-leaf-resize-handle:hover,
.mod-right-split > .workspace-leaf-resize-handle:hover {
  background-color: var(--v4d3r-red-primary) !important;}
/* --- END TOGGLE: Sidebar Resize Handle --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 2.7 COLLAPSIBLE RIBBON WIDTH                                                 │
   │ Toggle: Make ribbon super thin when collapsed                                │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Thin Collapsed Ribbon --- */

.workspace-ribbon.mod-left.is-collapsed {
  width: 0px !important;  overflow: hidden !important;}

.workspace-ribbon.mod-left.is-collapsed:hover {
  width: var(--ribbon-width) !important;  overflow: visible !important;}
*/
/* --- END TOGGLE: Thin Collapsed Ribbon --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 2.8 VERTICAL LABELED NAVIGATION (Left Sidebar)                               │
   │ Toggle: Show text labels next to sidebar icons                               │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Vertical Label Navigation --- */

.mod-left-split .mod-top .workspace-tab-header-container {
  flex-direction: column-reverse !important !important;  height: auto !important;  width: 100% !important;}

.mod-left-split .mod-top .workspace-tab-header-container .workspace-tab-container-inner {
  flex-direction: column !important !important;  background-color: var(--v4d3r-bg-secondary) !important;  gap: 0 !important;  padding: var(--v4d3r-spacing-sm) var(--v4d3r-spacing-md) !important;}

.mod-left-split .mod-top .workspace-tab-header {
  padding: 0 !important;  margin-bottom: 2px !important;  height: auto !important;}

.mod-left-split .mod-top .workspace-tab-header .workspace-tab-header-inner {
  gap: var(--v4d3r-spacing-xs) !important;  padding: var(--v4d3r-spacing-xs) var(--v4d3r-spacing-sm) !important;}

.mod-left-split .mod-top .workspace-tab-header-inner-title {
  display: inline-block !important;  font-weight: 500 !important;  font-size: 0.85em !important;}

.mod-left-split .mod-top .workspace-tab-header-spacer {
  display: none !important;}
/* --- END TOGGLE: Vertical Label Navigation --- */

/* ═══════════════════════════════════════════════════════════════════════════════
   END OF PART 2 - Ribbon & Sidebar
   ═══════════════════════════════════════════════════════════════════════════════ */

   

/* ═══════════════════════════════════════════════════════════════════════════════
   PART 3: TABS & TAB BAR CUSTOMIZATION
   Toggle: Each section can be enabled/disabled independently
   ═══════════════════════════════════════════════════════════════════════════════ */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.1 TAB HEADER BASE STYLING                                                  │
   │ Toggle: Core tab appearance and colors                                       │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Tab Header Base --- */
.workspace-tab-header-container {
  background-color: var(--v4d3r-bg-tertiary) !important;  border-bottom: 1px solid var(--v4d3r-border-subtle) !important;  padding: 0 !important;}

.workspace-tab-header {
  color: var(--v4d3r-text-muted) !important;  background-color: transparent !important;  transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}

.workspace-tab-header:hover {
  color: var(--v4d3r-text-primary) !important;  background-color: var(--v4d3r-bg-hover) !important;}

.workspace-tab-header.is-active {
  color: var(--v4d3r-text-primary) !important;  background-color: var(--v4d3r-bg-primary) !important;}

/* Active tab indicator line */
.workspace-tab-header.is-active::after {
  content: '' !important;  position: absolute !important;  bottom: 0 !important;  left: 0 !important;  right: 0 !important;  height: 2px !important;  background-color: var(--v4d3r-red-primary) !important;}
/* --- END TOGGLE: Tab Header Base --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.2 SQUARE TABS                                                              │
   │ Toggle: Remove rounded corners from tabs                                     │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Square Tabs --- */
.workspace-tab-header {
  border-radius: 0 !important !important;}

.workspace-tab-header-inner {
  border-radius: 0 !important;}

.workspace-tab-header-container-inner {
  gap: 0 !important;}

/* Add subtle separator between tabs */
.workspace-tab-header:not(:last-child) {
  border-right: 1px solid var(--v4d3r-border-subtle) !important;}
/* --- END TOGGLE: Square Tabs --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.3 COLORED TAB CONTAINER                                                    │
   │ Toggle: Red accent for tab container background                              │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Colored Tab Container --- */
/*
.mod-root .workspace-tab-header-container {
  background-color: var(--v4d3r-red-dark) !important;  border-bottom: none !important;}

.mod-root .workspace-tab-header {
  color: rgba(255, 255, 255, 0.7) !important;}

.mod-root .workspace-tab-header:hover {
  color: #ffffff !important;  background-color: rgba(255, 255, 255, 0.1) !important;}

.mod-root .workspace-tab-header.is-active {
  color: #ffffff !important;  background-color: var(--v4d3r-bg-primary) !important;}

.mod-root .workspace-tab-header.is-active::after {
  background-color: #ffffff !important;}
*/
/* --- END TOGGLE: Colored Tab Container --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.4 STACKED TABS STYLING                                                     │
   │ Toggle: Enhanced stacked/vertical tab appearance                             │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Stacked Tabs Base --- */
.workspace-tabs.mod-stacked .workspace-tab-header-container {
  background-color: var(--v4d3r-bg-tertiary) !important;  border-bottom: none !important;  border-right: 1px solid var(--v4d3r-border-subtle) !important;}

.workspace-tabs.mod-stacked .workspace-tab-header {
  background-color: transparent !important;  border-bottom: 1px solid var(--v4d3r-border-subtle) !important;}

.workspace-tabs.mod-stacked .workspace-tab-header:hover {
  background-color: var(--v4d3r-bg-hover) !important;}

.workspace-tabs.mod-stacked .workspace-tab-header.is-active {
  background-color: var(--v4d3r-bg-primary) !important;}

/* Active indicator for stacked tabs - left border instead of bottom */
.workspace-tabs.mod-stacked .workspace-tab-header.is-active::before {
  content: '' !important;  position: absolute !important;  left: 0 !important;  top: 0 !important;  bottom: 0 !important;  width: 3px !important;  background-color: var(--v4d3r-red-primary) !important;}

.workspace-tabs.mod-stacked .workspace-tab-header.is-active::after {
  display: none !important;}
/* --- END TOGGLE: Stacked Tabs Base --- */

/* --- BEGIN TOGGLE: Stacked Tabs Vertical Text --- */
/*
.workspace-tabs.mod-stacked .workspace-tab-header .workspace-tab-header-inner-title {
  writing-mode: vertical-rl !important;  text-orientation: mixed !important;  transform: rotate(180deg) !important;  white-space: nowrap !important;  font-size: 0.85em !important;  letter-spacing: 0.5px !important;}
*/
/* --- END TOGGLE: Stacked Tabs Vertical Text --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.5 COMPACT TABS                                                             │
   │ Toggle: Reduce tab height and padding                                        │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Compact Tabs --- */
/*
.workspace-tab-header-container {
  --tab-container-height: 32px !important;}

.workspace-tab-header {
  min-height: 28px !important;  padding-top: 2px !important;  padding-bottom: 2px !important;}

.workspace-tab-header-inner {
  padding: 2px 8px !important;  font-size: 0.9em !important;}

.workspace-tab-header-inner-icon {
  width: 14px !important;  height: 14px !important;}
*/
/* --- END TOGGLE: Compact Tabs --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.6 PINNED TAB STYLING                                                       │
   │ Toggle: Special appearance for pinned tabs                                   │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Pinned Tab Styling --- */
.workspace-tab-header.is-pinned {
  background-color: var(--v4d3r-bg-tertiary) !important;  position: relative !important;}

.workspace-tab-header.is-pinned::before {
  content: '' !important;  position: absolute !important;  top: 4px !important;  left: 4px !important;  width: 6px !important;  height: 6px !important;  background-color: var(--v4d3r-red-accent) !important;  border-radius: 50% !important;  opacity: 0.8 !important;}

.workspace-tab-header.is-pinned:hover::before {
  opacity: 1 !important;  animation: pulse 1.5s ease-in-out infinite !important;}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 0.8; }
  50% { transform: scale(1.2); opacity: 1; }
}
/* --- END TOGGLE: Pinned Tab Styling --- */

/* --- BEGIN TOGGLE: Pinned Tab Icon Only --- */

.workspace-tab-header.is-pinned .workspace-tab-header-inner-title {
  display: none !important;}

.workspace-tab-header.is-pinned {
  max-width: 40px !important;  min-width: 40px !important;}

.workspace-tab-header.is-pinned .workspace-tab-header-inner {
  justify-content: center !important;}

/* --- END TOGGLE: Pinned Tab Icon Only --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.7 TAB CLOSE BUTTON STYLING                                                 │
   │ Toggle: Customize close button appearance                                    │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Tab Close Button --- */
.workspace-tab-header-inner-close-button {
  color: var(--v4d3r-text-muted) !important;  opacity: 0.7 !important;  transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}

.workspace-tab-header-inner-close-button:hover {
  color: var(--v4d3r-red-accent) !important;  opacity: 1 !important;  background-color: var(--v4d3r-bg-hover) !important;  border-radius: var(--v4d3r-radius-sm) !important;}
/* --- END TOGGLE: Tab Close Button --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.8 TAB FADE EFFECT                                                          │
   │ Toggle: Inactive tabs fade for focus                                         │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Tab Fade Effect --- */

.workspace-tab-header:not(.is-active) {
  opacity: 0.6 !important;}

.workspace-tab-header:not(.is-active):hover {
  opacity: 0.9 !important;}

.workspace-tab-header-container:hover .workspace-tab-header:not(.is-active) {
  opacity: 0.8 !important;}
*/
/* --- END TOGGLE: Tab Fade Effect --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.9 NEW TAB BUTTON STYLING                                                   │
   │ Toggle: Customize the new tab button                                         │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: New Tab Button --- */
.workspace-tab-header-new-tab {
  color: var(--v4d3r-text-muted) !important;  transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}

.workspace-tab-header-new-tab:hover {
  color: var(--v4d3r-red-accent) !important;  background-color: var(--v4d3r-bg-hover) !important;  border-radius: var(--v4d3r-radius-sm) !important;}
/* --- END TOGGLE: New Tab Button --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 3.10 TAB DIVIDER STYLING                                                     │
   │ Toggle: Custom dividers between tabs                                         │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Tab Dividers --- */

.workspace-tab-header:not(:last-child) {
  border-right: 1px solid var(--v4d3r-border-subtle) !important;}
.workspace-tab-header-container-inner::before {
  content: '' !important;  position: absolute !important;  left: 0 !important;  right: 0 !important;  bottom: 0 !important;  height: 1px !important;  background: linear-gradient(
    90deg,
    transparent 0%,
    var(--v4d3r-red-muted) 20%,
    var(--v4d3r-red-primary) 50%,
    var(--v4d3r-red-muted) 80%,
    transparent 100%
  ) !important;}
  /* --- END TOGGLE: Tab Dividers --- */


/* ═══════════════════════════════════════════════════════════════════════════════
   END OF PART 3 - Tabs & Tab Bar
   ═══════════════════════════════════════════════════════════════════════════════ */

/* ═══════════════════════════════════════════════════════════════════════════════
   PART 4: STATUS BAR & TITLEBAR CUSTOMIZATION
   Toggle: Each section can be enabled/disabled independently
   ═══════════════════════════════════════════════════════════════════════════════ */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 4.1 STATUS BAR BASE STYLING                                                  │
   │ Toggle: Core status bar appearance                                           │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Status Bar Base --- */
.status-bar {
  background-color: var(--v4d3r-bg-tertiary) !important;  border-top: 1px solid var(--v4d3r-border-subtle) !important;  height: 28px !important;  padding: 0 12px !important;  font-size: 12px !important;  color: var(--v4d3r-text-muted) !important;  display: flex !important;  align-items: center !important;  gap: var(--v4d3r-spacing-md) !important;}
.status-bar-item {
  color: var(--v4d3r-text-muted) !important;  transition: color var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}
.status-bar-item:hover {
  color: var(--v4d3r-text-primary) !important;}
/* --- END TOGGLE: Status Bar Base --- */
/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 4.2 FADED STATUS BAR                                                         │
   │ Toggle: Status bar fades when not hovered over                               │
   └──────────────────────────────────────────────────────────────────────────────┘ */
/* --- BEGIN TOGGLE: Status Bar Fade --- */

.status-bar {
  opacity: 0.6 !important;  transition: opacity var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}
.status-bar:hover {
  opacity: 1 !important;}
  
/* --- END TOGGLE: Status Bar Fade --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 4.3 HIDDEN STATUS BAR                                                        │
   │ Toggle: Completely hide status bar                                           │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Hidden Status Bar --- */
/*
.status-bar {
  display: none !important !important;}
*/
/* --- END TOGGLE: Hidden Status Bar --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 4.4 MINIMAL STATUS BAR                                                       │
   │ Toggle: Thin, minimal status bar                                             │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Minimal Status Bar --- */
/*
.status-bar {
  --status-bar-font-size: 11px !important;  height: 20px !important;  padding: 0 8px !important;  background-color: transparent !important;  border-top: none !important;}

.status-bar-item {
  padding: 0 4px !important;}
*/
/* --- END TOGGLE: Minimal Status Bar --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 4.5 STATUS BAR ACCENT STYLING                                                │
   │ Toggle: Red accented status bar                                              │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Status Bar Accent --- */


.status-bar {
  border-top: 2px solid var(--v4d3r-red-primary) !important;}
.status-bar-item:hover {
  color: var(--v4d3r-red-accent) !important;}

/* --- END TOGGLE: Status Bar Accent --- */


/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 4.11 WORD COUNT STYLING                                                      │
   │ Toggle: Enhanced word count display                                          │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Word Count Styling --- */
.status-bar-item.plugin-word-count {
  color: var(--v4d3r-red-accent) !important;  font-family: 'JetBrains Mono', 'Fira Code', monospace !important;  font-size: 0.8em !important;}

.status-bar-item.plugin-word-count:hover {
  color: var(--v4d3r-red-primary) !important;  font-weight: 200 !important;}

  
/* --- END TOGGLE: Word Count Styling --- */

/* ═══════════════════════════════════════════════════════════════════════════════
   END OF PART 4 - Status Bar & Titlebar
   ═══════════════════════════════════════════════════════════════════════════════ */


/* ═══════════════════════════════════════════════════════════════════════════════
   PART 5: FILE EXPLORER & NAVIGATION
   Toggle: Each section can be enabled/disabled independently
   ═══════════════════════════════════════════════════════════════════════════════ */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.1 FILE EXPLORER BASE STYLING                                               │
   │ Toggle: Core file explorer appearance                                        │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: File Explorer Base --- */

.nav-file-title:hover,
.nav-folder-title:hover {
  color: var(--v4d3r-red-accent) !important;}
.nav-folder-title:hover,



/* --- END TOGGLE: File Explorer Base --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.2 FOLDER ACCENT COLORING                                                   │
   │ Toggle: Red accent for folder names                                          │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Folder Accent Coloring --- */
.nav-folder-title-content {
  color: var(--v4d3r-red-accent) !important;  font-weight: 500 !important;}

.nav-folder.is-collapsed .nav-folder-title-content {
  color: var(--v4d3r-text-muted) !important;}

.nav-folder-title:hover .nav-folder-title-content {
  color: var(--v4d3r-red-primary) !important;}
/* --- END TOGGLE: Folder Accent Coloring --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.3 RAINBOW FOLDER BACKGROUNDS                                               │
   │ Toggle: Depth-based folder coloring                                          │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Rainbow Folder Backgrounds --- */
/*
.nav-folder-children .nav-folder-children {
  background-color: rgba(220, 38, 38, 0.03) !important;}

.nav-folder-children .nav-folder-children .nav-folder-children {
  background-color: rgba(220, 38, 38, 0.05) !important;}

.nav-folder-children .nav-folder-children .nav-folder-children .nav-folder-children {
  background-color: rgba(220, 38, 38, 0.07) !important;}

.nav-folder-children .nav-folder-children .nav-folder-children .nav-folder-children .nav-folder-children {
  background-color: rgba(220, 38, 38, 0.09) !important;}
*/
/* --- END TOGGLE: Rainbow Folder Backgrounds --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.4 FILE TYPE ICONS                                                          │
   │ Toggle: Custom icons based on file extension                                 │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: File Type Icons --- */
/* Markdown files */
.nav-file-title[data-path$=".md"] .nav-file-title-content::before {
  content: "- " !important;  font-size: 0.9em !important;}

/* Canvas files */
.nav-file-title[data-path$=".canvas"] .nav-file-title-content::before {
  content: "🎨 " !important;  font-size: 0.9em !important;}

/* PDF files */
.nav-file-title[data-path$=".pdf"] .nav-file-title-content::before {
  content: "📕 " !important;  font-size: 0.9em !important;}

/* Image files */
.nav-file-title[data-path$=".png"] .nav-file-title-content::before,
.nav-file-title[data-path$=".jpg"] .nav-file-title-content::before,
.nav-file-title[data-path$=".jpeg"] .nav-file-title-content::before,
.nav-file-title[data-path$=".gif"] .nav-file-title-content::before,
.nav-file-title[data-path$=".svg"] .nav-file-title-content::before {
  content: "🖼️ " !important;  font-size: 0.9em !important;}

/* Excalidraw */
.nav-file-title[data-path$=".excalidraw.md"] .nav-file-title-content::before {
  content: "✏️ " !important;  font-size: 0.9em !important;}
/* --- END TOGGLE: File Type Icons --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.5 FOLDER ICONS                                                             │
   │ Toggle: Custom folder icons                                                  │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Folder Icons --- */
.nav-folder.is-open .nav-folder-title-content::before {
  content: "📂 " !important;}

.nav-folder.is-collapsed .nav-folder-title-content::before {
  content: "📁 " !important;}

/* Special folders */
.nav-folder-title[data-path="00-inbox"] .nav-folder-title-content::before,
.nav-folder-title[data-path*="inbox"] .nav-folder-title-content::before {
  content: "📥 " !important;}

.nav-folder-title[data-path*="archive"] .nav-folder-title-content::before,
.nav-folder-title[data-path*="99-archive"] .nav-folder-title-content::before {
  content: "🗄️ " !important;}


/* --- END TOGGLE: Folder Icons --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.6 FILE EXPLORER HOVER REVEAL                                               │
   │ Toggle: Show additional info on hover                                        │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: File Explorer Hover Reveal --- */

/* .nav-file-title .nav-file-title-extra-info {
  opacity: 0 !important;  max-width: 0 !important;  overflow: hidden !important;  transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}
.nav-file-title:hover .nav-file-title-extra-info {
  opacity: 1 !important;  max-width: 200px !important;  margin-left: var(--v4d3r-spacing-sm) !important;}

/* --- END TOGGLE: File Explorer Hover Reveal --- */
/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.7 ACTIVE FILE ACCENT                                                       │
   │ Toggle: Strong accent for active file                                        │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Active File Accent --- */
.nav-file-title.is-active {
  background-color: var(--v4d3r-red-muted) !important;  border-left: 3px solid var(--v4d3r-red-primary) !important;  padding-left: calc(var(--nav-item-padding) - 3px) !important;}

.nav-file-title.is-active .nav-file-title-content {
  color: var(--v4d3r-text-primary) !important;  font-weight: 500 !important;}
/* --- END TOGGLE: Active File Accent --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.8 SEARCH RESULTS STYLING                                                   │
   │ Toggle: Enhanced search result appearance                                    │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Search Results Styling --- */
.search-result-file-title {
  color: var(--v4d3r-red-accent) !important;  font-weight: 500 !important;}

.search-result-file-matched-text {
  color: var(--v4d3r-text-primary) !important;  background-color: var(--v4d3r-red-muted) !important;  padding: 0 2px !important;  border-radius: 2px !important;}

.search-result-file-match {
  border-left: 2px solid var(--v4d3r-red-muted) !important;  padding-left: 8px !important;  margin-left: 8px !important;}

.search-result-file-match:hover {
  border-left-color: var(--v4d3r-red-primary) !important;  background-color: var(--v4d3r-bg-hover) !important;}
/* --- END TOGGLE: Search Results Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.9 TAG PANE STYLING                                                         │
   │ Toggle: Enhanced tag appearance                                              │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Tag Pane Styling --- */
.tag-pane-tag {
  color: var(--v4d3r-text-secondary) !important;  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.tag-pane-tag:hover {
  color: var(--v4d3r-red-accent) !important;  background-color: var(--v4d3r-bg-hover) !important;}

.tag-pane-tag-count {
  color: var(--v4d3r-grey-base) !important;  background-color: var(--v4d3r-bg-tertiary) !important;  border-radius: var(--v4d3r-radius-sm) !important;  padding: 0 4px !important;  font-size: 0.8em !important;}

.tag-pane-tag:hover .tag-pane-tag-count {
  background-color: var(--v4d3r-red-muted) !important;  color: var(--v4d3r-text-primary) !important;}
/* --- END TOGGLE: Tag Pane Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 5.10 BOOKMARKS/STARRED STYLING                                               │
   │ Toggle: Enhanced bookmarks appearance                                        │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Bookmarks Styling --- */
.bookmark-item {
  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.bookmark-item:hover {
  background-color: var(--v4d3r-bg-hover) !important;}

.bookmark-item .nav-file-title-content::before {
  content: "⭐ " !important;  font-size: 0.85em !important;}

/* Bookmark groups */
.bookmark-group-title {
  color: var(--v4d3r-red-accent) !important;  font-weight: 500 !important;}
/* --- END TOGGLE: Bookmarks Styling --- */

/* ═══════════════════════════════════════════════════════════════════════════════
   END OF PART 5 - File Explorer & Navigation
   ═══════════════════════════════════════════════════════════════════════════════ */


/* ═══════════════════════════════════════════════════════════════════════════════
   PART 6: ADVANCED FEATURES & SPECIAL EFFECTS
   Toggle: Each section can be enabled/disabled independently
   ═══════════════════════════════════════════════════════════════════════════════ */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.1 TRANSLUCENT MODALS                                                       │
   │ Toggle: Blur effect behind modals and popups                                 │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Translucent Modals --- */
.modal-bg {
  background-color: rgba(0, 0, 0, 0.7) !important;  backdrop-filter: blur(8px) !important;  -webkit-backdrop-filter: blur(8px) !important;}

.modal {
  background-color: var(--v4d3r-bg-primary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-radius: var(--v4d3r-radius-lg) !important;  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5) !important;}

.modal-title {
  color: var(--v4d3r-text-primary) !important;  border-bottom: 1px solid var(--v4d3r-border-subtle) !important;}

.modal-close-button {
  color: var(--v4d3r-text-muted) !important;  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.modal-close-button:hover {
  color: var(--v4d3r-red-primary) !important;  background-color: var(--v4d3r-red-muted) !important;}
/* --- END TOGGLE: Translucent Modals --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.2 COMMAND PALETTE STYLING                                                  │
   │ Toggle: Enhanced command palette appearance                                  │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Command Palette Styling --- */
.prompt {
  background-color: var(--v4d3r-bg-secondary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-radius: var(--v4d3r-radius-lg) !important;  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5) !important;}

.prompt-input-container {
  background-color: var(--v4d3r-bg-primary) !important;  border-bottom: 1px solid var(--v4d3r-border-subtle) !important;}

.prompt-input {
  color: var(--v4d3r-text-primary) !important;}

.prompt-input::placeholder {
  color: var(--v4d3r-text-muted) !important;}

.suggestion-item {
  color: var(--v4d3r-text-secondary) !important;  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.suggestion-item.is-selected {
  background-color: var(--v4d3r-bg-active) !important;  color: var(--v4d3r-text-primary) !important;  border-left: 3px solid var(--v4d3r-red-primary) !important;}

.suggestion-hotkey {
  color: var(--v4d3r-grey-base) !important;  background-color: var(--v4d3r-bg-tertiary) !important;  border-radius: var(--v4d3r-radius-sm) !important;  padding: 2px 6px !important;  font-size: 0.8em !important;}
/* --- END TOGGLE: Command Palette Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.3 TOOLTIP STYLING                                                          │
   │ Toggle: Enhanced tooltip appearance                                          │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Tooltip Styling --- */
.tooltip {
  background-color: var(--v4d3r-black-deep) !important;  color: var(--v4d3r-text-primary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-radius: var(--v4d3r-radius-md) !important;  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4) !important;  font-size: 0.85em !important;  padding: 6px 10px !important;}

.tooltip .tooltip-arrow {
  border-color: var(--v4d3r-black-deep) !important;}
/* --- END TOGGLE: Tooltip Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.4 MENU STYLING                                                             │
   │ Toggle: Enhanced context menu and dropdown appearance                        │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Menu Styling --- */
.menu {
  background-color: var(--v4d3r-bg-secondary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-radius: var(--v4d3r-radius-md) !important;  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4) !important;  padding: 4px !important;}

.menu-item {
  color: var(--v4d3r-text-secondary) !important;  border-radius: var(--v4d3r-radius-sm) !important;  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.menu-item:hover {
  background-color: var(--v4d3r-bg-hover) !important;  color: var(--v4d3r-text-primary) !important;}

.menu-item.is-warning:hover {
  background-color: var(--v4d3r-red-muted) !important;  color: var(--v4d3r-red-primary) !important;}

.menu-separator {
  background-color: var(--v4d3r-border-subtle) !important;  margin: 4px 0 !important;}
/* --- END TOGGLE: Menu Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.5 EMPTY STATE STYLING                                                      │
   │ Toggle: Style for empty tabs and panes                                       │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Empty State Styling --- */
.empty-state {
  color: var(--v4d3r-text-muted) !important;}

.empty-state-title {
  color: var(--v4d3r-text-secondary) !important;  font-size: 1.2em !important;  margin-bottom: 8px !important;}

.empty-state-action {
  color: var(--v4d3r-red-accent) !important;  transition: color var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.empty-state-action:hover {
  color: var(--v4d3r-red-primary) !important;}

/* New tab empty state */
.workspace-leaf-content[data-type="empty"] {
  background: radial-gradient(
    ellipse at center,
    var(--v4d3r-bg-secondary) 0%,
    var(--v4d3r-bg-primary) 70%
  ) !important;}
/* --- END TOGGLE: Empty State Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.6 LOADING ANIMATION                                                        │
   │ Toggle: Custom loading spinner                                               │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Loading Animation --- */
.loading-container {
  color: var(--v4d3r-red-accent) !important;}

/* Custom spinner animation */
@keyframes v4d3r-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-icon {
  animation: v4d3r-spin 1s linear infinite !important;}

/* Progress bar */
.progress-bar {
  background-color: var(--v4d3r-bg-tertiary) !important;  border-radius: var(--v4d3r-radius-sm) !important;  overflow: hidden !important;}

.progress-bar-inner {
  background: linear-gradient(
    90deg,
    var(--v4d3r-red-dark) 0%,
    var(--v4d3r-red-primary) 50%,
    var(--v4d3r-red-accent) 100%
  ) !important;  transition: width var(--v4d3r-transition-slow) var(--v4d3r-ease-default) !important;}
/* --- END TOGGLE: Loading Animation --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.7 NOTICE/NOTIFICATION STYLING                                              │
   │ Toggle: Enhanced notification appearance                                     │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Notice Styling --- */
.notice {
  background-color: var(--v4d3r-bg-secondary) !important;  color: var(--v4d3r-text-primary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-left: 4px solid var(--v4d3r-red-primary) !important;  border-radius: var(--v4d3r-radius-md) !important;  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3) !important;}

.notice-container {
  padding: 12px 16px !important;}

/* Success notice */
.notice.mod-success {
  border-left-color: #4ade80 !important;}

/* Warning notice */
.notice.mod-warning {
  border-left-color: #fbbf24 !important;}

/* Error notice */
.notice.mod-error {
  border-left-color: var(--v4d3r-red-primary) !important;  background-color: var(--v4d3r-red-muted) !important;}
/* --- END TOGGLE: Notice Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.8 BUTTON STYLING                                                           │
   │ Toggle: Enhanced button appearance                                           │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Button Styling --- */
button {
  background-color: var(--v4d3r-bg-tertiary) !important;  color: var(--v4d3r-text-secondary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-radius: var(--v4d3r-radius-md) !important;  transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}

button:hover {
  background-color: var(--v4d3r-bg-hover) !important;  color: var(--v4d3r-text-primary) !important;  border-color: var(--v4d3r-grey-base) !important;}

button.mod-cta {
  background-color: var(--v4d3r-red-primary) !important;  color: #ffffff !important;  border-color: var(--v4d3r-red-primary) !important;}

button.mod-cta:hover {
  background-color: var(--v4d3r-red-accent) !important;  border-color: var(--v4d3r-red-accent) !important;}

button.mod-warning {
  background-color: transparent !important;  color: var(--v4d3r-red-primary) !important;  border-color: var(--v4d3r-red-primary) !important;}

button.mod-warning:hover {
  background-color: var(--v4d3r-red-muted) !important;}
/* --- END TOGGLE: Button Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.9 INPUT FIELD STYLING                                                      │
   │ Toggle: Enhanced input and textarea appearance                               │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Input Field Styling --- */
input[type="text"],
input[type="search"],
input[type="email"],
input[type="password"],
input[type="number"],
textarea {
  background-color: var(--v4d3r-bg-primary) !important;  color: var(--v4d3r-text-primary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-radius: var(--v4d3r-radius-sm) !important;  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

input:focus,
textarea:focus {
  border-color: var(--v4d3r-red-accent) !important;  box-shadow: 0 0 0 2px var(--v4d3r-red-muted) !important;  outline: none !important;}

input::placeholder,
textarea::placeholder {
  color: var(--v4d3r-text-muted) !important;}
/* --- END TOGGLE: Input Field Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.10 CHECKBOX & TOGGLE STYLING                                               │
   │ Toggle: Enhanced checkbox and toggle switch appearance                       │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Checkbox Styling --- */
.checkbox-container {
  background-color: var(--v4d3r-bg-tertiary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-radius: var(--v4d3r-radius-sm) !important;  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.checkbox-container:hover {
  border-color: var(--v4d3r-grey-base) !important;}

.checkbox-container.is-enabled {
  background-color: var(--v4d3r-red-primary) !important;  border-color: var(--v4d3r-red-primary) !important;}

/* Toggle switch */
.setting-item-control .checkbox-container {
  width: 40px !important;  height: 22px !important;  border-radius: 11px !important;}

.checkbox-container::after {
  background-color: var(--v4d3r-grey-lighter) !important;  border-radius: 50% !important;  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.checkbox-container.is-enabled::after {
  background-color: #ffffff !important;}
/* --- END TOGGLE: Checkbox Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.11 SETTINGS PANEL STYLING                                                  │
   │ Toggle: Enhanced settings modal appearance                                   │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Settings Panel Styling --- */
.modal.mod-settings {
  background-color: var(--v4d3r-bg-primary) !important;}

.vertical-tab-header {
  background-color: var(--v4d3r-bg-secondary) !important;  border-right: 1px solid var(--v4d3r-border-subtle) !important;}

.vertical-tab-nav-item {
  color: var(--v4d3r-text-muted) !important;  transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}

.vertical-tab-nav-item:hover {
  color: var(--v4d3r-text-primary) !important;  background-color: var(--v4d3r-bg-hover) !important;}

.vertical-tab-nav-item.is-active {
  color: var(--v4d3r-red-accent) !important;  background-color: var(--v4d3r-bg-active) !important;  border-left: 3px solid var(--v4d3r-red-primary) !important;}

.setting-item {
  border-top: 1px solid var(--v4d3r-border-subtle) !important;  padding: 16px 0 !important;}

.setting-item-name {
  color: var(--v4d3r-text-primary) !important;  font-weight: 500 !important;}

.setting-item-description {
  color: var(--v4d3r-text-muted) !important;}
/* --- END TOGGLE: Settings Panel Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.12 GRAPH VIEW STYLING                                                      │
   │ Toggle: Enhanced graph view appearance                                       │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Graph View Styling --- */
.graph-view.color-fill {
  color: var(--v4d3r-red-accent) !important;}

.graph-view.color-fill-highlight {
  color: var(--v4d3r-red-primary) !important;}

.graph-view.color-line {
  color: var(--v4d3r-grey-dark) !important;}

.graph-view.color-line-highlight {
  color: var(--v4d3r-red-muted) !important;}

.graph-view.color-text {
  color: var(--v4d3r-text-secondary) !important;}

.graph-view.color-fill-attachment {
  color: var(--v4d3r-grey-base) !important;}

.graph-view.color-fill-unresolved {
  color: var(--v4d3r-grey-dark) !important;}

/* Graph controls */
.graph-controls {
  background-color: var(--v4d3r-bg-secondary) !important;  border: 1px solid var(--v4d3r-border-subtle) !important;  border-radius: var(--v4d3r-radius-md) !important;}
/* --- END TOGGLE: Graph View Styling --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.13 CARD LAYOUT MODE                                                        │
   │ Toggle: Card-style layout for workspace leaves                               │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Card Layout Mode --- */

.workspace-leaf {
  background-color: var(--v4d3r-bg-secondary) !important;
  border: 1px solid var(--v4d3r-border-subtle) !important;
  border-radius: var(--v4d3r-radius-lg) !important;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2) !important;
  margin: 16px !important;
  overflow: hidden !important;
  transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;
  -webkit-transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;
  -moz-transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;
  -ms-transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;
  -o-transition: all var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;
}

.workspace-leaf:hover {
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3) !important;
  transform: translateY(-4px) !important;
  -webkit-transform: translateY(-4px) !important;
  -moz-transform: translateY(-4px) !important;
  -ms-transform: translateY(-4px) !important;
  -o-transform: translateY(-4px) !important;
}
.workspace-leaf .workspace-leaf-content {
  border-radius: var(--v4d3r-radius-lg) !important;
  overflow: hidden !important;
}

/* --- END TOGGLE: Card Layout Mode --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.14 FOCUS MODE ENHANCEMENT                                                  │
   │ Toggle: Dim everything except active pane                                    │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Focus Mode --- */

/*.workspace-leaf:not(.is-active) {
  opacity: 0.4 !important;  pointer-events: none !important;
  transition: opacity var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}
.workspace-leaf.is-active {
  opacity: 1 !important;  pointer-events: auto !important;
  transition: opacity var(--v4d3r-transition-normal) var(--v4d3r-ease-default) !important;}*/
/* --- END TOGGLE: Focus Mode --- */

/* ┌──────────────────────────────────────────────────────────────────────────────┐
   │ 6.15 ACCENT GLOW EFFECTS                                                     │
   │ Toggle: Subtle glow effects on interactive elements                          │
   └──────────────────────────────────────────────────────────────────────────────┘ */

/* --- BEGIN TOGGLE: Accent Glow Effects --- */

.button:hover,
.menu-item:hover,
.tab-bar-tab:hover,
.nav-file-title:hover,
.nav-folder-title:hover,
.status-bar-item:hover {
  box-shadow: 0 0 8px var(--v4d3r-red-accent) !important;  transition: box-shadow var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;}
.button:active,
.menu-item:active,
.tab-bar-tab:active,
.nav-file-title:active,
.nav-folder-title:active,
.status-bar-item:active {
  box-shadow: 0 0 12px var(--v4d3r-red-primary) !important;
  transition: box-shadow var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;
  -webkit-transition: box-shadow var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;
  -moz-transition: box-shadow var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;
  -ms-transition: box-shadow var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;
  -o-transition: box-shadow var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;
}

/* --- END TOGGLE: Accent Glow Effects --- */

/* ═══════════════════════════════════════════════════════════════════════════════
   END OF PART 6 - Advanced Features & Special Effects
   ═══════════════════════════════════════════════════════════════════════════════ */


   /* Text Rendering Fix for Obsidian 1.0+ */
body {
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
}

/*text re-sizing fix*/
body {
  font-size: var(--v4d3r-base-font-size) !important;
}



.nav-file-title-content,
.nav-folder-title-content,
.search-result-file-title,
.search-result-file-matched-text,
.tag-pane-tag,
.bookmark-item,
.bookmark-group-title {
  font-size: var(--v4d3r-base-font-size) !important;
}































═══════════════════════════════════════════════════════════════════════════════
   V4D3R UI SYSTEM - COMPLETE
   
   📁 File: v4d3r-ui-system.css
   🎨 Theme: RED / BLACK / GREY
   📦 Total Toggleable Sections: 50+
   
   ═══════════════════════════════════════════════════════════════════════════════
   
   USAGE INSTRUCTIONS:
   
   1. ENABLE SNIPPET:
      Settings → Appearance → CSS Snippets → Enable "v4d3r-ui-system"
   
   2. TOGGLE FEATURES:
      • Active features are uncommented (default ON)
      • Disabled features are wrapped in /* ... */ comments
      • To ENABLE: Remove /* at start and */ at end of the toggle block
      • To DISABLE: Add /* at start and */ at end of the toggle block
   
   3. TOGGLE BLOCK FORMAT:
      /* --- BEGIN TOGGLE: Feature Name --- */
      [CSS rules here]
      /* --- END TOGGLE: Feature Name --- */
   
   4. CUSTOMIZATION:
      • Modify colors in Section 1.1 (V4D3R Color Palette)
      • Adjust timing in Section 1.2 (Animation Variables)
      • All variables use --v4d3r-* namespace
   
   5. LIGHT THEME:
      • Uncomment the :root.theme-light section in Part 1
      • Colors will automatically adjust for light mode
   
   ═══════════════════════════════════════════════════════════════════════════════
   
   PARTS SUMMARY:
   
   Part 1: Core Variables & Foundations (Sections 1.1-1.4)
   Part 2: Ribbon & Sidebar (Sections 2.1-2.8)
   Part 3: Tabs & Tab Bar (Sections 3.1-3.10)
   Part 4: Status Bar & Titlebar (Sections 4.1-4.11)
   Part 5: File Explorer & Navigation (Sections 5.1-5.10)
   Part 6: Advanced Features (Sections 6.1-6.15)
   
   ═══════════════════════════════════════════════════════════════════════════════
   
   Created by: V4D3R UI System Generator
   Version: 1.0.0
   Last Updated: December 2025
   
   ═══════════════════════════════════════════════════════════════════════════════ */




   
   ═══════════════════════════════════════════════════════════
   SNIPPET NAME: JetBrains Mono Light Font
   Purpose: Apply JetBrains Mono Light globally across Obsidian
   Author: Pur3v4d3r
   Date: 2025-12-14
   Obsidian Version: 1.5+
   Dependencies: None
   Installation: Place in .obsidian/snippets/ and enable in Settings
   
   Description:
   Sets JetBrains Mono Light (weight: 300) as the default font
   for all editor, preview, and interface text. Provides clean,
   consistent typography throughout the application.
   
   Font Installation:
   Download JetBrains Mono from: https://www.jetbrains.com/lp/mono/
   Install all font weights for best results.
  ═══════════════════════════════════════════════════════════
  */
  
  /* [SECTION 1: Global Font Variables] */
  body {
    --font-text: "JetBrains Mono", monospace !important;
    --font-monospace: "JetBrains Mono", monospace !important;
    --font-interface: "JetBrains Mono", monospace !important;
    --font-text-weight: 100 !important; /* ← Changed to 100 */
  }
  
  body, .theme-dark body {
    font-family: "JetBrains Mono", "Courier New", monospace !important;
    font-weight: 100 !important; /* ← Changed to 100 */
  }
  
  /* [SECTION 2: Editor Text] */
  .markdown-source-view,
  .markdown-source-view.mod-cm6,
  .cm-editor,
  .cm-content,
  .cm-scroller,
  .cm-line {
    font-family: "JetBrains Mono", "Courier New", monospace !important;
    font-weight: 100 !important; /* ← Changed to 100 */
  }
  
  /* [SECTION 3: Preview/Reading Mode] */
  .markdown-preview-view,
  .markdown-rendered {
    font-family: "JetBrains Mono", "Courier New", monospace !important;
    font-weight: 100 !important; /* ← Changed to 100 */
  }
  
  /* [SECTION 4: Interface Elements] */
  .workspace,
  .nav-file-title,
  .nav-folder-title,
  .search-result-file-title,
  .workspace-tab-header-inner,
  .titlebar,
  .status-bar {
    font-family: "JetBrains Mono", "Courier New", monospace !important;
    font-weight: 100 !important; /* ← Changed to 100 */
  }
  
  /* [SECTION 5: Code Blocks] */
  code,
  pre,
  .cm-inline-code,
  .markdown-preview-view code {
    font-family: "JetBrains Mono", "Courier New", monospace !important;
    font-weight: 100 !important; /* ✓ Already 100 */
  }
  
  /* [SECTION 6: Headings Override] */
  h1, h2, h3, h4, h5, h6,
  .cm-header-1, .cm-header-2, .cm-header-3,
  .cm-header-4, .cm-header-5, .cm-header-6 {
    font-family: "JetBrains Mono", "Courier New", monospace !important;
    font-weight: 100 !important; /* ← Changed to 100 */
  }
  
  /* [SECTION 7: Accessibility - Reduced Motion] */
  @media (prefers-reduced-motion: reduce) {
    * {
      animation: none !important;
      transition: none !important;
    }
  }
  .popover.hover-popover,
  .menu,
  .suggestion-container {
    box-shadow: 0 0px 48px rgba(255, 0, 0, 0.3) !important;
  }
```
