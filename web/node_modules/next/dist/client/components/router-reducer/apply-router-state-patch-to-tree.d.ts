import type { FlightRouterState, FlightSegmentPath } from '../../../server/app-render/types';
/**
 * Apply the router state from the Flight response to the tree, including default segments.
 * Useful for patching the router cache when we expect to revalidate the full tree, such as with router.refresh or revalidatePath.
 * Creates a new router state tree.
 */
export declare function applyRouterStatePatchToFullTree(flightSegmentPath: FlightSegmentPath, flightRouterState: FlightRouterState, treePatch: FlightRouterState): FlightRouterState | null;
/**
 * Apply the router state from the Flight response, but skip patching default segments.
 * Useful for patching the router cache when navigating, where we persist the existing default segment if there isn't a new one.
 * Creates a new router state tree.
 */
export declare function applyRouterStatePatchToTreeSkipDefault(flightSegmentPath: FlightSegmentPath, flightRouterState: FlightRouterState, treePatch: FlightRouterState): FlightRouterState | null;
