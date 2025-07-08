from django.urls import path, include
from .views import *
from . import views

app_name = 'favorites'

urlpatterns = [
    path('songs/', views.songs_list, name='songs_list'),
    path('singers/', views.singer_list, name='singer_list'),
    ]