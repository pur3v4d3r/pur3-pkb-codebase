import { getAllWorkedExamples, getAllPracticeProblems } from '@/lib/content';
import WorkedExampleCard from '@/components/practice/WorkedExampleCard';
import PracticeProblemCard from '@/components/practice/PracticeProblemCard';
import Link from 'next/link';

export const metadata = {
  title: 'Practice — DeweyCT',
  description:
    'Deliberate practice for critical thinking: worked examples and practice problems across all frameworks.',
};

export default function PracticePage() {
  const workedExamples = getAllWorkedExamples();
  const practiceProblems = getAllPracticeProblems();

  return (
    <div className="mx-auto max-w-5xl space-y-14">
      {/* Hero */}
      <section className="space-y-3">
        <h1 className="text-3xl font-bold text-slate-900">Practice</h1>
        <p className="max-w-2xl text-base leading-relaxed text-slate-600">
          Deliberate practice is the fastest path from knowing the frameworks to using them fluently.
          Start with a worked example to see how an analysis is built from scratch, then attempt a
          practice problem independently before opening the template.
        </p>
        <div className="flex flex-wrap gap-3 pt-1 text-sm">
          <a href="#worked-examples" className="font-medium text-indigo-600 hover:underline">
            Worked Examples ({workedExamples.length})
          </a>
          <span className="text-slate-300">|</span>
          <a href="#practice-problems" className="font-medium text-indigo-600 hover:underline">
            Practice Problems ({practiceProblems.length})
          </a>
        </div>
      </section>

      {/* How to use this section */}
      <section className="rounded-xl border border-slate-200 bg-slate-50 p-6">
        <h2 className="mb-3 text-base font-semibold text-slate-800">
          Suggested workflow for each framework
        </h2>
        <ol className="space-y-2 text-sm leading-relaxed text-slate-600">
          <li>
            <span className="font-semibold text-slate-800">1. Read a worked example</span> — study
            how a complete analysis looks, including mistakes and confidence shifts.
          </li>
          <li>
            <span className="font-semibold text-slate-800">2. Attempt the practice problem</span> —
            try to solve it on paper or in a separate document before using hints.
          </li>
          <li>
            <span className="font-semibold text-slate-800">3. Open in Template</span> — use the
            interactive template to produce your full response with AI feedback.
          </li>
          <li>
            <span className="font-semibold text-slate-800">4. Compare against solution sketch</span>{' '}
            — the problem page shows key moves to look for, not a canonical answer.
          </li>
        </ol>
      </section>

      {/* Worked Examples */}
      <section id="worked-examples" className="space-y-5">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold text-slate-900">Worked Examples</h2>
          <Link
            href="/practice/worked-examples"
            className="text-sm text-indigo-600 hover:underline"
          >
            View all →
          </Link>
        </div>
        <p className="text-sm text-slate-500">
          Complete analyses with annotations, confidence tracking, and learning objectives. Read
          these before attempting the corresponding practice problems.
        </p>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {workedExamples.map((we) => (
            <WorkedExampleCard key={we.id} we={we} />
          ))}
        </div>
      </section>

      {/* Practice Problems */}
      <section id="practice-problems" className="space-y-5">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold text-slate-900">Practice Problems</h2>
          <Link href="/practice/problems" className="text-sm text-indigo-600 hover:underline">
            View all →
          </Link>
        </div>
        <p className="text-sm text-slate-500">
          Independent practice with hints, solution sketches, and direct links to the relevant
          template. Attempt problems without hints first.
        </p>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {practiceProblems.map((pp) => (
            <PracticeProblemCard key={pp.id} pp={pp} />
          ))}
        </div>
      </section>
    </div>
  );
}
