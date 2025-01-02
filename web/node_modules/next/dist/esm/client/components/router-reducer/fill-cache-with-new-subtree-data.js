import { invalidateCacheByRouterState } from "./invalidate-cache-by-router-state";
import { fillLazyItemsTillLeafWithHead } from "./fill-lazy-items-till-leaf-with-head";
import { createRouterCacheKey } from "./create-router-cache-key";
/**
 * Fill cache with rsc based on flightDataPath
 */ export function fillCacheWithNewSubTreeData(newCache, existingCache, flightDataPath, wasPrefetched) {
    const isLastEntry = flightDataPath.length <= 5;
    const [parallelRouteKey, segment] = flightDataPath;
    const cacheKey = createRouterCacheKey(segment);
    const existingChildSegmentMap = existingCache.parallelRoutes.get(parallelRouteKey);
    if (!existingChildSegmentMap) {
        // Bailout because the existing cache does not have the path to the leaf node
        // Will trigger lazy fetch in layout-router because of missing segment
        return;
    }
    let childSegmentMap = newCache.parallelRoutes.get(parallelRouteKey);
    if (!childSegmentMap || childSegmentMap === existingChildSegmentMap) {
        childSegmentMap = new Map(existingChildSegmentMap);
        newCache.parallelRoutes.set(parallelRouteKey, childSegmentMap);
    }
    const existingChildCacheNode = existingChildSegmentMap.get(cacheKey);
    let childCacheNode = childSegmentMap.get(cacheKey);
    if (isLastEntry) {
        if (!childCacheNode || !childCacheNode.lazyData || childCacheNode === existingChildCacheNode) {
            const seedData = flightDataPath[3];
            const rsc = seedData[2];
            childCacheNode = {
                lazyData: null,
                rsc,
                prefetchRsc: null,
                // Ensure segments other than the one we got data for are preserved.
                parallelRoutes: existingChildCacheNode ? new Map(existingChildCacheNode.parallelRoutes) : new Map()
            };
            if (existingChildCacheNode) {
                invalidateCacheByRouterState(childCacheNode, existingChildCacheNode, flightDataPath[2]);
            }
            fillLazyItemsTillLeafWithHead(childCacheNode, existingChildCacheNode, flightDataPath[2], seedData, flightDataPath[4], wasPrefetched);
            childSegmentMap.set(cacheKey, childCacheNode);
        }
        return;
    }
    if (!childCacheNode || !existingChildCacheNode) {
        // Bailout because the existing cache does not have the path to the leaf node
        // Will trigger lazy fetch in layout-router because of missing segment
        return;
    }
    if (childCacheNode === existingChildCacheNode) {
        childCacheNode = {
            lazyData: childCacheNode.lazyData,
            rsc: childCacheNode.rsc,
            prefetchRsc: childCacheNode.prefetchRsc,
            parallelRoutes: new Map(childCacheNode.parallelRoutes)
        };
        childSegmentMap.set(cacheKey, childCacheNode);
    }
    fillCacheWithNewSubTreeData(childCacheNode, existingChildCacheNode, flightDataPath.slice(2), wasPrefetched);
}

//# sourceMappingURL=fill-cache-with-new-subtree-data.js.map