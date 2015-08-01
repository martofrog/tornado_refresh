/**
 *
 * Created by martofrog on 01/08/15.
 */

function update_table(data) {
    $("#main_tab tbody").html(data)
}

(function poll() {
    $.ajax({
        url: "/refresh",
        type: "GET",
        success: function(data) {
            console.log("received data");
            update_table(data)
        },
        dataType: "html",
        complete: setTimeout(function() {poll()}, 2000),
        timeout: 1000
    })
})();