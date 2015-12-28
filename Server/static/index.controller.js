angular.module('LiteralLabViewApp').controller('IndexController', ['$scope', '$http', function ($scope, $http) {
    $scope.data = {
        screenshotImage: '',
        cameraImage: ''
    };

    $http.get('/api/data/recent').success(function (res) {
        $scope.data = res;
    });
}]);
