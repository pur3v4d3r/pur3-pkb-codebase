# Modular Callout CSS System — README

> **System Version:** 1.0.0
> **Location:** `.obsidian/snippets/`
> **Author:** Pur3v4d3r
> **Obsidian:** v1.5.0+

---

## Architecture Overview

```
callout-base.css          ← Foundation layer (ALWAYS enabled)
callout-mod-[name].css    ← Visual mod (enable ONE at a time)
```

**How it works:** The base file defines all CSS custom properties (colors, spacing, timing), animation keyframes, neutral callout structure, and color assignments for 250+ custom callout types. Each mod file overrides visual treatment (backgrounds, borders, shadows, text effects) using `!important` to layer on top of the base. The mods consume `var(--callout-color)` which the base sets per callout type — so mods automatically adapt their visual effect to each callout's assigned accent color.

**To switch looks:** Disable the current mod in Settings → Appearance → CSS Snippets, then enable a different one. The base must always remain enabled.

---

## File Inventory

### Foundation

| File | Purpose |
|------|---------|
| `callout-base.css` | Color palette (16 neon RGB accents), structural variables, animation keyframes, base callout structure, color assignments for 250+ callout types, accessibility |

### Visual Mods (enable ONE)

| File | Effect | Aesthetic |
|------|--------|-----------|
| `callout-mod-neon-glow.css` | Pulsing borders, radiant shadows, glowing text | Cyberneon, vivid |
| `callout-mod-card-premium.css` | Elevated card, side accent marker, gradient title | Polished, professional |
| `callout-mod-card-glass.css` | Glassmorphism, backdrop-filter blur, reflections | Frosted, translucent |
| `callout-mod-card-floating.css` | Airy card, ground shadow illusion, hover float | Light, ethereal |
| `callout-mod-minimal-clean.css` | Ultra-clean, subtle left accent only | Zen, barely-there |
| `callout-mod-edge-glow.css` | All edges emit colored glow, breathing animation | Luminous borders |
| `callout-mod-cyberpunk.css` | Scanlines, angular corners, monospace, uppercase | Cyber, glitch-ish |
| `callout-mod-terminal.css` | CLI window chrome, prompt prefix, cursor blink | Terminal/console |
| `callout-mod-stripe-accent.css` | Diagonal stripe pattern on left accent bar | Patterned, textured |
| `callout-mod-gradient-shift.css` | Animated gradient backgrounds | Flowing, chromatic |
| `callout-mod-neon-text.css` | Neon glowing title, bold, italic, and links | Text-focused glow |
| `callout-mod-icon-badge.css` | Circular icon badge with glow ring | Icon-centric |
| `callout-mod-hover-lift.css` | Spring-like elevation on hover, growing shadow | Interactive depth |
| `callout-mod-outlined.css` | No fill — wireframe with colored border only | Minimalist wireframe |
| `callout-mod-brutalist.css` | Harsh thick borders, offset shadow, inverted title | Raw, bold, intentional |
| `callout-mod-inset-shadow.css` | Recessed/carved into page with inner shadow | Inset, debossed |

---

## CSS Variable Reference

### Accent Colors (Section 1 of base)

All stored as raw RGB triplets for `rgba()` usage.

| Variable | Default | Hex | Usage |
|----------|---------|-----|-------|
| `--co-purple` | `149, 0, 255` | `#9500FF` | Primary accent, default fallback |
| `--co-purple-dim` | `119, 0, 204` | `#7700CC` | Muted purple |
| `--co-purple-deep` | `89, 0, 153` | `#590099` | Deep purple |
| `--co-cyan` | `0, 255, 255` | `#00FFFF` | Info, tech concepts |
| `--co-green` | `0, 255, 128` | `#00FF80` | Success, completion |
| `--co-pink` | `255, 0, 220` | `#FF00DC` | Questions, curiosity |
| `--co-blue` | `0, 150, 255` | `#0096FF` | Examples, exercises |
| `--co-amber` | `255, 183, 0` | `#FFB700` | Warnings, caution |
| `--co-red` | `255, 0, 68` | `#FF0044` | Danger, errors |
| `--co-orange` | `255, 119, 0` | `#FF7700` | Projects, tasks |
| `--co-teal` | `0, 204, 163` | `#00CCA3` | Research, reading |
| `--co-lavender` | `160, 140, 255` | `#A08CFF` | Communication |
| `--co-steel` | `102, 136, 170` | `#6688AA` | Meta, system |
| `--co-gold` | `204, 170, 68` | `#CCAA44` | Navigation, structure |
| `--co-lime` | `180, 255, 0` | `#B4FF00` | Highlights |
| `--co-coral` | `255, 100, 100` | `#FF6464` | Soft alerts |

### Surface & Text Colors

| Variable | Default | Purpose |
|----------|---------|---------|
| `--co-bg` | `10, 10, 10` | Rich black background |
| `--co-surface` | `18, 18, 18` | Elevated surface |
| `--co-surface-2` | `26, 26, 26` | Second surface |
| `--co-surface-3` | `34, 34, 34` | Third surface |
| `--co-border` | `42, 42, 42` | Default border |
| `--co-text` | `224, 224, 224` | Primary text |
| `--co-text-dim` | `160, 160, 160` | Secondary text |
| `--co-text-muted` | `100, 100, 100` | Muted text |

### Structural Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `--co-radius` | `8px` | Default border radius |
| `--co-radius-lg` | `14px` | Large radius (glass, gradient) |
| `--co-radius-sm` | `4px` | Small radius |
| `--co-border-width` | `3px` | Default border width |
| `--co-icon-size` | `20px` | Icon dimensions |
| `--co-speed` | `0.3s` | Standard transition duration |
| `--co-speed-fast` | `0.15s` | Fast transitions |
| `--co-speed-slow` | `0.5s` | Slow transitions |
| `--co-ease` | `cubic-bezier(0.4, 0, 0.2, 1)` | Standard easing |

### Animation Keyframes (defined in base, used by mods)

| Keyframe | Effect | Used By |
|----------|--------|---------|
| `co-glow-pulse` | Gentle opacity pulse | neon-glow, terminal |
| `co-neon-flicker` | Neon sign flicker | neon-glow |
| `co-fade-in` | Fade in with subtle scale | base |
| `co-slide-in` | Slide from left | base |
| `co-gradient-pan` | Animated background pan | gradient-shift |
| `co-scanline` | Scanline sweep | cyberpunk |
| `co-border-breathe` | Border opacity breathe | edge-glow, neon-glow |
| `co-icon-spin` | Full rotation | available for custom use |
| `co-hue-rotate` | Hue shift animation | available for custom use |

---

## How to Change Accent Colors

Open `callout-base.css` Section 1. Change any RGB triplet:

```css
/* Before: Electric Purple */
--co-purple: 149, 0, 255;

/* After: Custom Blue-Violet */
--co-purple: 100, 50, 230;
```

All callout types and mods using that variable automatically update.

---

## How to Reassign Callout Type Colors

Open `callout-base.css` Section 5. Find the callout type and change its group:

```css
/* Move "example" from blue group to green group */
/* Find in blue group and remove, then add to green group: */

.callout[data-callout="example"] {
  --callout-color: var(--co-green);  /* was --co-blue */
}
```

---

## How to Create a New Mod

1. Create `callout-mod-[your-name].css` in the snippets folder
2. Follow this template:

```css
@charset "UTF-8";
/*
╔═══════════════════════════════════════════════════════════════╗
║  CALLOUT MOD: Your Name                                       ║
║  Brief description of the effect                              ║
║  REQUIRES: callout-base.css enabled                           ║
╚═══════════════════════════════════════════════════════════════╝
*/

/* --- Container --- */
.callout {
  background: ... !important;
  border: ... !important;
  border-radius: ... !important;
  box-shadow: ... !important;
}

.callout:hover { ... }

/* --- Title --- */
.callout-title {
  background: ... !important;
  color: rgb(var(--callout-color)) !important;
}

/* --- Content --- */
.callout-content {
  padding: ... !important;
  color: rgba(var(--co-text), 0.9) !important;
}

/* --- Icon --- */
.callout-icon { ... }

/* --- Bold text accent --- */
.callout-content strong,
.callout-content b {
  color: rgb(var(--callout-color)) !important;
}

/* --- Nested --- */
.callout .callout { ... }
```

**Key rules for mods:**
- Use `!important` on every property to override the base
- Use `var(--callout-color)` for dynamic per-callout theming
- Use `var(--co-*)` variables for consistent colors/spacing
- Reference `co-*` keyframes for animations
- Include `:hover` states
- Handle `.callout .callout` for nested callouts
- Add `@media (prefers-reduced-motion)` if animations are used

---

## Naming Conventions

| Pattern | Example | Purpose |
|---------|---------|---------|
| `callout-base.css` | — | Foundation (only one) |
| `callout-mod-[name].css` | `callout-mod-neon-glow.css` | Visual mod |
| `--co-[color]` | `--co-purple` | Accent color variable |
| `--co-[property]` | `--co-radius` | Structural variable |
| `co-[name]` | `co-glow-pulse` | Animation keyframe |

---

## Color Assignment Groups (Section 5 of base)

| Group | Color Variable | Callout Types |
|-------|---------------|---------------|
| Purple Core | `--co-purple` | definition, concept, abstract, info, note, principle, etc. |
| Cyan (Info) | `--co-cyan` | tip, hint, helpful-tip, how-to, best-practice, recipe, etc. |
| Green (Success) | `--co-green` | success, check, done, complete, win, finding, proof, etc. |
| Amber (Warning) | `--co-amber` | warning, caution, attention, important, alert, constraints, etc. |
| Red (Danger) | `--co-red` | danger, error, bug, failure, critical, bug-report, etc. |
| Pink (Questions) | `--co-pink` | question, help, faq, what-if, quiz, ask-yourself, etc. |
| Blue (Examples) | `--co-blue` | example, code, experiment, exercise, flashcard, etc. |
| Teal (Research) | `--co-teal` | research, analysis, review, study, data, stats, etc. |
| Orange (Projects) | `--co-orange` | project, task, todo, workflow, plan, milestone, etc. |
| Lavender (Comm) | `--co-lavender` | meeting, decision, feedback, progress, methodology, etc. |
| Steel (Meta) | `--co-steel` | system, meta, debug, config, admin, plugin, etc. |
| Gold (Navigation) | `--co-gold` | toc, navigation, key-points, highlight, related, etc. |
| Coral (Quotes) | `--co-coral` | quote, cite, source, bibliography, acknowledgments, etc. |
| Deep Purple (Analysis) | `--co-purple-deep` | key-claim, evidence, counter-argument, hypothesis, etc. |
| Lime (Creativity) | `--co-lime` | idea, brainstorm, insight, discovery, learning, etc. |

---

## Legacy Files (from previous system)

The following files are from the previous fragmented system and can be disabled if the new base+mod system is active:

- `pur3v4d3r-ultimate-callout-system.css` — Old v5.0 monolithic system
- `unified-callout-system.css` — Old v3.0 design token system
- `dark-shadow-callout-system.css` — Old v3.0 dark system
- `callout-mod-neon.css` — Old neon mod (replaced by `callout-mod-neon-glow.css`)
- `callout-mod-card.css` — Old card mod (replaced by `callout-mod-card-premium.css`)
- `callout-mod-raised.css` — Old raised mod (covered by hover-lift/card-premium)
- `callout-mod-15-premium-card.css` — Old numbered mod (replaced by card-premium)
- `callout-mod-16-floating-light.css` — Old numbered mod (replaced by card-floating)
- `callout-mod-12-icon-style-variations.css` — Old icon mod (replaced by icon-badge)
- `callout-icon.css` — Old icon styling

---

## LLM Session Onboarding

When starting a new LLM session to work on this callout system, provide:

1. **This README** — for architecture, variable reference, and naming conventions
2. **callout-base.css** — for the full variable definitions and color assignments
3. **The specific mod file** being discussed — for current visual treatment

**Key facts for LLMs:**
- All colors are raw RGB triplets, not hex — used as `rgba(var(--co-purple), 0.5)`
- The bridge variable is `--callout-color` — set by the base per callout type, consumed by mods
- Mods must use `!important` on everything to override base
- Selectors target: `.callout`, `.callout-title`, `.callout-content`, `.callout-icon`
- Pseudo-elements: `::before` and `::after` are available on `.callout` for accents/effects
- Hover states: always define `.callout:hover` overrides
- Nested callouts: always handle `.callout .callout` for reduced intensity
- Reduced motion: use `@media (prefers-reduced-motion: reduce)` where animations exist
- The user has 250+ custom callout types — mods must work on ALL callouts, not just specific types
