/**
 Bootstrap Alerts -
 Function Name - showalert()
 Inputs - message,alerttype
 Example - showalert("Invalid Login","alert-error")
 Types of alerts -- "alert-error","alert-success","alert-info","alert-warning"
 Required - You only need to add a alert_placeholder div in your html page wherever you want to display these alerts "<div id="alert_placeholder"></div>"
 Written On - 14-Jun-2013
 **/
function showalert(message, alerttype) {

    $('#alert_placeholder').append('<div id="alertdiv" class="alert ' + alerttype + '"><a class="close" data-dismiss="alert">×</a><span>' + message + '</span></div>')
    setTimeout(function () { // this will automatically close the alert and remove this if the locations doesnt close it in 5 secs
        $("#alertdiv").remove();
    }, 15000);
}


//show alert message
var messages = document.getElementsByClassName('show-message')
for (var i = 0; i < messages.length; i++) {
    showalert(messages[i].getAttribute('data-message'), 'alert-info')
}


  $(document).on('click', '.delete', function () {
        $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
      });

    $(document).on('click', '#confirmDeleteButtonModal', function () {
      var caller = $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id");
      window.location = $("#".concat(caller)).attr("href");
    });