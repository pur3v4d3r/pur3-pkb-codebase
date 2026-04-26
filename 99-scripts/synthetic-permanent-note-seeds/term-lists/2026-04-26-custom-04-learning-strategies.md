---
batch_name: custom-04-learning-strategies
batch_date: 2026-04-26
default_domain: learning-science
default_confidence: high
notes: |
  Custom seeding batch 04: concrete study strategies. Pairs with the
  memory-science batch.
---

# Batch: Learning Strategies

## Active Recall

- domain: learning-science
- secondary_domains: [memory-science, study-strategy]
- aliases: [retrieval-based study, self-testing]
- broader: [retrieval-practice, testing-effect]
- related: [feynman-technique, leitner-system, spaced-retrieval, desirable-difficulties]
- prerequisites: [retrieval-practice, testing-effect]
- confidence: high

**definition**: Active Recall is the study practice of producing target information from memory in response to a cue — without consulting source material — as the principal mode of study, rather than relying on rereading or highlighting that allow the source to do the retrieval work.

**key_claim**: Active Recall consistently outperforms passive review on long-term retention because the act of retrieval itself reconsolidates the trace, even when retrieval initially feels harder and produces lower in-session confidence than rereading.

**warning**: Active Recall is often confused with re-exposure to questions; copying down the answer after looking it up is not Active Recall, and learners frequently overestimate how much retrieval their study actually involves because lookup feels like recall.

## Cornell Note Taking

- domain: learning-science
- secondary_domains: [study-strategy, pkm]
- aliases: [Cornell method, Cornell notes]
- broader: [note-taking-system]
- related: [active-note-making, sq3r-method, feynman-technique, active-recall]
- prerequisites: [note-taking]
- confidence: high

**definition**: Cornell Note Taking is a structured note-taking format that divides each page into a wide notes column, a narrow cue column on the left, and a summary band at the bottom, requiring the learner to extract cue questions and write a summary as a post-lecture review pass.

**key_claim**: Cornell Note Taking outperforms unstructured linear note-taking primarily because the cue and summary bands force a deliberate review-and-elaboration phase that converts the page into a self-quiz, embedding active recall into the artefact itself.

**warning**: Cornell Note Taking is often reduced to its visual layout, but adopting the three-column page without performing the cue-extraction and summary passes captures none of the benefit; the format is a scaffold for a process, not a study technique on its own.

## Feynman Technique

- domain: learning-science
- secondary_domains: [study-strategy, metacognition]
- aliases: [explain-it-to-a-child technique]
- broader: [self-explanation]
- related: [active-recall, self-explanation, elaborative-interrogation]
- prerequisites: [self-explanation]
- confidence: high

**definition**: The Feynman Technique is a four-step study procedure — pick a concept, explain it in simple language as if to a novice, identify gaps where the explanation breaks down, and study to repair those gaps before re-explaining — designed to surface unrecognized comprehension failures.

**key_claim**: The Feynman Technique works because it forces the learner to translate technical vocabulary into ordinary language, a translation that fails wherever the learner has only memorized terminology rather than mastered the underlying conceptual structure.

**warning**: The Feynman Technique can degrade into vague paraphrase if the "simple language" rule is interpreted as removing precision rather than removing jargon; the technique requires that the simplified explanation still preserve the inferential commitments of the original, not merely sound accessible.

## Leitner System

- domain: learning-science
- secondary_domains: [memory-science, spaced-repetition, study-strategy]
- aliases: [Leitner box system, paper SRS]
- broader: [spaced-repetition]
- related: [active-recall, spaced-retrieval, pomodoro-technique, anki]
- prerequisites: [spaced-repetition]
- confidence: high

**definition**: The Leitner System is a paper-based spaced-repetition scheme in which flashcards are sorted into a series of physical boxes; cards answered correctly graduate to a less-frequently-reviewed box, while cards missed are demoted to the most-frequently-reviewed box.

**key_claim**: The Leitner System is the historical prototype of all modern algorithmic spaced-repetition schedulers and embodies the same core idea: review interval should be a function of the recent retrieval success of an item, not of the calendar.

**warning**: The Leitner System is often dismissed as obsolete now that software schedulers exist, but the physical version offers a tangible feedback signal — the size of each box — that algorithmic SRS hides, and many learners regulate their workload better with the visible boxes than with an opaque queue.

## Pomodoro Technique

- domain: learning-science
- secondary_domains: [study-strategy, productivity, attention]
- aliases: [pomodoro method, 25/5 technique]
- broader: [time-management-technique]
- related: [attention-restoration-theory, deep-work, leitner-system]
- prerequisites: [attention]
- confidence: high

**definition**: The Pomodoro Technique is a time-management method in which work is performed in fixed timed intervals — traditionally 25 minutes — separated by short breaks, with longer breaks after a set number of intervals, intended to bound the cost of focused effort and reduce procrastination.

**key_claim**: The Pomodoro Technique works less by optimizing attentional capacity than by lowering the activation threshold to begin work: committing to a single short interval is psychologically cheaper than committing to a vague stretch of "studying."

**warning**: The Pomodoro Technique can become a form of productivity theatre when the timer becomes the goal; checking off pomodoros without tracking task progress lets the technique substitute completed intervals for completed work, especially on tasks that demand longer continuous concentration.

## SQ3R Method

- domain: learning-science
- secondary_domains: [study-strategy, reading-comprehension]
- aliases: [SQ3R, survey-question-read-recite-review]
- broader: [reading-strategy]
- related: [cornell-note-taking, active-recall, reading-workflow]
- prerequisites: [reading-comprehension]
- confidence: high

**definition**: The SQ3R Method is a five-step reading strategy — Survey, Question, Read, Recite, Review — devised by Francis Robinson in 1946, in which the reader previews structure, generates questions, reads to answer them, recites answers without the text, and schedules a later review pass.

**key_claim**: The SQ3R Method outperforms unstructured reading because each of its five steps embeds a recognized memory principle — generation effects, retrieval practice, and spaced review — within the act of reading itself, rather than treating reading and review as separate stages.

**warning**: The SQ3R Method's effect size collapses when learners perform the Survey and Question steps perfunctorily; the technique relies on the reader generating their own questions, and substituting publisher-supplied chapter-end questions removes the generation effect that does most of the work.
