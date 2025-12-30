---
aliases:
  - Project
  - "Project: Prompt Engineering"
  - Project Prompt Engineering
  - Long Output Project
  - Prompt Engineering Project
tags:
---



> [!lift] Project: Prompt-Engineering -> Long-Output
> ContentsThis is the starting note for a project. The project is about generating higher quality output from LLMs. Particularly learning and designing a new workflow to use for generating educational material.



<span style='color: #ff0000;'>Project -> Prompt Engineering: Long Output</span>

<span style='color: #FF6B6B; background-color: #FFE5E5; padding: 3px 8px; border-radius: 4px; font-weight: 500; border-left: 3px solid #FF6B6B;'>Items to Create</span>
- Check list for brevity before running prompts.
	- And for review.
- Check list for during Sessions.
- Pedagogical Scaffolds updated with new semantic triggers.






















> [!nexus]  **Least-to-Most Prompting (Decomposition)**
> 
> 
> This is the "Staged Generation" approach referenced previously. It addresses the [[Output Token Limit]] by breaking a large asset into constituent atomic units.
> 
> [**Least-to-Most-Prompting**:: A technique where a complex problem is decomposed into a list of sub-problems, which are then solved sequentially, with the solution to previous sub-problems fed into the context for the next.]
> > [!elevated] Protocol: The Sequential Build
> >**Step 1: The Decomposition**
> > Ask the model to break the topic into 5-7 distinct, logically ordered sub-topics.
> >
> > **Step 2: The Isolate Generation**
> > Prompt: *"Draft Section 1: [Topic Name]. Focus strictly on this scope. Do not summarize other sections. Use 800 words."*
> >
> > **Step 3: The Context Carryover**
> > Prompt: *"Reference the content of Section 1 above. Now, draft Section 2: [Topic Name]. Ensure logical flow from Section 1, but treat this as a standalone deep dive."*
> >
> > **Step 4: The Final Assembly**
> > (performed by the user in [[Obsidian]]): Stitch the distinct outputs into one master note.

>[!nexus] **Chain-of-Verification (CoVe)**
> 
> 
> Use this when accuracy and lack of [[Hallucination]] are paramount. This method forces the model to doubt its own output before finalizing it.
> 
> [**Chain-of-Verification**:: A prompting pattern where the model generates a baseline response, generates verification questions to check that response, answers those questions independently, and then generates a final verified response.
> > [!elevated] CoVe in Practice
> > **Turn 1 (Draft):** "Write a technical explanation of [[Transformer Architecture]]."
> > **Turn 2 (Critique):** "Review the text above. Identify 4 potential inaccuracies, simplifications, or missing mathematical context. List them as bullet points."
> > **Turn 3 (Correction):** "Using the critique above, rewrite the explanation. Expand on the missing math and correct the simplifications."
> 
> By forcing the "Critique" step, you activate a different set of weights—the model acts as an *editor* rather than a *writer*, often catching errors it made just seconds prior.

> [!nexus] Advanced Technique: **The Recursive Expansion Loop**
> 
> For your specific goal—generating massive, high-density reports—you need the **Recursive Expansion Loop**. This technique takes a "finished" section and explodes it into a new note, recursively.
> 
> > [!elevated] Workflow: Expanding the "Tiny Fraction"
> > 1.  **Initial Generation:** Get the model to generate a standard summary (the "tiny fraction" you are currently getting).
> > 2.  **The Target Selection:** Copy *one specific paragraph* from that summary that contains high-value density.
> > 3.  **The Explosion Prompt:**
> >     *"Take the paragraph quoted below. This is now the 'Abstract' for a new, detailed 1,000-word section. Explode this single paragraph into a comprehensive technical guide. Do not repeat the abstract; expand upon it."*
> > 4.  **Repeat:** Do this for every paragraph in the original summary.
>
> This turns a 500-word summary into five 1,000-word chapters.

> [!nexus] Semantic Anchoring for Iteration
> 
> When iterating, the model often loses track of formatting instructions (the "drift"). You must re-anchor the constraints in every single prompt of the chain.
> > [!critical] The Context Dilution Pitfall
> > As the conversation grows longer (hitting 10k, 20k tokens), the model's adherence to instructions given at the very start (Turn 1) weakens.

>[!nexus] The "System Reminders"
> 
> In every iterative turn, append a footer to your prompt:
> 
> ```markdown
> ---
> REMINDER:
> - Tone: Academic, rigorous.
> - Format: Strict Markdown.
> - Meta-Data: Include [[Wiki-Links]] for all technical terms.
> - Forbidden: Do not summarize.
> ---
> ```
> 
> [**Prompt-Injection-Footer**:: A repetitive block of text appended to every prompt in a chain to refresh the model's 'working memory' regarding constraints and formatting rules.]












