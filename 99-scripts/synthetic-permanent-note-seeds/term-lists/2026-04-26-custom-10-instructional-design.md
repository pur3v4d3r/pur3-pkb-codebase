---
batch_name: custom-10-instructional-design
batch_date: 2026-04-26
default_domain: instructional-design
default_confidence: high
notes: |
  Custom seeding batch 10: instructional-design constructs.
---

# Batch: Instructional Design

## ARCS Motivation Model

- domain: instructional-design
- secondary_domains: [motivation, learning-theory]
- aliases: [Keller ARCS model, ARCS-V]
- broader: [motivational-design]
- related: [self-determination-theory, expectancy-value-theory, gamification, intrinsic-motivation]
- prerequisites: [motivation-theory]
- confidence: medium

**definition**: The ARCS Motivation Model, developed by John Keller, is a framework for designing instruction that systematically addresses four motivational categories — Attention, Relevance, Confidence, and Satisfaction — each with specific strategies and diagnostic questions for instructional designers.

**key_claim**: The ARCS Motivation Model's distinctive contribution is treating motivation as a designable property of instruction rather than as a learner trait; by decomposing motivation into four conditions that instruction can manipulate, ARCS makes motivational design auditable and provides a vocabulary for diagnosing why a course "feels boring" or "feels overwhelming" beyond impressionistic critique.

**warning**: The ARCS Motivation Model is a heuristic framework rather than a tested causal theory; its categories were derived from synthesis of motivation research rather than from independent empirical validation, and few rigorous studies have isolated the contribution of ARCS-prescribed strategies from confounded design improvements, so the model is best treated as a useful design checklist rather than as evidence-based prescription.

## Competency Based Education

- domain: instructional-design
- secondary_domains: [assessment, higher-education]
- aliases: [CBE, mastery-based education]
- broader: [outcomes-based-education]
- related: [mastery-learning, summative-assessment, criterion-referenced-assessment, micro-credentialing]
- prerequisites: [assessment-theory]
- confidence: medium

**definition**: Competency Based Education is an instructional model in which progression is determined by demonstrated mastery of clearly specified competencies rather than by time spent in instruction, decoupling credentialing from seat-time and shifting accountability onto criterion-referenced assessment of observable performance.

**key_claim**: Competency Based Education's central theoretical commitment is that holding learning constant while letting time vary produces more equitable outcomes than the inverse, the inherited industrial model of holding time constant while letting learning vary; this reframing is what allows CBE to defend asynchronous progression and credit-by-assessment while preserving outcome guarantees.

**warning**: Competency Based Education depends critically on the validity and decomposability of its competency specifications; when competencies are too granular, instruction fragments into checkbox tasks that fail to integrate into deep expertise, and when they are too holistic, assessment becomes subjective and CBE loses its accountability advantage. Programs that adopt the CBE label without solving this granularity problem reproduce traditional pathologies under new branding.

## Elaborative Feedback

- domain: instructional-design
- secondary_domains: [learning-theory, assessment]
- aliases: [elaborative formative feedback, explanatory feedback]
- broader: [formative-feedback]
- related: [retrieval-practice, deliberate-practice, formative-assessment, knowledge-of-results]
- prerequisites: [formative-assessment]
- confidence: high

**definition**: Elaborative Feedback is feedback that, in addition to indicating whether a response is correct or incorrect, explains the underlying principle, identifies the source of the error, or models the correct reasoning process — going beyond simple knowledge-of-results to support conceptual change.

**key_claim**: Elaborative Feedback typically outperforms verification-only ("right/wrong") feedback for transfer and conceptual learning, but the meta-analytic record is more nuanced for retention of well-defined facts, where elaborative content can sometimes interfere with consolidation; the practical implication is that Elaborative Feedback should be calibrated to the nature of the learning objective rather than applied uniformly.

**warning**: Elaborative Feedback can become counterproductive when delivered in volumes that exceed working-memory capacity, when delivered immediately for procedural skills (where delayed feedback often promotes better transfer), or when it provides the answer in a way that bypasses the desirable difficulty of generation; "more elaboration is better" is not a defensible reading of the Elaborative Feedback evidence.

## Flipped Classroom

- domain: instructional-design
- secondary_domains: [pedagogy, blended-learning]
- aliases: [inverted classroom, flipped learning]
- broader: [blended-learning]
- related: [active-learning, peer-instruction, asynchronous-instruction, cognitive-load-theory]
- prerequisites: [pedagogy]
- confidence: medium

**definition**: The Flipped Classroom is an instructional model in which direct-instruction content (typically delivered as recorded video) is moved out of class time and assigned as preparation, freeing in-class time for higher-order activities such as problem solving, discussion, and individualized support.

**key_claim**: The Flipped Classroom's defensible theoretical claim is not "video lectures are better than live ones" but rather that synchronous instructor presence is a scarce resource that should be allocated to the cognitive activities that most benefit from real-time scaffolding — questioning, troubleshooting, and feedback — rather than to one-way information transmission.

**warning**: Flipped Classroom outcomes depend almost entirely on whether students complete the pre-class preparation and on whether in-class time is genuinely restructured around active learning; flipping that combines uncompleted video assignments with a class hour that reverts to lecture produces strictly worse outcomes than either pure mode, so the Flipped Classroom is not robust to partial implementation.

## Game Based Learning

- domain: instructional-design
- secondary_domains: [educational-technology, motivation]
- aliases: [GBL, serious games]
- broader: [educational-technology]
- related: [gamification, simulation-based-learning, intrinsic-motivation, experiential-learning]
- prerequisites: [learning-theory]
- confidence: medium

**definition**: Game Based Learning is an instructional approach that uses games — designed artifacts with goals, rules, feedback systems, and voluntary participation — as the primary medium for learning, distinguished from gamification by integrating instructional content into gameplay rather than overlaying game elements onto non-game tasks.

**key_claim**: Game Based Learning's strongest empirical case is for procedural and decision-making skills in well-defined domains where the game mechanics directly model the target skill (flight simulation, surgical training, strategic reasoning), because the game's feedback loop functions as deliberate practice with embedded scaffolding rather than as decoration.

**warning**: Meta-analyses of Game Based Learning report modest average effects with high heterogeneity, and many positive findings come from comparisons against weak control conditions rather than against well-designed conventional instruction; treating Game Based Learning as inherently superior to non-game instruction misreads the evidence, which more accurately supports "well-designed games" outperforming "poorly designed alternatives" — a much weaker claim.

## Gamification

- domain: instructional-design
- secondary_domains: [motivation, behavioral-design]
- aliases: [educational gamification, points-and-badges]
- broader: [motivational-design]
- related: [game-based-learning, self-determination-theory, intrinsic-motivation, extrinsic-rewards]
- prerequisites: [motivation-theory]
- confidence: medium

**definition**: Gamification is the application of game design elements — points, badges, leaderboards, levels, narrative framing — to non-game contexts including instruction, in order to increase engagement, motivation, and persistence with the underlying activity.

**key_claim**: Gamification's effects on intrinsic motivation are predicted by self-determination theory to depend on whether the game elements support competence and autonomy or function as controlling extrinsic rewards; when leaderboards and badges are perceived as controlling, Gamification can reduce intrinsic motivation through the overjustification effect, exactly opposite to its design intent.

**warning**: Gamification is often deployed as a generic engagement intervention without analysis of the underlying activity; when the underlying instruction is intrinsically dull or pedagogically unsound, Gamification adds a thin extrinsic reward layer that produces short-term compliance and long-term disengagement once the rewards are withdrawn, a failure mode well documented across educational and workplace deployments.

## Peer Instruction

- domain: instructional-design
- secondary_domains: [active-learning, higher-education]
- aliases: [Mazur peer instruction, ConcepTests]
- broader: [active-learning]
- related: [flipped-classroom, formative-assessment, elaborative-feedback, social-constructivism]
- prerequisites: [active-learning]
- confidence: high

**definition**: Peer Instruction is an active-learning method developed by Eric Mazur in which students respond to a conceptual question (a ConcepTest) individually, then discuss their reasoning with peers, then re-respond — converting lecture into a structured cycle of commitment, dialogue, and revision.

**key_claim**: Peer Instruction's empirical robustness, particularly in introductory physics, is grounded in two mechanisms: the initial individual commitment forces retrieval and exposes misconceptions, and peer dialogue is more effective than instructor exposition because near-peers can articulate the cognitive bridge from the misconception to the correct conception in a way an expert often cannot.

**warning**: Peer Instruction depends on a non-trivial supply of well-designed ConcepTests that target known misconceptions and on initial response distributions in the productive 30-70% correct range; using questions with near-uniform initial correctness produces uninformative discussion and converts Peer Instruction into a procedural ritual without the conceptual change it was designed to produce.

## Summative Assessment

- domain: instructional-design
- secondary_domains: [assessment, educational-measurement]
- aliases: [final assessment, assessment of learning]
- broader: [assessment]
- related: [formative-assessment, criterion-referenced-assessment, validity, reliability]
- prerequisites: [assessment]
- confidence: high

**definition**: Summative Assessment is evaluation conducted at the conclusion of an instructional unit, course, or program for the purpose of certifying or judging learning against established standards, contrasted with formative assessment whose purpose is to inform ongoing instruction.

**key_claim**: Summative Assessment's defining feature is its function rather than its instrument; the same test item can serve summative purposes in one administration and formative purposes in another, so reform efforts that try to "replace summative with formative assessment" misframe the issue — the policy question is which decisions require certification-grade Summative Assessment and how to design instruments fit for that decision-making purpose.

**warning**: Summative Assessment systems exert powerful washback on instruction: when high-stakes Summative Assessment narrowly samples a domain, instruction reliably narrows to match, often degrading the very competencies the assessment was meant to certify. Treating Summative Assessment as a neutral measurement instrument while ignoring its incentive effects misunderstands how it actually shapes the educational system in which it is embedded.
