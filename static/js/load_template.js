function loadTemplate(template_id, template_path){

    document.getElementById('temp_id').value = template_id;
    $('#template').load('/media/' + template_path);

    document.getElementById('errors').innerHTML = '';
    return false;
}

function templatePreview(){
    console.log(document.getElementById('title'));
}