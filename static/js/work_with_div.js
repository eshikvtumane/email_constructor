$(document).ready(function(){
    //http://xdsoft.net/jqplugins/datetimepicker/
    $('#datetimepicker').datetimepicker({
        lang:'ru',
        step:10
        /*allowTimes:[
          '12:00', '13:00', '15:00',
          '17:00', '17:05', '17:20', '19:00', '20:00'
         ]*/
    });

    $('#btn_next').click(function(){
        console.log('OK x 1');
        $('#email').hide();
        $('#setting').show();
        console.log('OK x 2');
    });

    $('#btn_back').click(function(){
        console.log('OK x 1');
        $('#setting').hide();
        $('#email').show();
        console.log('OK x 2');
    });

});