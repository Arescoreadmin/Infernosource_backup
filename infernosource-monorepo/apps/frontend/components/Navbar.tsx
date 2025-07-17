// /apps/frontend/components/Navbar.tsx
import Link from 'next/link';


export default function Navbar() {
  return (
    <nav className="flex items-center justify-between px-6 py-4 bg-black/70 backdrop-blur text-white shadow-md">
      <div className="flex items-center gap-3">
        <img src="/logo.png" alt="InfernoSource Logo" className="h-10 w-10 rounded-full bg-white p-1" />
        <span className="font-bold text-xl tracking-wide">InfernoSource</span>
      </div>
      <div className="flex gap-6">
        <a href="/" className="hover:underline">Home</a>
        <a href="/about" className="hover:underline">About</a>
        <a href="/features" className="hover:underline">Features</a>
        <a href="/login" className="bg-white text-black rounded px-4 py-1 font-semibold hover:bg-orange-100 transition">Login</a>
      </div>
    </nav>
  );
}