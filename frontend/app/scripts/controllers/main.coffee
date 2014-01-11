'use strict'

angular.module('chickenFrontendApp')
  .controller 'MainCtrl', ($scope, $http) ->
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
      'Blah'
    ]
    $scope.projectName = "Awesome Project!"

    $http(method: 'GET', url: '/api/data').
      success (data, status, headers, config) ->
        console.log data
        $scope.data = data




