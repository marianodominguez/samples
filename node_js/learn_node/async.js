var http=require('http');

var urls=[];

if(process.argv.length<5) {
  console.error('need 3 urls');
  return;
}

var responses = [];
var complete = [];

for (var i=0; i<3; i++) {
   urls[i] = process.argv[i+2];
};

urls

urls.forEach(function(url, current) {
  http.get(url, function(response) {
    responses[current] = "";
    response.setEncoding('utf8');

    response.on('data', function(data){
      responses[current] += data;
    });

    response.on('end', function() {
      complete.push(current);
      //console.log(complete);
      if(complete.length === 3) {
        responses.forEach(function(line) {
          console.log(line);
        });
      }
    });
  });
 });

