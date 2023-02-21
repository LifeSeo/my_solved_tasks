# Дан упорядоченный по неубыванию массив целых 32-разрядных чисел.
# Требуется удалить из него все повторения.
# Желательно получить решение, которое не считывает входной файл
# целиком в память, т.е., использует лишь константный объем памяти в процессе работы.

from time import perf_counter
from memory_profiler import memory_usage as mu
from random import randint as rnd

count_time_start = perf_counter()

rand_list = sorted(list(map(lambda _: rnd(1, 99), range(29))))

def print_list(rand_list):
    lst = []
    for i in rand_list:
        lst.append(i)
    return lst
        
list_none_duplicats = set(rand_list)       
count_time_end = perf_counter()    
print(print_list(rand_list))
print(f"Список без дубликатов: {list_none_duplicats}")
print(f"Памяти использовано: {mu()}")
print(f"Времени использовано: {count_time_end - count_time_start}")
   



