$(window).scroll(function() {
    if($(this).scrollTop() > 200){
        $('.go-top').show();
    } else {
        $('.go-top').hide();
    }
});
$('.go-top').click(function() {
    $('html.body').animate({
        scrollTop: 0
    },1000);
        
    return false;
});