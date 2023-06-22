import sqlite3

# Подключение к БД
conn = sqlite3.connect('common_chat.db')
# Создание курсора в БД
cursor = conn.cursor()
cursor.execute('DROP TABLE messages')
cursor.execute('''CREATE TABLE IF NOT EXISTS messages(
				msgId INTEGER PRIMARY KEY,
				userId INTEGER,
				msgDate VARCHAR,
				msgTime VARCHAR,
				msgText VARCHAR)''')

conn.commit()
conn.close()