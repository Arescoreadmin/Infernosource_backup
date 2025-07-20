'use client';
import { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';

type Campaign = {
  id: number;
  name: string;
  description?: string;
  page_ids: number[];
};

export default function CampaignDetails() {
  const params = useParams();
  const id = params?.id;
  const [campaign, setCampaign] = useState<Campaign | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!id) return;
    async function fetchCampaign() {
      setLoading(true);
      const res = await fetch(`http://localhost:8000/sites/campaigns/${id}`);
      const data = await res.json();
      setCampaign(data);
      setLoading(false);
    }
    fetchCampaign();
  }, [id]);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Campaign Details</h1>
      {loading ? (
        <div className="text-orange-400">Loading...</div>
      ) : campaign && (
        <div className="bg-zinc-900 rounded p-4">
          <div><b>ID:</b> {campaign.id}</div>
          <div><b>Name:</b> {campaign.name}</div>
          <div><b>Description:</b> {campaign.description || '—'}</div>
          <div className="mt-2">
            <b>Pages:</b>
            <ul className="list-disc ml-6">
              {campaign.page_ids.length ? campaign.page_ids.map(pid =>
                <li key={pid}>
                  <Link href={`/dashboard/${pid}`} className="text-orange-400 hover:underline">
                    Page {pid}
                  </Link>
                </li>
              ) : <li>None</li>}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}
