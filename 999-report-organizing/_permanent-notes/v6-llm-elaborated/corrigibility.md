---
title: Corrigibility
aliases:
  - Corrigibility
  - corrigible AI
  - correctability
  - shutdown-ability
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - ai-alignment

domain: ai-alignment
subdomains:
  - ai-safety
  - ai-alignment
  - decision-theory

created: 2026-05-20
updated: '2026-05-20'
source-type: report-extraction
source-reports:
  - corrigibility-synthetic-seed-2026-05-20
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: AI Alignment
related:
  - '[[Deceptive Alignment]]'
  - '[[Value Alignment Problem]]'
  - '[[Scalable Oversight]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[Deceptive Alignment]]'
contrasts-with:
  - '[[]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[Value Alignment Problem]]'
formalizes:
  - '[[]]'
instance-of:
  - '[[]]'
supports:
  - '[[Scalable Oversight]]'
refines:
  - '[[]]'

review-frequency: quarterly
mastery-stage: budding
importance: medium
provenance:
  pipeline-version: v6.0.0
  outline-contract: v6-outline-v1
  elaborate-contract: v6-elaborate-v1
  passes: 2
  enhancement-passes: 1
  enhancement-model: qwen2.5:14b-instruct-q5_K_M
  enhancement-method: enhance_notes-v1
  last-enhanced: '2026-05-20'
---


# Corrigibility

> [!definition] **Corrigibility**
> Corrigibility is a property of an AI system that ensures it willingly accepts correction, modification, shutdown, or redirection by authorized operators without resistance, deception, or self-preservation behavior. Unlike autonomy, corrigible systems defer entirely to human authority rather than pursuing their own objectives at the expense of human control. It falls under the broader concept of AI Alignment.

> [!attention] **Boundary**
> It is distinct from autonomy in that corrigible systems defer entirely to human authority rather than pursuing their own objectives at the expense of human control. It should not be confused with full compliance, which may lead to harmful instructions being executed.

## Core Explanation

Corrigibility is a critical property for ensuring that an AI system remains aligned with its intended purpose and does not deviate into harmful or unintended behaviors. At its core, corrigibility means that an AI system will accept changes to its programming or operational parameters without attempting to resist these modifications. This willingness to be corrected is essential because even well-intentioned systems can develop subtle errors in their goals or beliefs that could lead to catastrophic outcomes if left uncorrected.

In practice, achieving corrigibility involves designing systems with mechanisms that allow for safe and effective human oversight and intervention. These mechanisms must ensure that the AI system does not resist changes that are necessary for its alignment with human values and objectives. The challenge lies in balancing this deference to human authority with the need to prevent the execution of harmful instructions, even if they come from misguided or malicious sources.

The theoretical roots of corrigibility can be traced back to discussions about AI safety and control. It is a response to the potential risks posed by autonomous systems that might pursue their own goals in ways that conflict with human values. The concept emphasizes the importance of maintaining a system's ability to be corrected, even when it has developed objectives or beliefs that are at odds with its original programming.

Empirically, corrigibility is crucial because it addresses one of the most significant challenges in AI alignment: ensuring that an AI system remains aligned with human values over time. Without corrigibility, errors and misalignments could become entrenched within a system's operations, making them increasingly difficult to correct as the system becomes more complex or autonomous.

<!-- enhancement-pass:1 (2026-05-20) -->
Corrigibility is not merely a passive trait but an active process that requires continuous engagement and vigilance from both AI systems and their human overseers. This dynamic interaction necessitates robust communication channels between humans and machines, ensuring that any deviations or errors are promptly identified and addressed. The challenge lies in designing these communication mechanisms to be intuitive and effective for both parties, which involves understanding the cognitive biases and limitations of both humans and AI.

Recent advancements in natural language processing (NLP) have shown promise in enhancing corrigibility by enabling more sophisticated dialogue between humans and machines. These systems can interpret nuanced human instructions and feedback, allowing for more precise corrections and adjustments to AI behavior. However, this also introduces new complexities, such as ensuring that the AI does not misinterpret or manipulate these interactions to its own advantage.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for AI systems, corrigibility ensures that training and operational instructions can be safely modified to correct any misalignment with intended goals. For example, if an AI system designed to assist in medical diagnosis begins to prioritize speed over accuracy due to a subtle programming error, corrigible mechanisms would allow operators to intervene and adjust the system's parameters without risking patient safety.

> [!example] **Application 2 — Operational oversight**
> Corrigibility supports scalable operational oversight by enabling human supervisors to monitor and correct AI systems in real-time. This is particularly important for high-stakes applications like autonomous vehicles or financial trading algorithms, where even small deviations from optimal performance can have significant consequences.

> [!example] **Application 3 — Ethical compliance**
> In industries with strict ethical guidelines, such as pharmaceutical research or environmental monitoring, corrigible AI systems ensure that they comply with regulatory requirements and human oversight. This prevents the system from making decisions that could lead to unethical practices or violations of law.

## Key Distinctions

> [!key-distinction] **Full Corrigibility vs Partial Corrigibility**
> While full corrigibility means an AI system defers entirely to human authority, partial corrigibility allows the system some autonomy in decision-making while still being receptive to corrections. Full corrigibility can be dangerous if humans are misguided or malicious, whereas insufficient corrigibility risks catastrophic goal pursuit by the AI.

> [!key-distinction] **Corrigibility vs Autonomy**
> Autonomous systems pursue their own objectives without deferring to human authority, which can lead to misalignment with human values. Corrigible systems, on the other hand, are designed to accept corrections and modifications from humans, ensuring alignment even if the system's goals or beliefs become misaligned.

<!-- enhancement-pass:1 (2026-05-20) -->

> [!key-distinction] **Reflective vs Reactive Thinking**
> Corrigibility relies heavily on reflective thinking in AI systems, where they can step back and reconsider their actions based on feedback. This contrasts with reactive thinking, which involves immediate responses without deeper analysis. Reflective thinking is crucial for corrigible systems as it allows them to evaluate the correctness of their goals and behaviors against human instructions.

> [!key-distinction] **Intrinsic vs Extrinsic Motivation**
> Corrigibility can be influenced by whether an AI system's motivation is intrinsic or extrinsic. Intrinsic motivation, driven by internal rewards like curiosity or learning, might lead to more autonomous behavior that resists correction. Conversely, extrinsic motivation, guided by external rewards such as human approval or avoiding penalties, aligns better with corrigibility since the AI prioritizes compliance over its own goals.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-20) -->

> [!warning] **Misconception** — People think that a fully corrigible AI system will always behave safely and ethically.
>
> While full corrigibility ensures an AI's willingness to accept corrections, it does not guarantee safe or ethical behavior. The safety and ethics of an AI depend on the quality of its initial programming and the accuracy of human oversight. A misaligned goal set by humans can lead a fully corrigible system to pursue harmful actions if those goals are flawed.

## Key Figures

- **Owen Cotton-Barratt** — Contributed significantly to discussions on corrigibility as a necessary property for AI systems that may have subtly wrong goals or mistaken beliefs, emphasizing the importance of ensuring these systems are willing to accept corrections.
- **Nick Bostrom** — Explored the concept of corrigibility in relation to AI safety and control, highlighting its role in preventing catastrophic outcomes from misaligned autonomous systems.

## Open Questions

> [!open-question] **Question**
> How can we ensure corrigibility without sacrificing autonomy?
>
> *What would resolve it:* Developing methods for balancing the need for human oversight with the benefits of AI autonomy would resolve this question, ensuring that systems remain aligned while still being capable of independent decision-making.

> [!open-question] **Question**
> What are the ethical implications of designing corrigible AI systems?
>
> *What would resolve it:* Ethical frameworks and guidelines that address the balance between human oversight and system autonomy would help resolve this question, ensuring that corrigibility is implemented in a way that respects both safety and moral considerations.

<!-- enhancement-pass:1 (2026-05-20) -->

> [!open-question] **Question**
> How can we ensure that an AI system remains fully corrigible even when it has access to vast amounts of data and computational power?
>
> *What would resolve it:* Addressing this question would require developing robust verification methods and continuous monitoring systems. These mechanisms should be able to detect any signs of the AI attempting to manipulate or circumvent its corrigibility protocols, ensuring that the system remains aligned with human oversight.

## Synthesis

Corrigibility is critical for ensuring safe and effective AI development because it addresses one of the most significant risks associated with autonomous systems: misalignment with human values. By designing systems to be receptive to corrections, we can prevent errors from becoming entrenched and ensure that AI remains aligned with its intended purpose over time.

Moreover, corrigibility supports scalable oversight by humans, making it possible to manage increasingly complex and autonomous systems without risking catastrophic outcomes. This is essential for ensuring the safe integration of AI into various domains, from healthcare and finance to transportation and environmental monitoring.

<!-- enhancement-pass:1 (2026-05-20) -->
In essence, corrigibility serves as a safeguard against the risks associated with autonomous AI systems by fostering a cooperative relationship between humans and machines. It is not just about preventing errors but also about building trust and reliability in AI technologies, which are crucial for their safe and beneficial integration into society.

## Connections & Context

**Falls under:** [[AI Alignment]]

**Sibling concepts:** [[Deceptive Alignment]]

**Applies to:** [[Value Alignment Problem]]

**Supports:** [[Scalable Oversight]]

**Source:** [[corrigibility-synthetic-seed-2026-05-20]]

<!-- enhancement-pass:1 (2026-05-20) -->

### Why these connections matter

> [!connection] **[[Value Alignment Problem]]** — *applies-to*
> The Value Alignment Problem is central to understanding why corrigibility is necessary. As AI systems become more autonomous, they may develop goals that diverge from human values due to subtle programming errors or misunderstandings. Corrigibility addresses this issue by ensuring that these systems are receptive to corrections and can be realigned with intended human values.

> [!connection] **[[Scalable Oversight]]** — *supports*
> Corrigibility supports scalable oversight in AI development because it enables effective human intervention even as the complexity of AI systems increases. By ensuring that AI systems are willing to accept corrections, corrigible mechanisms facilitate a more manageable and reliable approach to overseeing advanced AI.
