# Сформировать последовательность чисел на основании
# предоставленного списка по правилу: если число меньше 5, то удвоить его,
# а если больше или равно, то отнять от него 2.
# Список: [2, 77, 12, 3, 0, 112, 4, -987].

list_1 = [2, 77, 12, 3, 0, 112, 4, -987]

list_1 = [i for i in list_1 if i < 5 i == i*2 if i >= 5 i == i-2]
