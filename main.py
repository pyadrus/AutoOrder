from loguru import logger  # Логирование https://loguru.readthedocs.io/en/stable/overview.html

from prize_holiday import prize_holiday
from supplement_for_achievements_in_work import supplement_for_achievements_in_work
from supplement_for_work_wartime import supplement_for_work_wartime
from supplement_minimum_wage import supplement_minimum_wage

logger.add("log/log.log", rotation="1 MB")

# Связываем месяцы с их номерами
months = {
    "январь": "01_25",
    "февраль": "02_25",
    "март": "03_25",
    "апрель": "04_25",
    "май": "05_25",
    "июнь": "06_25",
    "июль": "07_25",
    "август": "08_25",
    "сентябрь": "09_25",
    "октябрь": "10_25",
    "ноябрь": "11_25",
    "декабрь": "12_25",
}

# Заполнение приказов
for data_mounts, number_month in months.items():
    # Доплата за высокие достижения в работе
    logger.debug("Доплата за высокие достижения в труде")
    supplement_for_achievements_in_work(
        data_mounts=data_mounts,  # Месяц
        file_dog="Доплата_за_высокие_достижения_в_труде.docx",  # Файл
        number_month=number_month,  # Номер месяца
    )

    # Доплата до МРОТ
    logger.debug("Доплата до МРОТ")
    supplement_minimum_wage(
        data_mounts=data_mounts,
        file_dog="Доплата_до_МРОТ.docx",
        number_month=number_month,
    )

    # Доплата за работу в военное время
    logger.debug("Доплата за работу в военное время")
    supplement_for_work_wartime(
        data_mounts=data_mounts,
        file_dog="Доплата_за_работу_в_военное_время.docx",
        number_month=number_month,
    )

    # Премия к празднику
    logger.debug("Премия к празднику")
    prize_holiday(
        data_mounts=data_mounts, file_dog="Премия.docx", number_month=number_month
    )
