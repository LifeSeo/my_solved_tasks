from random import randint as rnd

def get_temperatura(sensor):
    return rnd(-20, 0) if sensor else rnd(0, 20)

def get_preasure(sensor):
    return rnd(720, 750) if sensor else rnd(750, 770)

def get_wind_speed(sensor):
    return rnd(0, 25) if sensor else rnd(25, 55)