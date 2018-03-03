$(function(){
  $("div").fadeOut(1);

  $(window).scroll(function(){
    if ($(window).scrollTop() > 350) {
        $("div").fadeIn();
      }
  });
});