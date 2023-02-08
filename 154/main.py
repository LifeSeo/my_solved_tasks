# Задача №31. Последовательностью Фибоначчи называется
# последовательность чисел
# a0, a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

from functools import lru_cache
from time import perf_counter

n = int(input("Введите количество чисел в ряду: "))

start_time_1 = perf_counter()
for i in range(n):
    def fib(n): return 1 if n < 2 else fib(n-1) + fib(n-2)
print(fib(i))
end_time_1 = perf_counter()
print(end_time_1 - start_time_1)

start_time_2 = perf_counter()
@lru_cache
def Fibonachi(n):
    if n in (1, 2):
        return 1
    return Fibonachi(n - 1) + Fibonachi(n - 2)

end_time_2 = perf_counter()
print(end_time_2 - start_time_2)

print(Fibonachi(n))
