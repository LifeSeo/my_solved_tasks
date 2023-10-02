print("Система расчёта штрафов")

car_speed = int(input("Введите скорость транспорта: "))

fine_for_1_to_10_town = 30
fine_for_11_to_15_town = 50
fine_for_16_to_20_town = 70
fine_for_21_to_25_town = 115
fine_for_26_to_30_town = 180
fine_for_31_to_40_town = 260
fine_for_41_to_50_town = 400
fine_for_51_to_60_town = 560
fine_for_61_to_70_town = 700
fine_for_71_and_more_town = 800

fine_for_1_to_10_country = 20
fine_for_11_to_15_country = 40
fine_for_16_to_20_country = 60
fine_for_21_to_25_country = 100
fine_for_26_to_30_country = 150
fine_for_31_to_40_country = 200
fine_for_41_to_50_country = 320
fine_for_51_to_60_country = 480
fine_for_61_to_70_country = 600
fine_for_71_and_more_country = 700

town_speed = 50
country_speed = 70

over_speed_town = car_speed - town_speed
over_speed_country = car_speed - country_speed

while car_speed < 0 or car_speed > 500:
    car_speed = int(input("Скорость не может быть отрицательной или такой большой. "
                          "Введите скорость транспорта заного: "))
    
def test_zero_speed(car_speed):
    if car_speed == 0:
        print("Вы стоите на месте, нажмите педаль газа!")

def speed_multa_town(over_speed_town):
    result_fine_town = 0
    if over_speed_town <= 0:
        result_fine_town = 0
    elif over_speed_town >= 1 and over_speed_town <= 10:
        result_fine_town = fine_for_1_to_10_town
    elif over_speed_town >= 11 and over_speed_town <= 15:
        result_fine_town = fine_for_11_to_15_town
    elif over_speed_town >= 16 and over_speed_town <= 20:
        result_fine_town = fine_for_16_to_20_town
    elif over_speed_town >= 21 and over_speed_town <= 25:
        result_fine_town = fine_for_21_to_25_town
    elif over_speed_town >= 26 and over_speed_town <= 30:
        result_fine_town = fine_for_26_to_30_town
    elif over_speed_town >= 31 and over_speed_town <= 40:
        result_fine_town = fine_for_31_to_40_town
    elif over_speed_town >= 41 and over_speed_town <= 50:
        result_fine_town = fine_for_41_to_50_town
    elif over_speed_town >= 51 and over_speed_town <= 60:
        result_fine_town = fine_for_51_to_60_town
    elif over_speed_town >= 61 and over_speed_town <= 70:
        result_fine_town = fine_for_61_to_70_town
    elif over_speed_town == 0:
        print("Вы стоите на месте, нажмите педаль газа!")
    else:
        result_fine_town = fine_for_71_and_more_town
    return result_fine_town

def speed_multa_town_country(over_speed_country):
    result_fine_country = 0
    if over_speed_country <= 0:
        result_fine_country = 0
    elif over_speed_country >= 1 and over_speed_country <= 10:
        result_fine_country = fine_for_1_to_10_country
    elif over_speed_country >= 11 and over_speed_country <=15:
        result_fine_country = fine_for_11_to_15_country
    elif over_speed_country >= 16 and over_speed_country <= 20:
        result_fine_country = fine_for_16_to_20_country
    elif over_speed_country >= 21 and over_speed_country <= 25:
        result_fine_country = fine_for_21_to_25_country
    elif over_speed_country >= 26 and over_speed_country <= 30:
        result_fine_country = fine_for_26_to_30_country
    elif over_speed_country >= 31 and over_speed_country <= 40:
        result_fine_country = fine_for_31_to_40_country
    elif over_speed_country >= 41 and over_speed_country <= 50:
        result_fine_country = fine_for_41_to_50_country
    elif over_speed_country >= 51 and over_speed_country <= 60:
        result_fine_country = fine_for_51_to_60_country
    elif over_speed_country >= 61 and over_speed_country <= 70:
        result_fine_country = fine_for_61_to_70_country
    else:
        result_fine_country = fine_for_71_and_more_country
    return result_fine_country
    
multa_city = speed_multa_town(over_speed_town)
print("В городе штраф составит:", multa_city)
multa_country_speed = speed_multa_town_country(over_speed_country)
print("В пригороде штраф составит:", multa_country_speed)
test_zero_speed(car_speed)


        
    