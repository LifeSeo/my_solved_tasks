# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

a = int(input("Введите количество элементов списка: "))

b = [int(input()) for i in range(a)]

def pars_elements(b):
    count = 0
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            if b[i] == b[j]:
                count += 1
    print(count)


print(b)
pars_elements(b)
