(function(){"use strict";var e={3540:function(e){
/*
object-assign
(c) Sindre Sorhus
@license MIT
*/
var t=Object.getOwnPropertySymbols;var r=Object.prototype.hasOwnProperty;var n=Object.prototype.propertyIsEnumerable;function toObject(e){if(e===null||e===undefined){throw new TypeError("Object.assign cannot be called with null or undefined")}return Object(e)}function shouldUseNative(){try{if(!Object.assign){return false}var e=new String("abc");e[5]="de";if(Object.getOwnPropertyNames(e)[0]==="5"){return false}var t={};for(var r=0;r<10;r++){t["_"+String.fromCharCode(r)]=r}var n=Object.getOwnPropertyNames(t).map((function(e){return t[e]}));if(n.join("")!=="0123456789"){return false}var o={};"abcdefghijklmnopqrst".split("").forEach((function(e){o[e]=e}));if(Object.keys(Object.assign({},o)).join("")!=="abcdefghijklmnopqrst"){return false}return true}catch(e){return false}}e.exports=shouldUseNative()?Object.assign:function(e,o){var a;var i=toObject(e);var s;for(var l=1;l<arguments.length;l++){a=Object(arguments[l]);for(var u in a){if(r.call(a,u)){i[u]=a[u]}}if(t){s=t(a);for(var c=0;c<s.length;c++){if(n.call(a,s[c])){i[s[c]]=a[s[c]]}}}}return i}},3037:function(e,t,r){
/** @license React v17.0.2
 * react-jsx-runtime.development.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
if(process.env.NODE_ENV!=="production"){(function(){"use strict";var e=r(7522);var n=r(3540);var o=60103;var a=60106;t.Fragment=60107;var i=60108;var s=60114;var l=60109;var u=60110;var c=60112;var d=60113;var f=60120;var p=60115;var m=60116;var v=60121;var b=60122;var g=60117;var h=60119;var y=60128;var x=60129;var _=60130;var w=60131;if(typeof Symbol==="function"&&Symbol.for){var E=Symbol.for;o=E("react.element");a=E("react.portal");t.Fragment=E("react.fragment");i=E("react.strict_mode");s=E("react.profiler");l=E("react.provider");u=E("react.context");c=E("react.forward_ref");d=E("react.suspense");f=E("react.suspense_list");p=E("react.memo");m=E("react.lazy");v=E("react.block");b=E("react.server.block");g=E("react.fundamental");h=E("react.scope");y=E("react.opaque.id");x=E("react.debug_trace_mode");_=E("react.offscreen");w=E("react.legacy_hidden")}var j=typeof Symbol==="function"&&Symbol.iterator;var O="@@iterator";function getIteratorFn(e){if(e===null||typeof e!=="object"){return null}var t=j&&e[j]||e[O];if(typeof t==="function"){return t}return null}var k=e.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED;function error(e){{for(var t=arguments.length,r=new Array(t>1?t-1:0),n=1;n<t;n++){r[n-1]=arguments[n]}printWarning("error",e,r)}}function printWarning(e,t,r){{var n=k.ReactDebugCurrentFrame;var o=n.getStackAddendum();if(o!==""){t+="%s";r=r.concat([o])}var a=r.map((function(e){return""+e}));a.unshift("Warning: "+t);Function.prototype.apply.call(console[e],console,a)}}var S=false;function isValidElementType(e){if(typeof e==="string"||typeof e==="function"){return true}if(e===t.Fragment||e===s||e===x||e===i||e===d||e===f||e===w||S){return true}if(typeof e==="object"&&e!==null){if(e.$$typeof===m||e.$$typeof===p||e.$$typeof===l||e.$$typeof===u||e.$$typeof===c||e.$$typeof===g||e.$$typeof===v||e[0]===b){return true}}return false}function getWrappedName(e,t,r){var n=t.displayName||t.name||"";return e.displayName||(n!==""?r+"("+n+")":r)}function getContextName(e){return e.displayName||"Context"}function getComponentName(e){if(e==null){return null}{if(typeof e.tag==="number"){error("Received an unexpected object in getComponentName(). "+"This is likely a bug in React. Please file an issue.")}}if(typeof e==="function"){return e.displayName||e.name||null}if(typeof e==="string"){return e}switch(e){case t.Fragment:return"Fragment";case a:return"Portal";case s:return"Profiler";case i:return"StrictMode";case d:return"Suspense";case f:return"SuspenseList"}if(typeof e==="object"){switch(e.$$typeof){case u:var r=e;return getContextName(r)+".Consumer";case l:var n=e;return getContextName(n._context)+".Provider";case c:return getWrappedName(e,e.render,"ForwardRef");case p:return getComponentName(e.type);case v:return getComponentName(e._render);case m:{var o=e;var b=o._payload;var g=o._init;try{return getComponentName(g(b))}catch(e){return null}}}}return null}var C=0;var T;var D;var P;var N;var R;var F;var I;function disabledLog(){}disabledLog.__reactDisabledLog=true;function disableLogs(){{if(C===0){T=console.log;D=console.info;P=console.warn;N=console.error;R=console.group;F=console.groupCollapsed;I=console.groupEnd;var e={configurable:true,enumerable:true,value:disabledLog,writable:true};Object.defineProperties(console,{info:e,log:e,warn:e,error:e,group:e,groupCollapsed:e,groupEnd:e})}C++}}function reenableLogs(){{C--;if(C===0){var e={configurable:true,enumerable:true,writable:true};Object.defineProperties(console,{log:n({},e,{value:T}),info:n({},e,{value:D}),warn:n({},e,{value:P}),error:n({},e,{value:N}),group:n({},e,{value:R}),groupCollapsed:n({},e,{value:F}),groupEnd:n({},e,{value:I})})}if(C<0){error("disabledDepth fell below zero. "+"This is a bug in React. Please file an issue.")}}}var A=k.ReactCurrentDispatcher;var M;function describeBuiltInComponentFrame(e,t,r){{if(M===undefined){try{throw Error()}catch(e){var n=e.stack.trim().match(/\n( *(at )?)/);M=n&&n[1]||""}}return"\n"+M+e}}var L=false;var B;{var H=typeof WeakMap==="function"?WeakMap:Map;B=new H}function describeNativeComponentFrame(e,t){if(!e||L){return""}{var r=B.get(e);if(r!==undefined){return r}}var n;L=true;var o=Error.prepareStackTrace;Error.prepareStackTrace=undefined;var a;{a=A.current;A.current=null;disableLogs()}try{if(t){var Fake=function(){throw Error()};Object.defineProperty(Fake.prototype,"props",{set:function(){throw Error()}});if(typeof Reflect==="object"&&Reflect.construct){try{Reflect.construct(Fake,[])}catch(e){n=e}Reflect.construct(e,[],Fake)}else{try{Fake.call()}catch(e){n=e}e.call(Fake.prototype)}}else{try{throw Error()}catch(e){n=e}e()}}catch(t){if(t&&n&&typeof t.stack==="string"){var i=t.stack.split("\n");var s=n.stack.split("\n");var l=i.length-1;var u=s.length-1;while(l>=1&&u>=0&&i[l]!==s[u]){u--}for(;l>=1&&u>=0;l--,u--){if(i[l]!==s[u]){if(l!==1||u!==1){do{l--;u--;if(u<0||i[l]!==s[u]){var c="\n"+i[l].replace(" at new "," at ");{if(typeof e==="function"){B.set(e,c)}}return c}}while(l>=1&&u>=0)}break}}}}finally{L=false;{A.current=a;reenableLogs()}Error.prepareStackTrace=o}var d=e?e.displayName||e.name:"";var f=d?describeBuiltInComponentFrame(d):"";{if(typeof e==="function"){B.set(e,f)}}return f}function describeFunctionComponentFrame(e,t,r){{return describeNativeComponentFrame(e,false)}}function shouldConstruct(e){var t=e.prototype;return!!(t&&t.isReactComponent)}function describeUnknownElementTypeFrameInDEV(e,t,r){if(e==null){return""}if(typeof e==="function"){{return describeNativeComponentFrame(e,shouldConstruct(e))}}if(typeof e==="string"){return describeBuiltInComponentFrame(e)}switch(e){case d:return describeBuiltInComponentFrame("Suspense");case f:return describeBuiltInComponentFrame("SuspenseList")}if(typeof e==="object"){switch(e.$$typeof){case c:return describeFunctionComponentFrame(e.render);case p:return describeUnknownElementTypeFrameInDEV(e.type,t,r);case v:return describeFunctionComponentFrame(e._render);case m:{var n=e;var o=n._payload;var a=n._init;try{return describeUnknownElementTypeFrameInDEV(a(o),t,r)}catch(e){}}}}return""}var z={};var W=k.ReactDebugCurrentFrame;function setCurrentlyValidatingElement(e){{if(e){var t=e._owner;var r=describeUnknownElementTypeFrameInDEV(e.type,e._source,t?t.type:null);W.setExtraStackFrame(r)}else{W.setExtraStackFrame(null)}}}function checkPropTypes(e,t,r,n,o){{var a=Function.call.bind(Object.prototype.hasOwnProperty);for(var i in e){if(a(e,i)){var s=void 0;try{if(typeof e[i]!=="function"){var l=Error((n||"React class")+": "+r+" type `"+i+"` is invalid; "+"it must be a function, usually from the `prop-types` package, but received `"+typeof e[i]+"`."+"This often happens because of typos such as `PropTypes.function` instead of `PropTypes.func`.");l.name="Invariant Violation";throw l}s=e[i](t,i,n,r,null,"SECRET_DO_NOT_PASS_THIS_OR_YOU_WILL_BE_FIRED")}catch(e){s=e}if(s&&!(s instanceof Error)){setCurrentlyValidatingElement(o);error("%s: type specification of %s"+" `%s` is invalid; the type checker "+"function must return `null` or an `Error` but returned a %s. "+"You may have forgotten to pass an argument to the type checker "+"creator (arrayOf, instanceOf, objectOf, oneOf, oneOfType, and "+"shape all require an argument).",n||"React class",r,i,typeof s);setCurrentlyValidatingElement(null)}if(s instanceof Error&&!(s.message in z)){z[s.message]=true;setCurrentlyValidatingElement(o);error("Failed %s type: %s",r,s.message);setCurrentlyValidatingElement(null)}}}}}var V=k.ReactCurrentOwner;var $=Object.prototype.hasOwnProperty;var U={key:true,ref:true,__self:true,__source:true};var K;var G;var Z;{Z={}}function hasValidRef(e){{if($.call(e,"ref")){var t=Object.getOwnPropertyDescriptor(e,"ref").get;if(t&&t.isReactWarning){return false}}}return e.ref!==undefined}function hasValidKey(e){{if($.call(e,"key")){var t=Object.getOwnPropertyDescriptor(e,"key").get;if(t&&t.isReactWarning){return false}}}return e.key!==undefined}function warnIfStringRefCannotBeAutoConverted(e,t){{if(typeof e.ref==="string"&&V.current&&t&&V.current.stateNode!==t){var r=getComponentName(V.current.type);if(!Z[r]){error('Component "%s" contains the string ref "%s". '+"Support for string refs will be removed in a future major release. "+"This case cannot be automatically converted to an arrow function. "+"We ask you to manually fix this case by using useRef() or createRef() instead. "+"Learn more about using refs safely here: "+"https://reactjs.org/link/strict-mode-string-ref",getComponentName(V.current.type),e.ref);Z[r]=true}}}}function defineKeyPropWarningGetter(e,t){{var warnAboutAccessingKey=function(){if(!K){K=true;error("%s: `key` is not a prop. Trying to access it will result "+"in `undefined` being returned. If you need to access the same "+"value within the child component, you should pass it as a different "+"prop. (https://reactjs.org/link/special-props)",t)}};warnAboutAccessingKey.isReactWarning=true;Object.defineProperty(e,"key",{get:warnAboutAccessingKey,configurable:true})}}function defineRefPropWarningGetter(e,t){{var warnAboutAccessingRef=function(){if(!G){G=true;error("%s: `ref` is not a prop. Trying to access it will result "+"in `undefined` being returned. If you need to access the same "+"value within the child component, you should pass it as a different "+"prop. (https://reactjs.org/link/special-props)",t)}};warnAboutAccessingRef.isReactWarning=true;Object.defineProperty(e,"ref",{get:warnAboutAccessingRef,configurable:true})}}var ReactElement=function(e,t,r,n,a,i,s){var l={$$typeof:o,type:e,key:t,ref:r,props:s,_owner:i};{l._store={};Object.defineProperty(l._store,"validated",{configurable:false,enumerable:false,writable:true,value:false});Object.defineProperty(l,"_self",{configurable:false,enumerable:false,writable:false,value:n});Object.defineProperty(l,"_source",{configurable:false,enumerable:false,writable:false,value:a});if(Object.freeze){Object.freeze(l.props);Object.freeze(l)}}return l};function jsxDEV(e,t,r,n,o){{var a;var i={};var s=null;var l=null;if(r!==undefined){s=""+r}if(hasValidKey(t)){s=""+t.key}if(hasValidRef(t)){l=t.ref;warnIfStringRefCannotBeAutoConverted(t,o)}for(a in t){if($.call(t,a)&&!U.hasOwnProperty(a)){i[a]=t[a]}}if(e&&e.defaultProps){var u=e.defaultProps;for(a in u){if(i[a]===undefined){i[a]=u[a]}}}if(s||l){var c=typeof e==="function"?e.displayName||e.name||"Unknown":e;if(s){defineKeyPropWarningGetter(i,c)}if(l){defineRefPropWarningGetter(i,c)}}return ReactElement(e,s,l,o,n,V.current,i)}}var Y=k.ReactCurrentOwner;var J=k.ReactDebugCurrentFrame;function setCurrentlyValidatingElement$1(e){{if(e){var t=e._owner;var r=describeUnknownElementTypeFrameInDEV(e.type,e._source,t?t.type:null);J.setExtraStackFrame(r)}else{J.setExtraStackFrame(null)}}}var X;{X=false}function isValidElement(e){{return typeof e==="object"&&e!==null&&e.$$typeof===o}}function getDeclarationErrorAddendum(){{if(Y.current){var e=getComponentName(Y.current.type);if(e){return"\n\nCheck the render method of `"+e+"`."}}return""}}function getSourceInfoErrorAddendum(e){{if(e!==undefined){var t=e.fileName.replace(/^.*[\\\/]/,"");var r=e.lineNumber;return"\n\nCheck your code at "+t+":"+r+"."}return""}}var Q={};function getCurrentComponentErrorInfo(e){{var t=getDeclarationErrorAddendum();if(!t){var r=typeof e==="string"?e:e.displayName||e.name;if(r){t="\n\nCheck the top-level render call using <"+r+">."}}return t}}function validateExplicitKey(e,t){{if(!e._store||e._store.validated||e.key!=null){return}e._store.validated=true;var r=getCurrentComponentErrorInfo(t);if(Q[r]){return}Q[r]=true;var n="";if(e&&e._owner&&e._owner!==Y.current){n=" It was passed a child from "+getComponentName(e._owner.type)+"."}setCurrentlyValidatingElement$1(e);error('Each child in a list should have a unique "key" prop.'+"%s%s See https://reactjs.org/link/warning-keys for more information.",r,n);setCurrentlyValidatingElement$1(null)}}function validateChildKeys(e,t){{if(typeof e!=="object"){return}if(Array.isArray(e)){for(var r=0;r<e.length;r++){var n=e[r];if(isValidElement(n)){validateExplicitKey(n,t)}}}else if(isValidElement(e)){if(e._store){e._store.validated=true}}else if(e){var o=getIteratorFn(e);if(typeof o==="function"){if(o!==e.entries){var a=o.call(e);var i;while(!(i=a.next()).done){if(isValidElement(i.value)){validateExplicitKey(i.value,t)}}}}}}}function validatePropTypes(e){{var t=e.type;if(t===null||t===undefined||typeof t==="string"){return}var r;if(typeof t==="function"){r=t.propTypes}else if(typeof t==="object"&&(t.$$typeof===c||t.$$typeof===p)){r=t.propTypes}else{return}if(r){var n=getComponentName(t);checkPropTypes(r,e.props,"prop",n,e)}else if(t.PropTypes!==undefined&&!X){X=true;var o=getComponentName(t);error("Component %s declared `PropTypes` instead of `propTypes`. Did you misspell the property assignment?",o||"Unknown")}if(typeof t.getDefaultProps==="function"&&!t.getDefaultProps.isReactClassApproved){error("getDefaultProps is only used on classic React.createClass "+"definitions. Use a static property named `defaultProps` instead.")}}}function validateFragmentProps(e){{var t=Object.keys(e.props);for(var r=0;r<t.length;r++){var n=t[r];if(n!=="children"&&n!=="key"){setCurrentlyValidatingElement$1(e);error("Invalid prop `%s` supplied to `React.Fragment`. "+"React.Fragment can only have `key` and `children` props.",n);setCurrentlyValidatingElement$1(null);break}}if(e.ref!==null){setCurrentlyValidatingElement$1(e);error("Invalid attribute `ref` supplied to `React.Fragment`.");setCurrentlyValidatingElement$1(null)}}}function jsxWithValidation(e,r,n,a,i,s){{var l=isValidElementType(e);if(!l){var u="";if(e===undefined||typeof e==="object"&&e!==null&&Object.keys(e).length===0){u+=" You likely forgot to export your component from the file "+"it's defined in, or you might have mixed up default and named imports."}var c=getSourceInfoErrorAddendum(i);if(c){u+=c}else{u+=getDeclarationErrorAddendum()}var d;if(e===null){d="null"}else if(Array.isArray(e)){d="array"}else if(e!==undefined&&e.$$typeof===o){d="<"+(getComponentName(e.type)||"Unknown")+" />";u=" Did you accidentally export a JSX literal instead of a component?"}else{d=typeof e}error("React.jsx: type is invalid -- expected a string (for "+"built-in components) or a class/function (for composite "+"components) but got: %s.%s",d,u)}var f=jsxDEV(e,r,n,i,s);if(f==null){return f}if(l){var p=r.children;if(p!==undefined){if(a){if(Array.isArray(p)){for(var m=0;m<p.length;m++){validateChildKeys(p[m],e)}if(Object.freeze){Object.freeze(p)}}else{error("React.jsx: Static children should always be an array. "+"You are likely explicitly calling React.jsxs or React.jsxDEV. "+"Use the Babel transform instead.")}}else{validateChildKeys(p,e)}}}if(e===t.Fragment){validateFragmentProps(f)}else{validatePropTypes(f)}return f}}function jsxWithValidationStatic(e,t,r){{return jsxWithValidation(e,t,r,true)}}function jsxWithValidationDynamic(e,t,r){{return jsxWithValidation(e,t,r,false)}}var ee=jsxWithValidationDynamic;var te=jsxWithValidationStatic;t.jsx=ee;t.jsxs=te})()}},1080:function(e,t,r){
/** @license React v17.0.2
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
r(3540);var n=r(7522),o=60103;t.Fragment=60107;if("function"===typeof Symbol&&Symbol.for){var a=Symbol.for;o=a("react.element");t.Fragment=a("react.fragment")}var i=n.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner,s=Object.prototype.hasOwnProperty,l={key:!0,ref:!0,__self:!0,__source:!0};function q(e,t,r){var n,a={},u=null,c=null;void 0!==r&&(u=""+r);void 0!==t.key&&(u=""+t.key);void 0!==t.ref&&(c=t.ref);for(n in t)s.call(t,n)&&!l.hasOwnProperty(n)&&(a[n]=t[n]);if(e&&e.defaultProps)for(n in t=e.defaultProps,t)void 0===a[n]&&(a[n]=t[n]);return{$$typeof:o,type:e,key:u,ref:c,props:a,_owner:i.current}}t.jsx=q;t.jsxs=q},505:function(e,t,r){if(process.env.NODE_ENV==="production"){e.exports=r(1080)}else{e.exports=r(3037)}},3876:function(e,t){Object.defineProperty(t,"__esModule",{value:true});0&&0;function _export(e,t){for(var r in t)Object.defineProperty(e,r,{enumerable:true,get:t[r]})}_export(t,{hydrationErrorWarning:function(){return r},hydrationErrorComponentStack:function(){return n},patchConsoleError:function(){return patchConsoleError}});let r;let n;const o=new Set(['Warning: Text content did not match. Server: "%s" Client: "%s"%s',"Warning: Expected server HTML to contain a matching <%s> in <%s>.%s",'Warning: Expected server HTML to contain a matching text node for "%s" in <%s>.%s',"Warning: Did not expect server HTML to contain a <%s> in <%s>.%s",'Warning: Did not expect server HTML to contain the text node "%s" in <%s>.%s']);function patchConsoleError(){const e=console.error;console.error=function(t,a,i,s){if(o.has(t)){r=t.replace("%s",a).replace("%s",i).replace("%s","");n=s}e.apply(console,arguments)}}if((typeof t.default==="function"||typeof t.default==="object"&&t.default!==null)&&typeof t.default.__esModule==="undefined"){Object.defineProperty(t.default,"__esModule",{value:true});Object.assign(t.default,t);e.exports=t.default}},4659:function(e,t){Object.defineProperty(t,"__esModule",{value:true});Object.defineProperty(t,"parseComponentStack",{enumerable:true,get:function(){return parseComponentStack}});var r;(function(e){e["FILE"]="file";e["WEBPACK_INTERNAL"]="webpack-internal";e["HTTP"]="http";e["PROTOCOL_RELATIVE"]="protocol-relative";e["UNKNOWN"]="unknown"})(r||(r={}));function getLocationType(e){if(e.startsWith("file://")){return"file"}if(e.startsWith("webpack-internal://")){return"webpack-internal"}if(e.startsWith("http://")||e.startsWith("https://")){return"http"}if(e.startsWith("//")){return"protocol-relative"}return"unknown"}function parseStackFrameLocation(e){const t=getLocationType(e);const r=e==null?void 0:e.replace(/^(webpack-internal:\/\/\/|file:\/\/)(\(.*\)\/)?/,"");var n;const[,o,a,i]=(n=r==null?void 0:r.match(/^(.+):(\d+):(\d+)/))!=null?n:[];switch(t){case"file":case"webpack-internal":return{canOpenInEditor:true,file:o,lineNumber:a?Number(a):undefined,column:i?Number(i):undefined};case"http":case"protocol-relative":case"unknown":default:{return{canOpenInEditor:false}}}}function parseComponentStack(e){const t=[];for(const r of e.trim().split("\n")){const e=/at ([^ ]+)( \((.*)\))?/.exec(r);if(e==null?void 0:e[1]){const r=e[1];const n=e[3];if(!n){t.push({canOpenInEditor:false,component:r});continue}if(n==null?void 0:n.includes("next/dist")){break}const o=parseStackFrameLocation(n);t.push({component:r,...o})}}return t}if((typeof t.default==="function"||typeof t.default==="object"&&t.default!==null)&&typeof t.default.__esModule==="undefined"){Object.defineProperty(t.default,"__esModule",{value:true});Object.assign(t.default,t);e.exports=t.default}},5204:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};var i=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:true});t.onRefresh=t.onBeforeRefresh=t.unregister=t.register=t.onBuildError=t.onBuildOk=t.ReactDevOverlay=t.getServerError=t.getErrorByType=void 0;const s=a(r(5851));const l=r(636);const u=r(4659);const c=r(3876);(0,c.patchConsoleError)();let d=false;let f=undefined;function onUnhandledError(e){const t=e?.error;if(!t||!(t instanceof Error)||typeof t.stack!=="string"){return}if(t.message.match(/(hydration|content does not match|did not match)/i)){if(c.hydrationErrorWarning){t.message+="\n\n"+c.hydrationErrorWarning}t.message+=`\n\nSee more info here: https://nextjs.org/docs/messages/react-hydration-error`}const r=t;const n=typeof c.hydrationErrorComponentStack==="string"?(0,u.parseComponentStack)(c.hydrationErrorComponentStack).map((e=>e.component)):undefined;s.emit({type:s.TYPE_UNHANDLED_ERROR,reason:t,frames:(0,l.parseStack)(r.stack),componentStack:n})}function onUnhandledRejection(e){const t=e?.reason;if(!t||!(t instanceof Error)||typeof t.stack!=="string"){return}const r=t;s.emit({type:s.TYPE_UNHANDLED_REJECTION,reason:t,frames:(0,l.parseStack)(r.stack)})}function register(){if(d){return}d=true;try{const e=Error.stackTraceLimit;Error.stackTraceLimit=50;f=e}catch{}window.addEventListener("error",onUnhandledError);window.addEventListener("unhandledrejection",onUnhandledRejection)}t.register=register;function unregister(){if(!d){return}d=false;if(f!==undefined){try{Error.stackTraceLimit=f}catch{}f=undefined}window.removeEventListener("error",onUnhandledError);window.removeEventListener("unhandledrejection",onUnhandledRejection)}t.unregister=unregister;function onBuildOk(){s.emit({type:s.TYPE_BUILD_OK})}t.onBuildOk=onBuildOk;function onBuildError(e){s.emit({type:s.TYPE_BUILD_ERROR,message:e})}t.onBuildError=onBuildError;function onRefresh(){s.emit({type:s.TYPE_REFRESH})}t.onRefresh=onRefresh;function onBeforeRefresh(){s.emit({type:s.TYPE_BEFORE_REFRESH})}t.onBeforeRefresh=onBeforeRefresh;var p=r(403);Object.defineProperty(t,"getErrorByType",{enumerable:true,get:function(){return p.getErrorByType}});var m=r(5233);Object.defineProperty(t,"getServerError",{enumerable:true,get:function(){return m.getServerError}});var v=r(5222);Object.defineProperty(t,"ReactDevOverlay",{enumerable:true,get:function(){return i(v).default}})},7790:function(e,t,r){var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:true});t.ErrorBoundary=void 0;const o=r(505);const a=n(r(7522));class ErrorBoundary extends a.default.PureComponent{constructor(){super(...arguments);this.state={error:null}}static getDerivedStateFromError(e){return{error:e}}componentDidCatch(e,t){this.props.onError(e,t?.componentStack||null);if(!this.props.globalOverlay){this.setState({error:e})}}render(){return this.state.error||this.props.globalOverlay&&this.props.isMounted?this.props.globalOverlay?(0,o.jsxs)("html",{children:[(0,o.jsx)("head",{}),(0,o.jsx)("body",{})]}):null:this.props.children}}t.ErrorBoundary=ErrorBoundary},5222:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};Object.defineProperty(t,"__esModule",{value:true});const i=r(505);const s=a(r(7522));const l=a(r(5851));const u=r(6338);const c=r(5936);const d=r(4355);const f=r(7790);const p=r(884);const m=r(4464);const v=r(9495);function pushErrorFilterDuplicates(e,t){return[...e.filter((e=>e.event.reason!==t.event.reason)),t]}function reducer(e,t){switch(t.type){case l.TYPE_BUILD_OK:{return{...e,buildError:null}}case l.TYPE_BUILD_ERROR:{return{...e,buildError:t.message}}case l.TYPE_BEFORE_REFRESH:{return{...e,refreshState:{type:"pending",errors:[]}}}case l.TYPE_REFRESH:{return{...e,buildError:null,errors:e.refreshState.type==="pending"?e.refreshState.errors:[],refreshState:{type:"idle"}}}case l.TYPE_UNHANDLED_ERROR:case l.TYPE_UNHANDLED_REJECTION:{switch(e.refreshState.type){case"idle":{return{...e,nextId:e.nextId+1,errors:pushErrorFilterDuplicates(e.errors,{id:e.nextId,event:t})}}case"pending":{return{...e,nextId:e.nextId+1,refreshState:{...e.refreshState,errors:pushErrorFilterDuplicates(e.refreshState.errors,{id:e.nextId,event:t})}}}default:const r=e.refreshState;return e}}default:{const r=t;return e}}}const shouldPreventDisplay=(e,t)=>{if(!t||!e){return false}return t.includes(e)};const b=function ReactDevOverlay({children:e,preventDisplay:t,globalOverlay:r}){const[n,o]=s.useReducer(reducer,{nextId:1,buildError:null,errors:[],refreshState:{type:"idle"}});s.useEffect((()=>{l.on(o);return function(){l.off(o)}}),[o]);const a=s.useCallback(((e,t)=>{}),[]);const b=n.buildError!=null;const g=Boolean(n.errors.length);const h=b?"build":g?"runtime":null;const y=h!==null;return(0,i.jsxs)(s.Fragment,{children:[(0,i.jsx)(f.ErrorBoundary,{globalOverlay:r,isMounted:y,onError:a,children:e??null}),y?(0,i.jsxs)(u.ShadowPortal,{globalOverlay:r,children:[(0,i.jsx)(v.CssReset,{}),(0,i.jsx)(p.Base,{}),(0,i.jsx)(m.ComponentStyles,{}),shouldPreventDisplay(h,t)?null:b?(0,i.jsx)(c.BuildError,{message:n.buildError}):g?(0,i.jsx)(d.Errors,{errors:n.errors}):undefined]}):undefined]})};t["default"]=b},5851:function(e,t){Object.defineProperty(t,"__esModule",{value:true});t.off=t.on=t.emit=t.TYPE_UNHANDLED_REJECTION=t.TYPE_UNHANDLED_ERROR=t.TYPE_BEFORE_REFRESH=t.TYPE_REFRESH=t.TYPE_BUILD_ERROR=t.TYPE_BUILD_OK=void 0;t.TYPE_BUILD_OK="build-ok";t.TYPE_BUILD_ERROR="build-error";t.TYPE_REFRESH="fast-refresh";t.TYPE_BEFORE_REFRESH="before-fast-refresh";t.TYPE_UNHANDLED_ERROR="unhandled-error";t.TYPE_UNHANDLED_REJECTION="unhandled-rejection";let r=new Set;let n=[];function drain(){setTimeout((function(){while(Boolean(n.length)&&Boolean(r.size)){const e=n.shift();r.forEach((t=>t(e)))}}),1)}function emit(e){n.push(Object.freeze({...e}));drain()}t.emit=emit;function on(e){if(r.has(e)){return false}r.add(e);drain();return true}t.on=on;function off(e){if(r.has(e)){r.delete(e);return true}return false}t.off=off},1987:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};var i=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:true});t.CodeFrame=void 0;const s=r(505);const l=i(r(7997));const u=a(r(7522));const c=i(r(7518));const d=r(7504);const f=function CodeFrame({stackFrame:e,codeFrame:t}){const r=u.useMemo((()=>{const e=t.split(/\r?\n/g);const r=e.map((e=>/^>? +\d+ +\| [ ]+/.exec((0,c.default)(e))===null?null:/^>? +\d+ +\| ( *)/.exec((0,c.default)(e)))).filter(Boolean).map((e=>e.pop())).reduce(((e,t)=>isNaN(e)?t.length:Math.min(e,t.length)),NaN);if(r>1){const t=" ".repeat(r);return e.map(((e,r)=>~(r=e.indexOf("|"))?e.substring(0,r)+e.substring(r).replace(t,""):e)).join("\n")}return e.join("\n")}),[t]);const n=u.useMemo((()=>l.default.ansiToJson(r,{json:true,use_classes:true,remove_empty:true})),[r]);const o=u.useCallback((()=>{const t=new URLSearchParams;for(const r in e){t.append(r,(e[r]??"").toString())}self.fetch(`${process.env.__NEXT_ROUTER_BASEPATH||""}/__nextjs_launch-editor?${t.toString()}`).then((()=>{}),(()=>{console.error("There was an issue opening this code in your editor.")}))}),[e]);return(0,s.jsxs)("div",{"data-nextjs-codeframe":true,children:[(0,s.jsx)("div",{children:(0,s.jsxs)("p",{role:"link",onClick:o,tabIndex:1,title:"Click to open in your editor",children:[(0,s.jsxs)("span",{children:[(0,d.getFrameSource)(e)," @ ",e.methodName]}),(0,s.jsxs)("svg",{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,s.jsx)("path",{d:"M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"}),(0,s.jsx)("polyline",{points:"15 3 21 3 21 9"}),(0,s.jsx)("line",{x1:"10",y1:"14",x2:"21",y2:"3"})]})]})}),(0,s.jsx)("pre",{children:n.map(((e,t)=>(0,s.jsx)("span",{style:{color:e.fg?`var(--color-${e.fg})`:undefined,...e.decoration==="bold"?{fontWeight:800}:e.decoration==="italic"?{fontStyle:"italic"}:undefined},children:e.content},`frame-${t}`)))})]})};t.CodeFrame=f},1413:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.CodeFrame=void 0;var n=r(1987);Object.defineProperty(t,"CodeFrame",{enumerable:true,get:function(){return n.CodeFrame}})},399:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.styles=void 0;const n=r(8910);const o=(0,n.noop)`
  [data-nextjs-codeframe] {
    overflow: auto;
    border-radius: var(--size-gap-half);
    background-color: var(--color-ansi-bg);
    color: var(--color-ansi-fg);
  }
  [data-nextjs-codeframe]::selection,
  [data-nextjs-codeframe] *::selection {
    background-color: var(--color-ansi-selection);
  }
  [data-nextjs-codeframe] * {
    color: inherit;
    background-color: transparent;
    font-family: var(--font-stack-monospace);
  }

  [data-nextjs-codeframe] > * {
    margin: 0;
    padding: calc(var(--size-gap) + var(--size-gap-half))
      calc(var(--size-gap-double) + var(--size-gap-half));
  }
  [data-nextjs-codeframe] > div {
    display: inline-block;
    width: auto;
    min-width: 100%;
    border-bottom: 1px solid var(--color-ansi-bright-black);
  }
  [data-nextjs-codeframe] > div > p {
    display: flex;
    align-items: center;
    justify-content: space-between;
    cursor: pointer;
    margin: 0;
  }
  [data-nextjs-codeframe] > div > p:hover {
    text-decoration: underline dotted;
  }
  [data-nextjs-codeframe] div > p > svg {
    width: auto;
    height: 1em;
    margin-left: 8px;
  }
  [data-nextjs-codeframe] div > pre {
    overflow: hidden;
    display: inline-block;
  }
`;t.styles=o},1616:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};Object.defineProperty(t,"__esModule",{value:true});t.Dialog=void 0;const i=r(505);const s=a(r(7522));const l=r(7169);const u=function Dialog({children:e,type:t,onClose:r,...n}){const[o,a]=s.useState(null);const[u,c]=s.useState(typeof document!=="undefined"&&document.hasFocus()?"dialog":undefined);const d=s.useCallback((e=>{a(e)}),[]);(0,l.useOnClickOutside)(o,r);s.useEffect((()=>{if(o==null){return}const e=o.getRootNode();if(!(e instanceof ShadowRoot)){return}const t=e;function handler(e){const r=t.activeElement;if(e.key==="Enter"&&r instanceof HTMLElement&&r.getAttribute("role")==="link"){e.preventDefault();e.stopPropagation();r.click()}}function handleFocus(){c(document.hasFocus()?"dialog":undefined)}t.addEventListener("keydown",handler);window.addEventListener("focus",handleFocus);window.addEventListener("blur",handleFocus);return()=>{t.removeEventListener("keydown",handler);window.removeEventListener("focus",handleFocus);window.removeEventListener("blur",handleFocus)}}),[o]);return(0,i.jsxs)("div",{ref:d,"data-nextjs-dialog":true,tabIndex:-1,role:u,"aria-labelledby":n["aria-labelledby"],"aria-describedby":n["aria-describedby"],"aria-modal":"true",children:[(0,i.jsx)("div",{"data-nextjs-dialog-banner":true,className:`banner-${t}`}),e]})};t.Dialog=u},2011:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.DialogBody=void 0;const n=r(505);const o=function DialogBody({children:e,className:t}){return(0,n.jsx)("div",{"data-nextjs-dialog-body":true,className:t,children:e})};t.DialogBody=o},8991:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.DialogContent=void 0;const n=r(505);const o=function DialogContent({children:e,className:t}){return(0,n.jsx)("div",{"data-nextjs-dialog-content":true,className:t,children:e})};t.DialogContent=o},342:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.DialogHeader=void 0;const n=r(505);const o=function DialogHeader({children:e,className:t}){return(0,n.jsx)("div",{"data-nextjs-dialog-header":true,className:t,children:e})};t.DialogHeader=o},5651:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.styles=t.DialogHeader=t.DialogContent=t.DialogBody=t.Dialog=void 0;var n=r(1616);Object.defineProperty(t,"Dialog",{enumerable:true,get:function(){return n.Dialog}});var o=r(2011);Object.defineProperty(t,"DialogBody",{enumerable:true,get:function(){return o.DialogBody}});var a=r(8991);Object.defineProperty(t,"DialogContent",{enumerable:true,get:function(){return a.DialogContent}});var i=r(342);Object.defineProperty(t,"DialogHeader",{enumerable:true,get:function(){return i.DialogHeader}});var s=r(5213);Object.defineProperty(t,"styles",{enumerable:true,get:function(){return s.styles}})},5213:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.styles=void 0;const n=r(8910);const o=(0,n.noop)`
  [data-nextjs-dialog] {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin-right: auto;
    margin-left: auto;
    outline: none;
    background: var(--color-background);
    border-radius: var(--size-gap);
    box-shadow: 0 var(--size-gap-half) var(--size-gap-double)
      rgba(0, 0, 0, 0.25);
    max-height: calc(100% - 56px);
    overflow-y: hidden;
  }

  @media (max-height: 812px) {
    [data-nextjs-dialog-overlay] {
      max-height: calc(100% - 15px);
    }
  }

  @media (min-width: 576px) {
    [data-nextjs-dialog] {
      max-width: 540px;
      box-shadow: 0 var(--size-gap) var(--size-gap-quad) rgba(0, 0, 0, 0.25);
    }
  }

  @media (min-width: 768px) {
    [data-nextjs-dialog] {
      max-width: 720px;
    }
  }

  @media (min-width: 992px) {
    [data-nextjs-dialog] {
      max-width: 960px;
    }
  }

  [data-nextjs-dialog-banner] {
    position: relative;
  }
  [data-nextjs-dialog-banner].banner-warning {
    border-color: var(--color-ansi-yellow);
  }
  [data-nextjs-dialog-banner].banner-error {
    border-color: var(--color-ansi-red);
  }

  [data-nextjs-dialog-banner]::after {
    z-index: 2;
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    /* banner width: */
    border-top-width: var(--size-gap-half);
    border-bottom-width: 0;
    border-top-style: solid;
    border-bottom-style: solid;
    border-top-color: inherit;
    border-bottom-color: transparent;
  }

  [data-nextjs-dialog-content] {
    overflow-y: auto;
    border: none;
    margin: 0;
    /* calc(padding + banner width offset) */
    padding: calc(var(--size-gap-double) + var(--size-gap-half))
      var(--size-gap-double);
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  [data-nextjs-dialog-content] > [data-nextjs-dialog-header] {
    flex-shrink: 0;
    margin-bottom: var(--size-gap-double);
  }
  [data-nextjs-dialog-content] > [data-nextjs-dialog-body] {
    position: relative;
    flex: 1 1 auto;
  }
`;t.styles=o},9831:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};Object.defineProperty(t,"__esModule",{value:true});t.LeftRightDialogHeader=void 0;const i=r(505);const s=a(r(7522));const l=r(865);const u=function LeftRightDialogHeader({children:e,className:t,previous:r,next:n,close:o}){const a=s.useRef(null);const u=s.useRef(null);const c=s.useRef(null);const[d,f]=s.useState(null);const p=s.useCallback((e=>{f(e)}),[]);s.useEffect((()=>{if(d==null){return}const e=d.getRootNode();const t=self.document;function handler(t){if(t.key==="ArrowLeft"){t.stopPropagation();if(a.current){a.current.focus()}r&&r()}else if(t.key==="ArrowRight"){t.stopPropagation();if(u.current){u.current.focus()}n&&n()}else if(t.key==="Escape"){t.stopPropagation();if(e instanceof ShadowRoot){const t=e.activeElement;if(t&&t!==c.current&&t instanceof HTMLElement){t.blur();return}}if(o){o()}}}e.addEventListener("keydown",handler);if(e!==t){t.addEventListener("keydown",handler)}return function(){e.removeEventListener("keydown",handler);if(e!==t){t.removeEventListener("keydown",handler)}}}),[o,d,n,r]);s.useEffect((()=>{if(d==null){return}const e=d.getRootNode();if(e instanceof ShadowRoot){const t=e.activeElement;if(r==null){if(a.current&&t===a.current){a.current.blur()}}else if(n==null){if(u.current&&t===u.current){u.current.blur()}}}}),[d,n,r]);return(0,i.jsxs)("div",{"data-nextjs-dialog-left-right":true,className:t,children:[(0,i.jsxs)("nav",{ref:p,children:[(0,i.jsx)("button",{ref:a,type:"button",disabled:r==null?true:undefined,"aria-disabled":r==null?true:undefined,onClick:r??undefined,children:(0,i.jsxs)("svg",{viewBox:"0 0 14 14",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[(0,i.jsx)("title",{children:"previous"}),(0,i.jsx)("path",{d:"M6.99996 1.16666L1.16663 6.99999L6.99996 12.8333M12.8333 6.99999H1.99996H12.8333Z",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round"})]})}),(0,i.jsx)("button",{ref:u,type:"button",disabled:n==null?true:undefined,"aria-disabled":n==null?true:undefined,onClick:n??undefined,children:(0,i.jsxs)("svg",{viewBox:"0 0 14 14",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[(0,i.jsx)("title",{children:"next"}),(0,i.jsx)("path",{d:"M6.99996 1.16666L12.8333 6.99999L6.99996 12.8333M1.16663 6.99999H12H1.16663Z",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round"})]})})," ",e]}),o?(0,i.jsx)("button",{"data-nextjs-errors-dialog-left-right-close-button":true,ref:c,type:"button",onClick:o,"aria-label":"Close",children:(0,i.jsx)("span",{"aria-hidden":"true",children:(0,i.jsx)(l.CloseIcon,{})})}):null]})};t.LeftRightDialogHeader=u},2732:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.styles=t.LeftRightDialogHeader=void 0;var n=r(9831);Object.defineProperty(t,"LeftRightDialogHeader",{enumerable:true,get:function(){return n.LeftRightDialogHeader}});var o=r(6543);Object.defineProperty(t,"styles",{enumerable:true,get:function(){return o.styles}})},6543:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.styles=void 0;const n=r(8910);const o=(0,n.noop)`
  [data-nextjs-dialog-left-right] {
    display: flex;
    flex-direction: row;
    align-content: center;
    align-items: center;
    justify-content: space-between;
  }
  [data-nextjs-dialog-left-right] > nav > button {
    display: inline-flex;
    align-items: center;
    justify-content: center;

    width: calc(var(--size-gap-double) + var(--size-gap));
    height: calc(var(--size-gap-double) + var(--size-gap));
    font-size: 0;
    border: none;
    background-color: rgba(255, 85, 85, 0.1);
    color: var(--color-ansi-red);
    cursor: pointer;
    transition: background-color 0.25s ease;
  }
  [data-nextjs-dialog-left-right] > nav > button > svg {
    width: auto;
    height: calc(var(--size-gap) + var(--size-gap-half));
  }
  [data-nextjs-dialog-left-right] > nav > button:hover {
    background-color: rgba(255, 85, 85, 0.2);
  }
  [data-nextjs-dialog-left-right] > nav > button:disabled {
    background-color: rgba(255, 85, 85, 0.1);
    color: rgba(255, 85, 85, 0.4);
    cursor: not-allowed;
  }

  [data-nextjs-dialog-left-right] > nav > button:first-of-type {
    border-radius: var(--size-gap-half) 0 0 var(--size-gap-half);
    margin-right: 1px;
  }
  [data-nextjs-dialog-left-right] > nav > button:last-of-type {
    border-radius: 0 var(--size-gap-half) var(--size-gap-half) 0;
  }

  [data-nextjs-dialog-left-right] > button:last-of-type {
    border: 0;
    padding: 0;

    background-color: transparent;
    appearance: none;

    opacity: 0.4;
    transition: opacity 0.25s ease;

    color: var(--color-font);
  }
  [data-nextjs-dialog-left-right] > button:last-of-type:hover {
    opacity: 0.7;
  }
`;t.styles=o},8017:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};var i=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:true});t.Overlay=void 0;const s=r(505);const l=i(r(8975));const u=a(r(7522));const c=r(7800);const d=function Overlay({className:e,children:t,fixed:r}){u.useEffect((()=>{(0,c.lock)();return()=>{(0,c.unlock)()}}),[]);const[n,o]=u.useState(null);const a=u.useCallback((e=>{o(e)}),[]);u.useEffect((()=>{if(n==null){return}const e=(0,l.default)({context:n});return()=>{e.disengage()}}),[n]);return(0,s.jsxs)("div",{"data-nextjs-dialog-overlay":true,className:e,ref:a,children:[(0,s.jsx)("div",{"data-nextjs-dialog-backdrop":true,"data-nextjs-dialog-backdrop-fixed":r?true:undefined}),t]})};t.Overlay=d},7800:function(e,t){Object.defineProperty(t,"__esModule",{value:true});t.unlock=t.lock=void 0;let r;let n;let o=0;function lock(){setTimeout((()=>{if(o++>0){return}const e=window.innerWidth-document.documentElement.clientWidth;if(e>0){r=document.body.style.paddingRight;document.body.style.paddingRight=`${e}px`}n=document.body.style.overflow;document.body.style.overflow="hidden"}))}t.lock=lock;function unlock(){setTimeout((()=>{if(o===0||--o!==0){return}if(r!==undefined){document.body.style.paddingRight=r;r=undefined}if(n!==undefined){document.body.style.overflow=n;n=undefined}}))}t.unlock=unlock},8278:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.Overlay=void 0;var n=r(8017);Object.defineProperty(t,"Overlay",{enumerable:true,get:function(){return n.Overlay}})},8975:function(e,t,r){var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:true});const o=n(r(7709));const a=n(r(7292));function nodeArray(e){if(!e){return[]}if(Array.isArray(e)){return e}if(e.nodeType!==undefined){return[e]}if(typeof e==="string"){e=document.querySelectorAll(e)}if(e.length!==undefined){return[].slice.call(e,0)}throw new TypeError("unexpected input "+String(e))}function contextToElement(e){var t=e.context,r=e.label,n=r===undefined?"context-to-element":r,o=e.resolveDocument,a=e.defaultToDocument;var i=nodeArray(t)[0];if(o&&i&&i.nodeType===Node.DOCUMENT_NODE){i=i.documentElement}if(!i&&a){return document.documentElement}if(!i){throw new TypeError(n+" requires valid options.context")}if(i.nodeType!==Node.ELEMENT_NODE&&i.nodeType!==Node.DOCUMENT_FRAGMENT_NODE){throw new TypeError(n+" requires options.context to be an Element")}return i}function getShadowHost(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context;var r=contextToElement({label:"get/shadow-host",context:t});var n=null;while(r){n=r;r=r.parentNode}if(n.nodeType===n.DOCUMENT_FRAGMENT_NODE&&n.host){return n.host}return null}function getDocument(e){if(!e){return document}if(e.nodeType===Node.DOCUMENT_NODE){return e}return e.ownerDocument||document}function isActiveElement(e){var t=contextToElement({label:"is/active-element",resolveDocument:true,context:e});var r=getDocument(t);if(r.activeElement===t){return true}var n=getShadowHost({context:t});if(n&&n.shadowRoot.activeElement===t){return true}return false}function getParents(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context;var r=[];var n=contextToElement({label:"get/parents",context:t});while(n){r.push(n);n=n.parentNode;if(n&&n.nodeType!==Node.ELEMENT_NODE){n=null}}return r}var i=["matches","webkitMatchesSelector","mozMatchesSelector","msMatchesSelector"];var s=null;function findMethodName(e){i.some((function(t){if(!e[t]){return false}s=t;return true}))}function elementMatches(e,t){if(!s){findMethodName(e)}return e[s](t)}var l=JSON.parse(JSON.stringify(o.default));var u=l.os.family||"";var c=u==="Android";var d=u.slice(0,7)==="Windows";var f=u==="OS X";var p=u==="iOS";var m=l.layout==="Blink";var v=l.layout==="Gecko";var b=l.layout==="Trident";var g=l.layout==="EdgeHTML";var h=l.layout==="WebKit";var y=parseFloat(l.version);var x=Math.floor(y);l.majorVersion=x;l.is={ANDROID:c,WINDOWS:d,OSX:f,IOS:p,BLINK:m,GECKO:v,TRIDENT:b,EDGE:g,WEBKIT:h,IE9:b&&x===9,IE10:b&&x===10,IE11:b&&x===11};function before(){var e={activeElement:document.activeElement,windowScrollTop:window.scrollTop,windowScrollLeft:window.scrollLeft,bodyScrollTop:document.body.scrollTop,bodyScrollLeft:document.body.scrollLeft};var t=document.createElement("iframe");t.setAttribute("style","position:absolute; position:fixed; top:0; left:-2px; width:1px; height:1px; overflow:hidden;");t.setAttribute("aria-live","off");t.setAttribute("aria-busy","true");t.setAttribute("aria-hidden","true");document.body.appendChild(t);var r=t.contentWindow;var n=r.document;n.open();n.close();var o=n.createElement("div");n.body.appendChild(o);e.iframe=t;e.wrapper=o;e.window=r;e.document=n;return e}function test(e,t){e.wrapper.innerHTML="";var r=typeof t.element==="string"?e.document.createElement(t.element):t.element(e.wrapper,e.document);var n=t.mutate&&t.mutate(r,e.wrapper,e.document);if(!n&&n!==false){n=r}!r.parentNode&&e.wrapper.appendChild(r);n&&n.focus&&n.focus();return t.validate?t.validate(r,n,e.document):e.document.activeElement===n}function after(e){if(e.activeElement===document.body){document.activeElement&&document.activeElement.blur&&document.activeElement.blur();if(l.is.IE10){document.body.focus()}}else{e.activeElement&&e.activeElement.focus&&e.activeElement.focus()}document.body.removeChild(e.iframe);window.scrollTop=e.windowScrollTop;window.scrollLeft=e.windowScrollLeft;document.body.scrollTop=e.bodyScrollTop;document.body.scrollLeft=e.bodyScrollLeft}function detectFocus(e){var t=before();var r={};Object.keys(e).map((function(n){r[n]=test(t,e[n])}));after(t);return r}var _="1.4.1";function readLocalStorage(e){var t=void 0;try{t=window.localStorage&&window.localStorage.getItem(e);t=t?JSON.parse(t):{}}catch(e){t={}}return t}function writeLocalStorage(e,t){if(!document.hasFocus()){try{window.localStorage&&window.localStorage.removeItem(e)}catch(e){}return}try{window.localStorage&&window.localStorage.setItem(e,JSON.stringify(t))}catch(e){}}var w=typeof window!=="undefined"&&window.navigator.userAgent||"";var E="ally-supports-cache";var j=readLocalStorage(E);if(j.userAgent!==w||j.version!==_){j={}}j.userAgent=w;j.version=_;var O={get:function get(){return j},set:function set(e){Object.keys(e).forEach((function(t){j[t]=e[t]}));j.time=(new Date).toISOString();writeLocalStorage(E,j)}};function cssShadowPiercingDeepCombinator(){var e=void 0;try{document.querySelector("html >>> :first-child");e=">>>"}catch(t){try{document.querySelector("html /deep/ :first-child");e="/deep/"}catch(t){e=""}}return e}var k="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";var S={element:"div",mutate:function mutate(e){e.innerHTML='<map name="image-map-tabindex-test">'+'<area shape="rect" coords="63,19,144,45"></map>'+'<img usemap="#image-map-tabindex-test" tabindex="-1" alt="" src="'+k+'">';return e.querySelector("area")}};var C={element:"div",mutate:function mutate(e){e.innerHTML='<map name="image-map-tabindex-test">'+'<area href="#void" tabindex="-1" shape="rect" coords="63,19,144,45"></map>'+'<img usemap="#image-map-tabindex-test" alt="" src="'+k+'">';return false},validate:function validate(e,t,r){if(l.is.GECKO){return true}var n=e.querySelector("area");n.focus();return r.activeElement===n}};var T={element:"div",mutate:function mutate(e){e.innerHTML='<map name="image-map-area-href-test">'+'<area shape="rect" coords="63,19,144,45"></map>'+'<img usemap="#image-map-area-href-test" alt="" src="'+k+'">';return e.querySelector("area")},validate:function validate(e,t,r){if(l.is.GECKO){return true}return r.activeElement===t}};var D={name:"can-focus-audio-without-controls",element:"audio",mutate:function mutate(e){try{e.setAttribute("src",k)}catch(e){}}};var P="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ";var N={element:"div",mutate:function mutate(e){e.innerHTML='<map name="broken-image-map-test"><area href="#void" shape="rect" coords="63,19,144,45"></map>'+'<img usemap="#broken-image-map-test" alt="" src="'+P+'">';return e.querySelector("area")}};var R={element:"div",mutate:function mutate(e){e.setAttribute("tabindex","-1");e.setAttribute("style","display: -webkit-flex; display: -ms-flexbox; display: flex;");e.innerHTML='<span style="display: block;">hello</span>';return e.querySelector("span")}};var F={element:"fieldset",mutate:function mutate(e){e.setAttribute("tabindex",0);e.setAttribute("disabled","disabled")}};var I={element:"fieldset",mutate:function mutate(e){e.innerHTML="<legend>legend</legend><p>content</p>"}};var A={element:"span",mutate:function mutate(e){e.setAttribute("style","display: -webkit-flex; display: -ms-flexbox; display: flex;");e.innerHTML='<span style="display: block;">hello</span>'}};var M={element:"form",mutate:function mutate(e){e.setAttribute("tabindex",0);e.setAttribute("disabled","disabled")}};var L={element:"a",mutate:function mutate(e){e.href="#void";e.innerHTML='<img ismap src="'+k+'" alt="">';return e.querySelector("img")}};var B={element:"div",mutate:function mutate(e){e.innerHTML='<map name="image-map-tabindex-test"><area href="#void" shape="rect" coords="63,19,144,45"></map>'+'<img usemap="#image-map-tabindex-test" tabindex="-1" alt="" '+'src="'+k+'">';return e.querySelector("img")}};var H={element:function element(e,t){var r=t.createElement("iframe");e.appendChild(r);var n=r.contentWindow.document;n.open();n.close();return r},mutate:function mutate(e){e.style.visibility="hidden";var t=e.contentWindow.document;var r=t.createElement("input");t.body.appendChild(r);return r},validate:function validate(e){var t=e.contentWindow.document;var r=t.querySelector("input");return t.activeElement===r}};var z=!l.is.WEBKIT;function focusInZeroDimensionObject(){return z}var W={element:"div",mutate:function mutate(e){e.setAttribute("tabindex","invalid-value")}};var V={element:"label",mutate:function mutate(e){e.setAttribute("tabindex","-1")},validate:function validate(e,t,r){var n=e.offsetHeight;e.focus();return r.activeElement===e}};var $="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtb"+"G5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBpZD0ic3ZnIj48dGV4dCB4PSIxMCIgeT0iMjAiIGlkPSJ"+"zdmctbGluay10ZXh0Ij50ZXh0PC90ZXh0Pjwvc3ZnPg==";var U={element:"object",mutate:function mutate(e){e.setAttribute("type","image/svg+xml");e.setAttribute("data",$);e.setAttribute("width","200");e.setAttribute("height","50");e.style.visibility="hidden"}};var K={name:"can-focus-object-svg",element:"object",mutate:function mutate(e){e.setAttribute("type","image/svg+xml");e.setAttribute("data",$);e.setAttribute("width","200");e.setAttribute("height","50")},validate:function validate(e,t,r){if(l.is.GECKO){return true}return r.activeElement===e}};var G=!l.is.IE9;function focusObjectSwf(){return G}var Z={element:"div",mutate:function mutate(e){e.innerHTML='<map name="focus-redirect-img-usemap"><area href="#void" shape="rect" coords="63,19,144,45"></map>'+'<img usemap="#focus-redirect-img-usemap" alt="" '+'src="'+k+'">';return e.querySelector("img")},validate:function validate(e,t,r){var n=e.querySelector("area");return r.activeElement===n}};var Y={element:"fieldset",mutate:function mutate(e){e.innerHTML='<legend>legend</legend><input tabindex="-1"><input tabindex="0">';return false},validate:function validate(e,t,r){var n=e.querySelector('input[tabindex="-1"]');var o=e.querySelector('input[tabindex="0"]');e.focus();e.querySelector("legend").focus();return r.activeElement===n&&"focusable"||r.activeElement===o&&"tabbable"||""}};var J={element:"div",mutate:function mutate(e){e.setAttribute("style","width: 100px; height: 50px; overflow: auto;");e.innerHTML='<div style="width: 500px; height: 40px;">scrollable content</div>';return e.querySelector("div")}};var X={element:"div",mutate:function mutate(e){e.setAttribute("style","width: 100px; height: 50px;");e.innerHTML='<div style="width: 500px; height: 40px;">scrollable content</div>'}};var Q={element:"div",mutate:function mutate(e){e.setAttribute("style","width: 100px; height: 50px; overflow: auto;");e.innerHTML='<div style="width: 500px; height: 40px;">scrollable content</div>'}};var ee={element:"details",mutate:function mutate(e){e.innerHTML="<summary>foo</summary><p>content</p>";return e.firstElementChild}};function makeFocusableForeignObject(){var e=document.createElementNS("http://www.w3.org/2000/svg","foreignObject");e.width.baseVal.value=30;e.height.baseVal.value=30;e.appendChild(document.createElement("input"));e.lastChild.type="text";return e}function focusSvgForeignObjectHack(e){var t=e.ownerSVGElement||e.nodeName.toLowerCase()==="svg";if(!t){return false}var r=makeFocusableForeignObject();e.appendChild(r);var n=r.querySelector("input");n.focus();n.disabled=true;e.removeChild(r);return true}function generate(e){return'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'+e+"</svg>"}function focus(e){if(e.focus){return}try{HTMLElement.prototype.focus.call(e)}catch(t){focusSvgForeignObjectHack(e)}}function validate(e,t,r){focus(t);return r.activeElement===t}var te={element:"div",mutate:function mutate(e){e.innerHTML=generate('<text focusable="true">a</text>');return e.querySelector("text")},validate:validate};var re={element:"div",mutate:function mutate(e){e.innerHTML=generate('<text tabindex="0">a</text>');return e.querySelector("text")},validate:validate};var ne={element:"div",mutate:function mutate(e){e.innerHTML=generate('<text tabindex="-1">a</text>');return e.querySelector("text")},validate:validate};var oe={element:"div",mutate:function mutate(e){e.innerHTML=generate(['<g id="ally-test-target"><a xlink:href="#void"><text>link</text></a></g>','<use xlink:href="#ally-test-target" x="0" y="0" tabindex="-1" />'].join(""));return e.querySelector("use")},validate:validate};var ae={element:"div",mutate:function mutate(e){e.innerHTML=generate('<foreignObject tabindex="-1"><input type="text" /></foreignObject>');return e.querySelector("foreignObject")||e.getElementsByTagName("foreignObject")[0]},validate:validate};var ie=Boolean(l.is.GECKO&&typeof SVGElement!=="undefined"&&SVGElement.prototype.focus);function focusSvgInIframe(){return ie}var se={element:"div",mutate:function mutate(e){e.innerHTML=generate("");return e.firstChild},validate:validate};var le={element:"div",mutate:function mutate(e){e.setAttribute("tabindex","3x")}};var ue={element:"table",mutate:function mutate(e,t,r){var n=r.createDocumentFragment();n.innerHTML="<tr><td>cell</td></tr>";e.appendChild(n)}};var ce={element:"video",mutate:function mutate(e){try{e.setAttribute("src",k)}catch(e){}}};var de=l.is.GECKO||l.is.TRIDENT||l.is.EDGE;function tabsequenceAreaAtImgPosition(){return de}var fe={cssShadowPiercingDeepCombinator:cssShadowPiercingDeepCombinator,focusInZeroDimensionObject:focusInZeroDimensionObject,focusObjectSwf:focusObjectSwf,focusSvgInIframe:focusSvgInIframe,tabsequenceAreaAtImgPosition:tabsequenceAreaAtImgPosition};var pe={focusAreaImgTabindex:S,focusAreaTabindex:C,focusAreaWithoutHref:T,focusAudioWithoutControls:D,focusBrokenImageMap:N,focusChildrenOfFocusableFlexbox:R,focusFieldsetDisabled:F,focusFieldset:I,focusFlexboxContainer:A,focusFormDisabled:M,focusImgIsmap:L,focusImgUsemapTabindex:B,focusInHiddenIframe:H,focusInvalidTabindex:W,focusLabelTabindex:V,focusObjectSvg:K,focusObjectSvgHidden:U,focusRedirectImgUsemap:Z,focusRedirectLegend:Y,focusScrollBody:J,focusScrollContainerWithoutOverflow:X,focusScrollContainer:Q,focusSummary:ee,focusSvgFocusableAttribute:te,focusSvgTabindexAttribute:re,focusSvgNegativeTabindexAttribute:ne,focusSvgUseTabindex:oe,focusSvgForeignobjectTabindex:ae,focusSvg:se,focusTabindexTrailingCharacters:le,focusTable:ue,focusVideoWithoutControls:ce};function executeTests(){var e=detectFocus(pe);Object.keys(fe).forEach((function(t){e[t]=fe[t]()}));return e}var me=null;function _supports(){if(me){return me}me=O.get();if(!me.time){O.set(executeTests());me=O.get()}return me}var ve=void 0;var be=/^\s*(-|\+)?[0-9]+\s*$/;var ge=/^\s*(-|\+)?[0-9]+.*$/;function isValidTabindex(e){if(!ve){ve=_supports()}var t=ve.focusTabindexTrailingCharacters?ge:be;var r=contextToElement({label:"is/valid-tabindex",resolveDocument:true,context:e});var n=r.hasAttribute("tabindex");var o=r.hasAttribute("tabIndex");if(!n&&!o){return false}var a=r.ownerSVGElement||r.nodeName.toLowerCase()==="svg";if(a&&!ve.focusSvgTabindexAttribute){return false}if(ve.focusInvalidTabindex){return true}var i=r.getAttribute(n?"tabindex":"tabIndex");if(i==="-32768"){return false}return Boolean(i&&t.test(i))}function tabindexValue(e){if(!isValidTabindex(e)){return null}var t=e.hasAttribute("tabindex");var r=t?"tabindex":"tabIndex";var n=parseInt(e.getAttribute(r),10);return isNaN(n)?-1:n}function isUserModifyWritable(e){var t=e.webkitUserModify||"";return Boolean(t&&t.indexOf("write")!==-1)}function hasCssOverflowScroll(e){return[e.getPropertyValue("overflow"),e.getPropertyValue("overflow-x"),e.getPropertyValue("overflow-y")].some((function(e){return e==="auto"||e==="scroll"}))}function hasCssDisplayFlex(e){return e.display.indexOf("flex")>-1}function isScrollableContainer(e,t,r,n){if(t!=="div"&&t!=="span"){return false}if(r&&r!=="div"&&r!=="span"&&!hasCssOverflowScroll(n)){return false}return e.offsetHeight<e.scrollHeight||e.offsetWidth<e.scrollWidth}var he=void 0;function isFocusRelevantRules(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.except,n=r===undefined?{flexbox:false,scrollable:false,shadow:false}:r;if(!he){he=_supports()}var o=contextToElement({label:"is/focus-relevant",resolveDocument:true,context:t});if(!n.shadow&&o.shadowRoot){return true}var a=o.nodeName.toLowerCase();if(a==="input"&&o.type==="hidden"){return false}if(a==="input"||a==="select"||a==="button"||a==="textarea"){return true}if(a==="legend"&&he.focusRedirectLegend){return true}if(a==="label"){return true}if(a==="area"){return true}if(a==="a"&&o.hasAttribute("href")){return true}if(a==="object"&&o.hasAttribute("usemap")){return false}if(a==="object"){var i=o.getAttribute("type");if(!he.focusObjectSvg&&i==="image/svg+xml"){return false}else if(!he.focusObjectSwf&&i==="application/x-shockwave-flash"){return false}}if(a==="iframe"||a==="object"){return true}if(a==="embed"||a==="keygen"){return true}if(o.hasAttribute("contenteditable")){return true}if(a==="audio"&&(he.focusAudioWithoutControls||o.hasAttribute("controls"))){return true}if(a==="video"&&(he.focusVideoWithoutControls||o.hasAttribute("controls"))){return true}if(he.focusSummary&&a==="summary"){return true}var s=isValidTabindex(o);if(a==="img"&&o.hasAttribute("usemap")){return s&&he.focusImgUsemapTabindex||he.focusRedirectImgUsemap}if(he.focusTable&&(a==="table"||a==="td")){return true}if(he.focusFieldset&&a==="fieldset"){return true}var l=a==="svg";var u=o.ownerSVGElement;var c=o.getAttribute("focusable");var d=tabindexValue(o);if(a==="use"&&d!==null&&!he.focusSvgUseTabindex){return false}if(a==="foreignobject"){return d!==null&&he.focusSvgForeignobjectTabindex}if(elementMatches(o,"svg a")&&o.hasAttribute("xlink:href")){return true}if((l||u)&&o.focus&&!he.focusSvgNegativeTabindexAttribute&&d<0){return false}if(l){return s||he.focusSvg||he.focusSvgInIframe||Boolean(he.focusSvgFocusableAttribute&&c&&c==="true")}if(u){if(he.focusSvgTabindexAttribute&&s){return true}if(he.focusSvgFocusableAttribute){return c==="true"}}if(s){return true}var f=window.getComputedStyle(o,null);if(isUserModifyWritable(f)){return true}if(he.focusImgIsmap&&a==="img"&&o.hasAttribute("ismap")){var p=getParents({context:o}).some((function(e){return e.nodeName.toLowerCase()==="a"&&e.hasAttribute("href")}));if(p){return true}}if(!n.scrollable&&he.focusScrollContainer){if(he.focusScrollContainerWithoutOverflow){if(isScrollableContainer(o,a)){return true}}else if(hasCssOverflowScroll(f)){return true}}if(!n.flexbox&&he.focusFlexboxContainer&&hasCssDisplayFlex(f)){return true}var m=o.parentElement;if(!n.scrollable&&m){var v=m.nodeName.toLowerCase();var b=window.getComputedStyle(m,null);if(he.focusScrollBody&&isScrollableContainer(m,a,v,b)){return true}if(he.focusChildrenOfFocusableFlexbox){if(hasCssDisplayFlex(b)){return true}}}return false}isFocusRelevantRules.except=function(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{};var t=function isFocusRelevant(t){return isFocusRelevantRules({context:t,except:e})};t.rules=isFocusRelevantRules;return t};var ye=isFocusRelevantRules.except({});function findIndex(e,t){if(e.findIndex){return e.findIndex(t)}var r=e.length;if(r===0){return-1}for(var n=0;n<r;n++){if(t(e[n],n,e)){return n}}return-1}function getContentDocument(e){try{return e.contentDocument||e.contentWindow&&e.contentWindow.document||e.getSVGDocument&&e.getSVGDocument()||null}catch(e){return null}}function getWindow(e){var t=getDocument(e);return t.defaultView||window}var xe=void 0;function selectInShadows(e){if(typeof xe!=="string"){var t=cssShadowPiercingDeepCombinator();if(t){xe=", html "+t+" "}}if(!xe){return e}return e+xe+e.replace(/\s*,\s*/g,",").split(",").join(xe)}var _e=void 0;function findDocumentHostElement(e){if(!_e){_e=selectInShadows("object, iframe")}if(e._frameElement!==undefined){return e._frameElement}e._frameElement=null;var t=e.parent.document.querySelectorAll(_e);[].some.call(t,(function(t){var r=getContentDocument(t);if(r!==e.document){return false}e._frameElement=t;return true}));return e._frameElement}function getFrameElement(e){var t=getWindow(e);if(!t.parent||t.parent===t){return null}try{return t.frameElement||findDocumentHostElement(t)}catch(e){return null}}var we=/^(area)$/;function computedStyle(e,t){return window.getComputedStyle(e,null).getPropertyValue(t)}function notDisplayed(e){return e.some((function(e){return computedStyle(e,"display")==="none"}))}function notVisible(e){var t=findIndex(e,(function(e){var t=computedStyle(e,"visibility");return t==="hidden"||t==="collapse"}));if(t===-1){return false}var r=findIndex(e,(function(e){return computedStyle(e,"visibility")==="visible"}));if(r===-1){return true}if(t<r){return true}return false}function collapsedParent(e){var t=1;if(e[0].nodeName.toLowerCase()==="summary"){t=2}return e.slice(t).some((function(e){return e.nodeName.toLowerCase()==="details"&&e.open===false}))}function isVisibleRules(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.except,n=r===undefined?{notRendered:false,cssDisplay:false,cssVisibility:false,detailsElement:false,browsingContext:false}:r;var o=contextToElement({label:"is/visible",resolveDocument:true,context:t});var a=o.nodeName.toLowerCase();if(!n.notRendered&&we.test(a)){return true}var i=getParents({context:o});var s=a==="audio"&&!o.hasAttribute("controls");if(!n.cssDisplay&&notDisplayed(s?i.slice(1):i)){return false}if(!n.cssVisibility&&notVisible(i)){return false}if(!n.detailsElement&&collapsedParent(i)){return false}if(!n.browsingContext){var l=getFrameElement(o);var u=isVisibleRules.except(n);if(l&&!u(l)){return false}}return true}isVisibleRules.except=function(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{};var t=function isVisible(t){return isVisibleRules({context:t,except:e})};t.rules=isVisibleRules;return t};var Ee=isVisibleRules.except({});function getMapByName(e,t){var r=t.querySelector('map[name="'+(0,a.default)(e)+'"]');return r||null}function getImageOfArea(e){var t=e.parentElement;if(!t.name||t.nodeName.toLowerCase()!=="map"){return null}var r=getDocument(e);return r.querySelector('img[usemap="#'+(0,a.default)(t.name)+'"]')||null}var je=void 0;function isValidArea(e){if(!je){je=_supports()}var t=contextToElement({label:"is/valid-area",context:e});var r=t.nodeName.toLowerCase();if(r!=="area"){return false}var n=t.hasAttribute("tabindex");if(!je.focusAreaTabindex&&n){return false}var o=getImageOfArea(t);if(!o||!Ee(o)){return false}if(!je.focusBrokenImageMap&&(!o.complete||!o.naturalHeight||o.offsetWidth<=0||o.offsetHeight<=0)){return false}if(!je.focusAreaWithoutHref&&!t.href){return je.focusAreaTabindex&&n||je.focusAreaImgTabindex&&o.hasAttribute("tabindex")}var a=getParents({context:o}).slice(1).some((function(e){var t=e.nodeName.toLowerCase();return t==="button"||t==="a"}));if(a){return false}return true}var Oe=void 0;var ke=void 0;var Se={input:true,select:true,textarea:true,button:true,fieldset:true,form:true};function isNativeDisabledSupported(e){if(!Oe){Oe=_supports();if(Oe.focusFieldsetDisabled){delete Se.fieldset}if(Oe.focusFormDisabled){delete Se.form}ke=new RegExp("^("+Object.keys(Se).join("|")+")$")}var t=contextToElement({label:"is/native-disabled-supported",context:e});var r=t.nodeName.toLowerCase();return Boolean(ke.test(r))}var Ce=void 0;function isDisabledFieldset(e){var t=e.nodeName.toLowerCase();return t==="fieldset"&&e.disabled}function isDisabledForm(e){var t=e.nodeName.toLowerCase();return t==="form"&&e.disabled}function isDisabled(e){if(!Ce){Ce=_supports()}var t=contextToElement({label:"is/disabled",context:e});if(t.hasAttribute("data-ally-disabled")){return true}if(!isNativeDisabledSupported(t)){return false}if(t.disabled){return true}var r=getParents({context:t});if(r.some(isDisabledFieldset)){return true}if(!Ce.focusFormDisabled&&r.some(isDisabledForm)){return true}return false}function isOnlyTabbableRules(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.except,n=r===undefined?{onlyFocusableBrowsingContext:false,visible:false}:r;var o=contextToElement({label:"is/only-tabbable",resolveDocument:true,context:t});if(!n.visible&&!Ee(o)){return false}if(!n.onlyFocusableBrowsingContext&&(l.is.GECKO||l.is.TRIDENT||l.is.EDGE)){var a=getFrameElement(o);if(a){if(tabindexValue(a)<0){return false}}}var i=o.nodeName.toLowerCase();var s=tabindexValue(o);if(i==="label"&&l.is.GECKO){return s!==null&&s>=0}if(l.is.GECKO&&o.ownerSVGElement&&!o.focus){if(i==="a"&&o.hasAttribute("xlink:href")){if(l.is.GECKO){return true}}}return false}isOnlyTabbableRules.except=function(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{};var t=function isOnlyTabbable(t){return isOnlyTabbableRules({context:t,except:e})};t.rules=isOnlyTabbableRules;return t};var Te=isOnlyTabbableRules.except({});var De=void 0;function isOnlyFocusRelevant(e){var t=e.nodeName.toLowerCase();if(t==="embed"||t==="keygen"){return true}var r=tabindexValue(e);if(e.shadowRoot&&r===null){return true}if(t==="label"){return!De.focusLabelTabindex||r===null}if(t==="legend"){return r===null}if(De.focusSvgFocusableAttribute&&(e.ownerSVGElement||t==="svg")){var n=e.getAttribute("focusable");return n&&n==="false"}if(t==="img"&&e.hasAttribute("usemap")){return r===null||!De.focusImgUsemapTabindex}if(t==="area"){return!isValidArea(e)}return false}function isFocusableRules(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.except,n=r===undefined?{disabled:false,visible:false,onlyTabbable:false}:r;if(!De){De=_supports()}var o=Te.rules.except({onlyFocusableBrowsingContext:true,visible:n.visible});var a=contextToElement({label:"is/focusable",resolveDocument:true,context:t});var i=ye.rules({context:a,except:n});if(!i||isOnlyFocusRelevant(a)){return false}if(!n.disabled&&isDisabled(a)){return false}if(!n.onlyTabbable&&o(a)){return false}if(!n.visible){var s={context:a,except:{}};if(De.focusInHiddenIframe){s.except.browsingContext=true}if(De.focusObjectSvgHidden){var l=a.nodeName.toLowerCase();if(l==="object"){s.except.cssVisibility=true}}if(!Ee.rules(s)){return false}}var u=getFrameElement(a);if(u){var c=u.nodeName.toLowerCase();if(c==="object"&&!De.focusInZeroDimensionObject){if(!u.offsetWidth||!u.offsetHeight){return false}}}var d=a.nodeName.toLowerCase();if(d==="svg"&&De.focusSvgInIframe&&!u&&a.getAttribute("tabindex")===null){return false}return true}isFocusableRules.except=function(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{};var t=function isFocusable(t){return isFocusableRules({context:t,except:e})};t.rules=isFocusableRules;return t};var Pe=isFocusableRules.except({});function createFilter(e){var t=function filter(t){if(t.shadowRoot){return NodeFilter.FILTER_ACCEPT}if(e(t)){return NodeFilter.FILTER_ACCEPT}return NodeFilter.FILTER_SKIP};t.acceptNode=t;return t}var Ne=createFilter(ye);function queryFocusableStrict(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.includeContext,n=e.includeOnlyTabbable,o=e.strategy;if(!t){t=document.documentElement}var a=Pe.rules.except({onlyTabbable:n});var i=getDocument(t);var s=i.createTreeWalker(t,NodeFilter.SHOW_ELEMENT,o==="all"?Ne:createFilter(a),false);var l=[];while(s.nextNode()){if(s.currentNode.shadowRoot){if(a(s.currentNode)){l.push(s.currentNode)}l=l.concat(queryFocusableStrict({context:s.currentNode.shadowRoot,includeOnlyTabbable:n,strategy:o}))}else{l.push(s.currentNode)}}if(r){if(o==="all"){if(ye(t)){l.unshift(t)}}else if(a(t)){l.unshift(t)}}return l}var Re=void 0;var Fe=void 0;function selector$2(){if(!Re){Re=_supports()}if(typeof Fe==="string"){return Fe}Fe=""+(Re.focusTable?"table, td,":"")+(Re.focusFieldset?"fieldset,":"")+"svg a,"+"a[href],"+"area[href],"+"input, select, textarea, button,"+"iframe, object, embed,"+"keygen,"+(Re.focusAudioWithoutControls?"audio,":"audio[controls],")+(Re.focusVideoWithoutControls?"video,":"video[controls],")+(Re.focusSummary?"summary,":"")+"[tabindex],"+"[contenteditable]";Fe=selectInShadows(Fe);return Fe}function queryFocusableQuick(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.includeContext,n=e.includeOnlyTabbable;var o=selector$2();var a=t.querySelectorAll(o);var i=Pe.rules.except({onlyTabbable:n});var s=[].filter.call(a,i);if(r&&i(t)){s.unshift(t)}return s}function queryFocusable(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.includeContext,n=e.includeOnlyTabbable,o=e.strategy,a=o===undefined?"quick":o;var i=contextToElement({label:"query/focusable",resolveDocument:true,defaultToDocument:true,context:t});var s={context:i,includeContext:r,includeOnlyTabbable:n,strategy:a};if(a==="quick"){return queryFocusableQuick(s)}else if(a==="strict"||a==="all"){return queryFocusableStrict(s)}throw new TypeError('query/focusable requires option.strategy to be one of ["quick", "strict", "all"]')}var Ie=void 0;var Ae=/^(fieldset|table|td|body)$/;function isTabbableRules(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.except,n=r===undefined?{flexbox:false,scrollable:false,shadow:false,visible:false,onlyTabbable:false}:r;if(!Ie){Ie=_supports()}var o=contextToElement({label:"is/tabbable",resolveDocument:true,context:t});if(l.is.BLINK&&l.is.ANDROID&&l.majorVersion>42){return false}var a=getFrameElement(o);if(a){if(l.is.WEBKIT&&l.is.IOS){return false}if(tabindexValue(a)<0){return false}if(!n.visible&&(l.is.BLINK||l.is.WEBKIT)&&!Ee(a)){return false}var i=a.nodeName.toLowerCase();if(i==="object"){var s=l.name==="Chrome"&&l.majorVersion>=54||l.name==="Opera"&&l.majorVersion>=41;if(l.is.WEBKIT||l.is.BLINK&&!s){return false}}}var u=o.nodeName.toLowerCase();var c=tabindexValue(o);var d=c===null?null:c>=0;if(l.is.EDGE&&l.majorVersion>=14&&a&&o.ownerSVGElement&&c<0){return true}var f=d!==false;var p=c!==null&&c>=0;if(o.hasAttribute("contenteditable")){return f}if(Ae.test(u)&&d!==true){return false}if(l.is.WEBKIT&&l.is.IOS){var m=u==="input"&&o.type==="text"||o.type==="password"||u==="select"||u==="textarea"||o.hasAttribute("contenteditable");if(!m){var v=window.getComputedStyle(o,null);m=isUserModifyWritable(v)}if(!m){return false}}if(u==="use"&&c!==null){if(l.is.BLINK||l.is.WEBKIT&&l.majorVersion===9){return true}}if(elementMatches(o,"svg a")&&o.hasAttribute("xlink:href")){if(f){return true}if(o.focus&&!Ie.focusSvgNegativeTabindexAttribute){return true}}if(u==="svg"&&Ie.focusSvgInIframe&&f){return true}if(l.is.TRIDENT||l.is.EDGE){if(u==="svg"){if(Ie.focusSvg){return true}return o.hasAttribute("focusable")||p}if(o.ownerSVGElement){if(Ie.focusSvgTabindexAttribute&&p){return true}return o.hasAttribute("focusable")}}if(o.tabIndex===undefined){return Boolean(n.onlyTabbable)}if(u==="audio"){if(!o.hasAttribute("controls")){return false}else if(l.is.BLINK){return true}}if(u==="video"){if(!o.hasAttribute("controls")){if(l.is.TRIDENT||l.is.EDGE){return false}}else if(l.is.BLINK||l.is.GECKO){return true}}if(u==="object"){if(l.is.BLINK||l.is.WEBKIT){return false}}if(u==="iframe"){return false}if(!n.scrollable&&l.is.GECKO){var b=window.getComputedStyle(o,null);if(hasCssOverflowScroll(b)){return f}}if(l.is.TRIDENT||l.is.EDGE){if(u==="area"){var g=getImageOfArea(o);if(g&&tabindexValue(g)<0){return false}}var h=window.getComputedStyle(o,null);if(isUserModifyWritable(h)){return o.tabIndex>=0}if(!n.flexbox&&hasCssDisplayFlex(h)){if(c!==null){return p}return Me(o)&&Le(o)}if(isScrollableContainer(o,u)){return false}var y=o.parentElement;if(y){var x=y.nodeName.toLowerCase();var _=window.getComputedStyle(y,null);if(isScrollableContainer(y,u,x,_)){return false}if(hasCssDisplayFlex(_)){return p}}}return o.tabIndex>=0}isTabbableRules.except=function(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{};var t=function isTabbable(t){return isTabbableRules({context:t,except:e})};t.rules=isTabbableRules;return t};var Me=ye.rules.except({flexbox:true});var Le=isTabbableRules.except({flexbox:true});var Be=isTabbableRules.except({});function queryTabbable(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.includeContext,n=e.includeOnlyTabbable,o=e.strategy;var a=Be.rules.except({onlyTabbable:n});return queryFocusable({context:t,includeContext:r,includeOnlyTabbable:n,strategy:o}).filter(a)}function compareDomPosition(e,t){return e.compareDocumentPosition(t)&Node.DOCUMENT_POSITION_FOLLOWING?-1:1}function sortDomOrder(e){return e.sort(compareDomPosition)}function getFirstSuccessorOffset(e,t){return findIndex(e,(function(e){return t.compareDocumentPosition(e)&Node.DOCUMENT_POSITION_FOLLOWING}))}function findInsertionOffsets(e,t,r){var n=[];t.forEach((function(t){var o=true;var a=e.indexOf(t);if(a===-1){a=getFirstSuccessorOffset(e,t);o=false}if(a===-1){a=e.length}var i=nodeArray(r?r(t):t);if(!i.length){return}n.push({offset:a,replace:o,elements:i})}));return n}function insertElementsAtOffsets(e,t){var r=0;t.sort((function(e,t){return e.offset-t.offset}));t.forEach((function(t){var n=t.replace?1:0;var o=[t.offset+r,n].concat(t.elements);e.splice.apply(e,o);r+=t.elements.length-n}))}function mergeInDomOrder(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.list,r=e.elements,n=e.resolveElement;var o=t.slice(0);var a=nodeArray(r).slice(0);sortDomOrder(a);var i=findInsertionOffsets(o,a,n);insertElementsAtOffsets(o,i);return o}var He=function(){function defineProperties(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||false;n.configurable=true;if("value"in n)n.writable=true;Object.defineProperty(e,n.key,n)}}return function(e,t,r){if(t)defineProperties(e.prototype,t);if(r)defineProperties(e,r);return e}}();function _classCallCheck(e,t){if(!(e instanceof t)){throw new TypeError("Cannot call a class as a function")}}var ze=function(){function Maps(e){_classCallCheck(this,Maps);this._document=getDocument(e);this.maps={}}He(Maps,[{key:"getAreasFor",value:function getAreasFor(e){if(!this.maps[e]){this.addMapByName(e)}return this.maps[e]}},{key:"addMapByName",value:function addMapByName(e){var t=getMapByName(e,this._document);if(!t){return}this.maps[t.name]=queryTabbable({context:t})}},{key:"extractAreasFromList",value:function extractAreasFromList(e){return e.filter((function(e){var t=e.nodeName.toLowerCase();if(t!=="area"){return true}var r=e.parentNode;if(!this.maps[r.name]){this.maps[r.name]=[]}this.maps[r.name].push(e);return false}),this)}}]);return Maps}();function sortArea(e,t){var r=t.querySelectorAll("img[usemap]");var n=new ze(t);var o=n.extractAreasFromList(e);if(!r.length){return o}return mergeInDomOrder({list:o,elements:r,resolveElement:function resolveElement(e){var t=e.getAttribute("usemap").slice(1);return n.getAreasFor(t)}})}var We=function(){function defineProperties(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||false;n.configurable=true;if("value"in n)n.writable=true;Object.defineProperty(e,n.key,n)}}return function(e,t,r){if(t)defineProperties(e.prototype,t);if(r)defineProperties(e,r);return e}}();function _classCallCheck$1(e,t){if(!(e instanceof t)){throw new TypeError("Cannot call a class as a function")}}var Ve=function(){function Shadows(e,t){_classCallCheck$1(this,Shadows);this.context=e;this.sortElements=t;this.hostCounter=1;this.inHost={};this.inDocument=[];this.hosts={};this.elements={}}We(Shadows,[{key:"_registerHost",value:function _registerHost(e){if(e._sortingId){return}e._sortingId="shadow-"+this.hostCounter++;this.hosts[e._sortingId]=e;var t=getShadowHost({context:e});if(t){this._registerHost(t);this._registerHostParent(e,t)}else{this.inDocument.push(e)}}},{key:"_registerHostParent",value:function _registerHostParent(e,t){if(!this.inHost[t._sortingId]){this.inHost[t._sortingId]=[]}this.inHost[t._sortingId].push(e)}},{key:"_registerElement",value:function _registerElement(e,t){if(!this.elements[t._sortingId]){this.elements[t._sortingId]=[]}this.elements[t._sortingId].push(e)}},{key:"extractElements",value:function extractElements(e){return e.filter((function(e){var t=getShadowHost({context:e});if(!t){return true}this._registerHost(t);this._registerElement(e,t);return false}),this)}},{key:"sort",value:function sort(e){var t=this._injectHosts(e);t=this._replaceHosts(t);this._cleanup();return t}},{key:"_injectHosts",value:function _injectHosts(e){Object.keys(this.hosts).forEach((function(e){var t=this.elements[e];var r=this.inHost[e];var n=this.hosts[e].shadowRoot;this.elements[e]=this._merge(t,r,n)}),this);return this._merge(e,this.inDocument,this.context)}},{key:"_merge",value:function _merge(e,t,r){var n=mergeInDomOrder({list:e,elements:t});return this.sortElements(n,r)}},{key:"_replaceHosts",value:function _replaceHosts(e){return mergeInDomOrder({list:e,elements:this.inDocument,resolveElement:this._resolveHostElement.bind(this)})}},{key:"_resolveHostElement",value:function _resolveHostElement(e){var t=mergeInDomOrder({list:this.elements[e._sortingId],elements:this.inHost[e._sortingId],resolveElement:this._resolveHostElement.bind(this)});var r=tabindexValue(e);if(r!==null&&r>-1){return[e].concat(t)}return t}},{key:"_cleanup",value:function _cleanup(){Object.keys(this.hosts).forEach((function(e){delete this.hosts[e]._sortingId}),this)}}]);return Shadows}();function sortShadowed(e,t,r){var n=new Ve(t,r);var o=n.extractElements(e);if(o.length===e.length){return r(e)}return n.sort(o)}function sortTabindex(e){var t={};var r=[];var n=e.filter((function(e){var n=e.tabIndex;if(n===undefined){n=tabindexValue(e)}if(n<=0||n===null||n===undefined){return true}if(!t[n]){t[n]=[];r.push(n)}t[n].push(e);return false}));var o=r.sort().map((function(e){return t[e]})).reduceRight((function(e,t){return t.concat(e)}),n);return o}var $e=void 0;function moveContextToBeginning(e,t){var r=e.indexOf(t);if(r>0){var n=e.splice(r,1);return n.concat(e)}return e}function sortElements(e,t){if($e.tabsequenceAreaAtImgPosition){e=sortArea(e,t)}e=sortTabindex(e);return e}function queryTabsequence(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.context,r=e.includeContext,n=e.includeOnlyTabbable,o=e.strategy;if(!$e){$e=_supports()}var a=nodeArray(t)[0]||document.documentElement;var i=queryTabbable({context:a,includeContext:r,includeOnlyTabbable:n,strategy:o});if(document.body.createShadowRoot&&l.is.BLINK){i=sortShadowed(i,a,sortElements)}else{i=sortElements(i,a)}if(r){i=moveContextToBeginning(i,a)}return i}var qe={tab:9,left:37,up:38,right:39,down:40,pageUp:33,"page-up":33,pageDown:34,"page-down":34,end:35,home:36,enter:13,escape:27,space:32,shift:16,capsLock:20,"caps-lock":20,ctrl:17,alt:18,meta:91,pause:19,insert:45,delete:46,backspace:8,_alias:{91:[92,93,224]}};for(var Ue=1;Ue<26;Ue++){qe["f"+Ue]=Ue+111}for(var Ke=0;Ke<10;Ke++){var Ge=Ke+48;var Ze=Ke+96;qe[Ke]=Ge;qe["num-"+Ke]=Ze;qe._alias[Ge]=[Ze]}for(var Ye=0;Ye<26;Ye++){var Je=Ye+65;var Xe=String.fromCharCode(Je).toLowerCase();qe[Xe]=Je}var Qe={alt:"altKey",ctrl:"ctrlKey",meta:"metaKey",shift:"shiftKey"};var et=Object.keys(Qe).map((function(e){return Qe[e]}));function createExpectedModifiers(e){var t=e?null:false;return{altKey:t,ctrlKey:t,metaKey:t,shiftKey:t}}function resolveModifiers(e){var t=e.indexOf("*")!==-1;var r=createExpectedModifiers(t);e.forEach((function(e){if(e==="*"){return}var t=true;var n=e.slice(0,1);if(n==="?"){t=null}else if(n==="!"){t=false}if(t!==true){e=e.slice(1)}var o=Qe[e];if(!o){throw new TypeError('Unknown modifier "'+e+'"')}r[o]=t}));return r}function resolveKey(e){var t=qe[e]||parseInt(e,10);if(!t||typeof t!=="number"||isNaN(t)){throw new TypeError('Unknown key "'+e+'"')}return[t].concat(qe._alias[t]||[])}function matchModifiers(e,t){return!et.some((function(r){return typeof e[r]==="boolean"&&Boolean(t[r])!==e[r]}))}function keyBinding(e){return e.split(/\s+/).map((function(e){var t=e.split("+");var r=resolveModifiers(t.slice(0,-1));var n=resolveKey(t.slice(-1));return{keyCodes:n,modifiers:r,matchModifiers:matchModifiers.bind(null,r)}}))}function getParentComparator(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{},t=e.parent,r=e.element,n=e.includeSelf;if(t){return function isChildOf(e){return Boolean(n&&e===t||t.compareDocumentPosition(e)&Node.DOCUMENT_POSITION_CONTAINED_BY)}}else if(r){return function isParentOf(e){return Boolean(n&&r===e||e.compareDocumentPosition(r)&Node.DOCUMENT_POSITION_CONTAINED_BY)}}throw new TypeError("util/compare-position#getParentComparator required either options.parent or options.element")}function whenKey(){var e=arguments.length>0&&arguments[0]!==undefined?arguments[0]:{};var t={};var r=nodeArray(e.context)[0]||document.documentElement;delete e.context;var n=nodeArray(e.filter);delete e.filter;var o=Object.keys(e);if(!o.length){throw new TypeError("when/key requires at least one option key")}var a=function registerBinding(e){e.keyCodes.forEach((function(r){if(!t[r]){t[r]=[]}t[r].push(e)}))};o.forEach((function(t){if(typeof e[t]!=="function"){throw new TypeError('when/key requires option["'+t+'"] to be a function')}var r=function addCallback(r){r.callback=e[t];return r};keyBinding(t).map(r).forEach(a)}));var i=function handleKeyDown(e){if(e.defaultPrevented){return}if(n.length){var o=getParentComparator({element:e.target,includeSelf:true});if(n.some(o)){return}}var a=e.keyCode||e.which;if(!t[a]){return}t[a].forEach((function(t){if(!t.matchModifiers(e)){return}t.callback.call(r,e,s)}))};r.addEventListener("keydown",i,false);var s=function disengage(){r.removeEventListener("keydown",i,false)};return{disengage:s}}function default_1({context:e}={}){if(!e){e=document.documentElement}queryTabsequence();return whenKey({"?alt+?shift+tab":function altShiftTab(t){t.preventDefault();var r=queryTabsequence({context:e});var n=t.shiftKey;var o=r[0];var a=r[r.length-1];var i=n?o:a;var s=n?a:o;if(isActiveElement(i)){s.focus();return}var l=void 0;var u=r.some((function(e,t){if(!isActiveElement(e)){return false}l=t;return true}));if(!u){o.focus();return}var c=n?-1:1;r[l+c].focus()}})}t["default"]=default_1},993:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.styles=void 0;const n=r(8910);const o=(0,n.noop)`
  [data-nextjs-dialog-overlay] {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    overflow: auto;
    z-index: 9000;

    display: flex;
    align-content: center;
    align-items: center;
    flex-direction: column;
    padding: 10vh 15px 0;
  }

  @media (max-height: 812px) {
    [data-nextjs-dialog-overlay] {
      padding: 15px 15px 0;
    }
  }

  [data-nextjs-dialog-backdrop] {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: var(--color-backdrop);
    pointer-events: all;
    z-index: -1;
  }

  [data-nextjs-dialog-backdrop-fixed] {
    cursor: not-allowed;
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
  }
`;t.styles=o},6338:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};Object.defineProperty(t,"__esModule",{value:true});t.ShadowPortal=void 0;const i=r(505);const s=a(r(7522));const l=r(2255);const u=function Portal({children:e,globalOverlay:t}){let r=s.useRef(null);let n=s.useRef(null);let o=s.useRef(null);let[,a]=s.useState();s.useLayoutEffect((()=>{const e=t?document:r.current.ownerDocument;n.current=e.createElement("nextjs-portal");o.current=n.current.attachShadow({mode:"open"});e.body.appendChild(n.current);a({});return()=>{if(n.current&&n.current.ownerDocument){n.current.ownerDocument.body.removeChild(n.current)}}}),[t]);return o.current?(0,l.createPortal)(e,o.current):t?null:(0,i.jsx)("span",{ref:r})};t.ShadowPortal=u},7215:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};var i=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:true});t.Terminal=void 0;const s=r(505);const l=i(r(7997));const u=a(r(7522));const c=function Terminal({content:e}){const t=u.useMemo((()=>l.default.ansiToJson(e,{json:true,use_classes:true,remove_empty:true})),[e]);return(0,s.jsx)("div",{"data-nextjs-terminal":true,children:(0,s.jsx)("pre",{children:t.map(((e,t)=>(0,s.jsx)("span",{style:{color:e.fg?`var(--color-${e.fg})`:undefined,...e.decoration==="bold"?{fontWeight:800}:e.decoration==="italic"?{fontStyle:"italic"}:undefined},children:e.content},`terminal-entry-${t}`)))})})};t.Terminal=c},8236:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.Terminal=void 0;var n=r(7215);Object.defineProperty(t,"Terminal",{enumerable:true,get:function(){return n.Terminal}})},5488:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.styles=void 0;const n=r(8910);const o=(0,n.noop)`
  [data-nextjs-terminal] {
    border-radius: var(--size-gap-half);
    background-color: var(--color-ansi-bg);
    color: var(--color-ansi-fg);
  }
  [data-nextjs-terminal]::selection,
  [data-nextjs-terminal] *::selection {
    background-color: var(--color-ansi-selection);
  }
  [data-nextjs-terminal] * {
    color: inherit;
    background-color: transparent;
    font-family: var(--font-stack-monospace);
  }
  [data-nextjs-terminal] > * {
    margin: 0;
    padding: calc(var(--size-gap) + var(--size-gap-half))
      calc(var(--size-gap-double) + var(--size-gap-half));
  }

  [data-nextjs-terminal] pre {
    white-space: pre-wrap;
    word-break: break-word;
  }
`;t.styles=o},9683:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.Toast=void 0;const n=r(505);const o=function Toast({onClick:e,children:t,className:r}){return(0,n.jsx)("div",{"data-nextjs-toast":true,onClick:e,className:r,children:(0,n.jsx)("div",{"data-nextjs-toast-wrapper":true,children:t})})};t.Toast=o},1120:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.Toast=t.styles=void 0;var n=r(2069);Object.defineProperty(t,"styles",{enumerable:true,get:function(){return n.styles}});var o=r(9683);Object.defineProperty(t,"Toast",{enumerable:true,get:function(){return o.Toast}})},2069:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.styles=void 0;const n=r(8910);const o=(0,n.noop)`
  [data-nextjs-toast] {
    position: fixed;
    bottom: var(--size-gap-double);
    left: var(--size-gap-double);
    max-width: 420px;
    z-index: 9000;
  }

  @media (max-width: 440px) {
    [data-nextjs-toast] {
      max-width: 90vw;
      left: 5vw;
    }
  }

  [data-nextjs-toast-wrapper] {
    padding: 16px;
    border-radius: var(--size-gap-half);
    font-weight: 500;
    color: var(--color-ansi-bright-white);
    background-color: var(--color-ansi-red);
    box-shadow: 0px var(--size-gap-double) var(--size-gap-quad)
      rgba(0, 0, 0, 0.25);
  }
`;t.styles=o},5936:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};Object.defineProperty(t,"__esModule",{value:true});t.styles=t.BuildError=void 0;const i=r(505);const s=a(r(7522));const l=r(5651);const u=r(8278);const c=r(8236);const d=r(8910);const f=function BuildError({message:e}){const t=s.useCallback((()=>{}),[]);return(0,i.jsx)(u.Overlay,{fixed:true,children:(0,i.jsx)(l.Dialog,{type:"error","aria-labelledby":"nextjs__container_build_error_label","aria-describedby":"nextjs__container_build_error_desc",onClose:t,children:(0,i.jsxs)(l.DialogContent,{children:[(0,i.jsx)(l.DialogHeader,{className:"nextjs-container-build-error-header",children:(0,i.jsx)("h4",{id:"nextjs__container_build_error_label",children:"Failed to compile"})}),(0,i.jsxs)(l.DialogBody,{className:"nextjs-container-build-error-body",children:[(0,i.jsx)(c.Terminal,{content:e}),(0,i.jsx)("footer",{children:(0,i.jsx)("p",{id:"nextjs__container_build_error_desc",children:(0,i.jsx)("small",{children:"This error occurred during the build process and can only be dismissed by fixing the error."})})})]})]})})})};t.BuildError=f;t.styles=(0,d.noop)`
  .nextjs-container-build-error-header > h4 {
    line-height: 1.5;
    margin: 0;
    padding: 0;
  }

  .nextjs-container-build-error-body footer {
    margin-top: var(--size-gap);
  }
  .nextjs-container-build-error-body footer p {
    margin: 0;
  }

  .nextjs-container-build-error-body small {
    color: var(--color-font);
  }
`},4355:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};Object.defineProperty(t,"__esModule",{value:true});t.styles=t.Errors=void 0;const i=r(505);const s=a(r(7522));const l=r(5851);const u=r(5651);const c=r(2732);const d=r(8278);const f=r(1120);const p=r(403);const m=r(5233);const v=r(8910);const b=r(865);const g=r(2484);function getErrorSignature(e){const{event:t}=e;switch(t.type){case l.TYPE_UNHANDLED_ERROR:case l.TYPE_UNHANDLED_REJECTION:{return`${t.reason.name}::${t.reason.message}::${t.reason.stack}`}default:{}}const r=t;return""}const h=function HotlinkedText(e){const{text:t}=e;const r=/https?:\/\/[^\s/$.?#].[^\s)'"]*/i;return(0,i.jsx)(i.Fragment,{children:r.test(t)?t.split(" ").map(((e,t,n)=>{if(r.test(e)){const o=r.exec(e);return(0,i.jsxs)(s.Fragment,{children:[o&&(0,i.jsx)("a",{href:o[0],target:"_blank",rel:"noreferrer noopener",children:e}),t===n.length-1?"":" "]},`link-${t}`)}return t===n.length-1?(0,i.jsx)(s.Fragment,{children:e},`text-${t}`):(0,i.jsxs)(s.Fragment,{children:[e," "]},`text-${t}`)})):t})};const y=function Errors({errors:e}){const[t,r]=s.useState({});const[n,o]=s.useMemo((()=>{let r=[];let n=null;for(let o=0;o<e.length;++o){const a=e[o];const{id:i}=a;if(i in t){r.push(t[i]);continue}if(o>0){const t=e[o-1];if(getErrorSignature(t)===getErrorSignature(a)){continue}}n=a;break}return[r,n]}),[e,t]);const a=s.useMemo((()=>n.length<1&&Boolean(e.length)),[e.length,n.length]);s.useEffect((()=>{if(o==null){return}let e=true;(0,p.getErrorByType)(o).then((t=>{if(e){r((e=>({...e,[t.id]:t})))}}),(()=>{}));return()=>{e=false}}),[o]);const[l,v]=s.useState("fullscreen");const[y,x]=s.useState(0);const _=s.useCallback((e=>{e?.preventDefault();x((e=>Math.max(0,e-1)))}),[]);const w=s.useCallback((e=>{e?.preventDefault();x((e=>Math.max(0,Math.min(n.length-1,e+1))))}),[n.length]);const E=s.useMemo((()=>n[y]??null),[y,n]);s.useEffect((()=>{if(e.length<1){r({});v("hidden");x(0)}}),[e.length]);const j=s.useCallback((e=>{e?.preventDefault();v("minimized")}),[]);const O=s.useCallback((e=>{e?.preventDefault();v("hidden")}),[]);const k=s.useCallback((e=>{e?.preventDefault();v("fullscreen")}),[]);if(e.length<1||E==null){return null}if(a){return(0,i.jsx)(d.Overlay,{})}if(l==="hidden"){return null}if(l==="minimized"){return(0,i.jsx)(f.Toast,{className:"nextjs-toast-errors-parent",onClick:k,children:(0,i.jsxs)("div",{className:"nextjs-toast-errors",children:[(0,i.jsxs)("svg",{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,i.jsx)("circle",{cx:"12",cy:"12",r:"10"}),(0,i.jsx)("line",{x1:"12",y1:"8",x2:"12",y2:"12"}),(0,i.jsx)("line",{x1:"12",y1:"16",x2:"12.01",y2:"16"})]}),(0,i.jsxs)("span",{children:[n.length," error",n.length>1?"s":""]}),(0,i.jsx)("button",{"data-nextjs-toast-errors-hide-button":true,className:"nextjs-toast-errors-hide-button",type:"button",onClick:e=>{e.stopPropagation();O()},"aria-label":"Hide Errors",children:(0,i.jsx)(b.CloseIcon,{})})]})})}const S=["server","edge-server"].includes((0,m.getErrorSource)(E.error)||"");return(0,i.jsx)(d.Overlay,{children:(0,i.jsx)(u.Dialog,{type:"error","aria-labelledby":"nextjs__container_errors_label","aria-describedby":"nextjs__container_errors_desc",onClose:S?undefined:j,children:(0,i.jsxs)(u.DialogContent,{children:[(0,i.jsxs)(u.DialogHeader,{className:"nextjs-container-errors-header",children:[(0,i.jsx)(c.LeftRightDialogHeader,{previous:y>0?_:null,next:y<n.length-1?w:null,close:S?undefined:j,children:(0,i.jsxs)("small",{children:[(0,i.jsx)("span",{children:y+1})," of"," ",(0,i.jsx)("span",{children:n.length})," unhandled error",n.length<2?"":"s"]})}),(0,i.jsx)("h1",{id:"nextjs__container_errors_label",children:S?"Server Error":"Unhandled Runtime Error"}),(0,i.jsxs)("p",{id:"nextjs__container_errors_desc",children:[E.error.name,":"," ",(0,i.jsx)(h,{text:E.error.message})]}),S?(0,i.jsx)("div",{children:(0,i.jsx)("small",{children:"This error happened while generating the page. Any console logs will be displayed in the terminal window."})}):undefined]}),(0,i.jsx)(u.DialogBody,{className:"nextjs-container-errors-body",children:(0,i.jsx)(g.RuntimeError,{error:E},E.id.toString())})]})})})};t.Errors=y;t.styles=(0,v.noop)`
  .nextjs-container-errors-header > h1 {
    font-size: var(--size-font-big);
    line-height: var(--size-font-bigger);
    font-weight: bold;
    margin: 0;
    margin-top: calc(var(--size-gap-double) + var(--size-gap-half));
  }
  .nextjs-container-errors-header small {
    font-size: var(--size-font-small);
    color: var(--color-accents-1);
    margin-left: var(--size-gap-double);
  }
  .nextjs-container-errors-header small > span {
    font-family: var(--font-stack-monospace);
  }
  .nextjs-container-errors-header > p {
    font-family: var(--font-stack-monospace);
    font-size: var(--size-font-small);
    line-height: var(--size-font-big);
    font-weight: bold;
    margin: 0;
    margin-top: var(--size-gap-half);
    color: var(--color-ansi-red);
    white-space: pre-wrap;
  }
  .nextjs-container-errors-header > div > small {
    margin: 0;
    margin-top: var(--size-gap-half);
  }
  .nextjs-container-errors-header > p > a {
    color: var(--color-ansi-red);
  }

  .nextjs-container-errors-body > h2:not(:first-child) {
    margin-top: calc(var(--size-gap-double) + var(--size-gap));
  }
  .nextjs-container-errors-body > h2 {
    margin-bottom: var(--size-gap);
    font-size: var(--size-font-big);
  }

  .nextjs-toast-errors-parent {
    cursor: pointer;
    transition: transform 0.2s ease;
  }
  .nextjs-toast-errors-parent:hover {
    transform: scale(1.1);
  }
  .nextjs-toast-errors {
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }
  .nextjs-toast-errors > svg {
    margin-right: var(--size-gap);
  }
  .nextjs-toast-errors-hide-button {
    margin-left: var(--size-gap-triple);
    border: none;
    background: none;
    color: var(--color-ansi-bright-white);
    padding: 0;
    transition: opacity 0.25s ease;
    opacity: 0.7;
  }
  .nextjs-toast-errors-hide-button:hover {
    opacity: 1;
  }
`},2484:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};Object.defineProperty(t,"__esModule",{value:true});t.RuntimeError=t.styles=void 0;const i=r(505);const s=a(r(7522));const l=r(1413);const u=r(8910);const c=r(7504);const d=function CallStackFrame({frame:e}){const t=e.originalStackFrame??e.sourceStackFrame;const r=Boolean(e.originalCodeFrame);const n=s.useCallback((()=>{if(!r)return;const e=new URLSearchParams;for(const r in t){e.append(r,(t[r]??"").toString())}self.fetch(`${process.env.__NEXT_ROUTER_BASEPATH||""}/__nextjs_launch-editor?${e.toString()}`).then((()=>{}),(()=>{console.error("There was an issue opening this code in your editor.")}))}),[r,t]);return(0,i.jsxs)("div",{"data-nextjs-call-stack-frame":true,children:[(0,i.jsx)("h3",{"data-nextjs-frame-expanded":Boolean(e.expanded),children:t.methodName}),(0,i.jsxs)("div",{"data-has-source":r?"true":undefined,tabIndex:r?10:undefined,role:r?"link":undefined,onClick:n,title:r?"Click to open in your editor":undefined,children:[(0,i.jsx)("span",{children:(0,c.getFrameSource)(t)}),(0,i.jsxs)("svg",{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,i.jsx)("path",{d:"M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"}),(0,i.jsx)("polyline",{points:"15 3 21 3 21 9"}),(0,i.jsx)("line",{x1:"10",y1:"14",x2:"21",y2:"3"})]})]})]})};const f=function RuntimeError({error:e}){const t=s.useMemo((()=>e.frames.findIndex((e=>e.expanded&&Boolean(e.originalCodeFrame)&&Boolean(e.originalStackFrame)))),[e.frames]);const r=s.useMemo((()=>e.frames[t]??null),[e.frames,t]);const n=s.useMemo((()=>t<0?[]:e.frames.slice(0,t)),[e.frames,t]);const[o,a]=s.useState(r==null);const u=s.useCallback((()=>{a((e=>!e))}),[]);const c=s.useMemo((()=>n.filter((e=>e.expanded||o))),[o,n]);const f=s.useMemo((()=>e.frames.slice(t+1)),[e.frames,t]);const p=s.useMemo((()=>f.filter((e=>e.expanded||o))),[o,f]);const m=s.useMemo((()=>f.length!==p.length||o&&r!=null),[o,f.length,r,p.length]);return(0,i.jsxs)(s.Fragment,{children:[r?(0,i.jsxs)(s.Fragment,{children:[(0,i.jsx)("h2",{children:"Source"}),c.map(((e,t)=>(0,i.jsx)(d,{frame:e},`leading-frame-${t}-${o}`))),(0,i.jsx)(l.CodeFrame,{stackFrame:r.originalStackFrame,codeFrame:r.originalCodeFrame})]}):undefined,e.componentStack?(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)("h2",{children:"Component Stack"}),e.componentStack.map(((e,t)=>(0,i.jsx)("div",{"data-nextjs-component-stack-frame":true,children:(0,i.jsx)("h3",{children:e})},t)))]}):null,p.length?(0,i.jsxs)(s.Fragment,{children:[(0,i.jsx)("h2",{children:"Call Stack"}),p.map(((e,t)=>(0,i.jsx)(d,{frame:e},`call-stack-${t}-${o}`)))]}):undefined,m?(0,i.jsx)(s.Fragment,{children:(0,i.jsxs)("button",{tabIndex:10,"data-nextjs-data-runtime-error-collapsed-action":true,type:"button",onClick:u,children:[o?"Hide":"Show"," collapsed frames"]})}):undefined]})};t.RuntimeError=f;t.styles=(0,u.noop)`
  button[data-nextjs-data-runtime-error-collapsed-action] {
    background: none;
    border: none;
    padding: 0;
    font-size: var(--size-font-small);
    line-height: var(--size-font-bigger);
    color: var(--color-accents-3);
  }

  [data-nextjs-call-stack-frame]:not(:last-child),
  [data-nextjs-component-stack-frame]:not(:last-child) {
    margin-bottom: var(--size-gap-double);
  }

  [data-nextjs-call-stack-frame] > h3,
  [data-nextjs-component-stack-frame] > h3 {
    margin-top: 0;
    margin-bottom: var(--size-gap);
    font-family: var(--font-stack-monospace);
    color: var(--color-stack-h6);
  }
  [data-nextjs-call-stack-frame] > h3[data-nextjs-frame-expanded='false'] {
    color: var(--color-stack-headline);
  }
  [data-nextjs-call-stack-frame] > div {
    display: flex;
    align-items: center;
    padding-left: calc(var(--size-gap) + var(--size-gap-half));
    font-size: var(--size-font-small);
    color: var(--color-stack-subline);
  }
  [data-nextjs-call-stack-frame] > div > svg {
    width: auto;
    height: var(--size-font-small);
    margin-left: var(--size-gap);

    display: none;
  }

  [data-nextjs-call-stack-frame] > div[data-has-source] {
    cursor: pointer;
  }
  [data-nextjs-call-stack-frame] > div[data-has-source]:hover {
    text-decoration: underline dotted;
  }
  [data-nextjs-call-stack-frame] > div[data-has-source] > svg {
    display: unset;
  }
`},403:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.getErrorByType=void 0;const n=r(5851);const o=r(5233);const a=r(7504);async function getErrorByType(e){const{id:t,event:r}=e;switch(r.type){case n.TYPE_UNHANDLED_ERROR:case n.TYPE_UNHANDLED_REJECTION:{const e={id:t,runtime:true,error:r.reason,frames:await(0,a.getOriginalStackFrames)(r.frames,(0,o.getErrorSource)(r.reason),r.reason.toString())};if(r.type===n.TYPE_UNHANDLED_ERROR){e.componentStack=r.componentStack}return e}default:{break}}const i=r;throw new Error("type system invariant violation")}t.getErrorByType=getErrorByType},5233:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.getServerError=t.decorateServerError=t.getErrorSource=t.getFilesystemFrame=void 0;const n=r(5974);function getFilesystemFrame(e){const t={...e};if(typeof t.file==="string"){if(t.file.startsWith("/")||/^[a-z]:\\/i.test(t.file)||t.file.startsWith("\\\\")){t.file=`file://${t.file}`}}return t}t.getFilesystemFrame=getFilesystemFrame;const o=Symbol("NextjsError");function getErrorSource(e){return e[o]||null}t.getErrorSource=getErrorSource;function decorateServerError(e,t){Object.defineProperty(e,o,{writable:false,enumerable:false,configurable:false,value:t})}t.decorateServerError=decorateServerError;function getServerError(e,t){let r;try{throw new Error(e.message)}catch(e){r=e}r.name=e.name;try{r.stack=`${r.toString()}\n${(0,n.parse)(e.stack).map(getFilesystemFrame).map((e=>{let t=`    at ${e.methodName}`;if(e.file){let r=e.file;if(e.lineNumber){r+=`:${e.lineNumber}`;if(e.column){r+=`:${e.column}`}}t+=` (${r})`}return t})).join("\n")}`}catch{r.stack=e.stack}decorateServerError(r,t);return r}t.getServerError=getServerError},8910:function(e,t){Object.defineProperty(t,"__esModule",{value:true});t.noop=void 0;function noop(e,...t){const r=e.length-1;return e.slice(0,r).reduce(((e,r,n)=>e+r+t[n]),"")+e[r]}t.noop=noop},636:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.parseStack=void 0;const n=r(5974);const o=/\/_next(\/static\/.+)/;function parseStack(e){const t=(0,n.parse)(e);return t.map((e=>{try{const t=new URL(e.file);const r=o.exec(t.pathname);if(r){const t=process.env.__NEXT_DIST_DIR?.replace(/\\/g,"/")?.replace(/\/$/,"");if(t){e.file="file://"+t.concat(r.pop())}}}catch{}return e}))}t.parseStack=parseStack},7504:function(e,t){Object.defineProperty(t,"__esModule",{value:true});t.getFrameSource=t.getOriginalStackFrames=t.getOriginalStackFrame=void 0;function getOriginalStackFrame(e,t,r){async function _getOriginalStackFrame(){const n=new URLSearchParams;n.append("isServer",String(t==="server"));n.append("isEdgeServer",String(t==="edge-server"));n.append("errorMessage",r);for(const t in e){n.append(t,(e[t]??"").toString())}const o=new AbortController;const a=setTimeout((()=>o.abort()),3e3);const i=await self.fetch(`${process.env.__NEXT_ROUTER_BASEPATH||""}/__nextjs_original-stack-frame?${n.toString()}`,{signal:o.signal}).finally((()=>{clearTimeout(a)}));if(!i.ok||i.status===204){return Promise.reject(new Error(await i.text()))}const s=await i.json();return{error:false,reason:null,external:false,expanded:!Boolean((e.file?.includes("node_modules")||s.originalStackFrame?.file?.includes("node_modules"))??true),sourceStackFrame:e,originalStackFrame:s.originalStackFrame,originalCodeFrame:s.originalCodeFrame||null}}if(!(e.file?.startsWith("webpack-internal:")||e.file?.startsWith("file:"))){return Promise.resolve({error:false,reason:null,external:true,expanded:false,sourceStackFrame:e,originalStackFrame:null,originalCodeFrame:null})}return _getOriginalStackFrame().catch((t=>({error:true,reason:t?.message??t?.toString()??"Unknown Error",external:false,expanded:false,sourceStackFrame:e,originalStackFrame:null,originalCodeFrame:null})))}t.getOriginalStackFrame=getOriginalStackFrame;function getOriginalStackFrames(e,t,r){return Promise.all(e.map((e=>getOriginalStackFrame(e,t,r))))}t.getOriginalStackFrames=getOriginalStackFrames;function getFrameSource(e){let t="";try{const r=new URL(e.file);if(typeof globalThis!=="undefined"&&globalThis.location?.origin!==r.origin){if(r.origin==="null"){t+=r.protocol}else{t+=r.origin}}t+=r.pathname;t+=" "}catch{t+=(e.file||"(unknown)")+" "}if(e.lineNumber!=null){if(e.column!=null){t+=`(${e.lineNumber}:${e.column}) `}else{t+=`(${e.lineNumber}) `}}return t.slice(0,-1)}t.getFrameSource=getFrameSource},7169:function(e,t,r){var n=this&&this.__createBinding||(Object.create?function(e,t,r,n){if(n===undefined)n=r;var o=Object.getOwnPropertyDescriptor(t,r);if(!o||("get"in o?!t.__esModule:o.writable||o.configurable)){o={enumerable:true,get:function(){return t[r]}}}Object.defineProperty(e,n,o)}:function(e,t,r,n){if(n===undefined)n=r;e[n]=t[r]});var o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t});var a=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var r in e)if(r!=="default"&&Object.prototype.hasOwnProperty.call(e,r))n(t,e,r);o(t,e);return t};Object.defineProperty(t,"__esModule",{value:true});t.useOnClickOutside=void 0;const i=a(r(7522));function useOnClickOutside(e,t){i.useEffect((()=>{if(e==null||t==null){return}const listener=r=>{if(!e||e.contains(r.target)){return}t(r)};const r=e.getRootNode();r.addEventListener("mousedown",listener);r.addEventListener("touchstart",listener);return function(){r.removeEventListener("mousedown",listener);r.removeEventListener("touchstart",listener)}}),[t,e])}t.useOnClickOutside=useOnClickOutside},865:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.CloseIcon=void 0;const n=r(505);const CloseIcon=()=>(0,n.jsxs)("svg",{width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[(0,n.jsx)("path",{d:"M18 6L6 18",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round"}),(0,n.jsx)("path",{d:"M6 6L18 18",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round"})]});t.CloseIcon=CloseIcon},884:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.Base=void 0;const n=r(505);const o=r(8910);function Base(){return(0,n.jsx)("style",{children:(0,o.noop)`
        :host {
          --size-gap-half: 4px;
          --size-gap: 8px;
          --size-gap-double: 16px;
          --size-gap-triple: 24px;
          --size-gap-quad: 32px;

          --size-font-small: 14px;
          --size-font: 16px;
          --size-font-big: 20px;
          --size-font-bigger: 24px;

          --color-background: white;
          --color-font: #757575;
          --color-backdrop: rgba(17, 17, 17, 0.2);

          --color-stack-h6: #222;
          --color-stack-headline: #666;
          --color-stack-subline: #999;

          --color-accents-1: #808080;
          --color-accents-2: #222222;
          --color-accents-3: #404040;

          --font-stack-monospace: 'SFMono-Regular', Consolas, 'Liberation Mono',
            Menlo, Courier, monospace;

          --color-ansi-selection: rgba(95, 126, 151, 0.48);
          --color-ansi-bg: #111111;
          --color-ansi-fg: #cccccc;

          --color-ansi-white: #777777;
          --color-ansi-black: #141414;
          --color-ansi-blue: #00aaff;
          --color-ansi-cyan: #88ddff;
          --color-ansi-green: #98ec65;
          --color-ansi-magenta: #aa88ff;
          --color-ansi-red: #ff5555;
          --color-ansi-yellow: #ffcc33;
          --color-ansi-bright-white: #ffffff;
          --color-ansi-bright-black: #777777;
          --color-ansi-bright-blue: #33bbff;
          --color-ansi-bright-cyan: #bbecff;
          --color-ansi-bright-green: #b6f292;
          --color-ansi-bright-magenta: #cebbff;
          --color-ansi-bright-red: #ff8888;
          --color-ansi-bright-yellow: #ffd966;
        }

        @media (prefers-color-scheme: dark) {
          :host {
            --color-background: rgb(28, 28, 30);
            --color-font: white;
            --color-backdrop: rgb(44, 44, 46);

            --color-stack-h6: rgb(200, 200, 204);
            --color-stack-headline: rgb(99, 99, 102);
            --color-stack-subline: rgba(142, 142, 147);

            --color-accents-3: rgb(118, 118, 118);
          }
        }

        .mono {
          font-family: var(--font-stack-monospace);
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
          margin-bottom: var(--size-gap);
          font-weight: 500;
          line-height: 1.5;
        }
      `})}t.Base=Base},4464:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.ComponentStyles=void 0;const n=r(505);const o=r(399);const a=r(5651);const i=r(6543);const s=r(993);const l=r(5488);const u=r(1120);const c=r(5936);const d=r(4355);const f=r(2484);const p=r(8910);function ComponentStyles(){return(0,n.jsx)("style",{children:(0,p.noop)`
        ${s.styles}
        ${u.styles}
        ${a.styles}
        ${i.styles}
        ${o.styles}
        ${l.styles}
        
        ${c.styles}
        ${d.styles}
        ${f.styles}
      `})}t.ComponentStyles=ComponentStyles},9495:function(e,t,r){Object.defineProperty(t,"__esModule",{value:true});t.CssReset=void 0;const n=r(505);const o=r(8910);function CssReset(){return(0,n.jsx)("style",{children:(0,o.noop)`
        :host {
          all: initial;

          /* the direction property is not reset by 'all' */
          direction: ltr;
        }

        /*!
         * Bootstrap Reboot v4.4.1 (https://getbootstrap.com/)
         * Copyright 2011-2019 The Bootstrap Authors
         * Copyright 2011-2019 Twitter, Inc.
         * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
         * Forked from Normalize.css, licensed MIT (https://github.com/necolas/normalize.css/blob/master/LICENSE.md)
         */
        *,
        *::before,
        *::after {
          box-sizing: border-box;
        }

        :host {
          font-family: sans-serif;
          line-height: 1.15;
          -webkit-text-size-adjust: 100%;
          -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        }

        article,
        aside,
        figcaption,
        figure,
        footer,
        header,
        hgroup,
        main,
        nav,
        section {
          display: block;
        }

        :host {
          margin: 0;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
            'Helvetica Neue', Arial, 'Noto Sans', sans-serif,
            'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol',
            'Noto Color Emoji';
          font-size: 16px;
          font-weight: 400;
          line-height: 1.5;
          color: var(--color-font);
          text-align: left;
          background-color: #fff;
        }

        [tabindex='-1']:focus:not(:focus-visible) {
          outline: 0 !important;
        }

        hr {
          box-sizing: content-box;
          height: 0;
          overflow: visible;
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
          margin-top: 0;
          margin-bottom: 8px;
        }

        p {
          margin-top: 0;
          margin-bottom: 16px;
        }

        abbr[title],
        abbr[data-original-title] {
          text-decoration: underline;
          -webkit-text-decoration: underline dotted;
          text-decoration: underline dotted;
          cursor: help;
          border-bottom: 0;
          -webkit-text-decoration-skip-ink: none;
          text-decoration-skip-ink: none;
        }

        address {
          margin-bottom: 16px;
          font-style: normal;
          line-height: inherit;
        }

        ol,
        ul,
        dl {
          margin-top: 0;
          margin-bottom: 16px;
        }

        ol ol,
        ul ul,
        ol ul,
        ul ol {
          margin-bottom: 0;
        }

        dt {
          font-weight: 700;
        }

        dd {
          margin-bottom: 8px;
          margin-left: 0;
        }

        blockquote {
          margin: 0 0 16px;
        }

        b,
        strong {
          font-weight: bolder;
        }

        small {
          font-size: 80%;
        }

        sub,
        sup {
          position: relative;
          font-size: 75%;
          line-height: 0;
          vertical-align: baseline;
        }

        sub {
          bottom: -0.25em;
        }

        sup {
          top: -0.5em;
        }

        a {
          color: #007bff;
          text-decoration: none;
          background-color: transparent;
        }

        a:hover {
          color: #0056b3;
          text-decoration: underline;
        }

        a:not([href]) {
          color: inherit;
          text-decoration: none;
        }

        a:not([href]):hover {
          color: inherit;
          text-decoration: none;
        }

        pre,
        code,
        kbd,
        samp {
          font-family: SFMono-Regular, Menlo, Monaco, Consolas,
            'Liberation Mono', 'Courier New', monospace;
          font-size: 1em;
        }

        pre {
          margin-top: 0;
          margin-bottom: 16px;
          overflow: auto;
        }

        figure {
          margin: 0 0 16px;
        }

        img {
          vertical-align: middle;
          border-style: none;
        }

        svg {
          overflow: hidden;
          vertical-align: middle;
        }

        table {
          border-collapse: collapse;
        }

        caption {
          padding-top: 12px;
          padding-bottom: 12px;
          color: #6c757d;
          text-align: left;
          caption-side: bottom;
        }

        th {
          text-align: inherit;
        }

        label {
          display: inline-block;
          margin-bottom: 8px;
        }

        button {
          border-radius: 0;
        }

        button:focus {
          outline: 1px dotted;
          outline: 5px auto -webkit-focus-ring-color;
        }

        input,
        button,
        select,
        optgroup,
        textarea {
          margin: 0;
          font-family: inherit;
          font-size: inherit;
          line-height: inherit;
        }

        button,
        input {
          overflow: visible;
        }

        button,
        select {
          text-transform: none;
        }

        select {
          word-wrap: normal;
        }

        button,
        [type='button'],
        [type='reset'],
        [type='submit'] {
          -webkit-appearance: button;
        }

        button:not(:disabled),
        [type='button']:not(:disabled),
        [type='reset']:not(:disabled),
        [type='submit']:not(:disabled) {
          cursor: pointer;
        }

        button::-moz-focus-inner,
        [type='button']::-moz-focus-inner,
        [type='reset']::-moz-focus-inner,
        [type='submit']::-moz-focus-inner {
          padding: 0;
          border-style: none;
        }

        input[type='radio'],
        input[type='checkbox'] {
          box-sizing: border-box;
          padding: 0;
        }

        input[type='date'],
        input[type='time'],
        input[type='datetime-local'],
        input[type='month'] {
          -webkit-appearance: listbox;
        }

        textarea {
          overflow: auto;
          resize: vertical;
        }

        fieldset {
          min-width: 0;
          padding: 0;
          margin: 0;
          border: 0;
        }

        legend {
          display: block;
          width: 100%;
          max-width: 100%;
          padding: 0;
          margin-bottom: 8px;
          font-size: 24px;
          line-height: inherit;
          color: inherit;
          white-space: normal;
        }

        progress {
          vertical-align: baseline;
        }

        [type='number']::-webkit-inner-spin-button,
        [type='number']::-webkit-outer-spin-button {
          height: auto;
        }

        [type='search'] {
          outline-offset: -2px;
          -webkit-appearance: none;
        }

        [type='search']::-webkit-search-decoration {
          -webkit-appearance: none;
        }

        ::-webkit-file-upload-button {
          font: inherit;
          -webkit-appearance: button;
        }

        output {
          display: inline-block;
        }

        summary {
          display: list-item;
          cursor: pointer;
        }

        template {
          display: none;
        }

        [hidden] {
          display: none !important;
        }
      `})}t.CssReset=CssReset},7997:function(e){e.exports=require("next/dist/compiled/anser")},7292:function(e){e.exports=require("next/dist/compiled/css.escape")},7709:function(e){e.exports=require("next/dist/compiled/platform")},5974:function(e){e.exports=require("next/dist/compiled/stacktrace-parser")},7518:function(e){e.exports=require("next/dist/compiled/strip-ansi")},7522:function(e){e.exports=require("react")},2255:function(e){e.exports=require("react-dom")}};var t={};function __nccwpck_require__(r){var n=t[r];if(n!==undefined){return n.exports}var o=t[r]={exports:{}};var a=true;try{e[r].call(o.exports,o,o.exports,__nccwpck_require__);a=false}finally{if(a)delete t[r]}return o.exports}if(typeof __nccwpck_require__!=="undefined")__nccwpck_require__.ab=__dirname+"/";var r=__nccwpck_require__(5204);module.exports=r})();