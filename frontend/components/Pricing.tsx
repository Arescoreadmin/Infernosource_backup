// components/Pricing.tsx
"use client";

export function Pricing() {
  return (
    <section id="pricing" className="bg-white py-20 px-6">
      <div className="max-w-4xl mx-auto text-center">
        <h2 className="text-4xl font-bold mb-10">Simple, Scalable Pricing</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="border rounded-2xl p-6 shadow">
            <h3 className="text-xl font-semibold mb-4">Starter</h3>
            <p className="text-3xl font-bold mb-4">$0</p>
            <ul className="text-left text-gray-700 space-y-2">
              <li>✅ 1 Site Clone</li>
              <li>✅ Basic SEO Setup</li>
              <li>✅ 3 Funnel Templates</li>
            </ul>
          </div>

          <div className="border-4 border-red-600 rounded-2xl p-6 shadow">
            <h3 className="text-xl font-semibold mb-4 text-red-600">Pro (Beta Special)</h3>
            <p className="text-3xl font-bold mb-4">$29/mo</p>
            <ul className="text-left text-gray-700 space-y-2">
              <li>✅ Unlimited Site Cloning</li>
              <li>✅ Full SEO Suite</li>
              <li>✅ Auto Funnels & Posting</li>
              <li>✅ Beta Tester Bonuses</li>
            </ul>
          </div>

          <div className="border rounded-2xl p-6 shadow">
            <h3 className="text-xl font-semibold mb-4">Agency</h3>
            <p className="text-3xl font-bold mb-4">$99/mo</p>
            <ul className="text-left text-gray-700 space-y-2">
              <li>✅ Multi-Client Support</li>
              <li>✅ Custom AI Branding</li>
              <li>✅ Dedicated Support</li>
              <li>✅ API + Webhooks</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}