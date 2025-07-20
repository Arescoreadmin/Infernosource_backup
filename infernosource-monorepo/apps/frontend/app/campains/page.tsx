'use client';
import { useEffect, useState } from 'react';
import Link from 'next/link';

type Campaign = {
  id: number;
  name: string;
  description?: string;
  page_ids: number[];
};

export default function CampaignsPage() {
  const [campaigns, setCampaigns] = useState<Campaign[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchCampaigns() {
      setLoading(true);
      const res = await fetch('http://localhost:8000/sites/campaigns');
      const data = await res.json();
      setCampaigns(data);
      setLoading(false);
    }
    fetchCampaigns();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Campaigns</h1>
      <Link href="/campaigns/create" className="bg-orange-500 text-black px-3 py-2 rounded font-semibold hover:bg-orange-400 mb-4 inline-block">
        + New Campaign
      </Link>
      {loading ? (
        <div className="text-orange-400">Loading...</div>
      ) : (
        <ul className="mt-4 space-y-4">
          {campaigns.map(camp => (
            <li key={camp.id} className="bg-zinc-900 p-4 rounded">
              <Link href={`/campaigns/${camp.id}`} className="text-lg text-orange-400 hover:underline">{camp.name}</Link>
              <div className="text-zinc-300">{camp.description}</div>
              <div className="text-sm text-zinc-500">Pages: {camp.page_ids.join(', ') || 'None'}</div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
