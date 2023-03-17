from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news'),
    path('<int:pk>', views.NewsDetailsView.as_view(), name='news-detail')
]