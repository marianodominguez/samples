var dgram = require('dgram');

var server = dgram.createSocket('udp4');

server.on('listening', function() {
    var address = server.address();
    console.log("server listening " +
    address.address + ":" + address.port);
});

server.on("message", function (msg, rinfo) {
  console.log("server got: " + msg + " from " +
    rinfo.address + ":" + rinfo.port);
});

server.bind(41234);