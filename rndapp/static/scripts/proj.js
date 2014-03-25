$(document).ready( function() {
	$("#addproj.phide").click( function() {
		if( $(this).hasClass("pshow") ) {
			$(this).removeClass("pshow").addClass("phide");
			$("#projform").hide(400);
		} else {
			$(this).removeClass("phide").addClass("pshow");
			$("#projform").show(400);
		}
	});
	$("#projform").hide();
});