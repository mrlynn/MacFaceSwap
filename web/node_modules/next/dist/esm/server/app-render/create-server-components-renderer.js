/**
 * Create a component that renders the Flight stream.
 * This is only used for renderToHTML, the Flight response does not need additional wrappers.
 */ export function createReactServerRenderer(children, ComponentMod, clientReferenceManifest, onError, onPostpone) {
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