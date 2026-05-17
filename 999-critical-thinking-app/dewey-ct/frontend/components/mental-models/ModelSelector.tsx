'use client';

import { useState, useMemo, useRef } from 'react';
import Link from 'next/link';
import type { MentalModel } from '@/types/framework';

// ---------- Scenario chips ----------
// label: shown in the button and filled into the input box
// query: expanded keyword string used for scoring (not shown to user)

const SCENARIOS = [
  {
    label: "I'm stuck on a decision",
    icon: '🎯',
    query: 'decision choose options deliberation commit difficult deciding',
  },
  {
    label: 'Stress-test a plan',
    icon: '🔩',
    query: 'stress-test plan failure modes before committing inversion worst case',
  },
  {
    label: 'Something feels wrong',
    icon: '🌀',
    query: 'counterintuitive hidden problem system unexpected outcome wrong missing',
  },
  {
    label: 'Challenge my assumptions',
    icon: '🏛️',
    query: 'challenge assumptions conventional wisdom accepted question inherited belief',
  },
  {
    label: "Analyze someone's argument",
    icon: '⚖️',
    query: 'evaluate argument claim evidence reasoning position opposing disagree',
  },
  {
    label: 'Group has blind spots',
    icon: '👥',
    query: 'group team decision consensus cohesive bias groupthink collective',
  },
  {
    label: 'Diagnose a recurring problem',
    icon: '🔬',
    query: 'root cause persistent recurring problem diagnose symptoms fix intervention',
  },
  {
    label: 'Evaluate evidence quality',
    icon: '📊',
    query: 'evidence certainty uncertainty knowledge calibrated confident claims quality',
  },
  {
    label: 'Need an innovative approach',
    icon: '💡',
    query: 'innovate new approach alternatives unconventional novel solution breakthrough',
  },
  {
    label: 'Predict downstream effects',
    icon: '🔮',
    query: 'predict outcomes consequences downstream second-order effects probability future',
  },
  {
    label: "Should I keep going or quit?",
    icon: '🚪',
    query: 'continue abandon stop project investment sunk cost irreversible exit',
  },
  {
    label: "Explain someone's behavior",
    icon: '🧠',
    query: 'explain behavior motives others organizational attribution failure harm intent',
  },
] as const;

// ---------- Scoring ----------

const STOPWORDS = new Set([
  'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
  'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should',
  'could', 'may', 'might', 'can', 'i', 'me', 'my', 'we', 'you', 'your',
  'it', 'its', 'this', 'that', 'these', 'those', 'to', 'of', 'in', 'on',
  'at', 'for', 'with', 'about', 'by', 'from', 'as', 'or', 'and', 'but',
  'if', 'not', 'when', 'what', 'how', 'why', 'which', 'who', 'am',
  'feel', 'feeling', 'need', 'want', 'trying', 'try', 'think', 'thinking',
  'know', 'something', 'someone', 'some', 'any', 'all', 'more', 'most',
  'just', 'really', 'very', 'get', 'got', 'im', 'dont', 'cant', 'also',
  'then', 'than', 'where', 'whether', 'so', 'use', 'using', 'used', 'keep',
]);

function tokenize(text: string): string[] {
  return text
    .toLowerCase()
    .replace(/[^a-z\s-]/g, ' ')
    .split(/[\s-]+/)
    .filter((t) => t.length > 2 && !STOPWORDS.has(t));
}

function scoreModel(model: MentalModel, tokens: string[]): number {
  if (tokens.length === 0) return 0;
  // Combine the most signal-rich fields for matching
  const searchable =
    `${model.when_to_use} ${model.definition} ${model.example}`.toLowerCase();
  const nameLower = model.name.toLowerCase();

  let score = 0;
  for (const token of tokens) {
    try {
      const re = new RegExp(token, 'g');
      // Each occurrence in the searchable body = 1 point
      score += (searchable.match(re) ?? []).length;
      // Name match = strong bonus (user likely described the model directly)
      if (nameLower.includes(token)) score += 5;
    } catch {
      // Skip tokens that aren't valid regex (e.g. user typed special chars)
    }
  }
  return score;
}

// ---------- Category colour map (matches MentalModelsHub) ----------

const CAT_COLORS: Record<string, { badge: string; accent: string; border: string }> = {
  'Reasoning and Logic': {
    badge: 'bg-indigo-50 text-indigo-700',
    accent: 'text-indigo-600',
    border: 'border-l-indigo-400',
  },
  'Systems Thinking': {
    badge: 'bg-teal-50 text-teal-700',
    accent: 'text-teal-600',
    border: 'border-l-teal-400',
  },
  'Decision Making': {
    badge: 'bg-amber-50 text-amber-700',
    accent: 'text-amber-600',
    border: 'border-l-amber-400',
  },
  'Cognitive Biases': {
    badge: 'bg-rose-50 text-rose-700',
    accent: 'text-rose-600',
    border: 'border-l-rose-400',
  },
  Epistemology: {
    badge: 'bg-violet-50 text-violet-700',
    accent: 'text-violet-600',
    border: 'border-l-violet-400',
  },
};

const RANK_STYLES = [
  'bg-amber-100 text-amber-700',  // 1st — gold
  'bg-slate-200 text-slate-600',  // 2nd — silver
  'bg-orange-100 text-orange-700', // 3rd — bronze
];

// ---------- Result card ----------

function ResultCard({ model, rank }: { model: MentalModel; rank: number }) {
  const colors = CAT_COLORS[model.category] ?? {
    badge: 'bg-slate-100 text-slate-600',
    accent: 'text-slate-600',
    border: 'border-l-slate-400',
  };
  // First clause of when_to_use (up to first semicolon or 120 chars)
  const whenClause = model.when_to_use.split(';')[0].trim();

  return (
    <Link
      href={`/mental-models/${model.id}`}
      className={`block rounded-xl border border-slate-200 bg-white p-4 border-l-4 ${colors.border} hover:shadow-md transition-shadow group`}
    >
      <div className="flex items-start justify-between gap-2 mb-2">
        <div className="flex items-center gap-2 min-w-0">
          <span
            className={`w-6 h-6 rounded-full text-[10px] font-bold flex items-center justify-center flex-shrink-0 ${RANK_STYLES[rank - 1]}`}
          >
            {rank}
          </span>
          <h3 className="font-semibold text-slate-800 text-sm group-hover:underline truncate">
            {model.name}
          </h3>
        </div>
        <span className={`text-[10px] font-medium px-1.5 py-0.5 rounded flex-shrink-0 ${colors.badge}`}>
          {model.category}
        </span>
      </div>

      <p className="text-xs text-slate-500 leading-relaxed mb-2 line-clamp-2">{whenClause}</p>

      <span className={`text-xs font-medium ${colors.accent}`}>
        View full model →
      </span>
    </Link>
  );
}

// ---------- Main selector ----------

interface Props {
  models: MentalModel[];
}

export default function ModelSelector({ models }: Props) {
  // displayText: shown in the input box (friendly label or user's own words)
  // scoreQuery: the keyword string used for scoring
  const [displayText, setDisplayText] = useState('');
  const [scoreQuery, setScoreQuery] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [activeScenario, setActiveScenario] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Score all models against the current query
  const results = useMemo(() => {
    if (!submitted || !scoreQuery.trim()) return [];
    const tokens = tokenize(scoreQuery);
    if (tokens.length === 0) return [];
    return models
      .map((m) => ({ model: m, score: scoreModel(m, tokens) }))
      .filter(({ score }) => score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 3)
      .map(({ model }) => model);
  }, [models, scoreQuery, submitted]);

  function handleScenario(label: string, query: string) {
    setDisplayText(label);
    setScoreQuery(query);
    setActiveScenario(label);
    setSubmitted(true);
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!displayText.trim()) return;
    setScoreQuery(displayText); // free text: score against what user typed
    setSubmitted(true);
    setActiveScenario(null);
  }

  function handleInputChange(e: React.ChangeEvent<HTMLInputElement>) {
    setDisplayText(e.target.value);
    setSubmitted(false); // clear results until user clicks Find
    setActiveScenario(null);
    setScoreQuery('');
  }

  function handleReset() {
    setDisplayText('');
    setScoreQuery('');
    setSubmitted(false);
    setActiveScenario(null);
    inputRef.current?.focus();
  }

  const showResults = submitted && scoreQuery.trim().length > 0;

  return (
    <section className="rounded-2xl border border-indigo-100 bg-gradient-to-br from-indigo-50/60 to-white p-6">
      {/* Heading */}
      <div className="mb-4">
        <div className="flex items-center gap-2 mb-1">
          <span className="text-xl" aria-hidden>🎯</span>
          <h2 className="text-base font-semibold text-slate-800">Which model should I use?</h2>
        </div>
        <p className="text-sm text-slate-500">
          Describe your situation — or pick a scenario below — and see the most relevant models.
        </p>
      </div>

      {/* Scenario chips */}
      <div className="flex flex-wrap gap-2 mb-4">
        {SCENARIOS.map(({ label, icon, query }) => (
          <button
            key={label}
            type="button"
            onClick={() => handleScenario(label, query)}
            className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-all ${
              activeScenario === label
                ? 'bg-indigo-600 text-white border-indigo-600 shadow-sm'
                : 'bg-white text-slate-600 border-slate-200 hover:border-indigo-300 hover:text-indigo-600'
            }`}
          >
            {icon} {label}
          </button>
        ))}
      </div>

      {/* Free-text input */}
      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          ref={inputRef}
          type="text"
          value={displayText}
          onChange={handleInputChange}
          placeholder="Or describe your situation in your own words…"
          className="flex-1 px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 bg-white"
        />
        <button
          type="submit"
          disabled={!displayText.trim()}
          className="px-4 py-2.5 rounded-lg bg-indigo-600 text-white text-sm font-medium hover:bg-indigo-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
        >
          Find
        </button>
        {(displayText || showResults) && (
          <button
            type="button"
            onClick={handleReset}
            className="px-4 py-2.5 rounded-lg bg-slate-100 text-slate-600 text-sm hover:bg-slate-200 transition-colors"
          >
            Clear
          </button>
        )}
      </form>

      {/* Hint for free-text */}
      {!activeScenario && !submitted && displayText === '' && (
        <p className="mt-2 text-[11px] text-slate-400">
          Tip: try keywords like{' '}
          <span className="italic">
            decision, assumptions, argument, group, prediction, root cause, bias, system,
            innovation
          </span>
        </p>
      )}

      {/* Results */}
      {showResults && (
        <div className="mt-5 pt-4 border-t border-slate-200">
          {results.length > 0 ? (
            <>
              <p className="text-xs text-slate-500 mb-3">
                Top {results.length} model{results.length !== 1 ? 's' : ''} for your situation:
              </p>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {results.map((model, i) => (
                  <ResultCard key={model.id} model={model} rank={i + 1} />
                ))}
              </div>
              <p className="mt-3 text-[11px] text-slate-400">
                Not quite right?{' '}
                <button
                  type="button"
                  onClick={() => inputRef.current?.focus()}
                  className="underline hover:text-slate-600"
                >
                  Refine your description
                </button>{' '}
                or browse the full library below.
              </p>
            </>
          ) : (
            <div className="rounded-lg bg-amber-50 border border-amber-200 p-4 text-sm text-amber-800">
              <p className="font-medium mb-1">No strong matches found.</p>
              <p className="text-xs text-amber-700">
                Try keywords like:{' '}
                <span className="italic">
                  decision, assumptions, plan, argument, evidence, group, prediction, root cause,
                  bias, system, innovation
                </span>
                . Or use one of the scenario chips above.
              </p>
            </div>
          )}
        </div>
      )}
    </section>
  );
}
