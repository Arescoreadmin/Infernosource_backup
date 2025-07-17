/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      // Example: Add custom colors here
      // colors: {
      //   'inferno-orange': '#F24E1E',
      //   'inferno-red': '#D7263D',
      // },
    },
  },
  plugins: [],
};
