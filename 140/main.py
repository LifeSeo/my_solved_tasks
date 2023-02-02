# Задача №21. Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

from itertools import chain

dictionary = [{"V":"S001"}, {"V": "S002"}, 
     {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Начальный словарь : ",dictionary)
unic_value = set( val for dic in dictionary for val in dic.values())
print("Уникальные значения: ",unic_value)

# result = list(sorted(set(chain(*dictionary.values()))))
# print(result)