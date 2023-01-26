# Скорость выполнения алгоритма, сортировка выбором, пузырьковая
# сортировка, встроенный метод сортировки.

from random import randint
import time

list = []
size = int(input("Введите длину списка: "))

for i in range(size):
    if i < size:
        list.append(randint(1, 99))
print("Первоначальный рандомный список:", list)

start_time_1 = time.perf_counter()

def sorting_list(list):
    for j in range(0, len(list) - 1):
        min = j
        for k in range(j + 1, len(list)):
            if list[k] < list[min]:
                min = k
        list[j], list[min] = list[min], list[j]

end_time_1 = time.perf_counter()

start_time_2 = time.perf_counter()
def sorting_list_bubble(list):
    for h in range(len(list)):
        for d in range(len(list) - 1):
            if list[d] > list[d + 1]:
                list[d], list[d + 1] = list[d + 1], list[d]

end_time_2 = time.perf_counter()

start_time_3 = time.perf_counter()
def sorting_reverse(list):
    reversed(list)
 
end_time_3 = time.perf_counter()               
sorting_list(list)
print("Метод сортировки выбором:", list)
sorting_list_bubble(list)
print("Метод пузырьковой сортировки:", list)
sorting_reverse(list)
print("Встроенный метод сортировки:", list)
print("Время выполнения сортировки выбором: ", end_time_1 - start_time_1)
print("Время выполнения пузырьковой сортировки: ", end_time_2 - start_time_2)
print("Время выполнения сортировки встроенным методом: ", end_time_3 - start_time_3)
