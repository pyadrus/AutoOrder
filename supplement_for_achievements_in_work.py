import sqlite3

from docxtpl import DocxTemplate
from loguru import logger
from openpyxl import load_workbook


def supplement_for_achievements_in_work(data_mounts, file_dog):
    """Доплата за высокие достижения в работе"""

    def record_data_salary_downtime_week():
        """Заполнение приказа"""
        doc = DocxTemplate(file_dog)

        # Получаем данные из базы данных
        rows = get_data_from_db()
        table_data = prepare_table_data(rows)

        context = {
            "data_mounts": f" {data_mounts} ",
            "table_data": table_data  # Передаем данные для таблицы
        }

        doc.render(context)
        doc.save(f"data/Доплата_за_высокие_достижения_в_труде_{data_mounts}.docx")

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

    def prepare_table_data(rows):
        """Подготовка данных для таблицы"""
        table_data = []
        for row in rows:
            table_data.append({
                "table_number": row[0],  # Табельный номер
                "surname_name_patronymic": row[1],  # ФИО
                "profession": row[2],  # Профессия
                "percent": row[3]  # Процент
            })
        return table_data

    def property_parsing():
        """Парсинг данных"""
        try:
            conn, cursor = opening_the_database()
            # Открываем выбор файла Excel для чтения данных
            workbook = load_workbook(filename='data/124.xlsx')  # Загружаем выбранный файл Excel
            sheet = workbook.active

            # Создаем таблицу в базе данных, если она еще не существует
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS data (table_number, surname_name_patronymic, profession, percent)')

            cursor.execute('DELETE FROM data')
            conn.commit()  # сохранить изменения

            # Считываем данные из колонок и вставляем их в базу данных
            for row in sheet.iter_rows(min_row=3, max_row=23, values_only=True):
                try:
                    # Проверяем, что строка содержит достаточно данных
                    if len(row) > 11:  # Убедимся, что в строке есть хотя бы 12 столбцов
                        table_number = row[1]  # table_number - табельный номер,
                        surname_name_patronymic = row[2]  # surname_name_patronymic - фамилия,
                        profession = row[5]  # profession - профессия,
                        percent = row[11]  # percent - процент

                        # Логируем данные для отладки
                        logger.info(
                            f'Данные для вставки: {table_number}, {surname_name_patronymic}, {profession}, {percent}')

                        # Вставляем данные в таблицу
                        cursor.execute('INSERT INTO data VALUES (?, ?, ?, ?)',
                                       (table_number, surname_name_patronymic, profession, percent))
                    else:
                        logger.warning(f"Строка содержит недостаточно данных: {row}")
                except Exception as e:
                    logger.error(f"Ошибка при обработке строки {row}: {e}")

            # Сохраняем изменения в базе данных и закрываем соединение
            conn.commit()
            conn.close()
        except Exception as e:
            logger.exception(e)

    property_parsing()
    record_data_salary_downtime_week()
