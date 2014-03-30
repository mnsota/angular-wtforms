(function ($ng, $) {

    var app = $ng.module('app', []);

    app.controller('RegisterCtrl', ['$scope', '$http', '$timeout', function ($scope, $http, $timeout) {
        var registration = {}, state = { registered: false};

        $timeout(function(){
            $scope.registration = registration;
            $scope.state = state;
        });

        $scope.submit = function () {
            $http({
                method: 'POST',
                url: '/register',
                data: $.param(dataObj(registration)),
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            })
                .success(function (resp) {
                    state.registered = true;
                    $ng.extend($scope.registration, resp);
                })
                .error(function (resp) {
                    $ng.extend($scope.registration, resp);
                });
        };

        function dataObj() {
            return {
                username: registration.username && registration.username.data,
                email: registration.email && registration.email.data,
                password: registration.password && registration.password.data,
                confirm: registration.confirm && registration.confirm.data,
                accept_tos: registration.accept_tos && registration.accept_tos.data
            }
        }

    }]);

}(window.angular, window.jQuery));


