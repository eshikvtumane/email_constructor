$(document).ready(function(){
    $('#add_group').click(function(){
        cloneOption('select_groups', 'adding_groups');
    });

    $('#delete_group').click(function(){
        cloneOption('adding_groups', 'select_groups');
    });

    document.getElementById('select_groups').ondblclick = function(){
        cloneOption('select_groups', 'adding_groups');
    };

    document.getElementById('adding_groups').ondblclick = function(){
        cloneOption('select_groups', 'adding_groups');
    };

});



