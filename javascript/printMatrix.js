function printMatrix(m) {
    if (size(m)==1) return m[0][0];
    else {
    return border(m).concat(printMatrix(submatrix(m)));
    }
}

function border(m) {
    result = [];
    var k = size(m);
    for (var i = 0; i<k ; i++) {
    result.push(m[ 0, i ]);
    }
    for (var i = 1; i<k ; i++) {
    result.push(m[ i , k-1]);
    }
    for (var i = k-1; i>0 ; i--) {
    result.push(m[ k-1 , i ]);
    }
    for (var i = k-1; i>0 ; i--) {
    result.push(m[i,0]);
    }
    return result;
}

function submatrix(m) {

}