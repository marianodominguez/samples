var http=require('http');

http.get(process.argv[2], function(response) {
  var lines=[];
  var count = 0;
  response.setEncoding('utf8');

  response.on('data', function(data) {
    lines.push(data);
    count +=data.length;
  });

  response.on('end', function() {
    console.log(count);
    console.log(lines.join(""));
  });
});