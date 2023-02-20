from data import input_data
import data

def put_file(input_data):
    if input_data == "1":
        dict = open("OOP_Phone_Book\phone_dictionary.txt", "a+")
        dict.write(input("Введите ФИО и телефон через пробел:\n").upper())
        dict.write("\n")
        return dict
    
    elif input_data == "2":
        find_word = input("Введите данные, которые требуется найти: ").upper()
        dict = open("OOP_Phone_Book\phone_dictionary.txt", "r")
        for i in dict:
            if find_word in i.upper():
                return i
    elif input_data == "3":
        find_data = input("Какие данные необходимо изменить: ").upper()
        dict = open("OOP_Phone_Book\phone_dictionary.txt", "r")
        for i in dict:
            if find_data in i.upper():
                change_data = input("На что будем менять: ").upper()
                dict = open("OOP_Phone_Book\phone_dictionary.txt", "r")
                new_dict_data = dict.read().replace(find_data, change_data)
                dict = open("OOP_Phone_Book\phone_dictionary.txt", "w")
                dict.write(new_dict_data)
                return new_dict_data
    elif input_data == "4":
        del_date = input("Что требуется удалить: ").upper()
        dict = open("OOP_Phone_Book\phone_dictionary.txt", "r")
        for i in dict:
            if del_date in i.upper():
                del_date_str = input("Удалить всю строку:1, Удалить только слово:2: ")
                if del_date_str == "1":
                    dict = open("OOP_Phone_Book\phone_dictionary.txt", "r")
                    new_dict_data = dict.read().replace(i, "")
                    dict = open("OOP_Phone_Book\phone_dictionary.txt", "w")
                    dict.write(new_dict_data)
                    return new_dict_data
                else:
                    dict = open("OOP_Phone_Book\phone_dictionary.txt", "r")
                    new_dict_data = dict.read().replace(del_date, "")
                    dict = open("OOP_Phone_Book\phone_dictionary.txt", "w")
                    dict.write(new_dict_data)
                    return new_dict_data
        dict.close()