"use client";
import Image from "next/image";

export default function Home() {
  return (
    <div className="relative flex flex-col items-center min-h-screen w-full bg-gradient-to-b from-black via-neutral-900 to-gray-800">
      {/* Logo - moved up */}
      <div className="pt-24 flex flex-col items-center w-full z-10 select-none pointer-events-none">
       <Image
          src="/logo.png"
          alt="InfernoSource Logo"
          width={400}
          height={200}
          className="opacity-50"
          style={{ maxWidth: "60vw", height: "auto" }}

 
        />
      </div>
      {/* Buttons and Tagline fixed at the bottom */}
      <div
        className="w-full flex flex-col items-center z-20"
        style={{ position: "absolute", bottom: "88px" }}
      >
        {/* Buttons */}
        <div className="flex gap-6 mb-8">
          <a
            href="/signup"
            className="px-8 py-3 rounded bg-white text-orange-600 font-semibold text-lg shadow hover:bg-orange-100 transition"
          >
            Get Started
          </a>
          <a
            href="/about"
            className="px-8 py-3 rounded bg-black/50 text-white font-semibold border border-white text-lg hover:bg-black/70 transition"
          >
            Learn More
          </a>
        </div>
        {/* Tagline */}
        <div className="mt-4">
          <span className="text-2xl text-white font-extrabold tracking-widest drop-shadow-xl">
            Ignite. Create. Dominate.
          </span>
        </div>
      </div>
    </div>
  );
}
