# -*- coding: utf8 -*-

# Написать программу деления чисел с обработчиком ошибок.
# Числа вводит пользователь.

first_digit = int(input("Введите первое число: "))
second_digit = int(input("Введите второе число: "))
result = 0

while second_digit == 0:
    try:
        second_digit = int(input("На ноль делить нельзя. Введите второе число: "))
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        
result = first_digit / second_digit
print(f"Результат деления: ", {result})
        