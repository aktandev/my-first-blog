from django.urls import path

from . import views

path('', views.post_list, name='post_list')
