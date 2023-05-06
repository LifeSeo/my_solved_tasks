from django import forms

class UserForm(forms.Form):
    url = forms.CharField(max_length=300)