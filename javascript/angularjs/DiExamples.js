var myMod = angular.module('mymod', []);

myMod.factory('myFactoryService', function(otherService) {
    var privateVal=10;
    return {
	push: function(x) {},
    }
});