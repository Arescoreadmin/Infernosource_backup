export const metadata = {
  title: "Sign Up | InfernoSource",
  description: "Create your InfernoSource account."
};

export default function SignupPage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Sign Up</h1>
      <form className="w-full max-w-sm space-y-4">
        <input type="text" placeholder="First Name" className="w-full px-4 py-2 rounded border border-black text-black" required />
        <input type="text" placeholder="Last Name" className="w-full px-4 py-2 rounded border border-black text-black" required />
        <input type="email" placeholder="Email Address" className="w-full px-4 py-2 rounded border border-black text-black" required />
        <input type="password" placeholder="Password" className="w-full px-4 py-2 rounded border border-black text-black" required />
        <button className="w-full py-2 bg-gradient-to-r from-orange-500 to-yellow-400 text-black rounded font-bold">Sign Up</button>
      </form>
    </main>
  );
}
