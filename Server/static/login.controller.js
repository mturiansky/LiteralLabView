angular.module('LiteralLabViewApp').controller('LoginController', ['$scope', '$http', '$window', '$location', '$stateParams', function ($scope, $http, $window, $location, $stateParams) {
    $scope.username = '';
    $scope.password = '';

    $scope.loginUser = function () {
        console.log('posting...');
        $http.post('/api/auth', { username: $scope.username, password: $scope.password }).success(function (res) {
            $window.location.reload();
        });
    };
}]);
