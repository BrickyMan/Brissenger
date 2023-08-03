import db_service
import re

def check_reg_data(name, login, password, password_repeat):
    if not (name and login and password):
        return (False, 'empty inputs')
    elif not validate_login(login):
        return (False, 'invalid login')
    elif not db_service.check_item(login, 'login'):
        return (False, 'login is already taken')
    elif password != password_repeat:
        return (False, 'passwords doesn\'t match')
    elif not validate_password(password):
        return (False, 'invalid password')
    return (True, 'success')

def validate_login(login):
    pattern = r'^[a-zA-Z0-9]{1,20}$'
    return bool(re.match(pattern, login))

def validate_password(password):
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d).{4,16}$'
    return bool(re.match(pattern, password))

print(validate_password('abcd1'))