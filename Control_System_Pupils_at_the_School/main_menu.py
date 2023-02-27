class MenuMain:

    def main_menu_choise():
        number = int(input("Рады приветствовать в системе управления контроля учеников,\n"
                                  "Пожалуйста выберите то, что хотите сделать:\n"
                                  "1. Добавить ученика\n"
                                  "2. Удалить ученика\n"
                                  "3. Найти ученика в базе\n"
                                  "4. Добавить(редактировать) информацию об ученике\n"
                                  "5. Посмотреть сводную таблицу по всем ученикам\n"
                                  "6. Выйти из программы\n"))
        match number:
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return 4
            case 5:
                return 5
            case 6:
                return 6
            case _:
                return 7
    
