module.exports = function (dirname, ext, callback) {
  fs.readdir(dirname, function(err, list) {
    ls(err, list, ext, callback);
  });
}

var fs = require('fs');
var path = require('path');

var ls = function(err, list, ext, callback) {
  if (err) {
    return callback(err);
  }
  var result = [];
  for (i in list) {
    if (path.extname(list[i]) === "." + ext) {
      result.push(list[i]);
    }
  }
  callback(null, result)
};


var wc = function() {
  fs.readFile(filename, 'utf8', count);
};

var count = function(err, lines, callback) {
  if (!err) {
    callback (null, lines.split('\n').length-1);
  }
};
