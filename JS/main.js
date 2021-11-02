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

// 추천책 클릭 시
$(document).ready(function(){
	$("#recommend_book").click(function(){	
		$("#book_recommend").css('display', 'flex');
		$("#book_new").css('display', 'none');
		$("#book_solution").css('display', 'none');
	});
});

// 새로운책 클릭 시
$(document).ready(function(){
	$("#new_book").click(function(){	
		$("#book_recommend").css('display', 'none');
		$("#book_new").css('display', 'flex');
		$("#book_solution").css('display', 'none');
	});
});

// 최근 솔루션 등록 클릭 시
$(document).ready(function(){
	$("#solution_book").click(function(){	
		$("#book_recommend").css('display', 'none');
		$("#book_new").css('display', 'none');
		$("#book_solution").css('display', 'flex');
	});
});