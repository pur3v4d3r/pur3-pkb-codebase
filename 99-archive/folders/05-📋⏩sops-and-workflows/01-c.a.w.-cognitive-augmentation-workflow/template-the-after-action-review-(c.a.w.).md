---
title: Template_The-After-Action-Review_(C.A.W.)
aliases:
  - AAR Prompt Template
  - LLM Experiment Analysis
  - Post-Generation Review Template
  - The-After-Action-Review-(AAR)-Prompt-Template_CAG
tags:
  - prompt-engineering
  - cognitive-science
  - pkm
status: 🪴 seedling
created: 2025-10-09T05:41:55.007Z
updated: 2025-10-09T05:43:14.198Z
source: "[Gemini-2.5-Flash]"
related:
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[report_the-cognitive-augmentation-workflow_(c.a.w.)]]"
date created: 2025-10-09T01:41:55.000-04:00
date modified: 2025-10-10T00:19:45.310-04:00
---

# The-After-Action-Review-(AAR)-Prompt-Template_CAG

**The After Action Review (AAR) Prompt Template**

> [!the-purpose]
> This reference material is an actionable template for **Phase IV: Conceptual Integration**. It operationalizes the continuous learning loop, helping you capture **tacit knowledge** by analyzing failure and success.

```
## **Template: Post-Generation AAR for LLM Workflow**

**Goal:** Treat the prompt and generation as a scientific experiment. Use this to identify failure modes and improve future prompts.

**A. Execution Summary**

- **Note Title:** `[[LLM Note Title]]`
    
- **Original Prompt URL/Link:** `[[Link to the Prompt Template/File]]`
    
- **Actual Outcome Metrics:**
    
    - `semantic_density:` (Was it above threshold? Y/N)
        
    - `coherence_score:`
        
    - `citation_check_status:` (Final Status)

**B. The Review Questions (The Core Analysis)**

1. **Intended Outcome:** What was the ideal, non-negotiable outcome defined in the initial Meta Prompt?
    
2. **Actual Outcome:** What was actually delivered by the LLM (based on the final report and metrics)?
    
3. **Cause of Difference (The Gap Analysis):** Why did the outcome fail to meet the intent? _Check all that apply and detail:_
    
    - `[ ]` **Low Semantic Density:** The LLM failed to deeply synthesize or ground the required evidence. _Cause:_ (E.g., RAG corpus was insufficient; ToT process was rushed.)
        
    - `[ ]` **Constraint Failure:** The LLM violated a System Role constraint (e.g., tone, format). _Cause:_ (E.g., Negative constraint was used; constraint was too ambiguous.)
        
    - `[ ]` **RAG Failure:** Cited material was either fictional (Hallucination) or factually incorrect despite grounding. _Cause:_ (E.g., Source material was poor; LLM misused source chunk.)
        
    - `[ ]` **Conceptual Gap:** The LLM missed a critical element or failed to question an obvious counter-argument (Review non-chosen ToT branches). _Detail:_

**C. Iteration and Application**

1. **Lessons Learned:** What is the primary, general lesson learned about the LLM's behavior or my prompt construction?
    
2. **Next Action/Hypothesis:** Based on the analysis, formulate the exact change for the next iteration.
    
    - `[ ]` **New Prompt Directive:** (e.g., _Add negative constraint against focusing on X._)
        
    - `[ ]` **New Research Hypothesis:** (The finding that needs to be explored next.)
        
    - `[ ]` **Personal Knowledge Base Fix:** (New linking or CMS action required

```
