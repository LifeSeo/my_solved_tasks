from random import randint as rnd

# Создать рандомный список

lst1 = list(map(lambda x:rnd(1,13), range(10)))
print(f'Выводим рандомный список 1: {lst1}')

lst2 = list(map(lambda x:rnd(1,13), range(10)))
print(f'Выводим рандомный список 2: {lst2}')

# Вернуть пересечение списков.

lst_set = set(lst1+lst2)
print(lst_set)

# Проверить симметрична ли запись числа.

a = int(input("Введите число: "))
x = reversed(list(map(int, str(a))))
res = int(''.join(map(str, x)))
print(res)

def semetric(a, res):
    if a == res:
        print("Число симетрично")
    else:
        print("Число не симетрично")
        
# Дан список строк, избавиться от пустых строк в нем
# разными способами (цикл, list comprehension, filter).

lst3 = ["", "test", "", "is", "best", ""]
lst3 = [i for i in lst3 if i]
print(f'Очистка списка с помощью list comprehension {lst3}')
lst3 = list(filter(None, lst3))
print(f'Очистка списка с помощью filter {lst3}')

def remove_empty(lst3):
    for i in lst3:
        if i == "":
            lst3.remove("")
    return lst3

# Реализовать алгоритм, который принимает массив и перемещает
# все нули в конец, сохраняя порядок остальных элементов.

lst4 = list(map(lambda x: rnd(0, 5), range(10)))
print(f'Выводим массив с нулями {lst4}')

def zero_end(lst4):
    count = 0
    lst_ready_1 = []
    lst_ready_2 = []
    for i in lst4:
        if i != 0:
            lst_ready_1.append(i)
        else:
            lst_ready_2.append(i)
    return lst_ready_1 + lst_ready_2
            

    return lst_ready

semetric(a, res)
print(f'Очистка списка с помощью цикла {remove_empty(lst3)}')
print(f'Новый список с нулями в конце {zero_end(lst4)}')