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
