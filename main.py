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
        "01": "01",
        "02": "02",
        "03": "03",
        "04": "04",
        "05": "05",
        "06": "06",
        "07": "07",
        "08": "08",
        "09": "09",
        "10": "10",
        "11": "11",
        "12": "12",
    }

    # Заполнение приказов
    for data_mounts, number_month in months.items():

        logger.debug("Доплата за высокие достижения в труде")  # Доплата за высокие достижения в работе
        supplement_for_achievements_in_work(
            data_mounts=data_mounts,  # Месяц
            file_dog="Доплата_за_высокие_достижения_в_труде.docx",  # Файл
            number_month=number_month,  # Номер месяца
        )

        logger.debug("Доплата до МРОТ")  # Доплата до МРОТ
        supplement_minimum_wage(
            data_mounts=data_mounts,
            file_dog="Доплата_до_МРОТ.docx",
            number_month=number_month,
        )

        logger.debug("Доплата за работу в военное время")  # Доплата за работу в военное время
        supplement_for_work_wartime(
            data_mounts=data_mounts,
            file_dog="Доплата_за_работу_в_военное_время.docx",
            number_month=number_month,
        )

        logger.debug("Премия к празднику")  # Премия к празднику
        prize_holiday(
            data_mounts=data_mounts,
            file_dog="Премия.docx",
            number_month=number_month
        )


if __name__ == "__main__":
    main()
