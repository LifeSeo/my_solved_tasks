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
    elif answer == "3":
         find_data = input("Какие данные необходимо изменить: ").upper()
         dict = open("Notebook/notebook.txt", "r", encoding="utf-8")
         for i in dict:
            if find_data in i.upper():
                change_data = input("На что будем менять: ").upper()
                dict = open("Notebook/notebook.txt", "r", encoding="utf-8")
                new_dict_data = dict.read().replace(find_data, change_data)
                dict = open("Notebook/notebook.txt", "w", encoding="utf-8")
                dict.write(new_dict_data)

            else:
                print("Данные не найдены")
    elif answer == "4":
        del_date = input("Что требуется удалить: ").upper()
        dict = open("Notebook/notebook.txt", "r", encoding="utf-8")
        for i in dict:
            if del_date in i.upper():
                del_date_str = input("Удалить всю строку:1, Удалить только слово:2: ")
                if del_date_str == "1":
                    dict = open("Notebook/notebook.txt", "r", encoding="utf-8")
                    new_dict_data = dict.read().replace(i, "")
                    dict = open("Notebook/notebook.txt", "w", encoding="utf-8")
                    dict.write(new_dict_data)
                    return new_dict_data
                else:
                    dict = open("Notebook/notebook.txt", "r", encoding="utf-8")
                    new_dict_data = dict.read().replace(del_date, "")
                    dict = open("Notebook/notebook.txt", "w", encoding="utf-8")
                    dict.write(new_dict_data)
                    return new_dict_data
        dict.close()
    
    