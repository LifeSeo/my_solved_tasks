from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import location

def index(request):
    data = {
        'values': ['TV', 'microwave','refrig','telefon','caps','water']
    }
    return render(request, 'main/index.html', data)