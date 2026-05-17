import { getCheatSheets } from '@/lib/content';
import CheatSheetsHub from '@/components/cheat-sheets/CheatSheetsHub';
import PrintButton from '@/components/cheat-sheets/PrintButton';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Cheat Sheets | DeweyCT',
  description:
    'Quick-reference cheat sheets for all 17 major critical thinking frameworks — from FRISCO to DIKW.',
};

export default function CheatSheetsPage() {
  const data = getCheatSheets();

  return (
    <div className="max-w-7xl mx-auto px-4 py-10">
      {/* Page header */}
      <div className="mb-8">
        <div className="flex items-start justify-between gap-4">
          <div>
            <h1 className="text-3xl font-bold text-slate-800 mb-2">Framework Cheat Sheets</h1>
            <p className="text-slate-600 max-w-2xl leading-relaxed print:hidden">
              The essential structure of every major critical thinking framework — under 30 seconds
              each. 17 frameworks, from FRISCO to DIKW, ready to deploy in any analysis.
            </p>
          </div>
          <PrintButton />
        </div>

        {/* Category stat strip */}
        <div className="flex flex-wrap gap-3 mt-6 print:hidden">
          {[
            { label: 'CT Frameworks', count: 5, color: 'text-indigo-600', bg: 'border-indigo-200 bg-indigo-50' },
            { label: 'Argument Analysis', count: 3, color: 'text-violet-600', bg: 'border-violet-200 bg-violet-50' },
            { label: 'Dispositions', count: 1, color: 'text-amber-600', bg: 'border-amber-200 bg-amber-50' },
            { label: 'Cognitive Models', count: 3, color: 'text-teal-600', bg: 'border-teal-200 bg-teal-50' },
            { label: 'Taxonomies', count: 5, color: 'text-emerald-600', bg: 'border-emerald-200 bg-emerald-50' },
          ].map(({ label, count, color, bg }) => (
            <div
              key={label}
              className={`border rounded-lg px-4 py-2 text-center min-w-[120px] ${bg}`}
            >
              <div className={`text-2xl font-bold ${color}`}>{count}</div>
              <div className="text-xs text-slate-500 mt-0.5">{label}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Usage tip */}
      <div className="bg-indigo-50 border border-indigo-200 rounded-xl p-4 mb-8 flex gap-3 print:hidden">
        <span className="text-indigo-400 flex-shrink-0 mt-0.5">💡</span>
        <p className="text-sm text-indigo-800 leading-relaxed">
          <span className="font-semibold">How to use:</span> Scan a sheet before starting any
          analysis to activate the right mental structure. Pick the framework that fits your task,
          note the key elements, then apply. The{' '}
          <a href="/ask" className="underline hover:text-indigo-600">
            AI Tutor
          </a>{' '}
          can walk you through any framework interactively.
        </p>
      </div>

      <CheatSheetsHub sheets={data.sheets} />
    </div>
  );
}
