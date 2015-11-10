/**
 * Created by k1 on 10/4/15.
 */
function moreTodo() {
    console.log(' >>> more-todo-form submiting <<<< ');
    $.ajax({ // create an AJAX call ...
        type: "POST", // GET or POST
        //url: $(this).attr('action'), // the file to call
        url: '/accounts/todo/more/', // the file to call
        dataType: "json",
        async: true,
        data: {
            'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            'username': "KeyvanGHanizadeh"
        },
        success: function (data) { // on success
            console.log('result : ' + data.result + " message : " + data.message);
            $('#more-todo-results').html('result : ' + data.result + " message : " + data.message);
        },
        error: function (xhr, textStatus, errorThrown) {
            $('#more-todo-results').html("Please report this error: " + errorThrown + xhr.status);
        }
    });

}

function addTodo() {
    $.ajax({
        type: $('#add-todo-form').attr('method'),
        //url: '/accounts/todo/add/',
        url: $('#add-todo-form').attr('action'),
        dataType: "json",
        async: true,
        data: {
            'item': $('#todo-item').val(),
            "username": "keyvan Ghanizadeh",
            'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (data) {
            console.log('result : ' + data.result + " message : " + data.message);
            $('#add-todo-results').html('result : ' + data.result + " message : " + data.message);
        },
        error: function (xhr, textStatus, errorThrown) {
            $('#add-todo-results').html("SOMEThing went WORNG " + errorThrown + " " + xhr.status);
        }
    });
}