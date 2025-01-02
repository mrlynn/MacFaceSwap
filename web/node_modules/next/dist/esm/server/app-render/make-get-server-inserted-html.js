import { jsx as _jsx, jsxs as _jsxs, Fragment as _Fragment } from "react/jsx-runtime";
import React from "react";
import { isNotFoundError } from "../../client/components/not-found";
import { getURLFromRedirectError, isRedirectError, getRedirectStatusCodeFromError } from "../../client/components/redirect";
import { renderToReadableStream } from "react-dom/server.edge";
import { streamToString } from "../stream-utils/node-web-streams-helper";
import { RedirectStatusCode } from "../../client/components/redirect-status-code";
export function makeGetServerInsertedHTML({ polyfills, renderServerInsertedHTML, hasPostponed }) {
    let flushedErrorMetaTagsUntilIndex = 0;
    // If the render had postponed, then we have already flushed the polyfills.
    let polyfillsFlushed = hasPostponed;
    return async function getServerInsertedHTML(serverCapturedErrors) {
        // Loop through all the errors that have been captured but not yet
        // flushed.
        const errorMetaTags = [];
        while(flushedErrorMetaTagsUntilIndex < serverCapturedErrors.length){
            const error = serverCapturedErrors[flushedErrorMetaTagsUntilIndex];
            flushedErrorMetaTagsUntilIndex++;
            if (isNotFoundError(error)) {
                errorMetaTags.push(/*#__PURE__*/ _jsx("meta", {
                    name: "robots",
                    content: "noindex"
                }, error.digest), process.env.NODE_ENV === "development" ? /*#__PURE__*/ _jsx("meta", {
                    name: "next-error",
                    content: "not-found"
                }, "next-error") : null);
            } else if (isRedirectError(error)) {
                const redirectUrl = getURLFromRedirectError(error);
                const statusCode = getRedirectStatusCodeFromError(error);
                const isPermanent = statusCode === RedirectStatusCode.PermanentRedirect ? true : false;
                if (redirectUrl) {
                    errorMetaTags.push(/*#__PURE__*/ _jsx("meta", {
                        httpEquiv: "refresh",
                        content: `${isPermanent ? 0 : 1};url=${redirectUrl}`
                    }, error.digest));
                }
            }
        }
        const stream = await renderToReadableStream(/*#__PURE__*/ _jsxs(_Fragment, {
            children: [
                !polyfillsFlushed && (polyfills == null ? void 0 : polyfills.map((polyfill)=>{
                    return /*#__PURE__*/ _jsx("script", {
                        ...polyfill
                    }, polyfill.src);
                })),
                renderServerInsertedHTML(),
                errorMetaTags
            ]
        }));
        // Mark polyfills as flushed so they don't get flushed again.
        if (!polyfillsFlushed) polyfillsFlushed = true;
        // Wait for the stream to be ready.
        await stream.allReady;
        return streamToString(stream);
    };
}

//# sourceMappingURL=make-get-server-inserted-html.js.map