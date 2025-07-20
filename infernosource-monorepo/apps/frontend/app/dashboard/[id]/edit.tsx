'use client';
import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';

type ScrapedPage = {
  id: number;
  url: string;
  html_content?: string;
  extracted_text?: string;
  site_id?: number | null;
};

export default function EditScrapedPage() {
  const params = useParams();
  const router = useRouter();
  const id = params?.id;
  const [page, setPage] = useState<ScrapedPage | null>(null);
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

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
        setUrl(data.url);
      } catch (err: any) {
        setError(err.message || 'Error fetching data');
      }
      setLoading(false);
    }
    fetchPage();
  }, [id]);

  async function handleSave(e: React.FormEvent) {
    e.preventDefault();
    setSaving(true);
    setError(null);
    try {
      const res = await fetch(`http://localhost:8000/sites/pages/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });
      if (!res.ok) throw new Error('Failed to update page');
      router.push(`/dashboard/${id}`);
    } catch (err: any) {
      setError(err.message || 'Error saving data');
    }
    setSaving(false);
  }

  return (
    <div>
      <button
        className="mb-4 bg-zinc-800 text-zinc-100 px-3 py-1 rounded hover:bg-zinc-700"
        onClick={() => router.back()}
      >
        &larr; Back
      </button>
      <h1 className="text-2xl font-bold mb-4">Edit Scraped Page</h1>
      {loading && <div className="mb-6 text-orange-400">Loading...</div>}
      {error && <div className="mb-6 text-red-500">{error}</div>}
      {page && (
        <form onSubmit={handleSave} className="space-y-4 bg-zinc-900 p-4 rounded">
          <div>
            <label className="block font-semibold mb-1">URL</label>
            <input
              className="w-full p-2 rounded bg-zinc-800 border border-zinc-700"
              value={url}
              onChange={e => setUrl(e.target.value)}
              required
            />
          </div>
          <button
            type="submit"
            className="bg-orange-500 px-4 py-2 rounded text-black font-semibold hover:bg-orange-400"
            disabled={saving}
          >
            {saving ? 'Saving...' : 'Save Changes'}
          </button>
        </form>
      )}
    </div>
  );
}
