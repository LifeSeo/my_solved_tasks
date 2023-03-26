from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from captcha.fields import CaptchaField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=2000, help_text='Required')
    captcha = CaptchaField(label='Are you an human? ')
    
  
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')