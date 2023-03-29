from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Name', max_length=50)
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Question', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)