'use client';
import { useState } from 'react';

export default function CreatePage() {
  const [url, setUrl] = useState('');
  const [siteId, setSiteId] = useState('');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function handleScrape(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    try {
      const res = await fetch('http://localhost:8000/scrape/scrape-url', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          url,
          site_id: siteId ? Number(siteId) : undefined
        })
      });
      const data = await res.json();
      setResult(data);
    } catch (err: any) {
      setResult({ error: err.message });
    }
    setLoading(false);
  }

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Scrape a Website</h1>
      <form onSubmit={handleScrape} className="mb-6 space-y-4">
        <input
          type="text"
          placeholder="Enter site URL"
          className="w-full p-2 rounded bg-zinc-800 border border-zinc-700"
          value={url}
          onChange={e => setUrl(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="(Optional) Site ID"
          className="w-full p-2 rounded bg-zinc-800 border border-zinc-700"
          value={siteId}
          onChange={e => setSiteId(e.target.value)}
        />
        <button
          type="submit"
          className="bg-orange-500 px-4 py-2 rounded text-black font-semibold hover:bg-orange-400"
          disabled={loading}
        >
          {loading ? 'Scraping...' : 'Scrape'}
        </button>
      </form>
      <pre className="bg-zinc-900 p-4 rounded text-white min-h-[120px]">
        {result && JSON.stringify(result, null, 2)}
      </pre>
    </div>
  );
}
