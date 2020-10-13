from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TownCreationForm
from .models import Town

def town_list(request):
    town_list = Town.objects.all()
    return render(request, 'Town/town_list.html', {
        'town_list': town_list,
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