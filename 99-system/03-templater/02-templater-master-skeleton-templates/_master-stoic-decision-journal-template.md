<%*
/* ---------------------------------------------------------------
   STOIC DECISION JOURNAL
   Use this for: Anxiety processing, Decision making, Reflection
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: STOIC LENS ---
const philosophers = [
    "Epictetus (Control)", 
    "Marcus Aurelius (Duty)", 
    "Seneca (Time/Anger)"
];
// --- INPUT PROMPTS ---
const situation = await tp.system.prompt("Situation / Event:");
const lens = await tp.system.suggester(philosophers, philosophers, false, "Philosophical Lens:");
_%>
---
type: "journal/stoic"
lens: "<% lens %>"
date: "<% tp.date.now("YYYY-MM-DD") %>"
tags:
  - "philosophy/stoicism"
  - "practice/journaling"
---

# 🏛️ Stoic Reflection: <% situation %>

> *"Some things are in our control and others not."* — Epictetus

## The Dichotomy of Control

### 🔴 Not In My Control (Externals)
*What elements here are dictated by fate, others, or nature?*
* [ ] The outcome of…
* [ ] Other people's opinions of…
* [ ] The past events…

### 🟢 In My Control (Internals)
*What are my reasoned choices?*
* [ ] My judgment of the event.
* [ ] My preparation.
* [ ] My integrity and character.

## Premeditatio Malorum (Negative Visualization)
*What is the worst-case scenario, and how will I endure it?*
> **Worst Case:** > **My Response:** I will accept it as nature's will and focus on…

## The View from Above
*Zoom out. How significant is this event in the context of the cosmos or a lifetime?*

---
**Actionable Virtue:** what is the *one* right thing to do right now?