import './globals.css';

export const metadata = {
  title: 'InfernoSource',
  description: 'AI-powered website generator',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="min-h-screen bg-gray-50 text-gray-900 antialiased">
          {children}
        </div>
      </body>
    </html>
  );
}
