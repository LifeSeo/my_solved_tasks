from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from captcha.fields import CaptchaField
from .models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=2000, help_text='Required')
    captcha = CaptchaField(label='Are you an human? ')
    
  
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'data_of_birth',  'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'telegramm', 'description')
        