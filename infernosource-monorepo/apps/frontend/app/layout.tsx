// /apps/frontend/app/layout.tsx
import './globals.css';

export const metadata = {
  title: 'InfernoSource',
  description: 'AI-powered website generator',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50 text-gray-900 antialiased">
        {children}
      </body>
    </html>
  );
}
