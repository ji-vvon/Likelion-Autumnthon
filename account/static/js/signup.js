$(document).ready( function() {
    $("input#id_username").attr("placeholder", "아이디")
    $("input#id_password1").attr("placeholder", "비밀번호")
    $("input#id_password2").attr("placeholder", "비밀번호 확인")
    $("input#id_email").attr("placeholder", "이메일")
    $("input#id_address").attr("placeholder", "주소")
});

$(document).ready(function(){
	$("#password_alert").click(function(){	
		$("#password_text").toggle('slow');
	});
});
