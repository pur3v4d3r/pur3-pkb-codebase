import { getChapterSummaries } from "@/lib/content";
import ChapterCard from "@/components/chapter/ChapterCard";


const PARTS = [
  { label: "Part I — The Problem of Training Thought", chapters: [1, 2, 3, 4, 5, 6] },
  { label: "Part II — Logical Considerations", chapters: [7, 8, 9, 10, 11] },
  { label: "Part III — The Training of Thought", chapters: [12, 13, 14, 15, 16, 17, 18, 19] },
];

export default function ChaptersPage() {
  const summaries = getChapterSummaries();
  const byChapter = Object.fromEntries(summaries.map((s) => [s.chapter, s]));

  return (
    <div className="space-y-10">
      <div className="space-y-2">
        <h1 className="text-3xl font-bold tracking-tight text-slate-900">How We Think</h1>
        <p className="text-slate-600">
          John Dewey &middot; 1933 Revised Edition &middot; 19 Chapters across 3 Parts
        </p>
        <p className="max-w-2xl text-sm text-slate-500">
          An interactive companion that surfaces Dewey&rsquo;s core arguments, key concepts,
          and pedagogical insights — alongside modern critical-thinking frameworks.
        </p>
      </div>

      {PARTS.map((part) => (
        <section key={part.label}>
          <h2 className="mb-4 text-sm font-semibold uppercase tracking-widest text-slate-500">
            {part.label}
          </h2>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {part.chapters.map((id) => {
              const summary = byChapter[id];
              return <ChapterCard key={id} summary={summary} />;
            })}
          </div>
        </section>
      ))}
    </div>
  );
}
