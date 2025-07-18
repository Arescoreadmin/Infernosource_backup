const path = require("path");

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    appDir: true,
  },
  images: {
    domains: ["infernosource.com"],
  },
  assetPrefix: "https://infernosource.com",
  webpack: (config) => {
    config.resolve.alias["@app"] = path.resolve(__dirname, "app");
    config.resolve.alias["@components"] = path.resolve(__dirname, "components");
    config.resolve.alias["@context"] = path.resolve(__dirname, "app/context");
    config.resolve.alias["@public"] = path.resolve(__dirname, "public");
    return config;
  },
};

module.exports = nextConfig;
