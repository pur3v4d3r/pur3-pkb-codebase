import { getMentalModelsData } from '@/lib/content';
import Link from 'next/link';
import { notFound } from 'next/navigation';

// ---- Static params for SSG ----

export async function generateStaticParams() {
  const data = getMentalModelsData();
  return data.models.map((m) => ({ id: m.id }));
}

// ---- Metadata ----

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const data = getMentalModelsData();
  const model = data.models.find((m) => m.id === id);
  if (!model) return { title: 'Not Found — DeweyCT' };
  return {
    title: `${model.name} — Mental Models — DeweyCT`,
    description: model.definition.slice(0, 160),
  };
}

// ---- Colour maps ----

const CATEGORY_COLORS: Record<string, string> = {
  'Reasoning and Logic': 'bg-indigo-50 text-indigo-700 border-indigo-200',
  'Systems Thinking': 'bg-teal-50 text-teal-700 border-teal-200',
  'Decision Making': 'bg-amber-50 text-amber-700 border-amber-200',
  'Cognitive Biases': 'bg-rose-50 text-rose-700 border-rose-200',
  Epistemology: 'bg-violet-50 text-violet-700 border-violet-200',
};

const BLOOM_COLORS: Record<string, string> = {
  Remember: 'bg-slate-100 text-slate-700',
  Understand: 'bg-blue-50 text-blue-700',
  Apply: 'bg-green-50 text-green-700',
  Analyze: 'bg-amber-50 text-amber-800',
  Evaluate: 'bg-orange-50 text-orange-700',
  Create: 'bg-purple-50 text-purple-700',
};

// ---- Page ----

export default async function MentalModelDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const data = getMentalModelsData();
  const model = data.models.find((m) => m.id === id);

  if (!model) notFound();

  const catCls = CATEGORY_COLORS[model.category] ?? 'bg-slate-50 text-slate-700 border-slate-200';
  const bloomCls = BLOOM_COLORS[model.bloom_level] ?? 'bg-slate-100 text-slate-700';

  // Sibling models in same category
  const siblings = data.models
    .filter((m) => m.category === model.category && m.id !== model.id)
    .slice(0, 4);

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      {/* Back */}
      <div>
        <Link
          href="/mental-models"
          className="inline-flex items-center gap-1 text-xs font-medium text-slate-500 hover:text-slate-800"
        >
          ← Mental Models
        </Link>
      </div>

      {/* Header */}
      <div className="space-y-3">
        <div className="flex flex-wrap items-center gap-2">
          <span className={`inline-flex items-center rounded border px-2 py-0.5 text-xs font-medium ${catCls}`}>
            {model.category}
          </span>
          <span className={`inline-flex items-center rounded px-2 py-0.5 text-xs font-medium ${bloomCls}`}>
            Bloom: {model.bloom_level}
          </span>
          {model.paul_elder_element && (
            <span className="inline-flex items-center rounded bg-slate-100 px-2 py-0.5 text-xs font-medium text-slate-600">
              Paul-Elder: {model.paul_elder_element}
            </span>
          )}
        </div>
        <h1 className="text-2xl font-bold tracking-tight text-slate-900">{model.name}</h1>
        {model.origin && (
          <p className="text-xs italic text-slate-500">Origin: {model.origin}</p>
        )}
      </div>

      {/* Definition */}
      <section className="space-y-2">
        <h2 className="text-xs font-semibold uppercase tracking-wider text-slate-500">Definition</h2>
        <p className="text-sm leading-relaxed text-slate-700">{model.definition}</p>
      </section>

      {/* When to use */}
      <section className="space-y-2">
        <h2 className="text-xs font-semibold uppercase tracking-wider text-slate-500">
          When to Use
        </h2>
        <p className="text-sm leading-relaxed text-slate-700">{model.when_to_use}</p>
      </section>

      {/* How to apply */}
      <section className="space-y-2">
        <h2 className="text-xs font-semibold uppercase tracking-wider text-slate-500">
          How to Apply
        </h2>
        <ol className="space-y-2">
          {model.how_to_apply.map((step, i) => (
            <li key={i} className="flex gap-3 text-sm text-slate-700">
              <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-slate-200 text-[11px] font-bold text-slate-600">
                {i + 1}
              </span>
              <span className="leading-relaxed">{step}</span>
            </li>
          ))}
        </ol>
      </section>

      {/* Dewey connection callout */}
      {model.dewey_connection && (
        <section className="rounded-lg border border-indigo-100 bg-indigo-50 p-4">
          <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-indigo-500">
            Dewey Connection
          </p>
          <p className="text-sm leading-relaxed text-indigo-900">{model.dewey_connection}</p>
        </section>
      )}

      {/* Example */}
      {model.example && (
        <section className="space-y-2">
          <h2 className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            Concrete Example
          </h2>
          <div className="rounded-lg border border-slate-200 bg-slate-50 p-4">
            <p className="text-sm leading-relaxed text-slate-700">{model.example}</p>
          </div>
        </section>
      )}

      {/* Common misuse warning */}
      {model.common_misuse && (
        <section className="rounded-lg border border-rose-100 bg-rose-50 p-4">
          <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-rose-500">
            Common Misuse — Avoid This
          </p>
          <p className="text-sm leading-relaxed text-rose-900">{model.common_misuse}</p>
        </section>
      )}

      {/* Related models in same category */}
      {siblings.length > 0 && (
        <section className="space-y-3 border-t border-slate-200 pt-8">
          <h2 className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            More in {model.category}
          </h2>
          <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
            {siblings.map((s) => (
              <Link
                key={s.id}
                href={`/mental-models/${s.id}`}
                className="group rounded-md border border-slate-200 bg-white p-3 transition hover:border-slate-400"
              >
                <p className="text-sm font-medium text-slate-800 group-hover:text-indigo-700">
                  {s.name}
                </p>
                <p className="mt-0.5 text-xs text-slate-500 line-clamp-1">{s.definition.slice(0, 80)}…</p>
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* Footer nav */}
      <div className="border-t border-slate-200 pt-6">
        <Link
          href="/mental-models"
          className="text-sm font-medium text-indigo-600 hover:underline"
        >
          ← Back to all mental models
        </Link>
      </div>
    </div>
  );
}
