from prize_holiday import prize_holiday
from supplement_for_achievements_in_work import supplement_for_achievements_in_work
from supplement_for_work_wartime import supplement_for_work_wartime
from supplement_minimum_wage import supplement_minimum_wage

# Месяц
data_mounts = "январь"

# Заполнение приказов

# Доплата за высокие достижения в работе
supplement_for_achievements_in_work(
    data_mounts=data_mounts,
    file_dog="Доплата_за_высокие_достижения_в_труде.docx"
)

# Доплата до МРОТ
supplement_minimum_wage(
    data_mounts=data_mounts,
    file_dog="Доплата_до_МРОТ.docx"
)

# Доплата за работу в военное время
supplement_for_work_wartime(
    data_mounts=data_mounts,
    file_dog="Доплата_за_работу_в_военное_время.docx"
)

# Премия к празднику
prize_holiday(
    data_mounts=data_mounts,
    file_dog="Премия.docx"
)
