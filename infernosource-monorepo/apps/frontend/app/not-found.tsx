export default function NotFound() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-neutral-900 text-white">
      <h1 className="text-5xl font-bold mb-4">404</h1>
      <p className="mb-6 text-xl">Page Not Found</p>
      <a href="/" className="px-4 py-2 rounded bg-orange-600 text-white hover:bg-orange-700 transition">Go Home</a>
    </main>
  );
}