import type { ChapterSummary } from '@/types/chapter';
import Link from 'next/link';

const PART_LABELS: Record<number, string> = {
  1: 'Part I', 2: 'Part I', 3: 'Part I', 4: 'Part I', 5: 'Part I', 6: 'Part I',
  7: 'Part II', 8: 'Part II', 9: 'Part II', 10: 'Part II', 11: 'Part II',
  12: 'Part III', 13: 'Part III', 14: 'Part III', 15: 'Part III',
  16: 'Part III', 17: 'Part III', 18: 'Part III', 19: 'Part III',
};

const PART_COLORS: Record<string, string> = {
  'Part I': 'bg-amber-100 text-amber-800',
  'Part II': 'bg-blue-100 text-blue-800',
  'Part III': 'bg-emerald-100 text-emerald-800',
};

interface ChapterCardProps {
  summary: ChapterSummary;
  isRead?: boolean;
}

export default function ChapterCard({ summary, isRead }: ChapterCardProps) {
  const part = PART_LABELS[summary.chapter] ?? '';
  const partColor = PART_COLORS[part] ?? 'bg-slate-100 text-slate-700';
  const totalCallouts = Object.values(summary.calloutCounts).reduce((a, b) => a + b, 0);

  return (
    <Link href={`/chapter/${summary.chapter}`}>
      <article className="group flex flex-col gap-3 rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:border-slate-400 hover:shadow-md h-full">
        {/* Header */}
        <div className="flex items-start justify-between gap-2">
          <div className="flex items-center gap-2">
            <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-900 text-sm font-bold text-white">
              {summary.chapter}
            </span>
            {isRead && (
              <span className="text-xs font-medium text-emerald-600">✓ Read</span>
            )}
          </div>
          <span className={`rounded-full px-2 py-0.5 text-xs font-semibold ${partColor}`}>
            {part}
          </span>
        </div>

        {/* Title */}
        <h2 className="text-base font-semibold leading-snug text-slate-900 group-hover:text-blue-700">
          {summary.title}
        </h2>

        {/* Abstract */}
        <p className="flex-1 text-sm leading-relaxed text-slate-600 line-clamp-3">
          {summary.abstract}
        </p>

        {/* Footer stats */}
        <div className="flex flex-wrap gap-1.5 pt-1">
          <Pill label={`${summary.conceptCount} concepts`} />
          {summary.calloutCounts.quote && (
            <Pill label={`${summary.calloutCounts.quote} quotes`} />
          )}
          {totalCallouts > 0 && (
            <Pill label={`${totalCallouts} callouts`} />
          )}
        </div>
      </article>
    </Link>
  );
}

function Pill({ label }: { label: string }) {
  return (
    <span className="rounded-full bg-slate-100 px-2.5 py-0.5 text-xs text-slate-600">
      {label}
    </span>
  );
}
