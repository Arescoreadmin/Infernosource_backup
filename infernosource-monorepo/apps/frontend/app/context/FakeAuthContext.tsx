// /app/context/FakeAuthContext.tsx
"use client";
import React, { createContext, useContext, useState } from "react";

// Define a simple fake user shape
type FakeUser = { email: string } | null;

// Context value type
type FakeAuthContextType = {
  user: FakeUser;
  login: (email: string) => void;
  logout: () => void;
};

// Create the context
const FakeAuthContext = createContext<FakeAuthContextType | undefined>(undefined);

// Provider component
export function FakeAuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<FakeUser>(null);

  const login = (email: string) => setUser({ email });
  const logout = () => setUser(null);

  return (
    <FakeAuthContext.Provider value={{ user, login, logout }}>
      {children}
    </FakeAuthContext.Provider>
  );
}

// Hook to use the context
export function useFakeAuth() {
  const ctx = useContext(FakeAuthContext);
  if (!ctx) throw new Error("useFakeAuth must be used within a FakeAuthProvider");
  return ctx;
}
