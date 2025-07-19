// apps/frontend/app/page.tsx

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-white text-gray-900 px-4">
      <section className="text-center space-y-4">
        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
          Welcome to InfernoSource 🔥
        </h1>
        <p className="text-lg text-gray-600 max-w-xl mx-auto">
          Ignite. Optimize. Dominate.  
          <br />
          Your AI-powered web replication platform is ready.
        </p>
        <div className="flex gap-4 justify-center mt-6">
          <button className="px-6 py-3 bg-black text-white rounded-lg hover:bg-gray-800 transition">
            Get Started
          </button>
          <button className="px-6 py-3 border border-black text-black rounded-lg hover:bg-black hover:text-white transition">
            Learn More
          </button>
        </div>
      </section>
    </main>
  );
}
