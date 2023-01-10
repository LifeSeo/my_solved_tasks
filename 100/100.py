# Напишите программу, которая принимает два списка и
# выводит все элементы первого, которых нет во втором.
# Списки задает пользователь с клавиатуры

first_list = []
second_list = []

len_first = int(input("Введите длину первого списка: "))
len_second = int(input("Введите длину второго списка: "))

for i in range(len_first):
    first_list.append(input(f"Введите элемент # {i}: "))
print(f"Первый список: {first_list}", sep = ",")

for j in range(len_second):
    second_list.append(input(f"Введите элемент # {j}: "))
print(f"Второй список: {second_list}", sep = ",")

print(set(first_list) - set(second_list))
