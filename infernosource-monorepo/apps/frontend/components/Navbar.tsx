'use client';

import Image from 'next/image';

export default function Navbar() {
  return (
    <nav className="w-full py-3 px-8 flex items-center justify-between bg-neutral-900 border-b border-neutral-800">
      {/* Logo on the left */}
      <div className="flex items-center gap-3">
        <Image
          src="/logo.png"
          alt="InfernoSource Logo"
          width={44}
          height={44}
          className="rounded-full bg-white p-1 shadow-lg"
          priority
        />
        <span className="text-2xl font-extrabold tracking-wider text-white">
          InfernoSource
        </span>
      </div>

      {/* Navigation Links on the right */}
      <div className="flex gap-6 items-center">
        <a href="/" className="hover:text-orange-400 transition">Home</a>
        <a href="/features" className="hover:text-orange-400 transition">Features</a>
        <a href="/about" className="hover:text-orange-400 transition">About</a>
        <a href="/contact" className="hover:text-orange-400 transition">Contact</a>
        <a href="/login" className="px-4 py-1 bg-orange-600 rounded text-white font-semibold hover:bg-orange-700 transition">
          Login
        </a>
      </div>
    </nav>
  );
}
