# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе. Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

from random import randint as rd

list_days = []
count = 0
max_count = 0

while True:
    try:
        n = int(input("Введите количество дней: "))
        break
    except ValueError:
        print("Введите целое число, а не букву!")


def List_Days(list_days):
    for i in range(n):
        if i < n:
            list_days.append(rd(-50, 50))
    return list_days

def MoreThenZero(list_days, count, max_count):
    for i in range(len(list_days)):
        if list_days[i] > 0:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    print(max_count)
    
List_Days(list_days)
print(list_days)
MoreThenZero(list_days, count, max_count)
