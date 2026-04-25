---
batch_name: 2026-04-25-batch-05-metacognition
batch_date: 2026-04-25
default_domain: cognitive-science
default_confidence: high
notes: |
  Metacognition cluster. Seeds the monitoring-judgment family
  (hypercorrection, retrospective confidence, illusion of knowing,
  tip-of-the-tongue, calibration accuracy) that complements the
  metacognitive-monitoring / metacognitive-control core in vault.
---

# Batch: Metacognition

## Hypercorrection Effect

- secondary_domains: [memory, metacognition]
- aliases: [hypercorrection]
- broader: [metacognitive-monitoring]
- related: [retrieval-practice, retrospective-confidence-judgment, error-correction, productive-failure]
- prerequisites: [metacognitive-monitoring]

**definition**: The Hypercorrection Effect is the empirical finding that errors made with high confidence are more likely to be corrected — and to stay corrected — after feedback than errors made with low confidence, contrary to the intuitive prediction that strongly-held wrong beliefs would be the hardest to dislodge.

**key_claim**: The Hypercorrection Effect implies that surprise produced by the gap between expected accuracy and actual accuracy is itself a learning signal, which is why high-confidence errors — where the surprise is largest — produce the deepest re-encoding of the correct answer.

**warning**: The Hypercorrection Effect is sometimes invoked as a license to elicit confident wrong answers in instruction; the effect requires immediate, clear corrective feedback, and the high-confidence-error pattern produces durable misconceptions when the feedback step is omitted or delayed.

## Retrospective Confidence Judgment

- secondary_domains: [metacognition, decision-making]
- aliases: [RCJ, post-decisional confidence]
- broader: [metacognitive-judgments]
- related: [judgment-of-learning, calibration, hypercorrection-effect, overconfidence-bias]
- prerequisites: [metacognitive-judgments]

**definition**: A Retrospective Confidence Judgment is a metacognitive rating made after producing an answer or completing a task, indexing how certain the actor is that the answer is correct, and is the workhorse measure for studies of calibration accuracy and overconfidence in decision-making and memory research.

**key_claim**: The Retrospective Confidence Judgment is dissociable from accuracy: people can be highly accurate while poorly calibrated, or moderately inaccurate while well calibrated, which is why confidence and accuracy must be measured separately rather than treated as proxies for each other.

**warning**: Retrospective Confidence Judgment data are routinely misread as direct windows into the underlying memory or decision strength; the judgments are themselves inferential constructions that depend on the cues available at the moment of judging, which is why changing post-hoc cues can shift confidence without changing the underlying response.

## Illusion of Knowing

- secondary_domains: [metacognition, reading-comprehension]
- aliases: [illusion of comprehension]
- broader: [metacognitive-monitoring]
- related: [fluency-illusion, judgment-of-learning, comprehension-monitoring, illusion-of-explanatory-depth]
- prerequisites: [metacognitive-monitoring]

**definition**: The Illusion of Knowing is the phenomenon in which a learner judges that material has been understood or memorized when an objective test would reveal that understanding or recall is markedly weaker than the felt confidence implies — most reliably produced by ease-of-processing cues that are diagnostic of fluency rather than of comprehension.

**key_claim**: The Illusion of Knowing exposes the central failure of fluency-based monitoring: the cues the mind defaults to (re-reading ease, familiarity, processing speed) are correlated with prior exposure rather than with current retrieval accessibility, which is why retrieval-based monitoring beats reading-based monitoring on calibration.

**warning**: The Illusion of Knowing is not eliminated by warning learners about it; explicit knowledge of the illusion does not change the monitoring cues the system spontaneously uses, so corrective interventions must replace the cue (e.g., by inserting retrieval attempts) rather than merely flagging the bias.

## Tip-of-the-Tongue Phenomenon

- secondary_domains: [psycholinguistics, memory]
- aliases: [TOT, tip-of-the-tongue state]
- broader: [metacognitive-experience]
- related: [feeling-of-knowing, semantic-memory, cue-encoding-bottleneck, metacognitive-feelings]
- prerequisites: [metacognitive-experience]

**definition**: The Tip-of-the-Tongue Phenomenon is the strong subjective experience of being on the verge of recalling a known word — typically accompanied by partial information such as initial letters, syllable count, or semantically related candidates — without successful retrieval of the word itself.

**key_claim**: The Tip-of-the-Tongue Phenomenon provides one of the clearest dissociations of access from storage in cognitive psychology: the partial-information accompaniments demonstrate that the target representation is present and partially accessible, ruling out trace-loss explanations and isolating retrieval failure as the locus of the impasse.

**warning**: The Tip-of-the-Tongue Phenomenon is often interpreted as evidence that the answer "is in there"; the inference is approximately right for high-frequency lexical items but generalizes poorly to conceptual or skill knowledge, where the felt-imminence cue is much less diagnostic of actual presence.

## Metacognitive Accuracy

- secondary_domains: [metacognition, decision-making]
- aliases: [metacognitive calibration accuracy, monitoring accuracy]
- broader: [metacognitive-calibration]
- related: [calibration, judgment-of-learning, retrospective-confidence-judgment, illusion-of-knowing]
- prerequisites: [metacognitive-monitoring]

**definition**: Metacognitive Accuracy is the degree of correspondence between a person's metacognitive judgment about their cognition (e.g., a confidence rating, a judgment of learning) and the actual state being judged (e.g., the probability of correct retrieval), and is operationalized through measures such as calibration curves, Goodman-Kruskal gamma, and meta-d'.

**key_claim**: Metacognitive Accuracy is a partially dissociable cognitive capacity from first-order ability: two people with the same task accuracy can differ substantially in how well their confidence tracks their accuracy, which means calibration is a trainable target rather than a byproduct of competence.

**warning**: Metacognitive Accuracy aggregated to a single number conceals the more diagnostic distinction between resolution (the discriminative power of confidence) and bias (systematic over- or under-confidence); a single calibration metric can hide the fact that a learner is well-resolved but biased, or unbiased but unresolved.
