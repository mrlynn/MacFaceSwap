"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
Object.defineProperty(exports, "createReactServerRenderer", {
    enumerable: true,
    get: function() {
        return createReactServerRenderer;
    }
});
function createReactServerRenderer(children, ComponentMod, clientReferenceManifest, onError, onPostpone) {
    let flightStream;
    return function renderToReactServerStream() {
        if (flightStream) {
            return flightStream;
        } else {
            flightStream = ComponentMod.renderToReadableStream(children, clientReferenceManifest.clientModules, {
                onError,
                onPostpone
            });
            return flightStream;
        }
    };
}

//# sourceMappingURL=create-server-components-renderer.js.map