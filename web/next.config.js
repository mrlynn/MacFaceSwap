/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  basePath: '/MacFaceSwap',
  images: { unoptimized: true },
  assetPrefix: './', // Relative paths
  basePath: '',
}

module.exports = nextConfig