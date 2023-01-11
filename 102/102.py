# -*- coding: utf8 -*-

# С помощью анонимной функции извлеките из списка числа, делимые на 15.
# Список необходимо задать рандомно

from random import randint

len = int(input("Введите длину списка: "))
list_random = []
i = 0

while i < len:
    list_random.append(randint(1, 290))
    i += 1
print(list_random)

result = list(filter(lambda x: not x % 15, list_random))
print("В списке делятся на 15", result)
