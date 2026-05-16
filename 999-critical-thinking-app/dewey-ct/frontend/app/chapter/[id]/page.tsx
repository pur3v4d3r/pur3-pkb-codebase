import { getChapter } from '@/lib/content';
import CalloutRenderer from '@/components/chapter/CalloutRenderer';
import MarkReadButton from '@/components/chapter/MarkReadButton';
import Link from 'next/link';
import { notFound } from 'next/navigation';

export async function generateStaticParams() {
  return Array.from({ length: 19 }, (_, i) => ({ id: String(i + 1) }));
}

export async function generateMetadata({ params }: { params: { id: string } }) {
  const id = parseInt(params.id, 10);
  if (isNaN(id) || id < 1 || id > 19) return {};
  const chapter = getChapter(id);
  return {
    title: `Ch. ${chapter.chapter}: ${chapter.title} — DeweyCT`,
    description: chapter.abstract,
  };
}

export default function ChapterPage({ params }: { params: { id: string } }) {
  const id = parseInt(params.id, 10);
  if (isNaN(id) || id < 1 || id > 19) notFound();

  const chapter = getChapter(id);

  const prevId = id > 1 ? id - 1 : null;
  const nextId = id < 19 ? id + 1 : null;

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm text-slate-500">
        <Link href="/" className="hover:text-slate-800">Chapters</Link>
        <span>/</span>
        <span className="text-slate-800">Chapter {chapter.chapter}</span>
      </nav>

      {/* Chapter header */}
      <header className="space-y-3">
        <div className="flex items-center gap-3">
          <span className="flex h-10 w-10 items-center justify-center rounded-full bg-slate-900 text-base font-bold text-white">
            {chapter.chapter}
          </span>
          <span className="text-xs font-semibold uppercase tracking-widest text-slate-400">
            Chapter {chapter.chapter} of 19
          </span>
        </div>
        <h1 className="text-2xl font-bold leading-tight text-slate-900">{chapter.title}</h1>
        <p className="text-sm leading-relaxed text-slate-600">{chapter.abstract}</p>
        <div className="flex flex-wrap items-center gap-2 pt-1">
          <MarkReadButton chapterId={chapter.chapter} />
          <Link
            href={`/ask?chapter=${chapter.chapter}`}
            className="inline-flex items-center gap-1.5 rounded-full border border-indigo-200 bg-indigo-50 px-3 py-1.5 text-xs font-semibold text-indigo-700 transition hover:bg-indigo-100"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z" />
            </svg>
            Ask about this chapter
          </Link>
        </div>
      </header>

      {/* Overview */}
      <section className="rounded-lg bg-white p-6 shadow-sm ring-1 ring-slate-200">
        <h2 className="mb-3 text-xs font-semibold uppercase tracking-widest text-slate-400">Overview</h2>
        <p className="text-sm leading-relaxed text-slate-700">{chapter.overview}</p>
      </section>

      {/* Key Concepts */}
      {chapter.concepts.length > 0 && (
        <section>
          <h2 className="mb-3 text-xs font-semibold uppercase tracking-widest text-slate-400">
            Key Concepts ({chapter.concepts.length})
          </h2>
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
            {chapter.concepts.map((concept) => (
              <div key={concept.name} className="rounded-lg border border-slate-200 bg-white p-4">
                <h3 className="mb-1 text-sm font-semibold text-slate-900">{concept.name}</h3>
                <p className="text-xs leading-relaxed text-slate-600">{concept.definition}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Callouts */}
      <section>
        <h2 className="mb-1 text-xs font-semibold uppercase tracking-widest text-slate-400">
          Annotations &amp; Insights
        </h2>
        <div className="space-y-1">
          {chapter.callouts.map((callout, i) => (
            <CalloutRenderer key={i} callout={callout} />
          ))}
        </div>
      </section>

      {/* Connections */}
      {(chapter.connections.anticipates.length > 0 || chapter.connections.contrasts_with.length > 0) && (
        <section className="rounded-lg bg-slate-100 p-5">
          <h2 className="mb-3 text-xs font-semibold uppercase tracking-widest text-slate-500">
            Connections
          </h2>
          {chapter.connections.anticipates.length > 0 && (
            <div className="mb-3">
              <span className="text-xs font-semibold text-slate-600">Anticipates →</span>
              <ul className="mt-1 space-y-1">
                {chapter.connections.anticipates.map((ref, i) => (
                  <li key={i} className="text-xs text-slate-600">
                    {ref.chapter ? (
                      <Link href={`/chapter/${ref.chapter}`} className="font-medium text-blue-700 hover:underline">
                        Chapter {ref.chapter}
                      </Link>
                    ) : null}{' '}
                    — {ref.reason}
                  </li>
                ))}
              </ul>
            </div>
          )}
          {chapter.connections.contrasts_with.length > 0 && (
            <div>
              <span className="text-xs font-semibold text-slate-600">Contrasts with</span>
              <ul className="mt-1 space-y-1">
                {chapter.connections.contrasts_with.map((ref, i) => (
                  <li key={i} className="text-xs text-slate-600">
                    <span className="font-medium">{ref.concept}</span> — {ref.reason}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </section>
      )}

      {/* Prev / Next navigation */}
      <nav className="flex items-center justify-between border-t border-slate-200 pt-6">
        {prevId ? (
          <Link
            href={`/chapter/${prevId}`}
            className="flex items-center gap-1 rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100"
          >
            ← Chapter {prevId}
          </Link>
        ) : <span />}
        <Link href="/" className="text-sm text-slate-400 hover:text-slate-700">
          All chapters
        </Link>
        {nextId ? (
          <Link
            href={`/chapter/${nextId}`}
            className="flex items-center gap-1 rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100"
          >
            Chapter {nextId} →
          </Link>
        ) : <span />}
      </nav>
    </div>
  );
}
