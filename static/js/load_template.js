function loadTemplate(template_id, template_path){

    document.getElementById('temp_id').value = template_id;
    //$('#template').load('/media/' + template_path);

    function_load = function(data){
        document.getElementById('template').innerHTML = data;
         //turn all textareas on the page into editors
           nicEditors.allTextAreas( );
    }

    document.getElementById('template').innerHTML = '<img src="/media/loader.GIF">';
    ajaxSend(
        'GET',
        '/template_load/' + template_id,
        { },
        function_load
    );

    document.getElementById('errors').innerHTML = '';
    return false;
}


function ajaxSend(method_type, template_url, data, function_success){

    $.ajax({
        type: method_type,
        url: template_url,
        data: data,
        success: function_success
    });
}

function templatePreview(){
    console.log(document.getElementById('title'));
}

function previewValidate(){
    id_template = document.getElementById('temp_id').value;
    if(id_template == ''){

        document.getElementById('errors').innerHTML = 'Выберите шаблон собщения';
        return false;
    }
    return true;
}
