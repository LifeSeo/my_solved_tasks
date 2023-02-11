# Игра крестики-нолики

from random import randint as rnd
# Наше игровое поле
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Выигрышные комбинации
victorias = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

# Выводим на печать игровое поле


def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

# Делаем ход и ставим значок крестика или нолика в нужную ячейку


def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# Делает автозаполнение роботом


def ai(maps):
    num = rnd(1, 9)
    count = 0
    while True:
        if num in maps and count < 998:
            return num
        elif count < 988:
            count += 1
            return ai(maps)
        else:
            for i in maps:
                if i != num:
                    print("Ничья")


# Проверяем текущий результат игры
def get_result():
    win = ""

    for i in victorias:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "Пользователь"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "Компьютер"

    return win


game_over = False
player1 = True
first_name = input("Введите свое имя: ")

while game_over == False:

    print_maps()

    if player1 == True:
        symbol = "X"
        step = int(input(f"{first_name}, делайте ход: "))
        print("---------")
    else:
        symbol = "O"
        step = ai(maps)
        print("---------")

    step_maps(step, symbol)
    win = get_result()

    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

print_maps()
print("Выиграл:", win)
