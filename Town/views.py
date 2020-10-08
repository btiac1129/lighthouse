from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Town

def town_list(request):
    town_list = Town.objects.all()
    return render(request, 'Town/town_list.html', {
        'town_list': town_list,
    })