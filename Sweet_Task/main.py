# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?


# Альтернативный вариант решения

from random import randint as rnd

sweets = 2021
lst_sweets_first_player = []
first_player = rnd(1, 28)
second_player = rnd(1, 28)
count_first_player = 0
count_second_player = 0

while sweets > 0:

    if sweets > 0:
        sweets = sweets - first_player
        lst_sweets_first_player.append(first_player)
        count_first_player += 1
    if sweets > 0:
        sweets = sweets - second_player
        count_second_player += 1
    if count_first_player > count_second_player:
        print("Выиграл первый игрок, он взял последним")


print("Игрок 1 начал игру с ввода:", lst_sweets_first_player[0])

print(f"Первый игрок взял (раз): {count_first_player}",
      f"Второй игрок взял (раз):, {count_second_player}")
