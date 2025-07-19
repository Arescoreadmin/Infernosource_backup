// apps/frontend/app/layout.tsx
import '../styles/globals.css';
import Sidebar from '../components/Sidebar';
import TopBar from '../components/TopBar';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="flex min-h-screen bg-black text-white">
        <Sidebar />
        <div className="flex-1 flex flex-col min-h-screen">
          <TopBar />
          <main className="flex-1 p-6">{children}</main>
        </div>
      </body>
    </html>
  );
}
