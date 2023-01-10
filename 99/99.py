# Написать таблицу умножения на Python, данные вводит пользователь

# -*- coding: utf8 -*-

# number = int(input("Введите число, которое будем умножать: "))
# first_digit = int(input("Введите первое число диапозона: "))
# second_digit = int(input("Введите второе число диапозона: "))


# for i in range(first_digit, second_digit):
#     print(number, "x", i, "=", number*i)
    
    
# Вывести на экран таблицу умножения по столбцам

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}\t", end = "")