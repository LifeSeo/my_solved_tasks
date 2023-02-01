# Задача №15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint as rd

watermelon = []

while True:
    try:
        n = int(input("Введите количество арбузов: "))
        break
    except ValueError:
        print("Введите целое число, а не букву!")


def WaterMelon_Weight(watermelon):
    for i in range(n):
        if i < n:
            watermelon.append(rd(1, 9))
    return watermelon


def MinAndMaxWaterMelon(watermelon):
    min_value = watermelon[0]
    max_value = watermelon[0]
    for i in watermelon:
        if i >= max_value:
            max_value = i
        elif i <= min_value:
            min_value = i
    return(min_value, max_value)


WaterMelon_Weight(watermelon)
print(watermelon)
print(MinAndMaxWaterMelon(watermelon))
