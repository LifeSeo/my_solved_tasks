# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint as rd

list = []

while True:
    try:
        n = int(input("Введите количество элементов списка: "))
        a = int(input("Какое число проверить на повторы: "))
        break
    except ValueError:
        print("Введите целое число, а не букву!")


def RandomList(list, n):
    for i in range(n):
        if i < n:
            list.append(rd(1, 9))
    return list


def FindElements(list, a):
    count = 0
    for i in list:
        if i == a:
            count += 1
    return count


print("Печатаем список:", *RandomList(list, n))
print("Количество повторяющихся элементов:", FindElements(list, a))
