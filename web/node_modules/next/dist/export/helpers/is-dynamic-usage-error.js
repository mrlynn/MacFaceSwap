"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
Object.defineProperty(exports, "isDynamicUsageError", {
    enumerable: true,
    get: function() {
        return isDynamicUsageError;
    }
});
const _hooksservercontext = require("../../client/components/hooks-server-context");
const _notfound = require("../../client/components/not-found");
const _redirect = require("../../client/components/redirect");
const _bailouttocsr = require("../../shared/lib/lazy-dynamic/bailout-to-csr");
const isDynamicUsageError = (err)=>(0, _hooksservercontext.isDynamicServerError)(err) || (0, _bailouttocsr.isBailoutToCSRError)(err) || (0, _notfound.isNotFoundError)(err) || (0, _redirect.isRedirectError)(err);

//# sourceMappingURL=is-dynamic-usage-error.js.map