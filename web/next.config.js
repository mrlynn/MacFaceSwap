/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: { unoptimized: true },
  assetPrefix: './', // Relative paths
  basePath: '',
}

module.exports = nextConfig