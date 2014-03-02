angular.module('twitt', [])
    .controller('TextAreaWithLimitCtrl', function($scope) {

    var MAX_LEN = 140;
    $scope.message = "";

    $scope.remaining = function () {
        return MAX_LEN - $scope.message.length;
    };

    $scope.send = function () {};
    $scope.clear = function() {
        $scope.message = "";
    };
    });