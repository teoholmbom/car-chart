/*global chartApp, $scope*/

chartApp.controller('mainController', ['$scope', '$http', function ($scope, $http) {
    'use strict';

    $scope.options = {
        legend: {
            display: true
        }
    };

    $http.get('api/cars').then(function (response) {
        $scope.series = response.data[0];
        $scope.labels = response.data[1];
        $scope.data = response.data[2];
    });


}]);