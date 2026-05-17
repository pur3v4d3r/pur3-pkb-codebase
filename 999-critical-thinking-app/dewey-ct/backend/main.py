import os
from pathlib import Path

from dotenv import load_dotenv

# Resolve .env path for both dev and packaged distribution.
# Packaged: launcher sets DEWEYCT_APP_ROOT before spawning this process.
# Dev:      .env lives one level above backend/ (in dewey-ct/).
_app_root_env = os.environ.get("DEWEYCT_APP_ROOT")
if _app_root_env:
    _env_path = Path(_app_root_env) / ".env"
else:
    _env_path = Path(__file__).parent.parent / ".env"

# Must run before any router import so OLLAMA_MODEL is set before llm.py reads it.
load_dotenv(_env_path)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from limiter import limiter
from routers import qa, feedback, data, evaluate, detect

# ---------------------------------------------------------------------------
# CORS — lock to explicit origins; never use "*" with user data
# Set ALLOWED_ORIGINS=https://yourapp.com,https://www.yourapp.com for prod
# ---------------------------------------------------------------------------
_origins_raw = os.environ.get("ALLOWED_ORIGINS", "http://localhost:3001")
ALLOWED_ORIGINS: list[str] = [o.strip() for o in _origins_raw.split(",") if o.strip()]

# ---------------------------------------------------------------------------
# Rate limiter (shared state — imported by routers)
# ---------------------------------------------------------------------------
# (limiter instance lives in limiter.py to avoid circular imports)

app = FastAPI(
    title="DeweyCT API",
    description="AI-powered backend for the DeweyCT critical thinking app",
    version="0.1.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)  # type: ignore[arg-type]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(qa.router, prefix="/api/qa", tags=["Q&A"])
app.include_router(feedback.router, prefix="/api/feedback", tags=["Feedback"])
app.include_router(data.router, prefix="/api/data", tags=["Data"])
app.include_router(evaluate.router, prefix="/api/evaluate", tags=["Evaluate"])
app.include_router(detect.router, prefix="/api/detect", tags=["Detect"])


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "deweyct-api"}
