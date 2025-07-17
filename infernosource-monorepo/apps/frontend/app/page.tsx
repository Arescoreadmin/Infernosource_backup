// /apps/frontend/app/page.tsx

export default function Home() {
  return (
    <main className="flex items-center justify-center min-h-screen bg-gradient-to-b from-black via-gray-800 to-gray-200">
      <div className="flex flex-col items-center">
        <img
          src="/logo.png"
          alt="InfernoSource Logo"
          className="opacity-50 mb-8 w-[300px] md:w-[400px] lg:w-[500px] max-w-full"
          style={{ filter: 'grayscale(1)' }}
        />
        <h1 className="text-5xl font-extrabold text-white mb-4 drop-shadow-lg tracking-tight text-center">
          InfernoSource
        </h1>
        <p className="text-xl text-gray-200/80 mb-8 text-center max-w-xl">
          AI-powered toolkit for modern web creation, rewriting, and research.
        </p>
      </div>
    </main>
  );
}
