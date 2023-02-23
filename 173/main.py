import pandas as pa

file = pa.read_csv(r'173\california_housing_train.csv')

print(file.head(10))

print("------------------")

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

print(file[file["population"] <= 500].median())

# Задача 42: Узнать какая максимальная households в зоне минимального значения population
print("------------------")
print((file["households"].max()) & (file["population"].min()))