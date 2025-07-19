// apps/frontend/components/Loading.tsx
export default function Loading() {
  return (
    <div className="flex items-center justify-center h-96">
      <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-orange-500"></div>
    </div>
  );
}
