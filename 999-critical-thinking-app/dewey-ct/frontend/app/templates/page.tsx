import Link from 'next/link';
import { getAllTemplates } from '@/lib/content';
import type { RawTemplate } from '@/components/template/TemplateForm';

const difficultyColors: Record<string, string> = {
  beginner: 'bg-green-100 text-green-700',
  intermediate: 'bg-yellow-100 text-yellow-700',
  advanced: 'bg-red-100 text-red-700',
};

export default function TemplatesPage() {
  const templates = getAllTemplates() as unknown as RawTemplate[];

  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <h1 className="text-2xl font-bold tracking-tight text-slate-900">Thinking Templates</h1>
        <p className="text-sm text-slate-500">
          {templates.length} structured worksheets — apply critical-thinking frameworks to real problems
        </p>
      </div>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        {templates.map((t) => (
          <Link
            key={t.template_id}
            href={`/templates/${t.template_id}`}
            className="group rounded-lg border border-slate-200 bg-white dark:bg-slate-700 p-5 shadow-sm transition-[box-shadow,border-color] duration-150 ease-in-out hover:border-slate-400 hover:shadow-md dark:border-slate-600 dark:hover:bg-slate-600"
          >
            <div className="mb-2 flex flex-wrap items-center gap-2">
              <h2 className="text-base font-semibold text-slate-900 group-hover:text-blue-700 dark:text-slate-100 dark:group-hover:text-blue-400">
                {t.name}
              </h2>
              {t.difficulty && (
                <span className={`rounded-full px-2 py-0.5 text-xs font-medium ${difficultyColors[t.difficulty] ?? 'bg-slate-100 text-slate-600'}`}>
                  {t.difficulty}
                </span>
              )}
            </div>
            <p className="text-sm leading-relaxed text-slate-600">{t.description}</p>
            <div className="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-400">
              {t.framework && <span>{t.framework}</span>}
              {t.estimated_time_minutes && <span>~{t.estimated_time_minutes} min</span>}
              {t.fields && <span>{t.fields.length} fields</span>}
            </div>
            <p className="mt-3 text-xs font-medium text-slate-500 group-hover:text-blue-600 dark:group-hover:text-blue-400">
              Open template →
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}
