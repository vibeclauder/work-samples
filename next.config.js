/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  basePath: '/work-samples',
  trailingSlash: true,
  images: { unoptimized: true },
};

module.exports = nextConfig;
