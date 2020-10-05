from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView
)
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm

login = LoginView.as_view(template_name="accounts/login_form.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, '회원가입 환영합니다.')
            signed_user.send_welcome_email() 
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })