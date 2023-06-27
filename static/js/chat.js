let msgTextarea = document.querySelector('#msgTextarea'),
	msgSentForm = document.querySelector('#msgSentForm'),
	chatMsgsList = document.querySelector('#chatMsgsList');

	
let socket = io.connect('http://' + document.domain + ':' + location.port);

// Установление соединения по веб-сокету
socket.on('connect', function() {
	console.log('Connected to the server!');
});

// Слушание события нажатия на Enter в поле ввода сообщения
msgTextarea.addEventListener('keypress', (e) => {
	if (e.key == 'Enter' && !e.ctrlKey && !e.shiftKey) {
		sendMessage(e);
	}
});

// Отправка сообщения по веб-сокету
function sendMessage(event) {
	event.preventDefault();
	let message = msgTextarea.value;
	msgTextarea.value = '';
	socket.emit('message', message);	
}

// Получение нового сообщения по веб-сокету
socket.on('response', function(response) {
	console.log('Server response:', response);
	showNewMessage(response);
});

// Создание структуры нового сообщения на сайте
function showNewMessage(msgData) {
	// Создание элементов
	let li = document.createElement('li');
	li.setAttribute('msg-id', msgData['msgId']);

	let div = document.createElement('div');
	div.setAttribute('class', 'msg-header');

	let link = document.createElement('a');
	link.setAttribute('href', '/id' + msgData['userId']);
	link.setAttribute('class', 'msg-header_user');
	link.textContent = msgData['userName'];

	let p1 = document.createElement('p');
	p1.setAttribute('class', 'msg-header_datetime');
	p1.textContent = msgData['msgDate'] + ' ' + msgData['msgTime'];

	let p2 = document.createElement('p');
	p2.setAttribute('class', 'msg-body');
	p2.textContent = msgData['msgText'];

	// Добавление элементов в структуру
	div.appendChild(link);
	div.appendChild(p1);

	li.appendChild(div);
	li.appendChild(p2);

	// Добавление нового сообщения в чат
	chatMsgsList.appendChild(li);
}