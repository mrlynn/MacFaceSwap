"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
0 && (module.exports = {
    getImageProps: null,
    default: null
});
function _export(target, all) {
    for(var name in all)Object.defineProperty(target, name, {
        enumerable: true,
        get: all[name]
    });
}
_export(exports, {
    getImageProps: function() {
        return getImageProps;
    },
    default: function() {
        return _default;
    }
});
const _interop_require_default = require("@swc/helpers/_/_interop_require_default");
const _getimgprops = require("./get-img-props");
const _imagecomponent = require("../../client/image-component");
const _imageloader = /*#__PURE__*/ _interop_require_default._(require("next/dist/shared/lib/image-loader"));
const getImageProps = (imgProps)=>{
    const { props } = (0, _getimgprops.getImgProps)(imgProps, {
        defaultLoader: _imageloader.default,
        // This is replaced by webpack define plugin
        imgConf: process.env.__NEXT_IMAGE_OPTS
    });
    // Normally we don't care about undefined props because we pass to JSX,
    // but this exported function could be used by the end user for anything
    // so we delete undefined props to clean it up a little.
    for (const [key, value] of Object.entries(props)){
        if (value === undefined) {
            delete props[key];
        }
    }
    return {
        props
    };
};
const _default = _imagecomponent.Image;

//# sourceMappingURL=image-external.js.map