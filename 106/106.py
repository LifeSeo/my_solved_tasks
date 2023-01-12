# Пузырьковая сортировка на Python

from random import randint

list = []
size = int(input("Введите длину списка: "))

for i in range(size):
    list.append(randint(1, 99))
print(list)

def list_sorting(list_sort):
    for i in range(len(list_sort)):
        for j in range(len(list_sort) - 1):
            min = list_sort[j]
            if list_sort[j] > list_sort[j +1]:          
                list_sort[j], list_sort[j +1] = list_sort[j +1], list_sort[j]

                
list_sorting(list)
print(list)