from main_menu import MenuMain
from csv import writer

def add_pupil(main_menu_choise):
    if main_menu_choise == 1:
        list_data = []
        list_data.append(input("Введите Фамилию: "))
        list_data.append(input("Введите Имя: "))
        list_data.append(input("Введите класс ученика: "))
        list_data.append(input("Успеваемость ученика: "))
        list_data.append(input("Введите адрес ученика: "))
        list_data.append(input("Номер телефона ученика: "))
        list_data.append(input("Дополнительная информация: "))
        with open(r"Control_System_Pupils_at_the_School\table_pupils.csv", \
            "a", newline='', encoding="utf-8") as file:
            writer_list = writer(file)
            writer_list.writerow(list_data)
            return writer_list