"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
0 && (module.exports = {
    applyRouterStatePatchToFullTree: null,
    applyRouterStatePatchToTreeSkipDefault: null
});
function _export(target, all) {
    for(var name in all)Object.defineProperty(target, name, {
        enumerable: true,
        get: all[name]
    });
}
_export(exports, {
    applyRouterStatePatchToFullTree: function() {
        return applyRouterStatePatchToFullTree;
    },
    applyRouterStatePatchToTreeSkipDefault: function() {
        return applyRouterStatePatchToTreeSkipDefault;
    }
});
const _segment = require("../../../shared/lib/segment");
const _matchsegments = require("../match-segments");
/**
 * Deep merge of the two router states. Parallel route keys are preserved if the patch doesn't have them.
 */ function applyPatch(initialTree, patchTree, applyPatchToDefaultSegment) {
    if (applyPatchToDefaultSegment === void 0) applyPatchToDefaultSegment = false;
    const [initialSegment, initialParallelRoutes] = initialTree;
    const [patchSegment, patchParallelRoutes] = patchTree;
    // if the applied patch segment is __DEFAULT__ then it can be ignored in favor of the initial tree
    // this is because the __DEFAULT__ segment is used as a placeholder on navigation
    // however, there are cases where we _do_ want to apply the patch to the default segment,
    // such as when revalidating the router cache with router.refresh/revalidatePath
    if (!applyPatchToDefaultSegment && patchSegment === _segment.DEFAULT_SEGMENT_KEY && initialSegment !== _segment.DEFAULT_SEGMENT_KEY) {
        return initialTree;
    }
    if ((0, _matchsegments.matchSegment)(initialSegment, patchSegment)) {
        const newParallelRoutes = {};
        for(const key in initialParallelRoutes){
            const isInPatchTreeParallelRoutes = typeof patchParallelRoutes[key] !== "undefined";
            if (isInPatchTreeParallelRoutes) {
                newParallelRoutes[key] = applyPatch(initialParallelRoutes[key], patchParallelRoutes[key], applyPatchToDefaultSegment);
            } else {
                newParallelRoutes[key] = initialParallelRoutes[key];
            }
        }
        for(const key in patchParallelRoutes){
            if (newParallelRoutes[key]) {
                continue;
            }
            newParallelRoutes[key] = patchParallelRoutes[key];
        }
        const tree = [
            initialSegment,
            newParallelRoutes
        ];
        if (initialTree[2]) {
            tree[2] = initialTree[2];
        }
        if (initialTree[3]) {
            tree[3] = initialTree[3];
        }
        if (initialTree[4]) {
            tree[4] = initialTree[4];
        }
        return tree;
    }
    return patchTree;
}
function applyRouterStatePatchToTreeImpl(flightSegmentPath, flightRouterState, treePatch, applyPatchDefaultSegment) {
    if (applyPatchDefaultSegment === void 0) applyPatchDefaultSegment = false;
    const [segment, parallelRoutes, , , isRootLayout] = flightRouterState;
    // Root refresh
    if (flightSegmentPath.length === 1) {
        const tree = applyPatch(flightRouterState, treePatch, applyPatchDefaultSegment);
        return tree;
    }
    const [currentSegment, parallelRouteKey] = flightSegmentPath;
    // Tree path returned from the server should always match up with the current tree in the browser
    if (!(0, _matchsegments.matchSegment)(currentSegment, segment)) {
        return null;
    }
    const lastSegment = flightSegmentPath.length === 2;
    let parallelRoutePatch;
    if (lastSegment) {
        parallelRoutePatch = applyPatch(parallelRoutes[parallelRouteKey], treePatch, applyPatchDefaultSegment);
    } else {
        parallelRoutePatch = applyRouterStatePatchToTreeImpl(flightSegmentPath.slice(2), parallelRoutes[parallelRouteKey], treePatch, applyPatchDefaultSegment);
        if (parallelRoutePatch === null) {
            return null;
        }
    }
    const tree = [
        flightSegmentPath[0],
        {
            ...parallelRoutes,
            [parallelRouteKey]: parallelRoutePatch
        }
    ];
    // Current segment is the root layout
    if (isRootLayout) {
        tree[4] = true;
    }
    return tree;
}
function applyRouterStatePatchToFullTree(flightSegmentPath, flightRouterState, treePatch) {
    return applyRouterStatePatchToTreeImpl(flightSegmentPath, flightRouterState, treePatch, true);
}
function applyRouterStatePatchToTreeSkipDefault(flightSegmentPath, flightRouterState, treePatch) {
    return applyRouterStatePatchToTreeImpl(flightSegmentPath, flightRouterState, treePatch, false);
}

if ((typeof exports.default === 'function' || (typeof exports.default === 'object' && exports.default !== null)) && typeof exports.default.__esModule === 'undefined') {
  Object.defineProperty(exports.default, '__esModule', { value: true });
  Object.assign(exports.default, exports);
  module.exports = exports.default;
}

//# sourceMappingURL=apply-router-state-patch-to-tree.js.map