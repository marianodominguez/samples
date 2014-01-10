var hello = angular.module('hello', []);

hello.controller('HelloCtrl', function($scope) {
    $scope.name = 'World!';
});