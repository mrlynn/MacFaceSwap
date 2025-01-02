import { jsx as _jsx, jsxs as _jsxs, Fragment as _Fragment } from "react/jsx-runtime";
import * as React from "react";
import { ACTION_UNHANDLED_ERROR } from "./error-overlay-reducer";
import { ShadowPortal } from "./components/ShadowPortal";
import { BuildError } from "./container/BuildError";
import { Errors } from "./container/Errors";
import { RootLayoutError } from "./container/RootLayoutError";
import { parseStack } from "./helpers/parseStack";
import { Base } from "./styles/Base";
import { ComponentStyles } from "./styles/ComponentStyles";
import { CssReset } from "./styles/CssReset";
class ReactDevOverlay extends React.PureComponent {
    static getDerivedStateFromError(error) {
        const e = error;
        const event = {
            type: ACTION_UNHANDLED_ERROR,
            reason: error,
            frames: parseStack(e.stack)
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
        return /*#__PURE__*/ _jsxs(_Fragment, {
            children: [
                reactError ? /*#__PURE__*/ _jsxs("html", {
                    children: [
                        /*#__PURE__*/ _jsx("head", {}),
                        /*#__PURE__*/ _jsx("body", {})
                    ]
                }) : children,
                isMounted ? /*#__PURE__*/ _jsxs(ShadowPortal, {
                    children: [
                        /*#__PURE__*/ _jsx(CssReset, {}),
                        /*#__PURE__*/ _jsx(Base, {}),
                        /*#__PURE__*/ _jsx(ComponentStyles, {}),
                        rootLayoutMissingTagsError ? /*#__PURE__*/ _jsx(RootLayoutError, {
                            missingTags: rootLayoutMissingTagsError.missingTags
                        }) : hasBuildError ? /*#__PURE__*/ _jsx(BuildError, {
                            message: state.buildError,
                            versionInfo: state.versionInfo
                        }) : reactError ? /*#__PURE__*/ _jsx(Errors, {
                            versionInfo: state.versionInfo,
                            initialDisplayState: "fullscreen",
                            errors: [
                                reactError
                            ]
                        }) : hasRuntimeErrors ? /*#__PURE__*/ _jsx(Errors, {
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
export default ReactDevOverlay;

//# sourceMappingURL=ReactDevOverlay.js.map