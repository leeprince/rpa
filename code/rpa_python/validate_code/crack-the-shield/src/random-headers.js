const pool = [
  "window",
  "self",
  "document",
  "name",
  "location",
  "customElements",
  "history",
  "locationbar",
  "menubar",
  "personalbar",
  "scrollbars",
  "statusbar",
  "toolbar",
  "status",
  "closed",
  "frames",
  "length",
  "top",
  "opener",
  "parent",
  "frameElement",
  "navigator",
  "origin",
  "external",
  "screen",
  "innerWidth",
  "innerHeight",
  "scrollX",
  "pageXOffset",
  "scrollY",
  "pageYOffset",
  "visualViewport",
  "screenX",
  "screenY",
  "outerWidth",
  "outerHeight",
  "devicePixelRatio",
  "clientInformation",
  "screenLeft",
  "screenTop",
  "defaultStatus",
  "defaultstatus",
  "styleMedia",
  "onsearch",
  "isSecureContext",
  "performance",
  "onappinstalled",
  "onbeforeinstallprompt",
  "crypto",
  "indexedDB",
  "webkitStorageInfo",
  "sessionStorage",
  "localStorage",
  "onbeforexrselect",
  "onabort",
  "onblur",
  "oncancel",
  "oncanplay",
  "oncanplaythrough",
  "onchange",
  "onclick",
  "onclose",
  "oncontextmenu",
  "oncuechange",
  "ondblclick",
  "ondrag",
  "ondragend",
  "ondragenter",
  "ondragleave",
  "ondragover",
  "ondragstart",
  "ondrop",
  "ondurationchange",
  "onemptied",
  "onended",
  "onerror",
  "onfocus",
  "onformdata",
  "oninput",
  "oninvalid",
  "onkeydown",
  "onkeypress",
  "onkeyup",
  "onload",
  "onloadeddata",
  "onloadedmetadata",
  "onloadstart",
  "onmousedown",
  "onmouseenter",
  "onmouseleave",
  "onmousemove",
  "onmouseout",
  "onmouseover",
  "onmouseup",
  "onmousewheel",
  "onpause",
  "onplay",
  "onplaying",
  "onprogress",
  "onratechange",
  "onreset",
  "onresize",
  "onscroll",
  "onseeked",
  "onseeking",
  "onselect",
  "onstalled",
  "onsubmit",
  "onsuspend",
  "ontimeupdate",
  "ontoggle",
  "onvolumechange",
  "onwaiting",
  "onwebkitanimationend",
  "onwebkitanimationiteration",
  "onwebkitanimationstart",
  "onwebkittransitionend",
  "onwheel",
  "onauxclick",
  "ongotpointercapture",
  "onlostpointercapture",
  "onpointerdown",
  "onpointermove",
  "onpointerup",
  "onpointercancel",
  "onpointerover",
  "onpointerout",
  "onpointerenter",
  "onpointerleave",
  "onselectstart",
  "onselectionchange",
  "onanimationend",
  "onanimationiteration",
  "onanimationstart",
  "ontransitionrun",
  "ontransitionstart",
  "ontransitionend",
  "ontransitioncancel",
  "onafterprint",
  "onbeforeprint",
  "onbeforeunload",
  "onhashchange",
  "onlanguagechange",
  "onmessage",
  "onmessageerror",
  "onoffline",
  "ononline",
  "onpagehide",
  "onpageshow",
  "onpopstate",
  "onrejectionhandled",
  "onstorage",
  "onunhandledrejection",
  "onunload",
  "alert",
  "atob",
  "blur",
  "btoa",
  "cancelAnimationFrame",
  "cancelIdleCallback",
  "captureEvents",
  "clearInterval",
  "clearTimeout",
  "close",
  "confirm",
  "createImageBitmap",
  "fetch",
  "find",
  "focus",
  "getComputedStyle",
  "getSelection",
  "matchMedia",
  "moveBy",
  "moveTo",
  "open",
  "postMessage",
  "print",
  "prompt",
  "queueMicrotask",
  "releaseEvents",
  "requestAnimationFrame",
  "requestIdleCallback",
  "resizeBy",
  "resizeTo",
  "scroll",
  "scrollBy",
  "scrollTo",
  "setInterval",
  "setTimeout",
  "stop",
  "webkitCancelAnimationFrame",
  "webkitRequestAnimationFrame",
  "chrome",
  "caches",
  "cookieStore",
  "ondevicemotion",
  "ondeviceorientation",
  "ondeviceorientationabsolute",
  "showDirectoryPicker",
  "showOpenFilePicker",
  "showSaveFilePicker",
  "speechSynthesis",
  "originAgentCluster",
  "onpointerrawupdate",
  "trustedTypes",
  "crossOriginIsolated",
  "openDatabase",
  "webkitRequestFileSystem",
  "webkitResolveLocalFileSystemURL",
  "GetParams",
  "__REDUX_DEVTOOLS_EXTENSION__",
  "devToolsExtension",
  "__REDUX_DEVTOOLS_EXTENSION_COMPOSE__",
  "__REACT_DEVTOOLS_APPEND_COMPONENT_STACK__",
  "__REACT_DEVTOOLS_BREAK_ON_CONSOLE_ERRORS__",
  "__REACT_DEVTOOLS_COMPONENT_FILTERS__",
  "__REACT_DEVTOOLS_SHOW_INLINE_WARNINGS_AND_ERRORS__",
  "$",
  "jQuery",
  "_0x2b38",
  "_0x3e98",
  "es",
  "sleep",
  "_insert",
  "forAwait",
  "findEvents",
  "_0x3a1d",
  "_0x29a9",
  "bf",
  "__VUE_DEVTOOLS_TOAST__",
  "temp1"
]

const getOneName = (withX = false) => {
  const randIDX = Math.floor(Math.random() * pool.length)
  return withX
    ? `x-${pool[randIDX]}`
    : pool[randIDX]
}

const getRandomHeaders = () => {
  const num = Math.floor(Math.random() * 10) + 1
  return Array(num)
    .fill('')
    .reduce((h, c) => {
      h[getOneName(true)] = getOneName()
      return h
    }, {})
}

module.exports = {
  pool,
  getRandomHeaders,
}
