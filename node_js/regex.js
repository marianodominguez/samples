// Regex test

var text = 'this is a 23 raw text to match 123 abc 1234 but not 567890 not';

var numbers = /[1-4]+/;
var allNumbers = /[1-4]+/g;

console.log( numbers.exec(text) );

console.log( text.search(numbers) );

console.log( text.split(numbers) );

console.log( text.replace(numbers, ',') );
console.log( text.replace(allNumbers, ',') );
