# Дано целое число n. Требуется вывести все правильные скобочные
# последовательности длины 2 ⋅ n, упорядоченные лексикографически 
# В задаче используются только круглые скобки.

from random import shuffle
import random
from itertools import *

n = int(input("Введите целое число: "))

rnd_bracket = ['(', ")"] * n

def generate_all_bracket(rnd_bracket):
    for i in permutations(rnd_bracket):
        if (i[0] != ")" and i[-1] != "("):
            data = "".join(i)
            lst = open("Yandex_bracket_sequence\list.txt", "a")
            lst.write(data)
            lst.write("\n")
            lst.close()
    return lst

    
def check_bracket():
    
    with open("Yandex_bracket_sequence\list.txt", "r") as file_first:
        with open("Yandex_bracket_sequence\list_2.txt", "a+") as second_file:
            stroka = " "
            while stroka != "":
                balance_1 = 0
                balance_2 = 0
                stroka = file_first.readline()
                if ")" in stroka: balance_1 += 1
                if "(" in stroka: balance_2 += 1
                if balance_1 == balance_2:
                    second_file.write(stroka)
            return second_file

def finall_check():       
    with open("Yandex_bracket_sequence\list_2.txt", "r") as second_file:
        with open("Yandex_bracket_sequence\list_3.txt", "a+") as third_file:
            lines = second_file.readlines()
            file = []
            for line in lines:
                if line not in file:
                    file.append(line)
            third_file.writelines(file)
    return third_file
    

generate_all_bracket(rnd_bracket)
check_bracket()
finall_check()

# print(generate_bracket(rnd_bracket))
# print(*check_bracket(generate_bracket, rnd_bracket))
        
        

 
 