/**
 * Created by egregors on 23.07.15.
 */

$.ajax({
    url: "/api/",
    type: "GET",
    success: function (data) {
        $('#resp').text(data['status']);
    },
    error: function (e) {
        $('#resp').test("FAILED!");

        console.log('ERR:: ');
        console.log(e);
    }
});

$.ajax({
    url: "/api/",
    type: "POST",
    data: {state: "very ok!"},
    success: function (data) {
        console.log(data)
    },
    error: function (e) {
        $('#resp').text("FAILED!");

        console.log('ERR:: ');
        console.log(e);
    }
});