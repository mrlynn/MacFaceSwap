"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
Object.defineProperty(exports, "restoreReducer", {
    enumerable: true,
    get: function() {
        return restoreReducer;
    }
});
const _createhreffromurl = require("../create-href-from-url");
const _computechangedpath = require("../compute-changed-path");
const _pprnavigations = require("../ppr-navigations");
function restoreReducer(state, action) {
    const { url, tree } = action;
    const href = (0, _createhreffromurl.createHrefFromUrl)(url);
    const oldCache = state.cache;
    const newCache = process.env.__NEXT_PPR ? // data for any segment whose dynamic data was already received. This
    // prevents an unnecessary flash back to PPR state during a
    // back/forward navigation.
    (0, _pprnavigations.updateCacheNodeOnPopstateRestoration)(oldCache, tree) : oldCache;
    var _extractPathFromFlightRouterState;
    return {
        buildId: state.buildId,
        // Set canonical url
        canonicalUrl: href,
        pushRef: {
            pendingPush: false,
            mpaNavigation: false,
            // Ensures that the custom history state that was set is preserved when applying this update.
            preserveCustomHistoryState: true
        },
        focusAndScrollRef: state.focusAndScrollRef,
        cache: newCache,
        prefetchCache: state.prefetchCache,
        // Restore provided tree
        tree: tree,
        nextUrl: (_extractPathFromFlightRouterState = (0, _computechangedpath.extractPathFromFlightRouterState)(tree)) != null ? _extractPathFromFlightRouterState : url.pathname
    };
}

if ((typeof exports.default === 'function' || (typeof exports.default === 'object' && exports.default !== null)) && typeof exports.default.__esModule === 'undefined') {
  Object.defineProperty(exports.default, '__esModule', { value: true });
  Object.assign(exports.default, exports);
  module.exports = exports.default;
}

//# sourceMappingURL=restore-reducer.js.map