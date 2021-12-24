$(document).ready(function(){
	$("#header").hover(function(){
		// $(this).css('width', '15%');
		$("#header_specific").css('height', '30vh');
	}, function(){
		// $(this).css('width', '10%');
		$("#header_specific").css('height', '0vh');
	});
});

$(document).ready(function(){
	$("#header_specific").hover(function(){
		$(this).css('height', '30vh');
	}, function(){
		$(this).css('height', '0vh');
	});
});
