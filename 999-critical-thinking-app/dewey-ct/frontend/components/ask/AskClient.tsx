'use client';

import { useState, useRef, useEffect } from 'react';
import { askQuestion, type QAResponse } from '@/lib/api';
import type { ChapterSummary } from '@/types/chapter';

interface QAEntry {
  question: string;
  answer: string;
  sources: string[];
  chapterContext?: string;
}

interface AskClientProps {
  chapters: ChapterSummary[];
  initialChapterId?: number;
}

const EXAMPLE_QUESTIONS = [
  "What's the difference between imagination and reflective thinking?",
  "How does Dewey's five-phase model relate to the scientific method?",
  "What role does doubt play in triggering reflective thought?",
  "How can I apply Bloom's Taxonomy to evaluate my own reasoning?",
  "What does Dewey mean by 'empirical' versus 'experimental' thinking?",
];

export default function AskClient({ chapters, initialChapterId }: AskClientProps) {
  const [question, setQuestion] = useState('');
  const [chapterId, setChapterId] = useState<string>(
    initialChapterId != null ? String(initialChapterId) : ''
  );
  const [history, setHistory] = useState<QAEntry[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const bottomRef = useRef<HTMLDivElement>(null);

  // Scroll to latest answer after update
  useEffect(() => {
    if (history.length > 0) {
      bottomRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }, [history]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const q = question.trim();
    if (!q || loading) return;

    const selectedChapter = chapterId
      ? chapters.find((c) => c.chapter === parseInt(chapterId))
      : undefined;

    setLoading(true);
    setError(null);

    try {
      const result: QAResponse = await askQuestion({
        question: q,
        chapter_id: chapterId ? parseInt(chapterId) : undefined,
      });

      setHistory((prev) => [
        ...prev,
        {
          question: q,
          answer: result.answer,
          sources: result.sources,
          chapterContext: selectedChapter
            ? `Ch. ${selectedChapter.chapter}: ${selectedChapter.title}`
            : undefined,
        },
      ]);
      setQuestion('');
    } catch {
      setError(
        'Could not reach the AI backend. Make sure the server is running at localhost:8000.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleExampleClick = (q: string) => {
    setQuestion(q);
  };

  return (
    <div className="space-y-6">
      {/* Q&A history — newest at bottom */}
      {history.length > 0 && (
        <div className="space-y-4">
          {history.map((entry, i) => (
            <div
              key={i}
              className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm space-y-4"
            >
              {/* Question */}
              <div className="space-y-1">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="text-xs font-semibold uppercase tracking-widest text-slate-400">
                    You asked
                  </span>
                  {entry.chapterContext && (
                    <span className="rounded-full bg-slate-100 px-2 py-0.5 text-xs text-slate-600">
                      {entry.chapterContext}
                    </span>
                  )}
                </div>
                <p className="text-sm font-medium text-slate-800">{entry.question}</p>
              </div>

              {/* Divider */}
              <div className="border-t border-slate-100" />

              {/* Answer */}
              <div className="space-y-2">
                <span className="text-xs font-semibold uppercase tracking-widest text-slate-400">
                  Socratic Tutor
                </span>
                <p className="text-sm leading-relaxed text-slate-700 whitespace-pre-wrap">
                  {entry.answer}
                </p>
              </div>

              {/* Sources */}
              {entry.sources.length > 0 && (
                <div className="space-y-1 border-t border-slate-100 pt-3">
                  <span className="text-xs font-semibold uppercase tracking-widest text-slate-400">
                    Context used
                  </span>
                  <ul className="space-y-0.5">
                    {entry.sources.map((s, si) => (
                      <li key={si} className="flex items-center gap-1.5 text-xs text-slate-500">
                        <span className="inline-block h-1.5 w-1.5 rounded-full bg-slate-300" />
                        {s}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          ))}
          <div ref={bottomRef} />
        </div>
      )}

      {/* Empty state — example questions */}
      {history.length === 0 && (
        <div className="rounded-xl border border-dashed border-slate-200 bg-slate-50 p-6 space-y-3">
          <p className="text-xs font-semibold uppercase tracking-widest text-slate-400">
            Example questions to get started
          </p>
          <ul className="space-y-2">
            {EXAMPLE_QUESTIONS.map((q, i) => (
              <li key={i}>
                <button
                  type="button"
                  onClick={() => handleExampleClick(q)}
                  className="text-left text-sm text-indigo-600 hover:text-indigo-800 hover:underline transition-colors"
                >
                  &ldquo;{q}&rdquo;
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Ask form — sticky at bottom of content area */}
      <form
        onSubmit={handleSubmit}
        className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm space-y-4"
      >
        <div className="space-y-2">
          <label
            htmlFor="chapter-select"
            className="text-xs font-semibold uppercase tracking-widest text-slate-500"
          >
            Chapter context <span className="font-normal normal-case text-slate-400">(optional)</span>
          </label>
          <select
            id="chapter-select"
            value={chapterId}
            onChange={(e) => setChapterId(e.target.value)}
            className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm text-slate-800 shadow-sm focus:border-slate-500 focus:outline-none focus:ring-2 focus:ring-slate-200"
          >
            <option value="">No specific chapter — general question</option>
            {chapters.map((ch) => (
              <option key={ch.chapter} value={ch.chapter}>
                Ch. {ch.chapter}: {ch.title}
              </option>
            ))}
          </select>
        </div>

        <div className="space-y-2">
          <label
            htmlFor="question-input"
            className="text-xs font-semibold uppercase tracking-widest text-slate-500"
          >
            Your question
          </label>
          <textarea
            id="question-input"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
                e.preventDefault();
                if (question.trim() && !loading) handleSubmit(e as unknown as React.FormEvent);
              }
            }}
            placeholder="Ask anything about Dewey's reflective thinking or critical thinking frameworks…"
            rows={3}
            maxLength={2000}
            className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2.5 text-sm leading-relaxed text-slate-800 shadow-sm placeholder:text-slate-400 focus:border-slate-500 focus:outline-none focus:ring-2 focus:ring-slate-200 resize-none"
          />
          <p className="text-right text-xs text-slate-400">
            {question.length}/2000 &nbsp;&middot;&nbsp; Ctrl+Enter to submit
          </p>
        </div>

        {error && (
          <p className="rounded-md bg-red-50 px-3 py-2 text-xs text-red-700">{error}</p>
        )}

        <button
          type="submit"
          disabled={loading || !question.trim()}
          className="w-full rounded-lg bg-slate-900 px-4 py-2.5 text-sm font-semibold text-white transition hover:bg-slate-700 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {loading ? (
            <span className="flex items-center justify-center gap-2">
              <span className="inline-block h-3.5 w-3.5 animate-spin rounded-full border-2 border-white border-t-transparent" />
              Thinking…
            </span>
          ) : (
            'Ask'
          )}
        </button>
      </form>
    </div>
  );
}
