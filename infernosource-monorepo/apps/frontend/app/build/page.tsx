// /app/build/page.tsx
"use client";
import { useConsent } from "../context/ConsentContext";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function BuildPage() {
  const { hasConsented, setHasConsented } = useConsent();
  const router = useRouter();
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    if (!hasConsented) {
      setShowModal(true);
    }
  }, [hasConsented]);

  function handleConsent() {
    setHasConsented(true);
    setShowModal(false);
    // Optionally check for auth and redirect to signup if needed
  }

  function handleClose() {
    setShowModal(false);
    router.push("/"); // Back to home
  }

  if (!hasConsented && showModal) {
    return (
      <div className="fixed inset-0 z-50 bg-black/60 flex items-center justify-center">
        <div className="bg-white rounded-lg shadow-lg p-8 max-w-lg w-full text-black">
          <h2 className="text-xl font-bold mb-4">Before You Build</h2>
          <p className="mb-3">
            With InfernoSource, you can generate a website based on a product/service idea. We'll search for top-rated similar sites, and you can choose to clone, merge, or get inspiration. You’ll see thumbnails, links, and SEO scores. Please note: we do not create exact copies to avoid copyright infringement.
          </p>
          <p className="mb-4 text-xs text-gray-600">
            <strong>Legal:</strong> By proceeding, you acknowledge you are not creating an exact duplicate of any site.
          </p>
          <div className="flex justify-end gap-4">
            <button onClick={handleClose} className="text-gray-600 px-4 py-2 rounded hover:bg-gray-200">Cancel</button>
            <button onClick={handleConsent} className="bg-orange-500 text-white font-semibold px-5 py-2 rounded shadow hover:bg-orange-600">I Consent</button>
          </div>
        </div>
      </div>
    );
  }

  // If not authenticated, redirect to signup after consent:
  // ... your logic here

  return (
    <main className="pt-20 text-center">
      {/* Actual build page content here */}
      <h1 className="text-3xl font-bold mb-6">Let's Build Your Website!</h1>
      {/* etc. */}
    </main>
  );
}
