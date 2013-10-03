/**
* binary tree implementation.
* includes DFS
*
**/

var Tree = function () {
    this.node = null;
    this.left = null;
    this.right = null;
};

module.exports = {
    Tree:Tree
};

function Node(val) {
    this.value = val;
};

Tree.prototype = 
{
    addNode : function (v) {
        var newNode = new Node(v);
        if (this.node === null) {
            this.node = newNode;
        }
        else if (this.node.value <= v) {
            if (this.left === null) {
                this.left = new Tree();
                this.left.node = newNode;
            } 
            else {
                this.left.addNode(v);
            }
        }
        else {
            if (this.right === null) {
                this.right = new Tree();
                this.right.node = newNode;
            }
            else {
                this.right.addNode(v);
            }
        }
    },
    dfsFind : function(val) {
        var stack= [this];
        var current = null;
        
        while (stack.length > 0) {
            current = stack.pop();
            console.log("reviewing " + current.node.value );
            if(current.node.value === val) {
                return current;
            }
            else {
                if (current.left !== null) {
                    stack.push(current.left);
                }
                if (current.right !== null) {
                    stack.push(current.right);
                }
            }
        }
        return null;
    },
    inorder : function inorder(tree) {
        if (tree === undefined) tree = this;
        if (tree === null) return;
        inorder(tree.left);
        console.log(tree.node.value + ",");
        inorder(tree.right);
    },
    binaryFind : function bf(v, root) {
        if (root === undefined) root = this;
        var val = root.node.value;
        console.log("BF examine : " + val);
        if ( val === v) {
            return root;
        }
        if (val < v) {
            if (root.left !== null) return bf(v, root.left);
        }
        else {
            if (root.right !== null) return bf(v, root.right);
        }
        return null;
    }
};

