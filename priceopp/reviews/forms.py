from .models import Reviews
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'review', 'date']
        
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            "review": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your review here'
                }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter date, (example: 15.02.1999)'
                })
        }