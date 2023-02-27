from main_menu import MenuMain
from add_pupils import add_pupil



def click_button():
    click = MenuMain.main_menu_choise()
    if click == 1:
        add_pupil(click)
    if click == 7:
        print("Такого пункта нет в меню")