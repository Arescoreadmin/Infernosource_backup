import "./globals.css";
import Navbar from "../components/Navbar";
import { ConsentProvider } from "./context/ConsentContext";

export const metadata = {
  title: "InfernoSource",
  description: "AI-powered website generator",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-neutral-900 text-white antialiased">
        <ConsentProvider>
          <Navbar />
          {children}
        </ConsentProvider>
      </body>
    </html>
  );
}
