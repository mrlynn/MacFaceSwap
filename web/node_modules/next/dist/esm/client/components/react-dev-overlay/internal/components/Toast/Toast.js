import { jsx as _jsx } from "react/jsx-runtime";
import * as React from "react";
export const Toast = function Toast(param) {
    let { onClick, children, className } = param;
    return /*#__PURE__*/ _jsx("div", {
        "data-nextjs-toast": true,
        onClick: onClick,
        className: className,
        children: /*#__PURE__*/ _jsx("div", {
            "data-nextjs-toast-wrapper": true,
            children: children
        })
    });
};

//# sourceMappingURL=Toast.js.map