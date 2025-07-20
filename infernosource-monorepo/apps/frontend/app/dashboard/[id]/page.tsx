'use client';
import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';

type ScrapedPage = {
  id: number;
  url: string;
  html_content?: string;
  extracted_text?: string;
  site_id?: number | null;
};

export default function ScrapedPageDetails() {
  const params = useParams();
  const router = useRouter();
  const id = params?.id;
  const [page, setPage] = useState<ScrapedPage | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [deleting, setDeleting] = useState(false);

  useEffect(() => {
    if (!id) return;
    async function fetchPage() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`http://localhost:8000/sites/pages/${id}`);
        if (!res.ok) throw new Error('Failed to fetch page');
        const data = await res.json();
        setPage(data);
      } catch (err: any) {
        setError(err.message || 'Error fetching data');
      }
      setLoading(false);
    }
    fetchPage();
  }, [id]);

  async function handleDelete() {
    if (!window.confirm('Are you sure you want to delete this page?')) return;
    setDeleting(true);
    try {
      const res = await fetch(`http://localhost:8000/sites/pages/${id}`, {
        method: 'DELETE',
      });
      if (!res.ok) throw new Error('Failed to delete page');
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message || 'Error deleting page');
    }
    setDeleting(false);
  }

  return (
    <div>
      <button
        className="mb-4 bg-zinc-800 text-zinc-100 px-3 py-1 rounded hover:bg-zinc-700"
        onClick={() => router.back()}
      >
        &larr; Back to Dashboard
      </button>
      <div className="flex items-center mb-4">
        <h1 className="text-2xl font-bold">Scraped Page Details</h1>
        {page && (
          <>
            <Link
              href={`/dashboard/${page.id}/edit`}
              className="text-orange-400 hover:underline ml-4"
            >
              Edit
            </Link>
            <button
              onClick={handleDelete}
              className="ml-4 bg-red-700 text-white px-3 py-1 rounded hover:bg-red-600"
              disabled={deleting}
            >
              {deleting ? 'Deleting...' : 'Delete'}
            </button>
          </>
        )}
      </div>
      {loading && <div className="mb-6 text-orange-400">Loading...</div>}
      {error && <div className="mb-6 text-red-500">{error}</div>}
      {page && (
        <div className="bg-zinc-900 rounded p-4">
          <div><b>ID:</b> {page.id}</div>
          <div><b>URL:</b> {page.url}</div>
          <div><b>Site ID:</b> {page.site_id ?? '—'}</div>
          <div className="mt-4">
            <b>Extracted Text:</b>
            <pre className="bg-zinc-800 p-2 rounded text-white max-h-64 overflow-auto">{page.extracted_text || '—'}</pre>
          </div>
          <div className="mt-4">
            <b>HTML Content:</b>
            <pre className="bg-zinc-800 p-2 rounded text-white max-h-64 overflow-auto">{page.html_content || '—'}</pre>
          </div>
        </div>
      )}
    </div>
  );
}
