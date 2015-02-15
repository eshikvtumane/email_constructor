function templateSave(){
    var subject = document.getElementById('subject').value;
    var title = document.getElementById('title').value;
    var text = document.getElementById('text').value;
    //var image = document.getElementById('image');
    var video = document.getElementById('video').value;

    var groups = selectToArray('adding_groups');
    var users = selectToArray('added_users');
    var locations = selectToArray('added_locations');
    var datetime = document.getElementById('datetimepicker').value;

    console.log(subject);
    console.log(title);
    console.log(datetime);

    console.log(locations);

    form_data = new FormData();

    $.ajax({
        type:'POST',
        url:'',
        data:'',
        success:function(data){

        }
    })
}

function selectToArray(select_id){
    var select_obj = document.getElementById(select_id);
    option_value = new Array();
    select_length = select_obj.length;

    for(var i = 0; i < select_length; i++){
        option_value.push(select_obj.options[i].value);
    }

    return option_value;
}