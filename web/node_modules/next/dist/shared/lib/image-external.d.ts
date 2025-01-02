import type { ImageLoaderProps } from './image-config';
import type { ImageProps, ImageLoader, StaticImageData } from './get-img-props';
import { Image } from '../../client/image-component';
export declare const getImageProps: (imgProps: ImageProps) => {
    props: import("./get-img-props").ImgProps;
};
export default Image;
export type { ImageProps, ImageLoaderProps, ImageLoader, StaticImageData };
