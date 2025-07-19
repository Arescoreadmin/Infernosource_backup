"use client";

import React, { createContext, useContext, useState, ReactNode } from "react";

type ConsentContextType = {
  hasConsented: boolean;
  setHasConsented: (value: boolean) => void;
};

const ConsentContext = createContext<ConsentContextType | undefined>(undefined);

export const ConsentProvider = ({ children }: { children: ReactNode }) => {
  const [hasConsented, setHasConsented] = useState(false);

  return (
    <ConsentContext.Provider value={{ hasConsented, setHasConsented }}>
      {children}
    </ConsentContext.Provider>
  );
};

export const useConsent = (): ConsentContextType => {
  const context = useContext(ConsentContext);
  if (!context) throw new Error("useConsent must be used within a ConsentProvider");
  return context;
};
