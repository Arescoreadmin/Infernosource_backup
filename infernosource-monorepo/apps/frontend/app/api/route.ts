// For Next.js 13+ App Router (TypeScript)
// /app/api/consent/route.ts
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { consented } = await req.json();
  // TODO: Track by user id/cookie/ip/etc. Now just logs.
  console.log("Consent tracked:", consented);
  return NextResponse.json({ ok: true });
}
