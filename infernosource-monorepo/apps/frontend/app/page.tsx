
// /apps/frontend/app/page.tsx
export default function Home() {
  return (
    <main className="flex flex-col min-h-screen items-center justify-center px-4 py-8">
      <h1 className="text-4xl font-bold mb-4">InfernoSource</h1>
      <p className="mb-8 text-lg text-gray-600 max-w-2xl text-center">
        Your AI-powered toolkit for scraping, rewriting, auditing, and generating websites with cutting-edge machine learning.
      </p>
      <div className="flex gap-4">
        <a href="/signup" className="px-6 py-3 bg-blue-600 text-white rounded shadow hover:bg-blue-700 transition">
          Get Started
        </a>
        <a href="/about" className="px-6 py-3 bg-white border border-blue-600 text-blue-600 rounded shadow hover:bg-blue-50 transition">
          Learn More
        </a>
      </div>
    </main>
  );
}
