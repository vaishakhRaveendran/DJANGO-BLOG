#we have to map the functions to the urls.

from . import views
from django.urls import path

urlpatterns = [
    path("", views.home,name='blog-home'),
]