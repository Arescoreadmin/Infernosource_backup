// components/Testimonials.tsx
"use client";

export function Testimonials() {
  return (
    <section className="bg-gray-50 py-20 px-6">
      <div className="max-w-6xl mx-auto text-center">
        <h2 className="text-4xl font-bold mb-12">Real Results. Real Voices.</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="bg-white shadow-lg p-6 rounded-2xl">
            <p className="text-gray-700 mb-4">
              “InfernoSource helped us clone and deploy a high-converting site in 48 hours. SEO results jumped in days.”
            </p>
            <p className="font-semibold text-gray-900">— Sarah T., Digital Strategist</p>
          </div>
          <div className="bg-white shadow-lg p-6 rounded-2xl">
            <p className="text-gray-700 mb-4">
              “Their AI funnel builder saved us weeks. We onboarded 200+ leads in the first week of launch.”
            </p>
            <p className="font-semibold text-gray-900">— Mike D., Startup Founder</p>
          </div>
          <div className="bg-white shadow-lg p-6 rounded-2xl">
            <p className="text-gray-700 mb-4">
              “Nothing out there touches this tool for branding, automation, and speed. Game-changer.”
            </p>
            <p className="font-semibold text-gray-900">— Lana R., Marketing Consultant</p>
          </div>
        </div>
      </div>
    </section>
  );
}
