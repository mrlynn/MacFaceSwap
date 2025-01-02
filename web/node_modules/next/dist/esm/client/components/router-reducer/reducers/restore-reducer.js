import { createHrefFromUrl } from "../create-href-from-url";
import { extractPathFromFlightRouterState } from "../compute-changed-path";
import { updateCacheNodeOnPopstateRestoration } from "../ppr-navigations";
export function restoreReducer(state, action) {
    const { url, tree } = action;
    const href = createHrefFromUrl(url);
    const oldCache = state.cache;
    const newCache = process.env.__NEXT_PPR ? // data for any segment whose dynamic data was already received. This
    // prevents an unnecessary flash back to PPR state during a
    // back/forward navigation.
    updateCacheNodeOnPopstateRestoration(oldCache, tree) : oldCache;
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
        nextUrl: (_extractPathFromFlightRouterState = extractPathFromFlightRouterState(tree)) != null ? _extractPathFromFlightRouterState : url.pathname
    };
}

//# sourceMappingURL=restore-reducer.js.map