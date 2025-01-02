"use client";

import { jsx as _jsx } from "react/jsx-runtime";
import React from "react";
import { createSearchParamsBailoutProxy } from "./searchparams-bailout-proxy";
export default function StaticGenerationSearchParamsBailoutProvider(param) {
    let { Component, propsForComponent, isStaticGeneration } = param;
    if (isStaticGeneration) {
        const searchParams = createSearchParamsBailoutProxy();
        return /*#__PURE__*/ _jsx(Component, {
            searchParams: searchParams,
            ...propsForComponent
        });
    }
    return /*#__PURE__*/ _jsx(Component, {
        ...propsForComponent
    });
}

//# sourceMappingURL=static-generation-searchparams-bailout-provider.js.map