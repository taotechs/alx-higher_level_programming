$(function()
{
    $('input#language_code').bind('keypress', function(event){
        if(event.key === 'Enter'){
            event.preventDefault();
            $('input#btn_translate').click();
        }
    })

    $('input#btn_translate').bind('click', function() {
        let lang = $('input#language_code').val();
        $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`, function(data, res){
            $('div#hello').text(data.hello);
        });   

    })
});