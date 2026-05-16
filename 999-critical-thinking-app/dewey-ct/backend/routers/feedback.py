import os
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator
import anthropic

router = APIRouter()

_anthropic_client: Optional[anthropic.Anthropic] = None


def get_client() -> anthropic.Anthropic:
    global _anthropic_client
    if _anthropic_client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise HTTPException(status_code=503, detail="ANTHROPIC_API_KEY not configured")
        _anthropic_client = anthropic.Anthropic(api_key=api_key)
    return _anthropic_client


class FeedbackRequest(BaseModel):
    template_id: str
    field_id: str
    response_text: str
    framework_context: Optional[str] = None

    @field_validator("response_text")
    @classmethod
    def response_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("response_text must not be empty")
        if len(v) > 5000:
            raise ValueError("response_text must be 5000 characters or fewer")
        return v

    @field_validator("template_id", "field_id")
    @classmethod
    def ids_safe(cls, v: str) -> str:
        if not v.replace("-", "").replace("_", "").isalnum():
            raise ValueError("id must be alphanumeric with hyphens/underscores only")
        return v


class FeedbackResponse(BaseModel):
    feedback: str
    score: Optional[int] = None  # 1-5 holistic quality, optional
    suggestions: list[str]


@router.post("/", response_model=FeedbackResponse)
def get_feedback(req: FeedbackRequest) -> FeedbackResponse:
    client = get_client()

    framework_note = (
        f"\n\nFramework context: {req.framework_context}" if req.framework_context else ""
    )

    system_prompt = (
        "You are a skilled critical-thinking coach. You provide constructive, specific feedback "
        "on learner responses within structured thinking templates. Your feedback should: "
        "1) acknowledge what the learner did well, 2) identify the most important gap or improvement, "
        "3) offer one concrete, actionable suggestion. "
        "Be encouraging but honest. Keep feedback under 200 words."
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Template: {req.template_id}\n"
                    f"Field: {req.field_id}\n"
                    f"Learner response:\n{req.response_text}"
                    f"{framework_note}\n\n"
                    "Please provide feedback in this JSON format:\n"
                    '{"feedback": "...", "suggestions": ["...", "..."]}'
                ),
            }
        ],
    )

    raw = message.content[0].text if message.content else "{}"

    # Parse the structured response safely
    import json, re

    json_match = re.search(r'\{.*\}', raw, re.DOTALL)
    if json_match:
        try:
            parsed = json.loads(json_match.group())
            return FeedbackResponse(
                feedback=str(parsed.get("feedback", raw)),
                suggestions=[str(s) for s in parsed.get("suggestions", [])],
            )
        except json.JSONDecodeError:
            pass

    return FeedbackResponse(feedback=raw, suggestions=[])
