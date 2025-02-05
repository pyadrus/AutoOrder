import sqlite3


def opening_the_database():
    """Открытие базы данных"""
    conn = sqlite3.connect('data/data.db')  # Создаем соединение с базой данных
    cursor = conn.cursor()
    return conn, cursor


def get_data_from_db():
    """Извлечение данных из базы данных"""
    conn, cursor = opening_the_database()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()  # Получаем все строки из таблицы
    conn.close()
    return rows


if __name__ == '__main__':
    opening_the_database()
    get_data_from_db()
