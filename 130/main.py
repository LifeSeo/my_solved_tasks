# Написать простой калькулятор

sign = input("Введите знак операции (+ - * /): " )
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

while True:
    if sign == "/" and y == 0:
        print("Деление на ноль невозможно")
        break
    elif sign == "/":
        print(f"Результат деления {x} на {y} = {x/y}")
        break
    elif sign == "*":
        print(f"Результат умножения {x} на {y} = {x*y}")
        break
    elif sign == "-":
        print(f"Результат вычитания {x} и {y} = {x-y}")
        break
    elif sign == "+":
        print(f"Результат сложения {x} и {y} = {x+y}")
        break