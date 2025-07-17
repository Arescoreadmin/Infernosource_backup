import './globals.css';
import Navbar from '../components/Navbar';

export const metadata = {
  title: 'InfernoSource',
  description: 'AI-powered website generator',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-neutral-900 text-white antialiased min-h-screen">
        {/* Use a flex column so Navbar + main fills the height */}
        <div className="flex flex-col min-h-screen">
          <Navbar />
          <main className="flex-1 flex flex-col items-center justify-center">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
