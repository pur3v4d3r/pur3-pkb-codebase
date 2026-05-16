import { getWorkedExample, type WorkedExampleId } from '@/lib/content';
import Link from 'next/link';
import { notFound } from 'next/navigation';

const VALID_IDS = ['WE-01', 'WE-02', 'WE-03'] satisfies WorkedExampleId[];

export function generateStaticParams() {
  return VALID_IDS.map((id) => ({ id }));
}

export async function generateMetadata({ params }: { params: { id: string } }) {
  if (!VALID_IDS.includes(params.id as WorkedExampleId)) return {};
  const we = getWorkedExample(params.id as WorkedExampleId);
  return {
    title: `${we.we_number}: ${we.title} — DeweyCT`,
    description: we.summary,
  };
}

const difficultyStyle: Record<string, string> = {
  beginner: 'bg-emerald-100 text-emerald-700',
  intermediate: 'bg-amber-100 text-amber-700',
  advanced: 'bg-red-100 text-red-700',
};

export default function WorkedExampleDetailPage({ params }: { params: { id: string } }) {
  if (!VALID_IDS.includes(params.id as WorkedExampleId)) notFound();

  const we = getWorkedExample(params.id as WorkedExampleId);

  return (
    <div className="mx-auto max-w-3xl space-y-10">
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm text-slate-500">
        <Link href="/practice" className="hover:text-slate-800">
          Practice
        </Link>
        <span>/</span>
        <Link href="/practice/worked-examples" className="hover:text-slate-800">
          Worked Examples
        </Link>
        <span>/</span>
        <span className="text-slate-800">{we.we_number}</span>
      </nav>

      {/* Header */}
      <header className="space-y-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className="rounded-md bg-slate-900 px-2 py-0.5 text-xs font-bold text-white">
            {we.we_number}
          </span>
          <span className="rounded-full bg-violet-100 px-2 py-0.5 text-xs font-medium text-violet-700">
            {we.framework_label}
          </span>
          <span
            className={`rounded-full px-2 py-0.5 text-xs font-medium ${difficultyStyle[we.difficulty] ?? 'bg-slate-100 text-slate-600'}`}
          >
            {we.difficulty}
          </span>
        </div>
        <h1 className="text-xl font-bold leading-snug text-slate-900">{we.title}</h1>
        {we.subtitle && <p className="text-sm text-slate-500">{we.subtitle}</p>}

        {/* Stats row */}
        <div className="flex flex-wrap gap-4 border-t border-slate-100 pt-3 text-xs text-slate-500">
          <span>{we.duration_minutes} min</span>
          {we.pre_confidence != null && we.post_confidence != null && (
            <span>
              Confidence: {we.pre_confidence} → {we.post_confidence}
            </span>
          )}
          {we.rigor_score != null && <span>Rigor: {we.rigor_score}/5</span>}
          {we.mastery_rating != null && <span>Mastery rating: {we.mastery_rating}/5</span>}
        </div>
      </header>

      {/* Summary & how to use */}
      <section className="space-y-3 rounded-xl border border-slate-200 bg-slate-50 p-5">
        <p className="text-sm leading-relaxed text-slate-700">{we.summary}</p>
        <p className="text-sm leading-relaxed text-slate-600">
          <span className="font-semibold text-slate-800">How to use: </span>
          {we.how_to_use}
        </p>
      </section>

      {/* Learning objectives */}
      {we.learning_objectives?.length > 0 && (
        <section className="space-y-2">
          <h2 className="text-base font-semibold text-slate-800">Learning Objectives</h2>
          <ul className="space-y-1.5">
            {we.learning_objectives.map((obj, i) => (
              <li key={i} className="flex gap-2 text-sm text-slate-600">
                <span className="mt-0.5 text-indigo-400">•</span>
                {obj}
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* Sections */}
      <div className="space-y-8">
        {we.sections.map((section, i) => (
          <section key={i} className="space-y-3">
            <h2 className="border-b border-slate-200 pb-1.5 text-base font-semibold text-slate-800">
              {section.section_label}
            </h2>
            {section.content && (
              <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
                {section.content}
              </p>
            )}
            {section.fields && (
              <dl className="space-y-4">
                {section.fields.map((field, j) => (
                  <div key={j} className="space-y-1">
                    <dt className="text-xs font-semibold uppercase tracking-wide text-slate-500">
                      {field.label}
                    </dt>
                    <dd className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
                      {field.content}
                    </dd>
                  </div>
                ))}
              </dl>
            )}
          </section>
        ))}
      </div>

      {/* Related links */}
      <footer className="flex flex-wrap gap-3 border-t border-slate-200 pt-6">
        {we.related_template_id && (
          <Link
            href={`/templates/${we.related_template_id}`}
            className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-700"
          >
            Open Template →
          </Link>
        )}
        {we.related_practice_problems?.map((ppId) => (
          <Link
            key={ppId}
            href={`/practice/problems/${ppId}`}
            className="rounded-md border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-50"
          >
            Practice: {ppId}
          </Link>
        ))}
      </footer>
    </div>
  );
}
