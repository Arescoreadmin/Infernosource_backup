// apps/frontend/components/TopBar.tsx
import Image from 'next/image';

export default function TopBar() {
  return (
    <header className="w-full flex items-center justify-between px-6 py-4 bg-zinc-900 border-b border-zinc-800">
      <span className="font-semibold text-lg">🔥 Welcome to InfernoSource</span>
      <div className="flex items-center gap-3">
        <Image src="/flame.png" width={28} height={28} alt="Flame" />
        <span className="text-sm text-zinc-300">v0.1 MVP</span>
      </div>
    </header>
  );
}
