---
batch_name: 2026-04-25-gap-batch-c-reasoning
batch_date: 2026-04-25
default_domain: critical-thinking
default_confidence: high
notes: |
  Gap-analysis batch C — formal logic, reasoning, and critical-thinking
  concepts referenced by existing notes but missing files.
---

# Batch: Reasoning & Critical Thinking Gaps

## Formal Logic

- domain: critical-thinking
- secondary_domains: [philosophy, mathematics]
- aliases: [symbolic logic, deductive logic systems]
- broader: [logic]
- related: [non-classical-logic, deductive-reasoning, propositional-logic, predicate-logic, truth-tables]
- prerequisites: [deductive-reasoning, deductive-logic]
- confidence: high

**definition**: Formal Logic is the systematic study of inference patterns whose validity depends solely on the syntactic structure of the propositions involved rather than on the empirical content, and it provides the canonical tools — propositional calculus, predicate calculus, truth tables, natural deduction — used to evaluate deductive arguments.

**key_claim**: Formal Logic separates the question of validity (does the conclusion follow from the premises?) from the question of soundness (are the premises true?), which is why a Formal Logic analysis can declare an argument valid even when it is empirically absurd, and unsound even when its conclusion happens to be true.

**warning**: Formal Logic is necessary but not sufficient for everyday critical thinking; many real arguments are inductive, abductive, or rely on background warrants that Formal Logic does not represent, so treating Formal Logic as the universal tool for argument evaluation produces a narrow and unhelpful understanding of reasoning.

## Non Classical Logic

- domain: critical-thinking
- secondary_domains: [philosophy, mathematics]
- aliases: [alternative logics, non-classical systems]
- broader: [logic]
- related: [formal-logic, modal-logic, fuzzy-logic, intuitionistic-logic, paraconsistent-logic, temporal-logic]
- prerequisites: [formal-logic]
- confidence: high

**definition**: Non Classical Logic is the family of formal systems that depart from classical bivalent two-valued logic in at least one of its core assumptions — bivalence, the law of excluded middle, ex contradictione quodlibet, or material implication — and it includes modal, intuitionistic, fuzzy, paraconsistent, relevance, and many-valued logics.

**key_claim**: Non Classical Logic is not a rejection of classical logic but a controlled relaxation of its assumptions to model phenomena classical logic cannot represent gracefully, such as necessity and possibility (modal), constructive proof (intuitionistic), graded truth (fuzzy), or contradictions without explosion (paraconsistent).

**warning**: Non Classical Logic is sometimes invoked as if it licensed loose reasoning ("logic is just one option"), but each Non Classical Logic system is at least as rigorous as classical logic; treating Non Classical Logic as permission for ambiguity reverses the actual relationship between formal systems and informal reasoning.

## Logical Reasoning

- domain: critical-thinking
- secondary_domains: [psychology, philosophy]
- aliases: [logical inference, structured reasoning]
- broader: [reasoning]
- related: [deductive-reasoning, inductive-reasoning, abductive-reasoning, formal-logic, critical-thinking]
- prerequisites: [reasoning, critical-thinking]
- confidence: high

**definition**: Logical Reasoning is the cognitive activity of drawing conclusions from premises in accordance with the canonical inference patterns — deductive, inductive, abductive — studied by logic, and it is one of the central competencies that critical thinking aims to develop.

**key_claim**: Logical Reasoning performance in laboratory tasks is highly content-sensitive: the same abstract inference pattern is solved at very different rates depending on the familiarity of the materials, which is why theories of Logical Reasoning have moved from purely formal accounts toward dual-process and pragmatic-reasoning-schema accounts.

**warning**: Logical Reasoning is often equated with formal logic, but most everyday Logical Reasoning is defeasible and probabilistic; teaching Logical Reasoning by drilling truth tables and syllogisms produces transfer failures because real reasoning environments rarely supply the closed premise sets formal logic requires.

## Elements of Thought

- domain: critical-thinking
- secondary_domains: [education, philosophy]
- aliases: [Paul-Elder elements, eight elements of reasoning]
- broader: [critical-thinking]
- related: [intellectual-standards, intellectual-traits, paul-elder-framework, argument-analysis]
- prerequisites: [critical-thinking]
- confidence: high

**definition**: The Elements of Thought are the eight structural components of any act of reasoning identified in the Paul-Elder critical-thinking framework — purpose, question, information, interpretation, concept, assumption, implication, and point of view — and they provide the analytic vocabulary used to dissect arguments in that tradition.

**key_claim**: The Elements of Thought are not a checklist but an interlocking system: changing the purpose changes the relevant question, which constrains the information needed, which shapes interpretation, which depends on concepts and assumptions, all of which combine to produce implications from a particular point of view, so Elements of Thought analysis is structural rather than additive.

**warning**: The Elements of Thought are widely taught in introductory courses as a routine grid to fill in, but a mechanical application produces shallow analyses; the framework only delivers value when paired with the intellectual standards (clarity, accuracy, depth, etc.) that the same framework specifies, and the Elements of Thought without those standards becomes formulaic.

## Case Based Reasoning

- domain: cognitive-science
- secondary_domains: [artificial-intelligence, education]
- aliases: [CBR, case-based problem solving]
- broader: [reasoning]
- related: [analogical-reasoning, structure-mapping-theory, expert-cognition, schema-theory, case-based-learning]
- prerequisites: [analogical-reasoning, schema-theory]
- confidence: high

**definition**: Case Based Reasoning is a problem-solving strategy in which a new problem is solved by retrieving a similar prior case from memory, adapting the prior solution to fit the new situation, evaluating the adapted solution, and storing the resulting case for future reuse, and it is a foundational paradigm in both cognitive science and AI.

**key_claim**: Case Based Reasoning models the way experts in domains such as medicine, law, and engineering actually solve problems — by retrieval and adaptation of prior episodes — far better than rule-based or first-principles models, which is why Case Based Reasoning is the dominant cognitive account of expertise in ill-structured domains.

**warning**: Case Based Reasoning is bounded by the quality and coverage of the case library; novices attempting Case Based Reasoning before they have a useful case library make systematic surface-similarity errors, so Case Based Reasoning is not a substitute for the slow accumulation of cases that produces expert intuition.

## Structure Mapping Theory

- domain: cognitive-science
- secondary_domains: [analogical-reasoning, artificial-intelligence]
- aliases: [Gentner structure mapping, SMT]
- broader: [analogical-reasoning]
- related: [analogical-reasoning, structure-mapping-engine, case-based-reasoning, relational-thinking, schema-construction]
- prerequisites: [analogical-reasoning]
- confidence: high

**definition**: Structure Mapping Theory is Dedre Gentner's account of analogical reasoning in which analogy is defined as the alignment of relational structure between a base domain and a target domain, with object attributes secondary, and the systematicity principle giving preference to mappings that preserve higher-order relations.

**key_claim**: Structure Mapping Theory predicts that good analogies are recognised and remembered for their relational rather than surface similarity, which is why expert analogical transfer is reliably superior to novice transfer and why Structure Mapping Theory has displaced earlier feature-overlap accounts of similarity.

**warning**: Structure Mapping Theory describes the alignment process well but is silent about retrieval; real analogical reasoning failures usually involve failure to retrieve a structurally relevant base, not failure to align it once retrieved, so Structure Mapping Theory must be paired with retrieval models to explain everyday analogical performance.

## Truth Tables

- domain: critical-thinking
- secondary_domains: [mathematics, formal-logic]
- aliases: [truth-table method, semantic tables]
- broader: [propositional-logic]
- related: [formal-logic, propositional-logic, validity, tautology, semantic-validity]
- prerequisites: [propositional-logic]
- confidence: high

**definition**: Truth Tables are the canonical semantic technique in propositional logic for determining the truth value of compound propositions under every possible assignment of truth values to their atomic components, and they provide a mechanical decision procedure for validity in propositional calculus.

**key_claim**: Truth Tables establish the validity of an argument by exhaustive search rather than by proof construction, and the exhaustive nature of Truth Tables guarantees a decision in finite time for propositional logic — a guarantee that does not extend to predicate logic, which is why Truth Tables play a more central role in propositional than in first-order systems.

**warning**: Truth Tables grow exponentially with the number of atomic propositions, so Truth Tables become unmanageable for arguments with more than five or six atoms; treating Truth Tables as the practical method of choice for serious logical analysis ignores the existence of more efficient proof systems such as natural deduction and tableau methods.

## Behaviorism

- domain: psychology
- secondary_domains: [learning-science, philosophy-of-psychology]
- aliases: [behaviourism, behaviorist psychology]
- broader: [learning-theory]
- related: [classical-conditioning, operant-conditioning, reinforcement, cognitive-revolution, learning-theories]
- prerequisites: [learning-theory]
- confidence: high

**definition**: Behaviorism is the school of psychology, dominant in the early twentieth century, that restricts the legitimate objects of psychological science to publicly observable behaviour and the environmental contingencies — stimuli, responses, reinforcements — that shape it, methodologically excluding mental states from explanation.

**key_claim**: Behaviorism produced a durable empirical legacy — schedules of reinforcement, behavioural assessment, applied behaviour analysis — even after the cognitive revolution rejected its strict ontological claims, which is why a contemporary understanding of Behaviorism distinguishes its methodological contributions from its philosophical commitments.

**warning**: Behaviorism is frequently caricatured as denying the existence of mental states; the more accurate reading is that methodological Behaviorism brackets mental states for scientific tractability, while radical Behaviorism (Skinner) reframes them as covert behaviours, so dismissing Behaviorism as "ignoring the mind" misses the actual theoretical position.

## Epistemology

- domain: philosophy
- secondary_domains: [critical-thinking, philosophy-of-science]
- aliases: [theory of knowledge]
- broader: [philosophy]
- related: [virtue-epistemology, justified-true-belief, foundationalism, coherentism, gettier-problem, intellectual-humility]
- confidence: high

**definition**: Epistemology is the branch of philosophy that investigates the nature, sources, scope, and justification of knowledge, taking as its central questions what knowledge is, how it is acquired, and how knowledge claims are evaluated against alternatives such as belief, opinion, and ignorance.

**key_claim**: Contemporary Epistemology has moved well beyond the classical justified-true-belief analysis of knowledge — destabilised by Gettier cases — into virtue, reliabilist, contextualist, and social Epistemology, and ignoring this internal pluralism produces oversimplified accounts of what "really knowing" something means.

**warning**: Epistemology is often invoked rhetorically in non-philosophical writing as a synonym for "perspective" or "way of knowing"; this usage drains the term of its analytic content and conflates Epistemology proper with cultural studies of knowledge, which obscures the genuinely philosophical questions Epistemology asks.

## Cognitive Science

- domain: cognitive-science
- secondary_domains: [interdisciplinary, psychology, philosophy]
- aliases: [cognitive sciences, the cognitive sciences]
- broader: [interdisciplinary-research]
- related: [cognitive-psychology, neuroscience, artificial-intelligence, philosophy-of-mind, linguistics, anthropology]
- confidence: high

**definition**: Cognitive Science is the interdisciplinary study of mind and intelligence that integrates psychology, computer science and artificial intelligence, neuroscience, philosophy, linguistics, and anthropology around the unifying assumption that cognition is a form of information processing realisable in multiple substrates.

**key_claim**: Cognitive Science is defined less by its subject matter than by its commitment to multi-level explanation — Marr's computational, algorithmic, and implementational levels are the canonical articulation — which is why Cognitive Science treats explanation as triangulation across disciplines rather than reduction to any single one.

**warning**: Cognitive Science is sometimes equated with cognitive psychology or with computational modelling; both equations are too narrow, and they obscure the genuinely interdisciplinary integration that distinguishes Cognitive Science from each of its constituent disciplines taken alone.

## Cognitive Behavioral Therapy

- domain: clinical-psychology
- secondary_domains: [psychotherapy, motivational-psychology]
- aliases: [CBT]
- broader: [psychotherapy]
- related: [cognitive-restructuring, behavioral-activation, attribution-retraining, learned-helplessness, explanatory-style]
- prerequisites: [cognitive-restructuring, attribution-theory]
- confidence: high

**definition**: Cognitive Behavioral Therapy is a structured, time-limited psychotherapy in which the therapist and client identify the interlocking thoughts, behaviours, and emotional responses that maintain the presenting problem and intervene on each in turn through cognitive restructuring, behavioural experiments, and homework.

**key_claim**: Cognitive Behavioral Therapy is the most empirically supported psychotherapy across a wide range of disorders — depression, anxiety, OCD, PTSD, eating disorders — and the active mechanism appears to be the modification of the thought-behaviour-emotion loops rather than insight or therapeutic alliance alone.

**warning**: Cognitive Behavioral Therapy is widely diluted in self-help and workplace-wellness contexts into "think positive" advice; this diluted Cognitive Behavioral Therapy lacks the structured protocols, behavioural experiments, and clinical supervision that produce the effect sizes the research literature reports.
