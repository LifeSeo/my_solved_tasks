print('Задача 1. Конвертация')


# При покупках за рубежом 
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например, 
# если купить что-то в евро, 
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
# 
# Напишите программу, 
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
# 
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

purchase_euro = float(input("Введите сумму покупки в евро: "))
ratio = (1.25 - 1) * 100
print("Разница в % =", ratio) 

purchase_rubles = (purchase_euro + (((purchase_euro * ratio) / 100))) * 60.87

print("Сумма покупки в рублях =", round(purchase_rubles, 2))

print('Задача 2. Грубая математика')

# В одном аналитическом центре,
# где занимаются разного рода математическим анализом,
# работал практикант,
# который написал программу для расчёта некоторых функций.
# Правда, он в тот день очень устал
# и немного не так прочитал техническое задание 
# и функции теперь рассчитываются довольно грубо.
# 
# Вводится последовательность из N вещественных чисел.
# При этом положительные числа округляются вверх, отрицательные округляются вниз.
# 
# Напишите программу,
# которая выводит натуральный логарифм от числа,
# если оно положительное, и экспоненту в степени числа, если оно отрицательное
# или равно нулю.
# 
# Пример:
# 
# Введите кол-во чисел: 3
# Введите число: 1.3
# x = 2   log(x) = 0.6931471805599453
# 
# Введите число: -2.1
# x = -3   exp(x) = 0.049787068367863944
# 
# Введите число: -5.9
# x = -6   exp(x) = 0.0024787521766663585

from math import log
from math import exp
from math import ceil
from math import floor

amount_numbers = int(input("Введите количество чисел: "))

for i in range(amount_numbers):
    digit = float(input("Введите вещественое число: "))
    if digit > 0:
        print(f"Логарифм числа {digit} равен: {float(log(ceil(digit)))}")
        print("===========================")
    else:
        print(f"Экспонета числа {digit} равен: {float(exp(floor(digit)))} ")
        print("===========================")
        
print('Задача 3. Аналог Steam')

# Вы пишете программу-инсталлятор для компьютерной игры.
# Пока инсталлятор скачивает обновление,
# пользователю нужно показать сколько процентов уже скачалось,
# чтобы он мог решить пойти заварить чаю, или подождать у экрана компьютера.
# 
# Обновления игры всегда занимают разное количество мегабайт,
# да и скорость интернет-соединения у игроков разная.
# 
# Напишите программу,
# принимающую на вход размер файла обновления в мегабайтах
# и скорость интернет соединения в мегабайтах в секунду.
# 
# Для каждой секунды программа рассчитывает
# и выводит на экран сколько процентов от всего объема уже скачано,
# до тех пор пока не будет скачан весь объем.
# В конце программа должна показать сколько всего секунд заняло скачивание обновления.
# Обеспечьте контроль ввода.
# 
# Пример:
# 
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения? 27
# 
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

from math import ceil

file_download = int(input("Укажите размер файла для скачивания: "))
speed_internet = int(input("Какова скорость вашего соединения: "))
intermediate_result = 0


for i in range(ceil(file_download / speed_internet)+1):
    print(f"Прошло {i} сек. Скачано {intermediate_result} из {file_download} Мб {(intermediate_result / file_download) * 100} %")
    intermediate_result += speed_internet
    if intermediate_result > file_download:
        intermediate_result = file_download
     
print('Задача 4. Первая цифра')

# Дано положительное действительное число X. 
# Выведите его первую цифру после десятичной точки. 
# При решении этой задачи нельзя пользоваться условной инструкцией,
# циклом или строками


number = float(input("Введите действительное число больше нуля: "))

while number < 0:
  number = float(input("Не верно. Введите действительное число больше нуля: "))

print(f"Первая цифра после десятичной точки: {int((number % 1)*10)}")

print('Задача 5. Вот это объёмы!')

# Для курсовой работы по физике
# Андрею нужно сравнить объёмы двух планет: Земли и какой-нибудь случайной,
# которая может в теории существовать в нашей вселенной.
# Андрей хорошо разбирается в формулах,
# а вот считать что-то, а уж тем более самому - это явно не его.
# Объём Земли ему известен заранее  - это 10.8321 * 10 ** 11 км3
# 
# А вот объём случайной планеты ему нужно будет посчитать.
# Благо, у него есть формула
# 
# V = 4/3 πR ** 3
# 
# где V - это объём, π - число пи, а R - радиус планеты.
# 
# Напишите программу, 
# которая получает на вход радиус случайной планеты
# и выводит на экран во сколько раз планета Земля меньше или больше по объёму.
# Ответ округлите до трёх знаков после запятой
 
# Пример:
# Введите радиус случайной планеты: 3389.5
# Объём планеты Земля больше в 6.641 раз

# Пример 2:
# Введите радиус случайной планеты: 7000
# Объём планеты Земля меньше в (1/0.754) = 1.326 раз

from math import pi

earht_volume = 10.8321 * 10**11
print("Обьем планеты Земля =", earht_volume)
radius_planet = float(input("Введите радиус случайной планеты: "))

while radius_planet < 0:
  radius_planet = float(
    input("Не верное значение. Введите радиус случайной планеты: "))

planet_volume = 4 / 3 * pi * radius_planet**3

if planet_volume > earht_volume:
  print(
    f"Масса планеты Земля меньше в: {round(planet_volume / earht_volume, 3)} раз(а)"
  )
else:
  print(
f"Масса планеты Земля больше в: {round(earht_volume / planet_volume, 3)} раз(а)")

print('Задача 6. Ход конём')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

x_hourse = float(input("Расположение по горизонтале: "))
y_hourse = float(input("Расположение по вертикале: "))

x_desk = float(input("Расположение по горизонтале: "))
y_desk = float(input("Расположение по вертикале: "))

x_hourse_point = int(x_hourse * 10)
y_hourse_point = int(y_hourse * 10)

x_desk_point = int(x_desk * 10)
y_desk_point = int(y_desk * 10)

print(f"Конь находится в координатах({x_hourse_point}, {y_hourse_point})")
print(f"Точка на доске({x_desk_point}, {y_desk_point})")

if abs(x_hourse_point - x_desk_point) == 2 and abs(y_hourse_point - y_desk_point) == 1:
    print("Можно выполнить ход конем")
else:
    print("Нельзя выполнить ход конем")
    
print('Задача 7. За что?')

# Вы встретились со своим старым другом,
# который тоже изучает программирование, правда, в другом учебном заведении.
# За чашкой кофе он пожаловался вам,
# что сумасбродный препод дал им задание написать программу,
# которая из двух введённых чисел определяет наибольшее,
# не используя при этом условные операторы, циклы и встроенные
# функции вроде max/min/sorted.
# 
# Радуясь, что на вашем курсе такого не требуют,
# вы всё-таки решаете помочь своему другу.
# 
# Напишите для него эту программу.
# 
# Пример:
# 
# Введите первое число: 10
# Введите второе число: 5
# 
# Наибольшее число: 10

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print('Наибольшее число:', (a // b * a + b // a * b) // (a // b + b // a))
