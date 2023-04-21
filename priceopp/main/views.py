from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from . import location
from django.utils import translation
from django.conf import settings
from accounts.models import Profile


def index(request):
    data = {
        'value': ['TV', 'microwave','refrig','telefon','caps','water']
    }
    return render(request, 'main/info.html', data)

def weather(request):
    object = location.Location()
    city = object.get_location() 
    apid = '50cc6f11287d4646c4903108ba4f2c52'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + apid
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
    headers = {'User-Agent': user_agent}
    res = requests.get(url.format(city), headers=headers).json()
    
    city_info = {
        'city': city,
        'temp': round(res["main"]["temp"]),
        'icon': res["weather"][0]["icon"],
        'values': ['TV', 'microwave','refrig','telefon','caps','water']
    }
    
    contex = {'info': city_info}
    
    return render(request, 'main/index.html', contex)

def about(request):
    return HttpResponse('<h4>Тест - О нас</h4>')


def subscribe(request):
    pass
    return render(request, 'main/subscribe.html',)

def set_language_from_url(request, user_language):
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

user_language = 'fr'  # example
translation.activate(user_language)

# persist using the cookie
response = HttpResponse(...)
response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

def status(request):
    template_name = 'main/subscribe.html'
    status = Profile.objects.all()
    context={'status':status}
    return render(request,template_name,context)
