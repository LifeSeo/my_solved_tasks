# -*- coding: utf8 -*-
# from random import randint

# a = []
# def random_list():
#     for i in range(10):
#         a.append(randint(1, 99))
#     return a

# def print_list(a):
#     for i in a:
#         if i < len(a):
#             print(a)

# random_list()
# res = sorted(a)
# print(res)
# res.reverse()
# print(res)
# print(a)

# Задать рандомный список. Содать программу, которая будет определять, сумма
# каких 3-х элементов подряд из списка со смещением вправа на один, больше.

from random import randint

a = []

for i in range(10):
    a.append(randint(1, 9))
print(a)
max = sum(a[0:3])
for i in a:

    if max < sum(a[0 + i+1:3 + i+1]):
        max = sum(a[0 + i+1:3 + i+1])
print(max)
