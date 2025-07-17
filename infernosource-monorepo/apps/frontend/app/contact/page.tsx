export const metadata = {
  title: "About InfernoSource",
  description: "Learn more about the InfernoSource platform and team.",
};

export default function ContactPage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-4xl font-bold mb-4">Contact Us</h1>
      <form className="w-full max-w-md space-y-4">
        <input type="text" placeholder="Name" className="w-full px-4 py-2 rounded" />
        <input type="email" placeholder="Email" className="w-full px-4 py-2 rounded" />
        <textarea placeholder="Message" className="w-full px-4 py-2 rounded min-h-[100px]" />
        <button className="w-full py-2 bg-orange-600 text-white rounded">Send Message</button>
      </form>
    </main>
  );
}
