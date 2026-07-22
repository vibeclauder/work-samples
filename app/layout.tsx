import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'William Bradway — AI workflow and agent reliability',
  description:
    'Offline n8n and AI-agent reliability audits, bounded remediation, and verified implementation work by William Bradway.',
  icons: { icon: 'favicon.png' },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-zinc-950 font-sans text-zinc-300 antialiased">
        {children}
      </body>
    </html>
  );
}
