import './globals.css';
import Navbar from '../components/Navbar'; // Adjust path if needed

export const metadata = {
  title: 'InfernoSource',
  description: 'AI-powered website generator',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        {children}
      </body>
    </html>
  );
}
