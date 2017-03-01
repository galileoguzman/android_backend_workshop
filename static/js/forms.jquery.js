$(document).ready(function(){
	
	if ($('.modal').length > 0) {

		console.log("modal exists");

		$('.modal-trigger').leanModal();
		$("#on_errors").trigger("click");
	}


	$('#new_post').submit(function(){
		swal("Buen trabajo!", "Tu información fue procesada con exito!", "success")
	});

	
});
          