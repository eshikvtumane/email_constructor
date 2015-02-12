$(document).ready(function(){
    $('#add_group').click(function(){
        cloneOption('select_groups', 'adding_groups');
    });

    $('#delete_group').click(function(){
        cloneOption('adding_groups', 'select_groups');
    });
});

