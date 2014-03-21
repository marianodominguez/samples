'use strict';

angular.module('mytodoApp')
  .controller('MainCtrl', function ($scope) {
    $scope.todos = ['item 1',
      'item 2',
      'item 3'];
  });
