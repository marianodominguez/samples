var assert = require('assert');

process.stdin.resume();
process.stdin.setEncoding("ascii");

var recordParent = function(map, child, parent) {
	if (!map[child]) {
		map[child] = [];
	}
	map[child].push(parent);
}

var dfs = function(tree, a, depth) {
	var stack = [];
	var visited = {};
	var paths = [];
	var count = 0;
	var parentMap = {};

	stack.push(a);
	while (stack.length > 0) {
		var current = stack.pop();
		var children = tree[current];
		for (var i in children) {
			var next = children[i];
			if (!visited[next]) {
				stack.push(next);
				recordParent(parentMap, next, current);
				visited[current] = 1;
			}
		}
	}
	console.log(parentMap);
	return count;
}

process.stdin.on("data", function(input) {
	var data = input.split('\n');
	var n = data[0];
	var array = data[1].split(' ')
		.map(function(x) {
		return parseInt(x, 10)
	});
	console.log(n);
	console.log(array);
	var path = {};
	var result = 0;

	for (var i = 0; i < n; i++) {
		var element = array[i];
		var last = element;
		path[element] = [];
		for (var j = i + 1; j < n; j++) {
			next = array[j];
			if (next > element && path[element].indexOf(next) < 0) {
				path[element].push(next);
				last = next;
			}
		}
	}

	console.log(path);

	result = dfs(path, array[0], 3);

	assert.ok(result === 28, "error in algorithm : " + result);
});
