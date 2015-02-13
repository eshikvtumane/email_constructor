$(document).ready(function(){
    //http://xdsoft.net/jqplugins/datetimepicker/
    // инициализируем datapicker
    $('#datetimepicker').datetimepicker({
        lang:'ru',
        step:10,
        format:'Y-m-d H:i'
    });

    $('#btn_next').click(function(){
    // проверка: существуют ли данные элементы
        try{
            var subject = document.getElementById('subject').value;
            var title = document.getElementById('title').value;
            var text = CKEDITOR.instances.text.getData();
            var footer = document.getElementById('footer').value; // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        }
        catch(e){
            document.getElementById('errors').innerHTML = 'Выберите шаблон письма';
            return;
        }

        // проверка на пустые значения
        error_arr = inputsValidate(subject, title, text, footer)
        len = error_arr.length

        // если ошибок нет
        if(len == 0){
        // переход на следующий блок
            $('#email').hide();
            $('#setting').show();
        }
        else{
        // если есть ошибки, остаёмся
            list_err = '<ul>';
            for(var i = 0; i < len; i++){
                list_err += '<li>' + error_arr[i] + '</li>';
            }
            list_err += '</ul>';
            document.getElementById('errors').innerHTML = list_err;
        }
    });

    // кнопка возврата в блок с шаблоном письма
    $('#btn_back').click(function(){
        $('#setting').hide();
        $('#email').show();
    });

});

// проверка значений на пустые значения
function inputsValidate(subject, title, text, footer, input_image_name){
    error_arr = new Array();

    if(subject == ''){
        error_arr.push('Введите тему письма');
    }
    if(title == ''){
        error_arr.push('Введите заголовок в шаблоне');
    }
    if(text == ''){
        error_arr.push('Введите текст письма в шаблоне');
    }
    if(footer == ''){
        error_arr.push('Заполните футер');
    }

// валидация изображение
    image_count = 0;
    quantity_count = 0;
    var image_inputs = document.getElementsByTagName('input');
        inputs_len = image_inputs.length;
        for(var i = 0; i < inputs_len; i++) {
            if(image_inputs[i].type.toLowerCase() == 'file') {
                quantity_count += 1;
                if(image_inputs[i].files[0] != null){
                    image_count += 1;
                }
            }
        }

    // если количество инпутов равен количеству загруженных изображений
    if(image_count != quantity_count){
        error_arr.push('Добавлены не все картинки');
    }
    return error_arr
}