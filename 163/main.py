# Задача №41. Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

a = int(input("Введите количество элементов списка: "))
lst = []
lst_fin = []


def append_lst(lst, a):
    for i in range(a):
        lst.append(int(input(f"Введитете {i+1} элемент списка: ")))
    return lst


def compare_elements(lst, a):
    count = 0
    for i in range(1, a - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            count += 1
    return count


print(append_lst(lst, a))
print(compare_elements(lst, a))
