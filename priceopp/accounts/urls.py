from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    
]