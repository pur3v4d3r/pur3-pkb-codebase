"""
POST /api/evaluate/

Evaluate a learner's free-text answer against the Paul-Elder Intellectual
Standards and the specific framework requirements of a practice problem.
Returns a structured rubric score, strengths/improvements list, and a
concrete next step — all grounded in the problem's solution sketch
(which never appears in the API response, only in the LLM prompt).
"""

import json
import os
import re
from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, field_validator

from limiter import limiter
from services.llm import chat

router = APIRouter()

from services.config import DATA_DIR

_EVAL_RATE_LIMIT = os.environ.get("EVAL_RATE_LIMIT", "6/minute")

# Paul-Elder Intellectual Standards — concise form for system prompt
_STANDARDS_SUMMARY = (
    "1. Clarity     — understandable, unambiguous; can the reader paraphrase it?\n"
    "2. Accuracy    — free from errors; is it actually true / verifiable?\n"
    "3. Precision   — specific and exact; not vague generalisations\n"
    "4. Relevance   — directly related to the question at issue\n"
    "5. Depth       — addresses the real complexity; goes beyond surface points\n"
    "6. Breadth     — considers multiple relevant viewpoints or factors\n"
    "7. Logic       — claims follow from evidence; no contradictions\n"
    "8. Significance — focuses on what is most important, not peripheral details\n"
    "9. Fairness    — impartial; considers opposing views charitably"
)


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------


class EvaluateRequest(BaseModel):
    problem_id: str
    user_answer: str

    @field_validator("problem_id")
    @classmethod
    def problem_id_safe(cls, v: str) -> str:
        v = v.strip().upper()
        if not re.match(r"^PP-\d{2}$", v):
            raise ValueError("problem_id must match PP-NN format (e.g. PP-09)")
        return v

    @field_validator("user_answer")
    @classmethod
    def answer_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("user_answer must not be empty")
        if len(v) > 5000:
            raise ValueError("user_answer must be 5000 characters or fewer")
        return v


class StandardFeedback(BaseModel):
    standard: str
    score: int   # 1–5
    comment: str


class EvaluateResponse(BaseModel):
    overall_score: int          # 1–5
    strengths: list[str]
    improvements: list[str]
    next_step: str
    standards_feedback: list[StandardFeedback]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load_problem(problem_id: str) -> dict:
    path = DATA_DIR / "practice-problems" / f"{problem_id}.json"
    if not path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Practice problem {problem_id} not found",
        )
    return json.loads(path.read_text(encoding="utf-8"))


def _build_system_prompt(problem: dict) -> str:
    key_moves = "\n".join(
        f"  - {m}"
        for m in problem.get("solution_sketch", {}).get("key_moves", [])
    )
    workspace_keys = ", ".join(problem.get("workspace_prompts", {}).keys())

    return (
        "You are a rigorous critical-thinking evaluator applying the Paul-Elder framework. "
        "Your job is to evaluate a learner's written analysis of a practice problem and return "
        "structured, specific, constructive feedback.\n\n"
        f"PAUL-ELDER INTELLECTUAL STANDARDS:\n{_STANDARDS_SUMMARY}\n\n"
        "PROBLEM CONTEXT\n"
        f"  Title:           {problem.get('title', '')}\n"
        f"  Framework:       {problem.get('framework_label', '')}\n"
        f"  Object:          {problem.get('object_of_analysis', '')[:400]}\n"
        f"  Instructions:    {problem.get('instructions', '')[:600]}\n"
        f"  Required parts:  {workspace_keys}\n\n"
        "REFERENCE KEY MOVES (expert benchmark — do NOT repeat or reveal these verbatim):\n"
        f"{key_moves}\n\n"
        "EVALUATION INSTRUCTIONS\n"
        "  - Score overall quality 1–5: 1=major gaps, 2=partial, 3=adequate, 4=strong, 5=expert.\n"
        "  - List 2–3 genuine strengths (specific, not generic praise).\n"
        "  - List 2–3 concrete improvements (name the exact gap and how to fix it).\n"
        "  - Give one actionable next step the learner should take.\n"
        "  - Rate 3–4 most relevant intellectual standards (1–5 each) with one precise comment.\n\n"
        "Respond ONLY in this JSON format (no markdown, no extra text):\n"
        '{\n'
        '  "overall_score": 3,\n'
        '  "strengths": ["...", "..."],\n'
        '  "improvements": ["...", "..."],\n'
        '  "next_step": "...",\n'
        '  "standards_feedback": [\n'
        '    {"standard": "Clarity", "score": 4, "comment": "..."},\n'
        '    {"standard": "Logic",   "score": 3, "comment": "..."}\n'
        '  ]\n'
        '}'
    )


def _parse_response(raw: str) -> EvaluateResponse:
    """Extract JSON from LLM output and validate into EvaluateResponse."""
    json_match = re.search(r"\{.*\}", raw, re.DOTALL)
    if json_match:
        try:
            parsed = json.loads(json_match.group())
            return EvaluateResponse(
                overall_score=max(1, min(5, int(parsed.get("overall_score", 3)))),
                strengths=[str(s) for s in parsed.get("strengths", [])],
                improvements=[str(i) for i in parsed.get("improvements", [])],
                next_step=str(parsed.get("next_step", "")),
                standards_feedback=[
                    StandardFeedback(
                        standard=str(sf.get("standard", "")),
                        score=max(1, min(5, int(sf.get("score", 3)))),
                        comment=str(sf.get("comment", "")),
                    )
                    for sf in parsed.get("standards_feedback", [])
                    if isinstance(sf, dict)
                ],
            )
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            pass

    # Graceful fallback — wrap raw text so the UI still renders something useful
    return EvaluateResponse(
        overall_score=3,
        strengths=[],
        improvements=[raw.strip()[:600]],
        next_step="Review the note above and revise your answer.",
        standards_feedback=[],
    )


# ---------------------------------------------------------------------------
# Route
# ---------------------------------------------------------------------------


@router.post("/", response_model=EvaluateResponse)
@limiter.limit(_EVAL_RATE_LIMIT)
def evaluate_answer(request: Request, req: EvaluateRequest) -> EvaluateResponse:
    problem = _load_problem(req.problem_id)
    system_prompt = _build_system_prompt(problem)

    try:
        raw = chat(
            system_prompt=system_prompt,
            user_content=f"Learner's answer:\n\n{req.user_answer}",
            max_tokens=900,
        )
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))

    return _parse_response(raw)
