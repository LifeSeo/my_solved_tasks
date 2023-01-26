# Работа с классами и БД, составляемм офисную структуру

from Department import Department
from Worker import Worker
from DataBase import DataBase

dep1: Department = Department(0, "Информационные технологии")
dep2: Department = Department(1, "Отдел кадров")
dep3: Department = Department(2, "Бухгалтерия")

# print(dep1)
# print(dep2)
# print(dep3)

worker1: Worker = Worker("Мария Ивановна", 23)
worker2: Worker = Worker("Мария Степановна", 26)
worker3: Worker = Worker("Василий Петрович", 33)
worker4: Worker = Worker("Игнат Петрович", 23)

db: DataBase = DataBase()
db.append_worker(worker1)
db.append_worker(worker2)
db.append_worker(worker3)
db.append_worker(worker4)

db.append_dep(dep1)
db.append_dep(dep2)
db.append_dep(dep3)

print(db.select_all_dep())
print('=====')
print(db.select_all_worker())
