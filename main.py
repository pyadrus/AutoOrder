from supplement_for_achievements_in_work import supplement_for_achievements_in_work
from supplement_for_work_wartime import supplement_for_work_wartime
from supplement_minimum_wage import supplement_minimum_wage

# Месяц
data_mounts = "январь"

# Заполнение приказов
supplement_for_achievements_in_work(data_mounts)  # Доплата за высокие достижения в работе
supplement_minimum_wage(data_mounts)  # Доплата до МРОТ
supplement_for_work_wartime(data_mounts)  # Доплата за работу в военное время
