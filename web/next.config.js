/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  trailingSlash: true,
  // Update basePath for GitHub Pages
  basePath: '/MacFaceSwap',
  // Update assetPrefix for GitHub Pages
  assetPrefix: '/MacFaceSwap/',
  optimizeFonts: false,
  webpack: (config) => {
    config.resolve.fallback = { fs: false, path: false };
    return config;
  },
}

module.exports = nextConfig