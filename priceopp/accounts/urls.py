from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'), name='password_reset_complete'),
    path(r'captcha/', include('captcha.urls')),
    path('edit/', views.edit, name='edit'),
]