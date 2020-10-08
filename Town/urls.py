from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.town_list, name='town_list'),
]