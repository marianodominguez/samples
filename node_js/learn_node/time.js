var net = require('net');

var port = process.argv[2];
//console.log(port);

function pad(s) {
  if ((""+s).length < 2) return "0"+s
  else return s;
}

var server = net.createServer(function(socket) {
  var now = new Date();
  var month = now.getMonth() + 1;
  var day = now.getDate();
  var strDate = now.getFullYear() + "-" + pad(month) + "-" + pad(day) + " " + pad(now.getHours()) + ":" + pad(now.getMinutes());
  socket.write(strDate);
  socket.end("\n");
});

server.listen(port);