'use client';

import { useState, useEffect } from 'react';

// ---- Types ----

interface QuizQuestion {
  id: string;
  text: string;
  options: { label: string; value: number; tag: string }[];
}

interface GoalEntry {
  id: string;
  goal: string;
  whyItMatters: string;
  schedule: string;
  accountability: string;
  savedAt: string;
}

type MotivationProfile = 'intrinsic' | 'integrated' | 'identified' | 'extrinsic';
type MotivationTab = 'quiz' | 'goals';

// ---- Constants ----

const GOALS_KEY = 'deweyct-motivation-goals';
const QUIZ_RESULTS_KEY = 'deweyct-motivation-quiz';

const QUIZ_QUESTIONS: QuizQuestion[] = [
  {
    id: 'q1',
    text: 'When you engage with a difficult argument or problem, which feels most true?',
    options: [
      { label: 'I genuinely enjoy the puzzle — figuring it out feels rewarding in itself.', value: 4, tag: 'intrinsic' },
      { label: 'I find it meaningful because it connects to values I care about.', value: 3, tag: 'integrated' },
      { label: 'I do it because I know it will pay off (grades, work, reputation).', value: 2, tag: 'identified' },
      { label: 'I usually only engage when there is pressure or a clear reward.', value: 1, tag: 'extrinsic' },
    ],
  },
  {
    id: 'q2',
    text: 'When you are free to choose what to learn, you gravitate toward:',
    options: [
      { label: 'Topics that fascinate me, regardless of usefulness.', value: 4, tag: 'intrinsic' },
      { label: 'Things that align with who I want to become.', value: 3, tag: 'integrated' },
      { label: 'Skills that clearly build toward a goal I have.', value: 2, tag: 'identified' },
      { label: 'Whatever is expected or assigned.', value: 1, tag: 'extrinsic' },
    ],
  },
  {
    id: 'q3',
    text: 'After a hard thinking session where you made genuine progress, you feel:',
    options: [
      { label: 'Energised — I want to keep going.', value: 4, tag: 'intrinsic' },
      { label: 'Satisfied — this is who I am working to become.', value: 3, tag: 'integrated' },
      { label: 'Accomplished — another step toward my goal.', value: 2, tag: 'identified' },
      { label: 'Relieved — glad that is done.', value: 1, tag: 'extrinsic' },
    ],
  },
  {
    id: 'q4',
    text: 'Procrastination hits hardest when:',
    options: [
      { label: 'Almost never — when I am curious, I just start.', value: 4, tag: 'intrinsic' },
      { label: 'When I lose sight of why this matters to me personally.', value: 3, tag: 'integrated' },
      { label: 'When the goal feels distant or the steps are unclear.', value: 2, tag: 'identified' },
      { label: 'Often — I need external deadlines to get moving.', value: 1, tag: 'extrinsic' },
    ],
  },
  {
    id: 'q5',
    text: 'If there were zero external rewards for practising critical thinking, would you still do it?',
    options: [
      { label: 'Yes — thinking well is its own reward.', value: 4, tag: 'intrinsic' },
      { label: 'Yes — it is central to who I want to be.', value: 3, tag: 'integrated' },
      { label: 'Probably — I see the long-term value even without immediate rewards.', value: 2, tag: 'identified' },
      { label: 'Unlikely — the external payoff is the main driver.', value: 1, tag: 'extrinsic' },
    ],
  },
];

const PROFILES: Record<MotivationProfile, { title: string; color: string; bg: string; border: string; description: string; strategies: string[] }> = {
  intrinsic: {
    title: 'Intrinsically Driven',
    color: 'text-emerald-700',
    bg: 'bg-emerald-50',
    border: 'border-emerald-200',
    description:
      'You engage with critical thinking because you find it genuinely rewarding. Curiosity and the joy of understanding are your fuel. Your challenge is sustaining breadth — you may stay in comfortable intellectual territory. Push yourself toward topics that initially feel alien.',
    strategies: [
      'Follow curiosity aggressively — let one question spawn three more.',
      'Keep a "thinking log" to capture insight sparks before they fade.',
      'Seek out domains you know nothing about to maintain the novelty that drives you.',
      'Teach others — explaining deepens intrinsic understanding.',
    ],
  },
  integrated: {
    title: 'Identity-Integrated',
    color: 'text-indigo-700',
    bg: 'bg-indigo-50',
    border: 'border-indigo-200',
    description:
      'Your motivation is anchored in your sense of self — critical thinking is part of who you are or aspire to be. This is the most durable form of motivation. When engagement dips, reconnect to values rather than outcomes.',
    strategies: [
      'Write a personal "thinking manifesto" — why does rigorous thought matter to you?',
      'Identify role models who embody the critical thinker you want to become.',
      'Audit your daily environment: does it reflect your identity as a thinker?',
      'Use the identity statement: "I am someone who examines evidence before concluding."',
    ],
  },
  identified: {
    title: 'Goal-Identified',
    color: 'text-amber-700',
    bg: 'bg-amber-50',
    border: 'border-amber-200',
    description:
      'You see the value in critical thinking and engage because of clear goals, even if it doesn\'t always feel intrinsically rewarding. You are well-positioned to deepen motivation by building the identity layer. Consistent goal achievement will generate genuine interest over time.',
    strategies: [
      'Break large goals into visible milestones to maintain the sense of progress.',
      'Pair CT practice with something you already enjoy (habit stacking).',
      'Reflect on past wins: when did your thinking actually change an outcome?',
      'Use implementation intentions: "When I sit down at 9am, I will do 25 minutes of CT practice."',
    ],
  },
  extrinsic: {
    title: 'Externally Motivated',
    color: 'text-rose-700',
    bg: 'bg-rose-50',
    border: 'border-rose-200',
    description:
      'External rewards and pressure are your current primary drivers. This is a starting point, not a fixed trait. The goal is to gradually internalise motivation by finding small moments of genuine interest, connecting practice to personal values, and reducing reliance on external scaffolding over time.',
    strategies: [
      'Start with the Pomodoro Technique — 25-min focused sprints lower the activation cost.',
      'Seek out the one sub-topic of CT that genuinely interests you and start there.',
      'Create your own rewards tied directly to practice (e.g. after 3 sessions, do something you enjoy).',
      'Find a thinking partner — social accountability is a bridge to internalised motivation.',
    ],
  },
};

// ---- Storage helpers ----

function loadGoals(): GoalEntry[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(GOALS_KEY);
    return raw ? (JSON.parse(raw) as GoalEntry[]) : [];
  } catch { return []; }
}

function saveGoal(entry: GoalEntry): void {
  const goals = loadGoals();
  const idx = goals.findIndex((g) => g.id === entry.id);
  if (idx >= 0) goals[idx] = entry; else goals.push(entry);
  localStorage.setItem(GOALS_KEY, JSON.stringify(goals));
}

function deleteGoal(id: string): void {
  const goals = loadGoals().filter((g) => g.id !== id);
  localStorage.setItem(GOALS_KEY, JSON.stringify(goals));
}

function loadSavedQuizResult(): { answers: Record<string, number>; profile: MotivationProfile; score: number } | null {
  if (typeof window === 'undefined') return null;
  try {
    const raw = localStorage.getItem(QUIZ_RESULTS_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch { return null; }
}

function saveQuizResult(answers: Record<string, number>, profile: MotivationProfile, score: number): void {
  localStorage.setItem(QUIZ_RESULTS_KEY, JSON.stringify({ answers, profile, score }));
}

function generateId(): string {
  return Date.now().toString(36) + Math.random().toString(36).slice(2);
}

function computeProfile(answers: Record<string, number>): { profile: MotivationProfile; score: number } {
  const values = Object.values(answers);
  const score = values.reduce((a, b) => a + b, 0) / values.length;
  let profile: MotivationProfile;
  if (score >= 3.5) profile = 'intrinsic';
  else if (score >= 2.5) profile = 'integrated';
  else if (score >= 1.75) profile = 'identified';
  else profile = 'extrinsic';
  return { profile, score };
}

// ---- Sub-components ----

function SectionHeader({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div>
      <p className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-1">{label}</p>
      <h2 className="text-xl font-bold text-slate-900 dark:text-slate-100">{children}</h2>
    </div>
  );
}

function InfoCard({ title, icon, children }: { title: string; icon: string; children: React.ReactNode }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white dark:bg-slate-800 dark:border-slate-700 p-5 shadow-sm">
      <div className="flex items-center gap-2 mb-3">
        <span className="text-xl">{icon}</span>
        <h3 className="font-semibold text-slate-800 dark:text-slate-100">{title}</h3>
      </div>
      <div className="text-sm leading-relaxed text-slate-600 dark:text-slate-400 space-y-2">
        {children}
      </div>
    </div>
  );
}

function PillBadge({ children, color = 'indigo' }: { children: React.ReactNode; color?: string }) {
  const map: Record<string, string> = {
    indigo: 'bg-indigo-100 text-indigo-700 dark:bg-indigo-900/40 dark:text-indigo-300',
    emerald: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-300',
    amber: 'bg-amber-100 text-amber-700 dark:bg-amber-900/40 dark:text-amber-300',
    rose: 'bg-rose-100 text-rose-700 dark:bg-rose-900/40 dark:text-rose-300',
    violet: 'bg-violet-100 text-violet-700 dark:bg-violet-900/40 dark:text-violet-300',
  };
  return (
    <span className={`inline-block rounded-full px-2.5 py-0.5 text-xs font-medium ${map[color] ?? map.indigo}`}>
      {children}
    </span>
  );
}

// ---- Quiz component ----

function MotivationQuiz() {
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [submitted, setSubmitted] = useState(false);
  const [result, setResult] = useState<{ profile: MotivationProfile; score: number } | null>(null);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    const saved = loadSavedQuizResult();
    if (saved) {
      setAnswers(saved.answers);
      setResult({ profile: saved.profile, score: saved.score });
      setSubmitted(true);
    }
    setHydrated(true);
  }, []);

  const allAnswered = QUIZ_QUESTIONS.every((q) => answers[q.id] !== undefined);

  function handleSubmit() {
    if (!allAnswered) return;
    const { profile, score } = computeProfile(answers);
    setResult({ profile, score });
    setSubmitted(true);
    saveQuizResult(answers, profile, score);
  }

  function handleRetake() {
    setAnswers({});
    setSubmitted(false);
    setResult(null);
    localStorage.removeItem(QUIZ_RESULTS_KEY);
  }

  if (!hydrated) return null;

  return (
    <div className="space-y-6">
      {!submitted ? (
        <>
          <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
            Answer honestly — there are no "good" or "bad" results. This quiz maps where you are
            on the Self-Determination Theory continuum so you can apply the right strategies.
          </p>

          <div className="space-y-6">
            {QUIZ_QUESTIONS.map((q, qi) => (
              <div key={q.id} className="rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-5 shadow-sm">
                <p className="text-sm font-semibold text-slate-800 dark:text-slate-100 mb-4">
                  <span className="text-indigo-500 mr-2">{qi + 1}.</span>
                  {q.text}
                </p>
                <div className="space-y-2">
                  {q.options.map((opt) => {
                    const selected = answers[q.id] === opt.value;
                    return (
                      <button
                        key={opt.value}
                        onClick={() => setAnswers((prev) => ({ ...prev, [q.id]: opt.value }))}
                        className={`w-full text-left rounded-lg border px-4 py-3 text-sm transition ${
                          selected
                            ? 'border-indigo-400 bg-indigo-50 dark:bg-indigo-950/60 dark:border-indigo-600 text-indigo-800 dark:text-indigo-200 font-medium ring-1 ring-indigo-200 dark:ring-indigo-800'
                            : 'border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-slate-300 dark:hover:border-slate-500 hover:bg-slate-50 dark:hover:bg-slate-800/60'
                        }`}
                      >
                        {opt.label}
                      </button>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>

          <button
            onClick={handleSubmit}
            disabled={!allAnswered}
            className="w-full rounded-lg bg-indigo-600 py-3 text-sm font-semibold text-white transition hover:bg-indigo-700 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            {allAnswered ? 'See my motivation profile →' : `Answer all ${QUIZ_QUESTIONS.length} questions to continue`}
          </button>
        </>
      ) : result ? (
        <QuizResult result={result} onRetake={handleRetake} />
      ) : null}
    </div>
  );
}

function QuizResult({ result, onRetake }: { result: { profile: MotivationProfile; score: number }; onRetake: () => void }) {
  const profile = PROFILES[result.profile];
  const pct = Math.round(((result.score - 1) / 3) * 100);

  return (
    <div className="space-y-5">
      <div className={`rounded-xl border ${profile.border} ${profile.bg} dark:bg-opacity-10 p-6`}>
        <p className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-1">Your Motivation Profile</p>
        <h3 className={`text-xl font-bold ${profile.color} mb-3`}>{profile.title}</h3>

        {/* Score bar */}
        <div className="mb-4">
          <div className="flex justify-between text-xs text-slate-500 mb-1">
            <span>Extrinsic</span>
            <span>Intrinsic</span>
          </div>
          <div className="h-2 rounded-full bg-slate-200 dark:bg-slate-700">
            <div
              className="h-2 rounded-full bg-indigo-500 transition-all duration-500"
              style={{ width: `${pct}%` }}
            />
          </div>
        </div>

        <p className="text-sm leading-relaxed text-slate-700 dark:text-slate-300">{profile.description}</p>
      </div>

      <div className="rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-5">
        <h4 className="font-semibold text-slate-800 dark:text-slate-100 mb-3 text-sm">Recommended strategies for your profile</h4>
        <ul className="space-y-2">
          {profile.strategies.map((s, i) => (
            <li key={i} className="flex items-start gap-2 text-sm text-slate-600 dark:text-slate-400">
              <span className="mt-0.5 flex-shrink-0 rounded-full bg-indigo-100 dark:bg-indigo-900/40 px-1.5 py-0.5 text-xs font-bold text-indigo-600 dark:text-indigo-300">
                {i + 1}
              </span>
              {s}
            </li>
          ))}
        </ul>
      </div>

      <button
        onClick={onRetake}
        className="text-sm text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 underline underline-offset-2 transition"
      >
        Retake quiz
      </button>
    </div>
  );
}

// ---- Goal-setting worksheet ----

function GoalWorksheet() {
  const [goals, setGoals] = useState<GoalEntry[]>([]);
  const [form, setForm] = useState({ goal: '', whyItMatters: '', schedule: '', accountability: '' });
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    setGoals(loadGoals());
    setHydrated(true);
  }, []);

  function handleSave() {
    if (!form.goal.trim()) return;
    setSaving(true);
    const entry: GoalEntry = {
      id: generateId(),
      ...form,
      savedAt: new Date().toISOString(),
    };
    saveGoal(entry);
    setGoals(loadGoals());
    setForm({ goal: '', whyItMatters: '', schedule: '', accountability: '' });
    setSaving(false);
    setSaved(true);
    setTimeout(() => setSaved(false), 2500);
  }

  function handleDelete(id: string) {
    deleteGoal(id);
    setGoals(loadGoals());
  }

  if (!hydrated) return null;

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
        Research on implementation intentions shows that specifying <em>what</em>, <em>why</em>,{' '}
        <em>when</em>, and <em>how you will stay accountable</em> dramatically increases
        follow-through. Fill in each field honestly.
      </p>

      {/* Form */}
      <div className="rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-5 shadow-sm space-y-4">
        <div>
          <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 mb-1.5">
            My CT Practice Goal
          </label>
          <textarea
            value={form.goal}
            onChange={(e) => setForm((p) => ({ ...p, goal: e.target.value }))}
            placeholder="e.g. I want to identify logical fallacies in news articles I read daily."
            rows={3}
            className="w-full rounded-lg border border-slate-200 dark:border-slate-600 bg-slate-50 dark:bg-slate-900 px-3 py-2 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-400 resize-none"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 mb-1.5">
            Why it matters to me (intrinsic connection)
          </label>
          <textarea
            value={form.whyItMatters}
            onChange={(e) => setForm((p) => ({ ...p, whyItMatters: e.target.value }))}
            placeholder="e.g. I want to make better decisions and not be misled. This matters because I value truth and autonomy."
            rows={3}
            className="w-full rounded-lg border border-slate-200 dark:border-slate-600 bg-slate-50 dark:bg-slate-900 px-3 py-2 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-400 resize-none"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 mb-1.5">
            When I will practice (specific schedule)
          </label>
          <input
            value={form.schedule}
            onChange={(e) => setForm((p) => ({ ...p, schedule: e.target.value }))}
            placeholder="e.g. Monday, Wednesday, Friday — 8:00–8:25 am with morning coffee."
            className="w-full rounded-lg border border-slate-200 dark:border-slate-600 bg-slate-50 dark:bg-slate-900 px-3 py-2 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 mb-1.5">
            How I will stay accountable
          </label>
          <input
            value={form.accountability}
            onChange={(e) => setForm((p) => ({ ...p, accountability: e.target.value }))}
            placeholder="e.g. Share one insight with a friend weekly. Track streak on dashboard."
            className="w-full rounded-lg border border-slate-200 dark:border-slate-600 bg-slate-50 dark:bg-slate-900 px-3 py-2 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <button
          onClick={handleSave}
          disabled={!form.goal.trim() || saving}
          className={`w-full rounded-lg py-2.5 text-sm font-semibold transition ${
            saved
              ? 'bg-emerald-500 text-white'
              : 'bg-indigo-600 text-white hover:bg-indigo-700 disabled:opacity-40 disabled:cursor-not-allowed'
          }`}
        >
          {saved ? '✓ Goal saved' : saving ? 'Saving…' : 'Save goal →'}
        </button>
      </div>

      {/* Saved goals */}
      {goals.length > 0 && (
        <div className="space-y-3">
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
            Your saved goals ({goals.length})
          </p>
          {goals.map((g) => (
            <div key={g.id} className="rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-4 shadow-sm">
              <div className="flex items-start justify-between gap-3 mb-3">
                <p className="text-sm font-semibold text-slate-800 dark:text-slate-100">{g.goal}</p>
                <button
                  onClick={() => handleDelete(g.id)}
                  className="flex-shrink-0 text-xs text-slate-400 hover:text-rose-500 transition"
                  title="Delete goal"
                >
                  ✕
                </button>
              </div>
              {g.whyItMatters && (
                <p className="text-xs text-slate-500 dark:text-slate-400 mb-1">
                  <span className="font-medium text-slate-600 dark:text-slate-300">Why: </span>
                  {g.whyItMatters}
                </p>
              )}
              {g.schedule && (
                <p className="text-xs text-slate-500 dark:text-slate-400 mb-1">
                  <span className="font-medium text-slate-600 dark:text-slate-300">When: </span>
                  {g.schedule}
                </p>
              )}
              {g.accountability && (
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  <span className="font-medium text-slate-600 dark:text-slate-300">Accountability: </span>
                  {g.accountability}
                </p>
              )}
              <p className="mt-2 text-xs text-slate-300 dark:text-slate-600">
                Saved {new Date(g.savedAt).toLocaleDateString()}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

// ---- Main page ----

export default function MotivationPage() {
  const [activeTab, setActiveTab] = useState<MotivationTab>('quiz');

  return (
    <div className="mx-auto max-w-4xl space-y-16 pb-16">

      {/* ── Hero ─────────────────────────────────────── */}
      <section className="space-y-4">
        <div className="space-y-1">
          <p className="text-xs font-semibold uppercase tracking-wider text-indigo-500">
            Before the work begins
          </p>
          <h1 className="text-3xl font-bold tracking-tight text-slate-900 dark:text-slate-100">
            Motivation for Critical Thinking
          </h1>
        </div>
        <p className="max-w-2xl text-base leading-relaxed text-slate-600 dark:text-slate-400">
          The biggest barrier to developing critical thinking is not difficulty — it is sustaining
          the will to practise. This page explains the psychology of motivation, gives you
          practical strategies to stay engaged, and helps you set concrete goals for your CT
          practice.
        </p>
        <div className="flex flex-wrap gap-2">
          <PillBadge color="indigo">Self-Determination Theory</PillBadge>
          <PillBadge color="emerald">Growth Mindset</PillBadge>
          <PillBadge color="amber">Habit Science</PillBadge>
          <PillBadge color="violet">Procrastination</PillBadge>
          <PillBadge color="rose">Goal Setting</PillBadge>
        </div>
      </section>

      {/* ── Self-Determination Theory ────────────────── */}
      <section className="space-y-5">
        <SectionHeader label="Core Theory">Self-Determination Theory (SDT)</SectionHeader>
        <p className="text-sm leading-relaxed text-slate-600 dark:text-slate-400 max-w-2xl">
          Deci and Ryan's Self-Determination Theory is the most empirically supported framework for
          understanding human motivation. It holds that sustained, high-quality engagement requires
          three basic psychological needs. When these are met, motivation becomes self-sustaining;
          when they are chronically frustrated, engagement collapses even with external rewards.
        </p>

        <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
          <InfoCard title="Autonomy" icon="🧭">
            <p>
              The need to feel that your actions arise from your own values — not external pressure
              or control.
            </p>
            <p className="mt-2 font-medium text-slate-700 dark:text-slate-300">For CT practice:</p>
            <p>
              Choose what you study. Set your own questions. Approach arguments on your own terms
              before reading others' analyses.
            </p>
          </InfoCard>

          <InfoCard title="Competence" icon="⚡">
            <p>
              The need to experience growth and effective action. Neither boredom (too easy) nor
              overwhelm (too hard) sustains motivation.
            </p>
            <p className="mt-2 font-medium text-slate-700 dark:text-slate-300">For CT practice:</p>
            <p>
              Work at the edge of your current ability. The Practice and Review modules are
              calibrated to expand this edge through spaced repetition.
            </p>
          </InfoCard>

          <InfoCard title="Relatedness" icon="🤝">
            <p>
              The need to feel connected to others who share your pursuits. Isolation erodes
              motivation over time.
            </p>
            <p className="mt-2 font-medium text-slate-700 dark:text-slate-300">For CT practice:</p>
            <p>
              Find a thinking partner. Share an argument map. Discuss a fallacy you spotted.
              Social engagement accelerates both motivation and skill.
            </p>
          </InfoCard>
        </div>
      </section>

      {/* ── Intrinsic vs Extrinsic ───────────────────── */}
      <section className="space-y-5">
        <SectionHeader label="Motivation Types">Intrinsic vs. Extrinsic Motivation</SectionHeader>
        <p className="text-sm leading-relaxed text-slate-600 dark:text-slate-400 max-w-2xl">
          SDT describes a continuum from fully extrinsic to fully intrinsic motivation. These are
          not opposites — they are stages of internalisation. The goal is not to eliminate external
          motivation but to progressively integrate it into your values and identity.
        </p>

        <div className="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-700">
          <table className="w-full text-sm">
            <thead className="bg-slate-50 dark:bg-slate-800">
              <tr>
                <th className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider text-slate-500">Type</th>
                <th className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider text-slate-500">Driver</th>
                <th className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider text-slate-500">Durability</th>
                <th className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider text-slate-500">CT Example</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 dark:divide-slate-700">
              {[
                { type: 'External', driver: 'Reward / punishment', durability: 'Low', eg: '"I will get a better grade."', dur: 'text-rose-600' },
                { type: 'Introjected', driver: 'Guilt / ego protection', durability: 'Low–Medium', eg: '"I should because others expect it."', dur: 'text-amber-600' },
                { type: 'Identified', driver: 'Personal importance', durability: 'Medium–High', eg: '"This will make me a better thinker."', dur: 'text-amber-500' },
                { type: 'Integrated', driver: 'Core values / identity', durability: 'High', eg: '"Thinking clearly is who I am."', dur: 'text-emerald-600' },
                { type: 'Intrinsic', driver: 'Inherent enjoyment', durability: 'Very High', eg: '"I love dissecting this argument."', dur: 'text-emerald-700' },
              ].map((row) => (
                <tr key={row.type} className="bg-white dark:bg-slate-900 hover:bg-slate-50 dark:hover:bg-slate-800/60">
                  <td className="px-4 py-3 font-medium text-slate-800 dark:text-slate-200">{row.type}</td>
                  <td className="px-4 py-3 text-slate-600 dark:text-slate-400">{row.driver}</td>
                  <td className={`px-4 py-3 font-semibold ${row.dur}`}>{row.durability}</td>
                  <td className="px-4 py-3 text-slate-600 dark:text-slate-400 italic">{row.eg}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* ── Cultivating Intrinsic Motivation ──────────── */}
      <section className="space-y-5">
        <SectionHeader label="Practical Strategies">Cultivating Intrinsic Motivation</SectionHeader>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
          {[
            {
              title: 'Follow genuine curiosity first',
              body: 'Pick a claim, argument, or topic you actually wonder about. Curiosity primes the brain for sustained attention. If nothing feels interesting yet, explore broadly until something catches — don\'t force topics that feel inert.',
              icon: '🔍',
            },
            {
              title: 'Shrink the scope until it feels achievable',
              body: 'Overwhelm kills intrinsic motivation. If "learn critical thinking" feels impossibly large, narrow it: "Analyse one paragraph today." Competence grows from completion, and completion generates motivation for the next session.',
              icon: '🎯',
            },
            {
              title: 'Notice and name your thinking',
              body: 'When you catch a fallacy or notice an unexamined assumption, name it explicitly: "That\'s an appeal to authority." Making invisible processes visible creates the small wins that fuel continued engagement.',
              icon: '🏷️',
            },
            {
              title: 'Tie practice to problems you already care about',
              body: 'Apply CT frameworks to real decisions in your life — career, health, finances. When you use thinking skills to navigate something that genuinely matters to you, practice stops being abstract and becomes personally meaningful.',
              icon: '🔗',
            },
            {
              title: 'Track visible progress',
              body: 'The Dashboard streak and SRS review metrics exist for this reason. Seeing your capabilities compound over time is motivationally powerful. Revisit your earliest attempts periodically to register genuine growth.',
              icon: '📈',
            },
            {
              title: 'Teach what you are learning',
              body: 'Explaining a concept to someone else — even in writing — deepens understanding and creates social connection around the practice. Both effects strengthen intrinsic motivation through competence and relatedness.',
              icon: '🎓',
            },
          ].map((item) => (
            <InfoCard key={item.title} title={item.title} icon={item.icon}>
              <p>{item.body}</p>
            </InfoCard>
          ))}
        </div>
      </section>

      {/* ── Pitfalls ─────────────────────────────────── */}
      <section className="space-y-5">
        <SectionHeader label="Common Obstacles">Motivation Pitfalls & How to Overcome Them</SectionHeader>

        <div className="space-y-4">
          {/* Procrastination */}
          <div className="rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-5 shadow-sm">
            <div className="flex items-start gap-3 mb-3">
              <span className="text-2xl">⏳</span>
              <div>
                <h3 className="font-semibold text-slate-800 dark:text-slate-100">Procrastination</h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                  Doing low-value tasks instead of the difficult thinking work
                </p>
              </div>
            </div>
            <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed mb-4">
              Procrastination is not laziness — it is avoidance of negative emotion (uncertainty,
              difficulty, fear of failure). Critical thinking is cognitively demanding by design,
              making it a high-procrastination target. The fix is reducing the activation cost, not
              pushing harder.
            </p>
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
              <div className="rounded-lg bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-700 p-3">
                <p className="text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">🍅 Pomodoro Technique</p>
                <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                  Work for 25 minutes, rest for 5. The finite time-box makes starting psychologically easy —
                  you're only committing to 25 minutes, not an unbounded session. After 4 Pomodoros, take a
                  longer 15–30 minute break. This is one of the most replicated productivity interventions.
                </p>
              </div>
              <div className="rounded-lg bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-700 p-3">
                <p className="text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">🔗 Habit Stacking</p>
                <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                  Attach CT practice to an existing daily habit using the formula: "After [current habit], I
                  will [CT practice]." E.g. "After I pour my morning coffee, I will open one practice
                  problem." The existing habit acts as an automatic trigger, bypassing the need for
                  decision-making.
                </p>
              </div>
              <div className="rounded-lg bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-700 p-3">
                <p className="text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">✂️ Two-Minute Rule</p>
                <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                  If starting feels hard, commit to just two minutes. Often starting is the hardest part —
                  the task's difficulty feels smaller once you've begun. If you stop at two minutes, you still
                  built the habit of starting.
                </p>
              </div>
              <div className="rounded-lg bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-700 p-3">
                <p className="text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">🎁 Temptation Bundling</p>
                <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                  Pair CT practice with something you genuinely enjoy — a specific playlist, a preferred
                  beverage, a comfortable environment. Over time, the enjoyable element triggers the
                  association with the practice, lowering resistance.
                </p>
              </div>
            </div>
          </div>

          {/* Overwhelm */}
          <div className="rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-5 shadow-sm">
            <div className="flex items-start gap-3 mb-3">
              <span className="text-2xl">🌊</span>
              <div>
                <h3 className="font-semibold text-slate-800 dark:text-slate-100">Overwhelm & Scope Paralysis</h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                  The curriculum feels too large to know where to start
                </p>
              </div>
            </div>
            <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
              When the scope of "learning critical thinking" feels unbounded, the brain defaults to
              avoidance. Antidote: always have the next concrete action defined. Before ending a
              session, write one sentence specifying exactly what you will do next time. This
              eliminates the start-up cost of deciding.
            </p>
          </div>

          {/* Burnout */}
          <div className="rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-5 shadow-sm">
            <div className="flex items-start gap-3 mb-3">
              <span className="text-2xl">🔋</span>
              <div>
                <h3 className="font-semibold text-slate-800 dark:text-slate-100">Motivation Depletion / Burnout</h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                  Engagement drops after an intense initial push
                </p>
              </div>
            </div>
            <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
              Motivation is finite on any given day — it depletes like a muscle. Willpower-dependent
              practice is inherently fragile. The solution is systematisation: automate the "when" and
              "what" of practice so motivation is not required to start, only to persist. The SRS review
              system, streaks, and habit stacking all serve this function.
            </p>
          </div>
        </div>
      </section>

      {/* ── Growth Mindset ───────────────────────────── */}
      <section className="space-y-5">
        <SectionHeader label="Foundational Belief">Growth Mindset & Critical Thinking</SectionHeader>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
          <div className="space-y-4">
            <p className="text-sm leading-relaxed text-slate-600 dark:text-slate-400">
              Carol Dweck's research on implicit theories of intelligence demonstrates that students
              who believe intelligence is malleable (growth mindset) consistently outperform those who
              believe it is fixed (fixed mindset) — especially when confronting difficult material.
            </p>
            <p className="text-sm leading-relaxed text-slate-600 dark:text-slate-400">
              Critical thinking is inherently about encountering the limits of your current thinking.
              Every time you recognise a fallacy you previously missed, or discover an assumption you
              didn't know you were making, you are directly experiencing intellectual growth. A fixed
              mindset reads this as evidence of inadequacy; a growth mindset reads it as the goal.
            </p>
            <div className="rounded-lg border border-indigo-100 dark:border-indigo-900 bg-indigo-50 dark:bg-indigo-950/30 p-4">
              <p className="text-xs font-semibold text-indigo-600 dark:text-indigo-400 uppercase tracking-wider mb-1">Key reframe</p>
              <p className="text-sm text-indigo-900 dark:text-indigo-200 italic">
                "I can't do this" → "I can't do this <em>yet</em>. What would I need to learn?"
              </p>
            </div>
          </div>

          <div className="space-y-3">
            <div className="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-700">
              <table className="w-full text-xs">
                <thead className="bg-slate-50 dark:bg-slate-800">
                  <tr>
                    <th className="px-3 py-2 text-left font-semibold text-slate-500 uppercase tracking-wider">Fixed Mindset</th>
                    <th className="px-3 py-2 text-left font-semibold text-slate-500 uppercase tracking-wider">Growth Mindset</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 dark:divide-slate-700 bg-white dark:bg-slate-900">
                  {[
                    ['Avoids challenging arguments', 'Seeks challenging arguments'],
                    ['Gives up when confused', 'Gets curious when confused'],
                    ['Hides errors or gaps', 'Surfaces errors as data'],
                    ['"I\'m not a logical person"', '"Logic is a learnable skill"'],
                    ['Threatened by better thinkers', 'Inspired by better thinkers'],
                  ].map(([fixed, growth], i) => (
                    <tr key={i}>
                      <td className="px-3 py-2 text-rose-700 dark:text-rose-400">{fixed}</td>
                      <td className="px-3 py-2 text-emerald-700 dark:text-emerald-400">{growth}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className="rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-4">
              <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-500 mb-2">Practices that build growth mindset</h4>
              <ul className="space-y-1.5 text-xs text-slate-600 dark:text-slate-400">
                <li className="flex items-start gap-1.5"><span className="text-emerald-500 font-bold mt-0.5">✓</span> Praise effort and strategy, not outcome.</li>
                <li className="flex items-start gap-1.5"><span className="text-emerald-500 font-bold mt-0.5">✓</span> Keep an error log — review mistakes as learning events.</li>
                <li className="flex items-start gap-1.5"><span className="text-emerald-500 font-bold mt-0.5">✓</span> Use "not yet" language when you fail a task.</li>
                <li className="flex items-start gap-1.5"><span className="text-emerald-500 font-bold mt-0.5">✓</span> Deliberately attempt arguments harder than your current level.</li>
                <li className="flex items-start gap-1.5"><span className="text-emerald-500 font-bold mt-0.5">✓</span> Reflect after each session: "What did I learn about my thinking?"</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* ── Interactive Tools ─────────────────────────── */}
      <section className="space-y-5">
        <SectionHeader label="Interactive Tools">Your Motivation Toolkit</SectionHeader>

        {/* Tab switcher */}
        <div className="flex gap-1 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 p-1 w-fit">
          {([['quiz', '🧭 Motivation Profile Quiz'], ['goals', '🎯 Goal-Setting Worksheet']] as const).map(([tab, label]) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`rounded-md px-4 py-2 text-sm font-medium transition ${
                activeTab === tab
                  ? 'bg-white dark:bg-slate-700 shadow-sm text-slate-900 dark:text-slate-100'
                  : 'text-slate-500 dark:text-slate-400 hover:text-slate-700 dark:hover:text-slate-200'
              }`}
            >
              {label}
            </button>
          ))}
        </div>

        {activeTab === 'quiz' ? <MotivationQuiz /> : <GoalWorksheet />}
      </section>

      {/* ── Next steps ───────────────────────────────── */}
      <section className="rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800/50 p-6">
        <h2 className="text-base font-semibold text-slate-800 dark:text-slate-100 mb-4">Ready to practise?</h2>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
          {[
            { href: '/practice', label: 'Practice Problems', desc: 'Apply frameworks to real arguments' },
            { href: '/chapters', label: 'Chapters', desc: "Structured progression through Dewey's model" },
            { href: '/assess', label: 'Self-Assess', desc: 'Rate your CT dispositions to find gaps' },
          ].map((link) => (
            <a
              key={link.href}
              href={link.href}
              className="rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-4 shadow-sm transition hover:border-indigo-300 dark:hover:border-indigo-700 hover:shadow-md"
            >
              <p className="text-sm font-semibold text-slate-800 dark:text-slate-100">{link.label}</p>
              <p className="mt-1 text-xs text-slate-500 dark:text-slate-400">{link.desc}</p>
              <p className="mt-2 text-xs text-indigo-600 dark:text-indigo-400">Go →</p>
            </a>
          ))}
        </div>
      </section>
    </div>
  );
}
