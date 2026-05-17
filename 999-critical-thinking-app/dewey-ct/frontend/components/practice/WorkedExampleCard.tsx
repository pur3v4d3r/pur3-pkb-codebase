import type { WorkedExample } from '@/types/framework';
import Link from 'next/link';

interface Props {
  we: WorkedExample;
}

const difficultyStyle: Record<string, string> = {
  beginner: 'bg-emerald-100 text-emerald-700',
  intermediate: 'bg-amber-100 text-amber-700',
  advanced: 'bg-red-100 text-red-700',
};

const frameworkStyle: Record<string, string> = {
  'paul-elder': 'bg-violet-100 text-violet-700',
  frisco: 'bg-blue-100 text-blue-700',
  'see-i': 'bg-teal-100 text-teal-700',
  metacognitive: 'bg-orange-100 text-orange-700',
};

export default function WorkedExampleCard({ we }: Props) {
  return (
    <div className="group flex flex-col gap-3 rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition-[box-shadow,border-color] duration-150 ease-in-out hover:border-slate-400 hover:shadow-md">
      <div className="flex items-start justify-between gap-3">
        <span className="shrink-0 rounded-md bg-slate-900 px-2 py-0.5 text-xs font-bold text-white">
          {we.we_number}
        </span>
        <div className="flex flex-wrap gap-1.5">
          <span
            className={`rounded-full px-2 py-0.5 text-xs font-medium ${frameworkStyle[we.framework] ?? 'bg-slate-100 text-slate-600'}`}
          >
            {we.framework_label}
          </span>
          <span
            className={`rounded-full px-2 py-0.5 text-xs font-medium ${difficultyStyle[we.difficulty] ?? 'bg-slate-100 text-slate-600'}`}
          >
            {we.difficulty}
          </span>
        </div>
      </div>

      <h3 className="text-sm font-semibold leading-snug text-slate-900 group-hover:text-blue-700">{we.title}</h3>

      <p className="text-xs leading-relaxed text-slate-500 line-clamp-3">{we.summary}</p>

      <div className="flex items-center justify-between pt-1">
        <div className="flex flex-col gap-0.5 text-xs text-slate-400">
          <span>{we.duration_minutes} min</span>
          {we.pre_confidence != null && we.post_confidence != null && (
            <span>
              Confidence: {we.pre_confidence} → {we.post_confidence}
            </span>
          )}
          {we.rigor_score != null && <span>Rigor: {we.rigor_score}/5</span>}
          {we.mastery_rating != null && <span>Mastery: {we.mastery_rating}/5</span>}
        </div>
        <Link
          href={`/practice/worked-examples/${we.id}`}
          className="rounded-md bg-slate-900 px-3 py-1.5 text-xs font-medium text-white transition hover:bg-slate-700"
        >
          Read Example →
        </Link>
      </div>
    </div>
  );
}
