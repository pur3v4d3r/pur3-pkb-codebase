<%*
/* ═══════════════════════════════════════════════════════════════════════════
   FRISCO QUICK ANALYSIS TEMPLATE  v1.0.0
   ─────────────────────────────────────────────────────────────────────────
   PURPOSE  Rapid 5-10 minute argument evaluation using Ennis's FRISCO model.
            Use when full Paul-Elder is overkill but you still need structure.
   PLACEMENT  03-notes/critical-thinking-practice/
   ═══════════════════════════════════════════════════════════════════════════ */
const subject = await tp.system.prompt("What argument/claim are you evaluating?");
if (!subject) return;
const source = await tp.system.prompt("Source (URL / book / person / 'self')", "self");
const slug   = subject.toLowerCase().replace(/[^a-z0-9\s-]/g,"").replace(/\s+/g,"-").slice(0,50);
const fname  = `${tp.date.now("YYYY-MM-DD")}_frisco_${slug}`;
await tp.file.rename(fname);
await tp.file.move(`/03-notes/critical-thinking-practice/${fname}`);
tR += "";
%>---
title: "FRISCO: <% subject %>"
aliases: []
tags:
  - critical-thinking
  - frisco
  - ennis
  - argument-analysis
  - deliberate-practice
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
type: critical-thinking-session
framework: frisco
source: "<% source %>"
status: in-progress
verdict: 
related: []
---

# FRISCO: <% subject %>

> [!abstract] FRISCO Quick Analysis
> Six-step argument evaluation from [[Robert Ennis|Ennis]]'s [[FRISCO Model]]. Target: 5-10 minutes. Each step gets ≤3 sentences. Force concision.

**Source:** <% source %>

---

## F · Focus

> *What is the main question, conclusion, or issue?*

[**Focus**:: ]

> 

---

## R · Reasons

> *What reasons are offered in support?*

[**Reason-1**:: ]
[**Reason-2**:: ]
[**Reason-3**:: ]

1. 
2. 
3. 

---

## I · Inference

> *Is the reasoning from those reasons to the conclusion acceptable?*

**Inference type:** `INPUT[inlineSelect(option(deductive), option(inductive), option(abductive), option(analogical), option(causal)):inference-type]`

**Quality assessment:**
- [ ] Premises actually support the conclusion
- [ ] No major [[Logical Fallacies|fallacies]] present
- [ ] Strength of conclusion is appropriately hedged

[**Inference-Verdict**:: ]

> 

---

## S · Situation

> *What is the context — physical, social, intellectual — that frames this argument?*

[**Context**:: ]

> 

---

## C · Clarity

> *Are the meanings of key terms clear?*

**Unclear or contested terms:**
- **Term:** → working definition: 
- **Term:** → working definition: 

---

## O · Overview

> *Step back: does the reasoning hold up under integrated review?*

**Verdict:** `INPUT[inlineSelect(option(sound), option(mostly-sound), option(questionable), option(unsound)):verdict]`

[**Final-Verdict**:: ]

> 

---

## ⚙ Metacognitive Check (mandatory, 60 seconds)

- What was I *inclined* to conclude before analyzing?
  > 
- Did the analysis change my conclusion? Why or why not?
  > 
- What [[Cognitive Biases|bias]] was I most at risk of in this session?
  > 

---

# 🔗 Related

- [[FRISCO Model]]
- [[Critical Thinking Practice MOC]]
- [[Argument Analysis]]
