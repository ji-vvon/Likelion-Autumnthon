$(document).ready(function(){
	$(".reply_button").click(function(){	
		alert("good");
		$(this).closest("div").find(".reply_in").toggle();
	});
});