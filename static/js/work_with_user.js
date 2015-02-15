$(document).ready(function(){
    $('#add_users').click(function(){
        cloneOption('searching_users', 'added_users');
    });

    $('#delete_users').click(function(){
        cloneOption('added_users', 'searching_users');
    });
});


function userSearch(){
       console.log($('#search_user').val());
       searching_word = $('#search_user').val();
        $.ajax({
            beforeSend:function(){
                console.log('Отправка ...');
                $('#searching_users option').remove();
            },
            type: 'GET',
            url:'/constructor/search_users/',
            data:{
                's_word': searching_word
            },
            dataType: 'json',
            success:function(data){
                console.log('-----------------------');
                console.log(data);
                count = 0;
                result_search = ''
                while(data[count]){
                    result_search += '<option value="' + data[count]['id'] + '">' + data[count]['company_name'] + '</option>';
                    count += 1
                }

                $('#searching_users').append(result_search);
            },
            complete: function(){
                console.log('Конец');
            }
        });
}