import type { Update as TurbopackUpdate } from '../../../build/swc';
export declare function extractModulesFromTurbopackMessage(data: TurbopackUpdate | TurbopackUpdate[]): Set<string>;
