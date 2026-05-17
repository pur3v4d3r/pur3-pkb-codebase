'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import { savePortfolioEntry, generateId } from '@/lib/storage';
import { saveUserSRSCard, type UserSRSCard } from '@/lib/srs';

interface ChapterAnnotatorProps {
  chapterId: number;
  chapterTitle: string;
}

interface SaveState {
  status: 'idle' | 'form' | 'saved' | 'error' | 'srs-form' | 'srs-saved';
  message?: string;
}

export default function ChapterAnnotator({ chapterId, chapterTitle }: ChapterAnnotatorProps) {
  const [buttonPos, setButtonPos] = useState<{ top: number; left: number } | null>(null);
  const [selectedText, setSelectedText] = useState('');
  const [saveState, setSaveState] = useState<SaveState>({ status: 'idle' });
  const [note, setNote] = useState('');
  const [front, setFront] = useState('');
  const panelRef = useRef<HTMLDivElement>(null);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Listen for text selections anywhere on the page
  const handleSelectionChange = useCallback(() => {
    const selection = window.getSelection();
    if (!selection || selection.isCollapsed || selection.toString().trim().length < 5) {
      // Don't clear button if user clicked inside the panel
      if (panelRef.current?.contains(document.activeElement)) return;
      setButtonPos(null);
      setSelectedText('');
      return;
    }

    const text = selection.toString().trim();
    const range = selection.getRangeAt(0);
    const rect = range.getBoundingClientRect();

    // Position the button above the selection
    setSelectedText(text);
    setButtonPos({
      top: rect.top + window.scrollY - 44, // 44px above selection
      left: Math.min(
        rect.left + window.scrollX + rect.width / 2 - 60,
        window.innerWidth - 140,  // keep within viewport
      ),
    });
  }, []);

  useEffect(() => {
    document.addEventListener('selectionchange', handleSelectionChange);
    return () => {
      document.removeEventListener('selectionchange', handleSelectionChange);
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
    };
  }, [handleSelectionChange]);

  // Close on Escape
  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') {
        setButtonPos(null);
        setSaveState({ status: 'idle' });
        setNote('');
      }
    }
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, []);

  function handleAnnotateClick() {
    setSaveState({ status: 'form' });
  }

  function handleSave() {
    try {
      const truncatedText = selectedText.slice(0, 60);
      const title = truncatedText.length < selectedText.length
        ? `${truncatedText}…`
        : truncatedText;

      savePortfolioEntry({
        id: generateId(),
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        type: 'reflection',
        title,
        chapterRef: chapterId,
        templateId: 'chapter-highlight',
        responses: {
          highlighted_text: selectedText,
          ...(note.trim() ? { note: note.trim() } : {}),
          chapter_ref: `Chapter ${chapterId}: ${chapterTitle}`,
        },
        tags: ['highlight', `chapter-${chapterId}`],
      });

      setSaveState({ status: 'saved', message: 'Saved to portfolio!' });
      setNote('');

      // Auto-dismiss after 2s
      timeoutRef.current = setTimeout(() => {
        setSaveState({ status: 'idle' });
        setButtonPos(null);
        window.getSelection()?.removeAllRanges();
      }, 2000);
    } catch {
      setSaveState({ status: 'error', message: 'Could not save — please try again.' });
    }
  }

  function handleCancel() {
    setSaveState({ status: 'idle' });
    setNote('');
    setFront('');
    setButtonPos(null);
    window.getSelection()?.removeAllRanges();
  }

  function handleSrsClick() {
    setSaveState({ status: 'srs-form' });
  }

  function handleSrsSave() {
    if (!front.trim()) return;
    try {
      const card: UserSRSCard = {
        id: `user-${generateId()}`,
        source: 'user',
        category: `Chapter ${chapterId}`,
        front: front.trim(),
        back: selectedText,
        createdAt: new Date().toISOString(),
        chapterId,
      };
      saveUserSRSCard(card);
      setSaveState({ status: 'srs-saved', message: 'Card added to review queue!' });
      setFront('');
      timeoutRef.current = setTimeout(() => {
        setSaveState({ status: 'idle' });
        setButtonPos(null);
        window.getSelection()?.removeAllRanges();
      }, 2000);
    } catch {
      setSaveState({ status: 'error', message: 'Could not save — please try again.' });
    }
  }

  if (!buttonPos) return null;

  return (
    <div
      ref={panelRef}
      className="fixed z-50"
      style={{ top: buttonPos.top, left: buttonPos.left }}
    >
      {saveState.status === 'idle' && (
        <div className="flex gap-1.5">
          <button
            type="button"
            onMouseDown={(e) => e.preventDefault()}
            onClick={handleAnnotateClick}
            className="flex items-center gap-1.5 rounded-lg bg-slate-900 px-3 py-1.5 text-xs font-medium text-white shadow-lg transition hover:bg-slate-700 active:scale-95"
          >
            <span>✏️</span>
            Annotate
          </button>
          <button
            type="button"
            onMouseDown={(e) => e.preventDefault()}
            onClick={handleSrsClick}
            className="flex items-center gap-1.5 rounded-lg bg-indigo-600 px-3 py-1.5 text-xs font-medium text-white shadow-lg transition hover:bg-indigo-500 active:scale-95"
          >
            <span>🃏</span>
            SRS Card
          </button>
        </div>
      )}

      {saveState.status === 'form' && (
        <div className="w-72 rounded-xl border border-slate-200 bg-white p-4 shadow-2xl">
          <p className="mb-2 text-xs font-semibold text-slate-700">Save highlight</p>
          <p className="mb-3 line-clamp-2 rounded bg-amber-50 px-2 py-1.5 text-xs italic text-amber-900">
            &ldquo;{selectedText.slice(0, 120)}{selectedText.length > 120 ? '…' : ''}&rdquo;
          </p>
          <textarea
            className="w-full resize-none rounded-md border border-slate-200 bg-slate-50 px-3 py-2 text-xs text-slate-700 placeholder-slate-400 focus:border-indigo-400 focus:outline-none focus:ring-1 focus:ring-indigo-300"
            placeholder="Add a personal note… (optional)"
            rows={2}
            value={note}
            onChange={(e) => setNote(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) handleSave();
            }}
            autoFocus
          />
          <div className="mt-3 flex justify-end gap-2">
            <button
              type="button"
              onClick={handleCancel}
              className="rounded-md px-3 py-1.5 text-xs text-slate-500 transition hover:bg-slate-100"
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={handleSave}
              className="rounded-md bg-indigo-600 px-3 py-1.5 text-xs font-medium text-white shadow-sm transition hover:bg-indigo-700"
            >
              Save to portfolio
            </button>
          </div>
        </div>
      )}

      {saveState.status === 'srs-form' && (
        <div className="w-80 rounded-xl border border-slate-200 bg-white p-4 shadow-2xl">
          <p className="mb-2 text-xs font-semibold text-slate-700">Create SRS card</p>
          <p className="mb-3 line-clamp-2 rounded bg-indigo-50 px-2 py-1.5 text-xs italic text-indigo-900">
            &ldquo;{selectedText.slice(0, 120)}{selectedText.length > 120 ? '\u2026' : ''}&rdquo;
          </p>
          <p className="mb-1 text-xs text-slate-500">Your question or term (card front):</p>
          <textarea
            className="w-full resize-none rounded-md border border-slate-200 bg-slate-50 px-3 py-2 text-xs text-slate-700 placeholder-slate-400 focus:border-indigo-400 focus:outline-none focus:ring-1 focus:ring-indigo-300"
            placeholder="e.g. What is the role of a leading idea in reflective thinking?"
            rows={2}
            value={front}
            onChange={(e) => setFront(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) handleSrsSave();
            }}
            autoFocus
          />
          <div className="mt-3 flex justify-end gap-2">
            <button
              type="button"
              onClick={handleCancel}
              className="rounded-md px-3 py-1.5 text-xs text-slate-500 transition hover:bg-slate-100"
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={handleSrsSave}
              disabled={!front.trim()}
              className="rounded-md bg-indigo-600 px-3 py-1.5 text-xs font-medium text-white shadow-sm transition hover:bg-indigo-700 disabled:opacity-40"
            >
              Create card
            </button>
          </div>
        </div>
      )}

      {(saveState.status === 'saved' || saveState.status === 'srs-saved' || saveState.status === 'error') && (
        <div
          className={`rounded-lg px-4 py-2.5 text-xs font-medium shadow-lg ${
            saveState.status === 'error'
              ? 'bg-red-600 text-white'
              : 'bg-green-600 text-white'
          }`}
        >
          {saveState.message}
        </div>
      )}
    </div>
  );
}
