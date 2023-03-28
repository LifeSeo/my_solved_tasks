from random import randint as rnd

digit = list(map(lambda x: rnd(99, 900), range(10)))
print(f"Первоначальный массив(список): {digit}")


def Sorting(digit):
    for j in range(len(digit)):
        for i in range(len(digit)-1):
            if digit[i] > digit[i+1]:
                digit[i], digit[i+1] = digit[i+1], digit[i]

# У вас есть массив чисел.
# Напишите три функции, которые вычисляют сумму этих чисел:
# с for-циклом, с while-циклом, с рекурсией.


def Mass_for(digit):
    sum = 0
    for i in digit:
        sum += i
    return sum


i = 0
sum = 0
while i < len(digit):
    sum += digit[i]
    i += 1
print(sum)


def Mass_Recursia(digit, i=0):
    if i >= len(digit):
        return 0
    else:
        return digit[i] + Mass_Recursia(digit, i + 1)

# Вычислить факториал числа n с помощью рекурсии


def Factorial(n=9):
    return 1 if n < 1 else Factorial(n-1)*n

# Напишите функцию, которая создаёт комбинацию двух списков таким образом:
# [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]


lst1 = [1, 2, 3]
lst2 = [11, 22, 33]


def ComboList(lst1, lst2):
    lst3 = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        lst3.append(lst1[i])
        lst3.append(lst2[j])
        i += 1
        j += 1
    return lst3

 # Вычислите первые 100 чисел Фибоначчи.


def Fibonachi(n=25):
    return 1 if n in (1, 2) else Fibonachi(n-1) + Fibonachi(n-2)

# У вас есть массив чисел, составьте из них максимальное число. Например:
# [61, 228, 9] -> 961228


lst = [61, 228, 9]


def DigitMax1(lst):
    lst = ''.join(map(str, lst))
    lst2 = []
    for i in lst:
        lst2.append(i)
    print(f"Вариант 1: {''.join(map(str, sorted(lst2, reverse=True)))}")



Sorting(digit)
print(f"Отсортированный список: {digit}")
print(f"Результат сложения: {Mass_for(digit)}")
print(f"Результат сложения через рекурсию: {Mass_Recursia(digit)}")
print(f"Факториал числа = {Factorial()}")
print(f"Комбинированные списки: {ComboList(lst1,lst2)}")
print(f"Число Фибоначи: {Fibonachi()}")
DigitMax1(lst)
