from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from House.models import House
from .forms import TownCreationForm
from .models import Town


def town_list(request):
    town_list = Town.objects.all()
    return render(request, 'Town/town_list.html', {
        'town_list': town_list,
    })

def my_town(request):
    user = request.user
    my_town = user.town_set.all()
    return render(request, 'Town/my_town.html', {
        'my_town': my_town,
    })

def town_new(request):
    if request.method == 'POST':
        form = TownCreationForm(request.POST, request.FILES)
        if form.is_valid():
            town = form.save(commit=False)
            town.operator = request.user
            town.save()
            messages.success(request, '타운을 만들었습니다.')
            return redirect('town_list')
    else:
        form = TownCreationForm()
    return render(request, 'Town/town_form.html', {
        'form': form,
    })

def town_houses(request, town_pk):
    town = Town.objects.filter(pk=town_pk)[0]
    houses_of_town = House.objects.filter(town_id=town_pk)
    return render(request, 'Town/town_houses.html', {
        'town' : town,
        'houses_of_town': houses_of_town,
    })

