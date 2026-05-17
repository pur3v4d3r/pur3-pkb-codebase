"""
bench_models.py — DeweyCT model benchmark
==========================================
Tests phi3:3.8b and qwen3:8b-q4_K_M against the three AI tasks the app uses:
  1. /api/qa      — free Q&A about a critical-thinking concept
  2. /api/evaluate — evaluates a user-submitted argument
  3. /api/detect  — detects fallacies in a paragraph

Usage:
    python bench_models.py              # tests both models, shows responses + timings
    python bench_models.py phi3:3.8b    # test a single model
"""

import sys
import time
from pathlib import Path

# ── locate the .env one level up (same logic as main.py) ──────────────────
from dotenv import load_dotenv, find_dotenv
_env_path = Path(__file__).parent / ".env"
load_dotenv(_env_path)

import ollama  # noqa: E402  (needs OLLAMA_BASE_URL potentially)

# ── prompts lifted verbatim from the actual backend services ───────────────
PROMPTS = {
    "qa": {
        "system": (
            "You are Dewey, a Socratic tutor specialising in critical thinking. "
            "Answer questions clearly and concisely. Use concrete examples. "
            "If a question is off-topic, gently redirect."
        ),
        "user": (
            "What is the difference between a deductive and an inductive argument? "
            "Give a one-sentence example of each."
        ),
    },
    "evaluate": {
        "system": (
            "You are an expert in informal logic and argument analysis. "
            "Evaluate the following argument: identify the conclusion, premises, "
            "any logical fallacies, and rate the overall strength as Weak / Moderate / Strong."
        ),
        "user": (
            "Everyone who studies hard gets good grades. Sarah studies hard. "
            "Therefore, Sarah must be very intelligent."
        ),
    },
    "detect": {
        "system": (
            "You are a fallacy detection engine. "
            "List every logical fallacy present in the text below. "
            "For each, give: the fallacy name, the exact phrase that contains it, "
            "and a one-sentence explanation. Respond in JSON array format."
        ),
        "user": (
            "You can't trust what Dr. Smith says about climate change — "
            "she drives a gas-powered car. Besides, everyone in my town "
            "agrees the weather has always been like this, so there's nothing unusual happening."
        ),
    },
}

MODELS = ["phi3:3.8b", "qwen3:8b-q4_K_M"]
MAX_TOKENS = 600


def run_task(model: str, task: str) -> tuple[str, float]:
    """Run one task against one model. Returns (response_text, elapsed_seconds)."""
    client = ollama.Client()
    p = PROMPTS[task]
    t0 = time.perf_counter()
    resp = client.chat(
        model=model,
        messages=[
            {"role": "system", "content": p["system"]},
            {"role": "user", "content": p["user"]},
        ],
        options={"num_predict": MAX_TOKENS},
    )
    elapsed = time.perf_counter() - t0
    return resp["message"]["content"], elapsed


def benchmark(models: list[str]) -> None:
    sep = "─" * 72
    for model in models:
        print(f"\n{'═' * 72}")
        print(f"  MODEL: {model}")
        print(f"{'═' * 72}")
        for task in PROMPTS:
            print(f"\n{sep}")
            print(f"  TASK: {task.upper()}")
            print(f"  USER: {PROMPTS[task]['user'][:120]}…" if len(PROMPTS[task]['user']) > 120 else f"  USER: {PROMPTS[task]['user']}")
            print(sep)
            try:
                text, elapsed = run_task(model, task)
                print(f"\n{text}\n")
                print(f"  ⏱  {elapsed:.1f}s")
            except Exception as exc:
                print(f"\n  ❌  ERROR: {exc}\n")
    print(f"\n{'═' * 72}\n  Done.\n{'═' * 72}\n")


if __name__ == "__main__":
    target_models = sys.argv[1:] if len(sys.argv) > 1 else MODELS
    benchmark(target_models)
