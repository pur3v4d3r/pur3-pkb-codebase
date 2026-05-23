---
title: "Inter-Annotator Agreement"
aliases:
  - "Inter-Annotator Agreement"
  - "Inter-Annotator Agreement in Evals"
  - "IAA in LLM evaluation"
  - "annotator consistency"
  - "human evaluator reliability"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - llm-evaluation
  - human-evaluation
  - annotation-quality

created: 2026-05-22
updated: 2026-05-22

source-type: report-extraction
source-reports:
  - "inter-annotator-agreement-in-evals-synthetic-seed-2026-05-22"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "LLM Evaluation"

related:
  - "[[LLM Evaluation]]"
  - "[[Human vs. LLM Agreement]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[LLM Evaluation]]"
broader:
  - "[[]]"
see-also:
  - "[[]]"
contrasts-with:
  - "[[Human vs. LLM Agreement]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[]]"
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

# Inter-Annotator Agreement

> [!definition] **Inter-Annotator Agreement**
> Inter-annotator agreement (IAA) in LLM evaluation measures how consistently different human annotators rate the same model outputs using statistical metrics like Cohen's kappa or Krippendorff's alpha, ensuring that evaluations reflect true quality rather than individual biases. It falls under LLM Evaluation and excludes broader inter-rater reliability concepts from other fields.

> [!attention] **Boundary**
> This concept is distinct from inter-rater reliability in other fields and focuses specifically on evaluations within LLM contexts, excluding technical aspects of metric calculation.

## Core Explanation

Inter-annotator agreement (IAA) is crucial for the validity of human evaluations in large language model (LLM) assessments, ensuring that judgments reflect true quality rather than individual biases. When annotators rate LLM outputs on a holistic scale, such as a five-point Likert scale, IAA often falls between moderate and substantial levels, typically yielding Cohen's kappa scores around 0.3 to 0.5 even after training. This indicates that while some consistency exists among evaluators, significant variability remains, which can undermine the reliability of evaluations based on these ratings.

In contrast, when evaluating LLM outputs against well-defined binary criteria like factual correctness or instruction compliance, IAA tends to be much higher, often exceeding 0.7 in Cohen's kappa scores. This suggests that clear and specific evaluation rubrics lead to more consistent judgments among annotators. The disparity between holistic and categorical evaluations underscores the importance of designing robust and precise evaluation frameworks to minimize variability.

The theoretical underpinnings of IAA draw from reliability theory, which seeks to quantify how consistently a measure performs across different evaluators or occasions. In LLM evaluation, this translates into ensuring that human judgments are not only consistent but also reflective of the model's true performance rather than idiosyncratic biases among annotators. This is particularly critical given the subjective nature of many quality assessments in natural language processing.

Empirical studies have shown that low IAA can lead to unreliable evaluation results, even if statistical significance is achieved due to large sample sizes. For instance, evaluations with kappa scores below 0.3 may still produce statistically significant differences between models but these findings are often driven by annotator variability rather than genuine model performance differences. Therefore, it is imperative that any human evaluation study in LLM contexts reports IAA statistics alongside primary results.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for LLM evaluations, ensuring high inter-annotator agreement (IAA) is crucial to produce reliable and valid assessments of model performance. Designing clear and specific evaluation rubrics that define criteria precisely can significantly enhance IAA, leading to more consistent judgments among annotators. For example, using well-defined binary criteria such as factual correctness or instruction compliance instead of holistic quality ratings on a Likert scale can improve agreement levels from moderate (kappa around 0.3-0.5) to substantial (above 0.7). Ignoring this distinction could result in evaluations that are more reflective of annotator biases than true model performance.

> [!example] **Application 2 — Transparency in reporting**
> Ensuring transparency in the reporting of inter-annotator agreement (IAA) statistics is essential for maintaining credibility and reliability in LLM evaluation studies. Reporting IAA alongside primary results allows readers to assess the consistency among human evaluators, which directly impacts the validity of the findings. Studies with low IAA scores (kappa < 0.3), even if statistically significant due to large sample sizes, should be interpreted cautiously as they may reflect more annotator variability than genuine model performance differences. Failing to report IAA can lead to misleading conclusions about LLM quality.

## Key Distinctions

> [!key-distinction] **Holistic vs Categorical Judgments**
> The distinction between holistic and categorical judgments in inter-annotator agreement (IAA) is critical for understanding the reliability of human evaluations in large language model (LLM) assessments. Holistic judgments, such as rating overall quality on a Likert scale, often yield lower IAA scores due to their subjective nature, typically around 0.3 to 0.5 in Cohen's kappa. In contrast, categorical judgments based on well-defined binary criteria like factual correctness or instruction compliance consistently achieve higher agreement levels, often exceeding 0.7 in kappa scores. This difference highlights the importance of designing evaluation frameworks that minimize subjectivity and enhance consistency among annotators.

## Open Questions

> [!open-question] **Question**
> What are effective strategies for improving IAA in holistic quality evaluations?
>
> *What would resolve it:* Empirical studies comparing different training methods, rubric designs, and feedback mechanisms could provide insights into which approaches most effectively enhance inter-annotator agreement (IAA) in holistic judgments.

> [!open-question] **Question**
> How can we design rubrics that maximize annotator agreement?
>
> *What would resolve it:* Research exploring the impact of various rubric designs on IAA, including detailed criteria definitions and examples, could identify best practices for creating evaluation frameworks that minimize variability among human evaluators.

## Synthesis

Inter-annotator agreement (IAA) is crucial for ensuring the validity and reliability of large language model (LLM) evaluations. By quantifying how consistently different annotators rate the same outputs, IAA helps distinguish true quality differences from individual biases, thereby enhancing the credibility of evaluation results. This concept underscores the importance of designing robust evaluation frameworks that minimize subjectivity and enhance consistency among human evaluators, ultimately contributing to more accurate assessments of LLM performance.

## Connections & Context

**Falls under:** [[LLM Evaluation]]

**Specializes:** [[LLM Evaluation]]

**Contrasts with:** [[Human vs. LLM Agreement]]

**Source:** [[inter-annotator-agreement-in-evals-synthetic-seed-2026-05-22]]
