'use client';

/**
 * DataHydrator
 *
 * Invisible client component mounted once in the root layout.
 * On first render it calls hydrateFromBackend(), which fetches any
 * persisted data from the FastAPI/SQLite backend and fills localStorage
 * keys that are currently empty. This means data survives browser-cache
 * clears as long as the backend has been running during at least one
 * previous session.
 */
import { useEffect } from 'react';
import { hydrateFromBackend } from '@/lib/storage';

export default function DataHydrator() {
  useEffect(() => {
    hydrateFromBackend();
  }, []);

  return null;
}
