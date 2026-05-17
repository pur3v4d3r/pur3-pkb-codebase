"""
Shared Ollama LLM client for DeweyCT backend.

Reads configuration from environment variables:
  OLLAMA_BASE_URL  — Ollama server URL  (default: http://localhost:11434)
  OLLAMA_MODEL     — Model tag to use   (default: qwen2.5:14b)
"""

import os
from typing import Optional

import ollama

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OLLAMA_BASE_URL: str = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL: str = os.environ.get("OLLAMA_MODEL", "qwen2.5:14b")

_client: Optional[ollama.Client] = None


def get_client() -> ollama.Client:
    """Return a module-level singleton Ollama client."""
    global _client
    if _client is None:
        _client = ollama.Client(host=OLLAMA_BASE_URL)
    return _client


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def chat(system_prompt: str, user_content: str, max_tokens: int = 800) -> str:
    """
    Send a single system+user turn to the configured Ollama model and return
    the assistant text.  Raises RuntimeError on connection / model failure.
    """
    client = get_client()
    try:
        response = client.chat(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            options={"num_predict": max_tokens},
        )
        return response["message"]["content"]
    except ollama.ResponseError as exc:
        raise RuntimeError(f"Ollama model error: {exc}") from exc
    except Exception as exc:
        raise RuntimeError(f"Ollama connection error: {exc}") from exc
