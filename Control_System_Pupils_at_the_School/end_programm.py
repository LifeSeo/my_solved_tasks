from control import click_button

def programm_end():
    data_end = int(input("Желаете продолжить работать с программой? \
        Да: 1, Нет: 2\n"))
    if data_end == 1:
        click_button()
    else:
        quit()