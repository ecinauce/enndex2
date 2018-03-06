$(function(){
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function isNear( element, distance, event ) {

    var left = element.offset().left - distance,
        top = element.offset().top - distance,
        right = left + element.width() + 2*distance,
        bottom = top + element.height() + 2*distance,
        x = event.pageX,
        y = event.pageY;

    return ( x > left && x < right && y > top && y < bottom );

}

var points = 0;
var speed = 1000;

$(document).bind('mousemove', function(e){
  if (isNear($("#ball"),20,e)){
    $("#ball").animate({
      left: getRandomInt(0,$(window).width()),
      top: getRandomInt(0,$(window).height())
      }, 200);
    $(".banner").text("Catch the ball :)");
  }
  });

$("#ball").on('click',function(e){
  alert("Congratulations! You just WON the game!");
  $(location).attr("href","/");
  /*points++;
  speed-=100;
  ("#ball").remove();
  $(document).append("<div id='ball'></div>");
  $("#points").text(points);*/
});

});