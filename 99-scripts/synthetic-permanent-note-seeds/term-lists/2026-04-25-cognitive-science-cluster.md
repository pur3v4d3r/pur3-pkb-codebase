---
batch_name: cognitive-science-cluster-2026-04-25
batch_date: 2026-04-25
default_domain: cognitive-science
default_confidence: high
notes: |
  Forty-nine foundational concepts spanning attention, memory systems,
  instructional design, motivation, self-regulated learning, reasoning,
  cognitive biases, PKM, wellbeing, and the neuroscience of learning.
  Authored to densify the wiki-link graph in v6-llm-elaborated/ where
  each term is currently a missing target referenced by other notes.
---

# Batch: Cognitive Science Foundations Cluster

A broad seeding batch covering nine sub-domains. Each term carries a
definition, a key claim, and a warning so V4 mining produces a
five-callout bundle (definition + 2 support + 2 derived) per concept.

---

## Attention Restoration Theory

- domain: cognitive-science
- secondary_domains: [environmental-psychology, cognitive-neuroscience]
- aliases: [ART, Kaplan ART]
- broader: [attention-and-cognitive-control]
- related: [sustained-attention, mind-wandering, cognitive-load-theory]
- prerequisites: [executive-function, selective-attention]

**definition**: Attention Restoration Theory is the proposition, advanced by Stephen and Rachel Kaplan in 1989, that directed attention is a finite cognitive resource that fatigues with sustained voluntary effort and is restored most effectively through exposure to environments rich in soft fascination — typically natural settings — that engage involuntary attention without depleting executive control.

**key_claim**: Attention Restoration Theory predicts a measurable rebound in performance on tasks taxing directed attention (such as proofreading or dichotic listening) following brief exposure to natural environments, an effect not produced by equally pleasant but attentionally demanding urban scenes.

**warning**: Attention Restoration Theory is sometimes invoked as a general "nature is good for you" claim, but the theoretical mechanism is specifically about replenishing top-down attentional control; using it to justify any pleasant break confuses restoration of attention with mere mood improvement.

## Inattentional Blindness

- domain: cognitive-science
- secondary_domains: [perception, attention-research]
- aliases: [perceptual blindness, the gorilla effect]
- broader: [selective-attention]
- related: [perceptual-load-theory, attentional-blink, cognitive-load-theory]
- prerequisites: [working-memory, attention-and-selective-processing]

**definition**: Inattentional Blindness is the failure to consciously perceive an unexpected but fully visible stimulus when attention is engaged on another task or location, demonstrated most famously by the Simons and Chabris invisible-gorilla study and explained by attention's role as a precondition for conscious access rather than as a mere intensifier of perception.

**key_claim**: Inattentional Blindness shows that attention is constitutive of conscious perception rather than merely modulatory: stimuli that fall outside the current attentional set can be looked at directly without producing any reportable awareness, even when they are large, salient, and persistent.

**warning**: Inattentional Blindness is often misread as a general weakness of vision, but the underlying claim is narrower — it concerns conscious access under high attentional load; the unattended stimulus is still processed perceptually, which is why subliminal-priming effects can survive a failure of conscious report.

## Attentional Blink

- domain: cognitive-science
- secondary_domains: [perception, attention-research]
- aliases: [AB phenomenon]
- broader: [attention-and-cognitive-control]
- related: [working-memory, inattentional-blindness, perceptual-load-theory]
- prerequisites: [selective-attention, working-memory]

**definition**: The Attentional Blink is the temporary inability to detect a second target stimulus presented roughly 200–500 milliseconds after a successfully detected first target in a rapid serial visual presentation, reflecting a transient bottleneck in the consolidation of perceptual representations into reportable working memory.

**key_claim**: The Attentional Blink reveals that conscious perception of discrete targets is rate-limited not by sensory processing but by the time required to encode each target into a stable working-memory representation, with the second target failing to clear the consolidation gate while the first is still being processed.

**warning**: The Attentional Blink should not be conflated with general slow reaction time; the deficit is specific to consciously reporting the second target, and an "unseen" T2 still shows electrophysiological and priming evidence of having been perceptually processed.

## Perceptual Load Theory

- domain: cognitive-science
- secondary_domains: [perception, attention-research]
- aliases: [Lavie's load theory]
- broader: [selective-attention]
- related: [inattentional-blindness, cognitive-load-theory, working-memory]
- prerequisites: [attention-and-selective-processing]

**definition**: Perceptual Load Theory, developed by Nilli Lavie in the 1990s, holds that selective attention's locus depends on the perceptual demands of the primary task: under high perceptual load, attention exhausts capacity at early sensory stages and excludes irrelevant stimuli, while under low perceptual load spare capacity spills over and processes distractors involuntarily.

**key_claim**: Perceptual Load Theory predicts a counterintuitive distractor-interference pattern in which difficult tasks produce less distractor processing than easy tasks, because the early-vs-late selection question is settled by whether the target task saturates perceptual capacity.

**warning**: Perceptual Load Theory is sometimes generalized to all forms of cognitive demand, but the theoretical mechanism is specifically about perceptual capacity; high working-memory load actually has the opposite effect, increasing distractor interference by depleting executive control needed for late selection.

## Cognitive Flexibility

- domain: cognitive-science
- secondary_domains: [executive-function, developmental-psychology]
- aliases: [mental flexibility, set-shifting]
- broader: [executive-function]
- related: [working-memory, inhibitory-control, metacognitive-regulation]
- prerequisites: [attention-and-cognitive-control]

**definition**: Cognitive Flexibility is the executive capacity to disengage from an established cognitive set and engage an alternative one in response to changing task demands, indexed by performance on shifting paradigms such as the Wisconsin Card Sorting Test and the task-switching paradigm.

**key_claim**: Cognitive Flexibility is partially dissociable from working memory and inhibitory control, forming one of three core executive functions in Miyake's unity-and-diversity model and contributing unique variance to higher-level outcomes such as creative problem-solving and academic achievement.

**warning**: Cognitive Flexibility is often confused with mere willingness to consider alternatives, but the construct measures the cost-bearing operation of switching between active task sets; switching always incurs measurable response-time and accuracy costs even in highly flexible individuals.

## Sustained Attention

- domain: cognitive-science
- secondary_domains: [attention-research, vigilance]
- aliases: [vigilance, tonic alertness]
- broader: [attention-and-cognitive-control]
- related: [mind-wandering, attention-restoration-theory, executive-function]
- prerequisites: [selective-attention]

**definition**: Sustained Attention is the capacity to maintain alert focus on a non-stimulating task or signal stream over extended intervals, typically measured by vigilance paradigms such as the Mackworth Clock or continuous performance tests, and characterized by a reliable performance decrement as a function of time on task.

**key_claim**: Sustained Attention is not a passive state but an effortful self-regulated process whose decrement curve reflects the cost of maintaining endogenous attentional control against accumulating mental fatigue, mind-wandering pressure, and habituation to monitored stimuli.

**warning**: Sustained Attention is often conflated with selective attention, but they tap distinct mechanisms; a person can be highly selective in resisting distractors over short intervals while showing pronounced vigilance decrements over long ones, and training one does not transfer to the other.

## Working Memory Updating

- domain: cognitive-science
- secondary_domains: [executive-function, working-memory]
- aliases: [WM updating, content monitoring]
- broader: [working-memory]
- related: [executive-function, cognitive-flexibility, central-executive]
- prerequisites: [working-memory-capacity, central-executive]

**definition**: Working Memory Updating is the executive process responsible for the dynamic monitoring and revision of items currently held in working memory — adding incoming information, evaluating its relevance, and replacing now-outdated content — and constitutes one of three core executive functions in Miyake's framework alongside shifting and inhibition.

**key_claim**: Working Memory Updating predicts performance on the n-back paradigm and complex span tasks better than passive storage capacity does, supporting the view that working memory's contribution to fluid intelligence flows through the active maintenance and replacement of relevant content rather than through raw buffer size.

**warning**: Working Memory Updating is often equated with rehearsal or refreshing, but the construct specifically requires evaluative replacement of stored items; pure rehearsal preserves content unchanged and recruits distinct phonological-loop machinery.

## Autobiographical Memory

- domain: cognitive-science
- secondary_domains: [memory-research, developmental-psychology]
- aliases: [self-referential memory]
- broader: [episodic-memory, declarative-memory]
- related: [flashbulb-memory, source-amnesia, false-memory, semantic-memory]
- prerequisites: [long-term-memory, episodic-memory]

**definition**: Autobiographical Memory is the memory system that integrates episodic recollections of personally experienced events with semantic knowledge about one's own life history, producing a temporally extended self-narrative that supports identity continuity, future-event simulation, and social communication of past experience.

**key_claim**: Autobiographical Memory exhibits a robust reminiscence bump in which adults disproportionately recall events from late adolescence and early adulthood, reflecting the formative encoding of self-defining experiences during the period of identity consolidation rather than mere recency or rehearsal.

**warning**: Autobiographical Memory is intuitively treated as a faithful replay of past experience, but its reconstructive nature means that current goals, mood, and post-event information routinely reshape recollections; high subjective vividness is not evidence of accuracy.

## Flashbulb Memory

- domain: cognitive-science
- secondary_domains: [memory-research, emotion-and-memory]
- aliases: [emotional flashbulb]
- broader: [autobiographical-memory, episodic-memory]
- related: [autobiographical-memory, source-amnesia, false-memory, memory-consolidation]
- prerequisites: [long-term-memory, autobiographical-memory]

**definition**: Flashbulb Memory is the term coined by Brown and Kulik in 1977 for the unusually vivid, detailed, and confidently held recollection of the personal circumstances surrounding the reception of surprising and emotionally consequential public news, often described phenomenologically as a photograph-like trace of the moment of learning.

**key_claim**: Flashbulb Memory is best understood as ordinary autobiographical memory accompanied by inflated metacognitive confidence; longitudinal studies repeatedly show that the content of flashbulb memories degrades and distorts at rates comparable to mundane memories, even as the subjective sense of vividness and certainty remains stable.

**warning**: Flashbulb Memory is often invoked to argue that strong emotion produces accurate memory, but the empirical finding is the opposite; the diagnostic feature of flashbulb memories is the dissociation between subjective vividness and objective accuracy, not enhanced fidelity.

## Prospective Memory

- domain: cognitive-science
- secondary_domains: [memory-research, executive-function]
- aliases: [memory for intentions, future memory]
- broader: [memory-systems]
- related: [implementation-intentions, executive-function, working-memory, episodic-memory]
- prerequisites: [long-term-memory, executive-function]

**definition**: Prospective Memory is the memory system responsible for remembering to perform a planned action at an appropriate future moment — either when a target time arrives (time-based) or when a triggering cue is encountered (event-based) — and uniquely combines retrospective storage of the intention with executive monitoring for the retrieval context.

**key_claim**: Prospective Memory failures are dissociable from retrospective memory failures: a person who can readily report what they intended to do nonetheless fails to act at the right moment, demonstrating that the executive-monitoring component of intention retrieval is the typical point of breakdown rather than content storage.

**warning**: Prospective Memory is often equated with a to-do list or general planning capacity, but it specifically denotes the cognitive system that bridges intention formation and context-cued retrieval; offloading intentions to external reminders bypasses prospective memory rather than training it.

## False Memory

- domain: cognitive-science
- secondary_domains: [memory-research, eyewitness-research]
- aliases: [memory distortion, memory illusion]
- broader: [reconstructive-memory, episodic-memory]
- related: [source-amnesia, autobiographical-memory, reconstructive-memory, source-monitoring]
- prerequisites: [long-term-memory, reconstructive-memory]

**definition**: False Memory is the confident recollection of events or details that did not in fact occur as remembered, produced by reconstructive processes that integrate gist representations, schema expectations, post-event suggestion, and source-monitoring failures into a coherent narrative indistinguishable phenomenologically from veridical recall.

**key_claim**: False Memory research, especially the DRM paradigm and eyewitness-suggestion studies, establishes that memory is constructive at retrieval rather than purely reproductive, and that the same mechanisms producing veridical recall also produce systematic distortions whenever stored gist conflicts with verbatim trace.

**warning**: False Memory should not be taken to imply that memory is generally unreliable; the same reconstructive system produces accurate gist recall most of the time, and the diagnostic concern is specifically when high subjective confidence coexists with verifiable error.

## Source Amnesia

- domain: cognitive-science
- secondary_domains: [memory-research, source-monitoring-research]
- aliases: [source-monitoring failure, source memory deficit]
- broader: [source-monitoring]
- related: [source-monitoring, false-memory, autobiographical-memory, semantic-memory]
- prerequisites: [long-term-memory, source-monitoring]

**definition**: Source Amnesia is the dissociation between preserved memory for content and impaired memory for the origin of that content — the speaker, location, modality, or time at which it was learned — and is characteristic of medial-temporal-lobe and frontal-lobe dysfunction as well as ordinary forgetting over long retention intervals.

**key_claim**: Source Amnesia explains why misinformation, rumor, and the illusory-truth effect are so resistant to correction: once the content trace decouples from its source attribution, the originally discredited claim re-enters memory as a free-standing fact whose epistemic status can no longer be re-evaluated against its provenance.

**warning**: Source Amnesia is sometimes treated as a neurological symptom alone, but the underlying source-monitoring failure is a graded property of normal memory that intensifies with delay, divided attention at encoding, and source-content similarity; clinical and everyday source amnesia lie on a single continuum.

## Long-Term Potentiation

- domain: cognitive-science
- secondary_domains: [neuroscience-of-learning, synaptic-plasticity]
- aliases: [LTP, Hebbian potentiation]
- broader: [neuroplasticity, memory-consolidation]
- related: [memory-consolidation, neuroplasticity, sleep-and-memory-consolidation, dopaminergic-reward-system]
- prerequisites: [neuroplasticity]

**definition**: Long-Term Potentiation is the persistent activity-dependent strengthening of synaptic transmission produced when a presynaptic input repeatedly succeeds in driving postsynaptic firing, first demonstrated by Bliss and Lømo in the rabbit hippocampus in 1973 and now accepted as the principal cellular mechanism by which experience encodes durable changes in the strength of neural connections.

**key_claim**: Long-Term Potentiation provides the strongest available cellular candidate for the Hebbian "neurons that fire together, wire together" principle, and its NMDA-receptor-dependent induction phase implements a precise coincidence-detection rule that links cellular plasticity directly to associative learning at the behavioral level.

**warning**: Long-Term Potentiation is often described as "the cellular basis of memory" without qualification, but the empirical bridge from synaptic strengthening in slice preparations to specific behavioral memories is much weaker than the slogan implies; LTP is necessary for many forms of learning but not sufficient evidence that any particular memory is stored at any particular synapse.

## Transformative Learning

- domain: cognitive-science
- secondary_domains: [adult-learning, educational-development]
- aliases: [Mezirow's theory, perspective transformation]
- broader: [andragogy, learning-theories]
- related: [andragogy, double-loop-learning, conceptual-change, reflective-thinking]
- prerequisites: [adult-learning, reflective-thinking]

**definition**: Transformative Learning, the theory developed by Jack Mezirow beginning in 1978, describes a distinct adult-learning process in which a disorienting dilemma destabilizes a previously taken-for-granted frame of reference and triggers critical reflection on one's assumptions, producing a structurally revised meaning perspective rather than the additive accumulation of new content within an unchanged frame.

**key_claim**: Transformative Learning differs from instrumental and communicative learning in that its endpoint is a reorganized epistemological framework rather than expanded content within the existing one; this is what makes it the canonical model for the developmental shifts that characterize adult education at its most significant.

**warning**: Transformative Learning is sometimes invoked for any subjectively meaningful insight, but Mezirow's construct requires structural change in habits of mind verified by altered action patterns; mere emotional resonance or temporary perspective-taking does not satisfy the criterion of perspective transformation.

## Kolb Experiential Learning Cycle

- domain: cognitive-science
- secondary_domains: [adult-learning, instructional-design]
- aliases: [Kolb cycle, experiential learning model, ELT]
- broader: [learning-theories, andragogy]
- related: [reflective-thinking, deweys-reflective-thinking, double-loop-learning, transformative-learning]
- prerequisites: [reflective-thinking]

**definition**: The Kolb Experiential Learning Cycle, formalized by David Kolb in 1984, describes learning as a four-phase recursive process — concrete experience, reflective observation, abstract conceptualization, and active experimentation — through which knowledge is created by the transformation of experience and in which a complete learning episode requires traversal of all four modes.

**key_claim**: The Kolb Experiential Learning Cycle frames learning as a structurally complete cycle rather than an act of acquisition: omitting any quadrant — for example, jumping from experience to action without reflection or abstraction — produces characteristic learning failures that the cycle's diagnostic structure makes recognizable.

**warning**: The Kolb Experiential Learning Cycle is often reduced to a personality typology of "learning styles" via Kolb's Learning Style Inventory, but the empirical evidence for stable, instruction-relevant style preferences is weak; the cycle's value lies in its account of phases of learning, not in matching teaching to fixed individual types.

## Cooperative Learning

- domain: cognitive-science
- secondary_domains: [instructional-design, social-learning]
- aliases: [Johnson and Johnson cooperative learning, structured peer learning]
- broader: [social-cognitive-theory, learning-theories]
- related: [reciprocal-teaching, communities-of-practice, social-cognitive-theory, observational-learning]
- prerequisites: [social-cognitive-theory]

**definition**: Cooperative Learning is an instructional approach, codified by David and Roger Johnson and by Robert Slavin, in which small heterogeneous groups work together on learning tasks under conditions of positive interdependence, individual accountability, promotive interaction, deliberate use of social skills, and structured group processing — five features that distinguish it from unstructured group work.

**key_claim**: Cooperative Learning produces consistent positive effects on academic achievement, intergroup relations, and motivation across grade levels and subjects when the five constitutive conditions are present, but the effect collapses to zero or negative when groups lack positive interdependence or individual accountability — making structure, not grouping per se, the active ingredient.

**warning**: Cooperative Learning is often confused with simply assigning students to groups, but the empirical literature is consistent: unstructured group work produces free-riding, sucker effects, and unequal participation; the term Cooperative Learning is reserved for designs that engineer the five conditions explicitly.

## Transfer-Appropriate Processing

- domain: cognitive-science
- secondary_domains: [memory-research, learning-science]
- aliases: [TAP framework, encoding-retrieval match]
- broader: [encoding-specificity-principle, levels-of-processing]
- related: [encoding-specificity-principle, levels-of-processing, context-dependent-memory, near-transfer]
- prerequisites: [encoding-specificity-principle, levels-of-processing]

**definition**: Transfer-Appropriate Processing, articulated by Morris, Bransford, and Franks in 1977, is the principle that retention performance depends not on the depth of encoding per se but on the degree of overlap between the cognitive operations engaged at study and those required at test; encoding is "good" only relative to the demands of the eventual retrieval task.

**key_claim**: Transfer-Appropriate Processing reframes the levels-of-processing finding by predicting cases where shallow encoding outperforms deep encoding — for instance, when the test requires rhyme recognition rather than semantic recognition — thereby exposing the relational rather than absolute nature of encoding quality.

**warning**: Transfer-Appropriate Processing is often confused with the encoding-specificity principle, but they are distinct: encoding specificity emphasizes overlap of cues and contexts, while transfer-appropriate processing specifically concerns overlap of cognitive operations and processing demands.

## Near Transfer

- domain: cognitive-science
- secondary_domains: [learning-science, transfer-research]
- aliases: [proximal transfer, low-road transfer]
- broader: [transfer-of-learning]
- related: [far-transfer, transfer-of-learning, transfer-appropriate-processing, knowledge-transfer]
- prerequisites: [transfer-of-learning]

**definition**: Near Transfer is the application of learned knowledge or skill to a new task that shares substantial surface and structural features with the original training context, contrasted with far transfer to dissimilar contexts; near transfer typically arises from highly automated procedural knowledge and shows reliably in trained populations whereas far transfer remains empirically scarce.

**key_claim**: Near Transfer is robust and ubiquitous in skill learning while far transfer is rare and usually requires explicit instruction in abstract principles; this asymmetry is one of the most stable findings in transfer research and underwrites the recommendation to teach for transfer explicitly rather than hoping it emerges.

**warning**: Near Transfer should not be dismissed as "merely" doing a similar task; it is the workhorse of practical skill acquisition, and overstating its ease while pursuing far transfer leads to curricula that achieve neither — failing to automate the proximal application while assuming distant generalization will follow.

## Seductive Details Effect

- domain: cognitive-science
- secondary_domains: [multimedia-learning, instructional-design]
- aliases: [seductive details, interesting irrelevancies]
- broader: [coherence-principle, cognitive-load-theory]
- related: [coherence-principle, cognitive-theory-of-multimedia-learning, extraneous-cognitive-load, redundancy-effect]
- prerequisites: [cognitive-load-theory, cognitive-theory-of-multimedia-learning]

**definition**: The Seductive Details Effect is the empirical finding, established by Garner, Brown, and Sanders in 1989 and replicated extensively by Mayer's group, that adding interesting but instructionally irrelevant material to a lesson — anecdotes, photographs, sound effects — reduces retention and transfer of the core content despite raising self-reported interest and engagement.

**key_claim**: The Seductive Details Effect demonstrates that subjective engagement and learning outcomes can dissociate sharply: the very features that make a lesson feel more interesting can divert limited working-memory capacity from the essential schema-construction work, producing an inverse relation between rated engagement and measured comprehension.

**warning**: The Seductive Details Effect is often misread as a blanket prohibition on illustrations or stories, but the boundary condition is whether the added material competes with the conceptual core for processing capacity; coherent narratives that carry the explanation forward do not produce the effect, while ornamental anecdotes do.

## Coherence Principle

- domain: cognitive-science
- secondary_domains: [multimedia-learning, instructional-design]
- aliases: [coherence rule, exclusion principle]
- broader: [cognitive-theory-of-multimedia-learning]
- related: [seductive-details-effect, redundancy-effect, extraneous-cognitive-load, cognitive-theory-of-multimedia-learning]
- prerequisites: [cognitive-theory-of-multimedia-learning, cognitive-load-theory]

**definition**: The Coherence Principle, one of the design principles of Mayer's Cognitive Theory of Multimedia Learning, states that people learn more deeply from multimedia presentations when extraneous words, pictures, and sounds are excluded rather than included, because every additional element competes for limited working-memory capacity even when it is intrinsically appealing.

**key_claim**: The Coherence Principle predicts a reliable retention and transfer benefit when interesting-but-irrelevant material is removed from a lesson, with effect sizes typically in the d = 0.3 to 0.5 range across multimedia studies, establishing exclusion of inessentials as a more effective design move than inclusion of supposedly motivating extras.

**warning**: The Coherence Principle is often resisted on the intuition that "more is more" or that extra elements add motivation; the empirical record consistently shows the opposite, and treating coherence as optional polish rather than core architecture produces measurably worse instruction.

## Pre-Training Principle

- domain: cognitive-science
- secondary_domains: [multimedia-learning, instructional-design]
- aliases: [pre-training, vocabulary pre-instruction]
- broader: [cognitive-theory-of-multimedia-learning]
- related: [cognitive-theory-of-multimedia-learning, cognitive-load-theory, prior-knowledge-activation, schema-construction]
- prerequisites: [cognitive-theory-of-multimedia-learning, cognitive-load-theory]

**definition**: The Pre-Training Principle, one of Mayer's multimedia design principles, holds that learning of complex material is improved when learners first acquire the names and characteristics of the key components in a brief preparatory phase, so that during the main lesson working memory can be devoted to integrating cause-and-effect relations rather than simultaneously bootstrapping a vocabulary.

**key_claim**: The Pre-Training Principle predicts that even very brief prior exposure to component names and features substantially improves transfer from a subsequent system-level explanation, because pre-training shifts intrinsic load onto a separate phase rather than competing with relational processing during the main lesson.

**warning**: The Pre-Training Principle should not be applied as if more prior detail is always better; the empirical sweet spot is brief vocabulary-and-feature pre-training, and exhaustive front-loading can produce the same overload it was meant to prevent.

## Psychological Reactance

- domain: cognitive-science
- secondary_domains: [motivational-psychology, social-psychology]
- aliases: [reactance theory, freedom restoration motivation]
- broader: [motivational-psychology, autonomy]
- related: [autonomy, intrinsic-motivation, controlling-teaching-styles, self-determination-theory]
- prerequisites: [motivational-psychology, autonomy]

**definition**: Psychological Reactance is the motivational state, theorized by Jack Brehm in 1966, that arises when a person perceives a salient freedom of choice as threatened or eliminated, producing an energized drive to restore the threatened freedom — often by performing the prohibited act, derogating the source of restriction, or seeking alternative routes to the same end.

**key_claim**: Psychological Reactance explains why directive and controlling persuasion frequently backfires: the perceived threat to autonomy activates a freedom-restoration motive that competes with — and in many cases overrides — the intended persuasive influence, producing the boomerang effect documented across health-communication, education, and parenting research.

**warning**: Psychological Reactance is often invoked as a synonym for stubbornness, but the construct is specifically about freedom-restoration motivation triggered by perceived threat to choice; not all opposition to a request reflects reactance, and not all reactance manifests as overt defiance.

## Four-Phase Model of Interest Development

- domain: cognitive-science
- secondary_domains: [motivational-psychology, educational-psychology]
- aliases: [Hidi Renninger model, four-phase interest model]
- broader: [motivational-psychology, individual-interest, situational-interest]
- related: [individual-interest, situational-interest, intrinsic-motivation, curiosity]
- prerequisites: [individual-interest, situational-interest]

**definition**: The Four-Phase Model of Interest Development, proposed by Suzanne Hidi and K. Ann Renninger in 2006, describes interest as a developmental construct that progresses through four sequential phases — triggered situational interest, maintained situational interest, emerging individual interest, and well-developed individual interest — each requiring distinct external supports for transition to the next.

**key_claim**: The Four-Phase Model of Interest Development reframes interest as a developmental trajectory rather than a stable trait, and identifies the maintained-situational phase as the critical bottleneck where most learners fail to internalize a triggered interest into an enduring personal interest unless content-relevant tasks and meaningful purpose are scaffolded.

**warning**: The Four-Phase Model of Interest Development should not be read as implying that all triggered interest will or should progress to individual interest; the model is descriptive of the conditions under which progression is possible, not a normative claim that every spark must be cultivated to maturity.

## Control-Value Theory

- domain: cognitive-science
- secondary_domains: [motivational-psychology, achievement-emotions-research]
- aliases: [CVT, Pekrun's control-value theory]
- broader: [achievement-emotions, motivational-psychology]
- related: [achievement-emotions, attribution-theory, self-efficacy, expectancy-value-theory]
- prerequisites: [attribution-theory, self-efficacy]

**definition**: Control-Value Theory, developed by Reinhard Pekrun, is an integrative framework for achievement emotions in which the type and intensity of emotion experienced in achievement settings is determined jointly by two appraisals — the perceived controllability of the activity or outcome and the subjective value placed on it — yielding a systematic taxonomy of activity, prospective-outcome, and retrospective-outcome emotions.

**key_claim**: Control-Value Theory predicts the emotional consequences of any achievement situation by intersecting control and value: high control combined with high positive value produces enjoyment and pride, low control combined with high value produces anxiety and hopelessness, and these distinct emotions then channel attention, motivation, and self-regulation in characteristic ways.

**warning**: Control-Value Theory is sometimes treated as a list of academic emotions, but its theoretical contribution is the appraisal-based generative mechanism; cataloguing emotions without modeling the control and value appraisals that produce them strips the theory of its predictive structure.

## Social Comparison Theory

- domain: cognitive-science
- secondary_domains: [social-psychology, motivational-psychology]
- aliases: [Festinger's social comparison theory]
- broader: [social-cognitive-theory, motivational-psychology]
- related: [self-efficacy, vicarious-experience, self-concept, mastery-climate-vs-performance-climate]
- prerequisites: [self-concept]

**definition**: Social Comparison Theory, advanced by Leon Festinger in 1954, holds that humans possess a fundamental drive to evaluate their opinions and abilities, and in the absence of objective standards they do so by comparing themselves to similar others, with upward comparisons typically motivating self-improvement and downward comparisons typically protecting self-esteem.

**key_claim**: Social Comparison Theory establishes that self-evaluation is intrinsically relational rather than absolute, which explains why classroom-level comparison structures — visible rankings, public grading distributions, ability-grouping practices — exert outsized effects on motivation and self-concept independent of objective performance.

**warning**: Social Comparison Theory is often simplified to "upward = bad, downward = good," but the consequences depend on the comparer's identification with the target and on the construal as inspiring versus contrastive; the same upward comparison can produce motivation in one frame and demoralization in another.

## Epistemic Curiosity

- domain: cognitive-science
- secondary_domains: [motivational-psychology, curiosity-research]
- aliases: [intellectual curiosity, knowledge-seeking curiosity]
- broader: [curiosity, motivational-psychology]
- related: [curiosity, intrinsic-motivation, need-for-cognition, four-phase-model-of-interest-development]
- prerequisites: [curiosity, intrinsic-motivation]

**definition**: Epistemic Curiosity is the desire to acquire new information for its own sake, distinguished by Berlyne and elaborated by Litman into two facets — interest-type curiosity that anticipates the pleasure of new knowledge and deprivation-type curiosity that responds aversively to a felt gap in understanding — both of which energize information-seeking behavior independent of instrumental reward.

**key_claim**: Epistemic Curiosity is dissociable into the I-type and D-type facets identified by Litman, with the deprivation form predicting persistence on difficult information-seeking tasks better than the interest form, supporting the view that the aversive "knowledge gap" signal is the engine of sustained intellectual inquiry.

**warning**: Epistemic Curiosity is sometimes treated as an undifferentiated appetite for novelty, but the I-type/D-type distinction matters because they have different antecedents, different time courses, and different relations to academic outcomes; collapsing them obscures the mechanism.

## Achievement Emotions

- domain: cognitive-science
- secondary_domains: [motivational-psychology, educational-psychology]
- aliases: [academic emotions, achievement-related emotions]
- broader: [motivational-psychology, academic-emotions]
- related: [control-value-theory, academic-emotions, attribution-dependent-emotion, attribution-theory]
- prerequisites: [academic-emotions]

**definition**: Achievement Emotions are the discrete affective states experienced in achievement contexts — enjoyment, hope, pride, anxiety, anger, shame, hopelessness, boredom, and relief — that emerge from appraisals of control and value over learning activities and their outcomes, and that systematically channel attention, motivation, strategy use, and self-regulation in characteristic directions.

**key_claim**: Achievement Emotions are not by-products of cognition but causally efficacious regulators of learning behavior: they bias which information is encoded, which strategies are deployed, and how persistence is allocated, with reciprocal feedback loops in which strategy success and failure further modulate emotional experience.

**warning**: Achievement Emotions are often grouped under broad labels like "academic affect," but the construct depends on the discrete-emotions distinction; treating boredom and anxiety as interchangeable negative states erases their opposite implications for engagement and intervention.

## Regulatory Fit Theory

- domain: cognitive-science
- secondary_domains: [motivational-psychology, decision-research]
- aliases: [Higgins regulatory fit, fit theory]
- broader: [regulatory-focus-theory, motivational-psychology]
- related: [regulatory-focus-theory, intrinsic-motivation, motivational-regulation, self-determination-theory]
- prerequisites: [regulatory-focus-theory]

**definition**: Regulatory Fit Theory, advanced by E. Tory Higgins, proposes that motivation and value are intensified when the manner of pursuing a goal matches the goal-pursuer's chronic or situational regulatory focus — promotion focus paired with eagerness strategies, prevention focus paired with vigilance strategies — producing a "feeling right" state that strengthens engagement, persuasion, and persistence independent of outcome value.

**key_claim**: Regulatory Fit Theory predicts that the value of a chosen action is amplified when strategy and orientation align, even when the action's objective outcome is held constant; this turns "fit" into an additional source of value that operates over and above the standard expectancy-value calculus.

**warning**: Regulatory Fit Theory is often confused with regulatory focus theory itself, but they are distinct: regulatory focus identifies promotion and prevention orientations, while regulatory fit specifies the match between orientation and strategy as the proximal mechanism producing the value-amplification effect.

## Winne's Model of Self-Regulated Learning

- domain: cognitive-science
- secondary_domains: [self-regulated-learning, metacognition]
- aliases: [Winne and Hadwin model, four-stage SRL model]
- broader: [self-regulated-learning, metacognition]
- related: [self-regulated-learning, metacognitive-monitoring, metacognitive-regulation, monitoring-control-loop]
- prerequisites: [self-regulated-learning, metacognition]

**definition**: Winne's Model of Self-Regulated Learning, developed by Philip Winne and Allyson Hadwin in 1998, decomposes SRL into a four-stage information-processing cycle — task definition, goal setting and planning, enactment of strategies, and adaptation — within which monitoring continuously compares evolving products against standards and triggers cognitive, behavioral, or motivational control responses.

**key_claim**: Winne's Model of Self-Regulated Learning treats SRL as a monitoring-and-control loop running on cognitive operations rather than as a sequence of phases with sharp boundaries, which makes it especially well-suited to fine-grained trace methodologies such as study-tactic logging and eye-tracking that capture moment-by-moment regulation.

**warning**: Winne's Model of Self-Regulated Learning is frequently confused with Zimmerman's cyclical phase model; both describe SRL but at different grain sizes, and the Winne model's information-processing emphasis on continuous monitoring within cognitive operations is distinct from Zimmerman's macro-cyclical forethought–performance–reflection structure.

## WOOP Method

- domain: cognitive-science
- secondary_domains: [self-regulation, motivational-psychology]
- aliases: [WOOP, Wish Outcome Obstacle Plan, mental contrasting with implementation intentions]
- broader: [mental-contrasting, implementation-intentions]
- related: [mental-contrasting, implementation-intentions, goal-setting, action-control-theory]
- prerequisites: [mental-contrasting, implementation-intentions]

**definition**: The WOOP Method, developed by Gabriele Oettingen, is a structured self-regulation protocol that integrates mental contrasting with implementation intentions through four sequential steps — identifying a meaningful Wish, vividly imagining the best Outcome, identifying the chief inner Obstacle, and forming an if-then Plan — and has been validated as a transferable life-skill for translating intentions into reliable action.

**key_claim**: The WOOP Method outperforms either mental contrasting or implementation intentions alone in head-to-head trials because it uses the contrast step to bind motivation to the realistic obstacle and the if-then step to automate the response when the obstacle is encountered, exploiting the complementary strengths of the two component techniques.

**warning**: The WOOP Method should not be applied to wishes the person cannot influence; mental contrasting with infeasible outcomes produces disengagement rather than energization, and the WOOP Method's empirical track record presumes the wish lies within the person's plausible reach.

## Action Control Theory

- domain: cognitive-science
- secondary_domains: [motivational-psychology, self-regulation]
- aliases: [Kuhl's action control theory, state vs action orientation theory]
- broader: [motivational-psychology, volitional-control]
- related: [volitional-control, implementation-intentions, woop-method, intention-behavior-gap]
- prerequisites: [volitional-control, motivational-psychology]

**definition**: Action Control Theory, developed by Julius Kuhl, distinguishes the post-decisional volitional processes that translate an intention into action from the pre-decisional motivational processes that produce the intention itself, and identifies a chronic individual difference between action-oriented persons who efficiently disengage from rumination and state-oriented persons who tend to dwell on past states or future possibilities.

**key_claim**: Action Control Theory explains the intention-behavior gap as a failure of volitional self-regulation rather than weak motivation: state-oriented individuals form intentions of equal strength but show systematically poorer translation into action under demanding conditions, with affect-regulation deficits as the proximal mechanism.

**warning**: Action Control Theory should not be read as classifying people into permanent "action" or "state" types; the distinction is dimensional, context-sensitive, and trainable, and treating it as a fixed personality category misses its diagnostic value for identifying when self-regulatory support is needed.

## Lateral Thinking

- domain: cognitive-science
- secondary_domains: [creativity-research, problem-solving]
- aliases: [De Bono lateral thinking, sideways thinking]
- broader: [creative-problem-solving, divergent-thinking]
- related: [divergent-thinking, creative-problem-solving, first-principles-thinking, productive-failure]
- prerequisites: [divergent-thinking]

**definition**: Lateral Thinking, a term coined by Edward de Bono in 1967, designates problem-solving by deliberate restructuring of the problem representation through provocative perturbations such as random entry, reversal, fractionation, and concept challenge, contrasted with vertical thinking that proceeds by sequential logical refinement within a fixed frame.

**key_claim**: Lateral Thinking treats the solution space as bounded primarily by the problem's framing rather than by available evidence, which is why provocations that violate the current framing can unblock progress even when they are illogical in their own right — a strategy fundamentally different from improving the search within the current frame.

**warning**: Lateral Thinking is often equated with general creativity, but the term denotes a specific set of frame-restructuring techniques that complement rather than replace analytical thinking; treating it as an alternative to evidence-based reasoning misuses the construct.

## Divergent Thinking

- domain: cognitive-science
- secondary_domains: [creativity-research, individual-differences]
- aliases: [generative thinking]
- broader: [creative-problem-solving]
- related: [creative-problem-solving, lateral-thinking, fluid-intelligence, cognitive-flexibility]
- prerequisites: [creative-problem-solving]

**definition**: Divergent Thinking is the cognitive capacity, theorized by J. P. Guilford in 1956, to generate many varied and original responses to an open-ended prompt — typically scored on fluency, flexibility, originality, and elaboration via tasks such as the Alternative Uses Test — and contrasted with convergent thinking that searches for the single correct answer.

**key_claim**: Divergent Thinking is necessary but not sufficient for creative achievement: scores on divergent-thinking tasks correlate modestly with real-world creative output, and the additional ingredients are the convergent evaluation that selects among generated alternatives and the domain-specific knowledge that constrains generation to viable possibilities.

**warning**: Divergent Thinking is often treated as a synonym for creativity, but the construct only captures the generative phase; high divergent-thinking scores without the evaluative and knowledge-driven phases produce volume without quality, and creativity research consistently identifies the integration of generation and evaluation as the operative skill.

## Counterfactual Reasoning

- domain: cognitive-science
- secondary_domains: [reasoning-and-decision-making, causal-cognition]
- aliases: [counterfactual thinking, what-if reasoning]
- broader: [reasoning-under-uncertainty, causal-attribution]
- related: [causal-attribution, reasoning-under-uncertainty, hindsight-bias, regulatory-fit-theory]
- prerequisites: [causal-attribution, mental-model]

**definition**: Counterfactual Reasoning is the capacity to construct and evaluate mental simulations of how the world would have been if some past event had unfolded differently, and underpins causal inference, regret and relief, attribution of responsibility, learning from outcomes, and the construction of "if only" alternatives that drive both negative emotion and adaptive future planning.

**key_claim**: Counterfactual Reasoning is the principal cognitive bridge between outcome experience and learning: the alternatives a person spontaneously generates after an outcome shape attributions, emotional reactions, and behavioral adjustments, which is why interventions that train upward-additive counterfactuals produce measurable gains in subsequent performance.

**warning**: Counterfactual Reasoning should not be treated as inherently maladaptive on the basis of regret research; the same machinery that produces ruminative regret also produces preparatory planning and causal learning, and the adaptive value depends on the direction (upward vs downward) and structure (additive vs subtractive) of the alternative generated.

## Creative Problem-Solving

- domain: cognitive-science
- secondary_domains: [creativity-research, problem-solving]
- aliases: [CPS, Osborn-Parnes process]
- broader: [problem-based-learning]
- related: [divergent-thinking, lateral-thinking, productive-failure, productive-struggle]
- prerequisites: [divergent-thinking]

**definition**: Creative Problem-Solving denotes both the broad cognitive capacity to produce novel and useful solutions to ill-structured problems and the specific staged process — clarifying, ideating, developing, implementing — codified by Alex Osborn and Sidney Parnes that alternates divergent and convergent thinking at each stage to channel creative production toward viable solutions.

**key_claim**: Creative Problem-Solving requires the disciplined alternation of divergent and convergent phases at each stage of the process; mixing the two prematurely — for instance, evaluating ideas during ideation — predictably collapses the solution space and produces conventional rather than creative outputs.

**warning**: Creative Problem-Solving is often equated with brainstorming, but brainstorming is a single technique used inside the ideation stage; the full Creative Problem-Solving process includes problem clarification, solution development, and implementation planning, and shortcutting any phase typically degrades the final product.

## Reasoning Under Uncertainty

- domain: cognitive-science
- secondary_domains: [reasoning-and-decision-making, judgment-research]
- aliases: [probabilistic reasoning, judgment under uncertainty]
- broader: [probabilistic-thinking, bayesian-reasoning]
- related: [probabilistic-thinking, bayesian-reasoning, heuristics-and-biases, dual-process-theory]
- prerequisites: [probabilistic-thinking]

**definition**: Reasoning Under Uncertainty is the family of judgment processes by which people draw inferences and choose actions when relevant outcomes, probabilities, or states of the world are not known with certainty, encompassing both formal probabilistic competence and the heuristic shortcuts described by Tversky and Kahneman that produce systematic departures from normative Bayesian inference.

**key_claim**: Reasoning Under Uncertainty in everyday cognition is characteristically heuristic rather than calculative, with availability, representativeness, anchoring, and affect substituting for formal probability assessment; this is adaptive in many environments but produces predictable biases when statistical structure violates the heuristic's assumptions.

**warning**: Reasoning Under Uncertainty is often discussed as if it required formal probability instruction to remediate, but the empirical evidence supports a more nuanced view: representing problems in frequency formats, providing visual outcome arrays, and using natural-sample design substantially improve performance without explicit Bayesian training.

## Planning Fallacy

- domain: cognitive-science
- secondary_domains: [judgment-research, project-management]
- aliases: [Kahneman planning fallacy, optimism in planning]
- broader: [cognitive-bias, optimism-bias]
- related: [cognitive-bias, sunk-cost-fallacy, anchoring-bias, hindsight-bias]
- prerequisites: [cognitive-bias]

**definition**: The Planning Fallacy, introduced by Daniel Kahneman and Amos Tversky in 1979, is the systematic tendency for individuals and organizations to underestimate the time, cost, and risk of future actions while overestimating their benefits, even when the same individuals know that comparable past projects routinely overran their forecasts.

**key_claim**: The Planning Fallacy persists despite contradicting reference-class evidence because forecasters anchor on the inside view — features specific to the current plan — rather than the outside view that aggregates the base rate of comparable past projects; this is why reference-class forecasting reliably outperforms intuitive estimation even with no additional task knowledge.

**warning**: The Planning Fallacy should not be treated as remediable by simple exhortation to "be realistic"; the bias is robust against feedback because the inside view feels more diagnostic than base rates, and durable correction requires structural debiasing such as mandatory reference-class comparison rather than greater self-discipline.

## Sunk Cost Fallacy

- domain: cognitive-science
- secondary_domains: [decision-research, behavioral-economics]
- aliases: [sunk cost effect, escalation of commitment]
- broader: [cognitive-bias]
- related: [cognitive-bias, framing-effect, anchoring-bias, planning-fallacy]
- prerequisites: [cognitive-bias]

**definition**: The Sunk Cost Fallacy is the tendency to continue investing resources in a course of action because of previously incurred and irrecoverable costs, in violation of the normative principle that only marginal future costs and benefits should determine current choice; the fallacy underwrites escalating commitment to failing projects, ventures, and relationships.

**key_claim**: The Sunk Cost Fallacy is robust to expertise and statistical instruction because it is supported by intuitions about waste-aversion and consistency that operate at a deep level of decision representation; debiasing interventions that target the marginal-only principle abstractly tend to fail, while interventions that reframe the choice as a fresh decision are more effective.

**warning**: The Sunk Cost Fallacy should not be invoked whenever someone persists with a difficult project; persistence based on a prospective expected-value calculation is rational, and the fallacy is specifically the case where past investment is the operative reason for continuation rather than future expected return.

## Anchoring Bias

- domain: cognitive-science
- secondary_domains: [judgment-research, decision-research]
- aliases: [anchoring effect, anchoring-and-adjustment]
- broader: [cognitive-bias, heuristics-and-biases]
- related: [cognitive-bias, heuristics-and-biases, framing-effect, availability-heuristic]
- prerequisites: [cognitive-bias, heuristics-and-biases]

**definition**: Anchoring Bias is the systematic influence of an initially considered numerical value — even when transparently arbitrary — on subsequent quantitative judgments, demonstrated repeatedly by Tversky and Kahneman and explained by insufficient adjustment from the anchor and by selective accessibility of anchor-consistent information during the judgment process.

**key_claim**: Anchoring Bias is one of the most replicable findings in judgment research, occurring even when participants are warned about the anchor, when the anchor is patently irrelevant, and when expert judgments are at stake; this resilience marks anchoring as a fundamental feature of the comparison-based judgment system rather than a correctable error.

**warning**: Anchoring Bias is often described as a problem of insufficient cognitive effort, but the selective-accessibility evidence shows that anchors bias judgment by changing what comes to mind during deliberation, not only by truncating adjustment; this means more careful thinking does not eliminate the bias and may even amplify it.

## Framing Effect

- domain: cognitive-science
- secondary_domains: [decision-research, behavioral-economics]
- aliases: [framing bias, attribute framing, risky choice framing]
- broader: [cognitive-bias, heuristics-and-biases]
- related: [cognitive-bias, anchoring-bias, sunk-cost-fallacy, prospect-theory]
- prerequisites: [cognitive-bias]

**definition**: The Framing Effect is the systematic shift in preference produced by logically equivalent reformulations of the same decision problem — most famously the gain-versus-loss framing in Tversky and Kahneman's Asian disease problem — and is taken by prospect theory as evidence that choice is governed by reference-dependent value functions rather than expected-utility maximization over absolute outcomes.

**key_claim**: The Framing Effect demonstrates that the descriptive invariance assumption of classical decision theory fails systematically: the same decision-maker reliably reverses preferences when the same outcomes are described as gains versus losses, indicating that the cognitive representation of a problem is itself a determinant of choice rather than a transparent window onto stable preferences.

**warning**: The Framing Effect should not be treated as a sign of irrationality to be eliminated; reference-dependent valuation is also adaptive in many environments, and the diagnostic concern is specifically when frame manipulation is used to engineer choices that the chooser would not endorse on reflective consideration.

## Representativeness Heuristic

- domain: cognitive-science
- secondary_domains: [judgment-research, heuristics-research]
- aliases: [representativeness, similarity heuristic]
- broader: [heuristics-and-biases, cognitive-bias]
- related: [heuristics-and-biases, base-rate-neglect, availability-heuristic, attribute-substitution]
- prerequisites: [heuristics-and-biases]

**definition**: The Representativeness Heuristic, identified by Tversky and Kahneman in 1972, is the cognitive shortcut by which people judge the probability that an instance belongs to a category by the degree to which it resembles the category's prototypical features, often producing systematic violations of probability theory such as base-rate neglect, the conjunction fallacy, and insensitivity to sample size.

**key_claim**: The Representativeness Heuristic explains a coherent family of biases — base-rate neglect, the conjunction fallacy (Linda problem), regression neglect, and the gambler's fallacy — as expressions of the same underlying substitution of similarity judgment for probability judgment, which is why these biases pattern together across populations rather than reflecting independent errors.

**warning**: The Representativeness Heuristic should not be dismissed as a mere error; similarity-based judgment is fast, often accurate, and frequently the best available strategy when statistical information is absent or unreliable, and the diagnostic problem is specifically when statistical information is present and ignored.

## Construal Level Theory

- domain: cognitive-science
- secondary_domains: [social-psychology, decision-research]
- aliases: [CLT social-psychology, psychological distance theory]
- broader: [social-cognitive-theory, motivational-psychology]
- related: [motivational-psychology, regulatory-focus-theory, regulatory-fit-theory, planning-fallacy]
- prerequisites: [motivational-psychology]

**definition**: Construal Level Theory, developed by Yaacov Trope and Nira Liberman, holds that psychological distance — temporal, spatial, social, or hypothetical — systematically shifts the abstractness of mental representation: distant entities are construed in high-level abstract terms that emphasize core features and goals, while near entities are construed in low-level concrete terms that emphasize incidental features and means.

**key_claim**: Construal Level Theory predicts a coherent family of effects across temporal discounting, prediction, planning, persuasion, and self-control by linking psychological distance to representation abstractness, with distance-induced abstraction producing more goal-consistent and value-consistent choices when the relevant judgment is at the high level of construal.

**warning**: Construal Level Theory should not be confused with construct-level distinctions such as concrete vs abstract reasoning per se; the theory's specific contribution is the systematic relationship between psychological distance and construal level, and treating any concrete-versus-abstract framing as a CLT effect dilutes the construct.

## Second Brain

- domain: cognitive-science
- secondary_domains: [personal-knowledge-management, productivity]
- aliases: [Forte second brain, building a second brain, BASB]
- broader: [personal-knowledge-management, externalized-cognitive-architecture]
- related: [personal-knowledge-base, externalized-cognitive-architecture, cognitive-offloading, knowledge-distillation]
- prerequisites: [personal-knowledge-management]

**definition**: A Second Brain, in the sense popularized by Tiago Forte in 2022, is a deliberately maintained external system for capturing, organizing, distilling, and expressing personally meaningful information so that it can be retrieved and recombined over years without depending on biological memory, supporting the broader claim that an externalized knowledge architecture functions as a working extension of cognition.

**key_claim**: A Second Brain reframes personal-knowledge management as a productivity infrastructure rather than a research practice, with its CODE workflow (Capture, Organize, Distill, Express) prescribing a pipeline that converts raw inputs into reusable creative output rather than archived information for its own sake.

**warning**: A Second Brain is often interpreted as a recommendation to capture more, but Forte's emphasis on Distill and Express makes clear that capture without progressive summarization and reuse produces a hoard rather than an extension of cognition; the diagnostic feature of an effective Second Brain is leverage, not volume.

## Knowledge Distillation

- domain: cognitive-science
- secondary_domains: [personal-knowledge-management, learning-science]
- aliases: [progressive distillation, summarization layering]
- broader: [personal-knowledge-management, knowledge-compilation]
- related: [progressive-summarization, knowledge-compilation, atomic-notes, second-brain]
- prerequisites: [personal-knowledge-management]

**definition**: Knowledge Distillation, in the personal-knowledge-management sense, is the iterative reduction of captured material into progressively higher-leverage summaries — typically through layered highlighting, restating in one's own words, and atomicizing into single-claim notes — designed to produce retrieval-friendly forms of knowledge whose cost of re-access is much lower than the original source.

**key_claim**: Knowledge Distillation predicts that the value of a personal-knowledge system scales not with the volume of captured information but with the quality of distillation passes performed on it; well-distilled small corpora outperform poorly-distilled large ones for the operative task of leveraging past learning into future work.

**warning**: Knowledge Distillation should not be confused with mere summarization; the distinguishing feature is iterative re-encounter and re-encoding across time, and a single one-shot summary produced at capture and never revisited fails to deliver the consolidation and integration benefits that distillation is intended to produce.

## Idea Emergence

- domain: cognitive-science
- secondary_domains: [creativity-research, personal-knowledge-management]
- aliases: [emergent ideation, bottom-up insight]
- broader: [creative-problem-solving, knowledge-graph]
- related: [creative-problem-solving, knowledge-graph, knowledge-distillation, linking-your-thinking]
- prerequisites: [creative-problem-solving, knowledge-graph]

**definition**: Idea Emergence, in the personal-knowledge-management and creativity tradition, denotes the bottom-up arising of novel insights from the dense interaction of accumulated atomic notes and their links rather than from top-down deliberate problem-solving, formalized by Niklas Luhmann's Zettelkasten claim that the slip-box is a thinking partner whose surprising suggestions arise from local link density.

**key_claim**: Idea Emergence reframes creativity as a property of well-connected knowledge graphs rather than an act of solitary cognition: the emergent insight is structurally available in the graph before any individual realization, and the practitioner's role is to maintain the conditions under which encounters with the relevant juxtaposition become probable.

**warning**: Idea Emergence is often invoked as a justification for collecting notes without consequence, but the empirical evidence from productive PKM practitioners is that emergence requires both atomicity (so ideas are recombinable) and active linking (so juxtapositions surface), and a passive corpus produces neither.

## Linking Your Thinking

- domain: cognitive-science
- secondary_domains: [personal-knowledge-management, note-making]
- aliases: [LYT, Nick Milo LYT, MOC method]
- broader: [personal-knowledge-management, maps-of-content]
- related: [maps-of-content, atomic-notes, knowledge-graph, second-brain]
- prerequisites: [personal-knowledge-management, maps-of-content]

**definition**: Linking Your Thinking, the framework articulated by Nick Milo, is a personal-knowledge-management approach centered on Maps of Content — curated index notes that group related material — as the primary structuring device for an evolving note network, contrasted with rigid hierarchical folders and with pure bottom-up Zettelkasten practice.

**key_claim**: Linking Your Thinking treats Maps of Content as living scaffolds that evolve with the note collection rather than as fixed taxonomies imposed in advance, which is the structural feature that distinguishes the LYT approach from both top-down classification systems and from purely emergent linking practices.

**warning**: Linking Your Thinking should not be reduced to "just make MOCs"; the framework explicitly emphasizes the iterative interplay of capture, atomic note-making, and Map of Content curation, and skipping the atomic-note layer leaves nothing meaningful for the maps to organize.

## Psychological Safety

- domain: cognitive-science
- secondary_domains: [organizational-psychology, team-research]
- aliases: [team psychological safety, Edmondson safety]
- broader: [organizational-psychology, social-cognitive-theory]
- related: [self-compassion, productive-failure, communities-of-practice, growth-mindset]
- prerequisites: [social-cognitive-theory]

**definition**: Psychological Safety, defined by Amy Edmondson in 1999, is the shared belief among team members that the team is safe for interpersonal risk-taking — for asking questions, admitting mistakes, raising concerns, and proposing untested ideas — without fear of humiliation, punishment, or career penalty, and is now recognized as a critical antecedent of team learning behavior and performance.

**key_claim**: Psychological Safety is the strongest single team-level predictor of effective learning behaviors such as error reporting, help-seeking, and constructive challenge, and Google's Project Aristotle identified it as the most consistent differentiator of high-performing teams across the dimensions they studied.

**warning**: Psychological Safety should not be confused with comfort or absence of conflict; high-safety teams routinely engage in vigorous disagreement and hold high performance standards, and the operative distinction is the absence of interpersonal threat for raising substantive concerns rather than the absence of substantive concerns themselves.

## Self-Compassion

- domain: cognitive-science
- secondary_domains: [positive-psychology, emotion-regulation]
- aliases: [Neff self-compassion, compassionate self-relating]
- broader: [emotional-regulation, self-concept]
- related: [psychological-safety, growth-mindset, emotional-regulation, self-concept]
- prerequisites: [emotional-regulation, self-concept]

**definition**: Self-Compassion, formalized by Kristin Neff in 2003, is a triadic stance toward one's own suffering composed of self-kindness rather than self-judgment, recognition of common humanity rather than isolation, and mindful awareness rather than over-identification with painful states; it is psychometrically distinct from self-esteem and predicts adaptive responses to failure independent of self-evaluative content.

**key_claim**: Self-Compassion predicts persistence and growth after failure better than self-esteem does, because it stabilizes a constructive stance toward setbacks without requiring positive self-evaluation; this dissociation explains why self-compassion interventions improve outcomes that self-esteem interventions characteristically fail to budge.

**warning**: Self-Compassion is often conflated with self-indulgence or lowered standards, but the empirical literature is consistent in showing the opposite: high self-compassion is associated with stronger personal accountability, greater willingness to acknowledge mistakes, and higher sustained achievement striving, because it removes the threat that drives defensive avoidance.

## Dopaminergic Reward System

- domain: cognitive-science
- secondary_domains: [neuroscience-of-learning, motivational-neuroscience]
- aliases: [mesolimbic dopamine system, reward prediction error system]
- broader: [neuroscience-of-learning, motivational-psychology]
- related: [intrinsic-motivation, long-term-potentiation, neuroplasticity, dopamine-reward-prediction-error]
- prerequisites: [neuroplasticity]

**definition**: The Dopaminergic Reward System is the family of midbrain dopaminergic projections — principally from the ventral tegmental area to the nucleus accumbens, prefrontal cortex, and amygdala — whose phasic firing encodes a reward prediction error signal that drives reinforcement learning and shapes the assignment of motivational value to predictive cues, formalized in the Schultz model of dopamine as a teaching signal.

**key_claim**: The Dopaminergic Reward System encodes a quantitative reward prediction error — the difference between received and expected reward — rather than reward magnitude itself, and this prediction-error coding is the cellular implementation of temporal-difference reinforcement learning that links behavioral conditioning, addiction, and modern reward-based AI on a common computational substrate.

**warning**: The Dopaminergic Reward System should not be glossed as the brain's "pleasure center"; the Berridge dissociation between wanting (incentive salience, dopamine-mediated) and liking (hedonic impact, opioid-mediated) shows that dopamine signals motivational value rather than pleasure per se, and conflating the two has propagated significant misunderstandings into popular accounts.

## Stress and Learning

- domain: cognitive-science
- secondary_domains: [neuroscience-of-learning, emotion-and-memory]
- aliases: [stress-learning interaction, cortisol and memory]
- broader: [neuroscience-of-learning, memory-consolidation]
- related: [memory-consolidation, long-term-potentiation, dopaminergic-reward-system, achievement-emotions]
- prerequisites: [memory-consolidation, long-term-potentiation]

**definition**: Stress and Learning denotes the bidirectional empirical relationship between physiological stress responses — principally hypothalamic-pituitary-adrenal axis activation and the resulting glucocorticoid release — and learning processes such as encoding, consolidation, and retrieval, with the canonical finding that the relationship is shaped jointly by stressor timing, intensity, and the phase of memory under examination.

**key_claim**: Stress and Learning interact according to an inverted-U dose-response in which moderate stress around encoding enhances long-term consolidation through glucocorticoid-amygdala-hippocampal interactions, while severe or chronic stress impairs hippocampal function and biases the system toward inflexible procedural learning, producing predictable shifts in what is learned rather than uniform enhancement or impairment.

**warning**: Stress and Learning should not be summarized as "stress is bad for learning"; the empirical pattern is timing-and-phase-specific, with moderate post-encoding stress reliably enhancing consolidation while severe pre-retrieval stress impairs reinstatement of the same memory, and curricular implications differ sharply across these conditions.
