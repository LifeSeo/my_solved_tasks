from django.shortcuts import render
from .models import Articles

def news_home(request):
    news = Articles.objects.order_by('date')[:3]
    return render(request, 'news/news.html', {'news' :news})