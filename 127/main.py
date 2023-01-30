# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые больше 5 по модулю.

from random import randint

n = int(input("Задайте длинну списка: "))
list = []
def Random_List(n, list):
    for elements in range(n):
        if elements < n:
            list.append(randint(1, 99))
    return list

    
def more_than_five(list):
    list_finall = []
    for elements in list:
        if elements > 5:
            list_finall.append(elements)
    print(list_finall)
    
    
Random_List(n, list)
more_than_five(list)