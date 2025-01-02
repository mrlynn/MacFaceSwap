import type { AppConfigDynamic } from '../../build/utils';
declare class StaticGenBailoutError extends Error {
    readonly code = "NEXT_STATIC_GEN_BAILOUT";
}
export declare function isStaticGenBailoutError(error: unknown): error is StaticGenBailoutError;
type BailoutOpts = {
    dynamic?: AppConfigDynamic;
    link?: string;
};
export type StaticGenerationBailout = (reason: string, opts?: BailoutOpts) => boolean | never;
export declare const staticGenerationBailout: StaticGenerationBailout;
export {};
