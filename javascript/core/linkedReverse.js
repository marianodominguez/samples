(function(){

    var Dlist = function(){
        this.HEAD=null;
    };

    var Node = function() {
        this.value = null;
        this.prev = null;
        this.next = null;
    }

    Dlist.prototype = {
        add : function(val) {
            var node = new Node();
            node.value = val;
            node.prev = null;
            node.next = this.HEAD;
            this.HEAD = node;
        },
        toString: function () {
            result = [];
            var node = this.HEAD;
            while(node) {
                result.push(node.value);
                node=node.next;
            }
            return result.toString();
        }
    };

    mylist = new Dlist();

    mylist.add(1);
    mylist.add(2);
    mylist.add(3);
    mylist.add(4);
    mylist.add(5);
    mylist.add(6);

    console.log(mylist.toString());

})();