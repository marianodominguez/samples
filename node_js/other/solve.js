function solve(map, miner, exit) {
  var xmax = map.length-1;
  var ymax = map[0].length-1;

  var samePos = function (a,b) {
    return (a.x===b.x && a.y===b.y);
  };

  var look = function (map,current, dir) {
    var pos = {};
    pos.x=current.x;
    pos.y=current.y;
    if (dir==='up' && pos.y>0) pos.y-=1;
    if (dir==='down' && pos.y<ymax) pos.y+=1;
    if (dir==='left' && pos.x>0) pos.x-=1;
    if (dir==='right' && pos.x<xmax) pos.x+=1;
    if (samePos(pos,current)) return null;

    if (map[pos.x][pos.y]) return pos;
    return null;
  };

  var stack = [];
  var result = [];
  var visited = [];
  stack.push(miner);
  var current = miner;
  visited[current.x+"_"+current.y] = true;

  var dirs = ['left', 'right', 'up', 'down'];
  while (stack.length>0) {
    current = stack.pop();

    //give preference to exit address
    for(var i=0; i<dirs.length; i++) {
      var next = look(map, current, dirs[i]);
      if(next && samePos(next,exit)) {
        result.push(dirs[i]);
        return result;
      }
      if (next && !visited[next.x+"_"+next.y]) {
        stack.push(next);
        result.push(dirs[i]);
        current=next;
        visited[current.x+"_"+current.y] = true;
      }
    }
  }
  return [];
}

var map = [[true]];
console.log(solve(map, {x:0,y:0}, {x:0,y:0}));
map = [[true, false],
    [true, true]];
console.log(solve(map, {x:0,y:0}, {x:1,y:0}));
console.log(solve(map, {x:0,y:0}, {x:1,y:1}));
map = [[true, true, true, false, true],
    [false, false, true, false, true],
    [true, true, true, true, true],
    [true, false, true, false, false],
    [false, true, true, true, true]];

console.log(solve(map, {x:0,y:0}, {x:4,y:4}));

  map = [[true, true, true, false, true],
    [false, false, true, false, true],
    [true, true, true, true, true],
    [true, false, true, false, false],
    [false, true, true, true, true]];

console.log(solve(map, {x:0,y:0}, {x:4,y:4}));


