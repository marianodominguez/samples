snail = function snail(array) {
  var border = function(array) {
    result = array[0];
    var n = array[0].length
    for(var i=1; i<n-1; i++) {
      result.push(array[i][n-1]);
    }
    for(var j=n-1; j>=0; j--) {
      result.push(array[n-1][j]);
    }
    for(var k=n-2; k>=1; k--) {
      result.push(array[k][0]);
    }
    return result;
  }

  var submatrix = function(array) {
    result = [];
    var n = array.length;
    if (n<3) return [[]];
    for(var i=1; i<n-1; i++) {
      result.push(array[i].slice(1,-1));
    }
    console.log(result);
    return result;
  }

  result = [];
  if (array[0].length === 0) return [];
  if (array[0].length === 1) return [array[0][0]];
  if (array[0].length === 2) return array[0].concat(array[1][1],array[1][0]);
  else {
    result = result.concat(border(array), snail(submatrix(array)) );
  }
  return result;
}