import type { PracticeProblem } from '@/types/framework';
import Link from 'next/link';

interface Props {
  pp: PracticeProblem;
}

const difficultyStyle: Record<string, string> = {
  easy: 'bg-emerald-100 text-emerald-700',
  medium: 'bg-amber-100 text-amber-700',
  hard: 'bg-red-100 text-red-700',
};

const frameworkStyle: Record<string, string> = {
  'paul-elder': 'bg-violet-100 text-violet-700',
  frisco: 'bg-blue-100 text-blue-700',
  'see-i': 'bg-teal-100 text-teal-700',
  metacognitive: 'bg-orange-100 text-orange-700',
};

export default function PracticeProblemCard({ pp }: Props) {
  return (
    <div className="flex flex-col gap-3 rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <div className="flex items-start justify-between gap-3">
        <span className="shrink-0 rounded-md bg-slate-900 px-2 py-0.5 text-xs font-bold text-white">
          {pp.pp_number}
        </span>
        <div className="flex flex-wrap gap-1.5">
          <span
            className={`rounded-full px-2 py-0.5 text-xs font-medium ${frameworkStyle[pp.framework] ?? 'bg-slate-100 text-slate-600'}`}
          >
            {pp.framework_label}
          </span>
          <span
            className={`rounded-full px-2 py-0.5 text-xs font-medium ${difficultyStyle[pp.difficulty] ?? 'bg-slate-100 text-slate-600'}`}
          >
            {pp.difficulty}
          </span>
        </div>
      </div>

      <h3 className="text-sm font-semibold leading-snug text-slate-900">{pp.title}</h3>

      <div className="text-xs text-slate-400">{pp.estimated_minutes} min estimated</div>

      <div className="flex flex-col gap-2 pt-1 sm:flex-row sm:items-center sm:justify-between">
        <Link
          href={`/practice/problems/${pp.id}`}
          className="rounded-md border border-slate-300 px-3 py-1.5 text-center text-xs font-medium text-slate-700 transition hover:bg-slate-50"
        >
          View Problem
        </Link>
        <Link
          href={`/templates/${pp.template_prefill.template_id}?context=${pp.id}`}
          className="rounded-md bg-slate-900 px-3 py-1.5 text-center text-xs font-medium text-white transition hover:bg-slate-700"
        >
          Open in Template →
        </Link>
      </div>
    </div>
  );
}
