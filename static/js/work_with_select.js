function cloneOption(from_clone, to_clone){

        $selected_options = $('#' + from_clone + ' > option:selected');
        var $options = $selected_options.clone();
        deleteOption(from_clone);

        console.log($options);
        $('#' + to_clone).append($options);
}

function deleteOption(from_delete){

    $('#' + from_delete + ' > option:selected').remove();
}