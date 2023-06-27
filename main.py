from flask import Flask, render_template, request, redirect, session, jsonify, url_for
from flask_socketio import SocketIO, emit
import db_service

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
socketio = SocketIO(app)

# Проверка авторизованности пользователя
def check_session():
	try:
		if session['authed_id']:
			return True
		else:
			return False
	except:
		if 'authed_id' not in session:
			session['authed_id'] = None
		return False

# РЕГИСТРАЦИЯ

# Открытие регистрации
@app.route('/reg')
def open_reg():
	error = request.args.get('error')
	if check_session():
		return redirect('common_chat')
	return render_template('reg.html', error = error)

# Запуск регистрации
@app.route('/reg_run', methods=['POST', 'GET'])
def reg_run():
	input_name = request.form['name']
	input_login = request.form['login']
	input_password = request.form['password']
	input_password_repeat = request.form['password-repeat']
	if input_name and input_login and input_password and (input_password == input_password_repeat):
		if db_service.register_user(input_login, input_password, input_name):
			return redirect('auth')
	return redirect('reg?error=reg_failed')

# Проверка логина при регистрации по AJAX
@app.route('/reg_login_check', methods = ['POST'])
def reg_login_check():
	data = request.get_json()
	if db_service.check_item('login', data['value']):
		return 'OK'
	return 'Failed'

# АВТОРИЗАЦИЯ

# Открытие авторизации
@app.route('/auth')
def open_auth():
	error = request.args.get('error')
	if check_session():
		return redirect('common_chat')
	return render_template('auth.html', error = error)

# Запуск авторизации
@app.route('/auth_run', methods=['POST', 'GET'])
def auth_run():
	# auth_data = request.get_json()
	# input_login = auth_data.get('login')
	# input_password = auth_data.get('password')
	input_login = request.form['login']
	input_password = request.form['password']
	# return 'Wrong login or password'
	print('data:', input_login, input_password)
	print('result:',db_service.check_auth(input_login, input_password))
	# Проверка логина и пароля
	if db_service.check_auth(input_login, input_password):
		session['authed_id'] = db_service.get_id(input_login)
		return redirect('common_chat')
	else:
		return redirect('auth?error=auth_failed')

# Вход в аккаунт
@app.route('/common_chat')
def open_common_chat():
	if not check_session():
		return redirect('auth')
	return render_template(
		'chat.html',
		id = session['authed_id'],
		name = db_service.get_userdata_item(session['authed_id'], 'name'),
		msgs_list = db_service.get_all_messages(),
		styles = ['chat'],
		scripts = ['menu', 'chat'])

# @app.route('/common_chat/update', methods = ['GET'])
# def update_common_chat():
# 	return db_service.get_all_messages()

# Страница пользователя
@app.route('/id<int:user_id>')
def open_my_page(user_id):
	if not check_session():
		return redirect('auth')
	return render_template(
		'userpage.html',
		id = session['authed_id'],
		name = db_service.get_userdata_item(session['authed_id'], 'name'),
		userdata = db_service.get_userdata(session['authed_id']),
		styles = ['userpage'],
		scripts = ['menu'])

# Выход из аккаунта и редирект на авторизацию
@app.route('/sign_out', methods=['POST', 'GET'])
def sign_out():
	session['authed_id'] = None
	return redirect('auth')

# ЧАТ

# Отправка сообщения по веб-сокету
@socketio.on('message')
def handle_message(message):
	db_service.send_message(message, session['authed_id'])
	emit('response', db_service.get_last_message(), broadcast=True)

# Отправка сообщения
@app.route('/send_msg', methods=['POST'])
def send_msg():
	msg_text = request.form['new-msg-text']
	db_service.send_message(msg_text, session['authed_id'])
	return redirect('common_chat')

# Корневой адрес
@app.route('/')
def open_main():	
	if not check_session():
		return redirect('auth')
	else:
		return redirect('common_chat')

# Запуск локального сервера
if __name__ == '__main__':
	socketio.run(app, host = '0.0.0.0')