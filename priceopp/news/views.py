from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator

def news_home(request):
    news = Articles.objects.order_by('date')[:3]
    return render(request, 'news/news.html', {'news' :news})

class NewsDetailsView(DetailView):
    model = Articles
    template_name = 'news/detail_name.html'
    context_object_name = 'article'
    
class Search(ListView):
    model = Articles
    paginate_by = 2
    template_name = 'news/search.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if not query :
            query = ""
        object_list = Articles.objects.filter(
            Q(title__icontains=query) | Q(full_article__icontains=query)
        )
        return object_list
    

