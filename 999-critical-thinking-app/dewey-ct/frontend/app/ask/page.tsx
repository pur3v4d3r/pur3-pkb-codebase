import { getChapterSummaries } from '@/lib/content';
import AskClient from '@/components/ask/AskClient';

export const metadata = {
  title: 'Ask Dewey — Socratic Tutor | DeweyCT',
  description:
    'Ask a Socratic tutor questions about reflective thinking, Dewey\u2019s philosophy, and critical thinking frameworks.',
};

export default function AskPage({
  searchParams,
}: {
  searchParams: { chapter?: string };
}) {
  const chapters = getChapterSummaries();
  const initialChapterId = searchParams.chapter
    ? parseInt(searchParams.chapter, 10)
    : undefined;

  return (
    <div className="mx-auto max-w-3xl space-y-6 px-4 py-8">
      {/* Header */}
      <div className="space-y-1">
        <div className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-indigo-50">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5 text-indigo-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth={1.75}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z"
              />
            </svg>
          </div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Ask Dewey</h1>
        </div>
        <p className="text-sm text-slate-500 leading-relaxed">
          A Socratic tutor grounded in Dewey&apos;s <em>How We Think</em>. Ask anything about
          reflective thinking, the five phases of inquiry, or how modern frameworks connect to
          Dewey&apos;s ideas. Optionally select a chapter for focused context.
        </p>
      </div>

      <AskClient chapters={chapters} initialChapterId={initialChapterId} />
    </div>
  );
}
