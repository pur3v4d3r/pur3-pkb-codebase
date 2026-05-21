# [snippet] Index

---
## Full Gradient Background
```
/* --- Snippet: Active Line - Full Gradient --- */
/* CSS: Applies a 3-color gradient to the active line's background. */
/* Affects: .cm-line.cm-active */

/* Define RGB versions of your colors for rgba() */
:root {
  --theme-purple-rgb: 120, 0, 244;
  --theme-gold-rgb: 255, 199, 0;
  --theme-teal-rgb: 114, 255, 241;
}

/* This is the CORRECT selector from your log! 
  We target the .active-line-on body class and the .cm-active line class.
*/
body.active-line-on .markdown-source-view.mod-cm6 .cm-line.cm-active {
  
  /* 1. Set a fallback background color */
  background-color: #1A1B1E !important;
  
  /* 2. Apply your 3-color gradient with 20% opacity */
  background-image: linear-gradient(
    90deg, 
    rgba(var(--theme-purple-rgb), 0.2), 
    rgba(var(--theme-gold-rgb), 0.2), 
    rgba(var(--theme-teal-rgb), 0.2)
  ) !important;
  
  /* 3. CRITICAL: Disable the theme's box-shadow "wings" */
  box-shadow: none !important; 

  /* 4. Clean up the appearance */
  background-size: 100% !important; 
  border-radius: 4px !important;

  /* 5. Make text bolder for readability */
  font-weight: 600 !important;
}
```

### Gradient Underline
```
/* --- Snippet: Active Line - Gradient Underline (V4 - CORRECTED) --- */
/* CSS: Applies a 3-color gradient as an underline to the active line's text. */
/* Affects: .cm-line.cm-active */

body.active-line-on .markdown-source-view.mod-cm6 .cm-line.cm-active {
  /* 1. We still set a slightly lighter background for clarity */
  background-color: #1A1B1E !important; 
  
  /* 2. This is the gradient underline */
  background-image: linear-gradient(
    to right, 
    var(--theme-purple), 
    var(--theme-gold), 
    var(--theme-teal)
  ) !important;
  
  /* 3. Position the gradient at the bottom */
  background-position: 0 100% !important;
  
  /* 4. Make it a 2px high line */
  background-size: 100% 2px !important; 
  
  /* 5. Don't repeat the gradient */
  background-repeat: no-repeat !important;

  /* 6. CRITICAL: Disable the theme's box-shadow "wings" */
  box-shadow: none !important; 
  border-radius: 4px !important;
}
```



### Horizontal Rules
```
/* -- HORIZONTAL RULES -- */
/* We replace the default <hr> line with an elegant, fading gradient. */
hr {
  height: 2px;
  border: none;                                /* Remove the default border */
  background: linear-gradient(
    to right,
    transparent,
    #ffc800,                                  /* Our primary accent blue in the center */
    transparent
  );
  margin-top: 2.5em;                           /* Give it some vertical space */
  margin-bottom: 2.5em;
}
/* End of Snippet */
```

### Gradient Horizontal Line
```
/* -- HORIZONTAL RULES -- */
/* We replace the default <hr> line with an elegant, fading gradient. */
hr {
  height: 2px;
  border: none;                                /* Remove the default border */
  background: linear-gradient(
    to right,
    transparent,                                /* Start with transparency */
    #9E6AD3,                                   /* Our primary accent purple on the left */
    #FFC700,                                   /* Transition to gold in the center */
    #2DD4BF,                                   /* End with teal on the right */     
    transparent                                 /* Fade back to transparency */
  );
  margin-top: 2.5em;                           /* Give it some vertical space */
  margin-bottom: 2.5em;
}
```

### Metadata Container
```
/* ---  A "Metadata Container" for Properties --- */
/* Style the main container for the properties */
.metadata-container {
  background-color: rgba(158, 106, 211, 0.3); /* */
  border: 2px solid var(--theme-gold); /* Warm Amber Gold border */
  border-radius: 10px; /* Rounded corners */
  padding: 12px 16px; /* Inner padding */
  margin: 16px 0; /* Vertical spacing */
  box-shadow: 0 4px 8px rgba(158, 106, 211, 0.2); /* Subtle shadow */ 

  font-family: 'JetBrains Mono', monospace; /* Monospaced font */
  font-size: 0.9em; /* Slightly smaller font size */
  color: var(--tx1); /* Use theme's primary text color */
  line-height: 1.4; /* Improved line spacing */
  
  transition: background-color 0.3s ease, border-color 0.3s ease; /* Smooth transitions */
}
.metadata-container:hover {
  background-color: rgba(158, 106, 211, 0.5); /* Slightly more opaque on hover */
  border-color: var(--theme-teal); /* Change border color on hover */
}
```


```
/* --- Snippet: Metadata Container Styling --- */
/* CSS: Styles the metadata container with a frosted glass effect and thematic colors. */ 
/* Style the main container for the properties */
.cm-content .metadata-container,
.markdown-preview-view .metadata-container {
  background-color: rgba(30, 30, 30, 0.6) !important; /* Semi-transparent dark background */
  border: 1px solid rgba(255, 199, 0, 0.3) !important; /* Semi-transparent gold border */
  border-radius: 8px !important;
  padding: 12px 18px !important;
  margin-bottom: 32px !important; /* Add some nice space before the content begins */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important; /* Subtle shadow for depth */
  position: relative !important;
  font-family: 'JetBrains Mono', monospace !important; /* Monospaced font for a techy look */
  font-size: 0.9em !important; /* Slightly smaller text for a compact feel */
  color: #FFFFFF !important; /* Bright white text for contrast */
  -webkit-backdrop-filter: blur(8px) !important; /* Frosted glass effect */
  backdrop-filter: blur(8px) !important; /* Frosted glass effect for Safari */
  transition: background-color 0.3s ease, border-color 0.3s ease-in-out !important;
} /* <-- This closing brace was moved */
```


```
/* --- Snippet: Active Line - Gradient Underline for Obsidian's CodeMirror Editor --- */
/* CSS: Applies a 3-color gradient as an underline to the active line's text.

/* Affects: .cm-line.cm-active (active line in editing mode, not preview mode) */

body.active-line-on .markdown-source-view.mod-cm6 .cm-line.cm-active {
  /* 1. We still set a slightly lighter background for clarity */
  background-color: #1A1B1E; 
  
  /* 2. This is the gradient underline */
  background-image: linear-gradient(
    to right, 
    var(--theme-purple, #9E6AD3), 
    var(--theme-gold, #FFC700),
    var(--theme-teal, #72FFF1)
  ) !important;
  
  background-position: 0 100% !important;
  background-size: 100% 2px !important; 
  background-repeat: no-repeat !important;
  
  border-bottom: none !important; /* Remove any existing underline */
  
  box-shadow: none !important; /* Remove any existing shadow */
}
```