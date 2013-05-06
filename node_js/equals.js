var assert = require("assert");

function bEquals(a, b) {
    if (a==b) {
        return true;
    } else {
        return false;
    }
}

// looks fine

assert(bEquals("", ''));
assert(bEquals("abc", "abc"));

assert(!bEquals("a", "b"));
assert(!bEquals("a", "A"));
assert(!bEquals("aBC", "Abc"));

// What about those?

assert(bEquals(123, "123"));
assert(bEquals( 7, '07') );
assert(!bEquals( '7', '07') );

//WTF
assert( bEquals( 010, '8') );
//more to come

assert( bEquals( null,  null) );
assert( bEquals( undefined,  undefined) );

//but
assert( !bEquals( NaN,  NaN) );

console.log("equals working ?");
