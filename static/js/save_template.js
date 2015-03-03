function templateSave(){
    document.getElementById('error-two').innerHTML = '<img src="/media/loader.GIF">';

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

    error_div = document.getElementById('error-two');
    if(datetime == ''){
        error_div.innerHTML = 'Выберите время отправки';
        return;
    }
    if(address == ''){
        error_div.innerHTML = 'Введите адрес';
        return;
    }
    if(validateEmail(address) == false){
        error_div.innerHTML = 'Введите адрес правильно';
        return;
    }

    //errors = inputsValidate(subject, title, text, footer)

// добаление данны
    form_data = new FormData();
    form_data.append('temp_id', template_id);
    form_data.append('subject', subject);


    form_data.append('background-color', bg_color);
    form_data.append('background-image', bg_img);
    form_data.append('head_background-color', header_color);
    form_data.append('head_background-image', header_img);

    form_data.append('footer', footer);
    form_data.append('social_buttons', social);

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
        form_data.append('text', text_inputs[i].value);
    }


    $.ajax({
        type:'POST',
        url:'/save_template/',
        data: form_data,
        processData: false,
        contentType: false,
        success:function(data){
            console.log(data);
            if(data=='200'){
                document.getElementById('error-two').innerHTML = '<label style="color: green">Письмо успешно сохранено</label>';
            }
            else{
                document.getElementById('error-two').innerHTML = 'Произошла ошибка. Пожалуйста, попробуйте произвести сохранение позже.';
            }
        }
    })


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

function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    console.log('ВВВвалидате')
    console.log(re.test(email))
    return re.test(email);
}