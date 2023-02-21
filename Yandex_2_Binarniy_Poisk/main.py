# Требуется найти в бинарном векторе самую длинную последовательность единиц
# и вывести её длину.

# Желательно получить решение, работающее за линейное время и при этом
# проходящее по входному массиву
# только один раз.

from random import randint as rnd
from memory_profiler import memory_usage as mu

binan_vector = list(map(lambda _: rnd(0, 1), range(10)))


count = 0
max = 0
for i in binan_vector:
    print(i, end="---")
    if i == 1:
        count += 1

    else:
        if count > max:
            max = count
        count = 0
print("Единица повторяется: ", max if max > count else count)

print(mu())
