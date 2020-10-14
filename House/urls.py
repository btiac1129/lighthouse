from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'House'

urlpatterns = [
    re_path(r'^town/(?P<town_pk>\d+)/house/new/', views.house_new, name='house_new'),
    # path('town_no<int:pk>/new/', views.house_new, name='house_new'),
]
