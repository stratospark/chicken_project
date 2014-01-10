'use strict'

angular.module('chickenFrontendApp')
  .controller 'MainCtrl', ($scope) ->
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
      'Blah'
    ]
    $scope.projectName = "Awesome Project!"

