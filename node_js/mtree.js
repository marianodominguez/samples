/**
M-ary tree implementation
*/

var wordTree = function() {
    this.value = null;
    this.children = [];
};

var findNode = function(list, val) {
    if (list == []) return -1;
    for (i in list) {
        if (list[i].value === val) return i;
    }
    return -1;
};

wordTree.prototype =
{
    addWord : function (s) {
    var root = this;
    var tree = this;
    if (s==='' || s === null) return;
    for (var i in s) {
        var letter = s[i];
        var index = findNode(tree.children, letter);
        if (index < 0 ) {
        var newNode = new wordTree();
        newNode.value = letter;
        tree.children.push(newNode);
        tree = newNode;
        }
        else {
        tree = tree.children[index];
        }
    }
    tree = root;
    },
    prefixes : function() {
    var root = this;
    var result = [];
    var prefix = '';
    var stack = [];
    var current = null;
    // ignore root

    for (i in root.children) {
        stack.push(root.children[i]);
    }

    while (stack.length > 0) {
        current = stack.pop();
        if (current.children.length ==1 ) {
        prefix += current.value;
        stack.push(current.children[0]);
        }
        else {
        prefix += current.value;
        if (current.children.length > 0) result.push(prefix);
        prefix = '';
        }
    }
    return result;
    }
};

var wordlist = ['book', 'boo', 'z', 'apple', 'appeal'];
var words = new wordTree();
words.value = '%';

for (var i in wordlist) {
    words.addWord(wordlist[i]);
}
console.log(words.prefixes());

//console.log(words);