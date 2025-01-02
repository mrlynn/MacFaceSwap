"use client";

"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
0 && (module.exports = {
    AppRouterContext: null,
    LayoutRouterContext: null,
    GlobalLayoutRouterContext: null,
    TemplateContext: null,
    MissingSlotContext: null
});
function _export(target, all) {
    for(var name in all)Object.defineProperty(target, name, {
        enumerable: true,
        get: all[name]
    });
}
_export(exports, {
    AppRouterContext: function() {
        return AppRouterContext;
    },
    LayoutRouterContext: function() {
        return LayoutRouterContext;
    },
    GlobalLayoutRouterContext: function() {
        return GlobalLayoutRouterContext;
    },
    TemplateContext: function() {
        return TemplateContext;
    },
    MissingSlotContext: function() {
        return MissingSlotContext;
    }
});
const _interop_require_default = require("@swc/helpers/_/_interop_require_default");
const _react = /*#__PURE__*/ _interop_require_default._(require("react"));
const AppRouterContext = _react.default.createContext(null);
const LayoutRouterContext = _react.default.createContext(null);
const GlobalLayoutRouterContext = _react.default.createContext(null);
const TemplateContext = _react.default.createContext(null);
if (process.env.NODE_ENV !== "production") {
    AppRouterContext.displayName = "AppRouterContext";
    LayoutRouterContext.displayName = "LayoutRouterContext";
    GlobalLayoutRouterContext.displayName = "GlobalLayoutRouterContext";
    TemplateContext.displayName = "TemplateContext";
}
const MissingSlotContext = _react.default.createContext(new Set());

//# sourceMappingURL=app-router-context.shared-runtime.js.map