"use client";

import { ReactNode } from "react";

interface BuildIntroModalProps {
  onClose: () => void;
}

export default function BuildIntroModal({ onClose }: BuildIntroModalProps) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm">
      <div className="bg-white rounded-xl shadow-lg p-8 max-w-lg w-full relative">
        <button
          className="absolute top-3 right-3 text-gray-600 hover:text-orange-500 text-xl"
          onClick={onClose}
          aria-label="Close modal"
        >
          &times;
        </button>
        <h2 className="text-2xl font-bold text-orange-600 mb-3 text-center">Welcome to Build!</h2>
        <p className="text-gray-800 mb-4 text-center">
          Here you can create a new website based on your product or service idea.
          InfernoSource will analyze the web, find the <b>top-rated competitor sites</b> that match your idea, and present you with <b>three top options</b>:
        </p>
        <ul className="list-disc pl-6 mb-4 text-gray-700">
          <li>Thumbnail preview of each competitor</li>
          <li>Direct links to view those sites</li>
          <li>SEO scores for each site</li>
        </ul>
        <p className="text-sm text-gray-600 mb-4">
          Choose to <b>clone</b> a site, <b>merge two</b> sites, or <b>create something entirely new</b> inspired by them.
        </p>
        <p className="text-xs text-red-500 font-semibold text-center">
          <b>Legal Disclaimer:</b> The sites you build are for inspiration and will not be exact duplicates. We strongly discourage copyright infringement—always make your content unique!
        </p>
        <button
          className="mt-6 w-full py-2 rounded bg-gradient-to-r from-orange-500 to-yellow-400 text-black font-bold shadow hover:from-orange-600 hover:to-yellow-500 transition-colors"
          onClick={onClose}
        >
          I Understand, Continue
        </button>
      </div>
    </div>
  );
}
