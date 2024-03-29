from collections import Counter

# 1. Создать произвольный список
list = [1, 2, 3, "Hello", 22.89]
print("Произвольный список:", list)
# 2. Добавить новый элемент типа str в конец списка
list = [1, 2, 3, "Hello", 22.89]
list.append("Новый элемент")
print("Элемент в конец списка", list)
# 3. Добавить новый элемент типа int на место с индексом
list = [1, 2, 3, "Hello", 22.89]
list[3] = 99
print("Добавили новый элемент на место индекса [3]: ", list)
# 4. Добавить новый элемент типа list в конец списка
list = [1, 2, 3, "Hello", 22.89]
list_2 = [9, 22, 55, 33]
list.append(list_2)
print("Добавили вложенный список:", list)
# 5. Добавить новый элементы типа tuple на место с индексом
list = [1, 2, 3, "Hello", 22.89]
list[3] = (555, 999)
print("Добавили элемент типа tuple:", list)
# 6. Получить элемент по индексу
list = [1, 2, 3, "Hello", 22.89]
print("Получаем элемент по индексу:", list[3])
# 7. Удалить элемент
list = [1, 2, 3, "Hello", 22.89]
list.remove(3)
print("Удаляем элемент по значению:", list)
# 8. Найти число повторений элемента спискам
list = [1, 1, 5, 3, 2, 3, "Hello", 22.89]
duble = Counter(list)
print("Количество повторений элементов:", duble)