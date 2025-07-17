// /apps/frontend/app/features/page.tsx

export const metadata = {
  title: "Features - InfernoSource",
  description: "Discover the powerful features of InfernoSource.",
};

const features = [
  {
    title: "AI Content Rewriting",
    description: "Rewrite and optimize your website’s content using advanced machine learning.",
    icon: "📝",
  },
  {
    title: "Competitor Scraping",
    description: "Easily gather data and insights from competitor websites for research and growth.",
    icon: "🕷️",
  },
  {
    title: "SEO Audit Tools",
    description: "Instantly audit your website for SEO opportunities and improvements.",
    icon: "🔍",
  },
  {
    title: "Analytics Dashboard",
    description: "Monitor your site’s performance and user behavior with clear, actionable analytics.",
    icon: "📊",
  },
  // Add more features here!
];

export default function FeaturesPage() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-neutral-900 via-neutral-800 to-neutral-700 text-white flex flex-col items-center pt-24 pb-16">
      <h1 className="text-4xl font-extrabold mb-4 tracking-tight">Features</h1>
      <p className="mb-10 text-lg text-gray-200 max-w-2xl text-center">
        Everything you need to <span className="text-orange-400 font-semibold">ignite</span>, <span className="text-yellow-400 font-semibold">create</span>, and <span className="text-red-400 font-semibold">dominate</span> your digital presence.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-4xl">
        {features.map(({ title, description, icon }) => (
          <div key={title} className="bg-neutral-800 rounded-xl shadow-md p-8 flex flex-col items-center transition hover:scale-105 hover:bg-neutral-700">
            <div className="text-5xl mb-4">{icon}</div>
            <h2 className="text-2xl font-bold mb-2">{title}</h2>
            <p className="text-gray-300 text-center">{description}</p>
          </div>
        ))}
      </div>
    </main>
  );
}
