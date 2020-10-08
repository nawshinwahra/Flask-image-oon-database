$(document).ready(function(e) {
	
$('#addimage').click(function(e) {
		$( "#msg" ).html('');
		var packagename = $('#packagename').val();
		var packagephoto_data = $('#packagephoto').prop('files')[0];
		var packagephoto2_data = $('#packagephoto2').prop('files')[0];

		var form_data = new FormData();

		form_data.append('packagephoto_name', packagephoto_data);
		form_data.append('packagephoto2_name', packagephoto2_data);
		form_data.append('packagename', packagename);
		$.ajax({
			url: "upload.php",
			type: 'POST',
			contentType: false,
			processData: false,
			data: form_data,
			success: function(data){
				if(data != '') {
				$( "#msg" ).append(data);
				} else {
				$( "#msg" ).append('No Data Found');       
				}
			}

		});
	});	
	
});   