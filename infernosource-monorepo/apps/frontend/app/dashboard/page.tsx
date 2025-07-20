'use client';
import { useEffect, useState } from 'react';
import Link from 'next/link';

type ScrapedPage = {
  id: number;
  url: string;
  html_content?: string;
  extracted_text?: string;
  site_id?: number | null;
};

export default function DashboardPage() {
  const [pages, setPages] = useState<ScrapedPage[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchPages() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch('http://localhost:8000/sites/pages');
        if (!res.ok) throw new Error('Failed to fetch pages');
        const data = await res.json();
        setPages(data);
      } catch (err: any) {
        setError(err.message || 'Error fetching data');
      }
      setLoading(false);
    }
    fetchPages();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Your Scraped Pages</h1>
      {loading && <div className="mb-6 text-orange-400">Loading...</div>}
      {error && <div className="mb-6 text-red-500">{error}</div>}
      {(!loading && pages.length === 0) && (
        <div className="text-zinc-400">No scraped pages found.</div>
      )}
      {pages.length > 0 && (
        <div className="overflow-x-auto">
          <table className="min-w-full bg-zinc-900 rounded">
            <thead>
              <tr>
                <th className="p-2 text-left">ID</th>
                <th className="p-2 text-left">URL</th>
                <th className="p-2 text-left">Site ID</th>
                <th className="p-2 text-left">Preview</th>
              </tr>
            </thead>
            <tbody>
              {pages.map(page => (
                <tr key={page.id} className="border-b border-zinc-800">
                  <td className="p-2">{page.id}</td>
                  <td className="p-2">
                    <Link href={`/dashboard/${page.id}`} className="text-orange-400 hover:underline">
                      {page.url}
                    </Link>
                  </td>
                  <td className="p-2">{page.site_id ?? '—'}</td>
                  <td className="p-2 max-w-xs truncate" title={page.extracted_text || ''}>
                    {page.extracted_text?.slice(0, 80) || '—'}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
