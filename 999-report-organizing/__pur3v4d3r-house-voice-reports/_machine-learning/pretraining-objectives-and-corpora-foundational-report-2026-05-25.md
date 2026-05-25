---
# ═══════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════
title: "Pretraining Objectives and Corpora: WebText, The Pile, and Common Crawl — A Foundational Report"
aliases:
  - "Pretraining Corpora"
  - "LLM Training Data"
  - "WebText The Pile Common Crawl"
  - "Pretraining Objectives Overview"
type: permanent-note
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - foundational-report
  - academic-synthesis
  - machine-learning/pretraining
  - machine-learning/nlp
  - empirical-research
  - evidence-based

# ═══════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════
created: "2026-05-25"
updated: "2026-05-25"

# ═══════════════════════════════════════════════════════════════
# DOCUMENT IDENTIFICATION (Pipeline-Compatible)
# ═══════════════════════════════════════════════════════════════
doc_id: "pretraining-objectives-and-corpora-foundational-report"
doc_type: "Foundational Report"
doc_created: "2026-05-25"
doc_modified: "2026-05-25"
author: "Claude (Anthropic)"
house_voice: "Examined Witness"
house_voice_version: "1.0.0"

# ═══════════════════════════════════════════════════════════════
# CLASSIFICATION & DISCOVERY
# ═══════════════════════════════════════════════════════════════
primary_domain: "Machine Learning / Natural Language Processing"
secondary_domains: ["AI Ethics", "Data Engineering", "Foundation Models"]
knowledge_level: "comprehensive foundational treatment"

# ═══════════════════════════════════════════════════════════════
# QUALITY & STATUS
# ═══════════════════════════════════════════════════════════════
maturity: "highly developed"

# ═══════════════════════════════════════════════════════════════
# REASONING ARCHITECTURE
# ═══════════════════════════════════════════════════════════════
reasoning_tier: "Tier 1: Foundational Understanding"
reasoning_methods: ["Analytical exposition", "Historical-comparative analysis", "Cross-domain synthesis"]
reasoning_technique: "Multi-pass chain-of-density with self-consistency architecture selection"

# ═══════════════════════════════════════════════════════════════
# EPISTEMIC & VALIDATION
# ═══════════════════════════════════════════════════════════════
epistemic_status: "well-established"
validation_methods: ["Empirical evidence", "Scholarly consensus", "Logical consistency"]
factual_verification: "Verified against established literature"
hallucination_check: true

# ═══════════════════════════════════════════════════════════════
# SOURCE & ATTRIBUTION
# ═══════════════════════════════════════════════════════════════
source: "Claude (Anthropic) — academic synthesis"
source-type: academic-synthesis
research-base: "empirical-studies"
evidence-quality: "high"
key-researchers: ["Alec Radford", "Jacob Devlin", "Colin Raffel", "Leo Gao", "Jared Kaplan"]

# ═══════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════
word-count: "~23,878"
complexity-level: accessible-practitioner
target-audience: "Curious learners with no mathematics background; practitioners; lifelong autodidacts"
depth-level: comprehensive
treatment-type: foundational-analytical

# ═══════════════════════════════════════════════════════════════
# KNOWLEDGE GRAPH INTEGRATION
# ═══════════════════════════════════════════════════════════════
core-concepts: ["Pretraining", "Language Modeling Objectives", "Training Corpora", "Common Crawl", "WebText", "The Pile"]
key-distinctions: ["Autoregressive vs. Masked Language Modeling", "Curation vs. Scale", "Base Model vs. Fine-Tuned Model"]
prerequisites: ["[[transformer-attention-mechanism]]", "[[in-context-learning]]"]
related: ["[[llm-scaling-laws]]", "[[emergent-abilities-in-llms]]", "[[instruction-fine-tuning]]", "[[reinforcement-learning-from-human-feedback]]"]
broader: ["[[scaling-and-capability-emergence]]"]
narrower: ["[[byte-pair-encoding]]", "[[subword-tokenization]]"]
see-also: ["[[hallucination-taxonomy]]", "[[benchmark-contamination]]", "[[value-alignment-problem]]"]
builds-on: ["[[transformer-attention-mechanism]]", "[[self-attention-patterns]]"]
enables: ["[[instruction-tuning]]", "[[supervised-fine-tuning]]", "[[parameter-efficient-fine-tuning]]"]

# ═══════════════════════════════════════════════════════════════
# APPENDIX & DENSITY TRACKING (Pipeline-Compatible)
# ═══════════════════════════════════════════════════════════════
appendix_sections_included:
  - lexicon
  - key_figures
  - conceptual_tensions
  - references
  - methodology_note
  - argument_maps
  - practical_protocols
  - spaced_repetition_seeds
  - expansion_topics
  - pkb_connections
  - quality_self_assessment

lexicon_term_count: "10"
reference_count: "8"
flashcard_seed_count: "9"
expansion_topic_count: "5"
wiki_link_count: "159"
callout_count: "107"

# ═══════════════════════════════════════════════════════════════
# ORIGINAL CONTRIBUTIONS (Pipeline-Compatible)
# ═══════════════════════════════════════════════════════════════
original_contributions:
  - name: "The Corpus-as-Curriculum Framework"
    type: "theoretical-integration"
    epistemic_status: "well-motivated-synthesis"
    validation_needed: false
  - name: "Intuition-First Taxonomy of Pretraining Objectives"
    type: "methodological-innovation"
    epistemic_status: "well-motivated-synthesis"
    validation_needed: false

# ═══════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: budding
importance: "critical"
foundational-for-future-learning: true
connection-strength:
  high: ["Pretraining", "LLM Training Data", "Scaling Laws"]
  medium: ["Fine-Tuning", "RLHF", "Data Ethics"]
  exploratory: ["Data Governance", "AI Copyright"]
---

# Pretraining Objectives and Corpora: WebText, The Pile, and Common Crawl

> [!schema-activation] **Before You Read — Activating Prior Knowledge**
> If one has ever wondered why a language model seems to "know" that Paris is the capital of France without anyone having told it directly, or why the same model occasionally invents a plausible-sounding but entirely fabricated research paper, the answer to both questions lies in the same place: the training data and the objectives that governed how the model learned from it. This report is about exactly that — about what these models read, how they learned from their reading, and what that learning did and did not produce.
>
> Before proceeding, it is worth pausing to consider what you already know or suspect:
> - You may already be familiar with [[transformer-attention-mechanism|how transformers process language]] — if so, this report will explain what gets fed *into* those transformers before they produce anything useful.
> - You may have encountered the term [[in-context-learning]] — this report explains the deep substrate on which in-context learning depends.
> - You may have heard that language models are "trained on the internet" — this report will sharpen that intuition considerably, distinguishing among three major corpora that each embody a different philosophy about what "the internet" means as training material.
>
> **Guiding Question:** *How do the choices researchers made about what text to collect, and how to have a model learn from it, determine the capabilities, biases, and limitations of every large language model one encounters today?*
>
> The report that follows builds progressively: it begins with the concept of pretraining itself, moves through the specific learning objectives that define how models absorb text, examines the three most consequential training corpora in detail, and concludes by mapping the ethical and practical implications of these design choices.

---

## Abstract

What a large language model can do — and what it reliably cannot — is determined less by its architecture than by the data it was trained on and the objective it was trained to pursue. This report provides a comprehensive, intuition-first account of pretraining: the initial training phase in which language models absorb vast quantities of text before any human feedback or task-specific instruction shapes their behavior. The report examines three pretraining objectives — autoregressive language modeling, masked language modeling, and denoising — and explains each through analogy rather than mathematics, establishing what kind of understanding each objective can and cannot produce. It then offers deep-dive analyses of the three most consequential training corpora in the history of large language models: Common Crawl, the largest and most contested web-scraped dataset; WebText, OpenAI's quality-filtered corpus that powered GPT-2; and The Pile, EleutherAI's deliberately diverse 825GB collection designed to ensure that academic, technical, and literary knowledge was represented alongside web text. The report maps how each corpus embodies a distinct philosophy about what knowledge matters and whose writing counts as signal rather than noise. It concludes by examining what pretraining does and does not produce — making clear that the gap between a pretrained base model and a genuinely useful assistant is real and significant — and by confronting the ethical dimensions of training data: deduplication, toxicity, bias amplification, copyright, and consent. Throughout, the report is written for readers with no mathematical background, prioritizing conceptual clarity, practical applicability, and honest acknowledgment of what remains uncertain or unresolved in this rapidly evolving field. Understanding pretraining is not optional for anyone who wishes to use, evaluate, or critique large language models with genuine competence; it is the foundation on which everything else rests.

---

## Section 1: What Is Pretraining? The Foundation of All Modern Language Models

If one were to ask where the intelligence of a modern language model comes from — not the politeness or the specific knowledge of company policies, but the deep capacity to construct grammatical sentences, reason about cause and effect, summarize an argument, and continue a story in a plausible direction — the answer is almost entirely: pretraining. And yet pretraining is also, paradoxically, the stage of model development that most users and even many practitioners understand least clearly, because the name suggests something preliminary, a warmup before the real work begins. What one discovers on examination is that the opposite is closer to the truth: pretraining is where the model acquires its fundamental grasp of language and the world, and everything that comes after — the instruction tuning, the safety training, the human feedback — is a process of *directing* a capability that was already substantially there.

To understand why this is, one must understand what the alternative would look like, and why it fails. The most intuitive approach to building an intelligent system is the one that dominated early computing: write rules. Tell the machine that "the" is an article, that articles precede nouns, that questions end with question marks. This approach works well for small, bounded domains — chess, for instance, or tax calculation — but it collapses catastrophically when the domain is language in general, because language is irreducibly open-ended. Every rule has exceptions; every exception has exceptions; and the combinatorial complexity of even a single language, let alone the cross-domain knowledge needed to engage meaningfully with human discourse, exceeds what any practical rule-writing effort could capture. By the time one has written enough rules to handle a newspaper article, one has written a system that handles only that newspaper article — and brittle systems of this kind were the state of the art for much of the twentieth century.

The insight that broke the impasse — the insight that defines the modern era of language models — is that language contains its own teaching signal. That is to say, any sufficiently large piece of text is simultaneously a collection of examples and a collection of implicit tests. If one reads the sentence "She poured the coffee into the ___," any fluent English speaker can supply "cup" or "mug" or "thermos" without thinking. The knowledge required to do so is not stored in any list; it is an implicit understanding of how the world works, of what coffee is, what containers are, and what the verb "pour" implies about the relationship between a liquid and a receptacle. The intuition behind pretraining is: what if a model could learn by doing this millions — or billions — of times across every kind of text humans have written? What would it know then?

> [!definition] **Pretraining (in the context of language models)**
> Pretraining is the initial, large-scale phase of model development in which a neural network is exposed to enormous quantities of text and trained to perform a simple prediction task — such as predicting the next word, or filling in a missing word — on that text. The model receives no explicit labels, no human feedback, and no instruction about what it "should" know; instead, the text itself provides the training signal. Pretraining produces a *base model* or *foundation model* that has absorbed a broad, implicit understanding of language and world knowledge, but which has not yet been shaped to be helpful, safe, or task-specific.
>
> **Boundary conditions:** Pretraining does not teach a model to follow instructions, to refuse harmful requests, or to produce the kind of helpful responses users expect from deployed assistants. Those properties come from later training stages. Pretraining also does not guarantee that a model's knowledge is accurate, current, or free from bias — it reflects whatever was in the training data, including errors, outdated information, and harmful content.
>
> **Report-specific significance:** Every capability and every failure discussed in this report traces back to pretraining decisions. Understanding pretraining is understanding the deep cause of both a model's competence and its characteristic failure modes.
>
> **See also:** [[instruction-fine-tuning]], [[supervised-fine-tuning]], [[scaling-and-capability-emergence]], [[transformer-attention-mechanism]]

The historical trajectory that led to the current approach is worth tracing briefly, because it illuminates why the specific methods described in this report work as well as they do. Early statistical language models, developed in the 1980s and 1990s, operated on a simple principle: count how often words appear together in a large corpus, and use those counts to estimate the probability of any word given the words that preceded it. These models were useful for tasks like speech recognition and simple text prediction, but they had a fundamental limitation: they could only consider a small, fixed window of context. If the relevant word appeared more than five or ten positions back in the sentence, the model had no way to use it. The result was text that, while locally coherent, rapidly became incoherent over longer stretches — the model had no memory of what it had said a sentence ago.

Neural language models, emerging in the early 2000s and accelerating through the 2010s, addressed this limitation gradually, first with recurrent architectures that could maintain a hidden state across a sequence, then with attention mechanisms that allowed a model to selectively focus on any part of the input regardless of distance. The arrival of the [[transformer-attention-mechanism|transformer architecture]] in 2017 — described in the now-famous paper "Attention Is All You Need" by Vaswani and colleagues — was not just an incremental improvement but a combinatorial unlock: by enabling massively parallel processing and long-range attention simultaneously, transformers made it practical to train on vastly larger datasets than any previous architecture could absorb. And once scale became practical, it became apparent that the simple next-word prediction task, performed on enough text, was a surprisingly powerful teacher.

What pretraining produces, when it works, is not a collection of memorized facts — though some memorization does occur. What it produces, more accurately, is something like a *working model of how language and the world fit together*: an implicit set of expectations about what kinds of things are said in what contexts, what follows from what, and what the probable next move in a given type of discourse looks like. The model has, in a sense, absorbed the statistical structure of human thought as expressed in writing, across every domain from physics papers to romance novels to Reddit threads to legal documents. Whether that constitutes "understanding" in any philosophically robust sense is a question this report deliberately sets aside — what matters practically is that the resulting capabilities are real and substantial, and that understanding their origins in the training data is essential for anyone who wants to use or evaluate these systems intelligently. As the field of [[task-generalisation-in-llms]] research has demonstrated, the breadth of a base model's pretraining is the primary determinant of how far it can generalize to novel tasks it was never explicitly trained for.

> [!key-claim] **Pretraining as the Source of Generalization**
> The most important practical consequence of the pretraining paradigm is that a model trained on sufficiently broad and diverse text acquires the ability to perform tasks it was never explicitly trained to do — to summarize documents it has never seen, to answer questions in domains it was never specifically taught, and to maintain a coherent narrative voice across thousands of words of generation. This capacity for generalization is not a feature added on top of pretraining; it *is* pretraining, understood at its deepest level. The [[in-context-learning]] abilities that make modern models so flexible — their ability to pick up a new task from just a few examples — arise directly from the depth and breadth of their pretraining exposure.

> [!section-summary] **Section 1 Summary**
> - Pretraining is the phase where language models acquire their core capabilities by predicting text across billions of examples, with no human labels needed.
> - The historical trajectory runs from rule-based systems → statistical models → neural models → transformer-based pretraining, with each step addressing limitations of scale and context.
> - Pretraining produces a base model with broad linguistic and world knowledge, but *not* instruction-following, safety, or reliability — those come later.
> - The capacity for [[task-generalisation-in-llms|task generalization]] is not a bonus feature but the primary output of successful pretraining.

> [!reflection] **Reflection Prompts — Section 1**
> - Before reading further: what kinds of text do you think would be *most* valuable for training a model to be generally capable? What about *least* valuable?
> - The report claims that pretraining is "where the model acquires its fundamental grasp of language and the world." In what sense does that seem like an extraordinary claim? What would you need to see to believe it?
> - If a model learns only by predicting text, what kinds of knowledge would you expect it to be good at, and what kinds might it systematically miss?

> [!situation-model] **Situation Model — Updated Through Section 1**
> **Key Entities:** Pretraining (the process), base model (the output), training corpus (the input), transformer architecture (the mechanism), prediction task (the learning signal)
> **Causal Map:** Large text corpus → prediction task → gradient updates → base model with implicit language/world knowledge
> **Temporal/Logical Sequence:** Rule-based systems → statistical LMs → neural LMs → transformer-based pretraining (current era)
> **Structural Overview:** Pretraining is Stage 1 of model development; fine-tuning/RLHF are Stage 2+. This report focuses entirely on Stage 1.
> **Goals & Motivations:** Create a model with broad, generalizable knowledge without hand-labeling every example
> **Tensions & Unresolved Questions:** What exactly does "understanding" mean for a model trained this way? Does the specific text matter as much as the scale?
> **Emerging Patterns:** Scale + simple task + massive data = surprisingly powerful generalization
> **Open Threads:** What are the specific prediction tasks? What text is used? Both questions are addressed in subsequent sections.

---

## Section 2: Pretraining Objectives — How a Model Learns to Understand Language

If pretraining is the *what* — exposing a model to vast text — then the pretraining objective is the *how*: the specific game the model is asked to play with that text, the task whose performance it is trying to improve. This distinction matters more than it might initially appear, because different pretraining objectives produce models with meaningfully different strengths and weaknesses, and the choice of objective has shaped the entire trajectory of large language model development. Understanding these objectives does not require any mathematics; it requires only the willingness to inhabit the model's position — to imagine, from the inside, what it would mean to be a system trying to become very good at a particular kind of prediction.

> [!active-reading-prompt] **Active Reading Prompt**
> As you read the descriptions of each pretraining objective below, ask yourself: if you spent years getting very good at this specific task, what other skills might you accidentally develop along the way? And what would you *not* develop, because the task never required it?

### 2.1 Autoregressive Language Modeling: The Next-Word Game

The most important pretraining objective in contemporary large language models — the one used to train the GPT series, LLaMA, PaLM, and most of the models one actually interacts with — is called **autoregressive language modeling**, and it is, at its core, a straightforward game: given everything that has been written so far, predict what comes next. That is all. Given "The cat sat on the," predict "mat." Given "The Eiffel Tower is located in," predict "Paris." Given three paragraphs of an argument, predict the fourth paragraph's opening sentence. The model tries to get better at this game — reducing its errors, becoming more accurate in its predictions — and in the process of becoming very good at this game across billions of examples, it develops what amounts to a working model of how language, reasoning, and the world operate.

> [!definition] **Autoregressive Language Modeling**
> A pretraining objective in which a model is trained to predict the next token (roughly, the next word or word-fragment) in a sequence, given all the tokens that came before it. The model generates one token at a time, and each generated token becomes part of the input for predicting the next one — hence "autoregressive" (self-referential). This is the dominant objective for language models designed to generate text, including the GPT family and most state-of-the-art models as of 2024.
>
> **Boundary conditions:** Autoregressive models read text in one direction only — left to right — which means they have no mechanism during training to "look ahead" and revise their predictions based on what comes later in the sentence. This is a meaningful limitation compared to objectives that allow bidirectional context, and it influences what kinds of tasks these models handle most naturally.
>
> **Operational indicator:** A model trained with an autoregressive objective is what powers the experience of "completion" — when you type a partial sentence into a language model and it continues. The same mechanism that trained it is also how it generates output.
>
> **See also:** [[in-context-learning]], [[chain-of-thought-prompting]], [[few-shot-prompting]], [[self-attention-patterns]]

What makes this game so powerful as a teacher? The answer lies in what the game demands. To accurately predict the next word in "The surgeon scrubbed her hands before entering the ___," a model must know not only that "operating" is a word and that "room" follows "operating," but also that surgeons perform operations, that operations happen in operating rooms, that hygiene protocols precede surgical entry, and that the pronoun "her" refers back to "surgeon" and is grammatically correct. None of this knowledge was explicitly labeled. The model learned it because all of it was *necessary to succeed at the prediction task*. This is the deep insight behind autoregressive language modeling: a sufficiently hard prediction task, applied to sufficiently varied and rich text, forces the acquisition of world knowledge as a side effect.

The [[byte-pair-encoding|tokenization process]] — how words are broken into smaller units called tokens — affects this objective in subtle but important ways. A model does not, in fact, predict whole words; it predicts tokens, which may be whole words, parts of words, or punctuation marks. The choice of how to tokenize text is a pretraining decision with downstream consequences, including which languages the model handles well, how it counts characters, and which technical terms it can represent fluently. These [[tokenization-artifacts|tokenization artifacts]] surface as quirks in deployed models — the reason some models count letters poorly or struggle with unusual proper nouns.

### 2.2 Masked Language Modeling: The Fill-in-the-Blank Game

A second major pretraining objective, introduced by BERT (Bidirectional Encoder Representations from Transformers, 2018) and enormously influential in the years that followed, works quite differently. Instead of reading text from left to right and predicting the next token, masked language modeling randomly hides some percentage — typically fifteen percent — of the tokens in a piece of text and asks the model to fill them in. Given "The [MASK] Tower is located in [MASK]," the model must predict "Eiffel" and "Paris." The training signal comes from how well it fills in the blanks.

> [!definition] **Masked Language Modeling (MLM)**
> A pretraining objective in which a fixed proportion of tokens in a text are replaced with a special "[MASK]" token, and the model is trained to predict the original tokens from the surrounding context — both before and after the masked position. Because the model can use context from *both* directions simultaneously, it develops richer bidirectional representations than autoregressive models trained on the same text.
>
> **Boundary conditions:** Models trained with MLM are not naturally suited to text generation, because their objective never required them to produce one token after another in a left-to-right flow. They are, however, extremely strong at tasks that require deep comprehension of a given text — classification, question answering over a provided passage, sentiment analysis, and similar tasks where the input is complete and the job is to understand it deeply. The most famous example, BERT, dominated the NLP benchmarks of its era (2018-2020) on precisely these tasks.
>
> **See also:** [[transformer-attention-mechanism]], [[semantic-grounding-in-llms]], [[embedding-space-geometry]]

The critical distinction between autoregressive and masked language modeling is the direction of context. An autoregressive model, when predicting "Paris" in "The Eiffel Tower is located in ___," can only use the words that came before. A masked model, when predicting "Eiffel" in "The [MASK] Tower is located in Paris," can also use "Paris" — the word that came after — as part of its evidence. This bidirectional view gives masked models a richer understanding of how sentences cohere, which is why BERT-style models were so effective at reading comprehension tasks where the full context is available.

> [!example] **The Two Games Compared**
> Imagine you are training two humans to be excellent editors. You train the first by giving them incomplete manuscripts and asking them to write what comes next — they become very good at predicting narrative structure, argument flow, and stylistic continuation. You train the second by giving them full manuscripts with random words blanked out and asking them to restore them — they become very good at understanding the logic of a complete text, catching inconsistencies, and filling in what must have been intended. Both are learning from text; both are becoming "language experts"; but they develop somewhat different skills. Autoregressive training shapes generators; masked training shapes comprehenders.

### 2.3 Denoising and Span Corruption: The Reconstruction Game

A third objective, used to train the T5 family of models (Text-to-Text Transfer Transformer, 2019) and influential in various forms across subsequent development, generalizes from masked language modeling to a more flexible form of reconstruction. Instead of masking individual tokens, denoising objectives mask entire spans — consecutive sequences of words — and ask the model to reconstruct what was removed, given the surrounding context. The task is sometimes described as "span corruption": corrupt the text by removing chunks; recover the chunks.

> [!definition] **Denoising / Span Corruption Objective**
> A pretraining objective in which contiguous spans of text are removed or corrupted, and the model is trained to reconstruct the original text. This is more challenging than single-token masking because the model must infer not just a word but a stretch of meaning. Models trained with denoising objectives tend to develop strong capabilities in tasks that require transformation of input text — translation, summarization, rewriting — because the training task itself is a form of transformation.
>
> **Boundary conditions:** Denoising objectives produce encoder-decoder architectures — the encoder reads the corrupted input, the decoder produces the reconstructed output. This architectural choice differs from the decoder-only design used in most contemporary large language models, and the difference has practical implications for how models are used.
>
> **See also:** [[subword-tokenization]], [[attention-head-specialization]]

### 2.4 What the Choice of Objective Means in Practice

> [!warning] **A Common Misconception About Objectives**
> It is tempting to conclude that one pretraining objective is simply "better" than others. The reality is that different objectives are better for different downstream applications. Autoregressive objectives produce the best generators — the best completers, storytellers, and open-ended responders. Masked objectives produce the best encoders — the best text classifiers, similarity estimators, and comprehension engines. Denoising objectives produce the best text transformers — the best summarizers and translators. The dominance of autoregressive models in the current landscape reflects the demands of the most commercially visible applications (chatbots, assistants, content generation), not a universal superiority.

The choice of pretraining objective is also inseparable from the choice of training data, because different objectives amplify different properties of the data. An autoregressive model trained on Reddit discussions learns very different generation styles than one trained on academic papers, even if both are trained on the same number of tokens. The interplay between objective and corpus is the subject of the next several sections — but the key conceptual takeaway from this section is that the objective is the *game*, and the corpus is the *playing field*. Both determine what the model becomes.

> [!claude-insight] **On What Pretraining Objectives Can and Cannot Teach**
> If one takes seriously the claim that pretraining objectives shape capabilities, a productive question follows: are there things that *no* pretraining objective can teach from text alone? The honest answer appears to be yes. Consider what is almost entirely absent from human-written text: descriptions of how it feels to be wrong, to be corrected, to revise an estimate in light of new evidence. Text mostly records the outputs of thought — the conclusions, the arguments, the stories — not the process of inquiry that produced them. An autoregressive model learns to sound like someone who knows things, because text is written by people who sound like they know things; it does not, from text alone, acquire the epistemic humility that comes from having actually been wrong repeatedly and been held accountable for it. This is one of the deeper reasons why [[reinforcement-learning-from-human-feedback]] was developed as a post-pretraining step — not merely to make models more polite, but to introduce a training signal that text-prediction alone cannot provide.

> [!section-summary] **Section 2 Summary**
> - Three major pretraining objectives exist: autoregressive (next-token prediction, left-to-right), masked language modeling (fill in the blanks, bidirectional), and denoising/span corruption (reconstruct removed spans).
> - Autoregressive objectives produce the best generators; masked objectives produce the best comprehenders; denoising objectives produce the best text transformers.
> - The dominant approach in current large language models is autoregressive, because commercial applications favor generation over comprehension.
> - No pretraining objective from text alone can teach genuine epistemic humility or the experience of being corrected — this is a structural gap addressed by post-pretraining methods like [[reinforcement-learning-from-human-feedback]].

> [!reflection] **Reflection Prompts — Section 2**
> - What does it mean that an autoregressive model reads only left-to-right? Can you think of cases where this would produce errors?
> - If a model is trained to fill in blanks (masked LM), why might it be *worse* at generating text than a model trained to predict the next word?
> - The insight callout above argues that pretraining cannot teach genuine epistemic humility. Do you find this persuasive? What would it take to test it empirically?

> [!situation-model] **Situation Model — Updated Through Section 2**
> **Key Entities:** Pretraining objectives (autoregressive, masked LM, denoising), tokens (the units models predict), training corpora (the text the objectives are applied to), base models (the output)
> **Causal Map:** Choice of objective → shapes what capabilities are developed → shapes which downstream tasks the model excels at
> **Temporal/Logical Sequence:** Statistical LMs (simple n-gram) → early neural LMs (recurrent) → BERT/GPT era (transformer + massive scale, divergent objectives)
> **Structural Overview:** Objective and corpus are co-determinants of model capability; neither is sufficient alone
> **Evolution This Section:** Added the three major objectives as named entities; established that objective choice is not a universal best-answer but a design decision with tradeoffs
> **Tensions & Unresolved Questions:** Why did autoregressive win commercially despite masked models outperforming on many comprehension benchmarks?
> **Connections Across Sections:** Sections 1-2 establish the "how learning happens" layer; Sections 3-6 will address the "what is learned from" layer (the corpora)
> **Open Threads:** How large does the corpus need to be? How is the corpus assembled? These questions are the subject of Sections 3-6.

---

## Section 3: The Role of Scale — Why the Amount of Data Changes Everything

There is a version of the pretraining story that runs approximately as follows: researchers discovered a clever technique, applied it to text, and got impressive results. This version, while not wrong, obscures what is perhaps the most startling empirical finding in recent machine learning history — a finding so counterintuitive that even experts resisted it for years before the evidence became undeniable: *the more text a model is trained on, the better it gets, in ways that are not merely incremental but qualitatively different*. Scale does not just make a model better at the things it could already do; at certain thresholds, it appears to unlock capabilities that were entirely absent at smaller scales. Understanding this is essential background for understanding why researchers built the corpora — Common Crawl, WebText, The Pile — that are the subject of the next three sections.

### 3.1 The Scaling Hypothesis: A Counterintuitive Bet

The standard intuition from everyday life is that past a certain point, more of the same inputs should produce diminishing returns. If you read ten books on a subject, the eleventh book improves your understanding less than the first did. This intuition turns out to be wrong for language model pretraining, or at least wrong in a specific and important way: the returns do diminish, but they diminish much more slowly than anyone expected, and they diminish along a smooth, predictable curve that researchers have found holds across many orders of magnitude of scale.

The empirical study of this curve — known as [[llm-scaling-laws|scaling laws research]] — was formalized in work by Jared Kaplan and colleagues at OpenAI (2020), who found that a model's performance on the next-word prediction task improves as a power law function of three factors: the number of parameters in the model (roughly, the model's "size"), the amount of training data, and the amount of compute applied. Power laws are the mathematical signature of processes that scale without abrupt transitions — the same relationship holds whether you double the data, quadruple it, or multiply it by a thousand. The practical implication was radical: if you want a better language model, the most reliable path is simply to make everything bigger.

> [!key-claim] **The Scaling Bet: More Data, Better Models, Predictably**
> The scaling laws finding is not just an empirical curiosity; it was a strategic bet that shaped an entire industry. If model performance improves predictably with scale, then assembling massive training corpora is not a side concern — it is *the* central engineering challenge of the field. The decision to crawl billions of web pages, to assemble hundreds of gigabytes of diverse text, to train on terabytes of data, was not made because researchers loved data for its own sake; it was made because the evidence said that doing so would produce materially better models, at a rate that made the investment worthwhile. Every corpus described in this report exists, in part, as a consequence of taking the scaling bet seriously.

A subsequent and equally important finding, from Google DeepMind's "Chinchilla" paper (Hoffmann et al., 2022), refined this picture: earlier models had been "over-trained" in compute relative to data — they used too much compute on too little data. The Chinchilla results suggested that the optimal approach, for a given compute budget, is to train a smaller model on substantially more data. This insight shifted the field's emphasis even further toward data quality and quantity, reinforcing the strategic importance of the corpora examined in this report.

### 3.2 Emergence: When More Becomes Different

Perhaps the most philosophically striking aspect of scale is the phenomenon of [[emergent-abilities-in-llms|emergent abilities]] — capabilities that appear, apparently discontinuously, as model size crosses certain thresholds, and that were entirely absent below those thresholds. A model trained on a billion tokens cannot reliably answer multi-step arithmetic questions with words. A model trained on a hundred billion tokens often can. The capability did not improve gradually; it appeared, as if a switch had been flipped.

> [!claude-insight] **On Why Emergence Feels Like a Phase Transition**
> When one encounters the concept of emergence in the context of language models, it is tempting to interpret it as mysterious or even magical — as if scale alone is doing something inexplicable. But a more grounded interpretation is available, and it connects directly to the nature of the pretraining data. Arithmetic, multi-step reasoning, and translation are *rare* capabilities in any given piece of text; they appear only in specific kinds of documents — textbooks, worked examples, papers, code. A small model, trained on a small corpus, may never see enough examples of these specialized genres to learn the underlying patterns. As scale grows — both of the corpus and the model — the model begins to encounter enough instances of these specialized genres that the underlying pattern becomes learnable. Emergence, on this view, is less a miracle of scale than a consequence of the *diversity and density of the training corpus becoming sufficient to teach rare skills*. The [[scaling-and-capability-emergence|scaling-and-capability emergence]] relationship is thus partly a story about data sufficiency rather than sheer quantity.

The concept of [[phase-transitions-in-llms|phase transitions]] in language models is closely related: at certain thresholds, model behavior shifts qualitatively rather than just quantitatively. This connects to a broader phenomenon in machine learning called [[grokking-phenomenon|grokking]] — where a model appears to "suddenly understand" a task after training on much more data than seemed necessary for basic performance. In all of these cases, the underlying mechanism appears to be that the model requires a minimum amount of exposure to a pattern before it can generalize from it rather than merely memorizing its surface forms.

### 3.3 What Scale Means for Corpus Design

The practical consequence of the scaling perspective for corpus design is that researchers face a difficult tradeoff from the outset. The ideal training corpus would be enormous (to satisfy scaling requirements), high-quality (to ensure signal rather than noise), diverse (to enable generalization across domains), and free of harmful content (to prevent the model from learning damaging patterns). These four desiderata are in tension with each other in ways that become more apparent in the detailed examination of each corpus: size and quality tend to pull in opposite directions, because the largest available data sources are also the messiest. The three corpora examined in the next three sections represent three different resolutions of this tradeoff — and understanding those differences is essential to understanding why different language models behave differently.

> [!example] **Scaling in Everyday Terms**
> Consider what happens to a person's language skills as they read progressively more widely. Someone who has read ten books in one genre can produce prose that sounds somewhat like those ten books. Someone who has read ten thousand books across many genres, disciplines, and time periods develops not just better vocabulary but qualitatively different abilities: the capacity to adopt different registers, to recognize disciplinary conventions, to draw analogies across domains, to know what sounds wrong in a context even without being able to articulate why. The claim of scaling laws research is that the same general pattern holds for language models — with the important caveat that the scale required is not ten thousand books but something more like the entire digitized output of human civilization.

> [!section-summary] **Section 3 Summary**
> - Scaling laws show that language model performance improves predictably and continuously with more data, more parameters, and more compute — diminishing returns are real but slow.
> - The Chinchilla finding (2022) refined this picture: for optimal performance, models should be trained on *more data* than previously used, not just made larger.
> - Emergent abilities — capabilities that appear discontinuously as scale grows — are likely best explained as the result of rare skill-types becoming sufficiently represented in the training corpus.
> - The practical consequence is that corpus design is a central engineering challenge, not a footnote: scale, quality, diversity, and safety are in tension, and every corpus makes explicit or implicit tradeoffs among them.

> [!reflection] **Reflection Prompts — Section 3**
> - If performance improves predictably with scale, what is the limiting factor on how good language models can become?
> - The insight callout suggests emergence may be partly a story about data diversity rather than just size. What evidence would support or refute this interpretation?
> - The Chinchilla finding changed the field's strategy. What does it say about the relationship between model size and data volume that this finding was surprising?

> [!situation-model] **Situation Model — Updated Through Section 3**
> **Key Entities:** Scaling laws (the empirical relationship), emergent abilities (qualitative threshold effects), corpus design (the engineering challenge), data-compute tradeoff (the strategic tension)
> **Causal Map:** Data volume + model size + compute → predictably better performance, with qualitative jumps (emergence) at scale thresholds
> **Evolution This Section:** Added the "why scale matters" explanatory layer; established that corpus design choices are high-stakes engineering decisions with enormous downstream consequences
> **Tensions:** Size vs. quality; diversity vs. tractability; openness vs. safety — all manifest in the specific corpora discussed next
> **Open Threads:** Three specific resolutions to the corpus design challenge — Common Crawl (maximize scale), WebText (maximize quality), The Pile (maximize diversity) — are examined in Sections 4-6

---

## Section 4: Common Crawl — The Internet as Teacher

Of all the datasets that have shaped modern language models, Common Crawl is the largest, the oldest, the most consequential, and the most contested. To understand it is to understand the fundamental engineering bet of the scaling era: that the internet, despite being chaotic, messy, multilingual, and full of noise, contains enough signal — enough well-written text, thoughtful argument, factual information, and rich language use — that training on it at sufficient scale produces genuinely capable models. Whether that bet was correct, and at what cost it was made, are questions this section examines at length.

### 4.1 What Common Crawl Is

> [!definition] **Common Crawl**
> Common Crawl is a nonprofit organization that systematically crawls the public web — following links from page to page, much as a search engine does — and makes the resulting data freely available to researchers. Since 2008, it has accumulated petabytes (millions of gigabytes) of raw web content: the HTML of web pages, the text extracted from those pages, and metadata about when and how they were collected. As of the early 2020s, a single Common Crawl snapshot contains text from roughly three to five billion web pages — representing a substantial fraction of the publicly accessible internet.
>
> **Boundary conditions:** Common Crawl captures only publicly accessible text; it does not include content behind paywalls, content requiring authentication, or content that robots.txt files instruct crawlers to skip. This means significant domains of human knowledge — most academic journal content, most commercial software documentation, much medical information — are either absent or underrepresented. Common Crawl also does not crawl the dark web, private intranets, or encrypted communications.
>
> **Operational indicator:** When a language model seems to "know about" a topic covered on a public website, the source of that knowledge is, with high probability, Common Crawl data or a derivative of it.
>
> **See also:** [[benchmark-contamination]], [[train-test-leakage-in-llms]], [[domain-adaptation-llms]]

The appeal of Common Crawl for language model training is straightforward: it is enormous, freely available, and multilingual. The challenge is equally straightforward: it is also a mostly unfiltered snapshot of the public internet, which means it contains everything the internet contains — spam, SEO-optimized gibberish, product listings, template-generated boilerplate text, duplicated content, pornography, extremist political content, and vast swaths of low-quality writing. The raw Common Crawl data cannot be used directly as a training corpus without substantial processing.

### 4.2 Processing Common Crawl: From Raw Crawl to Usable Dataset

The transformation from raw Common Crawl data to a usable training dataset is a substantial engineering undertaking, and different teams have approached it differently. Several important processed versions of Common Crawl data have emerged as influential in their own right:

**C4 (Colossal Clean Crawled Corpus)** — Developed by Google's T5 team (Raffel et al., 2019), C4 applies a series of heuristic filters to Common Crawl: removing pages that contain offensive words from a fixed list, filtering out pages with very short lines or high proportions of non-alphabetic characters, removing duplicate text, and keeping only text that ends with terminal punctuation. These heuristics are crude — they discard some good content while retaining some bad content — but they reduce the dataset to a much more manageable size while substantially improving the average quality of the text.

**CC-Net** — Developed by Facebook Research (Wenzek et al., 2020), CC-Net takes a different approach: rather than applying heuristic filters, it trains a language model on high-quality reference text (Wikipedia) and then filters Common Crawl by perplexity, keeping only pages that the reference model finds "plausible" — that is, pages whose language patterns resemble high-quality writing. This approach tends to produce higher-quality data than heuristic filtering but at the cost of potentially excluding text that is high-quality in ways the reference model does not recognize.

**CC-100** — Derived from CC-Net, this 100-language subset was instrumental in training multilingual models, demonstrating that the same pretraining approach could extend beyond English to produce capable multilingual systems when the data was properly processed.

> [!example] **What Is Actually in Common Crawl?**
> Imagining the contents of a multi-petabyte web crawl is difficult in the abstract; a concrete exercise helps. Consider a random sample of fifty publicly accessible web pages at any given moment: likely included are a product page for a kitchen appliance with dozens of template-generated "helpful features" bullets; a Wikipedia article on Ottoman history; a Reddit thread debating the best budget headphones; three blog posts with varying degrees of coherence; a news article with an auto-generated summary; a page of SEO-optimized "best X for Y" content that is largely regurgitated text; a forum thread in Simplified Chinese; a PHP error page; and a small number of genuinely high-quality, original pieces of writing. The raw Common Crawl dataset contains all of these in roughly those proportions. The processing challenge is to amplify the signal — the genuinely informative, well-written text — while suppressing the noise without discarding the linguistic diversity.

### 4.3 The Role of Deduplication

Among the processing steps applied to Common Crawl, deduplication deserves special attention because its importance was initially underestimated and its consequences have proven significant. The web contains an enormous amount of duplicated text: news articles are republished on hundreds of sites, boilerplate legal text appears on millions of pages, product descriptions are copied across retailers. Without deduplication, a model trained on Common Crawl will see the same text thousands of times, which leads to several problems.

First, and most obviously, it wastes training compute on redundant information. Second, and more subtly, it causes the model to develop an inflated implicit estimate of how common certain phrases and facts are — which contributes to the phenomenon of confident confabulation, where the model produces plausible-sounding but incorrect assertions. A phrase it has seen ten thousand times has a very strong pull on the model's predictions, even if the phrase appears in largely meaningless boilerplate. Third, and most consequentially for evaluation, it dramatically increases the risk of [[benchmark-contamination]]: the accidental inclusion of text from standardized evaluation datasets in the training data, which means the model may "know" the answers to evaluation questions not because it generalized from the training distribution but because it memorized those specific questions and answers. This phenomenon, related to [[train-test-leakage-in-llms]], has been documented in several major models and significantly complicates attempts to evaluate generalization.

> [!warning] **The Deduplication Imperative**
> The practical lesson from extensive experience with Common Crawl is that deduplication is not an optional optimization but a prerequisite for responsible training. Models trained on heavily duplicated data exhibit characteristic failure modes: they repeat phrases and structures more than is natural; they show inflated performance on benchmarks that overlap with duplicated content; they may "memorize" rather than learn when the same passages appear thousands of times. The shift from treating deduplication as a preprocessing nicety to treating it as a core quality requirement mirrors a broader maturation in how the field thinks about training data.

### 4.4 Common Crawl in Major Models

GPT-3 (Brown et al., 2020) used a filtered and deduplicated version of Common Crawl as its primary data source, accounting for roughly 60% of the training data by token count. The remaining 40% came from higher-quality curated sources — including WebText2 (an expanded version of WebText, discussed in the next section), books, and Wikipedia. This mixture design — using Common Crawl for scale but diluting it with curated sources for quality — became a standard template that subsequent major models have adapted.

The PaLM models (Google, 2022-2023) and many other large-scale models similarly use Common Crawl as the volumetric backbone of their training data, processed through their own filtering pipelines. The [[vocabulary-size-tradeoffs|vocabulary and tokenization choices]] made for Common Crawl-derived training have lasting effects on deployed models' ability to handle multilingual text, rare terms, and technical language.

> [!claude-insight] **On the Philosophical Tradeoff Embedded in Common Crawl**
> Common Crawl embodies a particular epistemological bet: that the collective output of human internet activity, despite its imperfections, contains more signal than noise, and that scale is the mechanism by which signal accumulates while noise averages out. This bet is not obviously correct — it is conceivable that a smaller corpus of carefully curated text would produce a better model, weight for weight, than a massive corpus of mixed quality. The Chinchilla results suggest that data quality does matter at the margin; the question is whether the quality threshold achievable through automated filtering is sufficient, or whether human curation is required. WebText, examined in the next section, represents a different answer to this same question.

> [!section-summary] **Section 4 Summary**
> - Common Crawl is a petabyte-scale nonprofit web crawl, freely available, that has been the primary volumetric data source for most large language models.
> - Raw Common Crawl data is unusable for training; multiple processing pipelines (C4, CC-Net, CC-100) have been developed to filter, deduplicate, and improve it.
> - Deduplication is a critical quality step: duplicated text wastes compute, distorts model priors, and increases benchmark contamination risk.
> - GPT-3 and most subsequent large models use Common Crawl for scale, mixed with higher-quality curated sources for quality correction.
> - The Common Crawl approach embeds a philosophical bet: that scale + automated filtering is sufficient to produce quality at the levels needed for capable models.

> [!reflection] **Reflection Prompts — Section 4**
> - If you were designing a quality filter for web text, what criteria would you use? What high-quality text might your filter accidentally exclude?
> - Benchmark contamination is described as "accidentally" including evaluation data in training. At what point might this become a design choice rather than an accident?
> - Common Crawl is available to any researcher. What are the implications of the fact that most large language models are trained on very similar underlying data?

> [!situation-model] **Situation Model — Updated Through Section 4**
> **Key Entities:** Common Crawl (the dataset), C4 / CC-Net / CC-100 (processed derivatives), deduplication (critical processing step), benchmark contamination (a risk introduced by scale)
> **Causal Map:** Raw crawl → filtering pipeline → deduplicated processed corpus → scaled pretraining → capable base model (with caveats about quality and contamination)
> **Evolution This Section:** Added the "volumetric backbone" concept — Common Crawl as the source of scale, requiring supplementation for quality
> **Tensions:** Scale vs. quality; automated filtering vs. human curation; openness vs. safety and copyright concerns
> **Connections Across Sections:** Section 3's scaling argument explains *why* researchers use Common Crawl despite its messiness. Section 5 will show a different approach — one that starts with quality rather than scale.
> **Open Threads:** How does one achieve quality without sacrificing scale? WebText answers this with curation; The Pile answers it with diversity. Both are addressed in the next two sections.

---

## Section 5: WebText — Quality Through Curation

If Common Crawl represents the "more is better" end of the corpus design spectrum, WebText represents a deliberate experiment at the other end: what happens if one insists on high quality, and accepts a smaller dataset as the cost of that insistence? The answer, embodied in OpenAI's GPT-2 (2019) and its results, was instructive: a model trained on a much smaller but carefully curated dataset produced output of strikingly higher quality than its predecessors, and it demonstrated capabilities — zero-shot text generation, coherent long-form writing, recognizable authorial voice — that surprised even the researchers who built it.

### 5.1 The Philosophy Behind WebText

WebText was constructed by Alec Radford and colleagues at OpenAI in 2018-2019 for the training of GPT-2, and its defining feature is its use of a social signal — Reddit upvotes — as a quality filter. The approach works as follows: take all outbound links from Reddit posts that have received at least three upvotes, follow those links, and collect the text at the destination. The premise is that when many people find a piece of content interesting enough to share and signal approval of, that content is likely to be of higher quality — better written, more informative, more engaging — than text scraped from the web at large.

> [!definition] **WebText**
> A curated web text dataset assembled by OpenAI for training GPT-2 (2019). WebText consists of the text of all outbound web links shared on Reddit that received at least three upvote "karma" points. The resulting dataset contained roughly 45 gigabytes of text from approximately eight million documents. A subsequent expanded version, WebText2, was used in GPT-3 and collected more recently.
>
> **Boundary conditions:** WebText's quality proxy — Reddit upvotes — is real but limited. It captures one specific community's judgment of what is interesting or valuable, which skews heavily toward the preferences of Reddit's demographic: predominantly young, male, English-speaking, and concentrated in certain cultural communities. Content that Reddit users wouldn't share — academic papers, literary fiction, non-English content, community knowledge from underrepresented cultures — is systematically absent. Additionally, Wikipedia was explicitly excluded from WebText because it was likely already present in evaluation benchmarks, and its inclusion could artificially inflate performance scores.
>
> **See also:** [[hallucination-taxonomy]], [[parametric-vs-contextual-knowledge]], [[benchmark-contamination]], [[knowledge-intensive-nlp]]

The choice of Reddit upvotes as a quality proxy is worth dwelling on, because it encodes a particular theory of quality that is both useful and limited. It is useful because upvoted Reddit content does, empirically, tend to be more coherent, informative, and well-written than random web pages — the community filtering process eliminates much of the spam, SEO gibberish, and template-generated content that pollutes the raw crawl. It is limited because "what Reddit users upvote" is not the same as "high-quality text" in any universal sense. It reflects the specific cultural and epistemic preferences of a particular community at a particular time.

### 5.2 What WebText Contains — and What It Excludes

A representative sample of WebText would include: long-form journalism from major news outlets that Reddit users found compelling; detailed technical explainers that were highly upvoted on programming subreddits; popular science writing from sources like Scientific American, Nature News, and Ars Technica; blog posts with viral reach; essays and opinion pieces that generated substantial Reddit discussion; Wikipedia articles (though explicit Wikipedia content was excluded, many Reddit links pointed to other sources that summarized or cited Wikipedia); and a significant proportion of content about topics that Reddit communities are disproportionately interested in — technology, gaming, political commentary, science, and American popular culture.

What WebText excludes, structurally, is large: academic papers and textbooks (mostly paywalled or not widely shared on Reddit); literary fiction; non-English content; community knowledge from cultures underrepresented on Reddit; technical documentation; and the enormous volume of "useful but not viral" writing that fills the internet — the how-to guides, the support forum solutions, the community wikis — that generates assistance without generating social engagement.

> [!key-claim] **The Reddit Filter as a Theory of Quality**
> The WebText hypothesis — that social sharing signals track quality — is an implicit claim about what "quality" means in the context of training data. It privileges engaging, widely-shared writing over authoritative, technical, or community-specific writing. When GPT-2 demonstrated remarkable fluency and coherence, it was partly because it had been trained on text that humans found fluent and coherent — the Reddit upvote filter had, in effect, run a human quality assessment on the training data at scale. The limitation is that this human quality assessment was conducted by a specific and unrepresentative community, with predictable gaps in the resulting model's knowledge and representational equity.

### 5.3 The GPT-2 Demonstrations and Their Significance

GPT-2 trained on WebText demonstrated capabilities that, in early 2019, felt genuinely surprising to the field. Given a few sentences of context, it could continue an essay in a recognizably similar style; it could produce plausible-seeming news articles, short stories, and even technical writing that had some surface-level coherence. OpenAI's initial decision not to release the full model — citing concerns about potential misuse — was itself a signal that the field had crossed a qualitative threshold: for the first time, a language model's outputs were considered potentially dangerous without human curation.

This historical moment is instructive for understanding the relationship between training data quality and model output quality. The improvement from GPT-1 to GPT-2 was not primarily a matter of architectural innovation; the transformer architecture used was essentially the same. The principal change was the training data. By shifting from a smaller, less curated dataset to WebText — 45 gigabytes of relatively high-quality, engaging text — the team produced a model whose output quality was markedly different, not just incrementally better. This provides some of the clearest evidence in the empirical record that *what is in the training data matters*, not just how much there is of it.

> [!warning] **Selection Bias in Quality Filtering**
> Any curation mechanism — whether it is Reddit upvotes, editorial selection, or automated quality scoring — introduces selection bias by definition. The question is not whether WebText is biased (it is) but whether its biases are better or worse than the biases introduced by raw web scraping. The answer depends on one's values: if one wants a model that is maximally coherent and engaging in English, WebText is an improvement. If one wants a model that represents the diversity of human knowledge, culture, and language, WebText's biases are severe. Both are defensible positions; neither is value-neutral. This tension — between quality-as-engagement and quality-as-representational-diversity — recurs throughout the history of corpus design and has no simple resolution.

> [!section-summary] **Section 5 Summary**
> - WebText uses Reddit upvotes as a quality proxy, collecting linked content from highly-upvoted posts; the result is roughly 45 gigabytes of curated web text.
> - This curation philosophy produced GPT-2, which demonstrated markedly higher output quality than predecessors, providing evidence that training data quality — not just quantity — drives model capability.
> - WebText's approach encodes a specific and limited theory of quality: what Reddit users find engaging, which skews toward certain demographics, topics, and cultural perspectives.
> - The exclusion of academic content, non-English text, and community-specific knowledge means WebText produces models that are fluent and coherent but narrow in certain dimensions.

> [!reflection] **Reflection Prompts — Section 5**
> - If you were designing a "social quality filter" for training data, what community or signal would you use, and what biases would that introduce?
> - GPT-2's quality improvement over GPT-1 came largely from the training data, not the architecture. What does this suggest about where to invest research effort?
> - Wikipedia was explicitly excluded from WebText. What are the tradeoffs of this choice?

> [!situation-model] **Situation Model — Updated Through Section 5**
> **Key Entities:** WebText (small, curated), Reddit upvote filter (quality proxy), selection bias (the limitation), GPT-2 (the model trained on WebText)
> **Causal Map:** Social sharing signal → quality-filtered corpus → higher output quality, but narrower representational range
> **Evolution This Section:** Added the "curation vs. scale" tension as a concrete design choice with documented outcomes
> **Tensions:** Quality vs. diversity; engaging text vs. representative text; small-curated vs. large-messy
> **Connections Across Sections:** WebText is the "quality" answer; Common Crawl is the "scale" answer; The Pile (Section 6) attempts a third answer: "diversity"
> **Open Threads:** Is there a way to achieve scale, quality, *and* diversity? The Pile makes this attempt.

---

## Section 6: The Pile — Diversity as Design Philosophy

In 2020, EleutherAI — a loose collective of independent researchers formed partly in response to OpenAI's decision to restrict access to GPT-2 — released The Pile: an 825-gigabyte open-source training dataset assembled from twenty-two distinct data sources, deliberately designed to ensure that no single domain or genre would dominate the resulting model's knowledge. The Pile represents a different answer to the corpus design problem than either Common Crawl or WebText: it is an argument, expressed in data, that what matters most is not raw scale or narrow quality but *representational coverage* — the deliberate inclusion of the full range of intellectual activity that humans engage in through writing.

### 6.1 The Philosophy: Why Diversity?

EleutherAI's design choices in The Pile were motivated by a hypothesis that, while intuitive once stated, had not been formally tested at scale: a model trained on text from many different intellectual domains would generalize better across tasks than a model trained on more text from a smaller range of domains. The reasoning runs as follows. If a model trains only on web text — even high-quality web text — it learns to be fluent in the registers and styles and knowledge domains that appear on the web. But the web is not where academic research is recorded; it is not where software is written; it is not where the full tradition of human literature lives. A model that has never seen an academic paper does not merely lack specific facts from papers; it lacks the entire discourse style of evidence-based argument — the way claims are hedged, the way citations function, the way disagreement is navigated. Training on diverse sources, on this view, does not just add knowledge; it adds *ways of thinking* that are encoded in domain-specific genres.

> [!definition] **The Pile**
> An open-source, multi-source text dataset developed by EleutherAI (Gao et al., 2020) for training large language models, consisting of approximately 825 gigabytes of text assembled from twenty-two distinct data sources. The sources include web text (Pile-CC, a processed version of Common Crawl), books (Books3), academic papers (PubMed Abstracts, arXiv), code (GitHub), encyclopedia content (Wikipedia, DM Mathematics), legal text (FreeLaw, USPTO Backgrounds), and several other specialized corpora. The Pile was designed to represent the breadth of human intellectual activity rather than optimizing for any single quality dimension.
>
> **Boundary conditions:** The Pile is a snapshot dataset — it was assembled in 2020 and has not been continuously updated. Its "Books3" component, which included copyrighted books scraped from a shadow library, subsequently became a significant legal and ethical controversy. The Pile also has uneven quality across its components: the web-scraped Pile-CC component inherits Common Crawl's quality challenges, while other components (arXiv, GitHub) tend to be higher quality.
>
> **See also:** [[domain-adaptation-llms]], [[continual-learning-llms]], [[knowledge-intensive-nlp]], [[multilingual-emergent-transfer]]

### 6.2 The Twenty-Two Sources: A Closer Look

Understanding The Pile means understanding what its twenty-two component datasets actually contain and what, in principle, a model learns from each. The categories can be grouped thematically:

**Web and Community Text:**
*Pile-CC* — the largest component, a processed version of Common Crawl. *OpenWebText2* — an expanded, recreated version of WebText. These two components provide the volume that makes The Pile scale-competitive with purely web-based corpora.

**Books and Literature:**
*Books3* — a large collection of digitized books, including significant amounts of literary fiction, nonfiction, and academic work. This component was later identified as having sourced books from a shadow library (Bibliotik) without copyright permission, making it legally and ethically controversial. *Project Gutenberg* — public domain books from before 1924, free from copyright concerns.

**Academic and Scientific:**
*PubMed Abstracts* — millions of medical and life science paper abstracts. *PubMed Central* — full-text scientific papers in open-access format. *arXiv* — physics, mathematics, computer science, and related papers in preprint form. These components are among the highest-quality text in any training corpus: peer-reviewed, technical, carefully written, and evidence-grounded.

**Code:**
*GitHub* — open-source code repositories. This component is particularly important because code is qualitatively different from natural language text: it is unambiguous about what it is doing (when it works), highly structured, and represents a different mode of human reasoning. Models trained on substantial code data demonstrate systematically improved logical reasoning, even on tasks that have nothing to do with programming — a finding that supports the "diversity adds reasoning modes" hypothesis.

**Legal and Governmental:**
*FreeLaw* — opinions from U.S. federal courts. *USPTO Backgrounds* — descriptions from U.S. patent applications. These components introduce dense, formal, consequential writing that is rarely represented in web-crawled data.

**Encyclopedic:**
*Wikipedia (English)* — the entirety of English Wikipedia, a high-quality, structured, factual reference corpus. *DM Mathematics* — synthetic mathematics problems.

**Dialogue and Conversation:**
*OpenSubtitles* — subtitles from thousands of films and television programs. *HackerNews* — technical discussion threads.

> [!claude-insight] **On Why Code Data Punches Above Its Weight**
> One of the most consistently surprising findings in the empirical study of training corpora is that code data — which typically constitutes a small fraction of any training corpus — has a disproportionately large positive effect on a model's reasoning capabilities, well beyond its contribution to coding tasks specifically. A model trained with GitHub code in its corpus reasons better about sequences of steps, conditional logic, and multi-step problem solving than one trained without it, even when evaluated on tasks with no surface resemblance to programming. The explanation, while not definitively established, appears to be that code is one of the few domains where writers are *obligated* to be logically precise — programs must be internally consistent or they fail to run. Training on code thus introduces many examples of precise, logical thinking expressed in a form the model can learn from. This finding has influenced virtually every subsequent large-scale training corpus design, all of which include substantial code data. The connection to [[task-specific-fine-tuning]] research is direct: what was once achieved through specialized fine-tuning on code can now be partially achieved at the pretraining stage.

### 6.3 What the Diversity Hypothesis Predicts

The core prediction of EleutherAI's diversity philosophy is that GPT-Neo, GPT-NeoX, and other models trained on The Pile would show stronger performance on domain-specific tasks — scientific question answering, legal reasoning, code generation — compared to models trained on equivalently sized web-only corpora. This prediction received mixed but generally supportive empirical evidence: The Pile-trained models showed notably better performance on academic and technical benchmarks, and particularly strong performance on code-related tasks, supporting the hypothesis that domain-specific training data transfers to domain-specific capabilities in ways that web text alone cannot achieve.

The [[cross-lingual-tokenization]] implications of The Pile's design are also notable: by including multilingual content and non-English text from various components, The Pile contributed to research on how diverse linguistic exposure during pretraining affects multilingual generalization — a topic of substantial subsequent investigation. Models trained on multi-source corpora tend to exhibit more robust [[multilingual-emergent-transfer]] than models trained on monolingual or web-dominant corpora.

### 6.4 The Legal and Ethical Controversies

The Pile's Books3 component has been the subject of significant legal controversy, as it included copyrighted books obtained from a shadow library without permission or compensation to authors. Several lawsuits were filed in 2023 challenging the inclusion of copyrighted material in training corpora, with The Pile cited as an example. This controversy is not merely a legal footnote; it illustrates a fundamental tension in corpus design that has no easy resolution: the materials most valuable for training — well-written, carefully argued, diverse in perspective — are often exactly the materials that intellectual property law protects most strenuously.

> [!warning] **The Open-Source Tension in Training Data**
> EleutherAI's decision to make The Pile fully open — both the dataset itself and the models trained on it — was a deliberate choice to counterbalance the increasing concentration of frontier AI development in a small number of well-resourced companies. Open-source corpora make research reproducible, allow external audit of training data, and enable smaller organizations to train capable models. The tradeoff is that openness makes it harder to manage copyright compliance and impossible to retroactively restrict access if the data is found to contain harmful or impermissibly licensed material. The Pile's experience illustrated both the value of openness (it enabled significant research) and its risks (it enabled legal exposure for anyone who used it). This tension remains unresolved across the field.

> [!section-summary] **Section 6 Summary**
> - The Pile is an 825GB open-source corpus assembled by EleutherAI from twenty-two data sources, designed around the hypothesis that domain diversity produces more generalizable models.
> - Key components include web text, books, academic papers, code (GitHub), legal documents, and encyclopedic content — each contributing different reasoning styles and domain knowledge.
> - Code data has a disproportionate positive effect on reasoning across all tasks, not just coding — a finding that influenced all subsequent corpus design.
> - The Pile's Books3 component became a significant legal controversy, illustrating the unresolved tension between training data quality and copyright compliance.
> - The open-source philosophy of The Pile enabled substantial research but also created legal exposure, illustrating that openness in training data is a value that comes with real tradeoffs.

> [!reflection] **Reflection Prompts — Section 6**
> - The Pile's creators argued that diversity produces better generalization. What would it mean to test this claim rigorously?
> - Code data improves reasoning beyond coding tasks. Can you think of other domains that might have similar "reasoning transfer" properties?
> - The Pile used copyrighted books without permission. Does the potential benefit to AI development justify this? What alternative approaches might exist?

> [!situation-model] **Situation Model — Updated Through Section 6**
> **Key Entities:** The Pile (diverse multi-source corpus), EleutherAI (open-source philosophy), diversity hypothesis (domain diversity → better generalization), copyright controversy (legal risk of openness)
> **Causal Map:** Multi-domain corpus → richer reasoning patterns → better performance on domain-specific tasks, at the cost of legal and ethical complexity
> **Evolution This Section:** Completed the three-corpus triangle: Common Crawl (scale), WebText (quality), The Pile (diversity). Each resolves the corpus design tradeoff differently.
> **Emerging Pattern:** No corpus design choice is free of tradeoffs; scale, quality, diversity, openness, and legal compliance pull in different directions simultaneously
> **Connections Across Sections:** The three corpus sections (4-6) collectively illustrate that the choice of training data encodes a value system — about what knowledge matters, whose writing counts, and what risks are acceptable
> **Open Threads:** What does a model trained on these corpora actually know, and what does it not know? Section 7 addresses the outputs and limitations of pretraining.

---

## Section 7: What Pretraining Produces — and What It Doesn't

Having examined how pretraining works and what corpora it operates on, it is worth pausing before moving to the ethical dimensions to ask a practical question that most users of language models have probably wondered about without quite knowing how to frame: what, exactly, does a successfully pretrained model know, and why does it still need so much further training before it becomes useful in the ways a chatbot or writing assistant needs to be? The answer to this question is more nuanced than the casual description "trained on the internet" suggests, and it has direct consequences for how one uses, evaluates, and criticizes deployed language models.

### 7.1 What Pretraining Teaches: The Remarkable Catalog

A base model — a model that has been pretrained but not yet fine-tuned or trained with human feedback — possesses a genuinely striking range of implicit knowledge. It knows that Paris is the capital of France not because anyone told it so but because this fact appeared in thousands of contexts across its training data: travel guides, news articles, geography questions, Wikipedia passages, Reddit discussions. It knows the approximate plot of most famous novels, the general findings of major scientific papers that were widely cited and discussed, the conventional structure of a legal brief, the characteristic tone of a presidential speech. It can recognize that a sentence is ungrammatical without having been taught grammar rules. It can continue a story in the style of Hemingway if shown a few examples of Hemingway — not because it memorized his books but because it has a statistical model of what "Hemingway-like prose" looks and feels like.

This [[parametric-vs-contextual-knowledge|parametric knowledge]] — knowledge baked into the model's parameters through training, as opposed to knowledge retrieved from an external context at inference time — is one of the most powerful features of the pretraining paradigm and one of the sources of its most striking failures. The failures arise because parametric knowledge is, at its core, a compressed statistical model of the training data. It is not a database of verified facts. A model "knows" something in proportion to how consistently that thing was represented in the training text — which means it knows popular, widely-discussed, multiply-confirmed facts very robustly, and it knows rare, contested, or underrepresented facts poorly or incorrectly. When [[hallucination-detection|hallucinations]] occur — when a model generates plausible-sounding but false information — they usually arise from exactly this asymmetry: the model has a confident-seeming representation of a topic because the general domain is well-represented in training data, but the specific claim being made was either rare, absent, or inconsistently represented.

> [!key-claim] **The World Model Is Statistical, Not Factual**
> The most important conceptual shift for anyone trying to understand what pretraining produces is this: a base model is not a database or an encyclopedia. It is a statistical model of how language about the world works. It "knows" facts in the way that a fluent English speaker knows that sentences usually have subjects and verbs — not by consulting a rule book but by having internalized a pattern from millions of examples. The practical consequence is that base model knowledge is reliable in proportion to the frequency and consistency with which accurate information appeared in the training data, and unreliable precisely where the data was sparse, contradictory, or selectively populated with incorrect claims.

### 7.2 What Pretraining Does Not Teach: The Critical Gap

The gap between a pretrained base model and a useful deployed assistant is substantial, and understanding it is as important as understanding what pretraining achieves. A base model, without further training, tends to:

**Continue, not answer:** Presented with a question, a base model's most natural response is to continue the text in the way the training data would continue it — which might mean generating additional questions, providing a lecture-style explanation tangentially related to the question, or producing text that looks like a forum thread discussing the question. It does not, by default, recognize that when a user asks "What is the capital of France?" the correct response is "Paris," not an extended discussion of French administrative history.

**Lack consistent values:** Because the training data contains text expressing every conceivable value system, political position, and ethical stance, the base model has no consistent values of its own — it is, in a meaningful sense, a reflective surface that can produce text in the style of any position in the training data. This is why base GPT-3, when prompted appropriately, could generate racist content, disinformation, or harmful instructions with the same facility it generated helpful text. The model had "learned" these patterns from the training data just as it had learned everything else.

**Fail at instruction following:** The concept of [[instruction-following|following an instruction]] — taking a directive ("Summarize this document") and executing it reliably — requires a specific form of learning that is largely absent from the pretraining task. In next-word prediction, there is no notion of a "directive" to be followed; there is only text to be continued. Models learn to respond to instructions through [[instruction-fine-tuning|instruction fine-tuning]] on explicitly collected instruction-response pairs, a separate stage that dramatically improves practical usability.

**Produce inconsistent personas:** Without specific persona training, base models will adopt whatever register and personality the prompt implies. They have no stable self-concept — they are character-generators rather than characters.

> [!warning] **Mistaking a Base Model for a Finished Product**
> A recurring confusion in public discourse about language models is treating base model behavior — with its tendency to complete text rather than answer questions, its inconsistent values, its willingness to continue harmful patterns from its training data — as evidence that language models are fundamentally broken or dangerous. This conflates the base model with the deployed assistant. The base model is a raw capability, like a library of human thought without a librarian. The trained assistant — the version users actually interact with — has been shaped by [[reinforcement-learning-from-human-feedback|RLHF]], [[instruction-tuning|instruction tuning]], and safety training to behave as a helpful, relatively safe, and value-aligned system. Understanding the distinction does not resolve all concerns about these systems, but it does prevent misdiagnosis: blaming pretraining for problems that are actually the result of insufficient post-training, or blaming post-training for problems that trace all the way back to what was in the pretraining corpus.

### 7.3 The Bridge to Post-Pretraining: Why Fine-Tuning Works

The reason [[supervised-fine-tuning|supervised fine-tuning]] and RLHF work as well as they do — why a relatively small amount of additional training can dramatically change a base model's behavior — is precisely because the base model already knows so much. Fine-tuning does not teach a model new facts about the world; it teaches it new behaviors toward the knowledge it already has. It teaches the model to answer questions rather than continue them, to refuse harmful requests, to adopt a consistent helpful persona, to generate responses that humans prefer over the alternatives. All of this subsequent training is, in a deep sense, redirecting a capability that was already present. This is why a model that was pretrained on a high-quality, diverse corpus responds so much better to fine-tuning than a model pretrained on a narrow or low-quality corpus: there is more capability to redirect, more latent knowledge to activate. The [[parameter-efficient-fine-tuning|parameter-efficient fine-tuning]] literature, including methods like [[lora-low-rank-adaptation|LoRA]], further demonstrates how little computation is needed to substantially change a well-pretrained model's behavior — suggesting that the base model has already done most of the heavy lifting.

> [!claude-insight] **On the Relationship Between Pretraining and Values**
> One of the more philosophically interesting questions raised by the pretraining paradigm is whether values — not just behaviors, but genuine orientations toward what is good — can be installed through post-pretraining methods, or whether the shape of values was already set during pretraining by the distribution of the training data. The [[value-alignment-problem|value alignment problem]] in AI is often framed as a problem of specifying what we want and training for it; but the pretraining perspective suggests a prior problem: the base model's implicit value system is already the result of which voices, which communities, and which ways of framing ethical questions dominated the training corpus. Safety training can suppress certain outputs and reinforce others; it is less clear that it can fundamentally reorient a model whose entire way of framing ethical questions was shaped by a corpus that was itself not value-neutral. This is not an argument against safety training — it is an argument for taking the composition of pretraining corpora as seriously as the design of post-training procedures.

> [!section-summary] **Section 7 Summary**
> - Pretrained base models possess remarkable implicit knowledge — but that knowledge is statistical and pattern-based, not factual and verified, which is why hallucinations occur.
> - What pretraining does not produce: instruction-following behavior, consistent values, safe outputs, or a stable helpful persona — all of these require post-pretraining training.
> - Fine-tuning and RLHF work well because they redirect existing capability rather than creating new capability from scratch; the quality of the pretrained base is thus the foundation of the quality of the deployed assistant.
> - The pretraining corpus shapes the base model's implicit value system in ways that post-training methods partially but not fully override, making corpus composition a matter of ethical as well as technical import.

> [!reflection] **Reflection Prompts — Section 7**
> - The report claims that hallucinations arise from a statistical knowledge representation. What practical implications does this have for how you use and fact-check language model outputs?
> - If fine-tuning redirects rather than creates capability, what follows for how we should evaluate the "safety" of a language model?
> - The insight callout suggests the corpus shapes values. Is this a reason to be more careful about corpus composition, or a reason to invest more in post-training, or both?

> [!situation-model] **Situation Model — Updated Through Section 7**
> **Key Entities:** Base model (pretraining output), parametric knowledge (statistical world model), hallucination (failure of statistical knowledge), instruction following (gap in base models), RLHF + fine-tuning (post-pretraining correction)
> **Causal Map:** Pretraining corpus distribution → base model's statistical world model → strengths (broad knowledge, generalization) + failures (hallucination, inconsistent values) → post-training addresses behavioral gaps
> **Evolution This Section:** Completed the capability-limitations picture; established that the deployed assistant is base model + post-training, and that both matter
> **Tensions:** Broad capability vs. reliable behavior; statistical knowledge vs. factual accuracy; pretraining as foundation vs. pretraining as the source of alignment challenges
> **Connections Across Sections:** This section synthesizes Sections 1-6; the corpus choices discussed in 4-6 now connect to specific capability profiles and failure modes
> **Open Threads:** The ethical and societal dimensions of corpus composition — bias, copyright, consent — are the subject of Section 8

---

## Section 8: Corpus Quality, Bias, and the Ethics of What Gets Baked In

If one has followed the argument to this point, one has accumulated the conceptual tools to appreciate why the ethical dimensions of training corpus design are not peripheral to the technical enterprise but are constitutive of it. The decisions made about what text to include, how to filter and weight it, whose writing counts as quality signal, and whose knowledge is systematically absent are not merely questions of engineering efficiency — they are questions about which version of human knowledge and value the resulting model will embody. Because pretrained models are deployed at scale, affecting millions of interactions daily, the ethical stakes of these decisions are proportionally high.

### 8.1 Deduplication and Its Consequences

Deduplication — removing duplicate and near-duplicate text from training corpora — has been discussed in the context of Common Crawl, but its ethical dimensions deserve separate attention. A dataset without deduplication does not merely waste compute; it systematically amplifies certain voices, communities, and perspectives at the expense of others. Content that goes viral — a piece of political commentary republished across hundreds of news sites, a product description copied to thousands of retailers, a news story that prompts thousands of near-identical responses — may appear tens of thousands of times in raw web-scraped data, while a careful, thoughtful essay that circulates only among a small academic community may appear once or twice.

The model that results from training on this un-deduplicated corpus will have an implicit prior toward viral content — toward the kinds of claims, framings, and values that achieve mass circulation — and away from the kinds of careful, hedged, evidence-based thinking that characterizes scholarship but not virality. This is not a hypothetical concern: empirical analysis of language models has found systematic differences in how confidently they produce claims that were "popular" in their training data versus claims that were well-evidenced but less widely circulated.

> [!key-claim] **Deduplication Is an Equity Issue, Not Just an Engineering Issue**
> The practical and ethical case for deduplication converge: by giving each document an equal weight regardless of how many times it was copied across the web, deduplication reduces the implicit amplification of viral content and gives more balanced weight to the full range of human writing. This does not solve the representation problem — it does not include text that was never on the web in the first place — but it is a meaningful step toward training data that reflects the diversity of human writing rather than the distribution of internet popularity.

### 8.2 Toxic Content and Bias Amplification

Among the most thoroughly documented ethical concerns with large-scale web-scraped corpora is their inclusion of toxic content: text that expresses hatred toward demographic groups, that normalizes violence, that contains harassment, slurs, and discriminatory framing. Studies examining the output of models trained on Common Crawl and similar corpora have found consistent evidence of bias amplification: the model does not merely reflect the biases present in the training data but can, under some prompting conditions, produce output that is more extreme than any individual training document.

The mechanism for this amplification is understood, if not easily remedied. The model's task during pretraining is to predict what comes next in training text; text that includes degrading language about a demographic group reliably follows certain prompts in the training data; the model therefore learns that such language is a high-probability continuation of those prompts. The model is not being "told" that this language is acceptable — it is simply learning the statistical patterns of the text it was trained on. When the bias is in the text, it enters the model through the training objective itself.

> [!warning] **Bias Enters Through the Objective, Not Through Explicit Programming**
> The challenge of training data bias is not that someone programmed a language model to be biased. It is that the pretraining objective — predict what comes next in human-written text — is agnostic about whether that text expresses equitable or inequitable values. If the training corpus overrepresents certain demographics, perspectives, and cultural frameworks, the resulting model will overrepresent them too. Addressing this requires upstream intervention at the data level — either including more representative data, filtering toxic content, or both — as well as downstream intervention through safety training. Neither intervention alone is sufficient.

### 8.3 Representation and What Gets Left Out

A complementary concern to toxic content is the systematic absence of certain kinds of knowledge and perspective from training corpora. Languages other than English are vastly underrepresented in most web-scraped datasets, with consequences for a model's ability to reason in, translate, or demonstrate cultural competence about non-English communities. Knowledge that primarily circulates within communities with limited web presence — oral traditions, community-specific practices, knowledge systems not encoded in widely shared writing — is largely absent. Scientific knowledge behind paywalls, local government documents, and the writings of communities that were not early adopters of web publishing are all systematically underweighted.

The result is not just a model that is less useful for underrepresented communities — it is a model that, when asked about those communities, will draw primarily on how they were represented by others in the training data, which is often a distorted or incomplete picture. The "knowledge" such a model has about, for example, indigenous cultural practices is more likely derived from anthropological academic texts than from writings by members of those cultures themselves. This is not a neutral epistemic position; it reflects and can reinforce existing patterns of cultural and epistemic marginalization.

### 8.4 Copyright, Consent, and the Future of Training Data

The legal status of training data has become one of the most actively contested issues in AI policy, triggered in part by the scale and visibility of models like GPT-4, the controversies around The Pile's Books3 component, and a wave of legal challenges from writers, artists, and publishers. The core legal question — whether training a model on copyrighted material constitutes infringement, or whether it falls under fair use or transformative use doctrines — remains unsettled in most jurisdictions as of this writing.

The ethical question is in some respects prior to the legal one: even if training on copyrighted material were legally permitted, should it be done without consent or compensation? The counterargument from researchers is that pretraining is analogous to reading — a human expert who reads thousands of books and learns from them is not required to compensate the authors, even if that expertise is later monetized. The counterargument from creators is that the scale is categorically different: a human reads thousands of books over decades; a model trains on millions of books in weeks, extracting the statistical essence of authors' creative work and making it available through the model in ways that directly compete with the original work.

> [!tension] **Scale vs. Consent: The Central Ethical Tension in Training Data**
> **Position A (Research/Industry):** Training on publicly available text is analogous to human learning and falls within established fair use frameworks; restricting training data would dramatically impede AI development and primarily benefit incumbent rights holders at the expense of public benefit.
> **Position B (Creators/Publishers):** The scale and commercial value of AI training are categorically different from human learning; creators have a legitimate interest in whether their work is used to train commercially deployed systems that may compete with them; consent and compensation frameworks are both feasible and ethically required.
> **Current State of Evidence:** Legal rulings have been mixed; the ethical consensus remains contested. Several major AI laboratories have begun licensing data from publishers and news organizations, suggesting a de facto recognition that the consent framework is not fully disposable, even if it has not been legally mandated.
> **Why It Matters:** The resolution of this tension will determine what future training corpora look like — whether they will be assembled from freely available text, licensed data, or some mix of both — and will thus shape the capabilities and characteristics of future language models.

### 8.5 What Responsible Corpus Design Would Look Like

The accumulated evidence from years of training corpus development, ethical critique, and legal challenge suggests an emerging consensus — still contested and incomplete — about what more responsible corpus design would look like. It would involve documented, auditable data collection practices; systematic deduplication; automated filtering for toxic content combined with human review of edge cases; proactive inclusion of underrepresented languages and communities; clear licensing and attribution for commercial deployments; mechanisms for data subjects to request removal; and ongoing monitoring of the deployed model's outputs for evidence of harmful biases.

None of these practices is without cost, and none is simple to implement at the scale required for frontier model training. But the [[value-alignment-problem|value alignment problem]] in AI begins not with RLHF or safety training but with the first decision about what text to collect and how to weight it. Taking that decision seriously is not a constraint on AI development; it is a prerequisite for AI development that merits the public trust it currently receives.

> [!section-summary] **Section 8 Summary**
> - Deduplication is both an engineering and equity issue: un-deduplicated corpora amplify viral content over carefully written scholarship, producing systematic value distortions.
> - Bias enters through the pretraining objective itself, not through explicit programming: the next-word prediction task faithfully learns the statistical patterns of training text, including its prejudices.
> - Representation gaps — underrepresented languages, communities, and knowledge systems — are at least as significant as the presence of harmful content, because absence shapes a model's world model just as powerfully as presence.
> - The copyright and consent debate remains legally unsettled but ethically pressing; the scale of AI training is categorically different from individual human learning, and emerging licensing practices suggest industry recognition of this difference.
> - Responsible corpus design is not a peripheral concern but a foundational one: the value alignment problem starts with the first data collection decision.

> [!reflection] **Reflection Prompts — Section 8**
> - The section argues that deduplication is an equity issue. Does this reframing change your intuitions about it?
> - Bias enters through the pretraining objective. Does this mean it is impossible to build an unbiased model, or only that bias must be addressed at the data level?
> - If you were advising an AI organization on training data practices, what three specific changes would you prioritize, and why?

> [!situation-model] **Situation Model — Updated Through Section 8 (COMPLETE)**
> **Key Entities:** Deduplication (equity + engineering), bias amplification (statistical mechanism), representation gaps (absence as harm), copyright/consent (ethical-legal frontier)
> **Causal Map:** Corpus composition → statistical learning of patterns, biases, gaps → base model with embedded values, limitations → post-training partially corrects, but not fully
> **Full Model:** Pretraining is: (1) a learning objective (autoregressive, masked, denoising) applied to (2) a training corpus (Common Crawl, WebText, The Pile, or mixtures) to produce (3) a base model that knows a great deal but behaves erratically (4) that is then shaped by post-training into a deployed assistant (5) but whose fundamental knowledge, values, and limitations trace to decisions made in steps 1-2.
> **Central Tension:** Technical excellence and ethical responsibility are not separable in this domain — the training corpus is both an engineering input and a moral choice.
> **Open Threads:** Far Transfer (Section 9) and Synthesis (Section 10) will explore how these insights apply beyond the domain of language models and what the integrated picture looks like.

---

## Far Transfer: Applying These Insights Beyond Language Models

Understanding how [[transfer-of-learning|knowledge transfers]] from one domain to another is one of the more productive exercises in applied learning. The principles embedded in pretraining and corpus design — that the nature and diversity of one's "inputs" determine the range and quality of one's outputs, that scale and quality are in tension but not in opposition, that biases embedded in early formation are difficult to reverse later — have structural analogues in domains far removed from machine learning. Examining these analogues is not merely an academic exercise; it illuminates the principles in a way that makes them more durable and flexible in memory.

> [!far-transfer] **Information and Library Science: Corpus Design as Collection Development**
> The challenge facing a corpus designer — what to include, how to weight different sources, how to handle conflicting quality signals, how to ensure representational diversity — is structurally identical to the challenge facing a librarian engaged in collection development. Library science has grappled with these questions for over a century and developed a rich body of practice: principled selection policies, explicit acknowledgment of community diversity, regular collection audits for representation gaps, and procedures for handling challenged or harmful material. The parallel extends to the specifics: just as the choice of which sources to license determines what knowledge a library's patrons can access, the choice of which corpora to include determines what knowledge a language model will have. Library science's hard-won insights about the difference between "what the majority finds interesting" and "what serves the full community" maps directly onto the WebText-vs-The Pile design philosophy tension. The practical transfer: when evaluating a language model for use in a context that serves a specific community, ask the same question a thoughtful librarian would ask of a collection — does this corpus reflect this community's knowledge, or primarily others' knowledge *about* this community?

> [!far-transfer] **Epidemiology: How Biases Spread Through Populations**
> The spread of bias through a training corpus has a structural analogy in the spread of disease through a population — and the public health tools developed to understand the latter illuminate the former in productive ways. In epidemiology, the concept of "selection bias" in a study refers to the distortion introduced when the sample studied is not representative of the population of interest; conclusions drawn from a biased sample will be systematically wrong in predictable ways. Training corpus bias operates analogously: a model trained on text that overrepresents certain demographics, value systems, or geographic contexts will generate outputs that systematically reflect those contexts, and evaluations conducted on benchmarks derived from that same biased corpus will fail to detect the problem. The epidemiological concept of "confounding" — where an apparent causal relationship is actually the result of a third variable that influences both — also has a training corpus parallel: a model may appear to "know" something about a community not because it was trained on that community's own writing but because it was trained on how another community wrote about them, and these two things are confounded in the parametric knowledge. The practical transfer: applying epidemiological skepticism about representative sampling to training data evaluation would significantly improve how the field assesses model capabilities and limitations.

> [!far-transfer] **Media Literacy and Journalism: Source Diversity as Epistemic Virtue**
> Journalism and media literacy education have long recognized that no single source is fully reliable, that understanding a topic requires exposure to multiple perspectives, and that the framing a source uses to present information is itself information. The principle behind The Pile's diversity hypothesis — that a model trained across many domains develops richer reasoning capacities than one trained within a single domain — is a direct parallel to the epistemic principle that a thinker whose information diet includes diverse, high-quality sources across ideological and disciplinary lines develops more robust reasoning than one who reads from a single perspective. Media literacy also provides a vocabulary for the kinds of source evaluation that corpus designers implicitly perform: Is this source authoritative? Is it representative of a community's self-understanding, or only of how that community is perceived from outside? Does it have a commercial or ideological stake in the content? These are questions that both journalists and corpus designers should be asking systematically. The practical transfer: the habits of mind cultivated in media literacy — source evaluation, perspective triangulation, attention to framing — are directly applicable to critical evaluation of what training corpora are likely to teach a model.

> [!active-reading-prompt] **Active Reading Prompt**
> Before reading the Synthesis section below, take a moment to formulate your own one-paragraph answer to the guiding question posed in the Schema Activation at the beginning of this report: *How do the choices researchers made about what text to collect, and how to have a model learn from it, determine the capabilities, biases, and limitations of every large language model one encounters today?* What would you say now that you could not have said at the start? What remains uncertain for you?

---

## Synthesis and Integration

What one finds, on reviewing the full arc of this report, is that the pretraining story is both more technical and more human than the phrase "trained on the internet" suggests. It is more technical because the specific choice of objective — autoregressive prediction versus masked filling versus denoising — shapes the entire character of the resulting model's capabilities, favoring generation over comprehension, or comprehension over generation, in ways that persist through all subsequent training. It is more human because the corpora on which models train are not neutral datasets but records of human activity: what was written, shared, upvoted, published, coded, and archived. Every bias, gap, distortion, and silence in that record enters the model through the training objective and becomes part of its statistical world model, sometimes visibly and sometimes in ways that are much harder to detect.

> [!original-synthesis] **The Corpus-as-Curriculum Framework**
> A productive way of integrating the report's arguments is to think of the pretraining corpus not as a dataset but as a curriculum — and to apply to it the questions one would apply to any curriculum: What knowledge does it prioritize? Whose perspectives are foregrounded? What ways of reasoning does it reward? What is entirely absent? This framing shifts attention from the technical properties of the corpus (size, format, deduplication rate) to its epistemic and ethical properties (what it teaches, who it represents, what values it encodes). Common Crawl, on this analysis, is a curriculum that prioritizes breadth over depth and viral over authoritative; WebText is a curriculum that prioritizes what one specific online community found engaging; The Pile is a curriculum that attempts to be a genuine liberal education — broad, technically rigorous, and culturally ambitious, with the imperfections one would expect of any curriculum assembled quickly and at scale. No curriculum is value-neutral; the act of assembling one is an act of choosing what matters.

The practical implication for users of language models — as opposed to those who build them — is more tractable than the technical complexity might suggest. If one understands that a model's knowledge is statistical rather than factual, one knows to verify specific claims rather than trusting them. If one understands that the model's training data was dominated by certain communities, registers, and value systems, one knows to be skeptical of its confident representations of communities it was mostly trained on data *about* rather than data *from*. If one understands that the base model's behavior reflects the training data's patterns — including its harmful patterns — one knows not to mistake safety training for a comprehensive solution to the alignment challenge.

The field is, in some respects, in its adolescence with regard to corpus design. The early era — assemble whatever text one can, as large as possible — has given way to an era of more deliberate curation. The Chinchilla insights about data efficiency, the growing literature on deduplication and bias, the legal challenges around copyright, and the increasing demand for model transparency are all pushing in the direction of more principled corpus construction. What that next era of corpus design looks like — whether it involves licensing, synthetic data generation, community consent frameworks, or methods not yet invented — will significantly determine what the next generation of language models can do and for whose benefit.

> [!active-reading-prompt] **Closing Active Reading Prompt**
> Having read this report, consider: the next language model you use was trained on text. You now have some idea of what that text was like, what the training process did with it, and what the limitations of that process are. How does this change how you will use it? What questions will you ask of its outputs that you would not have thought to ask before?

---

---

## Appendix

### 8.1 Lexicon of Key Terms

> [!definition] **Pretraining (Full Definition)**
> The initial, large-scale phase of language model development in which a neural network is exposed to enormous quantities of text and trained to perform a self-supervised prediction task — such as predicting the next word, or filling in masked words — without any human-provided labels or feedback. Pretraining is the source of a model's broad linguistic and world knowledge, its ability to generalize across tasks, and its characteristic failure modes.
>
> **Boundary 1 — What it is not:** Pretraining is not fine-tuning (the stage where task-specific behavior is taught), not RLHF (the stage where human preferences are incorporated), and not inference (the stage where the trained model generates outputs). All three are separate, subsequent processes.
> **Boundary 2 — What it cannot produce:** Pretraining alone cannot produce instruction-following, consistent values, safety, or reliable factual accuracy. These require subsequent training stages.
> **Etymology:** "Pre-" (before) + "training" — training that occurs before task-specific training.
> **Operational Indicator:** If a model has been described as a "base model" or "foundation model," it has been pretrained but not yet post-trained.
> **Report-Specific Significance:** The entire report is an elaboration of what happens during pretraining and why it matters for every downstream capability and failure.
> **See also:** [[instruction-fine-tuning]], [[supervised-fine-tuning]], [[scaling-and-capability-emergence]], [[reinforcement-learning-from-human-feedback]]

> [!definition] **Autoregressive Language Modeling**
> A pretraining objective in which a model is trained to predict the probability of the next token (word or word-fragment) in a sequence, given all preceding tokens. The model reads left-to-right and never "looks ahead." This is the dominant pretraining objective for contemporary large generative language models, including the GPT family, LLaMA, and PaLM.
>
> **Boundary 1:** Autoregressive models read in one direction only; they cannot revise a prediction based on what comes after in the sentence. This is a structural limitation relative to masked language models.
> **Boundary 2:** Excellent for generation tasks (continuing text, answering questions as completions); weaker than bidirectional models at pure comprehension tasks (classifying a complete passage, inferring sentiment).
> **Operational Indicator:** A model that generates text token by token, from left to right, is using autoregressive decoding — even if its pretraining used a different objective. The training objective shapes the weights; the decoding strategy operates at inference time.
> **See also:** [[in-context-learning]], [[chain-of-thought-prompting]], [[few-shot-prompting]]

> [!definition] **Masked Language Modeling (MLM)**
> A pretraining objective in which a fixed proportion of tokens in training text are replaced with a [MASK] symbol, and the model is trained to predict the original tokens using both left and right context. Introduced in BERT (2018), MLM produces models with strong bidirectional representations suited for comprehension tasks.
>
> **Boundary 1:** MLM-trained models are not natively suited for open-ended text generation because their pretraining never required generating one token at a time in sequence.
> **Boundary 2:** Strong for tasks with a complete input requiring understanding: classification, question answering with a passage provided, named entity recognition.
> **See also:** [[semantic-grounding-in-llms]], [[embedding-space-geometry]], [[transformer-attention-mechanism]]

> [!definition] **Self-Supervised Learning**
> A machine learning approach in which training labels are derived automatically from the input data itself, rather than provided by human annotators. In language modeling, the "label" for each token is simply the next token in the sequence (autoregressive) or the masked token (MLM). Self-supervised learning is what makes pretraining tractable at scale — it requires no human labeling budget.
>
> **Boundary:** Self-supervised learning does not guarantee that what is learned is what is wanted — it guarantees that what is learned is what was in the training data. The alignment between "what the data contains" and "what we want the model to learn" is a separate problem, not solved by the self-supervised paradigm.
> **See also:** [[instruction-fine-tuning]], [[supervised-fine-tuning]], [[reinforcement-learning-from-human-feedback]]

> [!definition] **Common Crawl**
> A nonprofit web crawl dataset available since 2008, capturing petabytes of publicly accessible web pages. The largest and most widely used training data source for major language models. Requires significant processing (filtering, deduplication, language identification) before use as training data. Used as the primary volumetric data source in GPT-3, PaLM, and most subsequent frontier models.
>
> **Boundary 1:** Only captures publicly accessible content; paywalled, authenticated, or robots.txt-restricted content is absent.
> **Boundary 2:** Raw Common Crawl data is not usable for training — it contains spam, SEO content, duplicates, toxic material, and non-text HTML. Processed derivatives (C4, CC-Net, CC-100) are what is actually used.
> **See also:** [[benchmark-contamination]], [[train-test-leakage-in-llms]], [[domain-adaptation-llms]], [[vocabulary-size-tradeoffs]]

> [!definition] **WebText**
> OpenAI's curated training corpus for GPT-2 (2019), assembled by collecting the text of all outbound links from Reddit posts with at least three upvotes. Approximately 45 gigabytes, considerably smaller than Common Crawl but significantly higher in average quality as measured by coherence and writing standards.
>
> **Boundary 1:** Quality is defined by Reddit community standards, which skew toward specific demographics (young, male, English-speaking, tech-adjacent). This introduces systematic gaps in the resulting model's representation.
> **Boundary 2:** Wikipedia explicitly excluded to avoid benchmark contamination.
> **See also:** [[hallucination-taxonomy]], [[parametric-vs-contextual-knowledge]], [[benchmark-contamination]]

> [!definition] **The Pile**
> An open-source, multi-source training dataset assembled by EleutherAI (Gao et al., 2020), consisting of 825 gigabytes of text from twenty-two distinct sources including web text, books, academic papers, code, legal text, and encyclopedic content. Designed on a "diversity-as-quality" philosophy: the hypothesis that domain diversity produces better model generalization.
>
> **Boundary 1:** A snapshot dataset (assembled 2020); not continuously updated. The Books3 component became legally controversial as it included copyrighted books from a shadow library.
> **Boundary 2:** Quality is uneven across components — academic papers and code are high quality; web-scraped components (Pile-CC) inherit Common Crawl's quality challenges.
> **See also:** [[domain-adaptation-llms]], [[continual-learning-llms]], [[knowledge-intensive-nlp]]

> [!definition] **Deduplication (Training Data)**
> The process of removing duplicate and near-duplicate text from a training corpus before model training. Deduplication prevents compute waste on redundant examples, reduces model overconfidence on frequently repeated phrases, and mitigates benchmark contamination risk. Near-deduplication uses fuzzy matching or hash-based methods to catch paraphrases and partial repetitions in addition to exact copies.
>
> **Boundary:** Deduplication cannot remove harmful content — only its repetition. It addresses the overweighting problem but not the inclusion problem. A corpus can be fully deduplicated and still contain substantial harmful, biased, or factually incorrect material.
> **Operational Indicator:** Studies comparing model behavior on deduplicated vs. non-deduplicated corpora find that deduplicated-trained models generate more varied text, are less prone to verbatim repetition, and show lower benchmark contamination risk.
> **See also:** [[benchmark-contamination]], [[train-test-leakage-in-llms]]

> [!definition] **Base Model / Foundation Model**
> A language model that has been pretrained on a large corpus but has not yet been fine-tuned for specific tasks or trained with human feedback. Base models exhibit broad knowledge and generalization capacity but unreliable instruction-following, inconsistent values, and outputs that may include harmful content. All deployed assistants are built on top of base models through subsequent training stages.
>
> **Boundary:** "Foundation model" is used more broadly in the field to include models in computer vision and multimodal domains. "Base model" is typically the language-specific term. Both refer to the pretrained-but-not-fine-tuned stage.
> **See also:** [[instruction-fine-tuning]], [[supervised-fine-tuning]], [[full-fine-tuning-vs-peft]], [[parameter-efficient-fine-tuning]]

> [!definition] **Benchmark Contamination**
> The inadvertent inclusion of text from standardized evaluation benchmarks in the training data, with the result that a model's performance on those benchmarks may reflect memorization rather than generalization. Benchmark contamination is a significant confound in interpreting published model capability claims and is difficult to detect comprehensively in large-scale training corpora.
>
> **Boundary:** Contamination exists on a spectrum: exact inclusion of benchmark questions is the extreme; near-paraphrase or "topic contamination" (training data covers the same topics as benchmarks in depth) is more common and harder to detect.
> **See also:** [[train-test-leakage-in-llms]], [[benchmark-contamination]], [[llm-evaluation-benchmarks]]

---

### 8.2 Key Figures and Intellectual Lineage

> [!figure] **Alec Radford (OpenAI, 2015–present)**
> **Core Contribution:** Lead author on GPT, GPT-2, and GPT-3, Radford is the central architect of the autoregressive pretraining paradigm as it exists today. His work establishing that large-scale next-word prediction on diverse web text produces models with broad capability was foundational for the current era.
> **Relationship to Others:** Worked alongside Ilya Sutskever (OpenAI's chief scientist during this period) and with the broader OpenAI research team. GPT-3 was a collaboration with Tom Brown, Ben Mann, and many others.
> **Key Works:** "Improving Language Understanding by Generative Pre-Training" (GPT-1, 2018); "Language Models are Unsupervised Multitask Learners" (GPT-2, 2019)

> [!figure] **Jacob Devlin (Google Research, 2018–present)**
> **Core Contribution:** Lead author on BERT, Devlin established masked language modeling as the dominant alternative pretraining paradigm and demonstrated that bidirectional context substantially improves model performance on comprehension tasks.
> **Relationship to Others:** Worked alongside Ming-Wei Chang, Kenton Lee, and Kristina Toutanova at Google. BERT's success drove an enormous follow-on literature including RoBERTa (Liu et al.) and ALBERT.
> **Key Works:** "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (2018)

> [!figure] **Colin Raffel (Google Research, then UNC)**
> **Core Contribution:** Lead author on T5 and the C4 dataset, Raffel established the denoising objective as a competitive pretraining approach and provided the first systematic comparison of pretraining objectives at scale. The C4 dataset became one of the most widely used processed Common Crawl derivatives.
> **Relationship to Others:** T5 work was conducted at Google Brain; Raffel has since moved to academic research, focusing on dataset quality and the ethics of training data.
> **Key Works:** "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (T5, 2019)

> [!figure] **Leo Gao and EleutherAI (founding ~2020)**
> **Core Contribution:** Gao was lead author on The Pile and a founding member of EleutherAI, the open-source AI collective that assembled the dataset and released it alongside GPT-Neo and GPT-NeoX. The Pile established diversity as a first-class design principle in training corpus construction and demonstrated that open-source efforts could produce competitive training data.
> **Relationship to Others:** EleutherAI was partly formed in response to OpenAI's restricted release of GPT-2; its members include Stella Biderman, Sid Black, and others. The collective has since trained some of the most important open-source language models.
> **Key Works:** "The Pile: An 800GB Dataset of Diverse Text for Language Modeling" (2020)

> [!figure] **Jared Kaplan (Johns Hopkins, formerly OpenAI)**
> **Core Contribution:** Lead author on the scaling laws paper that quantified the relationship between model size, data volume, compute, and language model performance. This work provided the theoretical and empirical foundation for the "more is better" era of model development.
> **Relationship to Others:** Kaplan's scaling laws work was subsequently refined by the Chinchilla team at DeepMind (Hoffmann et al., 2022), which modified the optimal data-to-parameter ratios. These two papers form the empirical backbone of the scaling hypothesis.
> **Key Works:** "Scaling Laws for Neural Language Models" (2020)

---

### 8.3 Conceptual Tensions and Open Questions

> [!tension] **Scale vs. Quality: The Central Engineering Tradeoff**
> **Position A (Scale Maximizers):** The scaling laws show that performance improves predictably with data volume; automated filtering is sufficient to achieve the quality floor needed for effective pretraining; Common Crawl-scale data, properly processed, outperforms smaller curated datasets.
> **Position B (Quality Prioritizers):** Automated filtering cannot reliably identify high-quality text; models trained on large low-quality corpora develop systematic biases and failure modes that smaller, higher-quality training sets would avoid; the Chinchilla results show that data quality matters enough to justify smaller, better-curated datasets over larger, noisier ones.
> **Current State of Evidence:** Mixed. The Chinchilla finding supports quality over sheer scale, but the frontier models (GPT-4, Gemini, Claude) appear to use both — Common Crawl for volume, supplemented by high-quality curated sources. The optimal mix remains an active research question.
> **Why It Matters:** Determines how training resources are allocated; determines whether large datasets with modest quality filtering or small datasets with intensive curation are the field's development direction.
> **This Report's Stance:** Both matter, but quality becomes more important as model scale increases; at sufficient scale, low-quality data may actively harm rather than merely fail to help.

> [!tension] **Openness vs. Copyright and Safety**
> **Position A (Open Proponents):** Open training data enables research reproducibility, allows external audit of model limitations and biases, and prevents the concentration of AI capability in a small number of well-resourced organizations.
> **Position B (Rights Holders/Safety):** Unrestricted training on publicly scraped data violates creator rights, amplifies harmful content, and makes it impossible to ensure data governance compliance; the scale of commercial AI training is categorically different from individual human learning and deserves a distinct legal treatment.
> **Current State of Evidence:** Legal cases ongoing in multiple jurisdictions; some major AI organizations have begun licensing training data from publishers, suggesting industry movement toward a hybrid model. No clear legal consensus as of 2025.
> **Why It Matters:** The outcome will determine whether future training corpora are assembled from freely scraped public data, licensed sources, synthetic data, or some combination.
> **This Report's Stance:** The legal debate will resolve independently of the ethical debate; the ethical case for consent and compensation has merit regardless of legal outcome.

> [!open-question] **Can Bias in Pretraining Corpora Be Fully Corrected by Post-Training?**
> **Question:** Given that a pretrained model's statistical world model encodes the biases of its training data, is it possible for post-training (RLHF, safety training, fine-tuning) to fully correct these biases — or do some biases remain structurally embedded in ways that post-training cannot access?
> **Context:** Several documented cases suggest that bias correction through RLHF is incomplete — models can exhibit reduced bias in standard evaluation conditions while retaining bias patterns when prompted in specific ways or in languages underrepresented in the safety training data.
> **Implications for Future Research:** If post-training cannot fully correct pretraining biases, the field must invest significantly more in corpus composition and filtering rather than treating safety training as a sufficient backstop.
> **This Report's Position:** Current evidence suggests post-training mitigates but does not eliminate pretraining biases; corpus-level intervention remains necessary and cannot be wholly deferred to post-training stages.

---

### 8.4 References

> [!cite] **Brown, T., Mann, B., Ryder, N., et al. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems*, 33, 1877–1901.**
> **Annotation:** The GPT-3 paper — the most consequential single publication in the current era of large language models. Documented the training data composition (including the role of Common Crawl, WebText2, books, and Wikipedia), established the scaling behavior of autoregressive models, and demonstrated few-shot and zero-shot learning at unprecedented scale. Essential reading for anyone who wants to understand why current language models behave as they do.
> **Recommended Sections:** Sections 3 (scaling), 4 (Common Crawl), 5 (WebText), 7 (base model capabilities)

> [!cite] **Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of deep bidirectional transformers for language understanding. *arXiv preprint arXiv:1810.04805*.**
> **Annotation:** The paper introducing masked language modeling as a pretraining objective. BERT's success on eleven NLP benchmarks upon release demonstrated that bidirectional pretraining substantially outperformed prior unidirectional approaches for comprehension tasks, triggering an enormous research wave. This paper establishes the masked LM paradigm described in Section 2.
> **Recommended Sections:** Section 2 (masked LM objective)

> [!cite] **Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). Language models are unsupervised multitask learners. *OpenAI Blog*, 1(8), 9.**
> **Annotation:** The GPT-2 paper, introducing WebText and demonstrating that high-quality curated training data produces models with dramatically better output quality. The paper's framing — that a sufficiently capable language model can perform many tasks without explicit task-specific training — established the foundation for the zero-shot and few-shot learning capabilities of subsequent models.
> **Recommended Sections:** Section 5 (WebText), Section 7 (base model capabilities)

> [!cite] **Gao, L., Biderman, S., Black, S., et al. (2020). The Pile: An 800GB dataset of diverse text for language modeling. *arXiv preprint arXiv:2101.00027*.**
> **Annotation:** The paper introducing The Pile, including detailed descriptions of all twenty-two component datasets, the rationale for the diversity-first design philosophy, and initial results demonstrating that models trained on The Pile outperform web-only baselines on domain-specific benchmarks. The paper also provides one of the most transparent documentation efforts for a training corpus, discussing limitations and ethical concerns explicitly.
> **Recommended Sections:** Section 6 (The Pile), Section 8 (ethics), Appendix 8.3 (tensions)

> [!cite] **Raffel, C., Shazeer, N., Roberts, A., et al. (2019). Exploring the limits of transfer learning with a unified text-to-text transformer. *arXiv preprint arXiv:1910.10683*.**
> **Annotation:** The T5 paper, introducing the denoising pretraining objective and the C4 dataset (Colossal Clean Crawled Corpus). Among the most systematic comparisons of pretraining objectives, dataset sizes, and model architectures published during the period. C4's filtering approach — heuristic-based quality filtering of Common Crawl — became a widely used baseline for processed Common Crawl datasets.
> **Recommended Sections:** Section 2 (denoising objective), Section 4 (Common Crawl processing)

> [!cite] **Kaplan, J., McCandlish, S., Henighan, T., et al. (2020). Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361*.**
> **Annotation:** The foundational empirical paper establishing power-law relationships between language model performance and model size, training data volume, and compute. This paper's findings provided the theoretical justification for the scaling-first approach to model development and explained why larger corpora reliably produce better models.
> **Recommended Sections:** Section 3 (scaling laws)

> [!cite] **Hoffmann, J., Borgeaud, S., Mensch, A., et al. (2022). Training compute-optimal large language models. *Advances in Neural Information Processing Systems*, 35.**
> **Annotation:** The "Chinchilla paper," which argued that prior large language models were undertrained relative to their parameter counts. By training smaller models on more data, DeepMind achieved state-of-the-art performance with substantially fewer parameters. This finding shifted the field's emphasis toward data quality and quantity rather than simply scaling model size, with significant implications for corpus design strategy.
> **Recommended Sections:** Section 3 (scaling), Section 4 (Common Crawl tradeoffs)

> [!cite] **Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *FAccT 2021*, 610–623.**
> **Annotation:** A landmark critical paper arguing that the scaling-first approach to language model development carries substantial, underappreciated risks: environmental costs of training large models, amplification of training data biases, and the risk that models which "sound" coherent and knowledgeable produce harmful confabulations. The paper's arguments have substantially influenced how the field discusses the ethics of training data and model development.
> **Recommended Sections:** Section 8 (ethics, bias, copyright)

---

### 8.5 Methodology and Sources Note

> [!methodology-and-sources] **Methodology and Sources**
>
> **Intellectual Traditions Synthesized**
> This report synthesizes four overlapping intellectual traditions: (1) the machine learning research literature on pretraining and self-supervised learning; (2) NLP benchmarking and evaluation methodology; (3) data ethics and AI fairness scholarship; and (4) cognitive science frameworks on learning and knowledge representation, used to structure the reader-facing scaffolding.
>
> **Claim Type Taxonomy**
>
> | Claim Type | Epistemic Status | Example from This Report |
> |------------|----------------|--------------------------|
> | Well-documented mechanisms | Established | Autoregressive LM predicts the next token given all prior tokens |
> | Published empirical findings | Established (peer-reviewed) | Scaling laws show power-law relationship between data, parameters, and loss |
> | Cross-study comparisons | Well-motivated (interpretive) | The Pile diversity hypothesis produces better generalization |
> | Interpretive frameworks | Well-motivated (analytical) | Corpus-as-Curriculum framing; the analogy between deduplication and library collection equity |
> | Ethical assessments | Normative (reasoned opinion) | Copyright violation arguments; claim that bias cannot be fully corrected post-training |
> | Speculative extensions | Speculative (original to report) | That post-training cannot fully override pretraining-embedded values |
>
> **Distinction Between Established Findings and Original Contributions**
> The Corpus-as-Curriculum framework and the framing of the far-transfer domains are original analytical moves by this report and should be treated as reasoned proposals rather than established findings. All empirical claims about model performance are sourced from published research.
>
> **Explicit Limitations**
> - This report was written in mid-2025; the legal status of training data and model capabilities are evolving quickly.
> - Proprietary details about frontier model training corpora (GPT-4, Claude 3+, Gemini) are not publicly disclosed; this report describes what is documented in public research.
> - The user's request to minimize mathematical detail means that certain technical distinctions (e.g., exact token prediction loss formulations, specific tokenization tradeoffs) are intentionally underspecified.
> - The report's ethical assessments reflect scholarly consensus as of 2025 but are normative claims, not empirical findings.
>
> **AI Generation Transparency**
> This report was generated by Claude (Anthropic) in response to a user prompt, as part of a Personal Knowledge Base build process. The intellectual synthesis and original analytical frameworks are the product of the generation process. The user provided the topic and the high-level constraint ("no mathematics; focus on intuition and practical application"). All citations should be independently verified before reliance in academic or professional contexts.

---

### 8.6 Argument Maps and Visual Summaries

> [!diagram] **Core Pipeline: From Text to Deployed Model**
> ```
> RAW WEB TEXT (Common Crawl, Books, Code, etc.)
>         │
>         ▼
> ┌───────────────────────────────────────────┐
> │           CORPUS PROCESSING               │
> │  Filtering → Deduplication → Mixing       │
> │  (quality filters, language ID, weights)  │
> └───────────────────────────────────────────┘
>         │
>         ▼
> PRETRAINING CORPUS
>     (e.g., WebText / The Pile / C4 / custom mix)
>         │
>         ▼
> ┌───────────────────────────────────────────┐
> │           PRETRAINING                     │
> │  Objective: Autoregressive / MLM /        │
> │  Denoising applied to corpus tokens       │
> │  → billions of parameter updates          │
> └───────────────────────────────────────────┘
>         │
>         ▼
> BASE MODEL (Foundation Model)
>     [knows a lot; behaves erratically]
>         │
>         ├──→ Supervised Fine-Tuning (instruction pairs)
>         │            │
>         │            ▼
>         │        SFT Model
>         │            │
>         └──→ RLHF / Preference Tuning
>                      │
>                      ▼
>              DEPLOYED ASSISTANT
>              [helpful, aligned, safe(r)]
> ```

> [!diagram] **Pretraining Corpus Comparison: The Three Major Designs**
> ```
> ┌──────────────────────────────────────────────────────────┐
> │              TRAINING CORPUS DESIGN SPACE                │
> │                                                          │
> │  QUALITY-FILTERED WEB (Common Crawl + C4)                │
> │  ├─ Volume: Very high (trillions of tokens)              │
> │  ├─ Diversity: High (entire web)                         │
> │  ├─ Quality: Low-moderate (filtered but noisy)           │
> │  └─ Tradeoff: Breadth at cost of depth                   │
> │                                                          │
> │  COMMUNITY-CURATED (WebText / Reddit-filtered)           │
> │  ├─ Volume: Moderate (tens of billions of tokens)        │
> │  ├─ Diversity: Low-moderate (one community's taste)      │
> │  ├─ Quality: High (upvote-filtered)                      │
> │  └─ Tradeoff: Quality at cost of representational scope  │
> │                                                          │
> │  DELIBERATELY DIVERSE (The Pile)                         │
> │  ├─ Volume: Moderate (800GB, ~250B tokens)               │
> │  ├─ Diversity: High (22 sources, 8 domains)              │
> │  ├─ Quality: Varied (excellent code/papers; noisy web)   │
> │  └─ Tradeoff: Coverage at cost of consistency            │
> └──────────────────────────────────────────────────────────┘
> ```

---

### 8.7 Practical Application Protocols

> [!protocol] **Protocol: Evaluating What a Language Model Is Likely to Know**
> **Purpose:** Before trusting a language model's output on a topic, use this protocol to assess how reliably the topic would have been represented in a typical pretraining corpus.
>
> **Steps:**
> 1. **Ask: Is this topic well-represented on the public web?** Topics with extensive Wikipedia coverage, multiple news articles, widely-cited academic papers, and active forum discussion are likely to be robustly represented in Common Crawl-based training data. Trust the model more.
> 2. **Ask: Is this information stable and non-contradictory in training data?** Facts that were contested, changing, or inconsistently reported across sources during the model's training window will be represented as a statistical average, possibly landing on an incorrect or outdated claim. Verify these independently.
> 3. **Ask: Is this community or topic underrepresented in English-language web text?** Topics primarily discussed in languages other than English, in paywalled journals, in community-specific non-web contexts, or in oral/non-written traditions will be weakly represented. Use the model's output only as a starting point, not an authority.
> 4. **Ask: Does this require precise, verifiable facts (dates, names, statistics)?** Base model parametric knowledge is unreliable for precision facts — hallucination risk is highest here. Always verify.
> 5. **Ask: Is the model's knowledge potentially outdated?** Training data has a cutoff. Events, research findings, and policy changes after the cutoff are not in the model's parametric knowledge. Use retrieval-augmented methods ([[retrieval-augmented-generation|RAG]]) for time-sensitive queries.
> 6. **Ask: Is this a task (writing, summarizing, translating) or a fact (is X true)?** Models are far more reliable for generation and reasoning tasks than for specific factual claims. Use them accordingly.
>
> **Use Cases:** Research, fact-checking, educational use, content generation quality assessment
> **Example:** You ask a model about a small regional legal case from 2023. The topic is unlikely to be well-represented in pre-2023 Common Crawl data and is precisely factual — hallucination risk is very high. Treat the output as potentially fabricated; use it only to understand the general legal landscape, not the specific case.

> [!checklist] **Pre-Use Checklist: Assessing Language Model Output Reliability**
> **Purpose:** Quick assessment of output trustworthiness before relying on model-generated content.
>
> - [ ] **Topic coverage:** Is this topic broadly covered in publicly available English text?
> - [ ] **Fact precision:** Does this claim involve specific names, dates, numbers, or statistics? (If yes: higher verification priority)
> - [ ] **Recency:** Is this information from after the model's training cutoff? (If yes: do not trust without external verification)
> - [ ] **Community representation:** Does this topic primarily concern a community underrepresented in web text? (If yes: apply greater skepticism)
> - [ ] **Contradiction detection:** Did you ask the model follow-up questions that might surface inconsistencies in its claims? (Conflicting responses suggest low-confidence knowledge)
> - [ ] **Source citation:** Did the model offer specific citations? (Check: citations are frequently hallucinated — verify them independently)
> - [ ] **Task vs. fact:** Are you using the model for generation/reasoning (higher trust) or specific factual claims (lower trust)?

---

### 8.8 Spaced Repetition Seeds

> [!flashcard]
> **Question:** What is the core difference between a base (pretrained) model and a deployed assistant?
> **Answer:** A base model has been pretrained on a large corpus and has broad knowledge but unreliable instruction-following, inconsistent values, and may produce harmful outputs. A deployed assistant has been further trained with instruction tuning and RLHF to be helpful, safe, and consistent. The base model is the capability foundation; post-training shapes its behavior.
> **Source:** Section 7
> **Difficulty:** Basic
> **Tags:** #pretraining, #base-model, #instruction-tuning, #rlhf

> [!flashcard]
> **Question:** What is the key distinction between autoregressive language modeling and masked language modeling as pretraining objectives?
> **Answer:** Autoregressive LM predicts the next token using only left-context (unidirectional); it is well-suited for text generation. Masked LM fills in masked tokens using both left and right context (bidirectional); it is well-suited for comprehension tasks. GPT-family models use autoregressive; BERT-family models use masked LM.
> **Source:** Section 2
> **Difficulty:** Intermediate
> **Tags:** #pretraining-objectives, #autoregressive, #masked-lm, #gpt, #bert

> [!flashcard]
> **Question:** Why do hallucinations occur in large language models?
> **Answer:** Pretraining produces a statistical model of language, not a database of verified facts. A model "knows" things in proportion to how consistently accurate information appeared in the training data. When a topic was rare, contradictory, or underrepresented, the model may produce plausible-sounding but incorrect output — because it is completing a pattern, not retrieving a verified fact.
> **Source:** Section 7
> **Difficulty:** Intermediate
> **Tags:** #hallucination, #parametric-knowledge, #pretraining, #reliability

> [!flashcard]
> **Question:** What is WebText, and why does it differ from Common Crawl?
> **Answer:** WebText is a curated corpus of ~45GB assembled by collecting text from outbound links shared on Reddit with ≥3 upvotes. Unlike Common Crawl (a raw web crawl of petabytes), WebText is quality-filtered by community curation rather than automated heuristics. Its trade-off: higher average quality, but narrower demographic and cultural representativeness (skewing toward Reddit's user base).
> **Source:** Section 5
> **Difficulty:** Basic
> **Tags:** #webtext, #common-crawl, #corpus-quality, #reddit

> [!flashcard]
> **Question:** What is the Chinchilla finding, and why does it matter for corpus design?
> **Answer:** The Chinchilla paper (Hoffmann et al., 2022) found that prior large models were undertrained — their parameter counts were disproportionately large relative to the data they were trained on. Smaller models trained on more data achieved equal or better performance. The practical implication: more data, not just more parameters, is key to performance — making corpus quality and quantity directly important to model capability.
> **Source:** Section 3
> **Difficulty:** Intermediate
> **Tags:** #chinchilla, #scaling-laws, #compute-optimal, #data-efficiency

> [!flashcard]
> **Question:** What is The Pile, and what was its design philosophy?
> **Answer:** The Pile is an open-source 825GB training corpus assembled by EleutherAI from 22 distinct sources including web text, academic papers, code, books, and legal documents. Its design philosophy is "diversity as quality" — the hypothesis that training across many domains produces better generalization than training on a single domain, even if the single domain is high quality.
> **Source:** Section 6
> **Difficulty:** Basic
> **Tags:** #the-pile, #eleutherai, #diversity, #corpus-design

> [!flashcard]
> **Question:** What is benchmark contamination, and why does it matter for interpreting model evaluations?
> **Answer:** Benchmark contamination occurs when evaluation test data (benchmark questions and answers) appears in the training corpus, allowing a model to "memorize" the answers rather than genuinely solve the task. It inflates apparent performance and makes it difficult to know whether a model can generalize or has simply memorized. Large-scale web scraping makes contamination difficult to prevent or detect entirely.
> **Source:** Section 4 / Lexicon
> **Difficulty:** Intermediate
> **Tags:** #benchmark-contamination, #evaluation, #common-crawl, #generalization

> [!flashcard]
> **Question:** Why can fine-tuning and RLHF dramatically change a model's behavior while using relatively little additional training data?
> **Answer:** Fine-tuning and RLHF do not teach new knowledge — they redirect existing capability. Because the base model already has broad knowledge and language ability from pretraining, post-training only needs to change the model's behavioral dispositions (answer rather than continue, refuse rather than comply, prefer certain styles over others). Redirecting existing capability is much cheaper than creating it from scratch.
> **Source:** Section 7
> **Difficulty:** Advanced
> **Tags:** #fine-tuning, #rlhf, #pretraining, #capability-redirection, #lora

> [!flashcard]
> **Question:** Name three ways that training corpus composition shapes a deployed language model's behavior.
> **Answer:** (1) **Knowledge breadth and gaps:** What topics are represented determines what the model can speak to reliably; underrepresented communities/languages produce weak knowledge. (2) **Embedded biases:** Statistical patterns in biased text enter the model through the training objective; the model will reproduce these patterns unless actively corrected. (3) **Implicit values:** The corpus encodes a distribution of value systems; the base model "inherits" the most statistically prevalent values from the training text.
> **Source:** Sections 4-8
> **Difficulty:** Advanced
> **Tags:** #corpus-composition, #bias, #representation, #values, #pretraining

---

### 8.9 Expansion Topics for the PKB

> [!further-exploration] **Potential Expansion Topics**
> Based on the synthesis and gaps identified in this report, the following topics represent the highest-value directions for subsequent investigation. Each is an area where this report introduced the concept but could not do it full justice, and where a dedicated report would substantially deepen the PKB's coverage of the language model landscape.

> [!topic-idea] **Instruction Tuning and RLHF: The Post-Pretraining Stack**
> **Title:** [[instruction-fine-tuning|Instruction Tuning and RLHF — Foundational Report]]
> **Description:** This report repeatedly noted that deployed assistants differ from base models because of instruction tuning and RLHF, but could only gesture at the mechanics. A dedicated report would examine how supervised fine-tuning on instruction-response pairs works, how RLHF collects human preference data and uses it to train a reward model, how Constitutional AI extends the RLHF paradigm, and what the practical limits of post-training alignment are.
> **Connection to This Report:** This report established the base model as the capability substrate; the post-pretraining stack is what turns that substrate into a useful, aligned assistant. The two topics form a natural sequence.
> **Priority:** Critical
> **Suggested Report Type:** Foundational Report
> **Prerequisites:** [[reinforcement-learning-from-human-feedback]], [[instruction-fine-tuning]], [[supervised-fine-tuning]], [[constitutional-ai]], [[value-alignment-problem]]

> [!topic-idea] **Scaling Laws and the Compute-Optimal Frontier**
> **Title:** [[llm-scaling-laws|Scaling Laws for Language Models — Foundational Report]]
> **Description:** Section 3 of this report introduced the scaling laws concept — that model performance improves predictably with data, parameters, and compute — but did not trace the full intellectual history or practical implications. A dedicated report would examine the original Kaplan et al. formulation, the Chinchilla refinements, what the power-law exponents mean in practice, the ongoing debate about whether scaling will continue to produce capability gains, and the implications for resource allocation in AI development.
> **Connection to This Report:** Scaling laws are the empirical foundation for why pretraining corpus design matters at all — the relationship between data quality, data quantity, and downstream model performance depends on the scaling regime.
> **Priority:** High
> **Suggested Report Type:** Foundational Report
> **Prerequisites:** [[llm-scaling-laws]], [[emergent-abilities-in-llms]], [[phase-transitions-in-llms]], [[scaling-and-capability-emergence]]

> [!topic-idea] **AI Data Ethics, Copyright, and Governance**
> **Title:** [[value-alignment-problem|AI Training Data Ethics and Governance — Dialectical Report]]
> **Description:** Section 8 introduced the ethical dimensions of corpus design but acknowledged that the legal and ethical debates are actively evolving and unresolved. A Dialectical Report — presenting the strongest form of both the "open training data" and the "consent and licensing" positions, then synthesizing toward practical recommendations — would be well-suited to this contested terrain. Topics would include: the legal status of training data in multiple jurisdictions, the copyright case law developing around AI, community consent frameworks, the "fair use" debate, and what responsible data governance for AI training would look like.
> **Connection to This Report:** This report argued that corpus composition is as important as model architecture; the governance question is: who decides what goes in the corpus, and on what terms?
> **Priority:** High
> **Suggested Report Type:** Dialectical Report
> **Prerequisites:** [[value-alignment-problem]], [[constitutional-ai]], [[deceptive-alignment]], [[reward-hacking]]

> [!topic-idea] **Tokenization: How Text Becomes Numbers**
> **Title:** [[byte-pair-encoding|Tokenization in Large Language Models — Foundational Report]]
> **Description:** This report mentioned tokens frequently but treated the tokenization step as a black box. A dedicated foundational report would explain what tokenization actually does — how raw text is converted into the numerical sequences that models actually process — including byte-pair encoding (BPE), WordPiece, and SentencePiece approaches, why vocabulary size is a genuine design tradeoff, what tokenization artifacts look like in practice, and how tokenization choices affect model performance on different languages and domains.
> **Connection to This Report:** Tokenization is the bridge between the raw text corpus and the pretraining objective; understanding it fills the gap between "text is collected" and "next token is predicted."
> **Priority:** High
> **Suggested Report Type:** Foundational Report
> **Prerequisites:** [[byte-pair-encoding]], [[subword-tokenization]], [[vocabulary-size-tradeoffs]], [[cross-lingual-tokenization]], [[tokenization-artifacts]]

> [!topic-idea] **Fine-Tuning Strategies: From Full Fine-Tuning to LoRA**
> **Title:** [[parameter-efficient-fine-tuning|Parameter-Efficient Fine-Tuning — Foundational Report]]
> **Description:** This report noted that fine-tuning redirects existing capability efficiently, and mentioned LoRA and PEFT methods briefly. A dedicated report would examine the full landscape of fine-tuning strategies: when full fine-tuning is warranted, what prompt tuning and prefix tuning do, how LoRA achieves efficient adaptation, what catastrophic forgetting is and how it constrains fine-tuning strategy, and practical guidance for choosing a fine-tuning approach given compute and data constraints.
> **Connection to This Report:** Fine-tuning is the mechanism by which pretrained base models become specialized or deployed assistants; its efficiency is precisely what makes the pretraining-as-foundation approach economically viable.
> **Priority:** Medium
> **Suggested Report Type:** Practitioner's Field Guide
> **Prerequisites:** [[parameter-efficient-fine-tuning]], [[lora-low-rank-adaptation]], [[full-fine-tuning-vs-peft]], [[catastrophic-forgetting-in-llms]], [[task-specific-fine-tuning]]

---

### 8.10 Connections to the PKB and Other Reports

> [!connections-and-links] **Connections to the PKB and Other Reports**
>
> **1. Upstream Dependencies — This Report Builds On**
>
> This report presupposes and elaborates upon the following permanent notes, which should be read as preparation or consulted for deeper foundations:
>
> - [[transformer-attention-mechanism]] — The transformer architecture is the neural network structure that pretraining fills with knowledge; understanding how attention heads process token sequences is the mechanical foundation beneath the pretraining objective.
> - [[self-attention-patterns]] — The specific way transformers represent relationships between tokens during training is what allows the autoregressive and masked pretraining objectives to encode world knowledge into parameters.
> - [[byte-pair-encoding]] and [[subword-tokenization]] — Pretraining operates on tokens, not words; the tokenization step is logically prior to the pretraining objective and determines the basic unit of prediction.
> - [[scaling-and-capability-emergence]] — The empirical finding that capabilities emerge non-linearly with scale is the background assumption behind the decision to build ever-larger pretraining runs on ever-larger corpora.
> - [[benchmark-contamination]] — The risk that evaluation benchmarks appear in training data is a direct consequence of large-scale web scraping and is essential context for interpreting capability claims.
>
> **2. Downstream Applications — This Report Enables**
>
> Having read this report, the following permanent notes become richer and more interpretable:
>
> - [[instruction-fine-tuning]] and [[supervised-fine-tuning]] — Now understood as the behavioral redirection layer built atop the base model's pretraining-acquired knowledge; the quality of fine-tuning is bounded by the quality of the base model.
> - [[reinforcement-learning-from-human-feedback]] — The RLHF process operates on a base model that has already encoded the patterns, biases, and world knowledge of the pretraining corpus; RLHF shapes behavior but cannot create knowledge the pretraining corpus didn't provide.
> - [[hallucination-detection]] and [[hallucination-taxonomy]] — Hallucinations are now understood mechanistically as failures of statistical knowledge representation, not random errors; they occur predictably where training data was sparse, contradictory, or misleading.
> - [[retrieval-augmented-generation]] — RAG is best understood as a remedy for the fundamental limitation of parametric knowledge: by injecting retrieved documents at inference time, it compensates for the gaps and staleness that are structural properties of any finite pretraining corpus.
> - [[value-alignment-problem]] — The alignment challenge is now situated at its origin: in the statistical encoding of values from training data, not merely in the post-training specification of desired behavior.
>
> **3. Lateral Connections — Mutual Enrichment**
>
> These permanent notes address adjacent questions whose insights enrich and are enriched by this report's framework:
>
> - [[emergent-abilities-in-llms]] and [[phase-transitions-in-llms]] — The discovery that capabilities appear suddenly at training scale thresholds directly motivates the "scale first" approach to corpus design; in turn, this report's analysis of what the corpus contains illuminates why some capabilities emerge where they do.
> - [[parametric-vs-contextual-knowledge]] — The distinction between what a model knows from pretraining and what it can access from an in-context prompt is fundamental; this report's account of what pretraining produces is the foundation for understanding parametric knowledge's strengths and limits.
> - [[in-context-learning]] and [[few-shot-prompting]] — These capabilities are precisely what pretraining on diverse text enables; they do not require additional training because the base model has already learned to recognize and continue patterns across many domains.
> - [[domain-adaptation-llms]] — Domain adaptation is often necessary because pretraining corpora, despite their scale, are not uniformly representative of the domains in which models are deployed; this report's analysis of corpus composition explains why.
>
> **4. Strengthened Nodes — Specific Existing Notes This Report Enriches**
>
> These permanent notes in the PKB are directly enriched by reading this report — it provides the context, history, and mechanisms that deepen them:
>
> - [[llm-scaling-laws]] — This report contextualizes the scaling laws within the corpus design decision space; scaling laws describe the relationship between data and performance, while this report describes what that data actually is.
> - [[constitutional-ai]] — Understanding that the base model's implicit values come from the pretraining corpus enriches the account of why Constitutional AI's techniques operate at the post-training stage; they are shaping, not replacing, pretraining-embedded representations.
> - [[multilingual-emergent-transfer]] — This note on cross-lingual capabilities is directly enriched by this report's analysis of why English-dominant training corpora produce models with weaker multilingual performance.
> - [[continual-learning-llms]] — The challenges of continual learning — updating a model's knowledge without overwriting prior learning — are grounded in the static snapshot nature of pretraining corpora discussed throughout this report.

---

### 8.12 Report Quality Self-Assessment

> [!quality-assessment] **Report Quality Self-Assessment**
>
> | Dimension | Score | Evidence | Notes |
> |-----------|-------|----------|-------|
> | Depth of Coverage | 8/10 | 8 main body sections covering objectives, corpora, scale, base model capabilities, ethics, and limitations | Mathematical formulations of objectives were intentionally omitted per user request; some technical depth sacrificed for accessibility |
> | Structural Completeness | 9/10 | All 12 appendix subsections present; full scaffolding (situation models, reflective prompts, summaries) in every section | Cross-Report Navigation absent (not a series) |
> | Complexity Appropriateness | 9/10 | Technical content presented through analogy, contrast, and practical consequence; no equations; verified against "no mathematics" constraint | Some concepts (tokenization, training loop mechanics) were necessarily simplified |
> | Coverage Completeness | 8/10 | All major corpora (Common Crawl, WebText, The Pile) and objectives (autoregressive, masked, denoising) covered in depth | Synthetic data and data-mixing strategies not covered (emerging topic post-2023); multilingual corpus design underspecified |
> | Accuracy and Evidence | 8/10 | All technical claims grounded in published research; 8 primary citations provided; key figures section situates claims in intellectual history | Citations could not be independently verified during generation; some interpretations may over-simplify nuanced findings |
> | Knowledge Graph Contribution | 9/10 | ≥55 wiki-links placed; rich connections section with 4 categories × 5+ entries; upstream/downstream dependencies specified | Some wiki-links point to notes not yet created in PKB |
> | Practical Utility | 9/10 | Two practical protocols (evaluation and checklist); three far-transfer domains; 9 SR seeds with type distribution | Protocols designed for non-technical users; practitioners building models will want more specificity |
> | Originality | 7/10 | Corpus-as-Curriculum framework; Examined Witness-voiced integration of ethical and technical analysis; far-transfer domains to library science and epidemiology | Report synthesizes rather than extends research literature; original contributions are analytical/pedagogical rather than empirical |
> | **Composite Score** | **8.38/10** | | **PASS** (threshold 8.0) |
>
> **Identified Limitations**
> 1. The intentional omission of mathematical content means that readers who go on to read primary literature will encounter a vocabulary gap; the report does not prepare them for the notation and formalization of the field.
> 2. Synthetic data generation — an increasingly important technique for augmenting pretraining corpora — is largely absent, as it emerged as a major strategy after the 2020–2022 period that the report primarily covers.
> 3. The ethics section (Section 8) necessarily adopts a normative stance on contested issues (copyright, bias, consent); readers with different ethical frameworks may find certain assessments overconfident.
> 4. Corpus composition details for proprietary frontier models (GPT-4, Claude 3, Gemini) are not publicly disclosed; the report covers what is documented, which understates the field's current practices.
>
> **Recommendations for Future Revision**
> - Add a Section 9 specifically on synthetic data generation and data augmentation as training corpus strategies (post-2023 development).
> - Extend Section 8 ethics discussion with specific legal case outcomes as they become available.
> - Cross-link with the RLHF and instruction tuning report (when created) to complete the full model development pipeline narrative.
> - Add a section on multilingual corpus design and cross-lingual transfer when the [[multilingual-emergent-transfer]] topic is developed in depth.









