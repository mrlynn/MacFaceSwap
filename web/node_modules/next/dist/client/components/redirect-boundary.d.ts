/// <reference types="react/experimental" />
import React from 'react';
import type { AppRouterInstance } from '../../shared/lib/app-router-context.shared-runtime';
import { RedirectType } from './redirect';
interface RedirectBoundaryProps {
    router: AppRouterInstance;
    children: React.ReactNode;
}
export declare class RedirectErrorBoundary extends React.Component<RedirectBoundaryProps, {
    redirect: string | null;
    redirectType: RedirectType | null;
}> {
    constructor(props: RedirectBoundaryProps);
    static getDerivedStateFromError(error: any): {
        redirect: string;
        redirectType: RedirectType;
    };
    render(): string | number | boolean | Iterable<React.ReactNode> | React.PromiseLikeOfReactNode | import("react/jsx-runtime").JSX.Element | null | undefined;
}
export declare function RedirectBoundary({ children }: {
    children: React.ReactNode;
}): import("react/jsx-runtime").JSX.Element;
export {};
