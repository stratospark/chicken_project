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
        data.last_updated = Date.parse(data.last_updated).toString('M/d/yyyy @ h:mm tt')
        data.sunrise = Date.parse(data.sunrise).toString('@ h:mm tt')
        data.sunset = Date.parse(data.sunset).toString('@ h:mm tt')
        $scope.data = data




