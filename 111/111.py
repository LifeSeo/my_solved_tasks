# Задать рандомно список, написать метод пузырьковой сортировки
# сделать многопоточность.

from random import randint
import time
import multiprocessing

size = 1000
list = []

for i in range(size):
    if i < size:
        list.append(randint(1, 99))
print("Выводим первоначальный список на печать:", list)

start_measurement_1 = time.perf_counter()

def sorting_bubble(list):
    for j in range(len(list)):
        for k in range(len(list) - 1):
            if list[k] > list[k +1]:
                list[k], list[k + 1] = list[k +1], list[k]
              
end_measurement_1 = time.perf_counter()    

start_measurement_2 = time.perf_counter()

def sorting_bubble_with_multiprocessing(list):
    for j in range(len(list)):
        for k in range(len(list) - 1):
            if list[k] > list[k +1]:
                list[k], list[k + 1] = list[k +1], list[k]

start_measurement_2 = time.perf_counter()
              
if __name__ == __name__:
    multi_processing = multiprocessing.Process(target=sorting_bubble_with_multiprocessing
                                               , args=list)
    multi_processing.start()
    multi_processing.join()
              
end_measurement_2 = time.perf_counter()
           
sorting_bubble(list)
print("Пузырьковый метод сортировки", list)
measurement = print("Время выполнения в 1 поток:",
                    end_measurement_1 - start_measurement_1)
sorting_bubble_with_multiprocessing(list)
print("Пузырьковый метод сортировки", list)
measurement = print("Время выполнения в мультипоток:",
                    end_measurement_2 - start_measurement_2)
