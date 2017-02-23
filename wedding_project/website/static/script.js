function showRegistrationForm() {
	$('#login').css('display', 'none');
	$('#modal').css('display', 'block');
}

function closeRegistrationForm() {
	$('#login').css('display', 'inline-block');
	$('#modal').css('display', 'none');
}

function appendNewPresent() {
	var newId = parseInt($('#addButton').parent().parent().prev().children().attr('id').replace('present', '')) + 1;
	var newPresentInput = '<div class="row"><input id="present' + newId + '" type="text"/></div>';
	$('#addButton').parent().parent().before(newPresentInput);
}

function saveList() {
	var presents = [];

	$('input[type="text"]').each(function() {
		presents.push($(this).val());
	});

	$.post("./test.py", presents);
}