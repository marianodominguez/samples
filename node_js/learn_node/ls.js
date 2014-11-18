var fs = require('fs');
var path = require('path');
var arguments = process.argv;

if (arguments.length <3) return;

var filename = arguments[2];
var ext = arguments[3];

var count = function(err, list) {
  if (err) return;
  for (i in list) {
    if (path.extname(list[i]) === "." + ext) {
      console.log(list[i]);
    }
  }
};

fs.readdir(filename, count);