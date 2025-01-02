"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
Object.defineProperty(exports, "createPrefetchCacheKey", {
    enumerable: true,
    get: function() {
        return createPrefetchCacheKey;
    }
});
const _addpathprefix = require("../../../../shared/lib/router/utils/add-path-prefix");
const _pathhasprefix = require("../../../../shared/lib/router/utils/path-has-prefix");
const _createhreffromurl = require("../create-href-from-url");
function createPrefetchCacheKey(url, nextUrl) {
    const pathnameFromUrl = (0, _createhreffromurl.createHrefFromUrl)(url, // Ensures the hash is not part of the cache key as it does not impact the server fetch
    false);
    // delimit the prefix so we don't conflict with other pages
    const nextUrlPrefix = "" + nextUrl + "%";
    // Route interception depends on `nextUrl` values which aren't a 1:1 mapping to a URL
    // The cache key that we store needs to use `nextUrl` to properly distinguish cache entries
    if (nextUrl && !(0, _pathhasprefix.pathHasPrefix)(pathnameFromUrl, nextUrl)) {
        return (0, _addpathprefix.addPathPrefix)(pathnameFromUrl, nextUrlPrefix);
    }
    return pathnameFromUrl;
}

if ((typeof exports.default === 'function' || (typeof exports.default === 'object' && exports.default !== null)) && typeof exports.default.__esModule === 'undefined') {
  Object.defineProperty(exports.default, '__esModule', { value: true });
  Object.assign(exports.default, exports);
  module.exports = exports.default;
}

//# sourceMappingURL=create-prefetch-cache-key.js.map