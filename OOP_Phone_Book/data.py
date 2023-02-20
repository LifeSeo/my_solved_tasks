def print_data(data):
    print(data)


def input_data():
    answer = ""
    data = input("Записать данные (нажмите 1) | Найти данные (нажмите 2)\n"
                 "Изменить данные (нажмите 3) | Удалить данные (нажмите 4): ")
    if data == "1":
        answer = "1"
    elif data == "2":
        answer = "2"
    elif data == "3":
        answer = "3"
    elif data == "4":
        answer = "4"
    else:
        print("Вы не верно ввели номер нужного действия!")
    return answer
