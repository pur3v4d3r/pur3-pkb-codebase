import Link from 'next/link';
import { getCrosswalk } from '@/lib/chapter-crosswalk';

// Badge colour per framework family
const FRAMEWORK_COLOR: Record<string, string> = {
  'Paul-Elder': 'bg-indigo-100 text-indigo-800 border-indigo-200',
  'Delphi': 'bg-violet-100 text-violet-800 border-violet-200',
  'Ennis': 'bg-teal-100 text-teal-800 border-teal-200',
  'Dewey 5-Phase': 'bg-slate-200 text-slate-800 border-slate-300',
  'Toulmin': 'bg-amber-100 text-amber-800 border-amber-200',
  'Bloom': 'bg-emerald-100 text-emerald-800 border-emerald-200',
  'Lipman': 'bg-rose-100 text-rose-800 border-rose-200',
  'Brookfield': 'bg-rose-100 text-rose-800 border-rose-200',
  'Metacognition': 'bg-sky-100 text-sky-800 border-sky-200',
  'Socratic Questioning': 'bg-yellow-100 text-yellow-800 border-yellow-200',
};

function badgeClass(framework: string): string {
  return (
    FRAMEWORK_COLOR[framework] ??
    'bg-slate-100 text-slate-700 border-slate-200'
  );
}

export default function FrameworkCrosswalk({ chapterId }: { chapterId: number }) {
  const crosswalk = getCrosswalk(chapterId);
  if (!crosswalk || crosswalk.tags.length === 0) return null;

  return (
    <section className="rounded-lg border border-amber-100 bg-amber-50 p-5">
      <h2 className="mb-1 text-xs font-semibold uppercase tracking-widest text-amber-700">
        Framework Crosswalk
      </h2>
      <p className="mb-3 text-xs text-amber-600">
        This chapter maps to the following concepts in modern CT frameworks:
      </p>
      <div className="flex flex-wrap gap-2">
        {crosswalk.tags.map((tag, i) => (
          <Link
            key={i}
            href={tag.href}
            className={`inline-flex items-center gap-1 rounded-full border px-2.5 py-1 text-[11px] font-medium transition hover:opacity-80 ${badgeClass(tag.framework)}`}
            title={tag.framework}
          >
            <span className="font-semibold">{tag.framework}:</span>
            <span>{tag.concept}</span>
          </Link>
        ))}
      </div>
    </section>
  );
}
