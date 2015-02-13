$(document).ready(function(){
    //http://xdsoft.net/jqplugins/datetimepicker/
    $('#datetimepicker').datetimepicker({
        lang:'ru',
        step:10,
        format:'Y-m-d H:i'
    });

    $('#btn_next').click(function(){
        try{
            var subject = document.getElementById('subject').value;
            var title = document.getElementById('title').value;
            var text = CKEDITOR.instances.text.getData();
            //var image = document.getElementById('image');
            var footer = document.getElementById('footer').value; // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        }
        catch(e){
            document.getElementById('errors').innerHTML = 'Выберите шаблон письма';
            return;
        }


        error_arr = inputsValidate(subject, title, text, footer)
        len = error_arr.length
        if(len == 0){
            console.log('OK x 1');
            $('#email').hide();
            $('#setting').show();
            console.log('OK x 2');
        }
        else{
            list_err = '<ul>';
            for(var i = 0; i < len; i++){
                list_err += '<li>' + error_arr[i] + '</li>';
            }
            list_err += '</ul>';
            document.getElementById('errors').innerHTML = list_err;
        }
    });

    $('#btn_back').click(function(){
        console.log('OK x 1');
        $('#setting').hide();
        $('#email').show();
        console.log('OK x 2');
    });

});

function inputsValidate(subject, title, text, footer){
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

    return error_arr
}