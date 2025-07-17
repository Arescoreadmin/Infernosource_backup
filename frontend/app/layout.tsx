import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'InfernoSource',
  description: 'Your one-stop AI-powered website builder and SEO suite.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50 text-gray-900 antialiased">
        {children}
      </body>
    </html>
  );
}
