import { jsx as _jsx, jsxs as _jsxs, Fragment as _Fragment } from "react/jsx-runtime";
import { CallStackFrame } from "./CallStackFrame";
import { FrameworkIcon } from "./FrameworkIcon";
function FrameworkGroup(param) {
    let { framework, stackFrames, all } = param;
    return /*#__PURE__*/ _jsx(_Fragment, {
        children: /*#__PURE__*/ _jsxs("details", {
            "data-nextjs-collapsed-call-stack-details": true,
            children: [
                /*#__PURE__*/ _jsxs("summary", {
                    tabIndex: 10,
                    children: [
                        /*#__PURE__*/ _jsx("svg", {
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
                            children: /*#__PURE__*/ _jsx("path", {
                                d: "M9 18l6-6-6-6"
                            })
                        }),
                        /*#__PURE__*/ _jsx(FrameworkIcon, {
                            framework: framework
                        }),
                        framework === "react" ? "React" : "Next.js"
                    ]
                }),
                stackFrames.map((frame, index)=>/*#__PURE__*/ _jsx(CallStackFrame, {
                        frame: frame
                    }, "call-stack-" + index + "-" + all))
            ]
        })
    });
}
export function GroupedStackFrames(param) {
    let { groupedStackFrames, all } = param;
    return /*#__PURE__*/ _jsx(_Fragment, {
        children: groupedStackFrames.map((stackFramesGroup, groupIndex)=>{
            // Collapse React and Next.js frames
            if (stackFramesGroup.framework) {
                return /*#__PURE__*/ _jsx(FrameworkGroup, {
                    framework: stackFramesGroup.framework,
                    stackFrames: stackFramesGroup.stackFrames,
                    all: all
                }, "call-stack-framework-group-" + groupIndex + "-" + all);
            }
            return(// Don't group non React and Next.js frames
            stackFramesGroup.stackFrames.map((frame, frameIndex)=>/*#__PURE__*/ _jsx(CallStackFrame, {
                    frame: frame
                }, "call-stack-" + groupIndex + "-" + frameIndex + "-" + all)));
        })
    });
}

//# sourceMappingURL=GroupedStackFrames.js.map