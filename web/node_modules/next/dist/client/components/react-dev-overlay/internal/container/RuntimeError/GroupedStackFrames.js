"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
Object.defineProperty(exports, "GroupedStackFrames", {
    enumerable: true,
    get: function() {
        return GroupedStackFrames;
    }
});
const _jsxruntime = require("react/jsx-runtime");
const _CallStackFrame = require("./CallStackFrame");
const _FrameworkIcon = require("./FrameworkIcon");
function FrameworkGroup(param) {
    let { framework, stackFrames, all } = param;
    return /*#__PURE__*/ (0, _jsxruntime.jsx)(_jsxruntime.Fragment, {
        children: /*#__PURE__*/ (0, _jsxruntime.jsxs)("details", {
            "data-nextjs-collapsed-call-stack-details": true,
            children: [
                /*#__PURE__*/ (0, _jsxruntime.jsxs)("summary", {
                    tabIndex: 10,
                    children: [
                        /*#__PURE__*/ (0, _jsxruntime.jsx)("svg", {
                            "data-nextjs-call-stack-chevron-icon": true,
                            fill: "none",
                            height: "20",
                            width: "20",
                            shapeRendering: "geometricPrecision",
                            stroke: "currentColor",
                            strokeLinecap: "round",
                            strokeLinejoin: "round",
                            strokeWidth: "2",
                            viewBox: "0 0 24 24",
                            children: /*#__PURE__*/ (0, _jsxruntime.jsx)("path", {
                                d: "M9 18l6-6-6-6"
                            })
                        }),
                        /*#__PURE__*/ (0, _jsxruntime.jsx)(_FrameworkIcon.FrameworkIcon, {
                            framework: framework
                        }),
                        framework === "react" ? "React" : "Next.js"
                    ]
                }),
                stackFrames.map((frame, index)=>/*#__PURE__*/ (0, _jsxruntime.jsx)(_CallStackFrame.CallStackFrame, {
                        frame: frame
                    }, "call-stack-" + index + "-" + all))
            ]
        })
    });
}
function GroupedStackFrames(param) {
    let { groupedStackFrames, all } = param;
    return /*#__PURE__*/ (0, _jsxruntime.jsx)(_jsxruntime.Fragment, {
        children: groupedStackFrames.map((stackFramesGroup, groupIndex)=>{
            // Collapse React and Next.js frames
            if (stackFramesGroup.framework) {
                return /*#__PURE__*/ (0, _jsxruntime.jsx)(FrameworkGroup, {
                    framework: stackFramesGroup.framework,
                    stackFrames: stackFramesGroup.stackFrames,
                    all: all
                }, "call-stack-framework-group-" + groupIndex + "-" + all);
            }
            return(// Don't group non React and Next.js frames
            stackFramesGroup.stackFrames.map((frame, frameIndex)=>/*#__PURE__*/ (0, _jsxruntime.jsx)(_CallStackFrame.CallStackFrame, {
                    frame: frame
                }, "call-stack-" + groupIndex + "-" + frameIndex + "-" + all)));
        })
    });
}

if ((typeof exports.default === 'function' || (typeof exports.default === 'object' && exports.default !== null)) && typeof exports.default.__esModule === 'undefined') {
  Object.defineProperty(exports.default, '__esModule', { value: true });
  Object.assign(exports.default, exports);
  module.exports = exports.default;
}

//# sourceMappingURL=GroupedStackFrames.js.map