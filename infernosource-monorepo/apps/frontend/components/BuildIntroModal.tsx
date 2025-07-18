"use client";
import { useConsent } from "../app/context/ConsentContext";
import { useFakeAuth } from "../app/context/FakeAuthContext";
import React from "react";
import { useRouter } from "next/navigation";

type BuildIntroModalProps = {
  open: boolean;
  onClose?: () => void;
};

export default function BuildIntroModal({ open, onClose }: BuildIntroModalProps) {
  const { setHasConsented } = useConsent();
  const { user } = useFakeAuth();
  const router = useRouter();

  const handleConsent = async () => {
    setHasConsented(true);
    setTimeout(() => {
      if (user) {
        router.push("/build");
      } else {
        router.push("/signup");
      }
    }, 200);
  };

  const handleClose = () => {
    setHasConsented(false);
    router.push("/");
    if (onClose) onClose();
  };

  if (!open) return null;

  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded shadow-lg w-full max-w-md">
        <h2 className="text-xl font-semibold mb-4">🚀 Ready to build?</h2>
        <p className="mb-4">By continuing, you consent to tracking and AI-powered optimization.</p>
        <div className="flex justify-end space-x-4">
          <button
            className="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300"
            onClick={handleClose}
          >
            Cancel
          </button>
          <button
            className="px-4 py-2 bg-black text-white rounded hover:bg-gray-800"
            onClick={handleConsent}
          >
            Let's Go
          </button>
        </div>
      </div>
    </div>
  );
}
