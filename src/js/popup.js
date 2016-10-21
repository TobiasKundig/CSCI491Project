/**
 * Created by toby on 10/13/16.
 */
$(function() {
    $('#register').avgrund({
        height: 200,
        holderClass: 'custom',
        showClose: true,
        showCloseText: 'close',
        onBlurContainer: '.container',
        template: '<div>' +
        '<br><br>Username: <input type="text" id="username" placeholder=" username"' +
        '<br><br>Password: <input type="text" id="password" placeholder=" password"' +
        '</div>' +
        '' +
        '<div>' +
        '<a href="index.html" class="twitter">Register</a>' +

        '</div>'
    });
});

$(function() {
    $('#login').avgrund({
        height: 200,
        holderClass: 'custom',
        showClose: true,
        showCloseText: 'close',
        onBlurContainer: '.container',
        template: '<form class="form-horizontal"' +
        '<div class="form-group">' +
            '<label class="control-label col-sm-4" for="usrname">Username: </label>' +
            '<div class="col-sm-6">' +
                '<input type="text" id="username" class="form-control" placeholder=" username">' +
            '</div>' +

            '<label class="control-label col-sm-4" for="pwd">Password: </label>' +
            '<div class="col-sm-6">' +
                '<input type="text" id="password" class="form-control" placeholder=" password">' +
            '</div>' +
        '</div>' +
        '<a href="index.html" class="dribble">Login</a>' +

        '</form>'

    });
});
