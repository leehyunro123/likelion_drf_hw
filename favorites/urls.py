from django.urls import path, include
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'favorites'

urlpatterns = [
    path('songs/', views.songs_list, name='songs_list'),
    path('singers/', views.singer_list, name='singer_list'),
    path('singers/<int:singer_id>/', views.singer_detail, name='singer_detail'),
    path('tags/<str:tags_name>/', views.find_tag, name='find_tag'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)