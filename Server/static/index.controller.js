angular.module('LiteralLabViewApp').controller('IndexController', ['$scope', '$http', function ($scope, $http) {
    $scope.data = {
        screenshotImage: '/static/loader.gif',
        cameraImage: '/static/loader.gif'
    };

    $http.get('/api/data/recent').success(function (res) {
        $scope.data = res;
    });
}]);
