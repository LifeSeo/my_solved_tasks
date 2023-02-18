import data_provider as dp
import log

def temperatura_view(sensor):
    data = dp.get_temperatura(sensor)
    log.temperatura_log(data)
    return data

def preasure_view(sensor):
    data = dp.get_preasure(sensor)
    log.preasure_log(data)
    return data

def wind_speed_view(sensor):
    data = dp.get_wind_speed(sensor)
    log.wind_speed_log(data)
    return data