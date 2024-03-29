print('Задача 1. Космическая еда')

# Ваш космический корабль потерпел крушение на пустынной планете.
# Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки.
# Из прошлого опыта вы знаете, что если будете экономно питаться,
# то у вас будет уходить по четыре килограмма гречки в месяц.

# Чтобы прикинуть гречневый бюджет, вы решили написать программу,
# которая выведет информацию о том, сколько килограммов гречки у вас
# должно быть в запасе через месяц, два и так далее, пока она не закончится.
# Используйте цикл for.

buckwheat = 100
eat_mounth = 4
counter = 1

for i in range(100, 0, -4):
    print(f"На {counter} месяц останется {i} кг гречки")
    counter+= 1
print("На:", counter, "месяц не останется ничего" )

print('Задача 2. Долги')

# «МирПрогБанк» наконец-то разделил законопослушных граждан и должников и
# поместил их в разные базы. Но банк не торопится сильно давить на неплательщиков.
# Операторам банка дали задание позвонить каждому пятому должнику из
# списка (нумерация начинается с нуля) и уточнить, какую сумму каждый
# из них задолжал банку.

# Напишите программу, которая получает данные о количестве должников,
# а затем спрашивает у каждого пятого (начиная с нуля) его долг.
# В конце выводится общая сумма долгов.

# Пример 1
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
# Общая сумма долга: 8000

# Пример 2
# Введите количество должников: 10
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Общая сумма долга: 6000

from random import randint as rnd

dept_people = int(input("Введите количество должников: "))
step = 5
start_dept = 1000
end_dept = 100000
full_dept = 0
# делаю авто заполнение долга, что бы постоянно не вводить руками
for i in range(0, dept_people+1, step):
    dept_for_one = rnd(start_dept, end_dept)
    full_dept+= dept_for_one
    print("Должник с номером", i)  
    print(f"Cколько должен? {dept_for_one}")  
print("Общий долг: ", full_dept)

print('Задача 3. Таймер для микроволновых печей')

# Мы разрабатываем микропрограмму — таймер обратного отсчета для микроволновых печей.
# Некоторым пользователям не нравится пищащий звук.
# Есть задача убрать звук по готовности и заменить его сообщением на LED-экране.
# В нашем случае будем выводить в консоль сообщение с обратным отсчетом в секундах
# от “reverse_timer” до момента готовности, то есть «0» секунд, и спрашивать
# пользователя, готов ли он забрать еду.

# Пользователь в любой момент может прервать режим разогрева,
# введя «1» (то есть ответить «Да, еда готова»), тогда программа
# выводит на экран сообщение «Ваша еда готова, можете забрать» и
# показывает, на какой секунде был прерван таймер.
# Если пользователь отвечает «0», что равноценно «Нет», то таймер
# уменьшается. Когда он достигнет «0» секунд, выводим сообщение
# «Ваша еда готова, осторожно горячo!»

# В данном задании используем цикл for.
# “reverse_timer” – переменная счетчик, значение которой запрашиваем
# у пользователя через функцию ввода input.

# 1) Задайте время до обнуления таймера.
# 2) Используйте цикл for.
# 3) На каждой итерации задавайте персонажу вопрос, хочет ли он сейчас
# остановить разогрев или нет.

reverse_timer = int(input("Введите количество секунд разогрева: "))
counter = reverse_timer

for i in range(reverse_timer, 0, -1):
    check_stop = 0
    check_stop = int(input("Хотите остановить разогрев? 1- да, 0 - нет: "))
    while check_stop != 1 and check_stop != 0:
        check_stop = int(input("Введено неверное значение. Попробуйте еще раз." 
                               "Хотите остановить разогрев? 1- да, 0 - нет: "))
    if check_stop == 1:
        print("Ваша еда готова раньше времени")
        break
    elif check_stop == 0:
        print("Ваша еда еще не готова, осталось", counter)
        counter -= 1
print("Таймер закончил работу.")

print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое всех чисел из
# отрезка [a; b], кратных числу c.

a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
c = int(input("Введите число С: "))

while c == 0:
    c = int(input("Деление на ноль запрещено. Введите число С больше нуля: "))
    
while a == b:
    print("Отрезок не может начинаться и заканчиваться в одной точке: ")
    a = int(input("Введите заного число А: "))
    b = int(input("Введите заного число В: "))
    
def arithmetic_mean(a, b, c):
    summa = 0
    counter = 0
    if a < b:
        for i in range(a, b):
            if i % c == 0:
                summa+= i
                counter += 1
                print("Кратное число(цифра):", i)
    else:
        for i in range(b, a):
            if i % c == 0:
                summa+= i
                counter += 1
                print("Кратное число(цифра):", i)        
    return summa / counter

result = arithmetic_mean(a, b, c)
print(f"Среднее арифметическое: {result}")

print('Задача 5. Функция')

# Перед изучением функций из программирования Саша решил оживить свои знания
# о функциях математики. Помогите Саше написать программу, которая будет
# считать значение функции в каждой точке отрезка с нужным шагом, начиная с конца).
# Напишите программу, которая получает на вход начало и конец отрезка,
# а также шаг (отрицательный), а затем высчитывает функцию y в каждой
# точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.

# Сама функция выглядит так:
# y = x**3 + 2*x**2 - 4*x + 1

# Пример:
# 
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9

start = int(input("Введите начало отрезка: "))
finish = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))

while step == 0:
    step = int(input("Шаг не может быть равен нулю. Введите заного: "))
    
while start == finish:
    print("Начало и конец отрезка не могут быт одинаковыми, введите заного")
    start = int(input("Введите начало отрезка: "))
    finish = int(input("Введите конец отрезка: "))
    
if step < 0: step = -step  

if start < finish:
    for x in range(finish, start, -step):
        y = x**3 + 2*x**2 - 4*x + 1
        print(f"В точне {x} функция равна: {y}")
else:
    for x in range(start, finish, -step):
        y = x**3 + 2*x**2 - 4*x + 1
        print(f"В точне {x} функция равна: {y}")
        
print('Задача 6. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant рублей,
# а расходы на проживание превышают стипендию и составляют expenses рублей в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# Обратите внимание, что каждый месяц цены увеличиваются на 3% относительного
# прошлого месяца. 

# Составьте программу расчёта суммы денег, которую необходимо получить у
# родителей один раз в начале обучения, чтобы можно было прожить учебный
# год (десять месяцев), используя только эти деньги и стипендию.

# Пример:

# Введите стипендию: 10000
# Введите расходы на проживание: 12000

# 1. месяц траты 12000 не хватает 2000
# 2. месяц траты 12360.0 не хватает 4360.0
# 3. месяц траты 12730.8 не хватает 7090.8
# 4. месяц траты 13112.7 не хватает 10203.52
# 5. месяц траты 13506.1 не хватает 13709.63
# 6. месяц траты 13911.2 не хватает 17620.92
# 7. месяц траты 14328.6не хватает 21949.55
# 8. месяц траты 14758.4 не хватает 26708.03
# 9. месяц траты 15201.2 не хватает 31909.27
# 10. месяц траты 15657.2 не хватает 37566.55

# Нужно попросить у родителей 37566.55 рублей

educational_grant = int(input("Введите стипендию студента: "))
expenses = int(input("Введите расходы на проживание: "))
summa = expenses
imbalance = summa - educational_grant

def need_money(educational_grant, summa, imbalance):
    for i in range(1, 11):
        if i == 1:
            print(f"{1}. месяц траты {summa} не хватает {imbalance}")
        else:
            summa += summa * 3 / 100
            imbalance += summa - educational_grant
            print(f"{i}. месяц траты {round(summa, 1)} не хватает {round(imbalance, 2)}")
    return imbalance

student_need_money = need_money(educational_grant, summa, imbalance)
print("Необходимо попросить у родителей:", round(student_need_money, 2))

print('Задача 7. Сумма ряда')

# Дано натуральное число N. Напишите программу для вычисления суммы N
# элементов последовательности по формуле 
# (-1)**n * 1/(2**n), где n — это порядковый номер
# элемента (расчёт начинается с нуля).

# Примеры расчётов

# При N = 4 элементы выражения будут равны:
# n = 0 
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# Сумма равна:
# s=1- 12+14-18 = 5/8 = 0,625

# При N = 6 элементы выражения будут равны:
# n = 0 
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# n = 4
# elem = (−1) ** 4 * (½) ** 4 = (1/16)
# n = 5
# elem = (−1) ** 5 * (½) ** 5 = (−1/32)
# Сумма равна:
# s = 1 − ½ + ¼ − ⅛ + 1/16 − 1/32 = 21/32 = 0,65625

# P. S. Не стоит выполнять расчёты каждого элемента вручную, используйте цикл.

n = int(input("Введите натуральное число N: "))
summa = 0
while n <= 0:
    n = int(input("Вы ошиблись. Введите натуральное число N 1, 2, 3....n: "))
    
for i in range(0, n):
    elem = (-1)**i * 1/(2**i)
    print(i, "элемент равен:", elem)
    summa += elem
print("Сумма всех элементов равно:", summa) 

print('Задача 8. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

x = int(input("Введите количество мальчиков: "))
y = int(input("Введите количество девочек: "))

while x < 0 or y < 0:
    x = int(input("Значение не может быть отрицательным. Введите количество девочек: "))
    y = int(input("Значение не может быть отрицательным. Введите количество мальчиков: "))

boy = "B"
girl = "G"
summa = str()
rest = str()

if (x > 2 * y) or (y > 2 * x):
    print("Решения нет")
elif x == y:
    for i in range(0, x):
        summa = summa + boy + girl
elif x > y:
    rest = x - y
    for j in range(rest):
        summa += "BGB"
    for k in range(y - rest):
        summa += "BG"
elif x < y:
    rest = y - x
    for m in range(rest):
        summa += "GBG"
    for bg in range(x - rest):
        summa += "GB"   
print(summa)


    