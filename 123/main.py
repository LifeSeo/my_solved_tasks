# Задача 2: Найдите сумму цифр трехзначного числа.

def Integer():
    while True:
        try:
            number = int(input("Введите трехзначное число: "))
        except ValueError:
            print("Вы ввели НЕ число!")

        else:
            if len(str(number)) == 3:
                return print(sum(map(int, str(number))))
            else:
                print("Вы ввели НЕ трехзначное число!")

Integer()

