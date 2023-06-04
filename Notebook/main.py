def input_date():
    answer = ""
    print("Что необходимо сделать:")
    answer = input("Добавить новые данные (1) : Найти данные (2) \n"
          "Изменить данные (3) : Удалить данные (4)\n"
          "Ввести: ")
    if answer == "1":
        note = open("Notebook/notebook.txt", "a+", encoding="utf 8")
        note.write(input("Введите Фамилию: \n"))
        note.write(" ")
        note.write(input("Введите Имя: \n"))
        note.write(" ")
        note.write(input("Введите Имя: \n"))
        note.write(" ")
        note.write(input("Введите номер телефона: \n"))
        note.write(" ")
        note.write(input("Введите адрес: \n"))
        note.write(" ")
        note.write(input("Примечание: \n"))
        note.write(" ")
    elif answer == "2":
        find_note = input("Введите данные, которые требуется найти: ").upper()
        note = open("Notebook/notebook.txt", "r", encoding="utf 8")
        for i in note:
            if find_note in i.upper():
                print(i)
            else:
                print("Данные не найдены")
    