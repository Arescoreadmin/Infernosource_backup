'use client'
import React, { ReactNode } from 'react';

type ErrorBoundaryProps = {
  children: ReactNode;
};

type ErrorBoundaryState = {
  hasError: boolean;
};

export default class ErrorBoundary extends React.Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="flex flex-col items-center justify-center h-96">
          <h2 className="text-2xl font-bold mb-4 text-red-500">Something went wrong.</h2>
          <p className="mb-4">Please refresh or contact support if the issue persists.</p>
        </div>
      );
    }
    return this.props.children;
  }
}
