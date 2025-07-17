"use client";
import React, { createContext, useContext, useState, useEffect } from "react";

type ConsentContextType = {
  hasConsented: boolean;
  setHasConsented: (val: boolean) => void;
};

const ConsentContext = createContext<ConsentContextType>({
  hasConsented: false,
  setHasConsented: () => {},
});

export const ConsentProvider = ({ children }: { children: React.ReactNode }) => {
  const [hasConsented, setHasConsented] = useState(false);

  useEffect(() => {
    // Sync with localStorage for persistence
    const storedConsent = localStorage.getItem("infernosource_consent");
    setHasConsented(storedConsent === "true");
  }, []);

  const updateConsent = (val: boolean) => {
    setHasConsented(val);
    localStorage.setItem("infernosource_consent", val ? "true" : "false");
  };

  return (
    <ConsentContext.Provider value={{ hasConsented, setHasConsented: updateConsent }}>
      {children}
    </ConsentContext.Provider>
  );
};

export const useConsent = () => useContext(ConsentContext);
