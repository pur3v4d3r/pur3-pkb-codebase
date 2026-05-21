<%*
/* SEE-I ELABORATION TEMPLATE  v1.0.0
   Use for: concept clarification, vocabulary mastery, exam prep,
   testing whether you truly understand an idea. Target: 10-15 min. */
const concept = await tp.system.prompt("Concept to elaborate?");
if (!concept) return;
const slug = concept.toLowerCase().replace(/[^a-z0-9\s-]/g,"").replace(/\s+/g,"-").slice(0,50);
const fname = `${tp.date.now("YYYY-MM-DD")}_see-i_${slug}`;
await tp.file.rename(fname);
await tp.file.move(`/03-notes/critical-thinking-practice/${fname}`);
tR += "";
%>---
title: "SEE-I: <% concept %>"
aliases: []
tags:
  - critical-thinking
  - see-i
  - paul-elder
  - concept-elaboration
  - deliberate-practice
  - learning
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
type: critical-thinking-session
framework: see-i
concept: "<% concept %>"
status: in-progress
mastery-self-rating: 
related: []
---

# SEE-I: <% concept %>

> [!definition] [[SEE-I Method]]
> A four-step elaboration tool from the [[Paul-Elder Framework]]. **S**tate it · **E**laborate it · **E**xemplify it · **I**llustrate it. If you cannot do all four, you do not yet understand the concept — you only recognize the words.

---

## S · STATE

> *State the concept clearly in **one** sentence. No jargon ladders.*

[**Statement**:: ]

> 

---

## E · ELABORATE

> *Explain it in your own words, in depth. ~150 words. Cover: what it includes, what it excludes, why it matters.*

> 

---

## E · EXEMPLIFY

> *Provide **two** concrete examples. At least one should be from a domain different from where you first learned the concept (transfer test).*

**Example 1 (familiar domain):**
> 

**Example 2 (different domain — transfer test):**
> 

**Counter-example (something that LOOKS like this concept but isn't):**
> 

---

## I · ILLUSTRATE

> *Use an analogy, metaphor, or visual to make the concept vivid.*

**Analogy:**  "<% concept %> is like ____ because ____ ."
> 

**(Optional) Visual / Mermaid diagram:**
```mermaid
%% Sketch the concept's structure visually
```

---

## 🧠 Mastery Self-Check

| Question | Answer |
|---|---|
| Could I teach this to a smart 12-year-old? | `INPUT[toggle:can-teach-12]` |
| Could I distinguish it from 2 commonly-confused concepts? | `INPUT[toggle:can-distinguish]` |
| Could I apply it to a novel case? | `INPUT[toggle:can-transfer]` |
| Can I name the [[Paul-Elder Framework|Paul-Elder]] element this concept belongs to? | `INPUT[toggle:knows-element]` |

**Commonly-confused concepts (and the distinction):**
- **<% concept %>** vs. **___** → 
- **<% concept %>** vs. **___** → 

**Mastery rating (1-5):** `INPUT[slider(minValue(1), maxValue(5), addLabels):mastery-self-rating]`

---

## ⚙ Metacognitive Check

- Which of the four steps was hardest? *(That step reveals where my understanding is weakest.)*
  > 
- What gap did this exercise expose?
  > 
- What further reading/practice would close that gap?
  > 

---

# 🔗 Related

- [[SEE-I Method]]
- [[Paul-Elder Framework]]
- [[Feynman Technique]]
- [[Concept Mastery]]
- [[Critical Thinking Practice MOC]]
