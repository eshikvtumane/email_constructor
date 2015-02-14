function loadTemplate(template_id){
    //document.getElementById('template').innerHTML = '<object type="text/html" data="/media/' + template_url + '"></object>';
    document.getElementById('temp_id').value = template_id;

    function_load = function(data){
        document.getElementById('template').innerHTML = data;


        CKEDITOR.replace('text', {
        language: 'ru'});

        CKEDITOR.config.extraPlugins = 'justify';

    }

    ajaxSend(
        'GET',
        '/constructor/template_load/' + template_id,
        { },
        function_load
    );


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