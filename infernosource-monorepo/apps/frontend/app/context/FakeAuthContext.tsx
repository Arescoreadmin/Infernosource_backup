"use client";

import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
} from "react";

type FakeAuthContextType = {
  user: any;
  setUser: (user: any) => void;
};

const defaultValue: FakeAuthContextType = {
  user: null,
  setUser: () => {},
};

const FakeAuthContext = createContext<FakeAuthContextType>(defaultValue);

export const useFakeAuth = () => useContext(FakeAuthContext);

export const FakeAuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    const storedUser = localStorage.getItem("fakeUser");
    if (storedUser) {
      try {
        setUser(JSON.parse(storedUser));
      } catch {
        setUser(null);
      }
    }
  }, []);

  useEffect(() => {
    if (user) {
      localStorage.setItem("fakeUser", JSON.stringify(user));
    } else {
      localStorage.removeItem("fakeUser");
    }
  }, [user]);

  return (
    <FakeAuthContext.Provider value={{ user, setUser }}>
      {children}
    </FakeAuthContext.Provider>
  );
};
