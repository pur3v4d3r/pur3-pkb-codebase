---
title: Theory of Planned Behavior
aliases:
  - Theory of Planned Behavior
  - TPB
  - Ajzen TPB
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - motivational-psychology

domain: motivational-psychology
subdomains:
  - social-psychology
  - health-psychology

created: 2026-04-25
updated: '2026-05-22'
source-type: report-extraction
source-reports:
  - theory-of-planned-behavior-synthetic-seed-2026-04-25
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Behavior Change Theory
related:
  - '[[Theory of Reasoned Action (TRA)]]'
  - '[[stages-of-change-model]]'
  - '[[implementation-intentions]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[Theory of Reasoned Action (TRA)]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[stages-of-change-model]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[implementation-intentions]]'
formalizes:
  - '[[]]'
instance-of:
  - '[[]]'
supports:
  - '[[]]'
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
  last-enhanced: '2026-05-02'
  diagram-passes: 1
  diagram-model: qwen2.5:14b-instruct-q5_K_M
  last-diagrammed: '2026-05-22'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-22) -->

> [!abstract] **Diagram 1 — TPB Structural Overview**
> *Follow the flow from attitudes to behavior.*
>
> ```mermaid
> graph TD
>   A[Attitudes]
>   B[Subjective Norms]
>   C[Perceived Behavioral Control]
>   D[Intention]
>   E[Behavior]
>   A -->|influence| D
>   B -->|influence| D
>   C -->|influence| D
>   D -->|predicts| E
> ```


> [!abstract] **Diagram 2 — TPB Mechanism Flowchart**
> *Trace the steps from attitudes to behavior.*
>
> ```mermaid
> flowchart LR
>   A[Attitudes] --> B[Initial Evaluation]
>   B --> C[Subjective Norms]
>   C --> D[Social Influence]
>   D --> E[Perceived Behavioral Control]
>   E --> F[Feasibility Assessment]
>   F --> G[Intention Formation]
>   G --> H[Predicted Behavior]
> ```


> [!abstract] **Diagram 3 — TPB vs Theory of Reasoned Action**
> *Compare TPB with its predecessor.*
>
> ```mermaid
> graph TD
>   A[Theory of Reasoned Action]
>   B[Attitudes]
>   C[Subjective Norms]
>   D[Intention]
>   E[Behavior]
>   F[Perceived Behavioral Control]
>   G[Intention]
>   H[Behavior]
>   A -->|includes| B
>   A -->|includes| C
>   B -->|influence| D
>   C -->|influence| D
>   D -->|predicts| E
>   A --> F
>   B -->|influence| G
>   C -->|influence| G
>   F -->|influence| G
>   G -->|predicts| H
> ```

# Theory of Planned Behavior

> [!definition] **Theory of Planned Behavior**
> The Theory of Planned Behavior (TPB) is a framework developed by Icek Ajzen that explains how attitudes toward behavior, subjective norms, and perceived behavioral control influence intention to perform a specific behavior, which in turn predicts actual behavior. It falls under [[Behavior Change Theory]], accommodating volitional behaviors by adding perceived behavioral control to its predecessor, the theory of reasoned action.

> [!attention] **Boundary**
> This theory focuses on volitional behaviors and does not address non-volitional or automatic behaviors. It also does not account for the entire process of behavior change but rather models the factors that lead to intention formation.

## Core Explanation

At the heart of TPB is the idea that our intentions to engage in certain behaviors are shaped by three key factors: attitudes toward the behavior (our positive or negative evaluation of performing it), subjective norms (the perceived social pressure from important others to perform or not perform the behavior), and perceived behavioral control (our belief about how easy or difficult it would be to carry out the behavior). These components interact in a way that forms our intention, which then predicts actual behavior.

For instance, if someone strongly believes that exercising is beneficial for their health (attitude) and feels supported by friends who also exercise (subjective norm), but doubts they have time or energy to do so (perceived behavioral control), TPB would predict a lower intention to exercise. This prediction then influences whether the person actually exercises.

TPB builds upon the theory of reasoned action, which posits that attitudes and subjective norms are sufficient for predicting behavior. However, TPB adds perceived behavioral control as an additional predictor, making it more comprehensive in explaining volitional behaviors—those where we have some degree of conscious control over our actions.

Empirical studies support these claims, showing that interventions targeting all three components can effectively change intentions and subsequent behaviors. For example, campaigns promoting vaccination might focus on increasing perceived efficacy (perceived behavioral control) to boost intention among those who are hesitant.

<!-- enhancement-pass:1 (2026-05-02) -->
The TPB framework has been widely applied in various fields, including public health and environmental psychology, to understand and predict behaviors such as smoking cessation, recycling habits, and dietary choices. Its strength lies in its ability to integrate subjective factors with perceived control over behavior, making it a versatile tool for designing interventions that target multiple psychological dimensions simultaneously.

## Mechanism

The mechanism by which TPB operates involves a step-by-step process: first, attitudes toward the behavior form our initial evaluation. Next, subjective norms influence us based on what we think others expect or approve of. Finally, perceived behavioral control assesses how feasible it is to perform the behavior. These factors collectively shape our intention, and if strong enough, this intention translates into actual behavior.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for health education programs, TPB can guide the creation of interventions that address all three components. For example, a program to encourage healthy eating might include information on the benefits (attitude), social support from peers and family (subjective norm), and practical tips on how to incorporate healthier choices into daily life (perceived behavioral control).

> [!example] **Application 2 — Environmental conservation**
> For environmental initiatives, TPB can help design campaigns that not only inform about the importance of recycling but also highlight community support for such practices and provide easy access to recycling bins. This multi-faceted approach is more likely to change intentions and behaviors compared to a single focus on information alone.

> [!example] **Application 3 — Consumer behavior**
> In marketing, TPB can be used to create advertisements that not only highlight the benefits of a product (attitude) but also show how it fits into one's social life (subjective norm) and is easily accessible or affordable (perceived behavioral control). This comprehensive approach can lead to stronger intentions among consumers.

<!-- enhancement-pass:1 (2026-05-02) -->

> [!example] **Application 4 — Spaced retrieval in MOOCs**
> In Massive Open Online Courses (MOOCs), spaced retrieval can be used to enhance learning outcomes by reinforcing key concepts over time. Applying TPB, educators might design interventions that not only provide information on the benefits of spaced retrieval (attitude) but also foster a supportive online community environment where learners feel encouraged to engage in this practice (subjective norm). Additionally, offering practical tools and resources for implementing spaced retrieval can increase perceived behavioral control, thereby enhancing students' intentions to use this strategy.

## Key Distinctions

> [!key-distinction] **Attitude vs. Subjective Norm**
> While attitudes reflect our personal evaluation of a behavior, subjective norms are based on perceived social pressure from others. For example, someone might have a positive attitude toward vegetarianism but feel pressured by their family to eat meat (high subjective norm). TPB recognizes that both factors play crucial roles in shaping intentions.

<!-- enhancement-pass:1 (2026-05-02) -->

> [!key-distinction] **Intrinsic vs Extrinsic Motivation**
> While TPB primarily focuses on the role of attitudes, norms, and perceived control in shaping behavior, it does not explicitly differentiate between intrinsic (internally driven) and extrinsic (externally driven) motivations. Understanding whether a person's intention to perform a behavior stems from internal satisfaction or external rewards can provide deeper insights into their motivation levels and persistence over time.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-02) -->

> [!warning] **Misconception** — People think TPB only applies to voluntary behaviors.
>
> TPB is specifically designed for volitional behaviors, but it does not mean it cannot be applied in contexts where some level of control over the behavior exists. For instance, while certain health behaviors may seem involuntary due to medical necessity, individuals can still exert some degree of control over how they manage their conditions.

## Key Figures

- **Icek Ajzen** — Icek Ajzen is the originator of TPB, developing it in 1985 as an extension of the theory of reasoned action to better predict volitional behaviors.

## Open Questions

> [!open-question] **Question**
> How can TPB be improved to better predict actual behavior?
>
> *What would resolve it:* Further research could explore how additional factors, such as implementation intentions or self-efficacy, might enhance the predictive power of TPB.

> [!open-question] **Question**
> What are the best strategies to address the intention-behavior gap?
>
> *What would resolve it:* Developing more effective interventions that bridge the gap between intention and behavior could involve integrating implementation intentions or other complementary models into TPB-based programs.

<!-- enhancement-pass:1 (2026-05-02) -->

> [!open-question] **Question**
> How does TPB account for changes in attitudes over time?
>
> *What would resolve it:* Further research could explore how dynamic changes in attitudes affect the stability of behavioral intentions and subsequent actions. Understanding these temporal dynamics can refine TPB's predictive power.

## Synthesis

The Theory of Planned Behavior is a cornerstone in motivational psychology, offering a robust framework for understanding and predicting volitional behaviors. Its application spans various domains, from health promotion to environmental conservation and consumer behavior. By addressing the complex interplay between attitudes, subjective norms, and perceived behavioral control, TPB provides valuable insights into how we can design effective interventions that not only change intentions but also lead to lasting changes in behavior.

TPB's influence extends beyond its theoretical contributions; it has inspired numerous empirical studies and practical applications. Its ability to account for volitional behaviors makes it a powerful tool for researchers and practitioners alike, highlighting the importance of considering multiple factors when designing interventions.

<!-- enhancement-pass:1 (2026-05-02) -->
By integrating subjective norms and perceived behavioral control, TPB offers a nuanced view of behavior prediction that goes beyond simple attitude-behavior correlations. This holistic approach makes it particularly useful for designing interventions aimed at fostering positive behavioral changes across diverse contexts.

## Connections & Context

**Falls under:** [[Behavior Change Theory]]

**Generalizes to:** [[Theory of Reasoned Action (TRA)]]

**Contrasts with:** [[stages-of-change-model]]

**Applies to:** [[implementation-intentions]]

**Source:** [[theory-of-planned-behavior-synthetic-seed-2026-04-25]]

<!-- enhancement-pass:1 (2026-05-02) -->

### Why these connections matter

> [!connection] **[[implementation-intentions]]** — *applies-to*
> Implementation intentions are a strategy that complements TPB by specifying when, where, and how to perform the intended behavior. This approach enhances perceived behavioral control within TPB's framework, making it more likely for individuals to translate their intentions into actual behaviors.
