
var dgram = require('dgram');

var message = new Buffer("Some weird message");

var client = dgram.createSocket("udp4");


var host = "localhost"
var port = 41234

client.send(message, 0, message.length, port, host, function(err, bytes) {
  client.close();
});