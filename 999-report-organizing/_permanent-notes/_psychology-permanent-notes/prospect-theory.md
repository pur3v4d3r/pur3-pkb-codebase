---
title: Prospect Theory
aliases:
  - Prospect Theory
  - Kahneman-Tversky prospect theory
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - decision-science

domain: decision-science
subdomains:
  - behavioral-economics
  - cognitive-psychology

created: 2026-04-25
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - prospect-theory-synthetic-seed-2026-04-25
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Decision Science
related:
  - '[[reference-dependence]]'
  - '[[expected-utility-theory]]'
  - '[[framing-effect]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[reference-dependence]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[]]'
contradicts:
  - '[[expected-utility-theory]]'
applies-to:
  - '[[framing-effect]]'
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
  last-diagrammed: '2026-05-23'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-23) -->

> [!abstract] **Diagram 1 — Prospect Theory Process Flow**
> *Follow the decision-making process from outcomes to choices.*
>
> ```mermaid
> flowchart LR
>   A[Outcomes] --> B[Reference Point]
>   B --> C[Transform into Gains/Losses]
>   C --> D[Value Function]
>   D --> E[Weighting Function]
>   E --> F[Decision]
> ```


> [!abstract] **Diagram 2 — Prospect Theory Value and Weight Functions**
> *Observe the shape of value and weighting functions for gains and losses.*
>
> ```mermaid
> graph TD
>   A[Value Function]
>   B[Weighting Function]
>   C[Gains]
>   D[Losses]
>   A -->|Concave| C
>   A -->|Convex| D
>   B -->|Overweight small probabilities| D
>   B -->|Underweight moderate-to-large probabilities| C
> ```


> [!abstract] **Diagram 3 — Prospect Theory Applications in Decision-Making**
> *Identify how Prospect Theory explains different decision-making scenarios.*
>
> ```mermaid
> flowchart LR
>   A[Insurance] --> B[Certainty Effect]
>   C[Investment Decisions] --> D[Risk Aversion]
>   E[Policymaking] --> F[Behavioral Nudges]
>   subgraph Insurance
>     A -->|Willing to pay premiums for small chance of avoiding large losses| end
>   subgraph Investment Decisions
>     C -->|Avoid high-risk investments despite higher potential returns| end
>   subgraph Policymaking
>     E -->|Automatic enrollment in retirement plans with opt-out provisions| end
> ```

# Prospect Theory

> [!definition] **Prospect Theory**
> Prospect Theory is a descriptive theory of decision-making under risk developed by Kahneman and Tversky in 1979, which explains how people evaluate outcomes relative to a reference point, weight probabilities non-linearly, and exhibit loss aversion. It falls under [[decision-science]], challenging the assumptions of expected-utility theory by focusing on psychological biases rather than economic rationality.

> [!attention] **Boundary**
> This concept excludes traditional expected-utility theory and focuses on the psychological aspects of decision-making rather than economic rationality.

## Core Explanation

At its core, Prospect Theory posits that individuals evaluate outcomes as gains or losses relative to a reference point, which is often their current state. This means that people do not simply assess the final wealth states but instead consider how much better or worse off they are compared to this baseline. For example, losing $100 feels more negative than gaining $100 feels positive, illustrating loss aversion.

The theory also introduces a value function that captures the asymmetric sensitivity of people to gains and losses. This function is concave for gains (people prefer smaller gains) and convex for losses (people fear larger losses), meaning that losses loom larger than equivalent gains. The weighting function, on the other hand, describes how probabilities are perceived; small probabilities are overweighted, while moderate-to-large probabilities are underweighted.

These components together explain why people often make decisions that deviate from what expected-utility theory would predict. For instance, the certainty effect shows that people prefer a certain outcome over a risky one with an equivalent expected value, and the reflection effect demonstrates how preferences reverse when framed differently (e.g., gaining $100 vs losing $100).

The empirical grounding of Prospect Theory comes from numerous experiments where participants were asked to make choices under risk. These studies consistently showed that people's decisions aligned with the predictions of Prospect Theory, challenging the traditional view that individuals are rational maximizers of utility.

<!-- enhancement-pass:1 (2026-05-02) -->
Prospect Theory's insights into loss aversion and reference dependence have profound implications for understanding financial behavior beyond just insurance and investment decisions. For instance, in consumer choice, the theory explains why discounts framed as 'losses' (e.g., 'buy one get one free') are more compelling than equivalent gains ('50% off'). This framing effect leverages people's tendency to avoid losses over acquiring additional gains, even when the economic outcomes are identical. Such insights underscore how subtle changes in presentation can significantly influence consumer preferences and decision-making processes.

## Mechanism

Prospect Theory operates through a two-step process: first, it transforms outcomes into gains or losses relative to a reference point. Then, it applies a value function and weighting function to these transformed outcomes. The value function captures the asymmetric sensitivity to gains and losses, while the weighting function reflects how probabilities are perceived.

For example, when faced with a choice between a sure gain of $100 and a 50% chance of winning $200 or nothing, most people prefer the sure gain despite the higher expected value. This is because the certain outcome feels more valuable than the risky one due to loss aversion.

## Practical Implications

> [!example] **Application 1 — Insurance**
> In insurance, Prospect Theory explains why individuals are willing to pay premiums for a small chance of avoiding large losses. The certainty effect and loss aversion make people value the security provided by insurance more than the expected cost.

> [!example] **Application 2 — Investment Decisions**
> Prospect Theory helps explain why investors might avoid high-risk investments even if they offer higher potential returns. Loss aversion makes them fear large losses, leading to risk-averse behavior that can be observed in their investment choices.

<!-- enhancement-pass:1 (2026-05-02) -->

> [!example] **Application 3 — Behavioral nudges in public policy**
> Public policymakers often use Prospect Theory to design behavioral nudges that encourage beneficial outcomes without restricting freedom of choice. For example, automatic enrollment in retirement savings plans with opt-out provisions leverages the status quo bias and loss aversion by making it psychologically easier for individuals to stay enrolled than to actively choose to disengage. This approach has been shown to increase participation rates significantly compared to traditional opt-in schemes.

## Key Distinctions

> [!key-distinction] **Prospect Theory vs Expected-Utility Theory**
> While expected-utility theory assumes individuals are rational maximizers of utility and make decisions based on the expected value, Prospect Theory focuses on psychological biases. The key distinction lies in their descriptive versus normative status; expected-utility is a prescriptive model of how an ideal agent should choose, whereas Prospect Theory describes how people actually behave.

<!-- enhancement-pass:1 (2026-05-02) -->

> [!key-distinction] **Reflective vs Reactive Thinking**
> Prospect Theory highlights the role of reactive thinking in decision-making, where individuals respond quickly and emotionally to potential gains or losses relative to a reference point. This contrasts with reflective thinking, which involves slower, more deliberate cognitive processes that might align better with expected utility theory's assumptions about rational choice. Understanding this distinction is crucial for recognizing how psychological biases can overshadow economic rationality in real-world decisions.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-02) -->

> [!warning] **Misconception** — Prospect Theory assumes all individuals are irrational.
>
> While Prospect Theory does highlight systematic deviations from rational decision-making, it does not imply that people are inherently irrational. Instead, it describes how psychological biases influence choices in predictable ways. These biases can lead to suboptimal decisions under certain conditions but do not negate the capacity for rational thought altogether.

## Key Figures

- **Daniel Kahneman** — Co-originator of Prospect Theory with Amos Tversky, Kahneman's work on cognitive biases and decision-making under risk has significantly influenced the field of behavioral economics.
- **Amos Tversky** — Tversky was a key collaborator with Kahneman in developing Prospect Theory. His research on heuristics and biases provided empirical evidence supporting the theory's predictions.

## Open Questions

> [!open-question] **Question**
> How does Prospect Theory apply in real-world economic policies?
>
> *What would resolve it:* Empirical studies analyzing how policymakers use Prospect Theory to design more effective interventions could help resolve this question.

> [!open-question] **Question**
> Can Prospect Theory be used to improve decision-making in business?
>
> *What would resolve it:* Case studies and experimental research demonstrating the practical benefits of applying Prospect Theory in corporate settings would provide insights into its potential applications.

<!-- enhancement-pass:1 (2026-05-02) -->

> [!open-question] **Question**
> How do cultural differences affect the application of Prospect Theory?
>
> *What would resolve it:* Cross-cultural studies are needed to determine if and how Prospect Theory's principles vary across different societal contexts. Understanding these variations could provide insights into more culturally sensitive applications of behavioral economics in policy-making.

## Synthesis

Prospect Theory matters because it provides a more accurate model of human decision-making under risk, accounting for psychological biases that traditional expected-utility theory overlooks. By understanding these biases, policymakers and businesses can design better incentives, policies, and strategies. The theory's implications extend beyond economics into psychology, marketing, and public health, offering valuable insights into how people perceive risks and make choices in uncertain situations.

The significance of Prospect Theory lies in its ability to bridge the gap between psychological reality and economic rationality, making it a cornerstone of behavioral decision science.

<!-- enhancement-pass:1 (2026-05-02) -->
By integrating psychological biases with economic decision-making, Prospect Theory offers a nuanced view that bridges cognitive psychology and economics. This interdisciplinary approach not only enhances our understanding of human behavior but also provides practical tools for designing interventions that align more closely with how people actually make decisions in real-world scenarios.

## Connections & Context

**Falls under:** [[decision-science]]

**Specializes:** [[reference-dependence]]

**Contradicts:** [[expected-utility-theory]]

**Applies to:** [[framing-effect]]

**Source:** [[prospect-theory-synthetic-seed-2026-04-25]]

<!-- enhancement-pass:1 (2026-05-02) -->

### Why these connections matter

> [!connection] **[[framing-effect]]** — *applies-to*
> The framing effect, which shows how the presentation of information can alter decision-making outcomes, is a critical application of Prospect Theory. By manipulating how options are framed as gains or losses relative to a reference point, individuals' preferences and choices can be systematically influenced. This connection underscores how psychological biases embedded in Prospect Theory manifest through specific cognitive heuristics like framing.
