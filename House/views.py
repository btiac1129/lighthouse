from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HouseCreationForm
from Town.models import Town
from .models import House

def house_new(request, town_pk):
    if request.method == 'POST':
        form = HouseCreationForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)
            house.town = Town.objects.filter(pk=town_pk)[0]
            house.builder = request.user
            house.town_name = house.town.name
            form.save()
            messages.success(request, '하우스를 시작했습니다.')
            return redirect('/')
    else:
        form = HouseCreationForm()
    return render(request, 'House/house_form.html', {
        'form': form,
    })
