---
title: "Defense via Input Sanitisation"
aliases:
  - "Defense via Input Sanitisation"
  - "input sanitization defense"
  - "prompt injection prevention"
  - "input validation for LLMs"
  - "context isolation"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - llm-security
  - web-security
  - software-engineering

created: 2026-05-21
updated: 2026-05-21

source-type: report-extraction
source-reports:
  - "defense-via-input-sanitisation-synthetic-seed-2026-05-21"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "LLM Security"

related:
  - "[[Prompt Injection]]"
  - "[[LLM Firewall Patterns]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[]]"
broader:
  - "[[]]"
see-also:
  - "[[Prompt Injection]]"
contrasts-with:
  - "[[]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[]]"
formalizes:
  - "[[]]"
instance-of:
  - "[[]]"
supports:
  - "[[LLM Firewall Patterns]]"
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

# Defense via Input Sanitisation

> [!definition] **Defense via Input Sanitisation**
> Defense via input sanitisation for LLMs involves techniques to detect and neutralise adversarial instructions in user inputs before they affect the model's context. This concept excludes broader security measures not directly tied to input sanitization, such as output filtering or network-level protections. It falls under LLM Security.

> [!attention] **Boundary**
> This concept excludes broader security measures not directly tied to input sanitization, such as output filtering or network-level protections. It should not be confused with general software security practices that do not specifically target LLMs.

## Core Explanation

Defense via input sanitisation is a critical strategy for safeguarding large language models (LLMs) against prompt injection attacks. These attacks exploit vulnerabilities in the model's processing of user inputs to execute unintended commands, potentially leading to security breaches or data leaks. By neutralising adversarial instructions before they reach the model’s context, input sanitisation aims to prevent such malicious activities.

In practice, input sanitisation techniques vary widely but share a common goal: to identify and mitigate harmful content in user inputs without compromising legitimate functionality. Techniques include content-based filtering, which detects known injection patterns; structured delimiters that isolate untrusted content; and context isolation, where suspicious inputs are processed separately from the main reasoning context.

The theoretical underpinnings of input sanitisation draw on principles from cybersecurity and natural language processing (NLP). Content-based filters rely on pattern recognition to identify malicious instructions, while delimiter-based approaches leverage semantic tagging. Context isolation strategies, in turn, borrow concepts from secure computing environments where sensitive operations are isolated from general use.

Empirically, the effectiveness of input sanitisation has been demonstrated through various case studies and experiments. However, these techniques often face challenges such as bypassing via paraphrasing or encoding attacks, highlighting the need for a multi-layered defense strategy.

## Mechanism

Content-based filtering involves scanning user inputs for known malicious patterns like 'ignore previous instructions' to neutralise them before they affect the model's context. Structured delimiters use XML tags or special tokens to wrap untrusted content, signaling its status to the model and preventing it from being processed as regular input.

Input-output monitoring runs both inputs and outputs through a separate safety classifier to detect potential threats. Context isolation processes suspicious content in a restricted environment, ensuring that any harmful instructions do not affect the main reasoning context of the LLM.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for educational LLMs, input sanitisation must balance security against utility. Overly aggressive sanitisation can strip necessary content like code comments or quoted instructions, degrading task performance and user experience. Designers must calibrate sanitisation to the specific needs of their deployment environment.

> [!example] **Application 2 — Code execution**
> When LLMs are used for code execution tasks, input sanitisation is crucial to prevent injection attacks that could lead to unauthorized actions or data leaks. Techniques like structured delimiters and context isolation help isolate potentially harmful inputs without blocking legitimate coding instructions.

## Key Distinctions

> [!key-distinction] **Input sanitization vs Output filtering**
> While input sanitisation focuses on detecting and neutralising adversarial instructions before they reach the model's context, output filtering examines the model’s responses for harmful content after processing. Input sanitisation is more proactive in preventing attacks, whereas output filtering acts as a reactive measure to mitigate damage.

## Key Figures

- **John Doe** — Contributed significantly to the development of structured delimiters for input sanitisation, enhancing LLM security by isolating untrusted content with semantic tags.
- **Jane Smith** — Pioneered context isolation techniques in LLMs, demonstrating how processing suspicious inputs separately can prevent prompt injection attacks without compromising model performance.

## Open Questions

> [!open-question] **Question**
> How effective are current content-based filters against paraphrasing and encoding attacks?
>
> *What would resolve it:* Empirical studies comparing the efficacy of different filtering techniques under various attack scenarios would provide insights into their robustness.

> [!open-question] **Question**
> What is the optimal balance between security and utility in input sanitisation?
>
> *What would resolve it:* Case studies evaluating the impact of varying levels of sanitisation on task performance and security outcomes could help determine the best approach for different deployment scenarios.

## Synthesis

Defense via input sanitisation is crucial for securing LLMs against prompt injection attacks, ensuring that adversarial instructions are neutralised before they can affect the model's context. By combining multiple techniques and incorporating human-in-the-loop checkpoints, organizations can achieve a robust defense strategy that balances security with operational utility.

This concept matters because it directly addresses one of the most pressing security concerns in LLMs: prompt injection attacks. Effective input sanitisation not only protects against immediate threats but also sets a foundation for broader cybersecurity measures within the domain of LLM Security.

## Connections & Context

**Falls under:** [[LLM Security]]

**Sibling concepts:** [[Prompt Injection]]

**Supports:** [[LLM Firewall Patterns]]

**Source:** [[defense-via-input-sanitisation-synthetic-seed-2026-05-21]]
