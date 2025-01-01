/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: { unoptimized: true },
  basePath: '',
  assetPrefix: './', // Add this line
  trailingSlash: true // Add this line
}

module.exports = nextConfig