var fs = require('fs');
var arguments = process.argv;
var filename = arguments[2];
var buf = fs.readFileSync(filename);
var lines = buf.toString()

console.log (lines.split('\n').length-1);