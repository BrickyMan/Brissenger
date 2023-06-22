let msgTextarea = document.querySelector('#msgTextarea'),
	msgSentForm = document.querySelector('#msgSentForm');

msgTextarea.addEventListener('keypress', (e) => {
	if (e.key == 'Enter' && !e.ctrlKey && !e.shiftKey) {
		e.preventDefault();
		msgSentForm.submit();
	}
});