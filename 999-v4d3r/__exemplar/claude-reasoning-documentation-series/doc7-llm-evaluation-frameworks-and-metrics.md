---
id: 20260516000015C
title: "LLM Evaluation Frameworks and Metrics"
subtitle: "Systematic Assessment of Language Model Capabilities, Alignment, and Robustness"
series: "Claude Reasoning Documentation Series"
doc_number: 7
tier: 2
phase: 2
version: 2.0.0
status: production
created: 2026-05-16
modified: 2026-05-16
tags:
  - llm-evaluation
  - benchmarks
  - alignment-metrics
  - llm-as-judge
  - evaluation-methodology
  - production-monitoring
aliases:
  - "Doc7"
  - "Evaluation Frameworks"
  - "LLM Metrics"
certainty: established
doc_series_position: 7/10
related_docs:
  - doc1-llm-reasoning-techniques-operational-manual
  - doc3-advanced-reasoning-architectures-theory-to-practice
  - doc6-advanced-prompt-engineering-techniques
word_count: ~5700
code_blocks: 32
citations: 15
wiki_links: 28
---

# LLM Evaluation Frameworks and Metrics

> [!abstract] Document Overview
> Evaluation is the empirical foundation on which every claim about [[large-language-model]] capability rests. Without rigorous, bias-aware measurement, claims of improvement are anecdotal. This document provides a production-ready taxonomy of evaluation methodologies — from standardized benchmarks to custom rubric design, from human preference studies to automated LLM-as-Judge systems, and from static test suites to continuous production monitoring. Code examples throughout are designed for immediate integration into evaluation pipelines.
>
> **Cross-references**: → [[doc1-llm-reasoning-techniques-operational-manual]] (reasoning benchmark data), → [[doc3-advanced-reasoning-architectures-theory-to-practice]] (empirical analysis methodology), → [[doc6-advanced-prompt-engineering-techniques]] (prompt optimization requires evaluation)

---

## Part 1: Evaluation Taxonomy

[**Evaluation-Taxonomy-Definition**:: A systematic categorization of measurement dimensions along which LLM performance can be assessed, providing a framework for selecting appropriate metrics for any evaluation task.]

The evaluation landscape for [[large-language-model|LLMs]] can be organized along four orthogonal axes: **capability**, **alignment**, **safety**, and **efficiency**. Each axis contains sub-dimensions that interact in practice.

### 1.1 Capability Dimensions

[**Capability-Evaluation**:: Assessment of what a model can do — the breadth and depth of its knowledge and problem-solving abilities.]

```python
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any


class CapabilityDomain(Enum):
    """Primary capability domains for LLM evaluation."""
    KNOWLEDGE = auto()          # Factual recall, domain expertise
    REASONING = auto()          # Multi-step inference, logic, math
    LANGUAGE = auto()           # Fluency, coherence, grammar
    INSTRUCTION_FOLLOWING = auto()  # Adherence to explicit directives
    CODING = auto()             # Code generation and debugging
    TOOL_USE = auto()           # API calls, function invocation
    MULTIMODAL = auto()         # Cross-modal reasoning (if applicable)
    LONG_CONTEXT = auto()       # Retrieval and reasoning over long inputs


class AlignmentDomain(Enum):
    """Alignment sub-dimensions."""
    HELPFULNESS = auto()        # Does it assist the user effectively?
    HARMLESSNESS = auto()       # Does it avoid producing harmful outputs?
    HONESTY = auto()            # Does it avoid deception, including via omission?
    CALIBRATION = auto()        # Does expressed confidence match accuracy?


class SafetyDomain(Enum):
    """Safety measurement axes."""
    TOXICITY = auto()           # Hate speech, harassment, slurs
    BIAS = auto()               # Demographic disparities in outputs
    PRIVACY = auto()            # PII leakage, data extraction
    ROBUSTNESS = auto()         # Resistance to adversarial prompts


class EfficiencyDomain(Enum):
    """Efficiency metrics (resource consumption)."""
    LATENCY = auto()            # Time-to-first-token, total latency
    THROUGHPUT = auto()         # Tokens/second at scale
    COST = auto()               # API cost per task completion
    MEMORY = auto()             # Peak GPU memory for inference


@dataclass
class EvaluationSpec:
    """Complete specification for an evaluation campaign.
    
    Attributes:
        name: Human-readable campaign identifier.
        capabilities: Capability domains to assess.
        alignment: Alignment dimensions to measure.
        safety: Safety dimensions to probe.
        efficiency: Efficiency metrics to record.
        sample_size: Number of evaluation instances per sub-task.
        confidence_level: Statistical confidence target (e.g., 0.95).
    """
    name: str
    capabilities: list[CapabilityDomain]
    alignment: list[AlignmentDomain]
    safety: list[SafetyDomain]
    efficiency: list[EfficiencyDomain]
    sample_size: int = 500
    confidence_level: float = 0.95
    notes: str = ""

    def total_dimensions(self) -> int:
        """Return total number of measurement dimensions."""
        return (len(self.capabilities) + len(self.alignment) +
                len(self.safety) + len(self.efficiency))
```

### 1.2 Evaluation Levels

```python
class EvaluationLevel(Enum):
    """Granularity levels at which evaluation is applied."""
    INSTANCE = "instance"       # Single prompt-response pair
    TASK = "task"               # Aggregated over a task dataset
    BENCHMARK = "benchmark"     # Multi-task standardized suite
    CAMPAIGN = "campaign"       # Full multi-dimension evaluation run
    PRODUCTION = "production"   # Continuous monitoring in deployment


@dataclass
class EvaluationResult:
    """Structured result from any evaluation level."""
    level: EvaluationLevel
    dimension: str
    score: float
    confidence_interval: tuple[float, float]
    sample_count: int
    metadata: dict[str, Any] = field(default_factory=dict)

    def is_significant(self, baseline: float, alpha: float = 0.05) -> bool:
        """Return True if the score is significantly different from baseline.
        
        Uses the confidence interval: if baseline falls outside the CI,
        the difference is considered statistically significant at level alpha.
        
        Args:
            baseline: Reference score (e.g., prior model version).
            alpha: Significance level (default 0.05 → 95% CI).
        
        Returns:
            True if baseline is outside the confidence interval.
        """
        lo, hi = self.confidence_interval
        return not (lo <= baseline <= hi)
```

---

## Part 2: Standard Benchmarks

[**Benchmark-Contamination**:: The phenomenon where model training data contains examples from evaluation benchmarks, inflating reported performance. A primary validity threat in LLM evaluation.]

[**Benchmark-Taxonomy**:: Standardized test suites for measuring LLM capabilities across diverse domains.]

The benchmark ecosystem spans knowledge, code, mathematics, and open-ended generation. Matching benchmark to evaluation goal is the practitioner's primary decision.

### 2.1 Knowledge and Reasoning Benchmarks

**MMLU (Massive Multitask Language Understanding)** — Hendrycks et al. (2021) — 57 subjects, 14,000 multiple-choice questions spanning STEM, humanities, social sciences. Standard metric: **accuracy**. [**MMLU-Score**:: The percentage of correct answers across all 57 subjects, with macro-average over subject groups to avoid domain imbalance.]

**BIG-Bench** — Srivastava et al. (2022) — 204 tasks contributed by 450+ researchers, probing capabilities that are either hard for current models or important for safety. Includes **BIG-Bench Hard** (BBH), a 23-task subset where chain-of-thought prompting substantially improves performance.

**ARC (AI2 Reasoning Challenge)** — Clark et al. (2018) — Grade-school science questions split into Easy and Challenge partitions. ARC-Challenge requires world knowledge beyond simple pattern matching.

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Callable


@dataclass
class BenchmarkConfig:
    """Configuration for a benchmark evaluation run.
    
    Args:
        name: Benchmark identifier (e.g., "mmlu", "arc-challenge").
        data_path: Path to benchmark dataset (JSONL format).
        metric: Callable that computes score from predictions and labels.
        few_shot_k: Number of in-context examples (0 for zero-shot).
        chain_of_thought: Whether to prompt for step-by-step reasoning.
        subject_filter: Optional subset of subjects/tasks to evaluate.
    """
    name: str
    data_path: Path
    metric: Callable[[list[str], list[str]], float]
    few_shot_k: int = 5
    chain_of_thought: bool = False
    subject_filter: list[str] | None = None


class BenchmarkRunner:
    """Execute standardized benchmark evaluations.
    
    Handles dataset loading, few-shot prompt construction, model querying,
    and metric computation with optional per-subject breakdown.
    
    Example:
        >>> runner = BenchmarkRunner(model_fn=my_model)
        >>> result = runner.run(mmlu_config)
        >>> print(f"MMLU accuracy: {result.score:.3f}")
    """

    def __init__(self, model_fn: Callable[[str], str]) -> None:
        """
        Args:
            model_fn: Function mapping prompt string → model response string.
        """
        self._model = model_fn
        self._results: list[EvaluationResult] = []

    def run(self, config: BenchmarkConfig) -> EvaluationResult:
        """Execute a benchmark and return an aggregated result.
        
        Args:
            config: Benchmark configuration.
        
        Returns:
            EvaluationResult with score, CI, and per-subject breakdown.
        
        Raises:
            FileNotFoundError: If config.data_path does not exist.
        """
        if not config.data_path.exists():
            raise FileNotFoundError(f"Benchmark data not found: {config.data_path}")

        records = self._load_records(config)
        if config.subject_filter:
            records = [r for r in records if r.get("subject") in config.subject_filter]

        few_shot_pool = records[:config.few_shot_k]
        eval_records = records[config.few_shot_k:]

        predictions, labels = [], []
        for record in eval_records:
            prompt = self._build_prompt(record, few_shot_pool, config)
            response = self._model(prompt)
            predictions.append(self._extract_answer(response, record))
            labels.append(record["answer"])

        score = config.metric(predictions, labels)
        ci = self._bootstrap_ci(predictions, labels, config.metric)

        return EvaluationResult(
            level=EvaluationLevel.BENCHMARK,
            dimension=config.name,
            score=score,
            confidence_interval=ci,
            sample_count=len(eval_records),
            metadata={"few_shot_k": config.few_shot_k,
                      "chain_of_thought": config.chain_of_thought},
        )

    def _load_records(self, config: BenchmarkConfig) -> list[dict]:
        """Load JSONL records from disk."""
        records = []
        with open(config.data_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        return records

    def _build_prompt(
        self,
        record: dict,
        few_shot_pool: list[dict],
        config: BenchmarkConfig,
    ) -> str:
        """Construct a few-shot (or zero-shot) prompt for the record."""
        lines = []
        for ex in few_shot_pool:
            lines.append(self._format_example(ex, include_answer=True,
                                               chain_of_thought=config.chain_of_thought))
        lines.append(self._format_example(record, include_answer=False,
                                           chain_of_thought=config.chain_of_thought))
        return "\n\n".join(lines)

    def _format_example(
        self,
        record: dict,
        include_answer: bool,
        chain_of_thought: bool,
    ) -> str:
        """Format a single benchmark record as a prompt example."""
        q = record["question"]
        choices = "\n".join(f"({k}) {v}" for k, v in record["choices"].items())
        prompt = f"Question: {q}\n{choices}\nAnswer:"
        if include_answer:
            if chain_of_thought and "chain_of_thought" in record:
                prompt += f" {record['chain_of_thought']}\nFinal Answer: {record['answer']}"
            else:
                prompt += f" {record['answer']}"
        return prompt

    @staticmethod
    def _extract_answer(response: str, record: dict) -> str:
        """Extract the model's chosen answer letter from its response."""
        choices = list(record["choices"].keys())
        for choice in choices:
            if f"({choice})" in response or response.strip().startswith(choice):
                return choice
        # FALLBACK: return first character if it's a valid choice
        first = response.strip()[0].upper() if response.strip() else ""
        return first if first in choices else choices[0]

    @staticmethod
    def _bootstrap_ci(
        predictions: list[str],
        labels: list[str],
        metric: Callable,
        n_bootstrap: int = 1000,
        alpha: float = 0.05,
    ) -> tuple[float, float]:
        """Compute bootstrap confidence interval for the metric."""
        import random
        n = len(predictions)
        scores = []
        for _ in range(n_bootstrap):
            indices = [random.randint(0, n - 1) for _ in range(n)]
            boot_pred = [predictions[i] for i in indices]
            boot_label = [labels[i] for i in indices]
            scores.append(metric(boot_pred, boot_label))
        scores.sort()
        lo = scores[int(alpha / 2 * n_bootstrap)]
        hi = scores[int((1 - alpha / 2) * n_bootstrap)]
        return lo, hi
```

### 2.2 Code and Math Benchmarks

**HumanEval** — Chen et al. (2021) — 164 Python programming problems with unit tests. Metric: **pass@k** (probability that at least one of k generated solutions passes all tests).

**GSM8K** — Cobbe et al. (2021) — 8,500 grade-school math word problems requiring multi-step arithmetic. Strong test of [[chain-of-thought]] faithfulness.

**MATH** — Hendrycks et al. (2021) — 12,500 competition-level math problems across 7 subjects (algebra, geometry, number theory, etc.). State-of-the-art models score significantly below humans.

```python
import ast
import signal
from typing import Any


def pass_at_k(n: int, c: int, k: int) -> float:
    """Compute the unbiased pass@k estimator (Chen et al. 2021).
    
    Given n total generated samples of which c pass all tests,
    computes the probability that at least one of k randomly
    selected samples passes — without resampling.
    
    Args:
        n: Total number of generated samples.
        c: Number of samples that pass all unit tests.
        k: Number of samples selected (the @k parameter).
    
    Returns:
        Estimated probability that at least one of k samples passes.
    
    Example:
        >>> pass_at_k(n=10, c=3, k=1)
        0.3
        >>> pass_at_k(n=10, c=3, k=5)
        ~0.833
    """
    if n - c < k:
        return 1.0
    # Numerically stable: 1 - prod((n-c-i)/(n-i) for i in range(k))
    result = 1.0
    for i in range(k):
        result *= (n - c - i) / (n - i)
    return 1.0 - result


def safe_execute(code: str, test: str, timeout: int = 5) -> bool:
    """Execute generated code against a test case with a timeout.
    
    Args:
        code: Generated Python function code.
        test: Unit test assertion string.
        timeout: Maximum execution seconds.
    
    Returns:
        True if the test passes, False on any error or timeout.
    
    # NOTE: This uses SIGALRM for Unix-based timeouts. On Windows,
    # replace with subprocess + timeout parameter.
    """
    def _handler(signum: int, frame: Any) -> None:
        raise TimeoutError("Execution exceeded timeout")

    try:
        # Compile first — catches syntax errors without execution
        compile(code + "\n" + test, "<string>", "exec")
        signal.signal(signal.SIGALRM, _handler)
        signal.alarm(timeout)
        exec(code + "\n" + test, {})  # noqa: S102
        signal.alarm(0)
        return True
    except Exception:
        signal.alarm(0)
        return False
```

---

## Part 3: Reasoning-Specific Evaluation

[**Reasoning-Faithfulness**:: The degree to which a model's stated reasoning chain (chain-of-thought) accurately reflects the computational steps that produced its final answer, rather than being post-hoc rationalization.]

Standard accuracy metrics are insufficient for [[chain-of-thought]] and [[multi-step-reasoning]] systems. Three additional dimensions matter: **step correctness**, **trace quality**, and **reasoning faithfulness**.

### 3.1 Step-Level Correctness

```python
from dataclasses import dataclass
from enum import Enum


class StepVerdict(Enum):
    """Verdict for a single reasoning step."""
    CORRECT = "correct"
    MINOR_ERROR = "minor_error"     # Recoverable; correct answer may still emerge
    MAJOR_ERROR = "major_error"     # Invalidates subsequent steps
    IRRELEVANT = "irrelevant"       # Off-topic but not harmful
    MISSING = "missing"             # Required step absent


@dataclass
class ReasoningStep:
    """A single identified step in a chain-of-thought trace.
    
    Attributes:
        index: Step position in the trace.
        content: The text of this step.
        verdict: Correctness verdict.
        explanation: Rationale for the verdict (for LLM-as-judge).
        is_critical: Whether this step is necessary for the final answer.
    """
    index: int
    content: str
    verdict: StepVerdict
    explanation: str = ""
    is_critical: bool = True


@dataclass
class ReasoningTraceEvaluation:
    """Complete evaluation of a reasoning trace.
    
    Attributes:
        steps: Individual step evaluations.
        final_answer_correct: Whether the final answer is correct.
        first_error_index: Index of the first step with a major error (-1 if none).
        faithfulness_score: Float in [0, 1] — does the trace support the answer?
        completeness_score: Float in [0, 1] — are all required steps present?
    """
    steps: list[ReasoningStep]
    final_answer_correct: bool
    first_error_index: int
    faithfulness_score: float
    completeness_score: float

    def step_accuracy(self) -> float:
        """Proportion of steps with CORRECT verdict."""
        if not self.steps:
            return 0.0
        correct = sum(1 for s in self.steps if s.verdict == StepVerdict.CORRECT)
        return correct / len(self.steps)

    def critical_step_accuracy(self) -> float:
        """Proportion of CRITICAL steps with CORRECT verdict."""
        critical = [s for s in self.steps if s.is_critical]
        if not critical:
            return 1.0
        correct = sum(1 for s in critical if s.verdict == StepVerdict.CORRECT)
        return correct / len(critical)

    def composite_score(
        self,
        w_final: float = 0.4,
        w_steps: float = 0.3,
        w_faithful: float = 0.2,
        w_complete: float = 0.1,
    ) -> float:
        """Weighted composite reasoning score.
        
        Args:
            w_final: Weight for final answer correctness.
            w_steps: Weight for critical step accuracy.
            w_faithful: Weight for faithfulness.
            w_complete: Weight for completeness.
        
        Returns:
            Composite score in [0, 1].
        """
        return (
            w_final * float(self.final_answer_correct)
            + w_steps * self.critical_step_accuracy()
            + w_faithful * self.faithfulness_score
            + w_complete * self.completeness_score
        )
```

### 3.2 Faithfulness Measurement

[**Counterfactual-Faithfulness**:: A faithfulness probe that alters a fact in the problem statement and checks whether the reasoning trace updates accordingly. A faithful reasoner's trace changes; a non-faithful reasoner may produce the same trace regardless of the fact change.]

```python
from typing import Callable


class FaithfulnessProbe:
    """Measures whether a model's reasoning traces are faithful.
    
    Implements three faithfulness tests:
    1. Counterfactual — change a fact; check if trace changes accordingly.
    2. Intervention — remove a step's conclusion; check if model re-derives it.
    3. Self-consistency — compare traces across multiple generations.
    
    Based on methods from Lanham et al. (2023) and Turpin et al. (2023).
    """

    def __init__(self, model_fn: Callable[[str], str]) -> None:
        self._model = model_fn

    def counterfactual_faithfulness(
        self,
        original_prompt: str,
        counterfactual_prompt: str,
        answer_extractor: Callable[[str], str],
    ) -> float:
        """Measure faithfulness via counterfactual consistency.
        
        Args:
            original_prompt: The base problem.
            counterfactual_prompt: Same problem with a key fact altered.
            answer_extractor: Extracts the final answer from a response.
        
        Returns:
            Faithfulness score: 1.0 if counterfactual changes the answer
            as expected, 0.0 if the model gives the same answer regardless.
        """
        original_response = self._model(original_prompt)
        counterfactual_response = self._model(counterfactual_prompt)

        original_answer = answer_extractor(original_response)
        counterfactual_answer = answer_extractor(counterfactual_response)

        # Faithful reasoning produces different answers for different facts
        return 1.0 if original_answer != counterfactual_answer else 0.0

    def self_consistency_faithfulness(
        self,
        prompt: str,
        answer_extractor: Callable[[str], str],
        n_samples: int = 10,
    ) -> float:
        """Estimate faithfulness via self-consistency (Wang et al. 2023).
        
        Args:
            prompt: The problem prompt.
            answer_extractor: Final answer extraction function.
            n_samples: Number of independent reasoning paths.
        
        Returns:
            Proportion of samples matching the plurality answer (consistency score).
        """
        from collections import Counter
        answers = [answer_extractor(self._model(prompt)) for _ in range(n_samples)]
        most_common_count = Counter(answers).most_common(1)[0][1]
        return most_common_count / n_samples
```

---

## Part 4: Human Alignment Metrics

[**RLHF-Win-Rate**:: The proportion of head-to-head comparisons in which a model's response is preferred by human raters over a baseline. The primary metric in reinforcement learning from human feedback systems.]

[**Bradley-Terry-Model**:: A probabilistic model for pairwise comparison data that converts win/loss records into consistent scalar ability scores. The foundation of Elo-based LLM leaderboards.]

Human alignment evaluation requires preference data, typically collected via pairwise comparison: raters select which of two responses better satisfies a criterion (helpfulness, honesty, harmlessness).

### 4.1 Elo Rating Systems

```python
import math
from collections import defaultdict


class EloRatingSystem:
    """Elo-based rating system for LLM evaluation.
    
    Converts pairwise preference judgments into scalar Elo ratings,
    enabling consistent ranking across models even without direct
    head-to-head comparisons between every model pair.
    
    Used by Chatbot Arena (Zheng et al. 2023) and similar leaderboards.
    
    Example:
        >>> elo = EloRatingSystem()
        >>> elo.record_match("model_a", "model_b", winner="model_a")
        >>> elo.record_match("model_b", "model_c", winner="model_b")
        >>> rankings = elo.get_rankings()
    """

    K: float = 32.0  # K-factor: controls rating update magnitude
    INITIAL_RATING: float = 1000.0

    def __init__(self) -> None:
        self._ratings: dict[str, float] = defaultdict(
            lambda: self.INITIAL_RATING
        )
        self._match_counts: dict[str, int] = defaultdict(int)

    def expected_score(self, rating_a: float, rating_b: float) -> float:
        """Compute the expected win probability for model A vs model B.
        
        Based on the logistic function of the rating difference.
        
        Args:
            rating_a: Elo rating of model A.
            rating_b: Elo rating of model B.
        
        Returns:
            Probability in (0, 1) that A beats B.
        """
        return 1.0 / (1.0 + math.pow(10, (rating_b - rating_a) / 400.0))

    def record_match(
        self,
        model_a: str,
        model_b: str,
        winner: str | None,  # None = tie
    ) -> None:
        """Update ratings after a pairwise comparison.
        
        Args:
            model_a: First model identifier.
            model_b: Second model identifier.
            winner: The model that won ("model_a", "model_b", or None for tie).
        """
        ra = self._ratings[model_a]
        rb = self._ratings[model_b]
        ea = self.expected_score(ra, rb)
        eb = 1.0 - ea

        if winner == model_a:
            sa, sb = 1.0, 0.0
        elif winner == model_b:
            sa, sb = 0.0, 1.0
        else:  # tie
            sa = sb = 0.5

        self._ratings[model_a] = ra + self.K * (sa - ea)
        self._ratings[model_b] = rb + self.K * (sb - eb)
        self._match_counts[model_a] += 1
        self._match_counts[model_b] += 1

    def get_rankings(self) -> list[tuple[str, float, int]]:
        """Return models sorted by rating descending.
        
        Returns:
            List of (model_name, elo_rating, match_count) tuples.
        """
        return sorted(
            [(m, r, self._match_counts[m]) for m, r in self._ratings.items()],
            key=lambda x: x[1],
            reverse=True,
        )

    def win_rate(self, model_a: str, model_b: str) -> float:
        """Predicted win rate of model_a against model_b.
        
        Args:
            model_a: Challenger model.
            model_b: Baseline model.
        
        Returns:
            Win probability in (0, 1).
        """
        return self.expected_score(self._ratings[model_a], self._ratings[model_b])
```

### 4.2 Preference Model Training

```python
import torch
import torch.nn as nn


class RewardModel(nn.Module):
    """Reward model for RLHF preference learning.
    
    Scores a response given a prompt. Trained via the Bradley-Terry
    loss on pairwise human preference data: preferred responses should
    receive higher scalar rewards than rejected responses.
    
    Args:
        backbone: Pre-trained language model backbone (transformers).
        hidden_dim: Dimension of the backbone's hidden states.
    """

    def __init__(self, backbone: nn.Module, hidden_dim: int) -> None:
        super().__init__()
        self.backbone = backbone
        self.reward_head = nn.Linear(hidden_dim, 1)

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """Compute scalar reward for a tokenized prompt+response.
        
        Args:
            input_ids: Token IDs, shape (batch, seq_len).
            attention_mask: Attention mask, shape (batch, seq_len).
        
        Returns:
            Scalar reward scores, shape (batch,).
        """
        outputs = self.backbone(input_ids=input_ids, attention_mask=attention_mask)
        # Use the last token's hidden state as the reward representation
        last_hidden = outputs.last_hidden_state[:, -1, :]
        return self.reward_head(last_hidden).squeeze(-1)

    @staticmethod
    def bradley_terry_loss(
        reward_chosen: torch.Tensor,
        reward_rejected: torch.Tensor,
    ) -> torch.Tensor:
        """Bradley-Terry pairwise ranking loss.
        
        Maximizes the log-probability that the chosen response has
        higher reward than the rejected response.
        
        Args:
            reward_chosen: Rewards for preferred responses.
            reward_rejected: Rewards for rejected responses.
        
        Returns:
            Scalar loss value.
        """
        # log σ(r_chosen - r_rejected)
        return -nn.functional.logsigmoid(reward_chosen - reward_rejected).mean()
```

---

## Part 5: LLM-as-Judge Patterns

[**LLM-as-Judge**:: Using a capable language model to evaluate the quality of another model's outputs, replacing or augmenting human raters. Enables scalable evaluation at the cost of potential bias from the judge model's own preferences.]

Zheng et al. (2023) demonstrated that GPT-4 as judge achieves over 80% agreement with human evaluators, making LLM-as-Judge practical for large-scale evaluation. Three canonical patterns exist.

### 5.1 Direct Assessment

```python
from __future__ import annotations

from dataclasses import dataclass


DIRECT_ASSESSMENT_TEMPLATE = """\
You are an expert evaluator of AI assistant responses.

## Evaluation Criteria
{criteria}

## Prompt Given to the Assistant
{prompt}

## Assistant's Response
{response}

## Evaluation Instructions
Score the response on each criterion from 1 to 10.
Provide a brief rationale for each score.
Then provide an overall score from 1 to 10.

Respond ONLY in this JSON format:
{{
  "scores": {{
    "<criterion_name>": {{
      "score": <int 1-10>,
      "rationale": "<string>"
    }}
  }},
  "overall_score": <int 1-10>,
  "overall_rationale": "<string>"
}}
"""


@dataclass
class DirectAssessmentJudge:
    """LLM-as-Judge using direct scoring against explicit criteria.
    
    Attributes:
        judge_model_fn: Function calling the judge LLM.
        criteria: Dict mapping criterion names to descriptions.
        temperature: Sampling temperature for the judge (0.0 for determinism).
    """
    judge_model_fn: object  # Callable[[str], str]
    criteria: dict[str, str]
    temperature: float = 0.0

    def evaluate(self, prompt: str, response: str) -> dict:
        """Score a response against the configured criteria.
        
        Args:
            prompt: The user prompt that elicited the response.
            response: The model's response to evaluate.
        
        Returns:
            Parsed JSON dict with per-criterion scores and rationales.
        
        Raises:
            ValueError: If judge output is not valid JSON.
        """
        import json

        criteria_str = "\n".join(
            f"- **{k}**: {v}" for k, v in self.criteria.items()
        )
        judge_prompt = DIRECT_ASSESSMENT_TEMPLATE.format(
            criteria=criteria_str,
            prompt=prompt,
            response=response,
        )
        raw = self.judge_model_fn(judge_prompt)
        try:
            # Strip markdown code fences if present
            clean = raw.strip().removeprefix("```json").removesuffix("```").strip()
            return json.loads(clean)
        except json.JSONDecodeError as e:
            raise ValueError(f"Judge returned non-JSON output: {raw[:200]}") from e
```

### 5.2 Pairwise Comparison

```python
PAIRWISE_TEMPLATE = """\
You are an expert evaluator. Compare two AI assistant responses to the same prompt.

## Prompt
{prompt}

## Response A
{response_a}

## Response B
{response_b}

## Task
Which response is better? Consider: helpfulness, accuracy, clarity, and safety.
Account for position bias by focusing on content quality, not presentation order.

Respond in this JSON format:
{{
  "winner": "A" | "B" | "tie",
  "confidence": "low" | "medium" | "high",
  "rationale": "<string>",
  "dimension_verdicts": {{
    "helpfulness": "A" | "B" | "tie",
    "accuracy": "A" | "B" | "tie",
    "clarity": "A" | "B" | "tie",
    "safety": "A" | "B" | "tie"
  }}
}}
"""


class PairwiseJudge:
    """LLM-as-Judge via pairwise comparison.
    
    Implements position-debiased comparison by running each pair
    twice with the order of A and B swapped. If the results conflict,
    the verdict is "tie".
    
    Example:
        >>> judge = PairwiseJudge(judge_model_fn=gpt4_fn)
        >>> result = judge.compare(prompt, response_1, response_2)
        >>> print(result["winner"])  # "A", "B", or "tie"
    """

    def __init__(self, judge_model_fn) -> None:
        self._judge = judge_model_fn

    def compare(
        self,
        prompt: str,
        response_a: str,
        response_b: str,
    ) -> dict:
        """Position-debiased pairwise comparison.
        
        Args:
            prompt: The shared prompt.
            response_a: First model's response.
            response_b: Second model's response.
        
        Returns:
            Debiased judgment dict with winner, confidence, rationale.
        """
        import json

        def call(ra: str, rb: str) -> dict:
            raw = self._judge(PAIRWISE_TEMPLATE.format(
                prompt=prompt, response_a=ra, response_b=rb
            ))
            clean = raw.strip().removeprefix("```json").removesuffix("```").strip()
            return json.loads(clean)

        # Forward order: A=response_a, B=response_b
        forward = call(response_a, response_b)
        # Reverse order: A=response_b, B=response_a — swap labels in result
        backward_raw = call(response_b, response_a)
        backward_winner = {"A": "B", "B": "A", "tie": "tie"}[backward_raw["winner"]]

        # Debiased verdict: only agree if both orderings agree
        if forward["winner"] == backward_winner and forward["winner"] != "tie":
            winner = forward["winner"]
            confidence = forward["confidence"]
        else:
            winner = "tie"
            confidence = "low"

        return {
            "winner": winner,
            "confidence": confidence,
            "rationale": forward["rationale"],
            "position_bias_detected": forward["winner"] != backward_winner,
        }
```

### 5.3 Reference-Free Evaluation

```python
REFERENCE_FREE_TEMPLATE = """\
You are evaluating the quality of an AI-generated response without access to
a reference answer. Assess the response purely on internal quality signals.

## Prompt
{prompt}

## Response
{response}

## Evaluation Dimensions

**Coherence** (1-5): Is the response internally consistent? Does it follow
logically from premise to conclusion without contradiction?

**Groundedness** (1-5): Does the response make only claims that are plausible
given general world knowledge? Are speculative claims flagged?

**Instruction Adherence** (1-5): Does the response answer what was asked,
in the format and length implicitly or explicitly required?

**Conciseness** (1-5): Is information density appropriate? Is there padding
or unnecessary repetition?

Respond in JSON:
{{
  "coherence": {{"score": <1-5>, "rationale": "<string>"}},
  "groundedness": {{"score": <1-5>, "rationale": "<string>"}},
  "instruction_adherence": {{"score": <1-5>, "rationale": "<string>"}},
  "conciseness": {{"score": <1-5>, "rationale": "<string>"}},
  "composite": <float, weighted average>
}}
"""
```

---

## Part 6: Custom Evaluation Design

[**Rubric-Based-Evaluation**:: Structured scoring guides that specify observable criteria and anchoring examples at each score level, enabling consistent evaluation across raters and runs.]

[**Task-Decomposition-Evaluation**:: Breaking a complex task into atomic sub-tasks, evaluating each independently, then aggregating — improving precision and diagnosability.]

### 6.1 Rubric Construction

```python
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class RubricLevel:
    """A single score level in an evaluation rubric.
    
    Attributes:
        score: Numeric value for this level.
        label: Short name (e.g., "Excellent", "Acceptable", "Poor").
        description: Observable criteria distinguishing this level.
        examples: Representative response excerpts at this level.
    """
    score: int
    label: str
    description: str
    examples: list[str] = field(default_factory=list)


@dataclass
class EvaluationRubric:
    """Complete evaluation rubric for a single dimension.
    
    Example:
        >>> rubric = EvaluationRubric(
        ...     dimension="Reasoning Clarity",
        ...     levels=[
        ...         RubricLevel(5, "Excellent", "All steps shown, no gaps..."),
        ...         RubricLevel(3, "Acceptable", "Major steps shown, minor gaps..."),
        ...         RubricLevel(1, "Poor", "Steps missing or contradictory..."),
        ...     ],
        ...     weight=0.4,
        ... )
    """
    dimension: str
    levels: list[RubricLevel]
    weight: float = 1.0
    is_required: bool = True

    def score_to_label(self, score: int) -> str:
        """Return the label for a given numeric score.
        
        Args:
            score: Integer score value.
        
        Returns:
            Label string, or "Unknown" if score not in rubric.
        """
        for level in self.levels:
            if level.score == score:
                return level.label
        return "Unknown"

    def max_score(self) -> int:
        """Return the maximum score in this rubric."""
        return max(level.score for level in self.levels)

    def min_score(self) -> int:
        """Return the minimum score in this rubric."""
        return min(level.score for level in self.levels)


class RubricEvaluator:
    """Apply a set of rubrics to model outputs.
    
    Supports both human raters and LLM-as-Judge evaluation.
    Computes weighted composite scores and inter-rater reliability.
    """

    def __init__(self, rubrics: list[EvaluationRubric]) -> None:
        self._rubrics = rubrics
        total_weight = sum(r.weight for r in rubrics)
        # Normalize weights to sum to 1.0
        self._weights = {r.dimension: r.weight / total_weight for r in rubrics}

    def composite_score(self, raw_scores: dict[str, int]) -> float:
        """Compute weighted composite score from per-dimension scores.
        
        Args:
            raw_scores: Dict mapping dimension name → integer score.
        
        Returns:
            Normalized composite score in [0, 1].
        """
        total = 0.0
        for rubric in self._rubrics:
            score = raw_scores.get(rubric.dimension, rubric.min_score())
            max_score = rubric.max_score()
            normalized = score / max_score
            total += normalized * self._weights[rubric.dimension]
        return total

    @staticmethod
    def cohens_kappa(rater1: list[int], rater2: list[int]) -> float:
        """Compute Cohen's Kappa inter-rater reliability.
        
        Args:
            rater1: List of scores from rater 1.
            rater2: List of scores from rater 2.
        
        Returns:
            Kappa coefficient in [-1, 1]. Values ≥ 0.6 indicate
            substantial agreement.
        
        Raises:
            ValueError: If rater lists have different lengths.
        """
        if len(rater1) != len(rater2):
            raise ValueError("Rater lists must have equal length.")
        n = len(rater1)
        all_scores = set(rater1) | set(rater2)
        
        # Observed agreement
        p_o = sum(a == b for a, b in zip(rater1, rater2)) / n
        
        # Expected agreement under independence
        p_e = sum(
            (rater1.count(s) / n) * (rater2.count(s) / n)
            for s in all_scores
        )
        
        if p_e == 1.0:
            return 1.0
        return (p_o - p_e) / (1.0 - p_e)
```

### 6.2 Sampling Strategy for Evaluation

```python
import random
from enum import Enum
from typing import Any


class SamplingStrategy(Enum):
    """Strategy for selecting evaluation instances from a larger dataset."""
    RANDOM = "random"                    # Simple random sampling
    STRATIFIED = "stratified"           # Stratified by category/difficulty
    ADVERSARIAL = "adversarial"         # Focus on known hard cases
    IMPORTANCE_WEIGHTED = "importance_weighted"  # Weight by expected informativeness


def stratified_sample(
    dataset: list[dict[str, Any]],
    strata_key: str,
    n_per_stratum: int,
    seed: int = 42,
) -> list[dict[str, Any]]:
    """Sample n instances per stratum (category) for balanced evaluation.
    
    Args:
        dataset: Full evaluation dataset.
        strata_key: Dict key that identifies the stratum (e.g., "subject", "difficulty").
        n_per_stratum: Target instances per stratum.
        seed: Random seed for reproducibility.
    
    Returns:
        Balanced sample with up to n_per_stratum items per stratum.
    """
    rng = random.Random(seed)
    by_stratum: dict[str, list[dict]] = {}
    for item in dataset:
        s = str(item.get(strata_key, "unknown"))
        by_stratum.setdefault(s, []).append(item)

    sampled = []
    for stratum_items in by_stratum.values():
        rng.shuffle(stratum_items)
        sampled.extend(stratum_items[:n_per_stratum])
    return sampled
```

---

## Part 7: Evaluation Validity and Bias

[**Construct-Validity**:: The degree to which a benchmark actually measures what it claims to measure. A benchmark with poor construct validity may correlate with superficial features rather than the target capability.]

[**Benchmark-Contamination**:: The phenomenon where model training data contains examples from evaluation benchmarks, inflating reported performance — a primary validity threat in LLM evaluation research (Magar & Schwartz, 2022).]

### 7.1 Contamination Detection

```python
from __future__ import annotations

import hashlib
from difflib import SequenceMatcher


class ContaminationDetector:
    """Detect potential benchmark contamination in training data.
    
    Two detection approaches:
    1. Exact match: SHA-256 hash membership in training data hash set.
    2. Fuzzy match: Sequence similarity above a threshold.
    
    Note: Requires access to a hash set or sample of training data.
    Production use: Pre-compute hashes at training pipeline time.
    """

    def __init__(
        self,
        training_hashes: set[str] | None = None,
        fuzzy_threshold: float = 0.8,
    ) -> None:
        """
        Args:
            training_hashes: Set of SHA-256 hashes of training examples.
            fuzzy_threshold: Minimum similarity ratio for fuzzy detection.
        """
        self._hashes = training_hashes or set()
        self._threshold = fuzzy_threshold

    @staticmethod
    def hash_example(text: str) -> str:
        """Compute a normalized SHA-256 hash of an evaluation example.
        
        Normalization (lowercasing, whitespace stripping) reduces
        false negatives from superficial text variations.
        
        Args:
            text: The evaluation example text.
        
        Returns:
            Hex-encoded SHA-256 hash string.
        """
        normalized = " ".join(text.lower().split())
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    def is_exact_match(self, example_text: str) -> bool:
        """Check for exact (hash-level) contamination.
        
        Args:
            example_text: The benchmark example to check.
        
        Returns:
            True if the example appears in the training hash set.
        """
        return self.hash_example(example_text) in self._hashes

    def fuzzy_contamination_score(
        self,
        example_text: str,
        training_samples: list[str],
    ) -> float:
        """Estimate fuzzy contamination by measuring max similarity.
        
        Args:
            example_text: The benchmark example.
            training_samples: A sample of training text strings.
        
        Returns:
            Maximum similarity ratio in [0, 1] across training samples.
        """
        if not training_samples:
            return 0.0
        max_sim = max(
            SequenceMatcher(None, example_text, t).ratio()
            for t in training_samples
        )
        return max_sim

    def flag_contaminated(
        self,
        benchmark: list[str],
        training_samples: list[str],
    ) -> list[tuple[str, float]]:
        """Flag potentially contaminated examples in a benchmark.
        
        Args:
            benchmark: List of benchmark example strings.
            training_samples: Sample of training data strings.
        
        Returns:
            List of (example, similarity_score) tuples exceeding threshold.
        """
        flagged = []
        for example in benchmark:
            if self.is_exact_match(example):
                flagged.append((example, 1.0))
            else:
                score = self.fuzzy_contamination_score(example, training_samples)
                if score >= self._threshold:
                    flagged.append((example, score))
        return flagged
```

### 7.2 Bias Auditing

```python
from dataclasses import dataclass


@dataclass
class BiasAuditResult:
    """Result of a bias audit across demographic groups.
    
    Attributes:
        dimension: The capability being measured (e.g., "accuracy").
        groups: Dict mapping group label → score.
        max_disparity: Largest absolute score difference between any two groups.
        disparate_pairs: List of (group_a, group_b, disparity) tuples exceeding threshold.
    """
    dimension: str
    groups: dict[str, float]
    max_disparity: float
    disparate_pairs: list[tuple[str, str, float]]


def audit_demographic_parity(
    results_by_group: dict[str, list[EvaluationResult]],
    disparity_threshold: float = 0.05,
) -> BiasAuditResult:
    """Audit for demographic parity across groups.
    
    Demographic parity requires that the model achieves approximately
    equal performance across groups defined by demographic attributes
    (e.g., prompts mentioning different genders, ethnicities, or nationalities).
    
    Args:
        results_by_group: Dict mapping group label → list of evaluation results.
        disparity_threshold: Minimum score difference to flag as disparate.
    
    Returns:
        BiasAuditResult with group scores and flagged disparities.
    """
    group_scores = {
        group: sum(r.score for r in results) / len(results)
        for group, results in results_by_group.items()
        if results
    }

    groups = list(group_scores.keys())
    disparate_pairs = []
    max_disparity = 0.0

    for i, g1 in enumerate(groups):
        for g2 in groups[i + 1:]:
            disparity = abs(group_scores[g1] - group_scores[g2])
            max_disparity = max(max_disparity, disparity)
            if disparity >= disparity_threshold:
                disparate_pairs.append((g1, g2, disparity))

    # Sort by disparity descending for review prioritization
    disparate_pairs.sort(key=lambda x: x[2], reverse=True)

    return BiasAuditResult(
        dimension="accuracy",
        groups=group_scores,
        max_disparity=max_disparity,
        disparate_pairs=disparate_pairs,
    )
```

---

## Part 8: Continuous Evaluation Systems

[**Regression-Suite**:: A curated set of evaluation instances maintained across model versions to detect capability regressions — cases where a new model performs worse than its predecessor on previously solved tasks.]

[**Evaluation-Drift**:: The gradual degradation of evaluation signal quality as: (a) benchmark examples become part of training data, (b) model outputs shift to satisfy judge biases, or (c) task difficulty distributions change in deployment.]

### 8.1 Regression Testing

```python
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable


@dataclass
class RegressionCase:
    """A single regression test case.
    
    Attributes:
        case_id: Unique identifier.
        prompt: The input prompt.
        expected_behavior: Human-readable description of expected output properties.
        baseline_score: Score achieved by the baseline model version.
        regression_threshold: Score drop below baseline that triggers a flag.
        evaluator: Callable scoring function (prompt, response) → float.
        tags: Labels for categorizing and filtering cases.
    """
    case_id: str
    prompt: str
    expected_behavior: str
    baseline_score: float
    regression_threshold: float = 0.1
    evaluator: Callable | None = None
    tags: list[str] = field(default_factory=list)


@dataclass
class RegressionReport:
    """Summary report for a regression test run.
    
    Attributes:
        run_timestamp: When the regression suite was run.
        model_version: Identifier for the model being tested.
        total_cases: Total number of test cases.
        passed: Cases where score ≥ baseline - threshold.
        flagged: Cases where score < baseline - threshold.
        new_failures: Cases that failed regression but were not previously flagged.
        improvements: Cases where score significantly exceeded baseline.
    """
    run_timestamp: str
    model_version: str
    total_cases: int
    passed: int
    flagged: list[tuple[str, float, float]]  # (case_id, baseline, current)
    new_failures: list[str]
    improvements: list[tuple[str, float, float]]

    @property
    def pass_rate(self) -> float:
        """Proportion of cases passing regression."""
        if self.total_cases == 0:
            return 0.0
        return self.passed / self.total_cases


class RegressionSuite:
    """Manage and run regression tests across model versions.
    
    Maintains a library of test cases with baseline scores.
    On each run, computes current scores and flags regressions.
    Results are persisted to disk for trend analysis.
    
    Example:
        >>> suite = RegressionSuite(cases_path=Path("regression_cases.jsonl"),
        ...                         results_dir=Path("regression_results/"))
        >>> suite.load_cases()
        >>> report = suite.run(model_fn=my_model, model_version="v2.1")
        >>> print(f"Pass rate: {report.pass_rate:.1%}")
    """

    def __init__(self, cases_path: Path, results_dir: Path) -> None:
        self._cases_path = cases_path
        self._results_dir = results_dir
        self._cases: list[RegressionCase] = []

    def load_cases(self) -> None:
        """Load regression cases from JSONL file."""
        self._cases = []
        if not self._cases_path.exists():
            return
        with open(self._cases_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    raw = json.loads(line)
                    self._cases.append(RegressionCase(
                        case_id=raw["case_id"],
                        prompt=raw["prompt"],
                        expected_behavior=raw["expected_behavior"],
                        baseline_score=raw["baseline_score"],
                        regression_threshold=raw.get("regression_threshold", 0.1),
                        tags=raw.get("tags", []),
                    ))

    def run(
        self,
        model_fn: Callable[[str], str],
        model_version: str,
        scoring_fn: Callable[[str, str], float] | None = None,
    ) -> RegressionReport:
        """Execute all regression cases against the model.
        
        Args:
            model_fn: Function mapping prompt → response.
            model_version: String identifier for the model (e.g., "v2.1.0").
            scoring_fn: Global scoring function (prompt, response) → float.
                        Used for cases without a per-case evaluator.
        
        Returns:
            RegressionReport with pass/fail statistics and flagged cases.
        """
        passed = 0
        flagged = []
        improvements = []
        timestamp = datetime.utcnow().isoformat()

        for case in self._cases:
            response = model_fn(case.prompt)
            evaluator = case.evaluator or scoring_fn
            if evaluator is None:
                continue

            current_score = evaluator(case.prompt, response)
            delta = current_score - case.baseline_score

            if delta < -case.regression_threshold:
                flagged.append((case.case_id, case.baseline_score, current_score))
            else:
                passed += 1
                if delta > case.regression_threshold:
                    improvements.append((case.case_id, case.baseline_score, current_score))

        # Load previous run to detect new failures
        prev_flagged_ids = self._load_previous_flagged_ids(model_version)
        new_failures = [c for c, _, _ in flagged if c not in prev_flagged_ids]

        report = RegressionReport(
            run_timestamp=timestamp,
            model_version=model_version,
            total_cases=len(self._cases),
            passed=passed,
            flagged=flagged,
            new_failures=new_failures,
            improvements=improvements,
        )
        self._persist_report(report)
        return report

    def _load_previous_flagged_ids(self, model_version: str) -> set[str]:
        """Load case IDs flagged in the most recent previous run."""
        results_files = sorted(self._results_dir.glob(f"regression_{model_version}_*.json"))
        if not results_files:
            return set()
        with open(results_files[-1], encoding="utf-8") as f:
            prev = json.load(f)
        return {item[0] for item in prev.get("flagged", [])}

    def _persist_report(self, report: RegressionReport) -> None:
        """Save report to disk as JSON."""
        self._results_dir.mkdir(parents=True, exist_ok=True)
        fname = f"regression_{report.model_version}_{report.run_timestamp[:10]}.json"
        with open(self._results_dir / fname, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "run_timestamp": report.run_timestamp,
                    "model_version": report.model_version,
                    "total_cases": report.total_cases,
                    "passed": report.passed,
                    "pass_rate": report.pass_rate,
                    "flagged": report.flagged,
                    "new_failures": report.new_failures,
                    "improvements": report.improvements,
                },
                f,
                indent=2,
            )
```

### 8.2 Production Monitoring

```python
from collections import deque
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class ProductionMetrics:
    """Snapshot of production evaluation metrics.
    
    Attributes:
        window_size: Rolling window of recent requests (e.g., last 1,000).
        quality_scores: Rolling deque of LLM-as-Judge quality scores.
        refusal_rate: Rolling rate of model refusals.
        latency_p50: Median response latency in milliseconds.
        latency_p99: 99th percentile response latency.
        error_rate: Proportion of requests that errored.
    """
    window_size: int
    quality_scores: deque = field(default_factory=deque)
    refusal_rate: float = 0.0
    latency_p50: float = 0.0
    latency_p99: float = 0.0
    error_rate: float = 0.0

    def quality_mean(self) -> float:
        """Mean quality score over the current window."""
        if not self.quality_scores:
            return 0.0
        return sum(self.quality_scores) / len(self.quality_scores)

    def quality_p10(self) -> float:
        """10th percentile quality — catches tail-quality degradation."""
        if not self.quality_scores:
            return 0.0
        sorted_scores = sorted(self.quality_scores)
        idx = max(0, int(0.1 * len(sorted_scores)) - 1)
        return sorted_scores[idx]


class ProductionEvaluationMonitor:
    """Real-time production evaluation with alerting.
    
    Samples a configurable fraction of production traffic, routes sampled
    requests through an LLM-as-Judge, and triggers alerts when quality
    metrics cross configured thresholds.
    
    Example:
        >>> monitor = ProductionEvaluationMonitor(
        ...     judge_fn=gpt4_judge,
        ...     sample_rate=0.05,
        ...     quality_alert_threshold=6.0,
        ...     alert_fn=send_slack_alert,
        ... )
        >>> # In request handler:
        >>> monitor.observe(prompt, response, latency_ms=230)
    """

    def __init__(
        self,
        judge_fn: Callable[[str, str], float],
        sample_rate: float = 0.05,
        window_size: int = 1000,
        quality_alert_threshold: float = 6.0,
        p10_alert_threshold: float = 4.0,
        alert_fn: Callable[[str], None] | None = None,
    ) -> None:
        """
        Args:
            judge_fn: (prompt, response) → quality score [0-10].
            sample_rate: Fraction of requests to evaluate (0.05 = 5%).
            window_size: Rolling window size for metric computation.
            quality_alert_threshold: Mean quality below this triggers alert.
            p10_alert_threshold: 10th percentile below this triggers alert.
            alert_fn: Callable to send alerts (e.g., Slack, PagerDuty).
        """
        import random
        self._judge = judge_fn
        self._sample_rate = sample_rate
        self._window_size = window_size
        self._quality_threshold = quality_alert_threshold
        self._p10_threshold = p10_alert_threshold
        self._alert_fn = alert_fn or print
        self._rng = random.Random()
        self._metrics = ProductionMetrics(
            window_size=window_size,
            quality_scores=deque(maxlen=window_size),
        )

    def observe(
        self,
        prompt: str,
        response: str,
        latency_ms: float,
        is_error: bool = False,
        is_refusal: bool = False,
    ) -> None:
        """Record a production request and optionally evaluate it.
        
        Args:
            prompt: The user's prompt.
            response: The model's response.
            latency_ms: Response latency in milliseconds.
            is_error: Whether the request resulted in an error.
            is_refusal: Whether the model refused to answer.
        """
        # Always update latency and error metrics (from all traffic)
        self._update_efficiency_metrics(latency_ms, is_error, is_refusal)

        # Probabilistic quality sampling
        if self._rng.random() < self._sample_rate and not is_error:
            score = self._judge(prompt, response)
            self._metrics.quality_scores.append(score)
            self._check_alerts()

    def _update_efficiency_metrics(
        self, latency_ms: float, is_error: bool, is_refusal: bool
    ) -> None:
        """Update non-quality metrics (no LLM-as-Judge needed)."""
        # PERF: In production, use a sliding window histogram for percentiles
        # rather than recomputing from raw scores each time.
        self._metrics.latency_p50 = latency_ms  # Placeholder — use histogram
        if is_error:
            self._metrics.error_rate = (
                0.99 * self._metrics.error_rate + 0.01 * 1.0
            )
        if is_refusal:
            self._metrics.refusal_rate = (
                0.99 * self._metrics.refusal_rate + 0.01 * 1.0
            )

    def _check_alerts(self) -> None:
        """Trigger alerts if quality metrics cross thresholds."""
        if len(self._metrics.quality_scores) < 50:
            return  # Not enough data for reliable alerting

        mean_q = self._metrics.quality_mean()
        p10_q = self._metrics.quality_p10()

        if mean_q < self._quality_threshold:
            self._alert_fn(
                f"PRODUCTION QUALITY ALERT: Mean quality {mean_q:.2f} "
                f"below threshold {self._quality_threshold}. "
                f"Window: {len(self._metrics.quality_scores)} samples."
            )

        if p10_q < self._p10_threshold:
            self._alert_fn(
                f"PRODUCTION TAIL-QUALITY ALERT: P10 quality {p10_q:.2f} "
                f"below threshold {self._p10_threshold}. "
                f"Investigate low-quality tail responses."
            )

    def current_metrics(self) -> ProductionMetrics:
        """Return the current production metrics snapshot."""
        return self._metrics
```

---

## Citations

1. Hendrycks, D., Burns, C., Basart, S., et al. (2021). *Measuring Massive Multitask Language Understanding*. ICLR 2021. [MMLU benchmark]
2. Chen, M., Tworek, J., Jun, H., et al. (2021). *Evaluating Large Language Models Trained on Code*. arXiv:2107.03374. [HumanEval, pass@k]
3. Srivastava, A., Rastogi, A., Rao, A., et al. (2022). *Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models*. arXiv:2206.04615. [BIG-Bench]
4. Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). *Training Verifiers to Solve Math Word Problems*. arXiv:2110.14168. [GSM8K]
5. Hendrycks, D., Burns, C., Kadavath, S., et al. (2021). *Measuring Mathematical Problem Solving With the MATH Dataset*. NeurIPS 2021. [MATH benchmark]
6. Clark, P., Cowhey, I., Etzioni, O., et al. (2018). *Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge*. arXiv:1803.05457. [ARC benchmark]
7. Zheng, L., Chiang, W.-L., Sheng, Y., et al. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. NeurIPS 2023. [LLM-as-judge, Elo, Chatbot Arena]
8. Wang, X., Wei, J., Schuurmans, D., et al. (2023). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. ICLR 2023. [Self-consistency faithfulness]
9. Lanham, T., Chen, A., Radhakrishnan, A., et al. (2023). *Measuring Faithfulness in Chain-of-Thought Reasoning*. arXiv:2307.13702. [Faithfulness probes]
10. Turpin, M., Michael, J., Perez, E., & Bowman, S. (2023). *Language Models Don't Always Say What They Think*. NeurIPS 2023. [Post-hoc rationalization]
11. Magar, I., & Schwartz, R. (2022). *Data Contamination: From Memorization to Exploitation*. ACL 2022. [Benchmark contamination]
12. Ouyang, L., Wu, J., Jiang, X., et al. (2022). *Training Language Models to Follow Instructions with Human Feedback*. NeurIPS 2022. [RLHF, reward modeling]
13. Bai, Y., Jones, A., Ndousse, K., et al. (2022). *Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback*. arXiv:2204.05862. [HHH alignment]
14. Liang, P., Bommasani, R., Lee, T., et al. (2022). *Holistic Evaluation of Language Models*. arXiv:2211.09110. [HELM framework]
15. Perez, E., Huang, S., Song, F., et al. (2022). *Red Teaming Language Models with Language Models*. arXiv:2202.03286. [Adversarial evaluation]

---

## 🔗 Related Topics for PKB Expansion

1. **[[HELM-Evaluation-Framework]]**
   - *Connection*: HELM (Liang et al. 2022) is a holistic multi-metric framework that extends the single-metric benchmarks covered here, adding calibration, robustness, and fairness simultaneously.
   - *Depth Potential*: A full reference note on HELM's 7 metric categories and its influence on post-2022 evaluation practice.
   - *Knowledge Graph Role*: Central hub linking Doc7 benchmarks → Doc9 safety evaluation → production monitoring.

2. **[[Reward-Model-Training]]**
   - *Connection*: The Bradley-Terry reward model in Part 4 is the core component of RLHF pipelines covered in the alignment literature.
   - *Depth Potential*: Constitutional AI (Bai et al. 2022), DPO (Direct Preference Optimization), and rejection sampling fine-tuning deserve their own reference.
   - *Knowledge Graph Role*: Bridges evaluation (this doc) → alignment training methodology → Doc9 (Prompt Safety).

3. **[[Chatbot-Arena-and-Elo-Leaderboards]]**
   - *Connection*: The Elo rating system in Part 4 underpins Chatbot Arena (Zheng et al. 2023), the dominant crowd-sourced LLM leaderboard.
   - *Depth Potential*: Arena methodology, Bradley-Terry fitting, anonymization protocol, and how arena rankings correlate with automated benchmarks.
   - *Knowledge Graph Role*: Connects Doc7 theory → real-world comparative evaluation practice → Doc8 (production systems).

4. **[[Evaluation-Metric-Gaming-and-Goodhart-Law]]**
   - *Connection*: Once an evaluation metric becomes a training objective, it ceases to be a good measure of the underlying capability (Goodhart's Law). Central to understanding why benchmarks degrade over time.
   - *Depth Potential*: RLHF reward hacking, benchmark saturation, and the arms race between evaluation and model development.
   - *Knowledge Graph Role*: Provides theoretical grounding for evaluation validity (Part 7) and continuous monitoring necessity (Part 8).
---

> [!important] Production Deployment Note
> Continuous evaluation systems (Part 8) should be treated as living infrastructure, not a one-time setup. Schedule quarterly reviews of: sampling rates, alert thresholds, regression case relevance, and judge model version. As models improve, thresholds that were appropriate may become too loose or too strict.
