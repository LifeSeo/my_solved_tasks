# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

from random import randint as rd

list = []
list_1 = []
while True:
    try:
        n = int(input("Введите количество элементов списка: "))
        a = int(input("К какому числу ищем самый близкий по величине элемент: "))
        break
    except ValueError:
        print("Введите целое число, а не букву!")


def RandomList(list, n):
    for i in range(n):
        if i < n:
            list.append(rd(1, 99))
    return list


def CloseElement(list, list_1, a):
    close_element = list[0]
    for i in list:
        if i < a:
            list_1.append(i)
            close_element = max(list_1)
    return close_element

print("Выводим список:", RandomList(list, n))
print("Выводим отсортированный лист:", sorted(list))
print("Минимально близкий элемент:",
      CloseElement(list, list_1, a))
