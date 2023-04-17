from django.contrib.syndication.views import Feed  
from django.template.defaultfilters import truncatewords  
from .models import Articles 
from django.urls import reverse
  
class LatestPostsFeed(Feed):  
    title = 'New offers'  
    link = '/news/'  
    description = 'New posts offers.'
    
    def items(self):  
        return Articles.objects.all()[:5]  
      
    def item_title(self, item):  
        return item.title  
      
    def item_description(self, item):  
        return truncatewords(item.anons, 30)
    
    def item_link(self, item):
        return f'/news/{item.pk}'
