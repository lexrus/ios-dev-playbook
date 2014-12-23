exports.init = function() {
    require('./console').init();
    require('./basicAuth').init();
    require('./email').init();
    require('./httpOptions').init();
    require('./patternMatcher').init();
}