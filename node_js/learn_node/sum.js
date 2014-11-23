var arguments = process.argv;

arguments = arguments.slice(2);
var result = 0
if (arguments.length<2) return;
arguments.forEach(function(e, i, arr) {
  result += parseInt(e,10);
});
console.log(result);

