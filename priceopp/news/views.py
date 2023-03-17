from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView

def news_home(request):
    news = Articles.objects.order_by('date')[:3]
    return render(request, 'news/news.html', {'news' :news})

class NewsDetailsView(DetailView):
    model = Articles
    template_name = 'news/detail_name.html'
    context_object_name = 'article'