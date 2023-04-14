from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, UserCreationForm, UserEditForm, ProfileEditForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from django.db.models import Q

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/acc_active_email.html', {
                'user':user, 
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            rendered = render_to_string('accounts/confirm.html')
            return HttpResponse(rendered)
        
    
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        rendered = render_to_string('accounts/activation.html')
        return HttpResponse(rendered)
    else:
        rendered = render_to_string('accounts/activation_invalid.html')
        return HttpResponse(rendered)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request,
                      'accounts/edit_ready.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'accounts/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
@login_required       
def get_user_profile(request, username=None):
    if User.objects.filter(username=username):
        user = User.objects.get(username=username)
        avatar = request.user.profile.avatar
        description = user.profile.description
        telegramm = user.profile.telegramm
        
        fields = {
            'user':user,
            'avatar':avatar,
            'description':description,
            'telegramm':telegramm
        }
        
        context = {'fields':fields}
        
        return render(request, 'registration/user_profile.html', context)
        
    else:
        return render(request, 'registration/not_exist.html')
    
      
class SearchProfile(ListView):
    model = Profile
    paginate_by = 1000
    template_name = 'accounts/profile.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query :
            query = ""
        object_list = Profile.objects.filter(
            Q(description__icontains=query) |
            Q(user__username__icontains=query) |
            Q(avatar__icontains=query)).order_by('-id').distinct()
        
        return object_list

