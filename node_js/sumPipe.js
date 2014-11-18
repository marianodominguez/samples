var sum=0;

process.stdin.on("data", function(data) {
  var number = parseInt(data, 10);
  if (isFinite(number)) {
    sum += number;
   }

  console.log("sum=" + sum);
});

process.stdin.resume();