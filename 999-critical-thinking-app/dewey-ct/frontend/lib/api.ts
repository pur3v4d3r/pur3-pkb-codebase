// Client-side API utility for communicating with the FastAPI backend.
// Requests use relative URLs (/api/*) — Next.js rewrites proxy them to the
// FastAPI server at localhost:8000. This avoids CORS entirely.

const API_BASE = '';

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

// ---- Evaluate ----

export interface StandardFeedback {
  standard: string;
  score: number;  // 1-5
  comment: string;
}

export interface EvaluatePayload {
  problem_id: string;
  user_answer: string;
}

export interface EvaluateResponse {
  overall_score: number;  // 1-5
  strengths: string[];
  improvements: string[];
  next_step: string;
  standards_feedback: StandardFeedback[];
}

/**
 * Submit a learner's free-text answer to a practice problem for
 * Paul-Elder structured evaluation. Calls POST /api/evaluate/
 */
export function evaluatePracticeAnswer(payload: EvaluatePayload): Promise<EvaluateResponse> {
  return post<EvaluateResponse>('/api/evaluate/', payload);
}

// ---- Detect ----

export interface DetectedFallacy {
  name: string;
  category: string;
  quote: string;
  explanation: string;
}

export interface DetectPayload {
  text: string;
}

export interface DetectResponse {
  fallacies: DetectedFallacy[];
}

/**
 * Submit text to the backend for logical fallacy detection.
 * Returns a (possibly empty) list of identified fallacies grounded in
 * the logical-fallacies.json reference. Calls POST /api/detect/
 */
export function detectFallacies(payload: DetectPayload): Promise<DetectResponse> {
  return post<DetectResponse>('/api/detect/', payload);
}
