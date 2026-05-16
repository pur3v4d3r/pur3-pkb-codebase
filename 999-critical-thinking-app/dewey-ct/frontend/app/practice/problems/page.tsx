import { getAllPracticeProblems } from '@/lib/content';
import PracticeProblemCard from '@/components/practice/PracticeProblemCard';
import Link from 'next/link';

export const metadata = {
  title: 'Practice Problems — DeweyCT',
  description: 'Critical thinking practice problems across Paul-Elder, FRISCO, SEE-I, and metacognitive frameworks.',
};

export default function PracticeProblemsPage() {
  const problems = getAllPracticeProblems();

  return (
    <div className="mx-auto max-w-5xl space-y-8">
      <nav className="flex items-center gap-2 text-sm text-slate-500">
        <Link href="/practice" className="hover:text-slate-800">
          Practice
        </Link>
        <span>/</span>
        <span className="text-slate-800">Practice Problems</span>
      </nav>

      <header className="space-y-2">
        <h1 className="text-2xl font-bold text-slate-900">Practice Problems</h1>
        <p className="max-w-2xl text-sm leading-relaxed text-slate-600">
          Each problem includes a context, instructions, and optional hints. Attempt the problem
          independently before using hints or viewing the solution sketch. Use the &quot;Open in
          Template&quot; link to generate structured AI feedback on your response.
        </p>
      </header>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {problems.map((pp) => (
          <PracticeProblemCard key={pp.id} pp={pp} />
        ))}
      </div>
    </div>
  );
}
