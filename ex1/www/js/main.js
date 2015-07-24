/**
 * Created by egregors on 23.07.15.
 */

$.ajax({
    url: "/",
    success: function (data) {
        $('#resp').text(data);
        console.log(data)
    },
    error: function (e) {
        console.log('ERR:: ');
        console.log(e);
    }
});