"use client";

import Link from "next/link";
import Image from "next/image";
import { usePathname, useRouter } from "next/navigation";
import { useState } from "react";

const navLinks = [
  { href: "/", label: "Home" },
  { href: "/features", label: "Features" },
  { href: "/about", label: "About" },
  { href: "/login", label: "Log In" },
];

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const [showBuildModal, setShowBuildModal] = useState(false);

  return (
    <>
      <nav className="w-full px-8 py-4 flex items-center justify-between bg-gradient-to-b from-neutral-950/70 via-neutral-900/80 to-neutral-900/60 shadow-md fixed top-0 z-20 backdrop-blur-md">
        {/* Logo (clickable, goes home) */}
        <Link href="/" className="flex items-center gap-3 group">
          <Image
            src="/logo.png"
            alt="InfernoSource Logo"
            width={48}
            height={48}
            priority
            className="rounded-full border border-white/10 group-hover:scale-105 transition-transform"
          />
          <span className="text-2xl font-extrabold tracking-wider text-white group-hover:text-orange-500 transition-colors">
            InfernoSource
          </span>
        </Link>

        {/* Navigation links */}
        <div className="flex items-center gap-6">
          {navLinks.map(({ href, label }) => (
            <Link
              key={href}
              href={href}
              className={`text-base font-medium hover:text-orange-400 transition-colors ${
                pathname === href ? "text-orange-500" : "text-white"
              }`}
            >
              {label}
            </Link>
          ))}

          {/* Build button (triggers modal) */}
          <button
            type="button"
            onClick={() => setShowBuildModal(true)}
            className="ml-2 px-5 py-2 rounded bg-gradient-to-r from-orange-500 to-yellow-400 text-black font-bold shadow hover:from-orange-600 hover:to-yellow-500 transition-colors"
          >
            Build
          </button>

          {/* Sign Up button */}
          <Link
            href="/signup"
            className="ml-2 px-5 py-2 rounded bg-gradient-to-r from-orange-500 to-yellow-400 text-black font-bold shadow hover:from-orange-600 hover:to-yellow-500 transition-colors"
          >
            Sign Up
          </Link>
        </div>
      </nav>

      {/* Build Modal */}
      {showBuildModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70">
          <div className="bg-white rounded-lg p-8 max-w-lg mx-auto shadow-xl relative">
            <button
              className="absolute top-3 right-3 text-gray-600 hover:text-black text-2xl font-bold"
              onClick={() => setShowBuildModal(false)}
              aria-label="Close"
            >
              &times;
            </button>
            <h2 className="text-2xl font-bold mb-3 text-gray-800">Welcome to Build!</h2>
            <p className="mb-4 text-gray-700">
              Create a new website from a product, idea, or service. We'll find top-rated sites for your inspiration.
              Choose from 3 options: <b>Clone</b>, <b>Merge</b> two sites, or <b>Create new</b>. 
              View thumbnails, SEO scores, and links.
            </p>
            <div className="mb-2 text-xs text-gray-500">
              <b>Legal:</b> We do <b>not</b> create exact duplicates. All sites are uniquely generated in compliance with copyright law.
            </div>
            <div className="flex gap-3 mt-4">
              <button
                className="px-5 py-2 rounded bg-orange-500 text-white font-bold hover:bg-orange-600"
                onClick={() => {
                  setShowBuildModal(false);
                  router.push("/build");
                }}
              >
                I Consent, Let's Build
              </button>
              <button
                className="px-5 py-2 rounded border border-gray-300 text-gray-700 font-bold hover:bg-gray-100"
                onClick={() => setShowBuildModal(false)}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
