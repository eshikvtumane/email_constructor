$(document).ready(function(){
    $('#add_location').click(function(){
        cloneOption('locations', 'added_locations');
    });

    $('#delete_locations').click(function(){
        cloneOption('added_locations', 'locations');
    });

    document.getElementById('locations').ondblclick = function(){
        cloneOption('locations', 'added_locations');
    };

    document.getElementById('added_locations').ondblclick = function(){
        cloneOption('added_locations', 'locations');
    };

});