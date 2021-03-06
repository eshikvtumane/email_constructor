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

        // проверка на пустые значения
        error_arr = inputsValidate('subject','temp_id');
        len = error_arr.length

        //var len = 0
        // если ошибок нет
        if(len == 0){
        // переход на следующий блок
            document.getElementById('errors').innerHTML = '';
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
function inputsValidate(subject, template){
    error_arr = new Array();

    if(document.getElementById(template).value == ''){
        error_arr.push('Выберите шаблон');
    }

    if(document.getElementById(subject).value == ''){
        error_arr.push('Введите тему письма');
    }

// валидация изображение
    /*image_count = 0;
    quantity_count = 0;
    var image_inputs = document.getElementsByName('image');
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
    }*/
    return error_arr
}