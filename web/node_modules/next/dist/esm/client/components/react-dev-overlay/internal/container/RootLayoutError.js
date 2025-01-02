import { _ as _tagged_template_literal_loose } from "@swc/helpers/_/_tagged_template_literal_loose";
function _templateObject() {
    const data = _tagged_template_literal_loose([
        "\n  .nextjs-container-root-layout-error-header > h4 {\n    line-height: 1.5;\n    margin: 0;\n    padding: 0;\n  }\n\n  .nextjs-container-root-layout-error-body footer {\n    margin-top: var(--size-gap);\n  }\n  .nextjs-container-root-layout-error-body footer p {\n    margin: 0;\n  }\n\n  .nextjs-container-root-layout-error-body small {\n    color: #757575;\n  }\n"
    ]);
    _templateObject = function() {
        return data;
    };
    return data;
}
import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import React from "react";
import { Dialog, DialogBody, DialogContent, DialogHeader } from "../components/Dialog";
import { Overlay } from "../components/Overlay";
import { Terminal } from "../components/Terminal";
import { noop as css } from "../helpers/noop-template";
export const RootLayoutError = function BuildError(param) {
    let { missingTags } = param;
    const message = "Please make sure to include the following tags in your root layout: <html>, <body>.\n\n" + ("Missing required root layout tag" + (missingTags.length === 1 ? "" : "s") + ": ") + missingTags.join(", ");
    const noop = React.useCallback(()=>{}, []);
    return /*#__PURE__*/ _jsx(Overlay, {
        fixed: true,
        children: /*#__PURE__*/ _jsx(Dialog, {
            type: "error",
            "aria-labelledby": "nextjs__container_root_layout_error_label",
            "aria-describedby": "nextjs__container_root_layout_error_desc",
            onClose: noop,
            children: /*#__PURE__*/ _jsxs(DialogContent, {
                children: [
                    /*#__PURE__*/ _jsx(DialogHeader, {
                        className: "nextjs-container-root-layout-error-header",
                        children: /*#__PURE__*/ _jsx("h4", {
                            id: "nextjs__container_root_layout_error_label",
                            children: "Missing required tags"
                        })
                    }),
                    /*#__PURE__*/ _jsxs(DialogBody, {
                        className: "nextjs-container-root-layout-error-body",
                        children: [
                            /*#__PURE__*/ _jsx(Terminal, {
                                content: message
                            }),
                            /*#__PURE__*/ _jsx("footer", {
                                children: /*#__PURE__*/ _jsx("p", {
                                    id: "nextjs__container_root_layout_error_desc",
                                    children: /*#__PURE__*/ _jsx("small", {
                                        children: "This error and can only be dismissed by providing all required tags."
                                    })
                                })
                            })
                        ]
                    })
                ]
            })
        })
    });
};
export const styles = css(_templateObject());

//# sourceMappingURL=RootLayoutError.js.map