from main_menu import MenuMain
import csv
import pandas as pd

def pupil_find(main_menu_choise):
    if main_menu_choise == 3:
        data = input("Введите данные для поиска: ").lower()
        with open(r"Control_System_Pupils_at_the_School\table_pupils.csv", "r+") as file:
            fl = file.readlines()
            file.seek(0)
            for i in fl:
                if data in i.lower():
                    i = i.replace(",", " ")
                    print("Найдено:", i)
            print("Поиск окончен")
                