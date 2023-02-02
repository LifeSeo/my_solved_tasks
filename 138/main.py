# Задача №17. Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint as rd

list = []
count = 0

while True:
    try:
        n = int(input("Введите количество элементов списка: "))
        break
    except ValueError:
        print("Введите целое число, а не букву!")


def RandomList(list):
    for i in range(n):
        if i < n:
            list.append(rd(1, 10))
    return list


print(RandomList(list))
print(set(list))
print(len(set(list)))
