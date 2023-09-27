print('Задача 1. Датчик погоды')

# В за окном квартиры стоит датчик погоды, который определяет, идёт ли дождь.
# Если идёт, датчик оповещает сообщением: «Пошёл дождь. Возьмите зонтик!»
# Напишите программу, которая получает на вход число 0 или 1. Единица означает,
# что дождь идёт. В таком случае выводите на экран сообщение: «Пошёл дождь.
# Возьмите зонтик!». Ноль означает, что дождя нет, в этом случае надо вывести
# сообщение «Дождя нет!»

# Пример 1:
# На улице идёт дождь? 1
# Пошёл дождь. Возьмите зонтик!

# Пример 2:
# На улице идёт дождь? 0
# Дождя нет!

rain_or_no = int(input("Введите показания датчика 0 или 1: "))

while rain_or_no < 0 or rain_or_no > 1:
    rain_or_no = int(input("Не верно. Введите показания датчика 0 или 1: "))
 
def check_rain(rain_or_no):   
    if rain_or_no == 1:
        return print("Пошёл дождь. Возьмите зонтик!")
    return print("Дождя нет!")

check_rain(rain_or_no)

print('Задача 2. Поступление')

# Вася работает разработчиком, и его компания создаёт сайт для образовательной компании.
# Заказчики попросили реализовать калькулятор баллов ЕГЭ в помощь поступающим.
# Эту задачу отдали Васе.

# Напишите программу, которая запрашивает у пользователя результаты ЕГЭ по трём
# экзаменам, и проверяет, поступил ли он на бюджет. Проходной балл равняется 270.
# Выведите соответствующее сообщение.

# Пример 1:
# Введите количество баллов по русскому языку: 90
# Введите количество баллов по математике: 90
# Введите количество баллов по информатике: 90

# Поздравляю, ты поступил на бюджет!

# Пример 2:
# Введите количество баллов по русскому языку: 100
# Введите количество баллов по математике: 50
# Введите количество баллов по информатике: 70

# К сожалению, ты не прошёл на бюджет.

rus_marks = int(input("Введите набранные балы по русскому языку: "))
mathematics_marks = int(input("Введите набранные балы по математике: "))
informatics_marks = int(input("Введите набранные балы по информатике: "))

your_score = rus_marks + mathematics_marks + informatics_marks
good_score = 270

def check_amount_marks(your_score, good_score):
    if your_score >= 270:
        print("Поздравляю, ты поступил на бюджет!")
    else:
        print("К сожалению, ты не прошёл на бюджет.")
 
check_amount_marks(your_score, good_score)   

print('Задача 3. Следим за расписанием')

# После выполненной задачи Вася устал и понял, что весь следующий день ему
# придётся восстанавливать силы. Вася решил, что работать он будет только в
# чётные дни и написал небольшую программу, которая поможет ему не пропустить
# рабочий день.

# Напишите программу, которая проверяет, чётное ли число ввёл пользователь,
# и выводит соответствующее сообщение. 

# Подсказка: для проверки чётности используйте оператор %.

number_for_check = int(input("Введите число: "))

def check_number(number_for_check):
    if number_for_check % 2 ==  0:
        return print("Число четное")
    return print("Число нечетное")

check_number(number_for_check)

print('Задача 4. Калькулятор скидки')

# Васин друг переехал в новую квартиру, и ему нужно купить три стула
# в разные комнаты. Цены на стулья  разные, а в некоторых магазинах есть скидки.
# Друг хочет заказать у Васи калькулятор скидки, чтобы проще ориентироваться в ценах.

# Напишите программу, которая запрашивает три стоимости товара и вычисляет сумму чека.
# Если сумма чека превышает 10 000 руб., нужно вычесть из этой суммы
# скидку 10% (умножить на 10, разделить на 100). Итоговая сумма должна выводиться
# на экран.

chair_1 = int(input("Введите стоимость первого стула: "))
chair_2 = int(input("Введите стоимость второго стула: "))
chair_3 = int(input("Введите стоимость третьего стула: "))

chair_amount = chair_1 + chair_2 + chair_3

def amout_discount(chair_amount):
    discount = 0
    amount_for_pay = chair_amount
    if chair_amount > 10000:
        discount = chair_amount * 10 / 100
        amount_for_pay = chair_amount - discount
    return amount_for_pay, discount

result = amout_discount(chair_amount)
print("Сумма к оплате:" ,*result, "скидка")

print('Задача 5. Модуль числа')

# Создайте программу, которая найдёт модуль очередного числа x.
# Если число x отрицательное, то она должна перевести его в положительное,
# а в конце на экране должен быть модуль введённого числа.

# Пример:
# Ввели 5, ответ 5
# Ввели −7, ответ 7

# Подсказка: в некоторых случаях достаточно переприсвоить переменную со знаком минус.

number = int(input("Введите число: "))

if number > 0:
    print(f"Ввели: {number}, Ответ: {number}")
else:
    print(f"Ввели: {number}, Ответ: {number * -1}")
    
print('Задача 6. Игра в кубики')

# Вася понимает, как важен отдых после тяжёлого рабочего дня, поэтому часто
# ходит в местный бар с друзьями. Владелец бара любит азартные игры и иногда
# предлагает посетителям с ним сыграть. Вася избегает азартные игры,
# но предложил владельцу купить у него программу для расчёта результатов игры,
# которую можно выводить на экраны бара.

# Напишите программу: на вход в неё подаётся два числа. Если первое число
# больше или равно второму, то нужно вывести на экран их разность и отдельной
# строкой: «Игрок платит». В противном случае, вывести их сумму и отдельной
# строкой: «Владелец платит». Последней строкой на экран должна быть выведена
# фраза: «Игра окончена».

# Пример:
# Кубик Кости: 3
# Кубик владельца: 4
# Сумма: 7
# Владелец платит
# Игра окончена

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

def check_digits(first_number, second_number):
    if first_number >= second_number:
        return print(f"Разность чисел: {first_number - second_number}\n"
                     "Игрок платит")
    else:
        return print(f"Сумма чисел чисел: {first_number + second_number}\n"
                     "Хозяин платит")
        
check_digits(first_number, second_number)
print("Игра окончена")

print('Задача 7. Хватит ли зарплаты')

# Вася набрался опыта и решил поискать вакансию с большей зарплатой.
# Его привлекла вакансия со странной формулой для расчёта заработной платы:
# 200 * hours / 2 ** 3 + hours

# Он хочет понять, сколько часов нужно отработать, чтобы хватило на
# погашение кредита и еду.

# Напишите программу, которая запрашивает у пользователя три числа:
# количество отработанных часов, остаток по кредиту и количество денег на еду.
# После этого рассчитывается зарплата по формуле. Если зарплата больше или равна сумме,
# которая требуется на кредит и еду, то выводится сообщение: «Часов хватает.
# Можно отдохнуть». В противном случае: «Часов не хватает.
# Придётся работать больше!»

# Пример:
# Введите отработанные часы: 80
# Введите остаток по кредиту: 1000
# Введите траты на еду: 5000
# Часов не хватает. Придётся работать больше!

hours_for_work = int(input("Введите отработанные часы: "))
loan_balance = int(input("Введите остаток по кредиту: "))
money_for_eat = int(input("Введите траты на еду: "))

def check_hours(hours_for_work, loan_balance, money_for_eat):
    check_need_or_no = 200 * hours_for_work / 2 ** 3 + hours_for_work
    if check_need_or_no >= (loan_balance + money_for_eat):
        return print("Часов хватает. Можно отдохнуть")
    else:
        return print("Часов не хватает. Придётся работать больше!")
    
check_hours(hours_for_work, loan_balance, money_for_eat)
                     
print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))

def max_number (num_1, num_2, num_3):
    max = num_1
    if num_1 > max:
        max = num_1
    if num_2 > max:
        max = num_2
    if num_3 > max:
        max = num_3
    return max

max_digit = max_number (num_1, num_2, num_3)
print("Максимальное число:", max_digit)
