angular.module('LiteralLabViewApp').controller('HeaderController', ['$scope', '$http', '$window', function ($scope, $http, $window) {
    $scope.logout = function () {
        $http.delete('/api/auth').success(function () {
            $window.location.reload();
        });
    };
}]);
