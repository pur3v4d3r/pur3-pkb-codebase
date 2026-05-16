// Client-side API utility for communicating with the FastAPI backend.
// The backend is expected to be running at localhost:8000 in development,
// or at the URL specified by NEXT_PUBLIC_API_URL in production.

const API_BASE =
  process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, '') ?? 'http://localhost:8000';

// ---- Types ----

export interface FeedbackPayload {
  template_id: string;
  field_id: string;
  response_text: string;
  framework_context?: string;
}

export interface FeedbackResponse {
  feedback: string;
  score?: number;
  suggestions: string[];
}

export interface QAPayload {
  question: string;
  chapter_id?: number;
}

export interface QAResponse {
  answer: string;
  sources: string[];
}

// ---- Helpers ----

async function post<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    throw new Error(`API error ${res.status}: ${text}`);
  }
  return res.json() as Promise<T>;
}

// ---- API functions ----

/**
 * Request AI feedback on a single template field response.
 * Calls POST /api/feedback/
 */
export function requestFeedback(payload: FeedbackPayload): Promise<FeedbackResponse> {
  return post<FeedbackResponse>('/api/feedback/', payload);
}

/**
 * Ask a Socratic-tutor question about a chapter (or general CT question).
 * Calls POST /api/qa/
 */
export function askQuestion(payload: QAPayload): Promise<QAResponse> {
  return post<QAResponse>('/api/qa/', payload);
}
