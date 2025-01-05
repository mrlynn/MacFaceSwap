// src/utils/routes.js
export const getBasePath = () => {
    if (typeof window !== 'undefined') {
      // Check if we're on the custom domain
      if (window.location.hostname === 'macfaceswap.com') {
        return '';
      }
    }
    // Default to repository name for GitHub Pages
    return process.env.GITHUB_PAGES ? '/MacFaceSwap' : '';
  };
  
  export const withBasePath = (path) => {
    return `${getBasePath()}${path}`;
  };