var http = require('http');


function sayHello(request, response) {
  response.writeHead(200, {'Content-Type': 'text/html'});
  response.write('<H1> Sample page </H1>');
  response.write('page from nodejs ');  
  response.end('\n');
}

http.createServer(sayHello).listen(8124);

console.log('Server running at http://127.0.0.1:8124/');
