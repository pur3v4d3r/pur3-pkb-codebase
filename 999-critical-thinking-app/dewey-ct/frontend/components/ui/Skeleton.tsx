/** Animated pulse block for loading skeleton states. */
export function SkeletonBlock({ className }: { className?: string }) {
  return (
    <div className={`animate-pulse rounded-lg bg-slate-200 ${className ?? ''}`} />
  );
}
