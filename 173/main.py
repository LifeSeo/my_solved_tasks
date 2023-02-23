import pandas as pa
print("\n")
file = pa.read_csv(r'173\california_housing_train.csv')
print("---------------Выводим с 0 по 9 индексы таблицы (10 значений)-----------------\n")
print(file.head(10))

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
print("\n")
print("---------------Средняя стоиомсть дома с населением до 500------------------\n")
middle_price = file[file["population"] <= 500].median()
print(middle_price.medianHouseValue) 
# сделал через переменную, интересно было посмотреть, как это работает

# Задача 42: Узнать какая максимальная households в зоне минимального значения population
print("\n")
print("---------------Максимальная households в зоне минимального значения population------------------\n")
print((file["households"].max()) & (file["population"].min()))
print("\n")