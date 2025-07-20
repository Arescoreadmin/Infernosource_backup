'use client';
import { useState } from 'react';

export default function RewritePage() {
  const [text, setText] = useState('');
  const [url, setUrl] = useState('');
  const [persona, setPersona] = useState('');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function handleRewrite(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const res = await fetch('http://localhost:8000/rewrite/rewrite-text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: text || undefined,
          url: url || undefined,
          persona: persona || undefined,
        }),
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
      <h1 className="text-2xl font-bold mb-4">AI Rewriter</h1>
      <form onSubmit={handleRewrite} className="mb-6 space-y-4">
        <textarea
          placeholder="Paste text to rewrite"
          className="w-full min-h-[120px] p-2 rounded bg-zinc-800 border border-zinc-700"
          value={text}
          onChange={e => setText(e.target.value)}
        />
        <input
          type="text"
          placeholder="(Optional) Source URL"
          className="w-full p-2 rounded bg-zinc-800 border border-zinc-700"
          value={url}
          onChange={e => setUrl(e.target.value)}
        />
        <input
          type="text"
          placeholder="(Optional) Persona/tone (e.g., witty marketer)"
          className="w-full p-2 rounded bg-zinc-800 border border-zinc-700"
          value={persona}
          onChange={e => setPersona(e.target.value)}
        />
        <button
          type="submit"
          className="bg-orange-500 px-4 py-2 rounded text-black font-semibold hover:bg-orange-400"
          disabled={loading}
        >
          {loading ? 'Rewriting...' : 'Rewrite'}
        </button>
      </form>
      <pre className="bg-zinc-900 p-4 rounded text-white min-h-[120px]">
        {result && JSON.stringify(result, null, 2)}
      </pre>
    </div>
  );
}
