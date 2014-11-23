var filemodule = require('./filemodule');
var arguments = process.argv;

var print = function(err, data) {
  if (err) return;
  data.forEach( function(file){
    console.log(file);
  });
};

filemodule(arguments[2], arguments[3], print);
