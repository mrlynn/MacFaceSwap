type OgModule = typeof import('next/dist/compiled/@vercel/og');
export declare class ImageResponse extends Response {
    static displayName: string;
    constructor(...args: ConstructorParameters<OgModule['ImageResponse']>);
}
export {};
