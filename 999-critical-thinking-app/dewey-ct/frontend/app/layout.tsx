import type { Metadata } from "next";
import localFont from "next/font/local";
import Header from "@/components/layout/Header";
import SearchPalette from "@/components/layout/SearchPalette";
import DataHydrator from "@/components/DataHydrator";
import ThemeProvider from "@/components/layout/ThemeProvider";
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "DeweyCT — Critical Thinking App",
  description: "Interactive companion to John Dewey's How We Think (1933)",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${geistSans.variable} ${geistMono.variable} min-h-screen bg-slate-50 text-slate-900 dark:bg-slate-900 dark:text-slate-100 antialiased`}>
        <ThemeProvider>
          <DataHydrator />
          <Header />
          <SearchPalette />
          <main className="mx-auto max-w-7xl px-4 py-8">
            {children}
          </main>
        </ThemeProvider>
      </body>
    </html>
  );
}
