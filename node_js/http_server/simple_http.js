http = require('http')
var count=0;

var requestHandler = function(request, response) {
	var message="";
	response.writeHead(201, {
			'Content-Type': 'text/plain'    
	});

	switch(request.url) {
		case '/count':
			message = "Vistor count: " + count ;
			count+=1;
		break;
		case '/hello':
		 	message = "World" ;
		break;
		case '/':
			message = "404 not found"
		break;
	}

	
	response.end(message);
}

server = http.createServer(requestHandler);

server.listen(8080, function() {
	console.log("listening in port 8080 ...")
});

