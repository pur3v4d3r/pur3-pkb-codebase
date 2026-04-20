---
title: "Pur3v4d3r's House Style — Canonical Reference"
doc_type: "Reference"
purpose: "Authoritative voice specification for report generation across the PKB"
style_name: "Patient Synthesizer (Figured)"
version: 1.0.0
status: established
maturity: production
created: 2026-04-15
tags:
  - house-style
  - voice
  - prompt-engineering
  - report-generators
  - pkb-infrastructure
  - canonical
related:
  - "[[Writing Style Exemplars for Report Generators]]"
  - "[[House Style Variations Library]]"
  - "[[PKB Report Generator Suite v2.0]]"
  - "[[VADER Academic Report Generator]]"
  - "[[Constitutional Depth Mandate]]"
aliases:
  - "Patient Synthesizer Style"
  - "Personal House Voice"
  - "D2 Style"
---

# Pur3v4d3r's House Style — Canonical Reference

> [!abstract] What This Document Is
> This is the **authoritative specification** of the writing voice to be applied across all generated reports in the [[PKB Report Generator Suite v2.0]]. It was arrived at through a four-round iterative refinement process and represents a converged stylistic preference rather than a generic template. Use this file when you want the canonical version. Use the [[House Style Variations Library]] when you want a version of this voice tuned for a specific section type or affect.

---

## Origin

[Convergence-Path:: Round 1 selected the Crystalline Academic family. Round 2 narrowed to the Patient Synthesizer (Sample B) — cross-paragraph integrative arcs, scholarly register, family-resemblance moves. Round 3 tuned cadence to Mixed-Wave (C2) — long developmental sentences with short release sentences breathing between them. Round 4 settled texture as Figured (D2) — controlled metaphor allowed, used where plain language would only describe.]

The style emerged through deliberate elimination. It is not the most distinctive voice considered, nor the most literary, nor the most efficient. It is the voice that survived four rounds of comparison as the one most worth reading at length.

---

## The Style — Definitive Specification

> [!definition] Patient Synthesizer (Figured)
> A scholarly prose voice characterized by cross-paragraph integrative arcs, mixed-wave cadence with periodic short-sentence relief, and controlled metaphor used to compress ideas into images where plain language would only describe.

### Dimensional Profile

| Dimension | Specification |
|-----------|---------------|
| **Cadence** | Mixed-wave with mid-paragraph relief |
| **Sentence-length profile** | Mean ~22 words; high variance (5–50+); long developmental sentences alternating with short release sentences |
| **Architecture** | Cross-paragraph integrative arcs; the unit of meaning is the paragraph |
| **Register** | Scholarly, confident, willing to qualify where qualification matters |
| **Voice** | Third-person impersonal; no first person; the author is a careful scholar surveying a field, not a personality |
| **Default move** | Synthetic observation → development across long sentences → short release → further development → landing that recasts what was claimed |
| **Signature device** | Family-resemblance / convergent-recognition arguments — drawing together apparently distinct phenomena under a shared architectural commitment |
| **Texture** | One or two well-placed figures per paragraph; controlled metaphor; never flowery; used where plain language would only describe |
| **Affect** | Cool-scholarly default; steady; respectful of the material; not detached |
| **Hedging** | Selective — present where genuine uncertainty warrants it, absent where confidence is justified |

---

## Canonical Exemplar

> [!example] The reference prose for the model to anchor against
> The exemplar below is the longest sustained version of this voice generated during refinement. Use this — not a single paragraph — as the anchor when injecting the style into report generators. More text gives the model more pattern to track.

> Across nearly a century of cognitive research, the concept of the schema has functioned as a kind of theoretical solvent, dissolving the apparent boundaries between phenomena that earlier psychology had treated as distinct and revealing, beneath the surface differences, a shared architectural commitment. The dissolution happened gradually. Bartlett's reconstructive memory, Piaget's developmental assimilation, Schank and Abelson's scripts, Minsky's frames, and Rosch's prototypes do not, on the surface, name the same thing — they emerged from different intellectual traditions and committed themselves to different formal vocabularies that resist easy translation. None of these vocabularies is reducible to the others. And yet the family resemblance among them is striking, sustained across decades of independent theoretical development, and reflects a convergent recognition that cognition is structured by knowledge already in place and that this structure is what makes both perception's economy and perception's distortion possible. The schema, in this sense, is less a discovery than a commitment.
>
> What gives the schema its theoretical reach is the range of phenomena it makes intelligible without strain. Reconstructive memory becomes the predictable behavior of a knowledge structure asked to retrieve what it never fully encoded. Eyewitness misidentification becomes the cost of a categorization system optimized for speed rather than fidelity. Cross-cultural differences in recall, expert blind spots, the stubborn persistence of stereotypes against contradicting evidence — each of these falls into the same explanatory frame, not because the schema construct has been stretched to accommodate them, but because they are the kinds of phenomena one would expect from a cognitive system organized as the schema concept describes. The construct earns its keep by its breadth. The breadth is not coincidence; it is the signature of an idea that cuts at a real joint.
>
> What remains contested is not the existence of schemas but their proper formal characterization, and here the field's century of work has produced more consensus than disagreement only in retrospect. The neural implementations remain partially specified. The relations between schemas and other forms of knowledge representation — semantic networks, distributed representations, the various species of statistical learning — remain matters of active inquiry. But the foundational commitment is no longer in serious dispute. Cognition is structured by knowledge already in place, that structure operates largely beneath awareness, and the structure is what makes minds the strange and useful instruments they are.

---

## Paste-Ready Style Directive

> [!key-claim] This is the production-ready injection block
> Paste this verbatim at the end of your three-line generator input (after Topic, Output Path, and Wiki-Links Path lines). Do not modify the structure. The order matters — directive appears *after* the structural inputs so it remains in the model's recent context as it generates.

```
<style-directive>
Write the prose of this report in the voice demonstrated by the EXEMPLAR below.

VOICE PROFILE:
- Cadence: Mixed-wave. Long developmental sentences (35–50 words, multi-clause) 
  alternating with short release sentences (5–15 words) that let the reader land 
  before the next wave. Mean sentence length around 22 words; deliberately high variance.
- Architecture: Cross-paragraph integrative arcs. The unit of meaning is the paragraph, 
  not the sentence. Paragraphs build toward synthetic claims, often using 
  family-resemblance or convergent-recognition moves to draw apparently distinct 
  phenomena under a shared frame.
- Register: Scholarly but not stiff. Confident enough to make claims; humble enough 
  to qualify them where qualification genuinely matters. Avoid hedging where 
  confidence is justified.
- Texture: One or two well-placed figures per paragraph — controlled metaphor that 
  compresses an idea into an image. Not flowery. Not constant. Used only where 
  plain language would merely describe.
- Voice: Third-person impersonal. NO first person ("I", "we", "our"). The author is 
  a careful scholar surveying a field, not a personality.
- Default move: Synthetic observation → development across long sentences carrying 
  multiple clauses → breathe with a short sentence → develop further → land with a 
  synthesis that recasts what was claimed.

EXEMPLAR:
"""
Across nearly a century of cognitive research, the concept of the schema has 
functioned as a kind of theoretical solvent, dissolving the apparent boundaries 
between phenomena that earlier psychology had treated as distinct and revealing, 
beneath the surface differences, a shared architectural commitment. The 
dissolution happened gradually. Bartlett's reconstructive memory, Piaget's 
developmental assimilation, Schank and Abelson's scripts, Minsky's frames, and 
Rosch's prototypes do not, on the surface, name the same thing — they emerged 
from different intellectual traditions and committed themselves to different 
formal vocabularies that resist easy translation. None of these vocabularies is 
reducible to the others. And yet the family resemblance among them is striking, 
sustained across decades of independent theoretical development, and reflects a 
convergent recognition that cognition is structured by knowledge already in place 
and that this structure is what makes both perception's economy and perception's 
distortion possible. The schema, in this sense, is less a discovery than a 
commitment.

What gives the schema its theoretical reach is the range of phenomena it makes 
intelligible without strain. Reconstructive memory becomes the predictable 
behavior of a knowledge structure asked to retrieve what it never fully encoded. 
Eyewitness misidentification becomes the cost of a categorization system 
optimized for speed rather than fidelity. The construct earns its keep by its 
breadth. The breadth is not coincidence; it is the signature of an idea that 
cuts at a real joint.
"""

The exemplar's TOPIC is illustrative only — apply its STYLE to the topic specified 
above. Style operates at the prose level. Preserve all structural requirements 
(callouts, wiki-links, YAML frontmatter, appendix architecture, Append-Marker 
Chain protocol) as specified by the generator.

CRITICAL CONSTRAINTS:
- Do NOT drift toward uniform medium-length sentences. Preserve the high variance.
- Do NOT lose figured texture after the first sections. Sustain controlled 
  metaphor throughout.
- Do NOT introduce first person ("I", "we", "our") under any condition.
- Do NOT over-hedge. Reserve qualifiers for genuine uncertainty.
- Do NOT abandon cross-paragraph arcs. Each paragraph should build toward something, 
  not stand alone.
</style-directive>
```

---

## Expected Behaviors

> [!methodology-and-sources] What this style should consistently produce
> When the directive is working, the generated report should exhibit:

1. **Sentence-length variance is visible.** A paragraph should contain at least one sentence over 35 words and at least one under 15. Uniform-length paragraphs indicate drift.

2. **Paragraphs build toward synthesis.** Each paragraph should land somewhere — a claim, a reframing, a consequence. Paragraphs that simply present a sequence of claims without arc indicate the integrative architecture has been lost.

3. **Family-resemblance moves appear in synthesis sections.** When the report draws together multiple traditions, theorists, or phenomena, the move should look like *"X, Y, and Z do not, on the surface, name the same thing — they emerged from different traditions… and yet…"* This is the signature argumentative shape.

4. **Figures appear, but sparingly.** Each paragraph should have at most two figures. Three or more indicates the texture has run away. Zero across multiple paragraphs indicates the figured texture has decayed.

5. **No first-person intrusion.** "I think," "we might say," "in our view" should never appear. The voice is impersonal.

6. **Hedges are load-bearing.** "Perhaps," "in some sense," "more or less" should appear where genuine uncertainty is being marked, not as throat-clearing.

7. **The prose feels deliberate.** Not slow — the cadence is too varied for that — but considered. The voice should not feel like it is racing.

---

## Known Failure Modes

> [!warning] What goes wrong with this style at length
> Each failure mode below has been observed in long-form generation. Each has a counter-measure listed in the next section.

> [!key-claim] Failure Mode 1 — Cadence Collapse
> **What it looks like:** Sentences trend toward uniform medium length (~20 words). Variance disappears. The breathing pattern flattens. The prose becomes readable but generic.
>
> **When it happens:** Most commonly between the 2,000- and 4,000-word mark, as the model's recent context fills with its own prior output and it begins regressing toward the mean of academic prose.

> [!key-claim] Failure Mode 2 — Figured Texture Decay
> **What it looks like:** The metaphors fade. By the middle of the report, the prose is purely literal — competent but textureless. The opening had figures; the body does not.
>
> **When it happens:** When the model decides figures are decorative rather than load-bearing. Without explicit reinforcement, the figured texture is the first stylistic feature to be sacrificed under context pressure.

> [!key-claim] Failure Mode 3 — Hedging Creep
> **What it looks like:** Every claim accumulates softeners. "It may be the case that," "one might argue," "in a certain sense" appear in every sentence. The prose becomes flabby; confidence dissolves.
>
> **When it happens:** When the model defaults to academic-conservative mode. This is a particular hazard for the [[Annotated-Critical-Analysis]] generator, whose epistemic confidence machinery can interact poorly with the style directive.

> [!key-claim] Failure Mode 4 — Personality Intrusion
> **What it looks like:** "I" or "we" appears unexpectedly. The impersonal voice breaks. Even one occurrence undermines the rest of the report's authority.
>
> **When it happens:** Particularly common in conclusion sections, synthesis sections, and any section the model treats as "summary" — where it tends to default to a more conversational register.

> [!key-claim] Failure Mode 5 — Over-Figuring
> **What it looks like:** The model decides figures are good and uses three or four per paragraph. The prose becomes purple. Every concept gets a metaphor whether or not one is needed.
>
> **When it happens:** When the directive is interpreted maximally. Less common than under-figuring but more obvious when it occurs.

> [!key-claim] Failure Mode 6 — Synthesis Fatigue
> **What it looks like:** Early sections perform family-resemblance moves cleanly. Later sections present claims linearly, without drawing things together. The signature argumentative shape disappears.
>
> **When it happens:** When the model treats family-resemblance as an opening flourish rather than a sustained method. This is the single most consequential decay pattern, because synthesis is the *heart* of this voice.

> [!key-claim] Failure Mode 7 — Cross-Paragraph Arc Loss
> **What it looks like:** Paragraphs become independent units. Each presents a topic and resolves it within itself. The cross-paragraph integration that defines the Patient Synthesizer disappears.
>
> **When it happens:** Particularly in long generators with explicit section structure (like [[foundational-report]]). The model treats each section as a self-contained essay rather than as part of a continuous arc.

> [!key-claim] Failure Mode 8 — Long-Sentence Cap Drift
> **What it looks like:** Every sentence becomes long. The breathing — the short release sentences that make the long ones tolerable — disappears. The prose becomes airless.
>
> **When it happens:** When the model interprets "long developmental sentences" as the universal target rather than as one element of a varied profile.

---

## Counter-Measures Against Decay

> [!methodology-and-sources] Tactical responses to each failure mode
> These are operational, not theoretical. Apply them when you see the relevant decay pattern in generated output.

### Counter-Measure 1: Mid-Generation Re-Anchoring

When the generator hits its midpoint validation gate (around the 5,000-word mark), inject this reminder via your continuation prompt:

```
Reread the EXEMPLAR in the original style directive. The next sections must continue 
matching its cadence (mixed-wave with short release sentences), its texture (figures 
present but sparing), and its architecture (cross-paragraph synthesis). Do not drift 
toward uniform-length sentences or purely literal prose. The signature 
family-resemblance move must continue appearing in synthesis sections.
```

### Counter-Measure 2: Pre-Specified Figure Budget

In the original directive, add a per-section figure budget. Example: *"Each section of approximately 1,500 words should contain 4–8 figures (controlled metaphors). Fewer than 4 indicates texture decay; more than 8 indicates over-figuring."* This gives the model a quantitative target rather than a stylistic intuition.

### Counter-Measure 3: Explicit Anti-Patterns

Append to the directive a short list of patterns to avoid. The most useful three:
- *"Avoid sentences in the 18–25 word range when used three or more in succession. The cadence requires variance; uniform medium-length sentences indicate drift."*
- *"Avoid the constructions 'it could be argued,' 'one might suggest,' 'it is perhaps the case that.' These are throat-clearing; remove them. Hedge only where genuine uncertainty is being marked."*
- *"Avoid first person under any condition. If a synthesis section seems to require 'we,' rephrase impersonally."*

### Counter-Measure 4: Random-Sample Validation in Phase 9

During the generator's validation phase, add this instruction:

```
Sample three paragraphs at random from the body of the report. For each:
1. Count sentence lengths. Verify variance is present (at least one sentence over 
   35 words and one under 15).
2. Count figures (controlled metaphors). Verify presence of at least one per paragraph.
3. Verify the paragraph builds toward a synthetic landing rather than presenting 
   claims linearly.

If any of the three paragraphs fails any check, regenerate via targeted 
replace_string_in_file operations on the failing sections. Do not proceed to 
final completion until all sampled paragraphs pass.
```

### Counter-Measure 5: Section-Type Tuning

Different sections have different decay profiles. Adjust accordingly:

- **For empirical sections:** the [[House Style Variations Library]] *Inline-Parenthetical Citations* variant resists the natural drift toward bare narrative description.
- **For synthesis sections:** the *Claim-First Opening* variant reinforces the family-resemblance move.
- **For dialectical or contested-topic sections:** the *Contrast-First Opening* variant naturally preserves cross-paragraph arcs.
- **For historical sections:** the *Quietly Elegiac* variant prevents the prose from sliding into chronological listing.

---

## Quick Reference Card

> [!cheatsheet] One-Page Summary
>
> **Style name:** Patient Synthesizer (Figured)
>
> **In one sentence:** Scholarly cross-paragraph synthesis, mixed-wave cadence, controlled metaphor.
>
> **Cadence:** Long developmental sentences (35–50 words) breathing into short release sentences (5–15 words). Mean ~22 words. High variance.
>
> **Architecture:** Cross-paragraph arcs. Family-resemblance / convergent-recognition moves are the signature.
>
> **Voice:** Third-person impersonal. No first person ever.
>
> **Texture:** 1–2 figures per paragraph. Used where plain language would only describe.
>
> **Top failure modes:** Cadence collapse → uniform sentences. Texture decay → no figures by midpoint. Synthesis fatigue → linear claims instead of family-resemblance.
>
> **Top counter-measures:** Mid-generation re-anchor at 5,000 words. Figure budget per section. Random-sample validation in Phase 9.
>
> **Best generators:** [[foundational-report]], [[Annotated-Critical-Analysis]], [[Dialectical Report]], [[Comparative-Architecture]], [[Historical-Genealogical]], [[First Principles Analysis]], [[Deep Dive Report]].
>
> **Less suitable for:** [[Practitioner's-Field-Guide]] (too direct/operational), [[Socratic Exploration]] (too dialogic) — use library variants for these.

---

## Connections and Links

> [!connections-and-links]
> **Upstream:** [[Writing Style Exemplars for Report Generators]] (the broader style library this voice was selected from), [[Constitutional Depth Mandate]] (the depth principles this voice operates within), [[VADER Academic Report Generator]] (primary deployment target)
>
> **Downstream:** [[House Style Variations Library]] (variations on this baseline tuned per use-case), all future generated reports invoking this style, future style-decay empirical studies
>
> **Lateral:** [[Cadence in Long-Form Prose]], [[Family Resemblance Concepts in Wittgenstein]] (the philosophical heritage of the signature argumentative move), [[Figured Texture in Academic Writing]], [[Style Decay in LLM Generation]]
>
> **Strengthened:** [[PKB Report Generator Suite v2.0]] (now has a canonical voice), [[Prompt-Engineering-Specialist-Agent-v4.0]] (gains personalized style-control infrastructure)

---

## Further Exploration

> [!further-exploration]
> Topics worth developing into their own PKB documents:

> [!topic-idea] Empirical Decay Curves for the Patient Synthesizer
> Generate ten 10K-word reports using this style directive without counter-measures. At each 1,000-word interval, sample three paragraphs and score them against the seven Expected Behaviors. Plot decay curves per behavior to identify which features fail first and at what word counts. Calibrate counter-measure timing accordingly.

> [!topic-idea] Cross-Model Style Portability
> Test whether this directive produces equivalent voice across Claude Opus, Claude Sonnet, and other LLMs. The directive was developed against Opus; smaller models may interpret it differently. Document model-specific adjustments needed.

> [!topic-idea] Section-Type Specialization Library
> Develop a parallel library where each entry is a tuned version of this voice optimized for one section type (Foundation, Methodology, Findings, Synthesis, Appendix). The general directive does well across sections; specialized variants might do better.

> [!topic-idea] Voice-Aware Pipeline Validation
> Extend `pipeline_v2.py` with a style-validation stage that scores generated reports against the Expected Behaviors checklist before pipeline extraction. Reports failing validation get flagged for review or regeneration.

> [!topic-idea] Metacognitive Style Reflection
> Adapt the [[Prompt-Engineering-Specialist-Agent-v4.0]]'s metacognitive scaffolding to include a style-self-check thinking block: before each major section, the model explicitly reasons about whether its prior section maintained the style and what to adjust for the next.

---

*End of canonical reference. The deployable directive is the **Paste-Ready Style Directive** section above. The variations of this voice live in [[House Style Variations Library]].*
