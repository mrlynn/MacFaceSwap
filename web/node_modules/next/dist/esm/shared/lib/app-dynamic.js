import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import React from "react";
import Loadable from "./lazy-dynamic/loadable";
export default function dynamic(dynamicOptions, options) {
    const loadableOptions = {
        // A loading component is not required, so we default it
        loading: (param)=>{
            let { error, isLoading, pastDelay } = param;
            if (!pastDelay) return null;
            if (process.env.NODE_ENV !== "production") {
                if (isLoading) {
                    return null;
                }
                if (error) {
                    return /*#__PURE__*/ _jsxs("p", {
                        children: [
                            error.message,
                            /*#__PURE__*/ _jsx("br", {}),
                            error.stack
                        ]
                    });
                }
            }
            return null;
        }
    };
    if (typeof dynamicOptions === "function") {
        loadableOptions.loader = dynamicOptions;
    }
    return Loadable({
        ...loadableOptions,
        ...options
    });
}

//# sourceMappingURL=app-dynamic.js.map