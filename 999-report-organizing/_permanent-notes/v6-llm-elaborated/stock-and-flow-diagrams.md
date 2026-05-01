---
title: "Stock and Flow Diagrams"
aliases:
  - "Stock and Flow Diagrams"
  - "stock-and-flow notation"
  - "SFD"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - systems-thinking

domain: systems-thinking
subdomains:
  - systems-thinking
  - modeling

created: 2026-05-01
updated: 2026-05-01

source-type: report-extraction
source-reports:
  - "stock-and-flow-diagrams-synthetic-seed-2026-05-01"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Systems Thinking"

related:
  - "[[Causal-Loop Diagrams]]"
  - "[[Feedback Loops]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[]]"
broader:
  - "[[]]"
see-also:
  - "[[]]"
contrasts-with:
  - "[[Causal-Loop Diagrams]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[Feedback Loops]]"
formalizes:
  - "[[]]"
instance-of:
  - "[[]]"
supports:
  - "[[]]"
refines:
  - "[[]]"

review-frequency: quarterly
mastery-stage: budding
importance: medium

provenance:
  pipeline-version: "v6.0.0"
  outline-contract: "v6-outline-v1"
  elaborate-contract: "v6-elaborate-v1"
  passes: 2
---

# Stock and Flow Diagrams

> [!definition] **Stock and Flow Diagrams**
> Stock and Flow Diagrams (SFD) are formal diagrams that distinguish between accumulations of quantities (stocks) and the rates at which they change (flows), falling under [[Systems Thinking]]. They enforce a clarification that prose descriptions and causal-loop diagrams systematically blur: the distinction between a stock, which can change only by inflow minus outflow over time, and the rates that act on it. This has direct quantitative consequences and routinely identifies modeling errors.

> [!attention] **Boundary**
> This concept excludes qualitative causal-loop diagrams and quantitative differential-equation models, focusing on the visual representation of stocks and flows in system dynamics.

## Core Explanation

Stock and Flow Diagrams are central to system dynamics, providing a visual representation of stocks (accumulations) and flows (rates). Stocks are represented as rectangular boxes, while flows are depicted with pipe-and-valve symbols. Auxiliary variables and information links connect these elements, bridging qualitative causal-loop diagrams with the quantitative differential-equation models required for simulation.

In practice, SFDs help in identifying and correcting modeling errors that arise from ambiguous arrows or unclear relationships between stocks and flows. By enforcing a clear distinction, they ensure that each stock's change is accurately represented as inflow minus outflow over time, which is crucial for accurate simulations and predictions.

Theoretical roots of SFDs lie in the broader field of systems thinking, where they are used to model complex systems by breaking them down into manageable components. This approach allows analysts to understand how different parts of a system interact and influence each other over time, leading to more robust models and better decision-making.

Historically, SFDs have been instrumental in various applications, from environmental management to business strategy. For instance, they can be used to model population dynamics, where the stock represents the number of individuals, and flows represent birth rates and death rates. This clarity helps in identifying critical points of intervention or potential bottlenecks.

## Mechanism

Creating a Stock and Flow Diagram involves several steps: first, identify the stocks (accumulations) within the system, such as inventory levels or population sizes. Next, determine the flows that affect these stocks, like production rates or migration patterns. Each flow must have units consistent with its associated stock's unit divided by time. For example, if a stock is measured in kilograms and changes over days, a flow might be expressed in kilograms per day.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design, SFDs can help educators model student learning processes. By representing knowledge acquisition as a stock and study time as a flow, designers can identify optimal pacing strategies that maximize learning efficiency.

> [!example] **Application 2 — Environmental management**
> SFDs are used to model ecosystems, where stocks represent species populations and flows represent birth rates, death rates, and migration. This helps in predicting the impact of environmental changes on these systems and developing effective conservation strategies.

## Key Distinctions

> [!key-distinction] **Intrinsic vs Extraneous Load**
> Stock and Flow Diagrams are distinct from qualitative causal-loop diagrams by their focus on intrinsic load (the inherent capacity of a system) versus extraneous load (additional demands placed on the system). SFDs clearly delineate these concepts, making it easier to identify and manage system constraints.

## Key Figures

- **John Sterman** — A prominent contributor in the field of system dynamics, John Sterman has extensively researched and popularized Stock and Flow Diagrams. His work includes developing educational tools that use SFDs to teach complex systems thinking.

## Open Questions

> [!open-question] **Question**
> How do Stock and Flow Diagrams handle non-linear dynamics?
>
> *What would resolve it:* Further research into modeling techniques specifically designed for non-linear systems would help clarify how SFDs can be adapted to represent these complex behaviors.

> [!open-question] **Question**
> What are the best practices for integrating Stock and Flow Diagrams with other modeling techniques?
>
> *What would resolve it:* Guidelines and case studies demonstrating successful integration of SFDs with differential-equation models or causal-loop diagrams would provide practical insights into combining these approaches.

## Synthesis

Stock and Flow Diagrams are crucial in systems thinking because they offer a clear, visual method for understanding complex interactions within systems. By distinguishing between stocks and flows, SFDs help identify modeling errors that can lead to inaccurate predictions or ineffective strategies. Their application spans various fields, from environmental management to business strategy, making them indispensable tools for decision-making.

The importance of SFDs extends beyond their practical utility; they also contribute to a deeper understanding of system dynamics by enforcing rigorous discipline in model construction. This clarity is essential for effective communication and collaboration among stakeholders.

## Connections & Context

**Falls under:** [[Systems Thinking]]

**Contrasts with:** [[Causal-Loop Diagrams]]

**Applies to:** [[Feedback Loops]]

**Source:** [[stock-and-flow-diagrams-synthetic-seed-2026-05-01]]
