var Vertex = function () {
    this.value = null;
    this.adj = [];
};

var Graph = function() {
    this.V = [];
    this.size = 0;
};

module.exports = {
    Graph : Graph
};

Graph.prototype = {
    addEdge : function (idx1, idx2) {
        if (typeof idx1 !== 'number' || typeof idx1 !== 'number' ) {
            throw "Graph indices should be numbers";
        }
        var V1 = this.V[idx1];
        var V2 = this.V[idx2];

        if (!V1) {
            V1 = new Vertex();
            this.V[idx1] = V1;
            this.size+=1;
        }
        if (!V2) {
            V2 = new Vertex();
            this.V[idx2] = V2;
            this.size+=1;
        }
        V1.adj.push(idx2);
        V2.adj.push(idx1);
    },
    addVertex: function(idx, value) {
        if (typeof idx !== 'number') {
            throw "Graph indices should be numbers";
        }
        var vertex = this.V[idx];
        if (!vertex) {
            vertex = new Vertex();
            this.V[idx] = vertex;
            this.size++;
        }
        vertex.value = value;
    },
    toString : function() {
        return JSON.stringify(this, null, 2);
    },
    get : function(i) {
        return this.V[i];
    },
    getAdj : function(i) {
        return this.V[i].adj;
    },
    dfs : function (start) {
        if (this.V===null || this.size===0) return [];
        if (!start) start=0;
        var visited = [];
        var path = [];
        var stack = [];
        stack.push(start);
        visited.push(start);
        var current = start;
        while(stack.length !== 0) {
            current = stack.pop();

            //console.log("current : " + current);

            var adjList = this.getAdj(current);
            for (var i in adjList) {
                var neighbor = adjList[i];
                if (visited.indexOf(neighbor) < 0 ) {
                    stack.push(neighbor);
                    visited.push(neighbor);
                }
            }

            path.push(current);
            //console.log(stack);
        }
        return path;
    }
};

