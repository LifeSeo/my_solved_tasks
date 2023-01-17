# Напишите программу, которая принимает рандомный текст и выводит
# самое длинное слово

import random
from random import randint

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
list = []

def random_choice():
    for j in range(randint(3, 12)):
        if j < randint(3, 12):
            list.append(''.join(random.choice(chars)
                        for i in range(randint(1, 9))))
    return list


def long_word(list):
    len_list = []
    for j in list:
        len_list.append(len(j))
    return list[len_list.index(max(len_list))]


random_choice()
print(list)
print("Самое длинное слово: ", long_word(list))
