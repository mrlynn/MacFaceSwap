/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  basePath: '/MacFaceSwap',
  images: { unoptimized: true },
  assetPrefix: '.',
}
module.exports = nextConfig
