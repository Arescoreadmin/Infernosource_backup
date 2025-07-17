export const metadata = {
  title: "About InfernoSource",
  description: "Learn more about the InfernoSource platform and team.",
};

export default function LoginPage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Log In</h1>
      <form className="w-full max-w-sm space-y-4">
        <input
          type="email"
          placeholder="Email"
          className="w-full px-4 py-2 rounded bg-white text-black border focus:outline-none focus:ring-2 focus:ring-orange-500"
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full px-4 py-2 rounded bg-white text-black border focus:outline-none focus:ring-2 focus:ring-orange-500"
        />
        <button className="w-full py-2 bg-orange-600 text-white rounded hover:bg-orange-700 transition">
          Log In
        </button>
      </form>
    </main>
  );
}
