'use client';

/**
 * Thin client button that opens the SearchPalette via Cmd+K simulation.
 * Avoids prop-drilling by dispatching a keyboard event the palette already handles.
 */
export default function SearchTrigger() {
  function handleClick() {
    // Simulate Cmd+K so SearchPalette's existing keyboard listener opens it
    document.dispatchEvent(
      new KeyboardEvent('keydown', { key: 'k', metaKey: true, ctrlKey: true, bubbles: true }),
    );
  }

  return (
    <button
      type="button"
      onClick={handleClick}
      aria-label="Search (⌘K)"
      className="ml-1 hidden items-center gap-1.5 rounded-md border border-slate-200 bg-white px-2.5 py-1 text-xs text-slate-400 shadow-sm transition hover:border-slate-300 hover:text-slate-600 sm:flex"
    >
      <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
        <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 11.5 11.5Z" />
      </svg>
      <span>Search</span>
      <kbd className="ml-1 rounded border border-slate-200 bg-slate-100 px-1 font-mono text-[10px] text-slate-400">⌘K</kbd>
    </button>
  );
}
