"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
Object.defineProperty(exports, "default", {
    enumerable: true,
    get: function() {
        return _default;
    }
});
const _interop_require_wildcard = require("@swc/helpers/_/_interop_require_wildcard");
const _jsxruntime = require("react/jsx-runtime");
const _react = /*#__PURE__*/ _interop_require_wildcard._(require("react"));
const _erroroverlayreducer = require("./error-overlay-reducer");
const _ShadowPortal = require("./components/ShadowPortal");
const _BuildError = require("./container/BuildError");
const _Errors = require("./container/Errors");
const _RootLayoutError = require("./container/RootLayoutError");
const _parseStack = require("./helpers/parseStack");
const _Base = require("./styles/Base");
const _ComponentStyles = require("./styles/ComponentStyles");
const _CssReset = require("./styles/CssReset");
class ReactDevOverlay extends _react.PureComponent {
    static getDerivedStateFromError(error) {
        const e = error;
        const event = {
            type: _erroroverlayreducer.ACTION_UNHANDLED_ERROR,
            reason: error,
            frames: (0, _parseStack.parseStack)(e.stack)
        };
        const errorEvent = {
            id: 0,
            event
        };
        return {
            reactError: errorEvent
        };
    }
    componentDidCatch(componentErr) {
        this.props.onReactError(componentErr);
    }
    render() {
        const { state, children } = this.props;
        const { reactError } = this.state;
        const hasBuildError = state.buildError != null;
        const hasRuntimeErrors = Boolean(state.errors.length);
        const rootLayoutMissingTagsError = state.rootLayoutMissingTagsError;
        const isMounted = hasBuildError || hasRuntimeErrors || reactError || rootLayoutMissingTagsError;
        return /*#__PURE__*/ (0, _jsxruntime.jsxs)(_jsxruntime.Fragment, {
            children: [
                reactError ? /*#__PURE__*/ (0, _jsxruntime.jsxs)("html", {
                    children: [
                        /*#__PURE__*/ (0, _jsxruntime.jsx)("head", {}),
                        /*#__PURE__*/ (0, _jsxruntime.jsx)("body", {})
                    ]
                }) : children,
                isMounted ? /*#__PURE__*/ (0, _jsxruntime.jsxs)(_ShadowPortal.ShadowPortal, {
                    children: [
                        /*#__PURE__*/ (0, _jsxruntime.jsx)(_CssReset.CssReset, {}),
                        /*#__PURE__*/ (0, _jsxruntime.jsx)(_Base.Base, {}),
                        /*#__PURE__*/ (0, _jsxruntime.jsx)(_ComponentStyles.ComponentStyles, {}),
                        rootLayoutMissingTagsError ? /*#__PURE__*/ (0, _jsxruntime.jsx)(_RootLayoutError.RootLayoutError, {
                            missingTags: rootLayoutMissingTagsError.missingTags
                        }) : hasBuildError ? /*#__PURE__*/ (0, _jsxruntime.jsx)(_BuildError.BuildError, {
                            message: state.buildError,
                            versionInfo: state.versionInfo
                        }) : reactError ? /*#__PURE__*/ (0, _jsxruntime.jsx)(_Errors.Errors, {
                            versionInfo: state.versionInfo,
                            initialDisplayState: "fullscreen",
                            errors: [
                                reactError
                            ]
                        }) : hasRuntimeErrors ? /*#__PURE__*/ (0, _jsxruntime.jsx)(_Errors.Errors, {
                            initialDisplayState: "minimized",
                            errors: state.errors,
                            versionInfo: state.versionInfo
                        }) : undefined
                    ]
                }) : undefined
            ]
        });
    }
    constructor(...args){
        super(...args);
        this.state = {
            reactError: null
        };
    }
}
const _default = ReactDevOverlay;

if ((typeof exports.default === 'function' || (typeof exports.default === 'object' && exports.default !== null)) && typeof exports.default.__esModule === 'undefined') {
  Object.defineProperty(exports.default, '__esModule', { value: true });
  Object.assign(exports.default, exports);
  module.exports = exports.default;
}

//# sourceMappingURL=ReactDevOverlay.js.map