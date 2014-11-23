var fs = require('fs');
var arguments = process.argv;
var filename = arguments[2];

var count = function(err, lines) {
  if (!err) {
    console.log (lines.split('\n').length-1);
  }
};

fs.readFile(filename, 'utf8', count);
