var assert = require('assert');

function mergeArrays (a , b) {
    var result = [];
    while(a.length > 0 && b.length > 0) {
	if(a[0] < b[0]) 
	    {
		result.push(a[0]);
		a = a.slice(1);
	    }
        else 
	    {
		result.push(b[0]);
		b = b.slice(1);
	    }
    }
    if (a.length > 0) {
        result = result.concat(a);
    }
    if (b.length > 0) {
        result = result.concat(b);
    }
    //console.log(result);
    return result;
}

function mergeSort(a) {
    if (a === [] || a === null) return a;        
    
    var len = a.length;
    if (len === 1) return a;
    if(len === 2) {
        if (a[0] > a[1]) {
            return [a[1], a[0]];
        } else {
            return a;
        }
    }
    else {
        //console.log(a);
        var mid = len/2;
        var left = mergeSort(a.slice(0, mid));
        var right = mergeSort(a.slice(mid, len));
        return mergeArrays(left, right);
    }
}
//test merge
assert.deepEqual(
    mergeArrays([1, 4, 5 ,6 ], [2, 3, 7] ), [1, 2, 3, 4, 5, 6, 7], "Merge is not working"
    );

var x = [];

for (var i = 0; i <= 100; i++) {
    x.push( Math.round(Math.random() * 100));
};

console.log(mergeSort(x));
