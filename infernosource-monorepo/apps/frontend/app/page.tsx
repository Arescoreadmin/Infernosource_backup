// apps/frontend/app/page.tsx
export default function Dashboard() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">🔥 InfernoSource Dashboard</h1>
      <p className="mb-8 text-lg">Clone. Rewrite. Monetize. Dominate.</p>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-zinc-900 rounded-lg p-6 shadow">
          <h2 className="text-xl font-semibold mb-2">Create Campaign</h2>
          <p>Generate new AI-powered ad funnels in seconds.</p>
        </div>
        <div className="bg-zinc-900 rounded-lg p-6 shadow">
          <h2 className="text-xl font-semibold mb-2">Clone Website</h2>
          <p>Scrape, rewrite, and rebuild your competitor’s site with a click.</p>
        </div>
        <div className="bg-zinc-900 rounded-lg p-6 shadow">
          <h2 className="text-xl font-semibold mb-2">Performance Analytics</h2>
          <p>Track campaign stats, heatmaps, and AI-driven recommendations.</p>
        </div>
      </div>
    </div>
  );
}
