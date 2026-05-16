import os
import json
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator
import anthropic

router = APIRouter()

DATA_DIR = Path(__file__).parent.parent.parent / "data"
_anthropic_client: Optional[anthropic.Anthropic] = None


def get_client() -> anthropic.Anthropic:
    global _anthropic_client
    if _anthropic_client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise HTTPException(status_code=503, detail="ANTHROPIC_API_KEY not configured")
        _anthropic_client = anthropic.Anthropic(api_key=api_key)
    return _anthropic_client


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
def ask_question(req: QARequest) -> QAResponse:
    client = get_client()

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

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=600,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {req.question}",
            }
        ],
    )

    answer = message.content[0].text if message.content else "No response generated."
    return QAResponse(answer=answer, sources=sources)
