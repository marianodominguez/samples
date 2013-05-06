var Tree = require('./tree.js').Tree;

var myTree = new Tree();

myTree.addNode(6);
myTree.addNode(7);
myTree.addNode(3);
myTree.addNode(4);
myTree.addNode(1);
myTree.addNode(5);
myTree.addNode(8);
myTree.addNode(2);

myTree.inorder();
console.log( myTree.dfsFind(8) );
console.log( myTree.binaryFind(8));
