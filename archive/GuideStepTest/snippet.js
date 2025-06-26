console.log("snippet.js loaded an executing at " + (new Date()).toString());

(function (apiKey) {
  (function (p, e, n, d, o) {
    var v, w, x, y, z; o = p[d] = p[d] || {}; o._q = [];
    v = ['initialize', 'identify', 'updateOptions', 'pageLoad']; for (w = 0, x = v.length; w < x; ++w)(function (m) {
      o[m] = o[m] || function () { o._q[m === v[0] ? 'unshift' : 'push']([m].concat([].slice.call(arguments, 0))); };
    })(v[w]);
    y = e.createElement(n); y.async = !0; y.src = 'https://cdn.pendo.io/agent/static/' + apiKey + '/pendo.js';
    z = e.getElementsByTagName(n)[0]; z.parentNode.insertBefore(y, z);
  })(window, document, 'script', 'pendo');
  // Call this whenever information about your visitors becomes available
  // Please use Strings, Numbers, or Bools for value types.
  pendo.initialize({
    visitor: {
      id: 'GuideStepTestUser',
      firstName: 'Phil',
      lang: 'eng'
    },
    account: {
      id: 'GuideStepTestUserAcct'
    },
    events: {
      ready: function () {
        // called with no parameter
        console.log("pendo: guides loaded, ready");
      }
    }
  });
  console.log("pendo: agent initialized");
})('a93e68a6-46fd-443a-699f-aa31985c066d');