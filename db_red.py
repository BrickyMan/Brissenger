import sqlite3

# Подключение к БД
conn = sqlite3.connect('common_chat.db')
# conn = sqlite3.connect('users.db')
# Создание курсора в БД
cursor = conn.cursor()
# cursor.execute('DROP TABLE messages')
# cursor.execute('''CREATE TABLE IF NOT EXISTS messages(
# 				msgId INTEGER PRIMARY KEY,
# 				userId INTEGER,
# 				msgDate VARCHAR,
# 				msgTime VARCHAR,
# 				msgText VARCHAR)''')
cursor.execute('DELETE FROM messages')

conn.commit()
conn.close()