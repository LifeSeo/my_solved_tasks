# Найти три самых больших числа из словаря

dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 9999}
lst = []

for value in dict.values():
    lst.append(value)
    lst = sorted(lst)
print(lst[-1], lst[-2], lst[-3])
