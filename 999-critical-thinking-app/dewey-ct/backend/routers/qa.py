import json
import os
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, field_validator

from limiter import limiter
from services.llm import chat

router = APIRouter()

from services.config import DATA_DIR

# Rate limit for this router — reads QA_RATE_LIMIT env var, falls back to 10/minute
_QA_RATE_LIMIT = os.environ.get("QA_RATE_LIMIT", "10/minute")


def load_chapter(chapter_id: int) -> dict:
    padded = str(chapter_id).zfill(2)
    path = DATA_DIR / "chapters" / f"chapter-{padded}.json"
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"Chapter {chapter_id} not found")
    return json.loads(path.read_text(encoding="utf-8"))


class QARequest(BaseModel):
    question: str
    chapter_id: Optional[int] = None

    @field_validator("question")
    @classmethod
    def question_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("question must not be empty")
        if len(v) > 2000:
            raise ValueError("question must be 2000 characters or fewer")
        return v


class QAResponse(BaseModel):
    answer: str
    sources: list[str]


@router.post("/", response_model=QAResponse)
@limiter.limit(_QA_RATE_LIMIT)
def ask_question(request: Request, req: QARequest) -> QAResponse:
    context_parts: list[str] = []
    sources: list[str] = []

    if req.chapter_id is not None:
        chapter = load_chapter(req.chapter_id)
        context_parts.append(
            f"Chapter {chapter['chapter']}: {chapter['title']}\n\n"
            f"Overview: {chapter['overview']}\n\n"
            f"Concepts: {', '.join(c['name'] for c in chapter.get('concepts', []))}"
        )
        sources.append(f"Chapter {chapter['chapter']}: {chapter['title']}")

    context = "\n\n---\n\n".join(context_parts) if context_parts else "General critical thinking inquiry."

    system_prompt = (
        "You are a Socratic tutor specializing in John Dewey's philosophy of reflective thinking "
        "and modern critical thinking frameworks. You help learners understand and apply the ideas "
        "from 'How We Think' (1933 revised edition). Be precise, cite specific Dewey passages "
        "or concepts when relevant, and encourage the learner to think rather than passively receive answers. "
        "Keep responses concise (under 300 words) unless the complexity of the question demands more."
    )

    try:
        answer = chat(
            system_prompt=system_prompt,
            user_content=f"Context:\n{context}\n\nQuestion: {req.question}",
            max_tokens=600,
        )
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))

    return QAResponse(answer=answer, sources=sources)
