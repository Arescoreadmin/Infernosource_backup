// app/page.tsx (main homepage)
"use client";

import { Hero } from "@/components/Hero";
import { Features } from "@/components/Features";
import { CTA } from "@/components/CTA";
import { Testimonials } from "@/components/Testimonials";
import { Pricing } from "@/components/Pricing";
import { FAQ } from "@/components/FAQ";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-white text-gray-900">
      <Hero />
      <Features />
      <CTA />
      <Testimonials />
      <Pricing />
      <FAQ />
    </main>
  );
}
