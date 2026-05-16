import { getAllWorkedExamples } from '@/lib/content';
import WorkedExampleCard from '@/components/practice/WorkedExampleCard';
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

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {examples.map((we) => (
          <WorkedExampleCard key={we.id} we={we} />
        ))}
      </div>
    </div>
  );
}
