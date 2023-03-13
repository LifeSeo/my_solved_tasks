from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('review_add', views.review_add, name='review_add'),
]