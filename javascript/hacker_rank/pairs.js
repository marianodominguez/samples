process.stdin.resume();
process.stdin.setEncoding("ascii");

var lines = [];

process.stdin.on("data", function (input) {
    input = input.toString().trim();
    var line = input.split('\n');
    lines = lines.concat(line);
});

process.stdin.on('end', function() {
    var header = lines[0].split(' ');
    var count = 0;
    var n = parseInt(header[0], 10);
    var k = parseInt(header[1], 10);
    var numbers=[];
    
    for (var l=1; l<lines.length; l++) {
        numbers = numbers.concat(lines[l].split(' ').map(function(x) {return parseInt(x, 10)}));
    }
    
    var count =0;
    lookup = {};
    for (var i =0; i<n; i++) {
        lookup[numbers[i]] = i;
    }
    
    for (var i =0; i<n; i++) {
        if (lookup[numbers[i]+k]) count +=1;
    }
    
    console.log(count);
});