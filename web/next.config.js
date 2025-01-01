/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: { unoptimized: true },
  assetPrefix: '',
  basePath: '',
  trailingSlash: true,
  distDir: 'out', // Add this
  experimental: {
    appDir: true
  }
}

module.exports = nextConfig