// import {hideElem, showElem} from 'util.js';

function checkInput(event) {
	postRequest(`reg_${event.target.name}_check`, {'value': event.target.value})
		.then(function(response) {
			console.log(response); // Обработка успешного ответа
			if (response == 'Failed') {
				event.target.classList.add('input-check_failed');
			}
			else {
				event.target.classList.remove('input-check_failed');
			}
		})
		.catch(function(error) {
			console.error(error); // Обработка ошибки
		});
}

function postRequest(url, data) {
	// Возвращаем новый промис, который позволит обрабатывать асинхронный запрос
	return new Promise(function(resolve, reject) {
		// Создаем объект XMLHttpRequest для отправки запроса
		let xhr = new XMLHttpRequest();
		xhr.open('POST', `/${url}`, true);
		xhr.setRequestHeader('Content-Type', 'application/json');
		
		// Устанавливаем обработчик события onreadystatechange
		xhr.onreadystatechange = function() {
			// Проверяем состояние и статус запроса
			if (xhr.readyState === 4) {
				if (xhr.status === 200) {
					// Если запрос успешен, вызываем функцию resolve с ответом сервера
					let res = xhr.responseText;
					resolve(res);
				} else {
					// Если произошла ошибка, вызываем функцию reject с кодом ошибки
					reject(xhr.status);
				}
			}
		};
		
		// Отправляем данные на сервер в формате JSON
		xhr.send(JSON.stringify(data));
	});
}

function checkPassword(event) {
	if (event.target.value.match(/^(?=.*\d).{4,16}$/)) {
		event.target.classList.remove('input-check_failed');
	}
	else {
		event.target.classList.add('input-check_failed');
	}
}