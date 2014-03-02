var assert = require('assert');

function cyberline(s) {

    if (s === null) {
    return s;
    };

    var clean = s.replace(/-/g, '');
    clean = clean.replace(/[^A-Za-z0-9@]+/g, ' ');
    //clean = clean.replace(/[^\w@]+/g, ' ');

    clean = clean.replace(/\s+/g, ' ');
    clean = clean.replace(/\s+$/g, '');
    console.log("["+clean+"]");
    var words = clean.split(/\s+/);
    console.log(words);
    return words[ words.length -1 ];
}

assert.equal(cyberline("Zowie:    This is a -line of##cyber-poetry## !"), 'cyberpoetry');
assert.equal(cyberline("@@@@@@"), '@@@@@@');