var express = require('express');
var app = express();

app.get('/hello.txt', function(req, res){ngth);
  res.send('Hello Express');
});

app.listen(3000);
console.log('listening on port 3000');