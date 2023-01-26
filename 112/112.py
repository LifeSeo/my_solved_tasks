# Метод быстрой сортировки по Хоара.

from random import randint
import time

list = []
size = int(input("Введите размер списка: "))

def random_list():
    for i in range(size):
        if i < size:
            list.append(randint(1, 99))
    return list

start_time = time.perf_counter()

def quick_sort(list):
    
    less = []
    equal = []
    greater = []
    
    if len(list) > 1:
        pivot = list[0]
        for j in list:
            if j < pivot:
                less.append(j)
            elif j == pivot:
                equal.append(j)
            elif j > pivot:
                greater.append(j)
            
        return quick_sort(less) + equal + quick_sort(greater)

    else:
        return list
            
end_time = time.perf_counter()
    
random_list()
print(list)
n = quick_sort(list)
print(n)
print(end_time - start_time)
    
            
