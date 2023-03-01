from main_menu import MenuMain
from add_pupils import add_pupil
from find_pupil import pupil_find
from del_pupil import pupil_del
from modarate_pupil import pupil_moderate
from table_pupils import pupils_table



def click_button():
    click = MenuMain.main_menu_choise()
    if click == 1:
        add_pupil(click)
    if click == 2:
        pupil_del(click)
    if click == 3:
        pupil_find(click)
    if click == 4:
        pupil_moderate(click)
    if click == 5:
        pupils_table(click)
    if click == 7:
        print("Такого пункта нет в меню")