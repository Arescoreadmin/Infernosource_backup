'use client';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function CreateCampaignPage() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [pageIds, setPageIds] = useState<number[]>([]);
  const [availablePages, setAvailablePages] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    async function fetchPages() {
      setLoading(true);
      const res = await fetch('http://localhost:8000/sites/pages');
      const data = await res.json();
      setAvailablePages(data);
      setLoading(false);
    }
    fetchPages();
  }, []);

  function handleTogglePage(id: number) {
    setPageIds(prev =>
      prev.includes(id) ? prev.filter(pid => pid !== id) : [...prev, id]
    );
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    await fetch('http://localhost:8000/sites/campaigns', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, description, page_ids: pageIds }),
    });
    router.push('/campaigns');
  }

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Create Campaign</h1>
      <form onSubmit={handleSubmit} className="space-y-4 bg-zinc-900 p-4 rounded">
        <div>
          <label className="block font-semibold mb-1">Name</label>
          <input
            className="w-full p-2 rounded bg-zinc-800 border border-zinc-700"
            value={name}
            onChange={e => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label className="block font-semibold mb-1">Description</label>
          <input
            className="w-full p-2 rounded bg-zinc-800 border border-zinc-700"
            value={description}
            onChange={e => setDescription(e.target.value)}
          />
        </div>
        <div>
          <label className="block font-semibold mb-1">Include Pages</label>
          <div className="max-h-40 overflow-y-auto">
            {availablePages.map(page => (
              <label key={page.id} className="block">
                <input
                  type="checkbox"
                  value={page.id}
                  checked={pageIds.includes(page.id)}
                  onChange={() => handleTogglePage(page.id)}
                />{' '}
                {page.url}
              </label>
            ))}
          </div>
        </div>
        <button
          type="submit"
          className="bg-orange-500 px-4 py-2 rounded text-black font-semibold hover:bg-orange-400"
        >
          Create Campaign
        </button>
      </form>
    </div>
  );
}
