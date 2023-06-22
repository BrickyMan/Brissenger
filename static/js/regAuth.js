import {hideElem, showElem} from 'util.js';

function verifyLogin(login) {

}

function postRequest(url, data) {
	let xhr = new XMLHttpRequest();
	xhr.open('POST', `/${url}`, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4 && xhr.status === 200) {
			return(xhr.responseText);
		}
		else {
			console.log('Error');
		}
	};
	xhr.send(JSON.stringify(data));
}