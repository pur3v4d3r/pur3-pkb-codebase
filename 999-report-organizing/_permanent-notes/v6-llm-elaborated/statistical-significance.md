---
title: "Statistical Significance"
aliases:
  - "Statistical Significance"
  - "p-value significance"
  - "NHST significance"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - research-methods

domain: research-methods
subdomains:
  - statistics
  - research-methods

created: 2026-05-01
updated: 2026-05-01

source-type: report-extraction
source-reports:
  - "statistical-significance-synthetic-seed-2026-05-01"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Null-Hypothesis Significance Testing"

related:
  - "[[Effect Size]]"
  - "[[Replication Crisis]]"
  - "[[Preregistration]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[]]"
broader:
  - "[[]]"
see-also:
  - "[[]]"
contrasts-with:
  - "[[Effect Size]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[Replication Crisis]]"
formalizes:
  - "[[]]"
instance-of:
  - "[[]]"
supports:
  - "[[Preregistration]]"
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

# Statistical Significance

> [!definition] **Statistical Significance**
> Statistical Significance refers to the decision criterion in null-hypothesis significance testing where results with p-values below a pre-specified threshold (commonly 0.05) are considered evidence against the null hypothesis, despite its limitations and critiques. It falls under [[Null-Hypothesis Significance Testing]], which is a procedural rule originating in Fisher and Neyman-Pearson with sharply different interpretive commitments in the two original frameworks.

> [!attention] **Boundary**
> This concept excludes measures of effect size or practical importance, which are distinct from statistical significance.

## Core Explanation

Statistical significance is a threshold used to decide whether an observed effect is likely due to chance or not. When a p-value, which measures the probability of observing the data under the null hypothesis, falls below this threshold (typically 0.05), researchers reject the null hypothesis in favor of an alternative one. However, this decision rule does not provide information about the magnitude of the effect or its practical importance; it only indicates whether the observed result is statistically unlikely to have occurred by chance.

The concept of statistical significance has been a focus of sustained methodological critique because users often misinterpret it as evidence that the null hypothesis is false, which is incorrect. The procedure controls only the long-run false-positive rate and provides no posterior probability for any individual hypothesis; equating 'statistically significant' with 'true' or 'important' inverts the procedure's logic and overstates by an unbounded amount what a single significant p-value warrants.

The origins of statistical significance can be traced back to Ronald Fisher, who introduced it as a decision rule in 1925. However, the Neyman-Pearson framework, which emerged later, emphasized the importance of setting both Type I and Type II error rates, leading to different interpretive commitments compared to Fisher's approach.

The threshold for statistical significance is often set at 0.05, but this arbitrary choice has led to widespread misinterpretation and misuse in research. For instance, a p-value just below 0.05 might be considered 'significant,' while one just above it might not, even though the difference between them may be negligible.

## Mechanism

Statistical significance is calculated by comparing the observed data to what would be expected under the null hypothesis using a test statistic and a p-value. If the p-value is below the pre-specified threshold (e.g., 0.05), it suggests that the observed effect is unlikely to have occurred due to chance alone, leading researchers to reject the null hypothesis.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design, misinterpreting statistical significance can lead educators to believe a new teaching method is effective when it might not be. For example, if a study finds that a new teaching strategy yields a p-value of 0.049, instructors might adopt the method without considering whether the effect size is meaningful or replicable.

> [!example] **Application 2 — Clinical trials**
> In clinical trials, misinterpreting statistical significance can result in the approval of ineffective treatments. For instance, a drug might show a statistically significant improvement over a placebo with a p-value just below 0.05, but this does not necessarily mean it is clinically relevant or safe for widespread use.

> [!example] **Application 3 — Economic policy**
> In economic policy, misinterpreting statistical significance can lead to the implementation of policies based on weak evidence. For example, a study might find that a new tax policy yields a p-value just below 0.05, but if the effect size is small and not practically significant, the policy could be ineffective or even harmful.

## Key Distinctions

> [!key-distinction] **Statistical vs Practical Significance**
> Statistical significance does not indicate the magnitude of an effect; it only suggests that the observed result is unlikely to have occurred by chance. In contrast, practical significance refers to whether the effect size is large enough to be meaningful in a real-world context. For example, a study might find a statistically significant increase in test scores with a p-value of 0.049, but if the actual improvement is only one point, it may not be practically significant.

## Key Figures

- **Ronald Fisher** — Ronald Fisher is credited as the originator of statistical significance in 1925. He introduced the concept as a decision rule for hypothesis testing, which has since become a cornerstone of modern research methods.

## Open Questions

> [!open-question] **Question**
> Why is the threshold for statistical significance often set at 0.05?
>
> *What would resolve it:* The choice of 0.05 as the standard threshold could be resolved by empirical evidence showing that other thresholds are more appropriate in different fields or contexts.

> [!open-question] **Question**
> How can researchers avoid misinterpreting p-values?
>
> *What would resolve it:* Researchers could avoid misinterpretation by focusing on effect sizes, confidence intervals, and preregistration of studies to reduce researcher degrees of freedom.

## Synthesis

Understanding statistical significance is crucial for researchers and practitioners because it helps them make informed decisions based on empirical evidence. However, the limitations of this concept highlight the need for a more nuanced approach that considers both statistical and practical significance. By integrating effect sizes, confidence intervals, and preregistration into research practices, we can mitigate issues related to misinterpretation and improve the reliability and replicability of scientific findings.

Statistical significance is also relevant in fields like psychology, economics, and medicine, where it plays a significant role in validating theories and informing policy decisions. Addressing ongoing debates about statistical significance will enhance the credibility and impact of research across these domains.

## Connections & Context

**Falls under:** [[Null-Hypothesis Significance Testing]]

**Contrasts with:** [[Effect Size]]

**Applies to:** [[Replication Crisis]]

**Supports:** [[Preregistration]]

**Source:** [[statistical-significance-synthetic-seed-2026-05-01]]
