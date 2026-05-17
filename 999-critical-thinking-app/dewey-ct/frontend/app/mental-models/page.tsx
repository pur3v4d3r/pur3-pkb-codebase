import { getMentalModelsData } from '@/lib/content';
import MentalModelsHub from '@/components/mental-models/MentalModelsHub';
import ModelSelector from '@/components/mental-models/ModelSelector';

export const metadata = {
  title: 'Mental Models — DeweyCT',
  description:
    'A curated library of 30 deployable mental models for critical thinking — organized by category and Bloom level.',
};

export default function MentalModelsPage() {
  const data = getMentalModelsData();

  return (
    <div className="mx-auto max-w-5xl space-y-10">
      {/* Hero */}
      <section className="space-y-3">
        <h1 className="text-3xl font-bold tracking-tight text-slate-900">Mental Models</h1>
        <p className="max-w-2xl text-base leading-relaxed text-slate-600">
          {data.description.split('.')[0]}. These are not a comprehensive encyclopedia — they are a
          working toolkit.
        </p>
        <div className="rounded-lg border border-indigo-100 bg-indigo-50 p-4">
          <p className="text-xs font-semibold uppercase tracking-wider text-indigo-500">
            Dewey Integration
          </p>
          <p className="mt-1 text-sm leading-relaxed text-indigo-900">{data.dewey_integration}</p>
        </div>
      </section>

      {/* Situation-based model finder */}
      <ModelSelector models={data.models} />

      {/* Category overview */}
      <section className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-5">
        {data.categories.map((cat) => (
          <div
            key={cat.category}
            className="rounded-lg border border-slate-200 bg-white p-3 text-center"
          >
            <p className="text-xl font-bold text-slate-800">{cat.model_count}</p>
            <p className="mt-0.5 text-xs font-medium text-slate-600">{cat.category}</p>
          </div>
        ))}
      </section>

      {/* How to use */}
      <section className="rounded-xl border border-slate-200 bg-slate-50 p-6">
        <h2 className="mb-3 text-base font-semibold text-slate-800">How to use this library</h2>
        <ol className="space-y-2 text-sm leading-relaxed text-slate-600">
          <li>
            <span className="font-semibold text-slate-800">1. Filter by situation</span> — use
            Category to find models suited to your type of problem; use Bloom Level to find models
            appropriate to your current depth of practice.
          </li>
          <li>
            <span className="font-semibold text-slate-800">2. Read the full model</span> — each
            model shows When to Use, How to Apply (step-by-step), a concrete Example, and the
            Common Misuse to avoid.
          </li>
          <li>
            <span className="font-semibold text-slate-800">3. Apply in practice</span> — bring the
            model to a Practice Problem or Template session. Naming the model you are applying
            forces explicit reasoning rather than implicit pattern-matching.
          </li>
          <li>
            <span className="font-semibold text-slate-800">4. Internalize a small set deeply</span>{' '}
            — a few models you can apply instinctively outperform a large catalog you can only
            name.
          </li>
        </ol>
      </section>

      {/* Filterable model grid */}
      <MentalModelsHub models={data.models} categories={data.categories} />
    </div>
  );
}
