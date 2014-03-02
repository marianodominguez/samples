var MergeSorter = function() {
    var public = {};
    public.sort = function sort(list) {
    if (list.length == 0 || list.length == 1) {
        return list;
    } else {
        var middle = Math.floor(list.length / 2);
        var left = list.slice(0, middle);
        var right = list.slice(middle, list.length);
        return merge(sort(left), sort(right))
    }
    }

    function merge(a, b) {
    var result = [];
    while (a.length > 0 && b.length > 0) {
        if (a[0] < b[0]) {
        result.push(a[0]);
        a = a.slice(1);
        } else {
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
    console.log(result);
    return result;
    }
    return public;
};

var list = [];
var orig = [];
var LIST_SIZE = 40;

for (var i = 0; i <= LIST_SIZE; i++) {
    orig[i] = i;
}

while (orig.length > 0) {
    var idx = Math.floor(Math.random() * orig.length);
    list.push(orig[idx]);
    orig.splice(idx, 1);
}

var sorter = new MergeSorter();
console.log(list);

console.log(sorter.sort(list));
