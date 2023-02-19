from data import input_data
import data

def put_file(input_data):
    if input_data == "1":
        dict = open("OOP_Phone_Book\phone_dictionary.txt", "a+")
        dict.write("\n")
        dict.write(input("Введите Фамилию Имя Отчество и телефон через пробел: "))
        return dict
    else:
        dict = open("OOP_Phone_Book\phone_dictionary.txt", "r")
        for i in dict:
            if input_data.lower() in i.lower():
                return i