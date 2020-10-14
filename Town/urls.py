from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views

app_name = 'Town'

urlpatterns = [
    path('', views.town_list, name='town_list'),
    path('new/', views.town_new, name='town_new'),
    path('mytown/', views.my_town, name='my_town'),
    path('<int:town_pk>/houses', views.town_houses, name='town_houses'),
]