"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
Object.defineProperty(exports, "HotlinkedText", {
    enumerable: true,
    get: function() {
        return HotlinkedText;
    }
});
const _interop_require_default = require("@swc/helpers/_/_interop_require_default");
const _jsxruntime = require("react/jsx-runtime");
const _react = /*#__PURE__*/ _interop_require_default._(require("react"));
const _getwordsandwhitespaces = require("./get-words-and-whitespaces");
const linkRegex = /https?:\/\/[^\s/$.?#].[^\s"]*/i;
const HotlinkedText = function HotlinkedText(props) {
    const { text } = props;
    const wordsAndWhitespaces = (0, _getwordsandwhitespaces.getWordsAndWhitespaces)(text);
    return /*#__PURE__*/ (0, _jsxruntime.jsx)(_jsxruntime.Fragment, {
        children: linkRegex.test(text) ? wordsAndWhitespaces.map((word, index)=>{
            if (linkRegex.test(word)) {
                return /*#__PURE__*/ (0, _jsxruntime.jsx)(_react.default.Fragment, {
                    children: /*#__PURE__*/ (0, _jsxruntime.jsx)("a", {
                        href: word,
                        children: word
                    })
                }, "link-" + index);
            }
            return /*#__PURE__*/ (0, _jsxruntime.jsx)(_react.default.Fragment, {
                children: word
            }, "text-" + index);
        }) : text
    });
};

if ((typeof exports.default === 'function' || (typeof exports.default === 'object' && exports.default !== null)) && typeof exports.default.__esModule === 'undefined') {
  Object.defineProperty(exports.default, '__esModule', { value: true });
  Object.assign(exports.default, exports);
  module.exports = exports.default;
}

//# sourceMappingURL=index.js.map