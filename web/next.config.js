/** @type {import('next').NextConfig} */
const isProd = process.env.NODE_ENV === 'production'

const nextConfig = {
  output: 'export',
  images: { unoptimized: true },
  assetPrefix: isProd ? 'https://macfaceswap.com' : '',
  basePath: '',
  publicRuntimeConfig: {
    staticFolder: '/_next',
  },
  trailingSlash: true
}

module.exports = nextConfig
