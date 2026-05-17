import { getPracticeProblem, type PracticeProblemId } from '@/lib/content';
import HintAccordion from '@/components/practice/HintAccordion';
import Link from 'next/link';
import { notFound } from 'next/navigation';

const VALID_IDS = [
  'PP-01', 'PP-02', 'PP-03', 'PP-04',
  'PP-05', 'PP-06', 'PP-07', 'PP-08',
  'PP-09', 'PP-10', 'PP-11', 'PP-12',
  'PP-13', 'PP-14', 'PP-15', 'PP-16',
  'PP-17', 'PP-18', 'PP-19', 'PP-20', 'PP-21', 'PP-22',
  'PP-23', 'PP-24', 'PP-25', 'PP-26', 'PP-27', 'PP-28',
] satisfies PracticeProblemId[];

export function generateStaticParams() {
  return VALID_IDS.map((id) => ({ id }));
}

export async function generateMetadata({ params }: { params: { id: string } }) {
  if (!VALID_IDS.includes(params.id as PracticeProblemId)) return {};
  const pp = getPracticeProblem(params.id as PracticeProblemId);
  return {
    title: `${pp.pp_number}: ${pp.title} — DeweyCT`,
  };
}

const difficultyStyle: Record<string, string> = {
  easy: 'bg-emerald-100 text-emerald-700',
  medium: 'bg-amber-100 text-amber-700',
  hard: 'bg-red-100 text-red-700',
};

export default function PracticeProblemDetailPage({ params }: { params: { id: string } }) {
  if (!VALID_IDS.includes(params.id as PracticeProblemId)) notFound();

  const pp = getPracticeProblem(params.id as PracticeProblemId);

  return (
    <div className="mx-auto max-w-3xl space-y-10">
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm text-slate-500">
        <Link href="/practice" className="hover:text-slate-800">
          Practice
        </Link>
        <span>/</span>
        <Link href="/practice/problems" className="hover:text-slate-800">
          Problems
        </Link>
        <span>/</span>
        <span className="text-slate-800">{pp.pp_number}</span>
      </nav>

      {/* Header */}
      <header className="space-y-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className="rounded-md bg-slate-900 px-2 py-0.5 text-xs font-bold text-white">
            {pp.pp_number}
          </span>
          <span className="rounded-full bg-violet-100 px-2 py-0.5 text-xs font-medium text-violet-700">
            {pp.framework_label}
          </span>
          <span
            className={`rounded-full px-2 py-0.5 text-xs font-medium ${difficultyStyle[pp.difficulty] ?? 'bg-slate-100 text-slate-600'}`}
          >
            {pp.difficulty}
          </span>
          <span className="text-xs text-slate-400">{pp.estimated_minutes} min</span>
        </div>
        <h1 className="text-xl font-bold leading-snug text-slate-900">{pp.title}</h1>
      </header>

      {/* Object of analysis */}
      <section className="space-y-2">
        <h2 className="text-base font-semibold text-slate-800">Object of Analysis</h2>
        <blockquote className="rounded-lg border-l-4 border-slate-300 bg-slate-50 px-4 py-3 text-sm italic leading-relaxed text-slate-700">
          {pp.object_of_analysis}
        </blockquote>
      </section>

      {/* Context */}
      {pp.context && (
        <section className="space-y-2">
          <h2 className="text-base font-semibold text-slate-800">Context</h2>
          <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-600">{pp.context}</p>
        </section>
      )}

      {/* Instructions */}
      <section className="space-y-2">
        <h2 className="text-base font-semibold text-slate-800">Instructions</h2>
        <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-600">
          {pp.instructions}
        </p>
      </section>

      {/* Workspace prompts */}
      {pp.workspace_prompts && Object.keys(pp.workspace_prompts).length > 0 && (
        <section className="space-y-3">
          <h2 className="text-base font-semibold text-slate-800">Workspace Prompts</h2>
          <dl className="space-y-4">
            {Object.entries(pp.workspace_prompts).map(([key, value]) => (
              <div key={key} className="space-y-1">
                <dt className="text-xs font-semibold uppercase tracking-wide text-slate-500">
                  {key}
                </dt>
                <dd className="text-sm leading-relaxed text-slate-600">{value}</dd>
              </div>
            ))}
          </dl>
        </section>
      )}

      {/* Open in Template CTA */}
      {pp.template_prefill && (
      <section className="rounded-xl border border-indigo-200 bg-indigo-50 p-5">
        <p className="mb-3 text-sm text-indigo-800">
          Ready to work through this problem? Open the template with this problem&apos;s context
          pre-loaded and submit your response for AI feedback.
        </p>
        <Link
          href={`/templates/${pp.template_prefill.template_id}?context=${pp.id}`}
          className="inline-block rounded-md bg-indigo-600 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-indigo-700"
        >
          Open in Template →
        </Link>
      </section>
      )}

      {/* Hints (collapsible) */}
      {pp.hints.length > 0 && (
        <section className="space-y-3">
          <h2 className="text-base font-semibold text-slate-800">
            Hints{' '}
            <span className="text-sm font-normal text-slate-400">(expand after attempting)</span>
          </h2>
          <HintAccordion hints={pp.hints} />
        </section>
      )}

      {/* Solution sketch (collapsible-ish — static collapsed via details/summary) */}
      <section className="space-y-3">
        <h2 className="text-base font-semibold text-slate-800">Solution Sketch</h2>
        <details className="rounded-lg border border-slate-200 overflow-hidden">
          <summary className="cursor-pointer px-4 py-3 text-sm font-medium text-slate-600 hover:bg-slate-50">
            Reveal key moves (complete your own analysis first)
          </summary>
          <div className="border-t border-slate-100 p-4 space-y-3">
            <ul className="space-y-3">
              {pp.solution_sketch.key_moves.map((move, i) => (
                <li key={i} className="flex gap-2 text-sm leading-relaxed text-slate-700">
                  <span className="shrink-0 font-semibold text-slate-400">{i + 1}.</span>
                  {move}
                </li>
              ))}
            </ul>
            {pp.solution_sketch.revised_position && (
              <div className="mt-4 rounded-md bg-slate-50 px-4 py-3 text-sm text-slate-600">
                <span className="font-semibold text-slate-800">Revised position: </span>
                {pp.solution_sketch.revised_position}
              </div>
            )}
          </div>
        </details>
      </section>

      {/* Related links */}
      <footer className="flex flex-wrap gap-3 border-t border-slate-200 pt-6">
        {pp.related_worked_example_id && (
          <Link
            href={`/practice/worked-examples/${pp.related_worked_example_id}`}
            className="rounded-md border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-50"
          >
            See Worked Example: {pp.related_worked_example_id}
          </Link>
        )}
        {pp.template_prefill && (
          <Link
            href={`/templates/${pp.template_prefill.template_id}?context=${pp.id}`}
            className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-700"
          >
            Open in Template →
          </Link>
        )}
      </footer>
    </div>
  );
}
