/*$(function(){
  $(".edit").on('mouseenter',function(){
    $(this).children("span").children().children().prop("disabled",false);
  });
  $(".edit").on('mouseleave',(function(){
    $(this).children("span").children().children().prop("disabled",true);
  });
  
  /*$(".regItem").mouseenter(function(){
    $(this).children().css("display", "block");
  });
  $(".regItem").mouseleave(function(){
    $(this).children().css("display", "none");
  });*/
  /*
});

$("a").click(function(){
  $.get('/test',function(data){
    $("#result").text(data.name);
  });
});

$("#submit").on("click", function() {
  var input = $("#tFormInput").val();
  $.ajax({
    url: "/", 
    method: "POST",
    data: { input: input },
    dataType: "json"
    });
  return false;
});

var id = 1;
var offset = 5;

$("#loadMore").on('click',function(){
  var loadIndex = id; //$("#loadIndex").val();
  var loadOffset = offset; //$("#loadOffset").val();
  var url="/getItem/"+loadIndex+"/"+loadOffset;
  var item;
  
  $.get(url,function(data){
    for (item in data) {
      $("fieldset").append("<hr>"+"<strong>ID: </strong>" + item.id + "<br>"+"<strong>URL: </strong>" + item.imgurl + "<br>"+"<strong>Name: </strong>" + item.name + "<br>"+"<strong>Price: </strong>" + item.price + "<br>"+"<strong>Type: </strong>" + item.type + "<br>"+"<hr>");
      id = item.id;
    }
  });
  return false;
});*/

/*function login(input){
  clearPage();
  if ((typeof input) == "object") {
    $("#container").append("<h1>Welcome "+ input.username +"!</h1>");
  } else {
    $("#container").append("<h1>Welcome Guest!</h1>");
  }
}*/

function clearPage(){
  $.each($("#container *"),function(){
    $(this).remove();
  });
  
  return false;
}

$("#postContent").on('keypress',function(e){
if (e.key=='Enter'){
  $("#postBtn").trigger("click");
} else {
  console.log("wew");
}
});

$("#postBtn").on('click',function(e){
//alert($("#postContent").text());
if ($("#postContent").text().length > 0){
    var postContent = $("#postContent").val();
    var date = new Date();
    
    $.post("/sendPost/",
    {
      'reply':postContent,
      'timestamp':date
    }, function (data, status) {
      window.location.replace("/");
    }); 
  } else {
    alert("The field is empty");
  }
});

var enndex = $("#postContainer div:last-of-type p[class*='id']").text();
var offset = 5;
  
$("#showMore").on('click',function(e){
  $("#postContainer").append("<h1 id='loading'>Loading posts...</h1>")
    
  $.post("/getPost/",
  {
    'index': enndex,
    'offset': offset
  }, function(data, status){  
    $.each(data,function(index,obj){
      if (parseInt(obj.id) != parseInt($("#postContainer div:last-of-type p[class*='id']").text())) {
        $("#postContainer").append("<div class='card'><div class='card-header'><p class='id'>"+obj.id+"</p></div><div class='card-body'><div class='card-title'><h5 class='username'>"+obj.username+"</h5></div><div class='card-text'><p class='reply'>"+obj.reply+"</p></div></div><div class='card-footer'><em class='timestamp'>"+obj.timestamp+"</em></div></div>");
        enndex = obj.id;
      } else {
        console.log("lmao");
        void(0);
      }
    });
  $("#postContainer #loading").remove();
  });  
});

$("#regUser").on('click',function(e){
  e.preventDefault();
  
  var username = $("#regUsername").val();
  var password = $("#regPassword").val();
  var email = $("#regEmail").val();
  var url = "/register/";

  $("#regError").append("<h1>[Registering user...]</h1>");
  
  $.post(url,
    {'username':username,
    'password':password,
    'email':email},
    function(data, status) {
      $("#regError h1").remove();
      alert("Data: "+JSON.stringify(data)+", Status: "+status);
      window.location.replace("/");
    });
});

$("#logout").on('click',function(e){
  $.get('/logout/', function(data){
    window.location.replace("/");
  });
});

$("#login").on('click',function(e){
  if (($("#username").val() === "") || ($("#password").val() === "")){
    alert("Fields must not be empty");
    return false;
  }
  var username = $("#username").val();
  var password = $("#password").val();
  var url = "/login/";
  
  $.post(url,{
    'username':username,
    'password':password
  },
  function(data, status){
    if (data.username) {
    window.location.replace("/");
    } else {
    $("#container").append(data.status);
  }
  });
  
  e.preventDefault();
  return false;
});

$(".carouSlick").slick();