from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from news.sitemaps import StaticViewSitemap, DynamicViewSitemap, ProfileViewSitemap, SearchViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from news.feeds import LatestPostsFeed 

sitemaps = {
    'static': StaticViewSitemap,
    'dynamic': DynamicViewSitemap,
    'profile': ProfileViewSitemap,
    'search' : SearchViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    path('reviews/', include('reviews.urls')),
    path('sendemail/', include('sendemail.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('rating/', include('rating.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('feed/', LatestPostsFeed(), name='post_feed'), 
    path('robots.txt' , include('robots.urls')),
    path('ysearch/', include('ysearch.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
