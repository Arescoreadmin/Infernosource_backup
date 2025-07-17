import Image from "next/image";

export default function Header() {
  return (
    <header className="w-full py-4 bg-white shadow flex items-center px-6">
      <Image
        src="/logo.png"
        alt="InfernoSource Logo"
        width={40}
        height={40}
        className="mr-4"
      />
      <nav className="flex gap-8">
        <a href="/" className="font-bold text-inferno-orange hover:underline">Home</a>
        <a href="/about" className="hover:underline">About</a>
        <a href="/signup" className="hover:underline">Sign Up</a>
        <a href="/dashboard" className="hover:underline">Dashboard</a>
      </nav>
    </header>
  );
}
