# Сортировка выбором на Python

from random import randint

size = int(input("Введите длину списка: "))
list = []
i = 0

while i < size:
    list.append(randint(1, 29))
    i += 1
print("Выводим рандомный список:", list)


def sorting_list(list_sort):
    for j in range(0, len(list) - 1):
        min = j
        for k in range(j + 1, len(list)):
            if list[k] < list[min]:
                min = k
        list[j], list[min] = list[min], list[j]


sorting_list(list)
print(list)
