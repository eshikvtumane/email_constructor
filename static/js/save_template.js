function templateSave(){
    var template_id = parseInt(document.getElementById('temp_id').value);


    var subject = document.getElementById('subject').value;
    var title = document.getElementById('title').value;
    var text = CKEDITOR.instances.text.getData();
    //var image = document.getElementById('image');
    var video = document.getElementById('video').value;
    //var footer = document.getElementById('footer').value; // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    footer = ''

    var groups = selectToArray('adding_groups');
    var users = selectToArray('added_users');
    var locations = selectToArray('added_locations');
    var datetime = document.getElementById('datetimepicker').value;


    errors = inputsValidate(subject, title, text, footer)


    if(errors.length == 0){

        form_data = new FormData();
        form_data.append('temp_id', template_id);
        form_data.append('subject', subject);
        form_data.append('title', title);
        form_data.append('text', text);
        form_data.append('multi_url', video);
        form_data.append('footer', footer);

        // добавление групп
        form_data.append('groups', JSON.stringify(groups));
        form_data.append('users', JSON.stringify(users));
        form_data.append('locations',JSON.stringify(locations));
        form_data.append('datetime', datetime);


        var image_inputs = document.getElementsByTagName('input');
        inputs_len = image_inputs.length;
        for(var i = 0; i < inputs_len; i++) {
            if(image_inputs[i].type.toLowerCase() == 'file') {
                form_data.append('images', image_inputs[i].files[0]);
            }
        }

        $.ajax({
            type:'POST',
            url:'/constructor/save_template/',
            data: form_data,
            processData: false,
            contentType: false,
            success:function(data){
                console.log(data);
            }
        })
    }
    else{
        len = error_arr.length;
        for(var i = 0; i < len; i++){

        }
    }
}

function selectToArray(select_id){
    var select_obj = document.getElementById(select_id);
    option_value = new Array();
    select_length = select_obj.length;

    for(var i = 0; i < select_length; i++){
        option_value.push(parseInt(select_obj.options[i].value));
    }

    return option_value;
}

