import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "CollabWorld",
  description: "Spatial work management platform",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
