from main_menu import MenuMain
from csv import *
import pandas as pd


def pupil_del(main_menu_choise):
    if main_menu_choise == 2:
        data = input("Введите информацию для поиска и удаления: ").lower()
        with open(r"Control_System_Pupils_at_the_School\table_pupils.csv", "r+") as file:
            fl = file.readlines()
            file.seek(0)
            for i in fl:
                if data not in i.lower():
                    file.write(i)
            print("Больше нет данных для удаления")
            file.truncate()
