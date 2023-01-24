# Создать программу поиска рандомного числа, загаданного компьютером.
# Ответы должны вбиваться автоматически из рандомного списка нужного диапазона

from random import randint

pc_number = int(randint(1, 99))
your_number = int(randint(1, 99))
print("Компьютер загадал число:", pc_number)
print("Компьютер ввел первое число:", your_number)
count = 1

while pc_number != your_number:
    count+=1
    if pc_number > your_number:
        your_number = randint(your_number,99)
    elif pc_number < your_number:
        your_number = randint(1, your_number)
    else:
        print("Вы угадали!")
print("Компьютер загадал число:", your_number, "и угадал за #", count, "раз(а)")
        
    