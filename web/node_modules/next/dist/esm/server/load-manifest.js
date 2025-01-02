import { readFileSync } from "fs";
import { runInNewContext } from "vm";
const cache = new Map();
export function loadManifest(path, shouldCache = true) {
    const cached = shouldCache && cache.get(path);
    if (cached) {
        return cached;
    }
    const manifest = JSON.parse(readFileSync(path, "utf8"));
    if (shouldCache) {
        cache.set(path, manifest);
    }
    return manifest;
}
export function evalManifest(path, shouldCache = true) {
    const cached = shouldCache && cache.get(path);
    if (cached) {
        return cached;
    }
    const content = readFileSync(path, "utf8");
    if (content.length === 0) {
        throw new Error("Manifest file is empty");
    }
    const contextObject = {};
    runInNewContext(content, contextObject);
    if (shouldCache) {
        cache.set(path, contextObject);
    }
    return contextObject;
}
export function clearManifestCache(path) {
    return cache.delete(path);
}

//# sourceMappingURL=load-manifest.js.map