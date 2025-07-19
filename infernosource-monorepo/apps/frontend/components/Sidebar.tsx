// apps/frontend/components/Sidebar.tsx
import Image from 'next/image';

export default function Sidebar() {
  return (
    <nav className="w-64 bg-zinc-950 h-screen flex flex-col justify-between py-8 px-6 border-r border-zinc-800">
      <div>
        <div className="flex items-center mb-8">
          <Image src="/infernosource-logo.png" width={40} height={40} alt="InfernoSource" />

          <span className="ml-3 font-bold text-xl text-orange-500">InfernoSource</span>
        </div>
        <ul className="space-y-4">
          <li><a href="/" className="hover:text-orange-400">Dashboard</a></li>
          <li><a href="/create" className="hover:text-orange-400">Create</a></li>
          <li><a href="/dashboard" className="hover:text-orange-400">Campaigns</a></li>
          <li><a href="/settings" className="hover:text-orange-400">Settings</a></li>
        </ul>
      </div>
      <div>
        <a href="https://your-upgrade-link" className="block text-center bg-orange-500 text-black font-semibold px-4 py-2 rounded hover:bg-orange-400 transition">Upgrade</a>
      </div>
    </nav>
  );
}
