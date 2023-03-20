from django.urls import path
from . import views

urlpatterns = [
    path('info', views.index, name='info'),
    path('', views.weather, name='home'),
    path('about', views.about, name='about'),
    
]