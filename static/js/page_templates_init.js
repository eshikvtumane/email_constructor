$(document).ready(function(){

// инициализация палитры с цветом
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
        })


    $(".fancybox").fancybox({
    helpers:  {
        thumbs : {
            width: 50,
            height: 50
        }
    }
});



// ---------------------------------------------------
});

function getImage(input, btn){
    var fullPath = input.value;
    if (fullPath) {
        $('#btn'+btn).css('background-color', '#1a9e06');
    }
    else{
        $('#btn'+btn).css('background-color', '#3399FF');
    }
}
