import "./globals.css";
import Navbar from "../components/Navbar";
import { ConsentProvider } from "./context/ConsentContext";
import { FakeAuthProvider } from "./context/FakeAuthContext";
import React from "react";

export const metadata = {
  title: "InfernoSource",
  description: "AI-powered website generator",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-neutral-900 text-white antialiased">
        <ConsentProvider>
          <FakeAuthProvider>
            <Navbar />
            {children}
          </FakeAuthProvider>
        </ConsentProvider>
      </body>
    </html>
  );
}
