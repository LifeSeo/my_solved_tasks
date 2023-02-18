from datetime import datetime
from time import time

def temperatura_log(data):
    time = datetime.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write(f"Время: {time} Температура: {data}")
        
def preasure_log(data):
    time = datetime.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write(f"Время: {time} Давление: {data}")
        
def wind_speed_log(data):
    time = datetime.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write(f"Время: {time} Скорость ветра: {data}")