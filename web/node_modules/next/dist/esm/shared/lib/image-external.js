import { getImgProps } from "./get-img-props";
import { Image } from "../../client/image-component";
// @ts-ignore - This is replaced by webpack alias
import defaultLoader from "next/dist/shared/lib/image-loader";
export const getImageProps = (imgProps)=>{
    const { props } = getImgProps(imgProps, {
        defaultLoader,
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
export default Image;

//# sourceMappingURL=image-external.js.map