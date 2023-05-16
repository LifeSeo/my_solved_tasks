from django.contrib.sitemaps import Sitemap
from .models import Articles
from accounts.models import Profile
from django.shortcuts import reverse
import os


class StaticViewSitemap(Sitemap):
    
    changefreq = 'monthly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return ['news', 'search']

    def location(self, item):
        return reverse(item)
    
    
class DynamicViewSitemap(Sitemap):
    
    changefreq = 'monthly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return Articles.objects.all()

    def location(self, item):
        # return reverse('news-page', args=[item.pk])
        return f'/news/{item.pk}'
    
class ProfileViewSitemap(Sitemap):
    
    changefreq = 'monthly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return Profile.objects.all()

    def location(self, item):
        # return reverse('news-page', args=[item.pk])
        return f'/accounts/profile/{item.user}/'
    
class SearchViewSitemap(Sitemap):
    
    changefreq = 'monthly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return os.listdir('ysearch/search/')

    def location(self, item):
        return f'/ysearch/search/{item}'