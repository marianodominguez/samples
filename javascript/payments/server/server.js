var http = require('http');
var url  = require('url');

var routes = "";
var ts = require('./transactionServer.js');

/*
  simple router to call service by path: TODO use a real one
*/
var simpleHandler = function (request, response) {
    var parsedUrl = url.parse(request.url, true); 
    var parameters = parsedUrl.query;
    
    var responseData = {};
    response.writeHead(200, { 'Content-Type': 'application/json', "Access-Control-Allow-Origin":"*" });
    
    //console.log(parsedUrl);
    
    if(parsedUrl.pathname === '/transactions') {
        var start = parameters.start || 0;
        var end = parameters.end || 10;
        console.log("get Transactions: ");
        responseData = ts.getTransactions(start, end);
    }
    else if (parsedUrl.pathname === '/transfer')
    {
        responseData = ts.postTransfer();
    }
    response.write(JSON.stringify(responseData)); 
    response.end();
};
 
var server = http.createServer(simpleHandler);

server.listen(3000, "0.0.0.0", function(){
    var addr = server.address();
    console.log("Chat server listening at", addr.address + ":" + addr.port);
});
