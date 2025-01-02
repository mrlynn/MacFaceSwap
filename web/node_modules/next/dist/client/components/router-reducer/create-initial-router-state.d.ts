import type { ReactNode } from 'react';
import type { CacheNode } from '../../../shared/lib/app-router-context.shared-runtime';
import type { FlightRouterState, CacheNodeSeedData } from '../../../server/app-render/types';
export interface InitialRouterStateParameters {
    buildId: string;
    initialTree: FlightRouterState;
    initialCanonicalUrl: string;
    initialSeedData: CacheNodeSeedData;
    initialParallelRoutes: CacheNode['parallelRoutes'];
    isServer: boolean;
    location: Location | null;
    initialHead: ReactNode;
}
export declare function createInitialRouterState({ buildId, initialTree, initialSeedData, initialCanonicalUrl, initialParallelRoutes, isServer, location, initialHead, }: InitialRouterStateParameters): {
    buildId: string;
    tree: FlightRouterState;
    cache: import("../../../shared/lib/app-router-context.shared-runtime").ReadyCacheNode;
    prefetchCache: Map<any, any>;
    pushRef: {
        pendingPush: boolean;
        mpaNavigation: boolean;
        preserveCustomHistoryState: boolean;
    };
    focusAndScrollRef: {
        apply: boolean;
        onlyHashChange: boolean;
        hashFragment: null;
        segmentPaths: never[];
    };
    canonicalUrl: string;
    nextUrl: string | null;
};
