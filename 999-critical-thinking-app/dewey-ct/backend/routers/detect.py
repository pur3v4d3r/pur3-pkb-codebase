"""
POST /api/detect/

Analyse a user-submitted paragraph for logical fallacies.

The reference fallacy list is loaded from logical-fallacies.json so the LLM is
grounded exclusively in the content the learner is actually studying. Each
detected fallacy includes: the fallacy name, its category, a verbatim quote
from the submitted text, and a brief explanation.
"""

import json
import os
from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, field_validator

from limiter import limiter
from services.llm import chat

router = APIRouter()

DATA_DIR = Path(__file__).parent.parent.parent / "data"

_DETECT_RATE_LIMIT = os.environ.get("DETECT_RATE_LIMIT", "6/minute")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load_fallacies() -> list[dict]:
    """Load the logical-fallacies reference list from the JSON data file."""
    path = DATA_DIR / "frameworks" / "logical-fallacies.json"
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data.get("fallacies", [])
    except (OSError, json.JSONDecodeError) as exc:
        raise HTTPException(
            status_code=503,
            detail="Fallacy reference data is unavailable.",
        ) from exc


def _build_fallacy_reference(fallacies: list[dict]) -> str:
    """Format the fallacy list as a compact reference for the system prompt."""
    lines = []
    for f in fallacies:
        name = f.get("name", "")
        category = f.get("category", "")
        definition = f.get("definition", "")
        lines.append(f"- {name} ({category}): {definition}")
    return "\n".join(lines)


def _build_system_prompt(fallacy_reference: str) -> str:
    return (
        "You are a logic instructor with expertise in identifying logical fallacies.\n\n"
        "Below is the complete list of recognized fallacies you may identify. "
        "Only report fallacies from this list — do not invent new ones.\n\n"
        "REFERENCE FALLACIES:\n"
        f"{fallacy_reference}\n\n"
        "INSTRUCTIONS:\n"
        "1. Read the user's text carefully.\n"
        "2. Identify any logical fallacies present, using only the fallacies above.\n"
        "3. For each fallacy found, provide:\n"
        '   - "name": exact fallacy name from the reference\n'
        '   - "category": the category from the reference\n'
        '   - "quote": a verbatim excerpt from the text (10–60 words) that demonstrates the fallacy\n'
        '   - "explanation": 2–3 sentences explaining why this specific quote is an instance of this fallacy\n\n'
        "Respond ONLY with valid JSON using this exact structure:\n"
        '{"fallacies":[{"name":"...","category":"...","quote":"...","explanation":"..."}]}\n'
        'If no fallacies are found, respond with: {"fallacies":[]}\n'
        "Output only the JSON object. No markdown fences, no preamble, no text outside the JSON."
    )


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------


class DetectRequest(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def text_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("text must not be empty")
        if len(v) > 3000:
            raise ValueError("text must be 3000 characters or fewer")
        return v


class DetectedFallacy(BaseModel):
    name: str
    category: str
    quote: str
    explanation: str


class DetectResponse(BaseModel):
    fallacies: list[DetectedFallacy]


# ---------------------------------------------------------------------------
# Endpoint
# ---------------------------------------------------------------------------


@router.post("/", response_model=DetectResponse)
@limiter.limit(_DETECT_RATE_LIMIT)
async def detect_fallacies(request: Request, body: DetectRequest) -> DetectResponse:
    """
    Analyse the submitted text and return any logical fallacies identified,
    grounded in the logical-fallacies.json reference list.
    """
    fallacies_ref = _load_fallacies()
    if not fallacies_ref:
        raise HTTPException(status_code=503, detail="Fallacy reference data is empty.")

    system_prompt = _build_system_prompt(_build_fallacy_reference(fallacies_ref))

    try:
        raw = chat(system_prompt, body.text, max_tokens=1400)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=f"LLM unavailable: {exc}") from exc

    # Parse the LLM JSON response; fall back to empty list rather than 500.
    try:
        cleaned = raw.strip()
        # Strip markdown code fences if the model included them
        if cleaned.startswith("```"):
            parts = cleaned.split("```")
            cleaned = parts[1] if len(parts) > 1 else cleaned
            if cleaned.startswith("json"):
                cleaned = cleaned[4:]
        parsed = json.loads(cleaned)
        detected = [DetectedFallacy(**f) for f in parsed.get("fallacies", [])]
    except (json.JSONDecodeError, TypeError, ValueError):
        detected = []

    return DetectResponse(fallacies=detected)
