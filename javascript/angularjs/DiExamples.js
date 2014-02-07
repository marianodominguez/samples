var myMod = angular.module('mymod', []);

myMod.factory('otherService', function($log) {
    return {
	out: function(x) {
	    $log.info('other service called with: ' + x);
	}
    }
});

myMod.factory('myFactoryService', function(otherService) {
    var privateVal = 10;
    return {
	push: function(x) {
	    otherService.out(x);
	    privateVal += x;
	}
    }
});