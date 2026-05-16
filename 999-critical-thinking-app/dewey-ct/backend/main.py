from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import qa, feedback

app = FastAPI(
    title="DeweyCT API",
    description="AI-powered backend for the DeweyCT critical thinking app",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://*.vercel.app",
    ],
    allow_credentials=False,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(qa.router, prefix="/api/qa", tags=["Q&A"])
app.include_router(feedback.router, prefix="/api/feedback", tags=["Feedback"])


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "deweyct-api"}
