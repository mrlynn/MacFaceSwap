"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
Object.defineProperty(exports, "isDefaultRoute", {
    enumerable: true,
    get: function() {
        return isDefaultRoute;
    }
});
function isDefaultRoute(value) {
    return value == null ? void 0 : value.endsWith("/default");
}

//# sourceMappingURL=is-default-route.js.map