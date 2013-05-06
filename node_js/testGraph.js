Graph = require('./Graph.js').Graph;

var g = new Graph();

g.addVertex(0, 'A');
g.addVertex(1, 'B');
g.addVertex(2, 'C');
g.addVertex(3, 'D');
g.addVertex(4, 'E');
g.addVertex(5, 'F');

g.addEdge(0, 1);
g.addEdge(0, 2);
g.addEdge(0, 3);
g.addEdge(0, 4);
g.addEdge(1, 2);
g.addEdge(3, 4);
g.addEdge(1, 3);

console.log('[%s]', g.dfs());
console.log('[%s]', g.dfs(1));
console.log('[%s]', g.dfs(2));
console.log('[%s]', g.dfs(3));
console.log('[%s]', g.dfs(4));

//console.log('%s', g);