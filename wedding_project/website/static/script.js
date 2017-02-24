function showRegistrationForm() {
	$('#login').css('display', 'none');
	$('#modal').css('display', 'block');
}

function closeRegistrationForm() {
	$('#login').css('display', 'inline-block');
	$('#modal').css('display', 'none');
}

function appendNewPresent() {
	var newId = parseInt($('#addButtonPresent').parent().parent().prev().children().attr('id').replace('present', '')) + 1;
	var newPresentInput = '<div class="row"><input id="present' + newId + '" type="text"/></div>';
	$('#addButtonPresent').parent().parent().before(newPresentInput);
}

function appendNewGuest() {
	var newId = parseInt($('#addButtonGuest').parent().parent().prev().children().attr('id').replace('guest', '')) + 1;
	var newGuestInput = '<div class="row"><input id="guest' + newId + '" type="text"/></div>';
	$('#addButtonGuest').parent().parent().before(newGuestInput);
}

function addNewSuggestions() {
	var newId = parseInt($('#addNewSuggestions').parent().parent().prev().children().attr('id').replace('guest', '')) + 1;
	var addNewSuggestionInput = '<div class="row"><input id="suggestion' + newId + '" type="text" placeholder="Add here..."/></div>';
	$('#addNewSuggestions').parent().parent().before(addNewSuggestionInput);
}

function saveList() {
	var presents = [];

	$('input[type="text"]').each(function() {
		presents.push($(this).val());
	});

	var postData = {
		presents: presents
	};
	$.post("./test.py", postData);
}