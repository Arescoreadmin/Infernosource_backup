"use client";

import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
} from "react";

type ConsentContextType = {
  hasConsented: boolean;
  setHasConsented: (value: boolean) => void;
};

const defaultValue: ConsentContextType = {
  hasConsented: false,
  setHasConsented: () => {},
};

const ConsentContext = createContext<ConsentContextType>(defaultValue);

export const useConsent = () => useContext(ConsentContext);

export const ConsentProvider = ({ children }: { children: ReactNode }) => {
  const [hasConsented, setHasConsented] = useState(false);

  useEffect(() => {
    const stored = localStorage.getItem("hasConsented");
    if (stored === "true") setHasConsented(true);
  }, []);

  useEffect(() => {
    localStorage.setItem("hasConsented", hasConsented.toString());
  }, [hasConsented]);

  return (
    <ConsentContext.Provider value={{ hasConsented, setHasConsented }}>
      {children}
    </ConsentContext.Provider>
  );
};
