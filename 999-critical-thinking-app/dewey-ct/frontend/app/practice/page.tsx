import { getAllWorkedExamples, getAllPracticeProblems } from '@/lib/content';
import PracticeFilters from '@/components/practice/PracticeFilters';

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

      <PracticeFilters workedExamples={workedExamples} practiceProblems={practiceProblems} />
    </div>
  );
}
