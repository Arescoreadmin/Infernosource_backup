"use client";

import React, { createContext, useContext, useState, ReactNode } from "react";

type FakeAuthContextType = {
  isLoggedIn: boolean;
  logIn: () => void;
  logOut: () => void;
};

const FakeAuthContext = createContext<FakeAuthContextType | undefined>(undefined);

export const FakeAuthProvider = ({ children }: { children: ReactNode }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const logIn = () => setIsLoggedIn(true);
  const logOut = () => setIsLoggedIn(false);

  return (
    <FakeAuthContext.Provider value={{ isLoggedIn, logIn, logOut }}>
      {children}
    </FakeAuthContext.Provider>
  );
};

export const useFakeAuth = (): FakeAuthContextType => {
  const context = useContext(FakeAuthContext);
  if (!context) throw new Error("useFakeAuth must be used within a FakeAuthProvider");
  return context;
};
