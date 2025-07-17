import React from "react";
type Props = React.ButtonHTMLAttributes<HTMLButtonElement> & { children: React.ReactNode };

export default function Button({ children, ...props }: Props) {
  return (
    <button
      {...props}
      className={`px-6 py-2 rounded bg-orange-600 text-white font-semibold shadow hover:bg-orange-700 transition ${props.className ?? ''}`}
    >
      {children}
    </button>
  );
}
