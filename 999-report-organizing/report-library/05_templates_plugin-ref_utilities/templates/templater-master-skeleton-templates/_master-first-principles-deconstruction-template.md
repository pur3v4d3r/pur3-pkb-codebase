<%*
/* ---------------------------------------------------------------
   FIRST PRINCIPLES DECONSTRUCTION
   Use this for: Physics, Optics, Complex Systems
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: DOMAINS ---
const domains = [
    "Physics / Astrophysics", 
    "Optics / Light", 
    "Cognitive Science", 
    "Philosophy", 
    "System Architecture"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Concept to Deconstruct:");
const domain = await tp.system.suggester(domains, domains, false, "Primary Domain:");
_%>
---
type: "concept-deconstruction"
model: "first-principles"
domain: "<% domain %>"
status: "In-Progress"
tags:
  - "learning/first-principles"
  - "domain/<% domain.split(" / ")[0].toLowerCase() %>"
---
# ⚛️ <% title %>
## 1. The Surface Level (The "What")
*How is this concept generally understood or defined?*
> [!quote] Standard Definition
> 
## 2. The Recursive "Why" (Deconstruction)
*Ask "Why?" five times to break the assumption.*
1. **Why does X happen?** * *Because…*
2. **Why is that true?** * *Because…*
3. **Why?** * *Because…*
## 3. The Bedrock Truths (Axioms)
*What are the fundamental, irreducible facts remaining? (Use LaTeX for physics)*
* **Fact A**: $$ E = mc^2 $$
* **Fact B**: 
## 4. Reconstruction (The Build)
*Re-derive the concept from the axioms above without using analogies.*
## 5. The Feynman Test
> [!check] Simplify
> *Explain this concept to a 12-year-old using the reconstructed logic above.*