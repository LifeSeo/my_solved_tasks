from django.shortcuts import render
from django.http import HttpResponse
import requests
def weather(request):
    city = "Москва"
    apid = '50cc6f11287d4646c4903108ba4f2c52'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + apid
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
    headers = {'User-Agent': user_agent}
    # city = 'Moscow'
    res = requests.get(url.format(city), headers=headers).json()
    
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    
    contex = {'info': city_info}
    
    return render(request, 'main/index.html', contex)

def index(request):
    data = {
        'values': ['TV', 'microwave','refrig','telefon','caps','water']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return HttpResponse('<h4>Тест - О нас</h4>')

