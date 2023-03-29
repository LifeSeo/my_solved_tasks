from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
            except BadHeaderError:
                return render(request, 'sent_email_missing.html')
            return render(request, 'sent_email.html')
    else:
        return render(request, 'sent_email_bad_way.html')
    return render(request, 'email.html', {'form': form})

