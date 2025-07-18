// components/CTA.tsx
"use client";

export function CTA() {
  return (
    <section className="bg-red-600 text-white py-20 px-6 text-center">
      <div className="max-w-4xl mx-auto">
        <h2 className="text-4xl font-bold mb-4">Ready to Ignite Your Brand?</h2>
        <p className="text-lg mb-8">
          Join the beta launch and unlock tools built to dominate SEO, branding, and performance.
        </p>
        <a
          href="#pricing"
          className="inline-block bg-white text-red-600 font-semibold text-lg px-8 py-4 rounded-2xl hover:bg-gray-100 transition"
        >
          Claim Free Beta Access Now
        </a>
      </div>
    </section>
  );
}
