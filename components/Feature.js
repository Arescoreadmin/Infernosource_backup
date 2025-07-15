export default function Feature({ title, desc }) {
  return (
    <div className="bg-gray-800 rounded-2xl p-6 shadow hover:shadow-lg transition">
      <h3 className="text-xl font-bold mb-2 text-infernoRed">{title}</h3>
      <p className="text-gray-300">{desc}</p>
    </div>
  );
}
