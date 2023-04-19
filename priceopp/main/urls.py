from django.urls import path, include
from . import views

urlpatterns = [
    path('info', views.index, name='info'),
    path('', views.weather, name='home'),
    path('about', views.about, name='about'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('i18n/', include('django.conf.urls.i18n')),
    
]