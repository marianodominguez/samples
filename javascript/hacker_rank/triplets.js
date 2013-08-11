var assert = require('assert');

process.stdin.resume();
process.stdin.setEncoding("ascii");

var array = [];
var n = 0;

process.stdin.on("data", function(input) {
	var lines = input.split('\n');

	assert(lines.length > 0, "input error, at least on line is required");

	if (lines[0].indexOf(' ') < 0) {
		n = parseInt(lines[0], 10);
	}

	for (var i = 0; i < lines.length; i++) {
		if (lines[i].indexOf(' ') > 0) {
			array = array.concat(lines[i].split(' '))
				.map(function(x) {
				return parseInt(x, 10)
			});
		}
	}
});

process.stdin.on("end", function() {

	assert(n >= 3, "not enough elements");
	assert(array.length === n, "array not matching size");

	var sequences = {};
	//console.log(array.length);
	var repeated = [];
	var triplets = {};
    var uniqueFirsts = {};
	for (var i = 0; i < array.length - 1; i++) {
		var current = array[i];
        if (! uniqueFirsts[current]) {
            uniqueFirsts[current] = i;
        }
        
		if ( !repeated[i]) {
			repeated[i] = {};
		}
		for (var j = i; j < array.length; j++) {
			var child = array[j];
			if (child > current && !repeated[i][j]) {
				sequences[i] ? "" : sequences[i] = [];
				sequences[i].push(j);
				repeated[i][j] = 1;
			}
		}
	}

    repeated = null;
	console.log(uniqueFirsts);

	// use greedy algorithm to create triplets map

	for (var i in uniqueFirsts) {
        var first = uniqueFirsts[i];
		var children = sequences[first];
		for (var j = 0; j < children.length; j++) {
			var second = children[j];
			var endOptions = sequences[second];
			if (endOptions && endOptions.length >= 1) {
				endOptions.forEach(function(third, idx) {
					triplets[array[first] + "," + array[second] + "," + array[third]] = 1;
				});
			}
		}
	}
	console.log(triplets);

	var result = 0;
    
    for(var i in triplets) {
        result++;
    }
    console.log(result);
    
});
var assert = require('assert');

process.stdin.resume();
process.stdin.setEncoding("ascii");

var array = [];
var n = 0;

process.stdin.on("data", function(input) {
	var lines = input.split('\n');

	assert(lines.length > 0, "input error, at least on line is required");

	if (lines[0].indexOf(' ') < 0) {
		n = parseInt(lines[0], 10);
	}

	for (var i = 0; i < lines.length; i++) {
		if (lines[i].indexOf(' ') > 0) {
			array = array.concat(lines[i].split(' '))
				.map(function(x) {
				return parseInt(x, 10)
			});
		}
	}
});

process.stdin.on("end", function() {

	assert(n >= 3, "not enough elements");
	assert(array.length === n, "array not matching size");

	var sequences = {};
	//console.log(array.length);
	var repeated = [];
	var triplets = {};
    var uniqueFirsts = {};
	for (var i = 0; i < array.length - 1; i++) {
		var current = array[i];
        if (! uniqueFirsts[current]) {
            uniqueFirsts[current] = i;
        }
        
		if ( !repeated[i]) {
			repeated[i] = {};
		}
		for (var j = i; j < array.length; j++) {
			var child = array[j];
			if (child > current && !repeated[i][j]) {
				sequences[i] ? "" : sequences[i] = [];
				sequences[i].push(j);
				repeated[i][j] = 1;
			}
		}
	}

    repeated = null;
	console.log(uniqueFirsts);

	// use greedy algorithm to create triplets map

	for (var i in uniqueFirsts) {
        var first = uniqueFirsts[i];
		var children = sequences[first];
		for (var j = 0; j < children.length; j++) {
			var second = children[j];
			var endOptions = sequences[second];
			if (endOptions && endOptions.length >= 1) {
				endOptions.forEach(function(third, idx) {
					triplets[array[first] + "," + array[second] + "," + array[third]] = 1;
				});
			}
		}
	}
	console.log(triplets);

	var result = 0;
    
    for(var i in triplets) {
        result++;
    }
    console.log(result);
    
});
var assert = require('assert');

process.stdin.resume();
process.stdin.setEncoding("ascii");

var array = [];
var n = 0;

process.stdin.on("data", function(input) {
	var lines = input.split('\n');

	assert(lines.length > 0, "input error, at least on line is required");

	if (lines[0].indexOf(' ') < 0) {
		n = parseInt(lines[0], 10);
	}

	for (var i = 0; i < lines.length; i++) {
		if (lines[i].indexOf(' ') > 0) {
			array = array.concat(lines[i].split(' '))
				.map(function(x) {
				return parseInt(x, 10)
			});
		}
	}
});
