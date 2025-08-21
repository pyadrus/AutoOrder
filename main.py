from loguru import logger  # Логирование https://loguru.readthedocs.io/en/stable/overview.html

from prize_holiday import prize_holiday
from supplement_for_achievements_in_work import supplement_for_achievements_in_work
from supplement_for_work_wartime import supplement_for_work_wartime
from supplement_minimum_wage import supplement_minimum_wage

logger.add("log/log.log", rotation="1 MB")


def main():
    """Главное меню программы"""

    # Связываем месяцы с их номерами
    months = {
        "01": ["01", "январь"],
        "02": ["02", "февраль"],
        "03": ["03", "март"],
        "04": ["04", "апрель"],
        "05": ["05", "май"],
        "06": ["06", "июнь"],
        "07": ["07", "июль"],
        "08": ["08", "август"],
        "09": ["09", "сентябрь"],
        "10": ["10", "октябрь"],
        "11": ["11", "ноябрь"],
        "12": ["12", "декабрь"],
    }
    months_data = months.items()
    logger.debug(months_data)

    # Заполнение приказов
    for month_num, month_info in months.items():
        logger.debug(f"Обработка месяца: {month_num} - {month_info[1]}")

        logger.debug("Доплата за высокие достижения в труде")  # Доплата за высокие достижения в работе
        supplement_for_achievements_in_work(
            data_mounts=month_num,  # Месяц
            file_dog="Доплата_за_высокие_достижения_в_труде.docx",  # Файл
            year="2025"
        )

        logger.debug("Доплата до МРОТ")  # Доплата до МРОТ
        supplement_minimum_wage(
            data_mounts=month_num,
            file_dog="Доплата_до_МРОТ.docx",
            year="2025"
        )

        logger.debug("Доплата за работу в военное время")  # Доплата за работу в военное время
        supplement_for_work_wartime(
            data_mounts=month_num,
            file_dog="Доплата_за_работу_в_военное_время.docx",
            year="2025"
        )

        logger.debug("Премия к празднику")  # Премия к празднику
        prize_holiday(
            data_mounts=month_num,
            file_dog="Премия.docx",
            year="2025"
        )


if __name__ == "__main__":
    main()
