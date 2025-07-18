// components/FAQ.tsx
"use client";

export function FAQ() {
  return (
    <section className="bg-gray-100 py-20 px-6">
      <div className="max-w-4xl mx-auto">
        <h2 className="text-4xl font-bold text-center mb-10">Frequently Asked Questions</h2>
        <div className="space-y-6">
          <div>
            <h3 className="text-xl font-semibold">How does site cloning work?</h3>
            <p className="text-gray-700 mt-2">
              You enter a URL, and our AI replicates its structure and key content in seconds—fully editable and SEO-optimized.
            </p>
          </div>

          <div>
            <h3 className="text-xl font-semibold">Is there a free trial?</h3>
            <p className="text-gray-700 mt-2">
              Yes, our Starter plan is free and includes limited but powerful tools to test drive the platform.
            </p>
          </div>

          <div>
            <h3 className="text-xl font-semibold">Can I use InfernoSource for clients?</h3>
            <p className="text-gray-700 mt-2">
              Absolutely. Our Agency plan is built for freelancers and firms that want to build and deploy for multiple clients.
            </p>
          </div>

          <div>
            <h3 className="text-xl font-semibold">What makes your SEO different?</h3>
            <p className="text-gray-700 mt-2">
              It's not cookie-cutter. Our AI dynamically crafts SEO structures per niche and target intent—always evolving.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}