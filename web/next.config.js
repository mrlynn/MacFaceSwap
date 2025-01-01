/** @type {import('next').NextConfig} */
const isProd = process.env.NODE_ENV === 'production'

const nextConfig = {
  output: 'export',
  images: { unoptimized: true },
  assetPrefix: isProd ? 'https://macfaceswap.com' : '',
  basePath: '',
  trailingSlash: true
}

module.exports = nextConfig