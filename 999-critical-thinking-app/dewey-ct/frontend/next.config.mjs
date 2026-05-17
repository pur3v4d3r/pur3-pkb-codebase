/** @type {import('next').NextConfig} */
const nextConfig = {
  /**
   * Proxy all /api/* requests to the FastAPI backend.
   * Because this rewrite runs server-side, the browser never makes a
   * cross-origin request to localhost:8000 — no CORS issues possible.
   *
   * Override BACKEND_URL (or NEXT_PUBLIC_BACKEND_URL) in .env.local
   * for production deployments.
   */
  async rewrites() {
    const backendUrl =
      process.env.BACKEND_URL?.replace(/\/$/, '') ??
      process.env.NEXT_PUBLIC_BACKEND_URL?.replace(/\/$/, '') ??
      'http://localhost:8000';
    return [
      {
        source: '/api/:path*',
        destination: `${backendUrl}/api/:path*`,
      },
    ];
  },
};

export default nextConfig;
