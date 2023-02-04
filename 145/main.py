# Сгенерировать список нечетных чисел от 70 до 100

from random import randint as rnd 

list1 = [i for i in range(70, 101) if i % 2 != 0]
print(*list1)