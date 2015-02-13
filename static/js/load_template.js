function loadTemplate(template_id){
    //document.getElementById('template').innerHTML = '<object type="text/html" data="/media/' + template_url + '"></object>';
    document.getElementById('temp_id').value = template_id;
    //$('#template').load('/media/' + template_name);

    function_load = function(data){
        document.getElementById('template').innerHTML = data;


        $('.color').ColorPicker({

            onSubmit: function(hsb, hex, rgb, el) {
                $(el).val(hex);
                $(el).ColorPickerHide();
            },
            onBeforeShow: function () {
                $(this).ColorPickerSetColor(this.value);
            }
        })
        .bind('keyup', function(){
            $(this).ColorPickerSetColor(this.value);

        });

    }

    ajaxSend(
        'GET',
        '/constructor/template_load/' + template_id,
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