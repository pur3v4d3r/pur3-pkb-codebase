---
batch_name: custom-16-research-methods
batch_date: 2026-04-26
default_domain: research-methods
default_confidence: high
notes: |
  Custom seeding batch 16: research-methods constructs covering
  inferential-statistics interpretation and the open-science reform movement.
---

# Batch: Research Methods

## Effect Size and Practical Significance

- domain: research-methods
- secondary_domains: [statistics, meta-science]
- aliases: [effect size, practical significance, magnitude of effect]
- broader: [inferential-statistics]
- related: [statistical-significance, p-value, confidence-interval, meta-analysis]
- prerequisites: [inferential-statistics]
- confidence: high

**definition**: Effect Size and Practical Significance refers jointly to the standardized magnitude of an empirical relationship — Cohen's d, Pearson's r, odds ratios, and related metrics — and to the substantive judgment of whether that magnitude is large enough to matter in the relevant theoretical or applied context, in contrast to the dichotomous reject/retain output of null-hypothesis significance testing.

**key_claim**: The central methodological argument for foregrounding Effect Size and Practical Significance is that statistical significance is confounded with sample size: with a large enough N, trivially small effects achieve p < .05, while with a small N, theoretically important effects fail to reach significance, so reporting effect sizes with confidence intervals — as the APA, AERA, and most journal standards now require — is the only way to separate the strength of evidence from the strength of effect.

**warning**: Effect Size and Practical Significance is frequently misapplied through Cohen's small/medium/large benchmarks (d = .2/.5/.8) as if they were universal thresholds; Cohen explicitly proposed them as defaults for cases where no domain-specific calibration exists, and reading a d = .2 as "small" in a context like medical mortality or educational achievement gaps inverts the ordinary meaning of practical significance, which is properly determined by domain, comparison class, and cost-benefit structure rather than by ritualized cutoffs.

## Open Science Practices

- domain: research-methods
- secondary_domains: [meta-science, philosophy-of-science]
- aliases: [open science, OSP, reproducible research practices]
- broader: [meta-science]
- related: [preregistration, replication-crisis, registered-reports, p-hacking]
- prerequisites: [inferential-statistics, replication-crisis]
- confidence: high

**definition**: Open Science Practices is a cluster of methodological reforms — preregistration, registered reports, open data, open materials, open code, and open access publishing — adopted in response to the replication crisis to constrain researcher degrees of freedom, enable independent verification, and align the published record more closely with the underlying empirical reality.

**key_claim**: Open Science Practices' most evidentially supported component is preregistration combined with the registered-reports format: registered-reports studies show a dramatically lower rate of statistically significant "positive" findings (roughly 40% versus 90% in matched conventional samples), suggesting that the conventional literature's success rate is driven less by veridical signal than by selective reporting and analytic flexibility that Open Science Practices are specifically designed to remove.

**warning**: Open Science Practices are sometimes treated as procedural fixes that automatically produce credible science, but several of their components can be performed in ways that satisfy the letter without the spirit: vague preregistrations are common and provide little constraint, "open" data are often released in formats that resist independent reanalysis, and exploratory work mislabeled as confirmatory passes through registered-report systems whose protections depend on analyst honesty about the inferential intent of each test.
