var Animal = function(name){
	this.id = Math.round(Math.random() * 1000 + 1);
	this.name  = name;
};

var Dog = function (name) {
	Animal.apply(this, arguments);
};

Animal.prototype.scanID = function() {
	console.log(this.id);
};

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
	console.log(this.name + ' barked');
};

var myDog = new Dog('rover');

myDog.bark();
myDog.scanID();

for (x in myDog) {
	console.log(x)
}

// Function call

// ASEF

(function() {
	var inner = "anonymous";
	console.log("created " + inner);
}());

// named

var named = (function() {
	var inner = "named";
	console.log("created " + inner);
	return {inner: inner};
})();

// Not called but hoisted

function other(){
	var inner = "not called";
	console.log("created " + inner);
	
}
//
console.log(named);