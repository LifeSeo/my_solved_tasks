from django.urls import path
from . import views

urlpatterns = [
    # path('weather', views.weather, name='weather_add'),
    path('', views.weather, name='home'),
    path('about', views.about, name='about'),
    
]