$(document).ready(function(){
	$(".reply_button").click(function(){	
		$(this).closest(".reply_container").find(".reply_in").toggle();
	});
});