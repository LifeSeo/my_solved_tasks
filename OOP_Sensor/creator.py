from user_interface import temperatura_view
from user_interface import preasure_view
from user_interface import wind_speed_view

def creator(device = 1):
    data = open("OOP_Sensor\parametors.html", "w", encoding="utf8")
    data.write(f"Температура: {temperatura_view(device)}\n")
    data.write(f"Давление: {preasure_view(device)}\n")
    data.write(f"Скорость ветра: {wind_speed_view(device)}")
        
    return data