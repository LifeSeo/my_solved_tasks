# Задача №33. Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint as rnd

n = int(input("Введите количество элемемнтов списка: "))
lst = []


def random_list(n):
    for i in range(n):
        lst.append(rnd(1, 5))
    return lst


def max_element(lst):
    max = 0
    for i in lst:
        if i > max:
            max = i
    return max


def new_list_max_element(lst):
    lst_2 = []
    for i in lst:
        if i == max_element(lst):
            lst_2.append(1)
        else:
            lst_2.append(i)
    return lst_2


random_list(n)
print(f"Изначальный список: {lst}")
print("Максимальный элемент", max_element(lst))
print("Измененные оценки:", new_list_max_element(lst))
