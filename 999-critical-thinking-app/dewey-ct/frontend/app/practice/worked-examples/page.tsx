import { getAllWorkedExamples } from '@/lib/content';
import FilteredWorkedExampleGrid from '@/components/practice/FilteredWorkedExampleGrid';
import Link from 'next/link';

export const metadata = {
  title: 'Worked Examples — DeweyCT',
  description: 'Annotated critical thinking analyses across Paul-Elder, FRISCO, and SEE-I frameworks.',
};

export default function WorkedExamplesPage() {
  const examples = getAllWorkedExamples();

  return (
    <div className="mx-auto max-w-5xl space-y-8">
      <nav className="flex items-center gap-2 text-sm text-slate-500">
        <Link href="/practice" className="hover:text-slate-800">
          Practice
        </Link>
        <span>/</span>
        <span className="text-slate-800">Worked Examples</span>
      </nav>

      <header className="space-y-2">
        <h1 className="text-2xl font-bold text-slate-900">Worked Examples</h1>
        <p className="max-w-2xl text-sm leading-relaxed text-slate-600">
          Each worked example walks through a complete analysis — including pre/post confidence,
          standards audit, and learning objectives. Read these before attempting the corresponding
          practice problems.
        </p>
      </header>

      <FilteredWorkedExampleGrid examples={examples} />
    </div>
  );
}
