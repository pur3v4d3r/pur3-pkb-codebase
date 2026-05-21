
```
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
.markdown-preview-view hr {
  border: none;
  border-top: 1px solid var(--text-faint);
  opacity: 0.5;
  margin: 2em 0;
}

/* ═══════════════════════════════════════════════════════════
   OPTION 2: Signature Purple Gradient
   Pur3v4d3r's purple-to-teal gradient
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  height: 2px;
  background: linear-gradient(90deg, #7800F4 0%, #72FFF1 100%);
  margin: 2.5em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 3: Dotted Separator
   Subtle dotted line
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  border-top: 3px dotted var(--text-muted);
  opacity: 0.6;
  margin: 2em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 4: Dashed Line
   Professional dashed separator
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  border-top: 2px dashed var(--text-normal);
  opacity: 0.4;
  margin: 2em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 5: Double Line
   Classic double border
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  border-top: 3px double var(--text-muted);
  opacity: 0.7;
  margin: 2em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 6: Centered Decorative Dots
   Three centered dots (ellipsis style)
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  text-align: center;
  height: 1em;
  position: relative;
  margin: 2.5em 0;
}

.markdown-preview-view hr::before {
  content: '• • •';
  color: var(--text-muted);
  font-size: 1.5em;
  letter-spacing: 1em;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 7: Centered Diamond
   Single centered decorative diamond
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  text-align: center;
  height: 1em;
  position: relative;
  margin: 2.5em 0;
}

.markdown-preview-view hr::before {
  content: '◆';
  color: #7800F4;
  font-size: 1.2em;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 8: Thick Accent Bar
   Bold, prominent divider
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  height: 4px;
  background-color: var(--interactive-accent);
  margin: 3em 0;
  border-radius: 2px;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 9: Fade-Out Gradient
   Edges fade to transparent
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  height: 2px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    var(--text-muted) 20%,
    var(--text-muted) 80%,
    transparent 100%
  );
  margin: 2.5em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 10: Centered Short Line
   Short centered rule (50% width)
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
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
/* .markdown-preview-view hr {
  border: none;
  height: 2px;
  background-color: #7800F4;
  box-shadow: 0 0 10px #7800F4, 0 0 20px rgba(120, 0, 244, 0.5);
  margin: 2.5em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 12: Neon Teal Glow
   Cyberpunk-style teal glow
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  height: 2px;
  background-color: #72FFF1;
  box-shadow: 0 0 8px #72FFF1, 0 0 15px rgba(114, 255, 241, 0.6);
  margin: 2.5em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 13: Wave Pattern (SVG)
   Decorative wave border
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  height: 15px;
  background-image: url("data:image/svg+xml,%3Csvg width='100' height='20' viewBox='0 0 100 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 10 Q 25 0, 50 10 T 100 10' stroke='%237800F4' stroke-width='2' fill='none'/%3E%3C/svg%3E");
  background-repeat: repeat-x;
  background-size: 100px 20px;
  margin: 2.5em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 14: Inset Shadow Style
   Appears carved into the page
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  height: 2px;
  background-color: transparent;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.3);
  margin: 2em 0;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 15: Rainbow Spectrum
   Full spectrum gradient
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  height: 3px;
  background: linear-gradient(
    90deg,
    #FF0080 0%,
    #FF0000 16.67%,
    #FFC700 33.33%,
    #00FF00 50%,
    #72FFF1 66.67%,
    #7800F4 83.33%,
    #FF0080 100%
  );
  margin: 2.5em 0;
  border-radius: 1.5px;
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 16: Ornamental (Stars)
   Decorative star pattern
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  text-align: center;
  height: 1em;
  position: relative;
  margin: 2.5em 0;
}

.markdown-preview-view hr::before {
  content: '✦ ✦ ✦';
  color: #FFC700;
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
/* @keyframes hr-pulse {
  0%, 100% { 
    box-shadow: 0 0 5px rgba(120, 0, 244, 0.5); 
  }
  50% { 
    box-shadow: 0 0 15px rgba(120, 0, 244, 0.8), 0 0 25px rgba(120, 0, 244, 0.4); 
  }
}

.markdown-preview-view hr {
  border: none;
  height: 2px;
  background-color: #7800F4;
  margin: 2.5em 0;
  animation: hr-pulse 3s ease-in-out infinite;
}

@media (prefers-reduced-motion: reduce) {
  .markdown-preview-view hr {
    animation: none;
    box-shadow: 0 0 5px rgba(120, 0, 244, 0.5);
  }
} */

/* ═══════════════════════════════════════════════════════════
   OPTION 18: Zig-Zag Pattern
   Geometric zig-zag border
   ═══════════════════════════════════════════════════════════ */
/* .markdown-preview-view hr {
  border: none;
  height: 10px;
  background: linear-gradient(135deg, transparent 33.33%, var(--text-muted) 33.33%, var(--text-muted) 66.66%, transparent 66.66%),
              linear-gradient(45deg, transparent 33.33%, var(--text-muted) 33.33%, var(--text-muted) 66.66%, transparent 66.66%);
  background-size: 20px 20px;
  background-position: 0 0, 10px 0;
  margin: 2.5em 0;
  opacity: 0.6;
} */
```