---
batch_name: batch-01-memory-systems
batch_date: 2026-04-24
default_domain: cognitive-science
default_confidence: high
notes: |
  Batch 1 of 8 from the user-supplied custom seed list (164 net-new terms after
  dedup against v6-llm-elaborated/). Focus: human memory systems, the
  multi-store / working-memory architecture, encoding/storage/retrieval
  primitives, and the levels-of-processing tradition. These notes anchor the
  prerequisite layer for downstream notes on study strategy, metacognition,
  and instructional design.
---

# Batch: Memory Systems & Architecture

## Short-Term Memory

- domain: cognitive-science
- secondary_domains: [memory-research, learning-science]
- aliases: [STM, primary memory]
- broader: [memory-systems, multi-store-model]
- narrower: [working-memory, phonological-loop, visuospatial-sketchpad]
- related: [long-term-memory, working-memory-capacity, magical-number-seven, maintenance-rehearsal]
- prerequisites: [memory-systems]
- confidence: high

**definition**: Short-Term Memory is the limited-capacity, time-limited store that briefly retains a small number of items in an immediately accessible state, classically theorised as the second stage of the [[multi-store-model]] between sensory registration and consolidation into [[long-term-memory]]; without active rehearsal its contents decay within roughly 15-30 seconds.

**key_claim**: Short-Term Memory is functionally distinguishable from working memory: it is conceived as a passive holding buffer characterised by capacity ([[magical-number-seven]]) and decay, whereas [[working-memory]] adds executive manipulation on top of those storage components.

**warning**: Short-Term Memory is often used as a loose synonym for [[working-memory]] in popular writing, but conflating the two erases the central theoretical move of Baddeley's revision and obscures why [[working-memory-capacity]] (not raw STM span) predicts complex cognition.

## Semantic Memory

- domain: cognitive-science
- secondary_domains: [memory-research, knowledge-representation]
- aliases: [conceptual memory, generic memory]
- broader: [declarative-memory, long-term-memory]
- related: [episodic-memory, schema-theory, [[spreading-activation]], priming]
- prerequisites: [long-term-memory, declarative-memory]
- confidence: high

**definition**: Semantic Memory is the long-term store of context-free general knowledge — facts, concepts, word meanings, and category structure — that is accessed without recollection of the learning episode in which it was acquired, distinguished by Tulving from the autobiographical contents of [[episodic-memory]].

**key_claim**: Semantic Memory is built incrementally from many [[episodic-memory]] traces whose contextual details fade while their schematic content abstracts and integrates, which is why repeated encounters across varied contexts produce robust semantic knowledge while a single vivid episode rarely does.

**warning**: Semantic Memory is sometimes treated as a static "fact warehouse," but it is constantly being restructured by new episodes; treating it as immutable misleads instructional design that assumes knowledge "sticks" once delivered, when in fact unrevisited semantic content drifts and decays just as other memory contents do.

## Episodic Memory

- domain: cognitive-science
- secondary_domains: [memory-research, autobiographical-memory]
- aliases: [autobiographical memory, event memory]
- broader: [declarative-memory, long-term-memory]
- related: [semantic-memory, [[reconstructive-memory]], [[encoding-specificity-principle]]]
- prerequisites: [long-term-memory, declarative-memory]
- confidence: high

**definition**: Episodic Memory is the long-term system that stores personally experienced events together with their spatial, temporal, and emotional context, supporting the conscious "mental time travel" through which a learner re-experiences a particular moment of acquisition rather than merely knowing the resulting fact.

**key_claim**: Episodic Memory provides the substrate from which [[semantic-memory]] is abstracted: repeated episodes lose their idiosyncratic context while their common conceptual structure consolidates, a transformation that explains why deliberate variation of study context strengthens later semantic retrieval.

**warning**: Episodic Memory is highly [[reconstructive-memory|reconstructive]] rather than veridical; treating recalled episodes as faithful recordings ignores decades of evidence on confabulation, schema-driven distortion, and post-event misinformation, with serious consequences in educational testimony and self-assessment.

## Declarative Memory

- domain: cognitive-science
- secondary_domains: [memory-research, neuroscience]
- aliases: [explicit memory]
- broader: [long-term-memory, memory-systems]
- narrower: [semantic-memory, episodic-memory]
- related: [procedural-memory, non-declarative-memory, [[hippocampus]]]
- prerequisites: [long-term-memory]
- confidence: high

**definition**: Declarative Memory is the long-term subsystem for consciously accessible knowledge that can be verbally reported — encompassing both [[semantic-memory]] (facts and concepts) and [[episodic-memory]] (events) — and is selectively impaired by medial-temporal-lobe damage that spares motor skills and conditioned responses.

**key_claim**: Declarative Memory and [[procedural-memory]] are functionally and neurally dissociable: the same patient can lose new declarative learning while continuing to acquire skills, which establishes that "memory" is not a single faculty but a federation of systems with distinct rules.

**warning**: Declarative Memory's introspective accessibility makes it deceptively easy to assess (you can ask the learner), whereas [[procedural-memory]] often requires behavioural probes; over-relying on verbal report as a measure of "what was learned" systematically undercounts implicit competence and overcounts shallow declarative knowledge.

## Procedural Memory

- domain: cognitive-science
- secondary_domains: [memory-research, motor-learning]
- aliases: [skill memory, motor memory]
- broader: [non-declarative-memory, long-term-memory]
- related: [declarative-memory, [[automaticity]], [[deliberate-practice]], [[power-law-of-practice]]]
- prerequisites: [long-term-memory, non-declarative-memory]
- confidence: high

**definition**: Procedural Memory is the long-term system supporting the acquisition and execution of skills, habits, and rule-governed sequences whose performance does not require conscious access to their underlying representations, classically demonstrated by H.M.'s preserved mirror-tracing learning despite dense declarative amnesia.

**key_claim**: Procedural Memory is acquired gradually through repetition and feedback rather than through single-trial declarative encoding, which is why a learner can describe a skill perfectly without being able to perform it and conversely can perform fluently without being able to articulate the rules in play.

**warning**: Procedural Memory is sometimes conflated with [[automaticity]], but the two are distinct: automaticity refers to a *property* a procedure can acquire (speed, low attentional cost), whereas Procedural Memory refers to the *substrate* in which the procedure lives; instructional schemes that pursue speed before correct procedural encoding produce fast but wrong performance.

## Non-Declarative Memory

- domain: cognitive-science
- secondary_domains: [memory-research, implicit-cognition]
- aliases: [implicit memory]
- broader: [long-term-memory, memory-systems]
- narrower: [procedural-memory, priming, [[classical-conditioning]]]
- related: [declarative-memory, automaticity]
- prerequisites: [long-term-memory]
- confidence: high

**definition**: Non-Declarative Memory is the umbrella category for long-term memory subsystems whose contents influence behaviour without conscious recollection, including [[procedural-memory]], [[priming]], conditioning, and habituation, and is typically intact in patients with [[declarative-memory]] deficits.

**key_claim**: Non-Declarative Memory establishes that influence on behaviour is not the same as availability to introspection: a learner can be reliably affected by experiences they cannot recall, which forces any complete account of learning to range beyond what can be elicited by direct questioning.

**warning**: Non-Declarative Memory's invisibility to self-report makes it easy to ignore in instructional contexts, but it carries much of what counts as expertise; assuming that "if the learner cannot articulate it, they have not learned it" systematically underestimates competence built through extended practice.

## Memory Systems

- domain: cognitive-science
- secondary_domains: [memory-research, cognitive-architecture]
- aliases: [multiple memory systems]
- broader: [cognitive-architecture]
- narrower: [declarative-memory, non-declarative-memory, working-memory, sensory-memory]
- related: [multi-store-model, [[long-term-memory]]]
- prerequisites: []
- confidence: high

**definition**: Memory Systems is the theoretical framework — most associated with Squire and Tulving — that treats human memory not as a single faculty but as a coordinated set of dissociable subsystems (working, declarative, non-declarative, perceptual) each with its own neural substrate, encoding rules, and forgetting dynamics.

**key_claim**: Memory Systems theory is supported by triple dissociations from neuropsychology and neuroimaging in which selective damage spares some subsystems while abolishing others, establishing that "improving memory" is not a single goal but a system-specific design choice.

**warning**: Memory Systems should not be reified into rigid boxes: the subsystems interact constantly during normal cognition (an episodic retrieval recruits semantic content; a procedural skill is initially scaffolded by declarative knowledge), and pedagogy that targets only one subsystem in isolation forfeits the integration that gives expertise its flexibility.

## Memory Consolidation

- domain: cognitive-science
- secondary_domains: [memory-research, neuroscience, sleep-research]
- aliases: [consolidation]
- broader: [long-term-memory]
- related: [reconstructive-memory, [[spacing-effect]], [[sleep-and-learning]], [[hippocampus]]]
- prerequisites: [long-term-memory]
- confidence: high

**definition**: Memory Consolidation is the time-dependent set of neural processes by which a labile, hippocampally-supported trace becomes a stable, distributed cortical representation, occurring across cellular timescales (minutes to hours) and systems timescales (days to years), and depending heavily on offline replay during sleep.

**key_claim**: Memory Consolidation reframes "what was learned today" as inherently provisional: the trace continues to be modified, integrated, and stabilised long after the study session ends, which is why the timing of subsequent rest, sleep, and review materially shapes what survives.

**warning**: Memory Consolidation is sometimes invoked as a hand-wave that "sleep fixes everything," but consolidation strengthens whatever is encoded — including misconceptions, errors, and surface features — so the strategy "study heavily, then sleep" can entrench wrong material as efficiently as right material if no error correction happens before the consolidation window closes.

## Reconstructive Memory

- domain: cognitive-science
- secondary_domains: [memory-research, social-cognition]
- aliases: [reconstructive recall, schema-driven recall]
- broader: [episodic-memory, long-term-memory]
- related: [schema-theory, [[confirmation-bias]], [[motivated-reasoning]]]
- prerequisites: [episodic-memory, schema-theory]
- confidence: high

**definition**: Reconstructive Memory is the principle, traceable to Bartlett's *Remembering* (1932), that recall is not a literal readout of stored content but an active reconstruction guided by current schemas, expectations, and goals — producing outputs that feel like veridical memories yet incorporate inferences, interpolations, and outright distortions.

**key_claim**: Reconstructive Memory predicts that confidence and accuracy are weakly coupled: a learner can be vividly certain of a recalled event whose details have been silently rewritten by the schemas active at retrieval, which undermines self-report as a reliable assessment of acquired knowledge.

**warning**: Reconstructive Memory does not license the conclusion that "memory is unreliable, period"; the same reconstructive mechanism that introduces distortion also enables productive inference, gist extraction, and transfer, and pedagogy should exploit the constructive side rather than treat reconstruction as a defect to be eliminated.

## Encoding Specificity Principle

- domain: cognitive-science
- secondary_domains: [memory-research, learning-science]
- aliases: [encoding specificity, transfer-appropriate processing]
- broader: [retrieval-practice, long-term-memory]
- related: [episodic-memory, [[context-dependent-memory]], [[state-dependent-memory]]]
- prerequisites: [long-term-memory, episodic-memory]
- confidence: high

**definition**: The Encoding Specificity Principle, articulated by Tulving and Thomson (1973), holds that retrieval is most effective when the cues present at retrieval overlap with the features encoded at the time of learning, making the *match* between encoding and retrieval contexts — not the absolute strength of the trace — the proximate determinant of recall.

**key_claim**: The Encoding Specificity Principle reframes "knowing something" as relational rather than absolute: a learner who reliably retrieves a fact in the classroom may fail to retrieve it in a clinical or workplace setting whose cues do not overlap with those of original encoding, which makes [[far-transfer]] hard precisely because it asks for retrieval under maximally different cue conditions.

**warning**: The Encoding Specificity Principle is sometimes read as endorsing study-context restriction ("study where you'll be tested"), but the more robust pedagogical inference is the opposite: deliberately *vary* encoding contexts so that the trace is bound to multiple cue sets and becomes retrievable from a wider range of future situations.

## Working Memory Capacity

- domain: cognitive-science
- secondary_domains: [individual-differences, intelligence-research]
- aliases: [WMC, working-memory span]
- broader: [working-memory]
- related: [fluid-intelligence, [[cognitive-load-theory]], [[executive-function]], magical-number-seven]
- prerequisites: [working-memory, short-term-memory]
- confidence: high

**definition**: Working Memory Capacity is the individual-difference variable indexing how much information a learner can simultaneously maintain *and* manipulate under conditions of interference, typically measured by complex span tasks (operation span, reading span) that require concurrent processing alongside storage.

**key_claim**: Working Memory Capacity correlates substantially with [[fluid-intelligence]] and predicts performance on tasks requiring controlled attention, conflict resolution, and novel problem-solving — making it among the strongest single cognitive predictors of complex skill acquisition.

**warning**: Working Memory Capacity has resisted durable training: brief gains on trained tasks rarely transfer to untrained tasks of the same construct, so commercial "brain training" programmes promising broad WMC enlargement consistently overstate their evidence and the more robust intervention is to *reduce demands* on WMC through schema-building and external scaffolding.

## Episodic Buffer

- domain: cognitive-science
- secondary_domains: [memory-research, working-memory]
- aliases: []
- broader: [working-memory]
- related: [phonological-loop, visuospatial-sketchpad, central-executive, episodic-memory, long-term-memory]
- prerequisites: [working-memory, multi-store-model]
- confidence: high

**definition**: The Episodic Buffer is the fourth component added to Baddeley's working-memory model in 2000, a limited-capacity store that integrates information from the [[phonological-loop]], the [[visuospatial-sketchpad]], and [[long-term-memory]] into coherent multimodal episodes available to consciousness and to the [[central-executive]].

**key_claim**: The Episodic Buffer was added to address phenomena Baddeley's original three-component model could not explain — chunking effects from long-term memory, cross-modal binding, and recall of prose passages whose span vastly exceeds the slave systems — by positing an explicit integrative workspace.

**warning**: The Episodic Buffer should not be treated as an unbounded "scratchpad" that resolves capacity limits; it remains capacity-limited, depends on the [[central-executive]] for attentional binding, and its proposed role in long-term-memory integration is still empirically contested by alternative accounts that locate binding inside long-term memory itself.

## Multi-Store Model

- domain: cognitive-science
- secondary_domains: [memory-research, history-of-cognitive-science]
- aliases: [Atkinson-Shiffrin model, modal model]
- broader: [memory-systems, cognitive-architecture]
- related: [short-term-memory, long-term-memory, working-memory, [[sensory-memory]]]
- prerequisites: [memory-systems]
- confidence: high

**definition**: The Multi-Store Model, proposed by Atkinson and Shiffrin (1968), partitions human memory into three sequential stores — sensory register, short-term store, and long-term store — connected by control processes such as attention, rehearsal, and retrieval, providing the framework against which all subsequent working-memory theories were developed.

**key_claim**: The Multi-Store Model's central commitment is that information must pass through a limited-capacity short-term stage to enter long-term storage, which makes the bottleneck at [[short-term-memory]] the principal locus of instructional design — a commitment inherited by [[cognitive-load-theory]] decades later.

**warning**: The Multi-Store Model has been substantially superseded: it cannot accommodate evidence that long-term knowledge influences short-term performance (chunking), that [[working-memory]] supports manipulation as well as storage, or that brain damage can dissociate STM and LTM in either direction; treating it as a current theory rather than an influential historical scaffold misrepresents the field.

## Central Executive

- domain: cognitive-science
- secondary_domains: [working-memory, executive-function]
- aliases: [executive controller, attentional controller]
- broader: [working-memory, executive-function]
- related: [phonological-loop, visuospatial-sketchpad, episodic-buffer, attention-and-cognitive-control]
- prerequisites: [working-memory]
- confidence: high

**definition**: The Central Executive is the supervisory component of Baddeley's working-memory model responsible for allocating attention, coordinating the slave systems, switching between tasks, suppressing irrelevant material, and interfacing working memory with [[long-term-memory]]; it is conceived as attentional rather than as a storage buffer.

**key_claim**: The Central Executive is the working-memory locus that does the most work explaining individual differences in [[working-memory-capacity]], [[fluid-intelligence]], and reasoning, because the cognitive operations it implements — controlled attention, interference resolution, goal maintenance — are precisely those that distinguish skilled from unskilled performance on novel problems.

**warning**: The Central Executive is the most under-specified component of the working-memory model and has been criticised as a "homunculus" that absorbs whatever the slave systems cannot explain; treating it as a unitary mechanism obscures that contemporary work has fractionated executive function into at least three partially separable processes (updating, switching, inhibition).

## Phonological Loop

- domain: cognitive-science
- secondary_domains: [working-memory, language-processing]
- aliases: [articulatory loop]
- broader: [working-memory]
- related: [central-executive, visuospatial-sketchpad, episodic-buffer, short-term-memory, [[subvocal-rehearsal]]]
- prerequisites: [working-memory]
- confidence: high

**definition**: The Phonological Loop is the slave system in Baddeley's model dedicated to the temporary storage and rehearsal of speech-based information, comprising a passive phonological store that holds material for roughly two seconds and an articulatory rehearsal process that refreshes the store via subvocal repetition.

**key_claim**: The Phonological Loop is supported by signature behavioural effects — the phonological similarity effect, the word-length effect, articulatory suppression, and the irrelevant speech effect — whose joint pattern is hard to explain without positing a domain-specific verbal store separate from a domain-general workspace.

**warning**: The Phonological Loop is often invoked as the primary substrate for "verbal working memory" in classroom contexts, but its capacity limits are easily breached and it is highly vulnerable to interference from background speech and music; designing study environments without accounting for irrelevant-speech effects systematically degrades verbal learning.

## Visuospatial Sketchpad

- domain: cognitive-science
- secondary_domains: [working-memory, spatial-cognition]
- aliases: [visuospatial scratchpad, visuo-spatial sketchpad]
- broader: [working-memory]
- related: [phonological-loop, central-executive, episodic-buffer, [[mental-imagery]]]
- prerequisites: [working-memory]
- confidence: high

**definition**: The Visuospatial Sketchpad is the slave system in Baddeley's model that maintains and manipulates visual and spatial information — object identity, location, and movement — supporting tasks such as mental rotation, navigation, and visual imagery, and is functionally separable from the verbal [[phonological-loop]].

**key_claim**: The Visuospatial Sketchpad's separation from the Phonological Loop is supported by selective interference: a concurrent visuospatial task (pattern-tapping, mental rotation) impairs visuospatial recall while leaving verbal recall intact, and the converse holds for articulatory suppression — establishing modality-specific resources rather than a single workspace.

**warning**: The Visuospatial Sketchpad is often treated as a unitary store, but more recent work splits it into dissociable visual ("what") and spatial ("where") components; pedagogical claims about "visual learners" routinely conflate these subsystems and ignore that visual presentation does not automatically engage the appropriate component for the task at hand.

## Working Memory in Reading

- domain: cognitive-science
- secondary_domains: [reading-research, learning-science]
- aliases: [reading working memory]
- broader: [working-memory, working-memory-capacity]
- related: [phonological-loop, central-executive, [[reading-comprehension]], [[reading-span-task]]]
- prerequisites: [working-memory]
- confidence: high

**definition**: Working Memory in Reading refers to the role of capacity-limited maintenance and integration during text comprehension — holding the just-processed clause active while parsing the next, integrating anaphoric reference, building situation models, and inhibiting irrelevant interpretations — and is the construct measured by Daneman and Carpenter's reading-span task.

**key_claim**: Working Memory in Reading correlates strongly with comprehension performance because complex text continually demands simultaneous storage of partial representations and active processing of incoming content, which makes reading among the most attention-demanding everyday cognitive activities and explains why distraction so reliably degrades comprehension.

**warning**: Working Memory in Reading limits cannot be eliminated by motivation or effort; pedagogical regimes that demand sustained reading of high-density text without scaffolding (chunking, advance organisers, retrieval prompts) systematically overload novice readers and produce the surface symptoms — slow reading, re-reading, comprehension failure — that are then misattributed to "low ability."

## Elaborative Rehearsal

- domain: cognitive-science
- secondary_domains: [memory-research, learning-strategies]
- aliases: [deep rehearsal, semantic rehearsal]
- broader: [rehearsal, deep-processing]
- related: [maintenance-rehearsal, levels-of-processing, elaboration, elaborative-interrogation, deep-processing]
- prerequisites: [working-memory, long-term-memory]
- confidence: high

**definition**: Elaborative Rehearsal is the encoding strategy in which a learner connects new material to existing knowledge through meaning-based processing — generating examples, paraphrasing, comparing, or relating new content to personal experience — rather than merely repeating it verbatim; it is the high-payoff pole on the levels-of-processing continuum.

**key_claim**: Elaborative Rehearsal produces substantially better long-term retention than [[maintenance-rehearsal]] of equivalent duration because the additional semantic associations create multiple retrieval routes back to the trace, increasing the probability that some cue available at retrieval will reach it.

**warning**: Elaborative Rehearsal is not merely "more rehearsal" — it must be semantically appropriate elaboration; *spurious* elaboration (relating material to false or misleading prior content) embeds the trace inside an incorrect schema and can produce confident but wrong recall, which is why elaboration without feedback is risky.

## Maintenance Rehearsal

- domain: cognitive-science
- secondary_domains: [memory-research, working-memory]
- aliases: [rote rehearsal, shallow rehearsal]
- broader: [rehearsal]
- related: [elaborative-rehearsal, phonological-loop, levels-of-processing, short-term-memory]
- prerequisites: [working-memory, short-term-memory]
- confidence: high

**definition**: Maintenance Rehearsal is the surface-level repetition of material — typically subvocal articulation in the [[phonological-loop]] — that holds information active in [[short-term-memory]] without engaging in deeper semantic processing, and is the strategy children spontaneously deploy long before they discover elaborative alternatives.

**key_claim**: Maintenance Rehearsal stabilises items in working memory but produces only weak long-term retention relative to time-equated [[elaborative-rehearsal]], which establishes that long-term storage benefits depend on *what* is done with information during rehearsal, not on the duration of attention itself.

**warning**: Maintenance Rehearsal is the default study strategy of struggling students ("re-reading the highlights"), and its short-term feeling of fluency creates an [[fluency-illusion]] that the material is mastered; the gap between this subjective fluency and actual delayed recall is one of the most consistent findings in metacognitive research.

## Priming

- domain: cognitive-science
- secondary_domains: [memory-research, implicit-cognition, social-psychology]
- aliases: [implicit priming]
- broader: [non-declarative-memory]
- narrower: [semantic-priming, perceptual-priming, [[repetition-priming]]]
- related: [spreading-activation, semantic-memory, [[implicit-memory]]]
- prerequisites: [non-declarative-memory]
- confidence: high

**definition**: Priming is the implicit memory phenomenon in which prior exposure to a stimulus facilitates its later processing — speeded recognition, lowered identification thresholds, biased completion — without the perceiver's awareness that the prior exposure is influencing current performance.

**key_claim**: Priming demonstrates that mere exposure leaves measurable, behaviourally consequential traces independently of any conscious recollection, which is among the strongest empirical grounds for positing [[non-declarative-memory]] as a system distinct from explicit recall.

**warning**: Priming has been at the centre of the replication crisis in social psychology, where many high-profile "behavioural priming" claims (elderly stereotypes slowing walking, money concepts affecting prosociality) have failed to reproduce; the well-replicated core of priming is *cognitive* (lexical, semantic, perceptual), and extrapolating from it to large behavioural effects requires evidence that has often not survived scrutiny.

## Deep Processing

- domain: cognitive-science
- secondary_domains: [learning-science, memory-research]
- aliases: [deep encoding, semantic processing]
- broader: [levels-of-processing]
- related: [elaborative-rehearsal, maintenance-rehearsal, elaboration, self-explanation, [[generative-learning-theory]]]
- prerequisites: [levels-of-processing]
- confidence: high

**definition**: Deep Processing is the end of Craik and Lockhart's [[levels-of-processing]] continuum at which incoming material is analysed for meaning, integrated with prior knowledge, and related to existing schemas — as opposed to surface-level analysis of physical or phonological features — and is the encoding regime that produces durable, retrievable traces.

**key_claim**: Deep Processing predicts retention better than the duration of study or the number of repetitions, which is why a learner who briefly elaborates on meaning often outperforms a learner who repeatedly re-reads, and why instructional designs that *force* meaning-level engagement (questions, self-explanation, application) outperform those that merely re-expose material.

**warning**: Deep Processing has been criticised as circular (depth is sometimes inferred from the very retention it is supposed to explain), and the modern replacement frame — *transfer-appropriate processing* — emphasises that it is not depth per se but the *match* between encoding operations and required retrieval operations that drives performance; treating depth as a one-dimensional ladder oversimplifies the underlying mechanism.

## Cognitive Chunking

- domain: cognitive-science
- secondary_domains: [working-memory, expertise-research]
- aliases: [chunking]
- broader: [chunking, working-memory]
- related: [magical-number-seven, schema-theory, [[hierarchical-chunk-structure]], [[expertise-development]]]
- prerequisites: [working-memory, long-term-memory]
- confidence: high

**definition**: Cognitive Chunking is the process by which a learner exploits long-term-memory structures to group several elements into a single higher-order unit, effectively expanding working-memory throughput by replacing many low-level items with fewer chunks that can each be manipulated as a single entity.

**key_claim**: Cognitive Chunking is the principal mechanism by which experts circumvent the [[magical-number-seven]] limit: chess masters do not have larger raw working memory than novices, but they encode positions in terms of meaningful piece configurations, allowing them to reproduce a chessboard from a single glance that would defeat a novice's item-by-item encoding.

**warning**: Cognitive Chunking depends on prior schema availability, so it cannot be invoked as a quick fix for novice overload; instructing a beginner to "chunk the material" presupposes the very long-term knowledge they are trying to acquire, and the productive intervention is to *build* the schemas that will eventually permit chunking, not to ask for chunking before those schemas exist.

## Magical Number Seven

- domain: cognitive-science
- secondary_domains: [memory-research, history-of-cognitive-science]
- aliases: [magical number seven plus or minus two, Miller's seven, working-memory span limit]
- broader: [working-memory, short-term-memory]
- related: [working-memory-capacity, cognitive-chunking, [[span-of-apprehension]]]
- prerequisites: [short-term-memory]
- confidence: high

**definition**: The Magical Number Seven, named after George Miller's 1956 paper, is the empirical generalisation that the immediate-memory span across diverse modalities clusters around seven plus or minus two items, and is the historical anchor for all subsequent capacity-limit work in cognitive psychology.

**key_claim**: The Magical Number Seven is best understood as a limit on *chunks* rather than raw items: the same span that holds seven random digits also holds seven memorised digit triplets — twenty-one digits — which establishes that capacity is jointly determined by working memory and by the long-term knowledge that supports [[cognitive-chunking]].

**warning**: The Magical Number Seven has been substantially revised: more recent work (Cowan, 2001) places the true capacity at around four chunks under conditions that prevent rehearsal and chunking, with seven appearing only when those strategies are available; treating "seven" as the bedrock capacity overstates the limit and underweights the role of strategy in apparent span.

## Dual Coding Theory

- domain: cognitive-science
- secondary_domains: [memory-research, multimedia-learning]
- aliases: [dual-coding, DCT, Paivio's theory]
- broader: [memory-systems, levels-of-processing]
- related: [cognitive-theory-of-multimedia-learning, [[modality-effect]], elaborative-rehearsal, mental-imagery]
- prerequisites: [long-term-memory]
- confidence: high

**definition**: Dual Coding Theory, developed by Allan Paivio, holds that human cognition is supported by two functionally and structurally distinct symbolic systems — a verbal system processing language-like representations and a non-verbal imagery system processing analog representations — that interact bidirectionally and jointly support memory and meaning.

**key_claim**: Dual Coding Theory predicts that material encoded in both systems is remembered better than material encoded in only one, because two independent retrieval routes exist; this prediction has driven decades of research on imagery-based mnemonic devices, illustrated text effects, and the multimedia design principles formalised by Mayer's [[cognitive-theory-of-multimedia-learning]].

**warning**: Dual Coding Theory is often invoked to justify "always add a picture," but the gain depends on the picture being semantically integrative rather than decorative; irrelevant or merely-illustrative imagery can compete for limited resources rather than augment them, and the [[redundancy-effect]] from CLT identifies cases where the supposedly dual encoding produces interference instead of facilitation.
