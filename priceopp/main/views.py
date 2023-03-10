from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'values': ['TV', 'microwave','refrig','telefon','caps','water']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return HttpResponse('<h4>Тест - О нас</h4>')
