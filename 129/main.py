# Простые задачи на словари:

# 1. Создать произвольный словарь
# 2. Добавить новый элемент с ключом типа str и значением типа int 
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# 4. Получить элемент по ключу
# 5. Удалить элемент по ключу
# 6. Получить список ключей словаря

dictionary = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(dictionary)

dictionary["New"] = 123456
print(dictionary)

dictionary[('it', 'is', 'tuple')] = [11, 22, 'list_value', 33, {1, 2, 3}]
print(dictionary)

print(dictionary["Age"])

dictionary.pop("Name")
print(dictionary)

print(dictionary.keys())
