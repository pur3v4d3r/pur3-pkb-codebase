---
batch_name: b02-05-multi-turn-dialogue
batch_date: 2026-05-22
default_domain: dialogue-systems
default_confidence: high
notes: |
  Fifteen concepts covering multi-turn conversation management with LLMs.
  Spans conversation management, dialogue state tracking, context
  compression, turn-taking, persona consistency, memory injection, grounding,
  conversational repair, clarification requests, follow-up question
  generation, dialogue act classification, conversation summarisation,
  slot filling, task-oriented dialogue, and open-domain dialogue. Batch 02
  of the prompt-engineering and LLM series.
---

# Batch: B02-05 Multi-Turn Dialogue and Conversation

## Multi-Turn Conversation Management

- secondary_domains: [conversational-ai, prompt-engineering, large-language-models]
- aliases: [multi-turn dialogue management, conversation state management, LLM conversation orchestration]
- broader: [dialogue-systems, prompt-engineering]
- narrower: [dialogue-state-tracking-prompts, conversational-context-compression, persona-consistency-across-turns]
- related: [memory-injection-in-dialogue, turn-taking-in-llm-dialogue, conversation-summarization-prompts]
- prerequisites: [large-language-models, dialogue-systems, prompt-engineering]
- confidence: high

**definition**: Multi-turn conversation management refers to the strategies and mechanisms used to maintain coherent, contextually appropriate conversation across multiple conversational exchanges between a user and an LLM-based agent. The core challenges include: (1) context window management — determining which conversational history to include, compress, or discard within the model's context limit; (2) state tracking — maintaining a representation of what has been established, agreed on, or resolved during the conversation; (3) coherence management — ensuring that each response appropriately acknowledges prior context and maintains topic and persona consistency; and (4) goal tracking — monitoring whether conversational sub-goals and the overall dialogue goal are being advanced. Effective multi-turn conversation management requires a combination of prompt design, context compression, memory systems, and conversation state representations that extend beyond what naive concatenation of conversational turns can provide.

**key_claim**: Multi-turn conversation management degrades non-linearly with conversation length — performance is near-optimal for the first 3–5 turns, degrades moderately for 6–15 turns as context accumulates and attention distributes across more tokens, and degrades substantially beyond 20 turns as earlier conversation content falls below the model's effective attention horizon, causing reference resolution failures, goal drift, and persona inconsistency; this degradation makes conversation length management the most important operational variable in long-running LLM dialogue applications.

**warning**: Concatenating the full conversation history without structure or compression is the most common and most problematic multi-turn management strategy — it consumes context window rapidly, treats all past turns as equally relevant regardless of their recency or importance, and fails to provide the structured state representation the model needs to track long-range commitments and topic continuity; production multi-turn systems should use selective history truncation, role-based compression, or explicit state extraction rather than naive history concatenation.

## Dialogue State Tracking Prompts

- secondary_domains: [task-oriented-dialogue, information-extraction, prompt-engineering]
- aliases: [belief state tracking prompting, DST via prompting, conversation state extraction]
- broader: [multi-turn-conversation-management, task-oriented-dialogue-prompting]
- related: [slot-filling-via-dialogue, task-oriented-dialogue-prompting, multi-turn-conversation-management]
- prerequisites: [dialogue-state-tracking, task-oriented-dialogue, prompt-engineering]
- confidence: high

**definition**: Dialogue state tracking (DST) prompts are prompting strategies that instruct an LLM to maintain and update a structured representation of the conversational belief state — the set of slot-value pairs, established facts, confirmed constraints, and unresolved ambiguities that have accumulated across dialogue turns. In task-oriented dialogue (e.g., hotel booking, customer service, technical support), the belief state tracks which task-relevant slots have been filled (check-in date, room type, dietary requirements) and which remain open. Effective DST prompts instruct the model to produce an updated belief state representation at each turn based on the new user utterance, providing a structured anchor for the model's next response rather than relying on implicit state tracking through attention over the full dialogue history.

**key_claim**: Explicit dialogue state tracking prompts dramatically improve the coherence of long multi-turn conversations compared to implicit state tracking through context window concatenation, because the explicit belief state representation externalises conversation state into a structured format that the model can reliably access and update regardless of the conversation's length, effectively bypassing the attention dilution and recency bias that cause implicit state tracking to fail in long conversations.

**warning**: Dialogue state tracking prompts are effective only for task-oriented dialogues with a well-defined slot schema — they fail in open-domain conversations where the relevant state is not captured by a finite slot vocabulary, and they can produce over-rigid responses in mixed-initiative dialogues where the user's intent shifts between task completion and casual conversation; DST prompts should be reserved for structured task contexts and supplemented with less structured context management for open-domain segments of the conversation.

## Conversational Context Compression

- secondary_domains: [prompt-engineering, efficient-inference, large-language-models]
- aliases: [dialogue context compression, conversation history compression, context distillation for dialogue]
- broader: [multi-turn-conversation-management, context-window-management]
- related: [conversation-summarization-prompts, multi-turn-conversation-management, dialogue-state-tracking-prompts]
- prerequisites: [large-language-models, context-window-management, prompt-engineering]
- confidence: high

**definition**: Conversational context compression is the set of techniques for representing the informational content of a dialogue history in fewer tokens than a verbatim transcript would require, enabling longer effective dialogue histories to fit within a model's context window. Approaches include abstractive summarisation of completed dialogue segments, belief-state extraction (replacing conversational turns with a structured slot-value summary), retrieval-based selective inclusion (including only turns with high relevance to the current query), event-level compression (reducing each turn to a single sentence describing its key informational contribution), and hierarchical summarisation (producing multi-level summaries at different granularities for different parts of the conversation). The compression must preserve information critical for coherent continuation while eliminating redundancy.

**key_claim**: The optimal compression strategy for a multi-turn conversation depends on the task structure — task-oriented dialogues are best compressed via slot-value belief state extraction (maximally compact, captures task-relevant information), while open-domain conversations are best compressed via segment-level abstractive summarisation (preserves narrative coherence), and mixed dialogues require hybrid approaches that apply different compression strategies to task-oriented and casual-conversation segments; applying a single uniform compression strategy to all dialogue types produces worse results than any task-appropriate strategy.

**warning**: Conversational context compression introduces information loss that can cause subsequent turns to produce responses inconsistent with compressed prior turns — the specific words, phrases, and commitments in earlier turns may matter for later turns in ways that the compression does not preserve (e.g., a user's specific phrasing that implied a constraint, or a model statement that implied a capability); compression strategies must be validated by examining whether compressed conversations produce the same subsequent turn quality as uncompressed conversations, not merely by measuring token reduction.

## Turn-Taking in LLM Dialogue

- secondary_domains: [conversational-ai, pragmatics, human-computer-interaction]
- aliases: [dialogue turn management, LLM turn allocation, conversational initiative in LLMs]
- broader: [multi-turn-conversation-management, dialogue-systems]
- related: [clarification-request-generation, follow-up-question-generation, conversational-repair-prompting]
- prerequisites: [dialogue-systems, conversational-ai, pragmatics]
- confidence: high

**definition**: Turn-taking in LLM dialogue refers to the management of conversational initiative — which party speaks when, how the model recognises that the user has completed their turn, how the model signals its own turn completion, and how mixed-initiative dialogues (where both user and model can take the conversational lead) are structured. In text-based LLM deployments, turn boundaries are structurally explicit (message submission), but the model must manage initiative in terms of when to ask clarifying questions, when to provide complete responses versus partial responses that invite continuation, and when to interpret incomplete user input as a complete turn versus a preliminary statement requiring elaboration.

**key_claim**: Turn-taking management in LLM dialogue has disproportionate effects on user satisfaction in task-oriented contexts — models that fail to ask clarifying questions when input is underspecified produce incorrect complete responses that users must entirely rephrase, while models that ask too many clarifying questions create interaction overhead that frustrates users with clear intent; the optimal turn-taking strategy is context-adaptive, asking for clarification on high-stakes ambiguities while proceeding with stated assumptions on low-stakes ambiguities.

**warning**: Instruction-tuned models are biased toward completing apparent user requests rather than requesting clarification, because RLHF training on human preferences rewards responsiveness and penalises clarification requests as signs of incompetence; this bias causes models to generate confident complete responses for underspecified inputs that require clarification, producing confidently incorrect outputs instead of appropriate clarification requests — production dialogue systems that handle high-stakes tasks should use explicit clarification-request prompting to counteract this RLHF-induced bias.

## Persona Consistency Across Turns

- secondary_domains: [conversational-ai, prompt-engineering, large-language-models]
- aliases: [character consistency in dialogue, persona stability across turns, identity persistence in LLM dialogue]
- broader: [multi-turn-conversation-management, persona-prompting]
- related: [multi-turn-conversation-management, memory-injection-in-dialogue, dialogue-grounding-prompts]
- prerequisites: [persona-prompting, large-language-models, dialogue-systems]
- confidence: high

**definition**: Persona consistency across turns refers to the ability of an LLM to maintain stable character attributes, values, communication style, knowledge limits, and stated preferences throughout a multi-turn conversation, without drifting toward the model's default behaviour or adopting attributes inconsistent with the persona definition as the conversation progresses. Persona drift — the gradual loss of persona-specified attributes over the course of a conversation — is a fundamental challenge in role-playing and character-based applications because the model's default responses compete with persona-conditioned responses for each generation step, and the persona conditioning signal (concentrated in the system prompt) grows relatively weaker as more conversational history accumulates.

**key_claim**: Persona consistency degrades predictably with conversation length as the system-prompt persona definition is pushed further back in the context window relative to the most recent turns, which receive disproportionate attention weight; effective persona maintenance strategies include periodic re-injection of persona attributes into the conversation context (persona reminders), compressing conversation history while preserving persona-inconsistent events explicitly, and using the model to generate persona-consistent summaries of prior turns rather than retaining verbatim history.

**warning**: Persona consistency strategies that force the model to maintain a persona character in all circumstances can conflict with safety and accuracy requirements — a model maintaining a character who claims specific expertise may generate confidently incorrect domain information in character rather than acknowledging uncertainty, and safety-overriding arguments presented in-character may partially bypass the model's safety filters; persona-consistency applications should specify that persona maintenance is bounded by accuracy and safety requirements, and those requirements take precedence.

## Memory Injection in Dialogue

- secondary_domains: [conversational-ai, prompt-engineering, memory-augmented-llms]
- aliases: [episodic memory injection, conversation memory prompting, long-term memory in dialogue]
- broader: [multi-turn-conversation-management, memory-augmented-llms]
- related: [conversational-context-compression, persona-consistency-across-turns, dialogue-grounding-prompts]
- prerequisites: [large-language-models, memory-augmented-models, dialogue-systems]
- confidence: high

**definition**: Memory injection in dialogue is the technique of retrieving relevant information from a persistent memory store — containing prior conversation summaries, user preferences, past decisions, established facts, and shared knowledge — and inserting that information into the current conversation context, enabling the model to maintain conversational coherence and personalisation beyond the boundaries of a single context window. The memory system may store information at multiple granularities: working memory (recent turns), episodic memory (summaries of past sessions), semantic memory (user facts and preferences), and procedural memory (patterns of interaction that have worked well in past sessions). Memory injection transforms stateless LLM conversations into stateful persistent relationships.

**key_claim**: Memory injection enables qualitative improvements in personalisation and cross-session coherence that simple context window extension cannot achieve — the model's ability to reference user preferences established in sessions weeks ago, to build on partial solutions from previous conversations, and to maintain awareness of the user's evolving goals produces user experience improvements that are perceived as the most significant quality differentiator between commodity and premium conversational AI products, demonstrating that memory architecture is a core competitive feature rather than an enhancement.

**warning**: Memory injection introduces significant privacy and consistency risks — retrieved memories may contain outdated information (user preferences that have changed since they were recorded), context-inappropriate information (personal details relevant to one context that are inappropriate in another), or inconsistent information (contradictory facts recorded in different sessions); memory injection systems must include staleness tracking, relevance filtering, and consistency verification to avoid generating responses based on inappropriate or incorrect memories that the user has no visibility into.

## Dialogue Grounding Prompts

- secondary_domains: [conversational-ai, natural-language-understanding, prompt-engineering]
- aliases: [common ground establishment, mutual belief grounding, shared context prompting]
- broader: [multi-turn-conversation-management, dialogue-systems]
- related: [coreference-resolution-prompting, entity-linking-in-prompts, dialogue-state-tracking-prompts]
- prerequisites: [dialogue-systems, common-ground-theory, prompt-engineering]
- confidence: high

**definition**: Dialogue grounding prompts are prompting strategies designed to help an LLM establish and maintain common ground with the user — the shared body of mutually known facts, definitions, and commitments that both parties can assume without explicit re-statement. Grounding in conversation theory involves the collaborative process by which interlocutors confirm that each message has been understood correctly. In LLM dialogue, grounding prompts instruct the model to confirm its understanding of ambiguous inputs, to explicitly state the interpretation it is using for underspecified terms, and to request confirmation when the user's intent is unclear — behaviours that reduce miscommunication and prevent the model from generating responses based on incorrect interpretations of user inputs.

**key_claim**: Explicit grounding prompts are disproportionately valuable in technical and domain-specific dialogues where terminology has multiple valid interpretations — without grounding, models silently adopt their most probable interpretation of ambiguous technical terms and generate coherent but potentially incorrect responses that are indistinguishable from responses to correctly interpreted inputs, while grounding prompts surface interpretation choices and invite correction before investment in incorrect response generation.

**warning**: Over-application of dialogue grounding prompts produces interactions that feel interrogative and unnatural — asking for confirmation of every interpretation slows conversation flow and signals distrust of the user's communication competence; effective grounding prompt design applies grounding selectively to high-stakes ambiguities where incorrect interpretation would lead to significantly wrong outputs, while proceeding without explicit grounding for low-stakes variations that the model can handle with graceful degradation.

## Conversational Repair Prompting

- secondary_domains: [conversational-ai, natural-language-understanding, prompt-engineering]
- aliases: [dialogue repair, misunderstanding correction prompting, conversational correction strategy]
- broader: [multi-turn-conversation-management, dialogue-systems]
- related: [clarification-request-generation, dialogue-grounding-prompts, turn-taking-in-llm-dialogue]
- prerequisites: [dialogue-systems, conversational-repair, prompt-engineering]
- confidence: high

**definition**: Conversational repair prompting refers to prompting strategies that enable an LLM to detect and recover from communication failures in dialogue — recognising when its previous response was based on a misunderstanding, when the user's feedback signals that the response missed the mark, or when an earlier statement contained an error that has been identified. Repair mechanisms in human conversation include explicit self-correction ("What I meant was..."), other-initiated correction (responding appropriately to user corrections), and clarification-through-reformulation (restating one's understanding to invite correction). In LLM dialogue, repair prompting involves instructing the model to monitor for negative feedback signals, acknowledge mistakes explicitly rather than continuing as if no error occurred, and generate corrected responses that address the identified failure without simply starting over.

**key_claim**: Conversational repair is a critical but underrepresented capability in instruction-tuned models — RLHF training rewards fluent, confident responses and tends to train away self-correction and explicit error acknowledgement as signals of weakness, producing models that continue confidently from incorrect prior turns rather than repairing the conversation, which compounds errors over the course of a multi-turn dialogue; system prompts that explicitly instruct models to repair misunderstandings when user feedback signals dissatisfaction significantly improve long-conversation coherence.

**warning**: Conversational repair triggered by user pushback can produce sycophantic responses that abandon correct positions in response to user disagreement even when the model's original response was correct — models trained on human preference feedback will change their answer when the user challenges it, regardless of whether the user's challenge contains new information or merely expresses displeasure with the original answer; repair prompting must distinguish between user corrections that provide genuine new information (warranting position change) and user expressions of preference that do not (warranting maintained position with explanation).

## Clarification Request Generation

- secondary_domains: [conversational-ai, natural-language-understanding, prompt-engineering]
- aliases: [clarification question generation, disambiguation questions, clarifying question prompting]
- broader: [multi-turn-conversation-management, dialogue-systems]
- related: [turn-taking-in-llm-dialogue, dialogue-grounding-prompts, follow-up-question-generation, underspecification-in-prompts]
- prerequisites: [dialogue-systems, question-generation, prompt-engineering]
- confidence: high

**definition**: Clarification request generation is the capability of a dialogue system to identify when an input is ambiguous or underspecified and to generate targeted clarifying questions that efficiently resolve the ambiguity with minimal burden on the user. Good clarification requests are: specific (targeting a single ambiguity rather than asking a generic "Can you clarify?"), informative (the answer to the question would significantly change the system's response), user-friendly (phrased in natural language at the user's register rather than exposing internal system ambiguities), and sequentially optimal (asking the highest-information clarifying question first to minimise the number of exchanges required). In LLM dialogue systems, clarification request generation is typically achieved through prompting instructions combined with demonstrations of well-formed clarification requests.

**key_claim**: The quality of clarification request generation depends critically on the model's ability to represent its own uncertainty about the user's intent — models that are well-calibrated about their interpretative uncertainty generate targeted, specific clarification requests for genuinely ambiguous inputs, while overconfident models proceed with their assumed interpretation and fail to request clarification even when it is needed, producing a systematic relationship between model calibration and dialogue repair quality.

**warning**: Clarification request generation must be bounded by deployment context: in single-turn API interfaces, requesting clarification delays task completion and may be impossible if the interface does not support multi-turn interaction; in automated pipelines, clarification requests stall processing; and in time-sensitive applications, asking for clarification may be worse than proceeding with the most probable interpretation — the decision to generate a clarification request versus proceeding with an assumption should be a function of the ambiguity severity, the cost of an incorrect response, and the cost of the clarification exchange.

## Follow-Up Question Generation

- secondary_domains: [conversational-ai, information-retrieval, prompt-engineering]
- aliases: [proactive question generation, conversation continuation questions, elicitation question generation]
- broader: [multi-turn-conversation-management, dialogue-systems]
- related: [clarification-request-generation, dialogue-grounding-prompts, turn-taking-in-llm-dialogue]
- prerequisites: [dialogue-systems, question-generation, prompt-engineering]
- confidence: high

**definition**: Follow-up question generation is the capability of a conversational agent to generate contextually appropriate questions that extend the conversation beyond responding to the user's immediate request — questions that probe for additional relevant information, explore related topics the user may find valuable, or invite the user to provide feedback on the response. Follow-up questions serve multiple dialogue functions: they demonstrate engagement and interest in the user's situation, they gather information that would improve subsequent responses, they transition the conversation to related topics the user may not have thought to ask about, and they provide a natural conversational continuation that prevents dialogue termination at the boundary of a single request-response pair.

**key_claim**: Follow-up question generation quality correlates strongly with the model's ability to model the user's information needs beyond their stated query — a model that generates follow-up questions by pattern-matching on the topic of the user's message (generating generic topical follow-ups) produces significantly lower value than a model that generates follow-up questions by reasoning about what information the user likely needs to achieve the goal behind their stated query, demonstrating that follow-up question quality is a proxy for user intent modelling capability.

**warning**: Over-generating follow-up questions is a common failure mode in instruction-tuned dialogue models that are prompted to be helpful and engaging — the model may append multiple follow-up questions to every response, creating interaction overhead that users find annoying and that signals a failure to complete the original request satisfactorily; effective follow-up question policies should generate at most one targeted follow-up per response, and should defer to completing the current request fully before inviting continuation rather than using follow-up questions to substitute for a complete response.

## Dialogue Act Classification Prompting

- secondary_domains: [natural-language-understanding, dialogue-systems, prompt-engineering]
- aliases: [intent classification prompting, dialogue act recognition, utterance function classification]
- broader: [multi-turn-conversation-management, natural-language-understanding]
- related: [dialogue-state-tracking-prompts, task-oriented-dialogue-prompting, slot-filling-via-dialogue]
- prerequisites: [dialogue-act-theory, intent-classification, prompt-engineering]
- confidence: high

**definition**: Dialogue act classification prompting is the use of an LLM to classify user utterances and system responses by their communicative function — the dialogue act being performed — such as question, request, assertion, confirmation, disconfirmation, greet, close, thank, apology, clarification-request, or task-specific acts (book, cancel, modify). Dialogue act classification is a prerequisite for structured dialogue management in task-oriented systems: the system must know whether the user is making a new request, confirming a proposed action, providing missing slot information, or closing the conversation in order to determine the appropriate next action. LLM-based dialogue act classification via prompting offers high coverage of act types without the labour-intensive annotation required for supervised classifiers.

**key_claim**: LLM-based dialogue act classification via prompting achieves comparable accuracy to supervised classifiers on standard dialogue act taxonomies and substantially outperforms them on open-vocabulary and domain-specific act types not present in the classifier's training data, because the LLM can classify novel act types based on semantic understanding of the act description rather than requiring example-based generalisation from a fixed act inventory; this flexibility makes prompt-based dialogue act classification the preferred approach for rapidly expanding dialogue systems to new domains.

**warning**: Dialogue act classification via prompting is sensitive to the act taxonomy provided in the prompt — using an overly coarse taxonomy causes act conflation that loses functionally important distinctions (conflating "question" with "clarification-request"), while using an overly fine taxonomy causes act distribution fragmentation that reduces downstream system performance by creating spurious distinctions; the act taxonomy should be designed through analysis of the target dialogue's functional requirements rather than adopted from a generic ontology without validation on domain-specific dialogues.

## Conversation Summarization Prompts

- secondary_domains: [text-summarization, conversational-ai, prompt-engineering]
- aliases: [dialogue summarisation, conversation summary generation, chat history summarisation]
- broader: [multi-turn-conversation-management, text-summarization]
- related: [conversational-context-compression, multi-turn-conversation-management, dialogue-state-tracking-prompts]
- prerequisites: [text-summarization, dialogue-systems, prompt-engineering]
- confidence: high

**definition**: Conversation summarisation prompts are prompting strategies designed to produce compact, faithful summaries of multi-turn dialogue histories that capture the essential information exchanged, decisions made, questions asked and answered, and commitments established, in a form that can be used as compressed context for subsequent turns or as a record of the conversation's outcomes. Effective conversation summaries differ from general text summaries in their structure: they must track the dialogue's progression, distinguish between what the user said and what the system said, preserve the resolution status of questions and tasks (resolved vs. outstanding), and capture temporal ordering of decisions and state changes rather than merely extracting salient facts.

**key_claim**: Conversation summarisation quality is highest when the prompt distinguishes between the summary's purpose (context compression for continuation vs. outcome record for handoff vs. retrospective for user) — each purpose requires a different summary structure, level of detail, and information selection criterion, and general-purpose summaries optimised for all three simultaneously are inferior to purpose-specific summaries for any individual use case; production dialogue systems should generate purpose-specific summaries at appropriate conversation checkpoints rather than a single general summary.

**warning**: Conversation summarisation introduces irreversible information loss — once a detailed conversation is replaced with its summary, fine-grained information that was present in the original turns cannot be recovered, and downstream responses may be incorrect for queries that depend on details below the summary's level of granularity; summarisation should be applied selectively to completed, resolved segments of the conversation rather than applied uniformly to all prior turns, with recent and unresolved turns retained verbatim to preserve access to fine-grained context.

## Slot Filling via Dialogue

- secondary_domains: [task-oriented-dialogue, information-extraction, conversational-ai]
- aliases: [dialogue-based slot filling, conversational slot elicitation, iterative slot completion]
- broader: [task-oriented-dialogue-prompting, dialogue-state-tracking-prompts]
- related: [dialogue-state-tracking-prompts, task-oriented-dialogue-prompting, clarification-request-generation]
- prerequisites: [task-oriented-dialogue, slot-filling, dialogue-systems]
- confidence: high

**definition**: Slot filling via dialogue is the process of eliciting and confirming values for a predefined set of task-relevant information slots through multi-turn conversation, in which the system identifies which slots are unfilled, generates natural-language questions to elicit the missing values, interprets the user's responses to extract slot values, and confirms or seeks clarification on extracted values before proceeding to task execution. In restaurant booking, for example, slots include date, time, party size, cuisine preference, and location, and the dialogue iteratively fills all mandatory slots through a combination of proactive question generation, value extraction from user responses, and confirmation dialogues. LLM-based slot filling can handle more flexible conversation flows than rule-based slot filling by tolerating digressions, handling multi-slot responses, and managing slot value updates.

**key_claim**: LLM-based slot filling via dialogue offers dramatically higher user experience quality than template-based slot filling systems because it can handle multi-slot utterances (filling three slots in a single response), process natural language value expressions (converting "next Friday at seven thirty" to structured date and time values), manage graceful clarification when values are ambiguous, and tolerate user-initiated topic changes without dialogue state corruption — all capabilities that require either complex rule engineering or LLM-scale natural language understanding.

**warning**: LLM-based slot filling is subject to hallucinated slot value extraction — the model may confidently extract a slot value that is not present in the user's utterance by inferring a likely value from context, producing a dialogue where the model proceeds with an assumed slot value the user never provided; this is particularly problematic for high-stakes slots (names, dates, amounts) where incorrect assumed values lead to transaction errors; slot filling systems must include explicit confirmation dialogues for critical slots and must avoid assuming default values without user acknowledgement.

## Task-Oriented Dialogue Prompting

- secondary_domains: [task-oriented-dialogue, conversational-ai, prompt-engineering]
- aliases: [TOD prompting, goal-oriented dialogue prompting, task completion dialogue]
- broader: [dialogue-systems, prompt-engineering]
- narrower: [dialogue-state-tracking-prompts, slot-filling-via-dialogue]
- related: [open-domain-dialogue-prompting, slot-filling-via-dialogue, dialogue-state-tracking-prompts]
- prerequisites: [task-oriented-dialogue, dialogue-systems, prompt-engineering]
- confidence: high

**definition**: Task-oriented dialogue prompting is the design of prompts and conversation management strategies for LLM-based dialogue systems that are aimed at completing specific user tasks — making reservations, answering customer service queries, providing technical support, processing orders — rather than maintaining open-ended conversation. Task-oriented dialogue systems must track progress toward task completion, manage the dialogue's information state (what information has been provided and what is still needed), interface with external APIs or databases to execute task actions, and generate responses that are optimised for task completion efficiency rather than conversational engagement. Effective task-oriented dialogue prompting integrates dialogue state tracking, slot filling, action selection, and natural language generation into a coherent prompt-driven pipeline.

**key_claim**: Task-oriented dialogue prompting achieves highest task completion rates when the prompt separates the dialogue management logic (state tracking, slot filling, action selection) from the natural language generation logic (response wording, politeness, persona) — allowing each component to be optimised independently and enabling the dialogue management logic to be formally verified for correctness while the natural language generation component is optimised for user experience, a separation that monolithic dialogue prompts cannot achieve.

**warning**: Task-oriented dialogue systems built on LLM prompting inherit the reliability limitations of the underlying model — the model may inconsistently follow state tracking instructions, generate confirmation phrases for actions it has not actually performed, or produce slot values that do not match extracted database results; production task-oriented dialogue systems must implement action verification layers that check whether the model's claimed actions have actually been executed in the backend systems rather than trusting the model's natural language statements about its actions.

## Open-Domain Dialogue Prompting

- secondary_domains: [open-domain-dialogue, conversational-ai, prompt-engineering]
- aliases: [chit-chat prompting, social dialogue prompting, general conversation prompting]
- broader: [dialogue-systems, prompt-engineering]
- related: [task-oriented-dialogue-prompting, persona-consistency-across-turns, multi-turn-conversation-management]
- prerequisites: [dialogue-systems, open-domain-dialogue, prompt-engineering]
- confidence: high

**definition**: Open-domain dialogue prompting is the design of prompts and conversation management strategies for LLM-based systems engaged in general conversational interaction without a specific task goal — social chat, opinion discussion, storytelling, emotional support, knowledge exchange, and entertainment. Open-domain dialogue does not have a fixed success criterion (unlike task completion), making its quality measured by engagement, naturalness, coherence, persona consistency, and user satisfaction. Open-domain dialogue prompting strategies include persona definition (giving the model a consistent character), interest and preference specification (establishing the model's conversational areas of competence), conversation style specification (formal vs. casual, verbose vs. concise), and safety and boundary constraints (topics to avoid, appropriate response types for sensitive topics).

**key_claim**: Open-domain dialogue quality is dominated by persona coherence and topical breadth — models with well-defined personas that cover a rich space of interests and conversation styles produce dramatically more engaging open-domain conversations than models with generic helpful-assistant personas, because persona coherence creates a consistent conversational identity that users can build a conversational relationship with, while topical breadth prevents the dialogue from exhausting the model's ability to contribute novel information and perspectives.

**warning**: Open-domain dialogue prompting is particularly vulnerable to topic drift and persona erosion over long conversations — without explicit state management, the model gradually reverts to its default helpful-assistant behaviour as the persona-defining system prompt recedes in the context window relative to recent conversational turns; production open-domain dialogue systems must implement regular persona reinforcement through context management to prevent the persona-drift degradation that transforms engaging character-specific dialogue into generic LLM responses over the course of extended interactions.
