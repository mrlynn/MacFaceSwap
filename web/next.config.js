/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  trailingSlash: true,
  optimizeFonts: false,
  pageExtensions: ['js', 'jsx', 'ts', 'tsx'],
  // Check if we're deploying to GitHub Pages
  assetPrefix: process.env.NODE_ENV === 'production' ? 'https://macfaceswap.com' : '',
  // Configure webpack
  webpack: (config) => {
    config.resolve.fallback = { fs: false, path: false };
    return config;
  },
}

module.exports = nextConfig