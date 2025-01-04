/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  trailingSlash: true,
  // For custom domain, we use minimal configuration
  optimizeFonts: false,
  // Ensure static files are handled correctly
  pageExtensions: ['js', 'jsx', 'ts', 'tsx'],
  // Add basePath for GitHub Pages
  basePath: '/MacFaceSwap',
  // Configure webpack
  webpack: (config) => {
    config.resolve.fallback = { fs: false, path: false };
    return config;
  },
}

module.exports = nextConfig