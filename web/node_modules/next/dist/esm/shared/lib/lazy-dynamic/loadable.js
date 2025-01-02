import { jsx as _jsx } from "react/jsx-runtime";
import { Suspense, lazy } from "react";
import { BailoutToCSR } from "./dynamic-bailout-to-csr";
// Normalize loader to return the module as form { default: Component } for `React.lazy`.
// Also for backward compatible since next/dynamic allows to resolve a component directly with loader
// Client component reference proxy need to be converted to a module.
function convertModule(mod) {
    var _mod_default;
    return {
        default: (_mod_default = mod == null ? void 0 : mod.default) != null ? _mod_default : mod
    };
}
const defaultOptions = {
    loader: ()=>Promise.resolve(convertModule(()=>null)),
    loading: null,
    ssr: true
};
function Loadable(options) {
    const opts = {
        ...defaultOptions,
        ...options
    };
    const Lazy = /*#__PURE__*/ lazy(()=>opts.loader().then(convertModule));
    const Loading = opts.loading;
    function LoadableComponent(props) {
        const fallbackElement = Loading ? /*#__PURE__*/ _jsx(Loading, {
            isLoading: true,
            pastDelay: true,
            error: null
        }) : null;
        const children = opts.ssr ? /*#__PURE__*/ _jsx(Lazy, {
            ...props
        }) : /*#__PURE__*/ _jsx(BailoutToCSR, {
            reason: "next/dynamic",
            children: /*#__PURE__*/ _jsx(Lazy, {
                ...props
            })
        });
        return /*#__PURE__*/ _jsx(Suspense, {
            fallback: fallbackElement,
            children: children
        });
    }
    LoadableComponent.displayName = "LoadableComponent";
    return LoadableComponent;
}
export default Loadable;

//# sourceMappingURL=loadable.js.map