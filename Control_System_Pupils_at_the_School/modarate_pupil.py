from main_menu import MenuMain

def pupil_moderate(main_menu_choise):
    if main_menu_choise == 4:
        data = input("Данные, которые необходимо отредактировать: ").lower()
        data_change = input("На что хотите заменить: ")
        with open(r"Control_System_Pupils_at_the_School\table_pupils.csv", "r+") as file:
            fl = file.readlines()
            file.seek(0)
            for i in fl:
                if data in i.lower():
                    i = i.lower().replace(data, data_change)
                    file.write(i)
                else:
                    file.write(i)
                
                    
