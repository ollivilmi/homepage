$(function() {
    $('#cvblock').hide();

    var clickables = document.getElementsByClassName('cvclick');

    for (var i = 0; i<clickables.length; i++)
        (function(i) {
            clickables[i].onclick = function()
        {
            $('#cvblock').show();
           //  window.scroll(0, 500);
           // TODO animation to scroll a bit down
            $('#cvp').html(clickables[i].id);
        }
        })(i);
});