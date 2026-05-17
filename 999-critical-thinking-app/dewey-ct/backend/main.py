import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from limiter import limiter
from routers import qa, feedback, data

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


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "deweyct-api"}
