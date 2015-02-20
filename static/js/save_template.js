function templateSave(){
    var template_id = parseInt(document.getElementById('temp_id').value);


    var subject = document.getElementById('subject').value;

    // цвет фона
    var bg_color = document.getElementById('background-color').value;
    // картинка для фона
    var bg_img = document.getElementById('background-image').files[0];
    // цвет фона шапки
    var header_color = document.getElementById('head_background-color').value;
    // картинка для фона шапки
    var header_img = document.getElementById('head_background-image').files[0];

    // фон футера
    var footer = document.getElementById('footer').value; // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    var social = document.getElementById('check').checked;
    console.log(social);

    var groups = selectToArray('adding_groups');
    var users = selectToArray('added_users');
    var locations = selectToArray('added_locations');
    var datetime = document.getElementById('datetimepicker').value;
    var address = document.getElementById('address').value;
    console.log(address)
/*
    if(datetime == ''){
        document.getElementById('error-two').innerHTML = 'Выберите время отправки';
        return;
    }
    if(address = ''){
        document.getElementById('error-two').innerHTML = 'Введите адрес';
        return;
    }
*/
    //errors = inputsValidate(subject, title, text, footer)

      len = 0;
    if(len == 0){

        form_data = new FormData();
        form_data.append('temp_id', template_id);
        form_data.append('subject', subject);


        form_data.append('background-color', bg_color);
        form_data.append('background-image', bg_img);
        form_data.append('head_background-color', header_color);
        form_data.append('head_background-image', header_img);

        form_data.append('footer', footer);
        form_data.append('social_button', social);

        // добавление групп
        form_data.append('groups', JSON.stringify(groups));
        form_data.append('users', JSON.stringify(users));
        form_data.append('locations',JSON.stringify(locations));
        form_data.append('datetime', datetime);
        form_data.append('address', address);


        // добавление изображений
        var inputs = document.getElementsByName('image');
        inputs_len = inputs.length;
        for(var i = 0; i < inputs_len; i++) {
            form_data.append('images', inputs[i].files[0]);
        }

        // добавление текста
        var text_inputs = document.getElementsByName('text');
        var inputs_len = text_inputs.length;
        for(var i = 0; i < inputs_len; i++) {
            form_data.append('texts', text_inputs[i].value);
        }

        // добавление цвета
       /* var colors = document.getElementsByName('color[]');
        colors_len = colors.length;
        for(var i = 0; i < colors_len; i++){
            console.log(colors[i].value);
            form_data.append('colors', colors[i].value);
        }*/


        $.ajax({
            type:'POST',
            url:'/constructor/save_template/',
            data: form_data,
            processData: false,
            contentType: false,
            success:function(data){
                console.log(data);
                if(data=='200'){
                    document.getElementById('error-two').innerHTML = 'Шаблон и параметры успешно сохранены';
                }
                else{
                    document.getElementById('error-two').innerHTML = 'Произошла ошибка. Пожалуйста, попробуйте произвести сохранение позже.';
                    document.getElementById('error-two').innerHTML = 'Произошла ошибка. Пожалуйста, попробуйте произвести сохранение позже.';
                }
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

