"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
0 && (module.exports = {
    isGroupSegment: null,
    PAGE_SEGMENT_KEY: null,
    DEFAULT_SEGMENT_KEY: null
});
function _export(target, all) {
    for(var name in all)Object.defineProperty(target, name, {
        enumerable: true,
        get: all[name]
    });
}
_export(exports, {
    isGroupSegment: function() {
        return isGroupSegment;
    },
    PAGE_SEGMENT_KEY: function() {
        return PAGE_SEGMENT_KEY;
    },
    DEFAULT_SEGMENT_KEY: function() {
        return DEFAULT_SEGMENT_KEY;
    }
});
function isGroupSegment(segment) {
    // Use array[0] for performant purpose
    return segment[0] === "(" && segment.endsWith(")");
}
const PAGE_SEGMENT_KEY = "__PAGE__";
const DEFAULT_SEGMENT_KEY = "__DEFAULT__";

//# sourceMappingURL=segment.js.map